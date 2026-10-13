"""Independent finite-field tests for simultaneous graphical Lie centralizers.

Run: python verify_joint_centralizers.py
"""
from collections import Counter
from itertools import product
from math import comb

def add(a,b,q):
    return a^b if q==4 else (a+b)%q

def mul(a,b,q):
    if q!=4:return (a*b)%q
    result=0
    while b:
        if b&1:result^=a
        b>>=1
        a<<=1
        if a&4:a^=7
    return result

def inverse(a,q):
    for j in range(1,q):
        if mul(a,j,q)==1:return j
    raise ValueError('zero')

def negative(a,q):return a if q==4 else (-a)%q

def matrix_rank(matrix,q):
    A=[list(row) for row in matrix]
    if not A:return 0
    h=len(A); w=len(A[0]); r=0
    for j in range(w):
        k=next((i for i in range(r,h) if A[i][j]),None)
        if k is None:continue
        A[k],A[r]=A[r],A[k]
        z=inverse(A[r][j],q)
        A[r]=[mul(z,v,q) for v in A[r]]
        for i in range(r+1,h):
            factor=A[i][j]
            if factor:
                A[i]=[add(v,negative(mul(factor,w,q),q),q) for v,w in zip(A[i],A[r])]
        r+=1
        if r==h:break
    return r

def components(S,edges):
    remaining=set(S); parts=[]
    while remaining:
        v=remaining.pop(); part={v};todo=[v]
        while todo:
            u=todo.pop()
            for a,b in edges:
                w=b if a==u else (a if b==u else None)
                if w in remaining:
                    remaining.remove(w);part.add(w);todo.append(w)
        parts.append(part)
    return parts

def formula(n,edges,q,t):
    projective=(q**t-1)//(q-1)
    out=Counter()
    for mask in range(1<<n):
        S={i for i in range(n) if mask>>i&1}
        dominated=set(S)
        for i,j in edges:
            if i in S:dominated.add(j)
            if j in S:dominated.add(i)
        cs=components(S,edges)
        pol=Counter({0:1})
        for C in cs:
            tmp=Counter()
            for r,v in pol.items():
                tmp[r]+=v*projective
                tmp[r+1]+=v*(projective**len(C)-projective)
            pol=tmp
        base=len(dominated)-len(cs)
        for offset,v in pol.items():
            out[base+offset]+=(q-1)**len(S)*v
    return +out

def direct(n,edges,q,t):
    out=Counter()
    for a in product(range(q),repeat=t*n):
        rows=[]
        for k in range(t):
            for i,j in edges:
                row=[0]*n
                row[i]=negative(a[k*n+j],q)
                row[j]=a[k*n+i]
                rows.append(row)
        out[matrix_rank(rows,q)]+=1
    return +out

def examples():
    return {
        'single':(1,[]),
        'edge':(2,[(0,1)]),
        'path3':(3,[(0,1),(1,2)]),
        'triangle':(3,[(0,1),(1,2),(0,2)]),
        'path4':(4,[(0,1),(1,2),(2,3)]),
        'star4':(4,[(0,1),(0,2),(0,3)]),
        'cycle4':(4,[(0,1),(1,2),(2,3),(0,3)]),
        'twoedges':(4,[(0,1),(2,3)]),
        'edgeiso':(3,[(0,1)]),
    }

def validate():
    total=0; cases=0
    for name,(n,edges) in examples().items():
        for q,t in [(2,1),(3,1),(4,1),(2,2),(3,2),(4,2),(2,3),(3,3)]:
            if q**(t*n)>100000:continue
            expected=formula(n,edges,q,t)
            observed=direct(n,edges,q,t)
            assert expected==observed,(name,q,t,expected,observed)
            assert sum(observed.values())==q**(t*n)
            assert sum(expected.values())*q**(t*len(edges))==q**(t*(n+len(edges)))
            total+=q**(t*n); cases+=1
    # Every one of the 64 simple graphs on four labeled vertices, t=2, q=2.
    all_edges=[(i,j) for i in range(4) for j in range(i+1,4)]
    for mask in range(1<<len(all_edges)):
        E=[e for j,e in enumerate(all_edges) if mask>>j&1]
        expected=formula(4,E,2,2)
        observed=direct(4,E,2,2)
        assert expected==observed,(mask,expected,observed)
        total+=2**8;cases+=1
    # Top-rank property for graphs with no isolated vertices.
    for n,E in [examples()[x] for x in ['edge','path3','triangle','path4','star4','cycle4','twoedges']]:
        for q in [2,3,4]:
            assert formula(n,E,q,2)[n]>0
            assert formula(n,E,q,1)[n]==0
    print('VERIFY_OK_JOINT_GRAPH',cases,'cases',total,'full vertex-tuples')
    for name in ['path4','star4','cycle4']:
        n,E=examples()[name]
        x=formula(n,E,2,2)
        print(name, 'q=2,t=2, full Lie-tuples:',dict(sorted((r,v*2**(2*len(E))) for r,v in x.items())))
if __name__=='__main__':validate()
