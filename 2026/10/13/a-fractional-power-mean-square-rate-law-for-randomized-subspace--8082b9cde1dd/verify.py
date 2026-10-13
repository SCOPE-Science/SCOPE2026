"""Exact finite-step identities and spectral checks for a coordinate-sketch accelerated quadratic."""
from fractions import Fraction as F
from itertools import product
import numpy as np


def state_matrices(d, t):
    th = t / d
    k0 = ((1 / (1 + th), th / (1 + th)),
          (th / (1 + th), 1 / (1 + th)))
    k1 = (((1 - t*t) / (1 + th), (1 - t*t)*th / (1 + th)),
          (-(d-1)*th / (1+th), 1-th-(d-1)*th*th/(1+th)))
    return k0,k1


def moment(k):
    (a,b),(c,e)=k
    return ((a*a,2*a*b,b*b),
            (a*c,a*e+b*c,b*e),
            (c*c,2*c*e,e*e))


def apply3(mat,v):
    return tuple(sum(a*b for a,b in zip(row,v)) for row in mat)


def transfer(d,t):
    k0,k1=state_matrices(d,t)
    s0,s1=moment(k0),moment(k1)
    return tuple(tuple(((d-1)*s0[i][j]+s1[i][j])/d for j in range(3)) for i in range(3))


count=0
for d in (2,3,4,7):
    for t in (F(1,2),F(1,7),F(1,23)):
        k0,k1=state_matrices(F(d),t)
        m=transfer(F(d),t)
        for q in (F(0),F(1),F(-2,3)):
            init=(F(1),q,q*q)
            for s in (k0,k1):
                a=s[0][0]+q*s[0][1]
                b=s[1][0]+q*s[1][1]
                assert apply3(moment(s),init)==(a*a,a*b,b*b)
                count+=1
            weighted=tuple(((d-1)*x+y)/d for x,y in zip(apply3(moment(k0),init),apply3(moment(k1),init)))
            assert apply3(m,init)==weighted
            count+=1
        for steps in range(1,6):
            initial=(F(1),F(1))
            w=(F(1),F(1),F(1))
            for _ in range(steps):
                w=apply3(m,w)
            direct=[F(0),F(0),F(0)]
            for seq in product((0,1),repeat=steps):
                a,b=initial
                prob=F(1)
                for j in seq:
                    k=(k0,k1)[j]
                    a,b=k[0][0]*a+k[0][1]*b,k[1][0]*a+k[1][1]*b
                    prob*=F(1,d) if j else F(d-1,d)
                for i,v in enumerate((a*a,a*b,b*b)):
                    direct[i]+=prob*v
            assert tuple(direct)==w
            count+=1

# The symbolic cubic coefficient is established by the displayed matrix expansion
# in the accompanying proof; this checker tests finite exact identities and
# numerical roots independently of that argument.

checks=0
for dim in (2,3,5,9):
    for tval in (0.003,0.001,0.0005):
        m=np.array(transfer(dim,tval),dtype=float)
        ev=np.linalg.eigvals(m)
        roots=sorted(ev,key=lambda v:abs(v),reverse=True)
        r=float(abs(roots[0]))
        assert abs(roots[0].imag)<1e-7
        assert r<1-tval/dim
        c=(2*(dim-1)/dim**4)**(1/3)
        approx=1-2*tval/dim+c*tval**(4/3)
        relative=abs(r-approx)/(c*tval**(4/3))
        assert relative<0.2,(dim,tval,relative)
        assert r>abs(roots[1]) and r>abs(roots[2])
        checks+=1
print(f'VERIFY_OK exact_finite_identities={count} spectral_cases={checks}')
