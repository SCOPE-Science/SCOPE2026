from itertools import combinations


def partitions(n, max_part=None):
    if max_part is None or max_part > n:
        max_part = n
    if n == 0:
        yield ()
        return
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions(n-first, first):
            yield (first,) + rest


def build_graph(parts):
    labels=[]
    for i,s in enumerate(parts):
        labels += [i]*s
    n=len(labels)
    adj=[[False]*n for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if labels[u] != labels[v]:
                adj[u][v]=adj[v][u]=True
    return labels, adj


def geodesic_triples(adj):
    n=len(adj)
    triples=[]
    # A length-2 simple path (a,b,c) is geodesic iff a,c are distinct nonadjacent vertices.
    for a in range(n):
        for c in range(a+1,n):
            if adj[a][c]:
                continue
            for b in range(n):
                if b!=a and b!=c and adj[a][b] and adj[b][c]:
                    triples.append(frozenset((a,b,c)))
    return tuple(set(triples))


def is_k32_dominating(D, n, triples_by_v):
    D=set(D)
    for v in range(n):
        if v in D:
            continue
        if not any(len(T & D) >= 2 for T in triples_by_v[v]):
            return False
    return True


def predicted(parts):
    n=sum(parts); r=len(parts); t2=sum(s==2 for s in parts); t3=sum(s==3 for s in parts)
    if all(s==1 for s in parts):
        return n, 1
    if r==2 or t2:
        if r==2:
            count=parts[0]*parts[1] + t2
        else:
            count=t2
        return 2, count
    count=t3
    for s in parts:
        count += s*(s-1)//2 * (n-s)
    if r==3:
        prod=1
        for s in parts: prod*=s
        count += prod
    return 3, count


def brute(parts):
    labels,adj=build_graph(parts)
    n=len(labels)
    triples=geodesic_triples(adj)
    triples_by_v=[[] for _ in range(n)]
    for T in triples:
        for v in T:
            triples_by_v[v].append(T)
    checked=0
    for k in range(n+1):
        good=[]
        for D in combinations(range(n), k):
            checked += 1
            if is_k32_dominating(D,n,triples_by_v):
                good.append(D)
        if good:
            return k,len(good),checked
    raise AssertionError('no dominating set')


def main():
    types=0; candidate_subsets=0
    for n in range(2,10):
        for parts in partitions(n):
            if len(parts)<2: continue
            got_k,got_count,checked=brute(parts)
            want_k,want_count=predicted(parts)
            candidate_subsets += checked
            types += 1
            if (got_k,got_count)!=(want_k,want_count):
                raise AssertionError((parts,(got_k,got_count),(want_k,want_count)))
    print(f'ALL CHECKS PASSED; multipartite_types={types}; candidate_subsets={candidate_subsets}; max_order=9')

if __name__=='__main__':
    main()
