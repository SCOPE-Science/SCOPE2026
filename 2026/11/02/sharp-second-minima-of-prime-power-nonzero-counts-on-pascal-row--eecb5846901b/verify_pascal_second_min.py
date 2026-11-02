#!/usr/bin/env python3
"""Independent integer/digit checks for sharp second minimum of nonzero Pascal rows."""
from collections import defaultdict
from math import comb

def digit_count(n, p, alpha):
    state={(0, 0):1}
    while n:
        digit=n%p
        nxt=defaultdict(int)
        for (borrow, total), mass in state.items():
            for choice in range(p):
                carry=int(choice+borrow>digit)
                if total+carry<alpha:
                    nxt[carry,total+carry]+=mass
        state=nxt
        n//=p
    return sum(mass for (b,c),mass in state.items() if b==0)

def predict(p,alpha,h):
    N=p**h
    if h<alpha:
        return N+1,N+2,[N+1]
    baseline=p**(alpha-1)+1
    if h==alpha:
        if p==2:
            if alpha==2:return baseline,6,[N+1,N+2]
            return baseline,3*2**(alpha-2)+3,[N+2]
        if alpha==2:return baseline,2*p+1,[2*N]
        if alpha==3:return baseline,2*p*p+1,[N+p,2*N]
        return baseline,(2*p-1)*p**(alpha-2)+p+1,[N+p]
    if p==2:
        if alpha==2:return baseline,6,[N+1,N+2**(h-1)]
        return baseline,2**alpha+2,[N+1]
    return baseline,2*p**(alpha-1)+1,[2*N]

def check():
    instances=0; indexes=0; exact=0
    for p in (2,3,5,7):
      for alpha in (2,3,4,5):
       for h in range(1,7):
        N=p**h
        if p*N>40000: continue
        baseline, second, winners=predict(p,alpha,h)
        vals=[(digit_count(n,p,alpha),n) for n in range(N,p*N)]
        first=min(v for v,n in vals)
        first_idx=[n for v,n in vals if v==first]
        sec=min(v for v,n in vals if v>first)
        sec_idx=[n for v,n in vals if v==sec]
        assert (first,first_idx,sec,sec_idx)==(baseline,[N],second,sorted(winners)),(p,alpha,h,first,first_idx,sec,sec_idx,baseline,second,winners)
        instances+=1;indexes+=len(vals)
    for p in (2,3,5,7):
      for n in range(0,230):
        for a in (1,2,3,4):
          c=sum(comb(n,k)%(p**a)!=0 for k in range(n+1))
          assert digit_count(n,p,a)==c,(p,n,a,c,digit_count(n,p,a))
          exact+=1
    print(f'CHECK_OK full_intervals={instances} counted_rows={indexes} direct_binomial_checks={exact}')
if __name__=='__main__':check()
