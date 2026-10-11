"""Exact cellular-chain sanity checks for sign-twisted two-point graph configuration homology.

Usage: python3 verify.py  (Python 3 standard library only)

A graph is given by numbered vertices and undirected edges.  We model the
square of the graph subdivided on each diagonal before quotienting by the
particle transposition and removing diagonal cells.  Twisting parameter
chi=+1 means constant coefficients and chi=-1 the exchange-sign local system.
"""
from fractions import Fraction
from itertools import combinations
from random import Random


def rank_q(a):
    if not a: return 0
    n=len(a[0]); m=[list(map(Fraction,r)) for r in a]
    row=0
    for c in range(n):
        p=next((j for j in range(row,len(m)) if m[j][c]),None)
        if p is None: continue
        m[row],m[p]=m[p],m[row]
        z=m[row][c]
        for j in range(row+1,len(m)):
            if m[j][c]:
                q=m[j][c]/z
                for k in range(c,n):m[j][k]-=q*m[row][k]
        row+=1
        if row==len(m):break
    return row


def rank_two(a):
    if not a:return 0
    cols=len(a[0]); rows=[]
    for row in a:
        x=0
        for i,z in enumerate(row):
            if z&1:x|=1<<i
        rows.append(x)
    basis={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k in basis:x^=basis[k]
            else:
                basis[k]=x
                break
    return len(basis)


def chain_matrices(n,edges,chi):
    assert chi in (-1,1)
    edges=[tuple(sorted(e)) for e in edges]
    assert len(set(edges))==len(edges) and all(0<=u<v<n for u,v in edges)
    vertices=range(n); en=range(len(edges))
    c0=list(combinations(vertices,2))
    c1=[(w,e) for w in vertices for e in en]
    c2=[('cross',i,j) for i,j in combinations(en,2)]+[('same',i) for i in en]
    i0={x:i for i,x in enumerate(c0)}
    i1={x:i for i,x in enumerate(c1)}
    d1=[[0]*len(c1) for _ in c0]
    d2=[[0]*len(c2) for _ in c1]
    def vpair(a,b,coef,j):
        if a!=b:d1[i0[tuple(sorted((a,b)))]][j]+=coef*(1 if a<b else chi)
    for j,(w,e) in enumerate(c1):
        u,v=edges[e]
        vpair(w,v,1,j)
        vpair(w,u,-1,j)
    for j,obj in enumerate(c2):
        if obj[0]=='cross':
            _,e,f=obj
            ue,ve=edges[e]; uf,vf=edges[f]
            d2[i1[(ve,f)]][j]+=1
            d2[i1[(ue,f)]][j]-=1
            d2[i1[(vf,e)]][j]-=chi
            d2[i1[(uf,e)]][j]+=chi
        else:
            _,e=obj
            u,v=edges[e]
            d2[i1[(u,e)]][j]+=1
            d2[i1[(v,e)]][j]+=chi
    for i in range(len(c0)):
        for j in range(len(c2)):
            assert sum(d1[i][k]*d2[k][j] for k in range(len(c1)))==0
    return d1,d2,(len(c0),len(c1),len(c2))


def connected(n,edges):
    todo={0}; reached=set()
    while todo:
        v=todo.pop()
        if v in reached:continue
        reached.add(v)
        todo.update(w for e in edges for w in e if v in e and w!=v)
    return len(reached)==n


def run_case(n,edges):
    b=len(edges)-n+1
    for chi in (-1,1):
        d1,d2,(c0,c1,c2)=chain_matrices(n,edges,chi)
        r1,r2=rank_q(d1),rank_q(d2)
        assert c0-r1==0
        if chi==-1:
            assert (c1-r1-r2,c2-r2)==(b,b*(b+1)//2)
            # Over F2 both types have mod-two homology of dimensions b and b(b+1)/2.
            assert (c1-rank_two(d1)-rank_two(d2),c2-rank_two(d2))==(b,b*(b+1)//2)
        else:
            assert (c1-r1-r2,c2-r2)==(0,b*(b-1)//2)
            assert (c1-rank_two(d1)-rank_two(d2),c2-rank_two(d2))==(b,b*(b+1)//2)
    return b


def main():
    examples=[
        (2,[(0,1)]),
        (3,[(0,1),(1,2)]),
        (3,[(0,1),(0,2),(1,2)]),
        (4,[(0,1),(0,2),(1,2),(1,3),(2,3)]),
        (4,list(combinations(range(4),2))),
        (5,[(0,1),(1,2),(2,3),(3,4),(0,4),(0,2)]),
        (5,list(combinations(range(5),2))),
    ]
    rng=Random(271828)
    allcases=set((n,tuple(edges)) for n,edges in examples)
    for n in (4,5):
        possible=list(combinations(range(n),2))
        for _ in range(90):
            chosen=tuple(e for e in possible if rng.randrange(3)!=0)
            if connected(n,chosen):allcases.add((n,chosen))
    out={}
    for n,edges in sorted(allcases):
        b=run_case(n,edges)
        out[b]=out.get(b,0)+1
    assert set(out)>=set(range(5))
    print('EXACT_CELLULAR_CASES',sum(out.values()),'CYCLE_RANK_COUNTS',sorted(out.items()))
    print('BOUNDARY_SQUARE_ZERO_AND_Q_F2_HOMOLOGY_OK')
    print('VERIFY_OK')

if __name__=='__main__':main()
