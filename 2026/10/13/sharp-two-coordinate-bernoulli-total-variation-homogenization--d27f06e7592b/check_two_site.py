"""Exact-arithmetic checks for two-coordinate Bernoulli TV homogenization.
No external packages; run with `python3 check_two_site.py`. Finite checks
supplement, and do not replace, the universal proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product


def twos(n, p, r):
    return ((n-p)*(n-r), (n-p)*r, p*(n-r), p*r)


def run(n):
    cnt=0
    equal=0
    for p,q,r,s in product(range(n+1), repeat=4):
        # Site one: p,q; site two: r,s.
        pp=twos(n,p,r)
        qq=twos(n,q,s)
        tv2=sum(abs(x-y) for x,y in zip(pp,qq))
        dif=abs(p+r-q-s)
        tot=p+q+r+s
        rhs=4*dif*(2*n+abs(2*n-tot))
        assert 9*tv2>=rhs, (n,p,q,r,s,tv2,rhs)
        # Stronger mass-sensitive inequality, not required for sharp factor.
        den=(6*n-tot if tot>=2*n else 2*n+tot)
        assert tv2*den>=4*n*n*dif, (n,p,q,r,s)
        if 9*tv2==rhs and dif:
            equal+=1
        cnt+=1
    return cnt,equal


if __name__=='__main__':
    for n in (2,4,8,12):
        count,equalities=run(n)
        print(f'grid 1/{n}: {count} quadruples checked, {equalities} nontrivial equalities')
    for epsilon in (Fraction(1,2),Fraction(1,10),Fraction(1,100),Fraction(1,1000)):
        p,r=1-2*epsilon,Fraction(1,2)
        q,s=Fraction(1),Fraction(1,2)+epsilon
        P=((1-p)*(1-r),(1-p)*r,p*(1-r),p*r)
        Q=((1-q)*(1-s),(1-q)*s,q*(1-s),q*s)
        tv=sum(abs(x-y) for x,y in zip(P,Q))/2
        hp,hq=(p+r)/2,(q+s)/2
        Pbar=((1-hp)**2,(1-hp)*hp,hp*(1-hp),hp**2)
        Qbar=((1-hq)**2,(1-hq)*hq,hq*(1-hq),hq**2)
        ht=sum(abs(x-y) for x,y in zip(Pbar,Qbar))/2
        assert tv==2*epsilon,(epsilon,tv)
        assert tv/ht==Fraction(8,1)/(9-3*epsilon)
        print(f'epsilon={epsilon}: TV/TV_hom={tv/ht}')
    print('All exact tests passed.')
