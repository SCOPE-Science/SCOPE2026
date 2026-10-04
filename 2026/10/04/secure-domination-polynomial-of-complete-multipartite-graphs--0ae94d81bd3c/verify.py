from itertools import combinations
from math import comb


def integer_partitions(n, minimum=1, prefix=()):
    if n == 0:
        if len(prefix) >= 2:
            yield prefix
        return
    for a in range(minimum, n + 1):
        yield from integer_partitions(n-a, a, prefix+(a,))


def build(parts):
    blocks=[]; part=[]; start=0
    for i,n in enumerate(parts):
        block=list(range(start,start+n)); blocks.append(block)
        part.extend([i]*n); start+=n
    N=start
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if u != v and part[u] != part[v]:
                adj[u].add(v)
    return blocks,part,adj


def dominates(S,adj):
    D=set(S)
    for v in S: D |= adj[v]
    return len(D)==len(adj)


def secure_direct(S,adj):
    S=set(S); N=len(adj)
    if not dominates(S,adj): return False
    for u in range(N):
        if u in S: continue
        if not any(u in adj[v] and dominates((S-{v})|{u},adj) for v in S):
            return False
    return True


def structural(S,parts,blocks):
    S=set(S)
    occ=[len(S.intersection(B)) for B in blocks]
    supp=[i for i,s in enumerate(occ) if s]
    if len(supp)>=3:
        return True
    if len(supp)==1:
        i=supp[0]
        if occ[i] != parts[i]:
            return False
        if parts[i]>=2:
            return True
        return all(n==1 for n in parts)
    if len(supp)==2:
        i,j=supp
        ti,tj=parts[i]-occ[i],parts[j]-occ[j]
        return (ti<=1 or occ[j]>=2) and (tj<=1 or occ[i]>=2)
    return False


def add(A,B):
    n=max(len(A),len(B)); C=[0]*n
    for i,a in enumerate(A): C[i]+=a
    for i,b in enumerate(B): C[i]+=b
    return C

def sub(A,B):
    n=max(len(A),len(B)); C=[0]*n
    for i,a in enumerate(A): C[i]+=a
    for i,b in enumerate(B): C[i]-=b
    return C

def mul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B): C[i+j]+=a*b
    return C

def mon(c,d):
    A=[0]*(d+1); A[d]=c; return A

def f(n):
    return [0]+[comb(n,k) for k in range(1,n+1)]
def h(n):
    A=[0]*(n+1)
    for k in range(1,max(1,n-1)):
        if k<=n-2: A[k]=comb(n,k)
    return A


def formula(parts):
    r=len(parts); N=sum(parts)
    fs=[f(n) for n in parts]
    # subsets meeting >= 3 parts
    allpoly=[comb(N,k) for k in range(N+1)]
    R=sub(allpoly,[1])
    for F in fs: R=sub(R,F)
    for i in range(r):
        for j in range(i+1,r): R=sub(R,mul(fs[i],fs[j]))
    # one-part secure sets
    U=[0]*(N+1)
    if all(n==1 for n in parts):
        U[1]=r
    else:
        for n in parts:
            if n>=2: U[n]+=1
    # secure sets meeting exactly two parts
    Q=[0]*(N+1)
    for i in range(r):
        for j in range(i+1,r):
            q=mul(fs[i],fs[j])
            q=sub(q, mon(parts[j],1) if False else [0])
            # bad: choose exactly one in j and leave >=2 outside i
            badA=mul(mon(parts[j],1),h(parts[i]))
            badB=mul(mon(parts[i],1),h(parts[j]))
            q=sub(q,badA); q=sub(q,badB)
            if parts[i]>=3 and parts[j]>=3:
                q=add(q,mon(parts[i]*parts[j],2))
            Q=add(Q,q)
    return add(add(R,U),Q)


def trim(A,N):
    return (A+[0]*(N+1-len(A)))[:N+1]

graph_types=subset_checks=coefficient_checks=classification_checks=0
max_order=10
for N in range(2,max_order+1):
    for parts in integer_partitions(N):
        graph_types+=1
        blocks,part,adj=build(parts)
        direct=[0]*(N+1)
        for mask in range(1<<N):
            S={v for v in range(N) if mask>>v&1}
            d=secure_direct(S,adj)
            s=structural(S,parts,blocks)
            subset_checks+=1; classification_checks+=1
            if d != s:
                raise AssertionError((parts,S,d,s))
            if d: direct[len(S)]+=1
        closed=trim(formula(parts),N)
        coefficient_checks += N+1
        if direct != closed:
            raise AssertionError((parts,direct,closed))
print(f'VERIFY_OK graph_types={graph_types} subsets={subset_checks} classification_checks={classification_checks} coefficient_checks={coefficient_checks} max_order={max_order}')
