#!/usr/bin/env python3
"""Independent finite-field tests of rank-one algebraic Nijenhuis identities on sl_2.
Uses the Lie-bracket structure constants and the unmodified torsion identity.
"""
from itertools import product, combinations

def field(q):
    if q==9:
        def dec(x): return (x%3,x//3)
        def enc(a,b): return (a%3)+3*(b%3)
        def add(x,y):
            a,b=dec(x);c,d=dec(y);return enc(a+c,b+d)
        def mul(x,y):
            a,b=dec(x);c,d=dec(y);return enc(a*c-b*d,a*d+b*c)
        neg=lambda x:enc(-x%3,-(x//3)%3)
    else:
        add=lambda x,y:(x+y)%q
        mul=lambda x,y:(x*y)%q
        neg=lambda x:(-x)%q
    plus=[[add(a,b) for b in range(q)] for a in range(q)]
    times=[[mul(a,b) for b in range(q)] for a in range(q)]
    minus=[neg(a) for a in range(q)]
    inv=[None]*q
    for a in range(1,q):
        inv[a]=next(b for b in range(1,q) if times[a][b]==1)
    return plus,times,minus,inv

def verify(q):
    add,mul,neg,inv=field(q)
    zero=(0,0,0)
    vecs=list(product(range(q),repeat=3))
    nz=[v for v in vecs if v!=zero]
    def dot(x,y):
        return add[add[mul[x[0]][y[0]]][mul[x[1]][y[1]]]][mul[x[2]][y[2]]]
    def scale(s,x):return (mul[s][x[0]],mul[s][x[1]],mul[s][x[2]])
    def subv(x,y):return tuple(add[x[i]][neg[y[i]]] for i in range(3))
    def addv(x,y):return tuple(add[x[i]][y[i]] for i in range(3))
    def bracket(x,y):
        # [e,f]=h, [h,e]=2e, [h,f]=-2f
        a=add[mul[x[2]][y[0]]][neg[mul[x[0]][y[2]]]]
        b=add[mul[x[1]][y[2]]][neg[mul[x[2]][y[1]]]]
        c=add[mul[x[0]][y[1]]][neg[mul[x[1]][y[0]]]]
        return (add[a][a],add[b][b],c)
    basis=[(1,0,0),(0,1,0),(0,0,1)]
    lines=[]
    for f in nz:
        pivot=next(x for x in f if x)
        if pivot==1:lines.append(f)
        # This logic picks first nonzero =1, exactly one rep per line.
    assert len(lines)==q*q+q+1,(q,len(lines))
    nij=0
    squares=[]
    good_f=set()
    for f in lines:
        # Spectral quadric in dual coordinates (u,w,z): 4uw+z^2.
        term=add[mul[4%q if q!=9 else 1][mul[f[0]][f[1]]]][mul[f[2]][f[2]]] if q!=9 else add[mul[1][mul[f[0]][f[1]]]][mul[f[2]][f[2]]]
        # For GF9, integer 4=1 in prime subfield, yes.
        for v in nz:
            def N(x):return scale(dot(f,x),v)
            torsion_zero=True
            for i,j in combinations(range(3),2):
                x,y=basis[i],basis[j]
                nx,ny=N(x),N(y)
                z=subv(subv(addv(bracket(nx,ny),N(N(bracket(x,y)))),N(bracket(nx,y))),N(bracket(x,ny)))
                if z!=zero:torsion_zero=False;break
            if torsion_zero:
                nij+=1
                good_f.add(f)
                if dot(f,v)==0:
                    squares.append((f,v))
            assert torsion_zero==(term==0),(q,f,v,term,torsion_zero)
    assert nij==(q+1)*(q**3-1),(q,nij)
    assert len(good_f)==q+1,(q,len(good_f))
    assert len(squares)==(q+1)*(q*q-1),(q,len(squares))
    ops=[None]+squares
    n=len(ops)
    adjacency=[0]*n
    pair_by_support=[0,0,0]
    # Direct algebraic product N_i N_j=(f_i(v_j))v_i f_j.
    for i in range(n):
        for j in range(n):
            if i==0 or j==0:
                compatible=True
            else:
                fi,vi=ops[i];fj,vj=ops[j]
                a=dot(fi,vj);b=dot(fj,vi)
                # Test the actual compositions on each original basis vector.
                def compose_scalar(f,g,v,w,x):
                    return scale(dot(f,w),scale(dot(g,x),v))
                cm=True
                for x in basis:
                    left=compose_scalar(fi,fj,vi,vj,x)
                    right=compose_scalar(fj,fi,vj,vi,x)
                    if left!=right:cm=False;break
                assert cm==(a==0 and b==0),(q,i,j,cm,a,b)
                compatible=cm
            if compatible:
                adjacency[i]|=1<<j
                pair_by_support[(i>0)+(j>0)]+=1
    single=len(squares)
    pair_pred=(q+1)*(q*q-1)**2+(q*(q+1)//2)*2*(q-1)**2
    assert pair_by_support==[1,2*single,pair_pred],(q,pair_by_support,pair_pred)
    triple_pred=0
    for s in range(4):
        from math import comb
        if s==0:C=1
        else:C=(q+1)*(q*q-1)**s+(q*(q+1)//2)*(2**s-2)*(q-1)**s
        triple_pred+=comb(3,s)*C
    triple_count=sum((adjacency[i]&adjacency[j]).bit_count() for i in range(n) for j in range(n) if adjacency[i]>>j &1)
    assert triple_count==triple_pred,(q,triple_count,triple_pred)
    print(f'GF({q}): rank-one Nijenhuis={nij}; rank-one square-zero={single}; commuting pairs={sum(pair_by_support)}; commuting triples={triple_count}; raw torsion and composition PASS')

if __name__=='__main__':
    for q in (3,5,7,9):verify(q)
    print('LIE_NIJENHUIS_SL2_ALL_DIRECT_CHECKS_OK')
