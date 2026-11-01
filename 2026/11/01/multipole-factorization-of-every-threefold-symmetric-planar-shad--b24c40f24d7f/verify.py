#!/usr/bin/env python3
"""Exact and numerical checks for the harmonic-cubic shadow-area factorization.
Requires Python >=3.10 and SymPy >=1.12; no network or external data.
Finite numerical tests illustrate, but do not replace, the proof.
"""
import math
import cmath
import itertools
import random
import sympy as S

x,y,z=S.symbols('x y z', real=True)
X=S.Matrix([x,y,z]); q=x*x+y*y+z*z


def vec(a): return S.Matrix(a)
def lap(P): return sum(S.diff(P,t,2) for t in [x,y,z])
def H_of(vs):
    L=S.prod((vec(v).dot(X)) for v in vs)
    return S.expand(L-q*lap(L)/10)
def eval3(P,m): return complex(S.N(P.subs({x:m[0],y:m[1],z:m[2]},simultaneous=True),17))
def prod_factor(vs,n):
    return math.prod(float(vec(v).dot(vec(v))) - float(sum(float(vec(v)[i])*n[i] for i in range(3)))**2 for v in vs)
def dot(a,b): return sum(a[i]*b[i] for i in range(3))
def norm(a): return math.sqrt(dot(a,a))
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def plane_basis(n):
    m=min([(abs(n[i]),i) for i in range(3)])[1]
    e=[int(j==m) for j in range(3)]
    a=cross(n,e); a=[v/norm(a) for v in a]
    b=cross(n,a); return a,b

def projected_area_by_fourier(P,p,v):
    # Extract Fourier coefficients independently, by uniform trapezoid rule.
    N=192
    hs=[]
    for j in range(N):
        th=2*math.pi*j/N
        u=[p[i]*math.cos(th)+v[i]*math.sin(th) for i in range(3)]
        hs.append(eval3(P,u).real)
    # Use exact frequency weights for h=1+P. Modes 1 and 3 are the only ones.
    c3=sum(hs[j]*cmath.exp(-6j*math.pi*j/N) for j in range(N))/N
    return math.pi-16*math.pi*abs(c3)**2


def verify():
    assert S.simplify(lap(H_of([(1,0,0),(0,1,0),(0,0,1)])))==0
    cases=[
        [(1,0,0),(0,1,0),(0,0,1)],
        [(0,0,1)]*3,
        [(1,0,0),(1,0,0),(0,1,0)],
        [(S.Rational(3,5),S.Rational(4,5),0),(0,S.Rational(5,13),S.Rational(12,13)),(S.Rational(8,17),0,S.Rational(15,17))],
    ]
    checks=0
    t=S.symbols('t',real=True)
    for vs in cases:
        P=H_of(vs)
        assert S.expand(lap(P))==0
        # The highest Fourier component on any great circle reads off P(p+iq)/8.
        for n in [(1.,0.,0.),(0.,1.,0.),(0.,0.,1.),(1/math.sqrt(3),)*3, (.24,.3,math.sqrt(1-.24**2-.3**2))]:
            a,b=plane_basis(n)
            m=[a[i]+1j*b[i] for i in range(3)]
            lhs=abs(eval3(P,m))**2
            rhs=prod_factor(vs,n)
            assert abs(lhs-rhs)<2e-9*(1+rhs), (vs,n,lhs,rhs)
            # Independent numerical area integral with sinusoidal Fourier extractor.
            if lhs<10:
                area_analytic=math.pi*(1-lhs/4)
                area_fourier=projected_area_by_fourier(P,a,b)
                assert abs(area_analytic-area_fourier)<2e-8, (vs,n,area_analytic,area_fourier)
            checks+=2
        # Verify full polynomial trace identity exactly (since harmonic projection term is q*linear).
        L=S.prod(vec(v).dot(X) for v in vs)
        assert S.expand(P-L+q*lap(L)/10)==0
        checks+=2
    # explicit binary-sextic formula: xyz maps to 2 i s t (s^4-t^4).
    s,t=S.symbols('s t')
    m=(s*s-t*t,S.I*(s*s+t*t),2*s*t)
    P0=x*y*z
    zz=S.factor(P0.subs({x:m[0],y:m[1],z:m[2]},simultaneous=True))
    assert S.expand(zz-2*S.I*s*t*(s**4-t**4))==0
    checks+=1
    # If all 3 multipoles align, the sextic has a triple antipodal pair.
    Pz=H_of([(0,0,1)]*3)
    fz=S.expand(Pz.subs({x:m[0],y:m[1],z:m[2]},simultaneous=True))
    assert S.expand(fz-8*s**3*t**3)==0
    checks+=1
    # Independently integrate the direct support-function area formula with
    # central finite differences, rather than extracting Fourier coefficient 3.
    eps=S.Rational(1,8)
    for vs in cases:
        P=H_of(vs)
        pf=S.lambdify((x,y,z),P,"math")
        for n in [(1.,0.,0.),(.24,.3,math.sqrt(1-.24**2-.3**2))]:
            a,b=plane_basis(n)
            N=2048
            dt=2*math.pi/N
            samples=[1+float(eps)*pf(*[a[i]*math.cos(j*dt)+b[i]*math.sin(j*dt) for i in range(3)]) for j in range(N)]
            area_direct=.5*dt*sum(samples[j]**2-((samples[(j+1)%N]-samples[j-1])/(2*dt))**2 for j in range(N))
            target=math.pi*(1-float(eps)**2*prod_factor(vs,n)/4)
            assert abs(area_direct-target)<1e-5, (vs,n,area_direct,target)
            checks+=1
    # Random normals and axes, including repeated axis pairs and intentionally nonorthogonal ones.
    rng=random.Random(161803)
    for i in range(1500):
        def unit():
            vv=[rng.gauss(0,1) for _ in range(3)]
            return [v/norm(vv) for v in vv]
        vs=cases[i%4]
        P=H_of(vs)
        n=unit()
        p,b=plane_basis(n)
        m=[p[j]+1j*b[j] for j in range(3)]
        lhs=abs(eval3(P,m))**2
        rhs=prod_factor(vs,n)
        assert abs(lhs-rhs)<4e-9*(1+abs(lhs)),(lhs,rhs)
        checks+=1
    print(f'PASS {checks} exact and deterministic finite geometric diagnostics')

if __name__=='__main__': verify()
