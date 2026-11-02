"""Finite numerical diagnostics for a weighted two-moment Hardy-space inequality.

This program does not prove the continuum theorem; the proof is analytical.
Uses only the Python standard library.
"""
import cmath
import math
import random


def norms(values, weights, angle):
    z = [complex(v) * cmath.exp(-1j * angle) for v in values]
    x = [v.real for v in z]
    a = sum(w * math.sqrt(max(0.0, 1.0 + t)) for w, t in zip(weights, x))
    b = sum(w * math.sqrt(max(0.0, 1.0 - t)) for w, t in zip(weights, x))
    p = (a*a+b*b)/2.0
    var = sum(w*t*t for w,t in zip(weights,x))-(sum(w*t for w,t in zip(weights,x)))**2
    return p, var


def test():
    rng = random.Random(62951)
    checks=0
    for length in range(2,9):
        for _ in range(45):
            angles=[rng.uniform(-math.pi,math.pi) for _ in range(length)]
            vals=[cmath.exp(1j*t) for t in angles]
            unnormalized=[rng.uniform(0.01,1) for _ in range(length)]
            weights=[x/sum(unnormalized) for x in unnormalized]
            alpha=sum(w*z for w,z in zip(weights,vals))
            beta=sum(w*z*z for w,z in zip(weights,vals))
            S=1-abs(alpha)**2+abs(beta-alpha**2)
            if S<0 and S>-1e-11: S=0
            assert S>=-1e-11
            for j in range(48):
                angle=math.pi*j/24
                p,var=norms(vals,weights,angle)
                assert p<=1-var/4+2e-12,(length,p,var)
                x=[(z*cmath.exp(-1j*angle)).real for z in vals]
                var_formula=(1-abs(alpha)**2+(cmath.exp(-2j*angle)*(beta-alpha**2)).real)/2
                assert abs(var_formula-var)<3e-12
                if j==0: p_min=p
                else: p_min=min(p_min,p)
                checks+=2
            assert p_min<=1-S/8+0.015, (p_min,S) # grid may miss optimum
            checks+=1
    for d in [0.3,0.1,0.03,0.01,0.003]:
        vals=[cmath.exp(1j*d),cmath.exp(-1j*d)]
        weights=[0.5,0.5]
        best=min(norms(vals,weights,j*math.pi/8192)[0] for j in range(8192))
        exact=(1+math.cos(d))/2
        S=2*math.sin(d)**2
        assert abs(best-exact)<2e-11
        assert abs((1-exact)/S-1/(4*(1+math.cos(d))))<1e-9
        checks+=2
    print('PASS:',checks,'finite identity and inequality checks; sharpness approach verified.')


if __name__=='__main__':
    test()
