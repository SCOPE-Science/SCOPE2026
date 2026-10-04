from itertools import combinations


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(1, total - parts + 2):
        yield from compositions(total - x, parts - 1, prefix + (x,))


def graph(alpha, beta):
    p = len(alpha)
    V = []
    for i,a in enumerate(alpha,1):
        for q in range(a):
            V.append(('A',i,q))
    for j,b in enumerate(beta,1):
        for q in range(b):
            V.append(('B',j,q))
    ids = {v:t for t,v in enumerate(V)}
    N=[set() for _ in V]
    for i,a in enumerate(alpha,1):
        for qa in range(a):
            u=ids[('A',i,qa)]
            for j in range(1,i+1):
                for qb in range(beta[j-1]):
                    v=ids[('B',j,qb)]
                    N[u].add(v); N[v].add(u)
    return V,N


def kpds(N,S,k):
    seen=set(S)
    for v in list(S):
        seen.update(N[v])
    while True:
        add=set()
        for v in tuple(seen):
            w=N[v]-seen
            if 0 < len(w) <= k:
                add.update(w)
        if not add:
            return len(seen)==len(N)
        seen.update(add)


def predicted(alpha,beta,k):
    LA=max(tuple(alpha[:-1])+(alpha[-1]-1,))
    LB=max((beta[0]-1,)+tuple(beta[1:]))
    return 1 if min(LA,LB) <= k else 2

profiles=0
singleton_checks=0
extreme_pair_checks=0
for k in range(1,5):
    for p in range(1,6):
        for n in range(2*p,12):
            for parts in compositions(n,2*p):
                alpha,beta=parts[:p],parts[p:]
                V,N=graph(alpha,beta)
                actual1=False
                for v in range(n):
                    singleton_checks += 1
                    if kpds(N,[v],k):
                        actual1=True
                        break
                g=1 if actual1 else 2
                if g != predicted(alpha,beta,k):
                    raise AssertionError((k,alpha,beta,g,predicted(alpha,beta,k)))
                if not actual1:
                    a=next(i for i,v in enumerate(V) if v[:2]==('A',p))
                    b=next(i for i,v in enumerate(V) if v[:2]==('B',1))
                    extreme_pair_checks += 1
                    if not kpds(N,[a,b],k):
                        raise AssertionError(('extreme-pair',k,alpha,beta))
                profiles += 1
print(f'VERIFY_OK profiles={profiles} singleton_checks={singleton_checks} extreme_pair_checks={extreme_pair_checks} max_order=11 k_max=4')
