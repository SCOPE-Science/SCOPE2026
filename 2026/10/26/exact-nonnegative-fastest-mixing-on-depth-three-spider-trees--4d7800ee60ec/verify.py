"""Reproduce the exact and numerical checks for length-three spider mixing.
Run with Python 3 and packages numpy and sympy.
"""
import math
import numpy as np
import sympy as sp


def parameters(k):
    assert isinstance(k, int) and k >= 3
    g = 2 / (3*k + 5 + math.sqrt((3*k + 5)**2 - 24*k))
    return (1/k, (2-g)/3, (1+g)/3, g)


def blocks(k, x, y, z):
    B = np.array([[x+y, -y, 0], [-y,y+z,-z], [0,-z,z]],dtype=float)
    R = np.array([[k*x,-math.sqrt(k)*x,0,0],
                  [-math.sqrt(k)*x,x+y,-y,0],
                  [0,-y,y+z,-z],
                  [0,0,-z,z]],dtype=float)
    return B,R


def full_laplacian(k,x,y,z):
    L = np.zeros((3*k+1,3*k+1),dtype=float)
    for j in range(k):
        for a,b,w in ((0,1+3*j,x),(1+3*j,2+3*j,y),(2+3*j,3+3*j,z)):
            L[a,a] += w;L[b,b] += w;L[a,b] -= w;L[b,a] -= w
    return L


def exact_identities():
    x,g,t=sp.symbols('x g t',real=True)
    F=6*g**2-(5*x+3)*g+x
    y,z=(2-g)/3,(1+g)/3
    a=(1-5*g)/(3*g)
    v=sp.Matrix([a,a+1,a+2])
    B=sp.Matrix([[x+y,-y,0],[-y,y+z,-z],[0,-z,z]])
    assert all(sp.cancel(z0).subs(x,(3*g-6*g*g)/(1-5*g)).cancel()==0 for z0 in B*v-g*v)
    # Root relation reduces the radial characteristic polynomial.
    f0=t-1
    f1=(t-x-y)*f0-x
    f2=(t-y-z)*f1-y*y*f0
    f3=(t-z)*f2-z*z*f1
    target=t*(t-1-g)*(t**2-(2+x-g)*t+(3+x)*(2-g)/9)
    assert sp.rem(sp.together(f3-target).expand(),F,g).simplify()==0
    q=(2-g)**2-(2+x-g)*(2-g)+(3+x)*(2-g)/9
    assert sp.simplify(q-(2-g)*(3-8*x)/9)==0
    assert sp.simplify((B-g*sp.eye(3)).det()-(2-g)*F/9)==0  # det(B-gI)
    # Direct Rayleigh certificate: root vector gives the bound.
    numerator = sp.fraction(sp.cancel(x*a*a+1-g*sum(z0*z0 for z0 in v)))[0]
    assert sp.rem(numerator,F,g).simplify()==0
    return 5


def finite_checks():
    full=0; spectra=0; random_trials=0
    rng=np.random.default_rng(4351)
    for k in range(3,31):
        x,y,z,g=parameters(k)
        assert abs(6*g*g-(3+5*x)*g+x)<1e-12
        assert x > 0 and y > 0 and z > 0
        assert k*x <= 1+1e-12 and x+y <=1+1e-12 and y+z <=1+1e-12
        B,R=blocks(k,x,y,z)
        eb=np.linalg.eigvalsh(B); er=np.linalg.eigvalsh(R)
        assert abs(eb[0]-g)<1e-12
        assert er[1]>g and max(er[-1],eb[-1]) < 2-g+1e-12
        spectra+=1
        if k<=14:
            L=full_laplacian(k,x,y,z)
            w=np.linalg.eigvalsh(L)
            assert abs(w[1]-g)<1e-12
            assert abs(max(abs(1-w[1]),abs(1-w[-1]))-(1-g))<1e-12
            assert abs(w[-1]-max(er[-1],eb[-1]))<1e-12
            full+=1
        # Check deterministic pseudorandom admissible competitors in the reduced blocks.
        for _ in range(100):
            xx=rng.random()/k
            yy=rng.random()*min(1-xx,1)
            zz=rng.random()*(1-yy)
            b,r=blocks(k,xx,yy,zz)
            objective=max(1-np.linalg.eigvalsh(b)[0],
                          np.linalg.eigvalsh(r)[-1]-1)
            assert objective > 1-g-1e-10
            random_trials+=1
    return spectra,full,random_trials

if __name__=='__main__':
    ids=exact_identities()
    spectra,full,trials=finite_checks()
    print(f'VERIFY_OK symbolic_identities={ids} reduced_spectra={spectra} full_laplacians={full} feasibility_trials={trials}')
    for k in (3,4,5,10,20):
        x,y,z,g=parameters(k)
        print(f'k={k} x={x:.15g} y={y:.15g} z={z:.15g} gap={g:.15g} SLEM={1-g:.15g}')
