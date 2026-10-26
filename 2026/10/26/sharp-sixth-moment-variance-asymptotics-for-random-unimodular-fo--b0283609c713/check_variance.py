"""Exact finite checks for the leading sixth-moment variance law."""
from itertools import combinations_with_replacement
from collections import defaultdict
from math import factorial


def coefficient_counts(n):
    blocks=defaultdict(list)
    for a,b,c in combinations_with_replacement(range(n),3):
        m=1 if a==b==c else (3 if a==b or b==c else 6)
        blocks[a+b+c].append(((a,b,c),m))
    coeff=defaultdict(int)
    for group in blocks.values():
        for a,wa in group:
            for b,wb in group:
                if a==b: continue
                counts={}
                for t in a: counts[t]=counts.get(t,0)+1
                for t in b: counts[t]=counts.get(t,0)-1
                key=tuple(sorted((k,v) for k,v in counts.items() if v))
                if key: coeff[key]+=wa*wb
    return coeff


def predicted_generic(n,coeff):
    group22=group33=rest=0
    for delta,c in coeff.items():
        pos=sum(v for k,v in delta if v>0)
        neg=-sum(v for k,v in delta if v<0)
        if len(delta)==4 and pos==2 and neg==2 and all(abs(v)==1 for _,v in delta):
            assert c==36*(n-2), (n,delta,c)
            group22+=c*c
        elif len(delta)==6:
            assert pos==neg==3 and all(abs(v)==1 for _,v in delta)
            assert c==36,(n,delta,c)
            group33+=c*c
        else: rest+=c*c
    return group22,group33,rest

if __name__=='__main__':
    for n in range(4,17):
        v=predicted_generic(n,coefficient_counts(n))
        print(n, *v, sum(v), round(sum(v)/n**5,6))
