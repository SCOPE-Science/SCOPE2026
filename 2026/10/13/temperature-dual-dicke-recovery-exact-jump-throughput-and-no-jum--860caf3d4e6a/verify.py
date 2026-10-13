"""Reproduce exact combinatorial identities and selected full GAD-channel checks.

Dependencies: Python >=3.10 and NumPy. Finite tests corroborate, rather than
replace, the analytic statements in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb, sqrt
import numpy as np


def variance_coefficient(n, a, p):
    b = n-a
    q = 1-p
    vals = []
    for ell in range(n+1):
        weight = Fraction(comb(n, ell))*q**ell*p**(n-ell)
        # Mean count of A0-occupied plus B0-unoccupied sites at weight w.
        h_a = Fraction(a*ell+(n-a)*(n-ell), n)
        h_b = Fraction(b*ell+(n-b)*(n-ell), n)
        vals.append((weight, h_a-h_b))
    assert sum(w for w, _ in vals) == 1
    m = sum(w*x for w,x in vals)
    var = sum(w*(x-m)**2 for w,x in vals)
    return var/Fraction(8)


def hypergeom_amplitude(n, w, ell, gamma):
    ans = 0.0
    for t in range(max(0, w-(n-ell)), min(w,ell)+1):
        ex = n-ell-w+2*t
        ans += comb(ell,t)*comb(n-ell,w-t)/comb(n,w)*(1-gamma)**(ex/2)
    return ans


def nojump_overlap(n,a,p,gamma):
    b=n-a
    moments = []
    for u,v in [(a,a),(a,b),(b,b)]:
        moments.append(sum(comb(n,ell)*(1-p)**ell*p**(n-ell)*
            hypergeom_amplitude(n,u,ell,gamma)*hypergeom_amplitude(n,v,ell,gamma)
            for ell in range(n+1)))
    return moments[1]/sqrt(moments[0]*moments[2])


def full_channel(n,a,p,gamma):
    b=n-a; N=2**n
    def dicke(w):
        return np.array([(1/sqrt(comb(n,w))) if x.bit_count()==w else 0.0
                         for x in range(N)])
    V=np.stack([dicke(a),dicke(b)],axis=1)
    xi=sqrt(a*(b+1)/(b*(a+1)))
    s=lambda w:(1-p)*w+p*(n-w)
    smax=max(s(a),s(b))
    coeffs=[1-gamma*(smax-s(a))/2,1-gamma*(smax-s(b))/2]
    rec=[]
    for ws,fac in (([a,b],coeffs),([a-1,b-1],[1.0,xi]),([a+1,b+1],[xi,1.0])):
        R=np.vstack([fac[j]*dicke(ws[j]) for j in range(2)])
        rec.append(R)
    A0=sqrt(1-p)*np.diag([1,sqrt(1-gamma)])
    A1=sqrt((1-p)*gamma)*np.array([[0,1],[0,0]])
    B0=sqrt(p)*np.diag([sqrt(1-gamma),1])
    B1=sqrt(p*gamma)*np.array([[0,0],[1,0]])
    Kraus=[A0,A1,B0,B1]
    ps=0.0; ent_num=0.0
    for t in product(range(4), repeat=n):
        E=np.array([[1.0]])
        for j in t: E=np.kron(E,Kraus[j])
        EV=E@V
        for R in rec:
            K=R@EV
            ps+=np.sum(abs(K)**2)/2
            ent_num+=abs(np.trace(K))**2/4
    return ps,ent_num/ps


def main():
    checks=0
    for n in range(5,25):
        for a in range(1,(n-3)//2+1):
            b=n-a
            for p in (Fraction(0),Fraction(1,4),Fraction(2,5),Fraction(1,2),Fraction(3,4),Fraction(1)):
                target=Fraction((b-a)**2,2*n)*p*(1-p)
                assert variance_coefficient(n,a,p)==target
                assert Fraction(a*(b+1),n)==Fraction(b*(a+1),n)*Fraction(a*(b+1),b*(a+1))
                checks+=2
    for n,a in ((5,1),(7,2),(8,2),(11,3)):
        for p in (0.2,0.4,0.7):
            coeff=(n-2*a)**2*p*(1-p)/(2*n)
            g=0.002
            delta=(1-nojump_overlap(n,a,p,g))/g**2
            assert abs(delta-coeff)<0.035, (n,a,p,delta,coeff)
            checks+=1
        for p in (0.0,1.0):
            assert abs(nojump_overlap(n,a,p,0.25)-1)<1e-12
            checks+=1
    for n,a,p in ((5,1,0.3),(6,1,0.4)):
        b=n-a
        rate=max((1-p)*a+p*b,(1-p)*b+p*a)-a*(b+1)/n
        for gamma in (0.01,0.005):
            P,F=full_channel(n,a,p,gamma)
            assert abs((1-P)/gamma-rate)<0.055,(n,a,p,gamma,P,rate)
            assert 0<=1-F<16*gamma**2,(n,a,p,gamma,F)
            checks+=2
    print('VERIFY_OK',checks,'exact/combinatorial and full-Kraus checks')


if __name__=='__main__':main()
