#!/usr/bin/env python3
"""Exact finite-tree enumeration and high-precision series checks.

Usage: python3 verify.py
"""
from fractions import Fraction
from decimal import Decimal, localcontext
from math import log

REP = {'M':(1,1,1),'P':(0,0,1),'F':(0,1,1)}

def brute(h, forbidden):
    nodes=(1<<h)-1
    children=(1<<(h-1))-1
    ans=[0,0]
    v0,v1,v2=forbidden
    for bits in range(1<<nodes):
        good=True
        for j in range(children):
            if (((bits>>j)&1)==v0 and
                ((bits>>(2*j+1))&1)==v1 and
                ((bits>>(2*j+2))&1)==v2):
                good=False
                break
        if good: ans[bits&1]+=1
    return tuple(ans)

def advance(a,b,mode):
    s=a+b
    if mode=='M': return s*s,s*s-b*b
    if mode=='P': return s*s-a*b,s*s
    if mode=='F': return s*s-b*b,s*s
    raise ValueError(mode)

def q_and_next(p,mode):
    if mode=='M': q=2-p*p; return q,(1-p*p)/q
    if mode=='P': q=2-p*(1-p); return q,1/q
    if mode=='F': q=2-p*p; return q,1/q
    raise ValueError(mode)

def main():
    count=0
    exact={}
    for mode,pat in REP.items():
        a,b=1,1
        for h in range(1,5):
            assert (a,b)==brute(h,pat),(mode,h,a,b)
            exact[(mode,h)]=a+b
            count+=1
            a,b=advance(a,b,mode)
    assert [exact[(m,3)] for m in ('M','P','F')]==[89,86,82]
    for bits in range(8):
        pat=((bits>>2)&1,(bits>>1)&1,bits&1)
        sig=brute(3,pat)
        total=sum(sig)
        assert total in (89,86,82),(pat,total)
        # Global bit complement and global child exchange are count-preserving.
        comp=tuple(1-v for v in pat)
        mir=(pat[0],pat[2],pat[1])
        assert total==sum(brute(3,comp))==sum(brute(3,mir))
        count+=3
    for h in range(2,9):
        sc=[]
        for mode in ('M','P','F'):
            a,b=1,1
            for _ in range(1,h): a,b=advance(a,b,mode)
            sc.append(a+b)
        if h==2: assert sc==[7,7,7]
        else: assert sc[0]>sc[1]>sc[2]
        count+=1
    # Exact interval invariance and strict termwise order after the common first step.
    i_lo=Fraction(3,7); i_hi=Fraction(40,89)
    p_lo=Fraction(9,16); p_hi=Fraction(4,7)
    f_lo=Fraction(1,2); f_hi=Fraction(2,3)
    for m,lo,hi in [('M',i_lo,i_hi),('P',p_lo,p_hi),('F',f_lo,f_hi)]:
        a=q_and_next(lo,m)[1];b=q_and_next(hi,m)[1]
        assert lo<=min(a,b)<=max(a,b)<=hi,(m,a,b)
        count+=1
    assert i_hi*i_hi < p_hi*(1-p_hi)
    assert p_lo>Fraction(1,2) and Fraction(4,7)**2>Fraction(1,4)
    count+=2
    # Numeric series with a mathematical tail enclosure (all logarithms positive and < log 2).
    with localcontext() as ctx:
        ctx.prec=75
        LN2=Decimal(2).ln()
        terms=50
        means={}; roots={}; pref={}
        for mode in ('M','P','F'):
            p=Decimal('0.5'); a=LN2/2
            for j in range(1,terms):
                q,pnew=q_and_next(p,mode)
                a+=(q.ln()) / (Decimal(2)**(j+1))
                p=pnew
            tail=LN2/(Decimal(2)**terms)
            assert tail<Decimal('1e-14')
            for _ in range(150): p=q_and_next(p,mode)[1]
            qstar=q_and_next(p,mode)[0]
            means[mode]=(a,a+tail)
            roots[mode]=p
            pref[mode]=1/qstar
            count+=1
        assert means['M'][0]>means['P'][1]
        assert means['P'][0]>means['F'][1]
        assert roots['M']<roots['P']<roots['F']
        count+=3
        for m in ('M','P','F'):
            print(f'{m}: alpha in [{means[m][0]:.18f}, {means[m][1]:.18f}], root p={roots[m]:.18f}, prefactor={pref[m]:.18f}')
        print(f'VERIFY_OK: {count} exact finite-enumeration, symmetry, interval, and high-precision assertions')

if __name__=='__main__':main()
