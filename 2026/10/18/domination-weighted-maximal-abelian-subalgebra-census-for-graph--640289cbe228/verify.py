"""Independent finite-field verification of maximal abelian graph Lie subalgebras.

Usage: python verify.py
Only the canonical RREF and centralizer calculations are used for the
algebraic count; dominating subsets enter only in the predicted formula.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

class Field:
    def __init__(self, q):
        assert q in (2, 3, 4, 5)
        self.q = q
    def add(self, x, y):
        return (x ^ y) if self.q == 4 else (x + y) % self.q
    def neg(self, x):
        return x if self.q == 4 else (-x) % self.q
    def sub(self, x, y):
        return self.add(x, self.neg(y))
    def mul(self, x, y):
        if self.q != 4:
            return (x * y) % self.q
        z=0
        for j in range(2):
            if (y >> j)&1:
                z ^= x << j
        for j in (2,):
            if (z >> j)&1:
                z ^= 7 << (j-2)   # x^2 = x+1
        return z
    def inv(self, x):
        assert x
        for a in range(1, self.q):
            if self.mul(x,a)==1: return a
        raise AssertionError('not a field')

def rank(A, field):
    if not A: return 0
    B=[list(row) for row in A]
    rows=len(B); cols=len(B[0]); i=0
    for j in range(cols):
        t=next((s for s in range(i,rows) if B[s][j]), None)
        if t is None: continue
        B[i],B[t]=B[t],B[i]
        inv=field.inv(B[i][j])
        B[i]=[field.mul(inv,v) for v in B[i]]
        for s in range(rows):
            if s!=i and B[s][j]:
                mul=B[s][j]
                B[s]=[field.sub(B[s][k], field.mul(mul,B[i][k])) for k in range(cols)]
        i+=1
        if i==rows: break
    return i

def subspaces(n,q):
    # Every k-dimensional subspace has one unique reduced row echelon basis.
    for k in range(n+1):
        for pivots in combinations(range(n),k):
            free=[]
            for i,pivot in enumerate(pivots):
                for j in range(pivot+1,n):
                    if j not in pivots:
                        free.append((i,j))
            for values in product(range(q),repeat=len(free)):
                B=[[0]*n for _ in range(k)]
                for i,p in enumerate(pivots): B[i][p]=1
                for (i,j),a in zip(free,values): B[i][j]=a
                yield B

def maximal_abelian_profile(n,edges,q):
    f=Field(q)
    ans=Counter()
    for B in subspaces(n,q):
        k=len(B)
        if any(f.sub(f.mul(u[i],v[j]), f.mul(u[j],v[i]))
               for i,j in edges for u,v in combinations(B,2)):
            continue
        # An abelian U is inclusion-maximal iff its centralizer in V is U.
        eqns=[]
        for u in B:
            for i,j in edges:
                row=[0]*n
                row[i]=u[j]
                row[j]=f.neg(u[i])
                eqns.append(row)
        if rank(eqns,f) == n-k:
            ans[k]+=1
    return ans

def predicted(n,edges,q):
    ans=Counter()
    for mask in range(1<<n):
        S={i for i in range(n) if mask & (1<<i)}
        if any(v not in S and not any((min(u,v),max(u,v)) in edges for u in S)
               for v in range(n)):
            continue
        cc=0; unseen=set(S)
        while unseen:
            cc+=1
            stack=[unseen.pop()]
            while stack:
                v=stack.pop()
                nbr={u for u in unseen if (min(u,v),max(u,v)) in edges}
                unseen-=nbr
                stack.extend(nbr)
        ans[cc]+=(q-1)**(len(S)-cc)
    return ans

def graphs(n):
    pairs=list(combinations(range(n),2))
    for mask in range(1<<len(pairs)):
        yield tuple(pairs[i] for i in range(len(pairs)) if mask & (1<<i))

def check():
    cases=0
    for q in (2,3,4,5):
        for n in range(1,5):
            for edges in graphs(n):
                predicted_count=predicted(n,edges,q)
                direct_count=maximal_abelian_profile(n,edges,q)
                assert predicted_count==direct_count,(n,q,edges,predicted_count,direct_count)
                cases+=1
        print('ALL_GRAPHS_UP_TO_FOUR_VERTICES_VERIFIED',q)
    print('STAR_K_1_3', dict(sorted(maximal_abelian_profile(4,((0,1),(0,2),(0,3)),3).items())))
    print('COMPLETE_K_4', dict(sorted(maximal_abelian_profile(4,tuple(combinations(range(4),2)),3).items())))
    print('ALL_GRAPH_LIE_MAXIMAL_ABELIAN_CHECKS_PASSED',cases)

if __name__=='__main__': check()
