"""Type-level weighted-equitable quotient and orbit-class test.
Usage: python verify_types.py
"""
from collections import Counter,defaultdict
from math import comb
from functools import lru_cache

@lru_cache(None)
def partitions(n, upper):
    if not n:return ((),)
    return tuple(t+(a,) for a in range(1,min(n,upper)+1) for t in partitions(n-a,a))

def type_transition(n):
    types=partitions(n,n)
    index={t:i for i,t in enumerate(types)}
    outgoing=[[] for _ in types]; incoming=[[] for _ in types]
    for i,typ in enumerate(types):
        mult=Counter(typ)
        for a in mult:
            for b in mult:
                if a>b or (a==b and mult[a]<2):continue
                new=list(typ);new.remove(a);new.remove(b);new.append(a+b)
                new.sort();j=index[tuple(new)]
                q=mult[a]*mult[b] if a!=b else comb(mult[a],2)
                p=mult[a+b]+1
                # In every coarser set partition, any one of the p blocks of
                # size a+b can be split into sizes a,b; equal halves unordered.
                qdown=p*comb(a+b,a)//(2 if a==b else 1)
                outgoing[i].append((j,q));incoming[j].append((i,qdown))
    return types,outgoing,incoming

def next_colors(col,up,dn):
    signatures=[]
    for i in range(len(col)):
        out=defaultdict(int);inc=defaultdict(int)
        for j,w in up[i]:out[col[j]]+=w
        for j,w in dn[i]:inc[col[j]]+=w
        signatures.append((col[i],tuple(sorted(out.items())),tuple(sorted(inc.items()))))
    palette={s:i for i,s in enumerate(sorted(set(signatures)))}
    return [palette[s] for s in signatures]

def main():
    worst=[]
    for n in range(1,37):
        t,up,dn=type_transition(n)
        c0=[0]*len(t);c1=next_colors(c0,up,dn);c2=next_colors(c1,up,dn)
        assert len(set(c2))==len(t),(n,len(set(c2)),len(t))
        same1=len(set(c1))==len(t)
        worst.append((n,len(t),len(set(c1)),len(set(c2))))
        assert same1 == (n<=13), ('first round threshold',n)
    print('WEIGHTED_ORBIT_QUOTIENT_PASS')
    print('n,types,round1_classes,round2_classes')
    for n,ty,r1,r2 in worst:print(n,ty,r1,r2,sep=',')
    print('minimal_first_round_collision_n=14; all_n_ge_14_witness_by_adding_singletons')
if __name__=='__main__':main()
