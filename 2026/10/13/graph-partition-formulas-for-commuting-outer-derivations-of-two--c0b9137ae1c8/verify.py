"""Finite-field checks of a quiver outer-derivation commutativity formula.

Run: python3 verify.py
All arithmetic and enumeration use the Python standard library.
"""
from collections import Counter
from fractions import Fraction
from itertools import product


def add(a, b, q):
    return a ^ b if q in (2, 4) else (a + b) % q


def neg(a, q):
    return a if q in (2, 4) else (-a) % q


def mul(a, b, q):
    if q == 4:
        x = 0
        for i in range(2):
            for j in range(2):
                if ((a >> i) & 1) and ((b >> j) & 1):
                    x ^= 1 << (i + j)
        if x & 8:
            x ^= 0b1110   # x^3=x^2+x, modulo x^2+x+1
        if x & 4:
            x ^= 0b111    # x^2=x+1
        return x
    return (a*b) % q


def mat_comm(a, b, q):
    a00,a01,a10,a11 = a
    b00,b01,b10,b11 = b
    ab = (add(mul(a00,b00,q),mul(a01,b10,q),q),
          add(mul(a00,b01,q),mul(a01,b11,q),q),
          add(mul(a10,b00,q),mul(a11,b10,q),q),
          add(mul(a10,b01,q),mul(a11,b11,q),q))
    ba = (add(mul(b00,a00,q),mul(b01,a10,q),q),
          add(mul(b00,a01,q),mul(b01,a11,q),q),
          add(mul(b10,a00,q),mul(b11,a10,q),q),
          add(mul(b10,a01,q),mul(b11,a11,q),q))
    return tuple(add(x,neg(y,q),q) for x,y in zip(ab,ba))


def matrix_tables(q):
    mats = list(product(range(q), repeat=4))
    identity = lambda t:(t,0,0,t)
    dic={m:i for i,m in enumerate(mats)}
    scalar_values=[dic[identity(t)] for t in range(q)]
    table=[]
    count=Counter()
    for x in mats:
        row=[]
        for y in mats:
            c=mat_comm(x,y,q)
            i=dic[c]
            row.append(i)
            count[i]+=1
        table.append(row)
    c0=q**6+q**5-q**3
    assert count[scalar_values[0]]==c0,(q,count[scalar_values[0]],c0)
    if q%2==0:
        c1=q**3*(q*q-1)
        assert all(count[i]==c1 for i in scalar_values[1:])
    else:
        assert all(count[i]==0 for i in scalar_values[1:])
    return mats,table,scalar_values


def subgraph_counts(q, vertices, edges):
    c0=q**6+q**5-q**3
    if q%2:
        return Fraction(c0**len(edges),q**(8*len(edges)))
    c1=q**3*(q*q-1)
    # Directly sum over the graph coboundary code; each element is counted once.
    shifts=set()
    for assignment in product(range(q), repeat=vertices):
        shifts.add(tuple(add(assignment[u],assignment[v],q) for u,v in edges))
    numerator=sum(__import__('math').prod(c0 if x==0 else c1 for x in s) for s in shifts)
    # Independently compute the graph-subset/Fortuin-Kasteleyn expression.
    sum_subset=0
    for bits in product((0,1),repeat=len(edges)):
        parent=list(range(vertices))
        def root(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        for take,(u,v) in zip(bits,edges):
            if take:
                parent[root(u)] = root(v)
        components=len({root(k) for k in range(vertices)})
        k=sum(bits)
        sum_subset+=q**components * c1**(len(edges)-k) * (c0-c1)**k
    full=sum_subset//q**components_count(vertices,edges)
    assert full*q**components_count(vertices,edges)==sum_subset
    assert full==numerator,(q,vertices,edges,numerator,full)
    return Fraction(numerator,q**(8*len(edges)))


def components_count(vertices,edges):
    parent=list(range(vertices))
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for u,v in edges: parent[root(u)] = root(v)
    return len({root(i) for i in range(vertices)})


def quotient_commuting_count(q, vertices, edges, table, scalar_values):
    m=len(edges)
    # A block is represented by its index among all q^4 matrices.
    # Scalar translation by sI is an additive coboundary.
    dim=q**4
    mats=list(product(range(q),repeat=4))
    index={a:i for i,a in enumerate(mats)}
    plus={}
    for a in range(dim):
        for t in range(q):
            x=mats[a]
            plus[a,t]=index[(add(x[0],t,q),x[1],x[2],add(x[3],t,q))]
    shifts={tuple(add(colors[u], neg(colors[v],q),q) for u,v in edges)
            for colors in product(range(q), repeat=vertices)}
    canonical={}
    for arr in product(range(dim), repeat=m):
        key=min(tuple(plus[x,t] for x,t in zip(arr,s)) for s in shifts)
        canonical[key]=None
    reps=list(canonical)
    code=set(shifts)
    scalar_inverse={v:k for k,v in enumerate(scalar_values)}
    count=0
    for a in reps:
        for b in reps:
            comm=[]
            for x,y in zip(a,b):
                t=scalar_inverse.get(table[x][y])
                if t is None: break
                comm.append(t)
            else:
                if tuple(comm) in code: count+=1
    expect=subgraph_counts(q,vertices,edges)
    actual=Fraction(count,len(reps)**2)
    assert actual==expect,(q,vertices,edges,len(reps),count,actual,expect)
    print('QUOTIENT_OK',q,vertices,edges,'size',len(reps),'commuting_pairs',count,'probability',actual)


def main():
    for q in (2,3,4,5):
        mats,table,scalars=matrix_tables(q)
        print('MATRIX_OK',q,'pairs',len(mats)**2)
        if q in (2,3,4):
            quotient_commuting_count(q,2,[(0,1)],table,scalars)
        if q==2:
            quotient_commuting_count(q,3,[(0,1),(1,2)],table,scalars)
            quotient_commuting_count(q,4,[(0,1),(1,2),(2,3)],table,scalars)
            quotient_commuting_count(q,3,[(0,1),(1,2),(0,2)],table,scalars)
            assert subgraph_counts(q,4,[(0,1),(1,2),(2,3)])==Fraction(343,4096)
            assert subgraph_counts(q,3,[(0,1),(1,2),(0,2)])==Fraction(407,8192)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
