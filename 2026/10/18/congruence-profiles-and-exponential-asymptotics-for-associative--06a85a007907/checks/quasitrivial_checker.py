"""Independent finite verification of congruence profiles for associative quasitrivial semigroups."""
import itertools
import math
from functools import lru_cache

@lru_cache(None)
def set_partitions(n):
    if n == 0:
        return ((),)
    v=[]
    for par in set_partitions(n-1):
        v.append(par+((n-1,),))
        for i in range(len(par)):
            p=list(par)
            p[i]=p[i]+(n-1,)
            v.append(tuple(p))
    return tuple(v)

def ordered_partitions(n):
    for p in set_partitions(n):
        yield from itertools.permutations(p)

def operation(blocks, orientations, n):
    levels=[0]*n
    for i,block in enumerate(blocks):
        for a in block: levels[a]=i
    table=[]
    for x in range(n):
        row=[]
        for y in range(n):
            if levels[x]<levels[y]: row.append(y)
            elif levels[x]>levels[y]: row.append(x)
            else: row.append(x if orientations[levels[x]]==0 else y)
        table.append(tuple(row))
    return tuple(table)

def congruence_profile(table):
    n=len(table)
    cnt=[0]*(n+1)
    for partition in set_partitions(n):
        labels=[0]*n
        for i,block in enumerate(partition):
            for x in block: labels[x]=i
        is_cong=True
        for a in range(n):
            for b in range(a+1,n):
                if labels[a]!=labels[b]:continue
                for c in range(n):
                    if labels[table[a][c]] !=labels[table[b][c]] or labels[table[c][a]] != labels[table[c][b]]:
                        is_cong=False
                        break
                if not is_cong:break
            if not is_cong:break
        if is_cong:cnt[len(partition)]+=1
    return tuple(cnt)

def bell_poly(n):
    v=[0]*(n+1)
    for partition in set_partitions(n):v[len(partition)]+=1
    return tuple(v)

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def by_interval_formula(sizes):
    n=sum(sizes)
    v=[0]*(n+1)
    for cuts in itertools.product((0,1),repeat=len(sizes)-1):
        starts=(0,)+tuple(i+1 for i,b in enumerate(cuts) if b)
        ends=tuple(starts[1:])+(len(sizes),)
        p=[1]
        for i,j in zip(starts,ends):
            p=mul(p,bell_poly(sizes[i]) if j-i==1 else [0,1])
        for j,x in enumerate(p):v[j]+=x
    return tuple(v)

def direct(n):
    all_ops=set()
    checked=0
    full=[0]*(n+1)
    for blocks in ordered_partitions(n):
        ns=[len(b) for b in blocks]
        positions=[i for i,s in enumerate(ns) if s>=2]
        pred=by_interval_formula(tuple(ns))
        for bits in itertools.product((0,1),repeat=len(positions)):
            orient=[0]*len(ns)
            for i,b in zip(positions,bits):orient[i]=b
            op=operation(blocks,orient,n)
            assert op not in all_ops, ('duplicate',n,blocks)
            all_ops.add(op)
            real=congruence_profile(op)
            assert real==pred,(n,blocks,orient,real,pred)
            for j,x in enumerate(real):full[j]+=x
            checked+=1
    return checked,full

def egf_coeffs(N):
    # EGF for B and U and R, using exponential-coefficient arithmetic over rationals.
    from fractions import Fraction as Q
    def series_prod(a,b):
        return [sum(a[j]*b[i-j] for j in range(i+1)) for i in range(N+1)]
    def inv_one_minus(a):
        r=[Q(1)]+[Q(0)]*N
        for i in range(1,N+1):r[i]=sum(a[j]*r[i-j] for j in range(1,i+1))
        return r
    B=[Q(0)]+[Q(1)]+[Q(2,math.factorial(k)) for k in range(2,N+1)]
    # Bell EGF = exp(e^x-1), via known Bell numbers from independent partitions.
    U=[Q(0)]+[Q(1)]+[Q(2*len(set_partitions(k)),math.factorial(k)) for k in range(2,N+1)]
    RR=series_prod(series_prod(B,B),inv_one_minus(B))
    R=[U[i]+RR[i] for i in range(N+1)]
    H=inv_one_minus(R)
    return [(int(H[i]*math.factorial(i))) for i in range(N+1)],R

if __name__=='__main__':
    for n in range(1,5):
        c,p=direct(n)
        print('BRUTE',n,c,p,'total_pairs',sum(p))
    pred,R=egf_coeffs(9)
    print('EGF',pred)
    for n in range(1,5):
        c,p=direct(n)
        assert sum(p)==pred[n]
    print('CHECKER_OK')
