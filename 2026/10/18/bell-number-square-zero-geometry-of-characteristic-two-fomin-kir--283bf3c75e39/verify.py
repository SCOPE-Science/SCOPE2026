#!/usr/bin/env python3
"""Independent quadratic-quotient checks for degree-one square-zero elements of E_n."""
from itertools import combinations,product
from math import comb

def partitions(n):
    blocks=[]
    def rec(i):
        if i==n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(i)
            yield from rec(i+1)
            b.pop()
        blocks.append([i]); yield from rec(i+1); blocks.pop()
    yield from rec(0)

def predicted(coeffs,edges,n):
    adjacency={i:set() for i in range(n)}
    for (i,j),x in zip(edges,coeffs):
        if x:
            adjacency[i].add(j); adjacency[j].add(i)
    visited=set()
    for i in range(n):
        if i in visited:continue
        stack=[i]; comp=set()
        while stack:
            j=stack.pop()
            if j in comp:continue
            comp.add(j);stack.extend(adjacency[j]-comp)
        visited.update(comp)
        if len(comp)>=2:
            values={coeffs[edges.index((a,b))] for a,b in combinations(sorted(comp),2)}
            if len(values)!=1 or 0 in values:return False
    return True

def relations(n):
    edges=list(combinations(range(n),2)); M=len(edges)
    idx={x:i for i,x in enumerate(edges)}
    def mon(e,f):return 1<<(idx[e]*M+idx[f])
    R=[]
    for e in edges:R.append(mon(e,e))
    for e,f in combinations(edges,2):
        if len(set(e+f))==4:R.append(mon(e,f)^mon(f,e))
    for i,j,k in combinations(range(n),3):
        a,b,c=(i,j),(i,k),(j,k)
        R.append(mon(a,c)^mon(c,b)^mon(b,a))
        R.append(mon(c,a)^mon(a,b)^mon(b,c))
    basis={}
    for v in R:
        while v:
            p=v.bit_length()-1
            if p in basis:v^=basis[p]
            else:
                basis[p]=v;break
    return edges,tuple(sorted(basis.items(),reverse=True)),len(R),len(basis)

def gf_mul(a,b,q):
    # q=2 or q=4, both fields explicitly defined over F2
    if q==2:return a&b
    assert q==4
    x=0
    while b:
        if b&1:x^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return x

def vanishes(coeffs,q,base,M):
    v=[0]*(M*M)
    for i,a in enumerate(coeffs):
        if not a:continue
        for j,b in enumerate(coeffs):
            if b:v[i*M+j]=gf_mul(a,b,q)
    for pivot,mask in base:
        z=v[pivot]
        if z:
            while mask:
                lowest=mask & -mask
                p=lowest.bit_length()-1
                v[p]^=z
                mask^=lowest
    return not any(v)

def expected(n,q):
    return sum((q-1)**sum(len(B)>=2 for B in pi) for pi in partitions(n))

def run(n,q):
    edges,base,raw_rank,rank=relations(n)
    M=len(edges)
    count=0
    for vals in product(range(q),repeat=M):
        lhs=vanishes(vals,q,base,M)
        rhs=predicted(vals,edges,n)
        assert lhs==rhs,(n,q,vals,lhs,rhs)
        count+=lhs
    assert count==expected(n,q),(n,q,count,expected(n,q))
    print('checked',n,q,'M',M,'quadratic relation rank',rank,'square-zero',count)

def component_test(n):
    es=list(combinations(range(n),2))
    parts=list(partitions(n))
    def gens(pi):
        return tuple(sum(1<<es.index((i,j)) for i,j in combinations(block,2))
                     for block in pi if len(block)>=2)
    def span(gen):
        out={0}
        for v in gen:out.update({w^v for w in tuple(out)})
        return out
    subspaces=[span(gens(pi)) for pi in parts]
    for p,pi in enumerate(parts):
        for j,rho in enumerate(parts):
            lhs=subspaces[p].issubset(subspaces[j])
            actual={tuple(b) for b in pi if len(b)>=2}.issubset(
                {tuple(b) for b in rho if len(b)>=2})
            assert lhs==actual,(n,pi,rho)
    maximals=[p for p,S in enumerate(subspaces)
              if not any(S<T for T in subspaces)]
    count=sum(sum(len(b)==1 for b in pi)<=1 for pi in parts)
    assert len(maximals)==count,(n,len(maximals),count)
    assert max(len(gens(parts[p])) for p in maximals)==n//2
    print('geometry',n,'components',len(maximals),'maximal dimension',n//2)

if __name__=='__main__':
    for n,q in [(2,2),(3,2),(3,4),(4,2),(4,4),(5,2),(6,2)]:
        run(n,q)
    for n in range(2,7):component_test(n)
    print('VERIFY_OK_FK_CHARACTERISTIC_TWO')
