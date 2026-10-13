"""Standalone checks for Boolean modal term spectra of finite full successor trees.
No third-party modules required. This is finite corroboration, not a proof of the general theorem.
"""
from itertools import product
from math import comb, factorial
from fractions import Fraction


def children(b,h):
    ch=[]
    def build(level):
        index=len(ch); ch.append([])
        if level:
            for _ in range(b):
                ch[index].append(build(level-1))
        return index
    build(h)
    return ch


def polynomial_count(b,h,q):
    vals=[q]
    for _ in range(h):
        t=vals[-1]
        vals.append(q*sum(comb(t,k) for k in range(1,min(b,t)+1)))
    return sum(vals),vals


def observed_type_counts(b,h,q,max_coloring=200000):
    ch=children(b,h)
    n=len(ch)
    if q**n>max_coloring: return None
    levels=[None]*n
    def height(v):
        if levels[v] is None:
            levels[v]=0 if not ch[v] else 1+height(ch[v][0])
        return levels[v]
    for v in range(n):height(v)
    seen=[set() for _ in range(h+1)]
    for cols in product(range(q),repeat=n):
        ty=[None]*n
        for v in range(n-1,-1,-1):
            ty[v]=(cols[v],frozenset(ty[w] for w in ch[v]))
            seen[levels[v]].add(ty[v])
    return tuple(len(s) for s in seen)


def modal_closure(b,h):
    ch=children(b,h)
    n=len(ch)
    assert n<=4
    worlds=(1<<n)
    full=(1<<(worlds*n))-1
    X=0
    for val in range(worlds):
        for w in range(n):
            if val & (1<<w): X|=1<<(val*n+w)
    def dia(mask):
        out=0
        for val in range(worlds):
            for w in range(n):
                if any(mask & (1<<(val*n+child)) for child in ch[w]):
                    out|=1<<(val*n+w)
        return out
    S={0,full,X,full^X}
    while True:
        old=len(S)
        elems=list(S)
        S.update(full^x for x in elems)
        S.update(dia(x) for x in elems)
        elems=list(S)
        S.update(x|y for i,x in enumerate(elems) for y in elems[i:])
        if len(S)==old:break
        assert len(S)<2000
    return len(S)


def leading(b,h):
    size=sum(b**i for i in range(h+1))
    return size, Fraction(1,factorial(b)**sum(b**i for i in range(h)))


def main():
    exhaustive=0
    for b in range(1,5):
        for h in range(0,4):
            for q in (1,2,3,4):
                observed=observed_type_counts(b,h,q)
                if observed is not None:
                    count,parts=polynomial_count(b,h,q)
                    assert observed==tuple(parts),(b,h,q,observed,parts)
                    exhaustive+=1
    assert modal_closure(1,1)==2**(2+4)
    assert modal_closure(2,1)==2**(2+6)
    assert modal_closure(3,1)==2**(2+6)
    n1,c1=leading(2,4)
    n2,c2=leading(5,2)
    assert n1==n2==31 and c1!=c2
    for b in range(1,8):
        for h in range(1,5):
            n,c=leading(b,h)
            assert c==Fraction(1,factorial(b)**((n-1)//b))
    # Two different 31-point trees have same polynomial degree but different leading coefficients.
    print('VERIFY_OK type_censuses',exhaustive,'direct_closures',3,
          'equal_order_reconstruction',n1,'leading_binary',str(c1),
          'leading_fiveary',str(c2))

if __name__=='__main__':main()
