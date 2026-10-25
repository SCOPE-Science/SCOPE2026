from verify_johnson_rep import parts,make_rep,build,character_model
from functools import lru_cache
from collections import Counter
from math import factorial

def boxes(shape):return frozenset((i,j) for i,r in enumerate(shape) for j in range(r))
@lru_cache(None)
def char(shape,cycles):
    if not cycles:return int(not shape)
    r=cycles[0];sh=boxes(shape); total=0
    for inner in parts(sum(shape)-r):
        if len(inner)>len(shape) or any(inner[i]>shape[i] for i in range(len(inner))):continue
        rem=sh-boxes(inner)
        if len(rem)!=r:continue
        rows={i for i,j in rem}; todo={next(iter(rem))}; seen=set(todo)
        while todo:
            a,b=todo.pop()
            for x in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                if x in rem and x not in seen:seen.add(x);todo.add(x)
        if len(seen)!=r:continue
        if any((a+1,b) in rem and (a,b+1) in rem and (a+1,b+1) in rem for a,b in rem):continue
        total+=(-1)**(len(rows)-1)*char(inner,cycles[1:])
    return total

def go(n,k):
    vs,es,stars,tops,_=build(n,k)
    chi={la:character_model(n,k,make_rep(la),vs,es,stars,tops) for la in parts(n)}
    decomposition={}
    for sh in parts(n):
        nums=0
        for la,tr in chi.items():
            den=1
            for len_,ct in Counter(la).items():den*=len_**ct*factorial(ct)
            nums+=tr*char(sh,la)*factorial(n)//den
        assert nums%factorial(n)==0,(sh,nums)
        val=nums//factorial(n)
        assert val>=0,(sh,val)
        if val:decomposition[sh]=val
    print(n,k,decomposition)
for n,k in [(6,3),(7,3),(8,3),(8,4),(9,4),(10,5)]:go(n,k)
