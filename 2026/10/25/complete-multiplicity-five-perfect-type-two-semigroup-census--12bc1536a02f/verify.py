#!/usr/bin/env python3
"""Independent exhaustive checks of multiplicity-five perfect type-two semigroups.

Run: python3 verify.py
Standard library only.
"""
from itertools import product
from math import ceil


def kunz_valid(x):
    if min(x) < 1:
        return False
    v = [0] + list(x)
    return all(v[(i+j) % 5] <= v[i]+v[j]+(i+j)//5
               for i in range(1,5) for j in range(1,5)
               if (i+j)%5)


def direct_invariants(x):
    """Compute membership, gaps, and PF from the additive semigroup itself."""
    apery = [0] + [5*t+i for i,t in enumerate(x,1)]
    ceiling = 2 * max(apery) + 6
    member = [False] * (ceiling+1)
    member[0] = True
    generators = [5] + apery[1:]
    for n in range(1,ceiling+1):
        member[n] = any(n >= d and member[n-d] for d in generators)
    gaps = [i for i in range(ceiling+1) if not member[i]]
    F = max(gaps)
    pf = [i for i in gaps if all(i+d<=ceiling and member[i+d] for d in generators)]
    msg = [i for i in range(1,ceiling+1) if member[i] and
           not any(member[j] and member[i-j] for j in range(1,i))]
    return F, pf, msg, len(gaps)


def family(x):
    a,b,c,d = x
    if a == b == c+d+1 and 1<=d<=c<=2*d+1:
        return 'U'
    if c == d == a+b and 1<=a<=b<=2*a:
        return 'V'
    return None


def family_counts(s):
    if s<2:return 0,0,0,0
    u=s//2 - ((s+1)//3) + 1  # ceil((s-1)/3)=floor((s+1)/3)
    v=s//2 - ((s+2)//3) + 1  # ceil(s/3)=floor((s+2)/3)
    u4=max(0,(s-1)//2 - ((s+2)//3) + 1)
    v4=max(0,(s-1)//2 - ((s+3)//3) + 1)
    return u,v,u4,v4


def main():
    genus_bound=60
    stats={}
    checked=0
    for a in range(1,genus_bound-2):
        for b in range(1,genus_bound-a-1):
            for c in range(1,genus_bound-a-b):
                for d in range(1,genus_bound-a-b-c+1):
                    x=(a,b,c,d)
                    if not kunz_valid(x):continue
                    checked+=1
                    F,pf,msg,g=direct_invariants(x)
                    is_ptt=(len(pf)==2 and pf==[F-1,F])
                    f=family(x)
                    assert is_ptt==(f is not None),(x,is_ptt,f,pf)
                    if not is_ptt:continue
                    s=(c+d if f=='U' else a+b)
                    assert g==(3*s+2 if f=='U' else 3*s)
                    assert F==(5*s+2 if f=='U' else 5*s-1)
                    if f=='U':
                        assert len(msg)==(4 if d<c<2*d+1 else 3)
                    else:
                        assert len(msg)==(4 if a<b<2*a else 3)
                    key=(f,s)
                    dct=stats.setdefault(key,[0,0]);dct[0]+=1
                    if len(msg)==4:dct[1]+=1
    for s in range(2,genus_bound+1):
        u,v,u4,v4=family_counts(s)
        if 3*s+2 <= genus_bound:
            assert stats.get(('U',s),[0,0]) == [u,u4],('U',s,stats.get(('U',s)),u,u4)
        if 3*s <= genus_bound:
            assert stats.get(('V',s),[0,0]) == [v,v4],('V',s,stats.get(('V',s)),v,v4)
    # Distinct algebraic census over larger parameters, checking both formulations.
    for s in range(2,1001):
        count_u=sum(1 for d in range(1,s) if d<=s-d<=2*d+1)
        count_v=sum(1 for a in range(1,s) if a<=s-a<=2*a)
        count_u4=sum(1 for d in range(1,s) if d<s-d<2*d+1)
        count_v4=sum(1 for a in range(1,s) if a<s-a<2*a)
        assert [count_u,count_v,count_u4,count_v4] == list(family_counts(s))
    print('VERIFY_OK', 'valid_Kunz_4tuples_genus_le_60=', checked,
          'PTT_instances=',sum(v[0] for v in stats.values()),
          'embedding_dim_4=',sum(v[1] for v in stats.values()),
          'parameter_s_checked_through=',1000)

if __name__ == '__main__': main()
