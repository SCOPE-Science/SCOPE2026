from itertools import product
from math import factorial
from fractions import Fraction


def integer_partitions(n, min_part=1):
    # nondecreasing tuples
    if n == 0:
        yield ()
        return
    for first in range(min_part, n+1):
        for rest in integer_partitions(n-first, first):
            yield (first,)+rest


def build_parts(sizes):
    parts=[]
    part_of=[]
    for i,s in enumerate(sizes):
        inds=list(range(len(part_of), len(part_of)+s))
        parts.append(inds)
        part_of += [i]*s
    return parts, part_of


def proper_total(assign, part_of):
    n=len(assign)
    if any(c<0 for c in assign): return False
    for u in range(n):
        for v in range(u+1,n):
            if part_of[u]!=part_of[v] and assign[u]==assign[v]:
                return False
    return True


def forceable(assign0, sizes):
    parts, part_of=build_parts(sizes)
    r=len(sizes); n=sum(sizes)
    start=tuple(assign0)
    seen=set()
    def rec(a):
        if a in seen: return False
        seen.add(a)
        if all(c>=0 for c in a):
            return proper_total(a, part_of)
        # If already has a same-color cross-part conflict, no proper extension.
        for u in range(n):
            if a[u]<0: continue
            for v in range(u+1,n):
                if a[v]>=0 and part_of[u]!=part_of[v] and a[u]==a[v]:
                    return False
        moves=[]
        for v in range(n):
            if a[v]>=0: continue
            neigh_colors={a[u] for u in range(n) if part_of[u]!=part_of[v] and a[u]>=0}
            if len(neigh_colors)==r-1:
                missing=[c for c in range(r) if c not in neigh_colors]
                if len(missing)==1:
                    b=list(a); b[v]=missing[0]
                    moves.append(tuple(b))
        if not moves:
            return False
        return any(rec(b) for b in moves)
    return rec(start)


def characterization(assign, sizes):
    parts,_=build_parts(sizes)
    r=len(sizes)
    seeded=0
    seen_colors=set()
    for inds in parts:
        cs={assign[v] for v in inds if assign[v]>=0}
        if cs:
            seeded+=1
            if len(cs)!=1: return False
            c=next(iter(cs))
            if c in seen_colors: return False
            seen_colors.add(c)
    return seeded>=r-1


def formula_counts(sizes):
    # coefficient counts by domain size using polynomials in x
    r=len(sizes); N=sum(sizes)
    # Ai=(1+x)^ni-1 coefficients
    from math import comb
    As=[]
    for s in sizes:
        a=[0]*(s+1)
        for k in range(1,s+1): a[k]=comb(s,k)
        As.append(a)
    def mul(a,b):
        c=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): c[i+j]+=x*y
        return c
    total=[1]
    for a in As: total=mul(total,a)
    out=total+[0]*(N+1-len(total))
    for j in range(r):
        p=[1]
        for i,a in enumerate(As):
            if i!=j: p=mul(p,a)
        p += [0]*(N+1-len(p))
        out=[x+y for x,y in zip(out,p)]
    return [factorial(r)*x for x in out]


def formula_prob(sizes,p):
    r=len(sizes)
    q=1-r*p
    s=1-(r-1)*p
    A=[s**ni-q**ni for ni in sizes]
    prodA=Fraction(1)
    for x in A: prodA*=x
    W=prodA
    for j,nj in enumerate(sizes):
        term=q**nj
        for i,x in enumerate(A):
            if i!=j: term*=x
        W+=term
    return factorial(r)*W


def eval_counts(counts,sizes,p):
    N=sum(sizes); r=len(sizes); q=1-r*p
    return sum(Fraction(c)*p**k*q**(N-k) for k,c in enumerate(counts))


def main():
    types=0; assignments=0; forceable_count=0
    maxN=6
    grids=[Fraction(0),Fraction(1,20),Fraction(1,10)]
    for N in range(2,maxN+1):
        for sizes in integer_partitions(N):
            if len(sizes)<2: continue
            r=len(sizes)
            # sorted sizes => graph isomorphism type
            types+=1
            counts=[0]*(N+1)
            for a in product(range(-1,r), repeat=N):
                assignments+=1
                f=forceable(a,sizes)
                c=characterization(a,sizes)
                if f!=c:
                    raise AssertionError((sizes,a,f,c))
                if f:
                    forceable_count+=1
                    counts[sum(x>=0 for x in a)] +=1
            fc=formula_counts(sizes)
            if counts!=fc:
                raise AssertionError(('coeff',sizes,counts,fc))
            for p in grids+[Fraction(1,r), Fraction(1,2*r)]:
                if p>Fraction(1,r): continue
                if eval_counts(counts,sizes,p)!=formula_prob(sizes,p):
                    raise AssertionError(('prob',sizes,p,eval_counts(counts,sizes,p),formula_prob(sizes,p)))
            # r=2 specialization of Farr's connected bipartite formula
            if r==2:
                for p in [Fraction(1,10), Fraction(1,4), Fraction(1,2)]:
                    if p>Fraction(1,2): continue
                    N=sum(sizes)
                    want=2*((1-p)**N-(1-2*p)**N)
                    if formula_prob(sizes,p)!=want:
                        raise AssertionError(('bipartite',sizes,p))
    print(f'ALL CHECKS PASSED; multipartite_types={types}; partial_assignments={assignments}; forceable_assignments={forceable_count}; max_order={maxN}')

if __name__=='__main__': main()
