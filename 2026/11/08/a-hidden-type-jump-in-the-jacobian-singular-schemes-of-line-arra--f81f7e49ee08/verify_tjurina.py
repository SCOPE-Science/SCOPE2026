#!/usr/bin/env python3
"""Exact finite-field cross-checks for local Tjurina algebras of line pencils.
No external packages. This tests homogeneous quotient dimensions, not the general proof.
"""
from itertools import product

def field(p, e):
    if (p,e)==(2,2):
        def add(a,b): return a^b
        def mul(a,b):
            c=0
            for i in range(2):
                for j in range(2):
                    if (a>>i &1) and (b>>j&1): c^=1<<(i+j)
            if c&4: c^=7
            return c
        values=[0,1,2,3]
    elif e==1:
        def add(a,b): return (a+b)%p
        def mul(a,b): return (a*b)%p
        values=list(range(p))
    else: raise ValueError('unsupported field')
    def neg(a):
        for b in values:
            if add(a,b)==0: return b
        raise ValueError
    def inv(a):
        for b in values[1:]:
            if mul(a,b)==1: return b
        raise ValueError
    return values,add,mul,neg,inv

def polynomial_product(lines, add, mul):
    f={(0,0):1}
    for a,b in lines:
        z={}
        for (i,j),v in f.items():
            for key,c in (((i+1,j),a),((i,j+1),b)):
                z[key]=add(z.get(key,0),mul(v,c))
        f={x:y for x,y in z.items() if y}
    return f

def deriv(f,axis,p,mul):
    z={}
    for (i,j),v in f.items():
        k=(i,j)[axis]
        if k%p:
            z[((i-1,j) if axis==0 else (i,j-1))]=mul(k%p,v)
    return z

def matrix_rank(rows,ncols,field_ops):
    values,add,mul,neg,inv=field_ops
    rows=[r[:] for r in rows]
    rank=0
    for c in range(ncols):
        pivot=next((t for t in range(rank,len(rows)) if rows[t][c]),None)
        if pivot is None:continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        x=inv(rows[rank][c]);rows[rank]=[mul(x,u) for u in rows[rank]]
        for t in range(rank+1,len(rows)):
            if rows[t][c]:
                v=rows[t][c];rows[t]=[add(a,neg(mul(v,b))) for a,b in zip(rows[t],rows[rank])]
        rank+=1
        if rank==len(rows):break
    return rank

def ideal_rank(degree,gens,ops):
    values,add,mul,neg,inv=ops
    cols=[(i,degree-i) for i in range(degree+1)]
    rows=[]
    for g in gens:
        if not g:continue
        d=next(iter(g)); base=sum(d)
        if degree<base:continue
        for i in range(degree-base+1):
            a,b=i,degree-base-i
            rr=[0]*(degree+1)
            for (u,v),w in g.items():rr[cols.index((u+a,v+b))]=w
            rows.append(rr)
    return matrix_rank(rows,len(cols),ops)

cases=[(2,2,[(1,0),(0,1),(1,1),(1,2)]),
       (3,1,[(1,0),(0,1),(1,1)]),
       (5,1,[(1,0),(0,1),(1,1),(1,2),(1,3)]),
       (3,1,[(1,0),(0,1),(1,1),(1,2)]),
       (2,2,[(1,0),(0,1),(1,2)]),
       (5,1,[(1,0),(0,1),(1,1),(1,2)])]
for p,e,lines in cases:
    ops=field(p,e);_,add,mul,neg,inv=ops
    m=len(lines)
    f=polynomial_product(lines,add,mul)
    fx=deriv(f,0,p,mul);fy=deriv(f,1,p,mul)
    assert len(fx)>0 and len(fy)>0
    # ordinary m-fold point: all slopes [a:b] distinct
    assert len({tuple(x) for x in lines})==len(lines)
    hf=[]
    for d in range(2*m):
        colength=d+1-ideal_rank(d,[f,fx,fy],ops)
        predicted=max(0,min(d+1,2*m-3-d))
        hf.append(colength)
        assert colength==predicted,(p,e,m,d,colength,predicted)
    before=ideal_rank(m,[fx,fy],ops)
    after=ideal_rank(m,[fx,fy,f],ops)
    assert after-before==(1 if m%p==0 else 0),(p,m,before,after)
    assert sum(hf)==(m-1)**2
    print(f'OK: characteristic {p}, degree {m}, q={p**e}, HF={hf[:2*m-3]}, extra_equation={after-before}')
print('ALL_CHECKS_PASSED')
