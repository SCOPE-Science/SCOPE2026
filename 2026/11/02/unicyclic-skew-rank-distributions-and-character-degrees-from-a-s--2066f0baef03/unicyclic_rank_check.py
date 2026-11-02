"""Independent finite-field verification of the unicyclic skew-rank correction.
Run with python3 unicyclic_rank_check.py. No external packages required.
"""
from collections import Counter
from itertools import product

def matchings(edges):
    out=[]
    def rec(i, used, chosen):
        if i==len(edges):
            out.append(tuple(chosen)); return
        rec(i+1, used, chosen)
        a,b=edges[i]
        if a not in used and b not in used:
            chosen.append(i); rec(i+1,used|{a,b},chosen); chosen.pop()
    rec(0,set(),[])
    return out

def polynomial(n,edges,cycle,q):
    allm=matchings(edges); cyc=set(cycle); C=Counter()
    for bit in product([0,1],repeat=len(edges)):
        support={i for i,b in enumerate(bit) if b}
        admiss=[m for m in allm if set(m)<=support]
        nu=max(len(m) for m in admiss)
        maximal=[m for m in admiss if len(m)==nu]
        exceptional=(cyc<=support and len(cycle)%2==0 and
                     all(len(set(m)&cyc)*2==len(cycle) for m in maximal))
        multiplier=(q-1)**len(support)
        C[nu]+=multiplier
        if exceptional:
            assert multiplier%(q-1)==0
            C[nu]-=multiplier//(q-1)
            C[nu-1]+=multiplier//(q-1)
    return C

def add(a,b,q): return a^b if q==4 else (a+b)%q
def neg(a,q): return a if q==4 else (-a)%q
def mul(a,b,q):
    if q!=4:return a*b%q
    x=((a&1)*(b&1)) ^ ((((a&1)*(b>>1))^((a>>1)*(b&1)))<<1)
    if (a>>1) and (b>>1):x^=3
    return x

def inverse(a,q):
    return next(v for v in range(1,q) if mul(a,v,q)==1)

def rank(A,q):
    A=[r[:] for r in A]; n=len(A); pivot=0
    for j in range(n):
        k=next((i for i in range(pivot,n) if A[i][j]),None)
        if k is None:continue
        A[pivot],A[k]=A[k],A[pivot]
        t=inverse(A[pivot][j],q)
        A[pivot]=[mul(t,x,q) for x in A[pivot]]
        for i in range(pivot+1,n):
            z=A[i][j]
            if z:A[i]=[add(x,neg(mul(z,y,q),q),q) for x,y in zip(A[i],A[pivot])]
        pivot+=1
        if pivot==n:break
    return pivot

def observed(n,edges,q):
    ctr=Counter()
    for values in product(range(q),repeat=len(edges)):
        A=[[0]*n for _ in range(n)]
        for (a,b),v in zip(edges,values):
            A[a][b]=v;A[b][a]=neg(v,q)
        r=rank(A,q)
        assert r%2==0
        ctr[r//2]+=1
    return ctr

def check():
    cases=[
        ('triangle',3,[(0,1),(1,2),(0,2)],[0,1,2]),
        ('square',4,[(0,1),(1,2),(2,3),(0,3)],[0,1,2,3]),
        ('square_leaf',5,[(0,1),(1,2),(2,3),(0,3),(0,4)],[0,1,2,3]),
        ('square_path2',6,[(0,1),(1,2),(2,3),(0,3),(0,4),(4,5)],[0,1,2,3]),
        ('triangle_path2',5,[(0,1),(1,2),(0,2),(0,3),(3,4)],[0,1,2]),
        ('square_double_leaf',6,[(0,1),(1,2),(2,3),(0,3),(0,4),(1,5)],[0,1,2,3]),
    ]
    k=0
    for name,n,edges,cycle in cases:
        for q in (2,3,4):
            want=polynomial(n,edges,cycle,q)
            got=observed(n,edges,q)
            assert want==got,(name,q,want,got)
            assert sum(got.values())==q**len(edges)
            k+=1
            print(name,q,dict(sorted(got.items())))
    print('UNICYCLIC_SKEW_RANK_CORRECTION_OK',k)
if __name__=='__main__':check()
