from itertools import product
from math import comb


def compositions(n, r):
    if r == 1:
        if n >= 1:
            yield (n,)
        return
    for first in range(1, n-r+2):
        for rest in compositions(n-first, r-1):
            yield (first,) + rest


def build_graph(parts):
    cls=[]
    for i,n in enumerate(parts):
        cls += [i]*n
    N=len(cls)
    adj=[set() for _ in range(N)]
    for u in range(N):
        for v in range(u+1,N):
            if cls[u] != cls[v]:
                adj[u].add(v); adj[v].add(u)
    return cls, adj


def literal_k_forcing(adj, mask, k):
    N=len(adj)
    blue={v for v in range(N) if (mask>>v)&1}
    while len(blue)<N:
        forced=set()
        for v in blue:
            white_neighbors=[u for u in adj[v] if u not in blue]
            if 1 <= len(white_neighbors) <= k:
                forced.update(white_neighbors)
        if not forced:
            return False
        blue.update(forced)
    return True


def theorem_criterion(parts, cls, mask, k):
    N=len(cls)
    r=len(parts)
    w=[0]*r
    for v,i in enumerate(cls):
        if not ((mask>>v)&1):
            w[i]+=1
    W=sum(w)
    if W==0:
        return True
    for i,n_i in enumerate(parts):
        blue_i=n_i-w[i]
        if blue_i>0 and 1 <= W-w[i] <= k and w[i] <= k:
            return True
    return False


def theorem_minimum(parts, k):
    N=sum(parts)
    M=max(min(k,n_i-1)+min(k,N-n_i) for n_i in parts)
    return N-M, M


def theorem_minimum_count(parts, k):
    N=sum(parts)
    _,M=theorem_minimum(parts,k)
    a=[min(k,n_i-1) for n_i in parts]
    c=[min(k,N-n_i) for n_i in parts]
    I=[i for i in range(len(parts)) if a[i]+c[i]==M]
    total=0
    for sel in range(1,1<<len(I)):
        J=[I[t] for t in range(len(I)) if (sel>>t)&1]
        top=N-sum(parts[i] for i in J)
        bot=M-sum(a[i] for i in J)
        term=1
        for i in J:
            term*=comb(parts[i],a[i])
        term*=comb(top,bot) if 0<=bot<=top else 0
        total += term if len(J)%2 else -term
    return total


def main():
    profiles=0
    parameter_checks=0
    subset_checks=0
    count_checks=0
    for N in range(2,10):
        for r in range(2,N+1):
            for parts in compositions(N,r):
                profiles += 1
                cls,adj=build_graph(parts)
                for k in range(1,min(4,N)+1):
                    parameter_checks += 1
                    forcing_sizes=[]
                    minimum_count=0
                    for mask in range(1<<N):
                        literal=literal_k_forcing(adj,mask,k)
                        predicted=theorem_criterion(parts,cls,mask,k)
                        subset_checks += 1
                        if literal != predicted:
                            raise AssertionError((parts,k,mask,literal,predicted))
                        if literal:
                            forcing_sizes.append(mask.bit_count())
                    F=min(forcing_sizes)
                    predicted_F,_=theorem_minimum(parts,k)
                    if F != predicted_F:
                        raise AssertionError(('minimum',parts,k,F,predicted_F))
                    for mask in range(1<<N):
                        if mask.bit_count()==F and literal_k_forcing(adj,mask,k):
                            minimum_count += 1
                    predicted_count=theorem_minimum_count(parts,k)
                    count_checks += 1
                    if minimum_count != predicted_count:
                        raise AssertionError(('count',parts,k,minimum_count,predicted_count))
    print(f'VERIFY_OK profiles={profiles} parameter_checks={parameter_checks} subset_checks={subset_checks} count_checks={count_checks} max_order=9 k_max=4')

if __name__=='__main__':
    main()
