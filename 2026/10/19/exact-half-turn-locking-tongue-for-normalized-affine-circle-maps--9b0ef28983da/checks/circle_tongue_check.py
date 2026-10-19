"""Supplementary symbolic and numerical diagnostics for the half-turn locking theorem.

Requires Python 3.10+ and SymPy. Finite testing supplements, but does not replace,
the analytic proof contained in RESULT.md.
"""
import cmath
import math
import sympy as sp


def circle_map(z, alpha, phase):
    numerator = alpha + phase*z
    return numerator / abs(numerator)


def cycles(alpha, theta):
    """One ordered representative (z,w) per admissible two-cycle, theta != pi."""
    phase = cmath.exp(1j*theta)
    sine = abs(math.sin(theta))
    cosine = -math.cos(theta)
    if cosine <= 0 or sine == 0:
        return []
    discriminant = (alpha*alpha + 4*sine*sine)**2 - 16*sine*sine
    if discriminant < -1e-13:
        return []
    roots = [(alpha*alpha+4*sine*sine+sgn*math.sqrt(max(discriminant,0)))/2
             for sgn in (-1,1)]
    result=[]
    for q in roots:
        if not (sine*sine - 1e-10 <= q < 1):
            continue
        p=1-q
        u=cosine + math.sqrt(max(q-sine*sine,0))
        v=cosine - math.sqrt(max(q-sine*sine,0))
        if min(u,v)<=0:
            continue
        z=alpha*(u+phase)/(p-phase*phase)
        w=alpha*(v+phase)/(p-phase*phase)
        multiplier=((u*u+1-alpha*alpha)*(v*v+1-alpha*alpha))/(4*p*p)
        result.append((q,z,w,multiplier))
    return result


q,s,A=sp.symbols('q s A', real=True)
p=1-q
Q=q*q-(A+4*s*s)*q+4*s*s
numerator=p*p+(1-A)*(2+2*q-4*s*s)+(1-A)**2
A_on_Q=(q*q+4*s*s*(1-q))/q
assert sp.simplify((numerator-4*p*p).subs(A,A_on_Q)
                   - 4*(1-q)*(q*q-4*s*s)*(q-s*s)/q**2)==0
assert sp.simplify(Q.subs(q,2*s) - 2*s*(4*s*(1-s)-A))==0
assert sp.simplify(Q.subs(q,s*s) - s*s*(4-A-3*s*s))==0
assert sp.simplify(((A+4*s*s)**2-16*s*s) - \
       (A-4*s*(1-s))*(A+4*s*(1+s))) == 0

checks=0
for alpha in (.04,.2,.55,.8,.95):
    s_critical=(1-math.sqrt(1-alpha*alpha))/2
    for direction in (-1,1):
        for scale in (.025,.15,.65,.98,1.02,1.17):
            sine=s_critical*scale
            theta=math.pi + direction*math.asin(sine)
            phase=cmath.exp(1j*theta)
            pairs=cycles(alpha,theta)
            assert len(pairs)==(2 if scale<1 else 0), (alpha,scale,len(pairs))
            for q,z,w,lam in pairs:
                assert abs(abs(z)-1)<1e-10 and abs(abs(w)-1)<1e-10
                assert abs(circle_map(z,alpha,phase)-w)<1e-10
                assert abs(circle_map(w,alpha,phase)-z)<1e-10
                assert (lam>1)==(q>2*sine)
                predicted=(q*q-4*sine*sine)*(q-sine*sine)/((1-q)*q*q)
                assert abs(lam-1-predicted)<2e-8
                checks+=1
    # At theta=pi the source's two orbits reappear as an exact singular limit.
    phase=-1
    for z in (1+0j, complex(alpha/2, math.sqrt(1-alpha*alpha/4))):
        w=circle_map(z,alpha,phase)
        assert abs(circle_map(w,alpha,phase)-z)<1e-10
        assert abs(w-z)>1e-8
        checks+=1
print('Four exact symbolic identities passed, and',checks,
      'numeric orbit/multiplier checks passed.')
