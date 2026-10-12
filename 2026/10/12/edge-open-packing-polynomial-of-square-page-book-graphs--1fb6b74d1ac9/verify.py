from itertools import combinations
from collections import Counter
from math import comb


def book_edges(m):
    # vertices: x=0, y=1, page i has u_i=2+2*i, v_i=3+2*i
    edges=[(0,1)]
    names=['s']
    for i in range(m):
        u=2+2*i; v=3+2*i
        edges.extend([(0,u),(u,v),(v,1)])
        names.extend([f'L{i}',f'M{i}',f'R{i}'])
    return edges,names


def has_common_edge(e,f,edges):
    se=set(e); sf=set(f)
    for g in edges:
        if g==e or g==f:
            continue
        a,b=g
        if (a in se and b in sf) or (b in se and a in sf):
            return True
    return False


def is_eop(indices,edges):
    return all(not has_common_edge(edges[i],edges[j],edges)
               for i,j in combinations(indices,2))


def classified(indices,names,m):
    S={names[i] for i in indices}
    if 's' in S:
        if any(x.startswith('M') for x in S): return False
        L={x for x in S if x.startswith('L')}
        R={x for x in S if x.startswith('R')}
        return not (L and R)
    mids={x for x in S if x.startswith('M')}
    L={x for x in S if x.startswith('L')}
    R={x for x in S if x.startswith('R')}
    if not mids:
        return not (L and R)
    if len(mids)>=2:
        return not L and not R
    # exactly one middle edge M_i
    i=int(next(iter(mids))[1:])
    allowed={f'M{i}',f'L{i}',f'R{i}'}
    if not S <= allowed: return False
    return not (f'L{i}' in S and f'R{i}' in S)


def formula_counter(m):
    c=Counter()
    # (1+z)^m + 2((1+z)^m-1) + 2mz^2 + z(2(1+z)^m-1)
    for k in range(m+1):
        c[k] += 3*comb(m,k)
        c[k+1] += 2*comb(m,k)
    c[0] -= 2
    c[2] += 2*m
    c[1] -= 1
    return c

checked=0
print('VERIFY_OK')
for m in range(1,7):
    edges,names=book_edges(m)
    counts=Counter()
    good=[]
    for mask in range(1<<len(edges)):
        checked += 1
        I=[i for i in range(len(edges)) if (mask>>i)&1]
        direct=is_eop(I,edges)
        structural=classified(I,names,m)
        assert direct==structural,(m,[names[i] for i in I],direct,structural)
        if direct:
            counts[len(I)] += 1
            good.append(I)
    assert counts==formula_counter(m),(m,counts,formula_counter(m))
    rho=max(counts)
    assert rho==m+1
    maxima=sum(1 for I in good if len(I)==rho)
    assert maxima==(4 if m==1 else 2),(m,maxima)
    print(f'm={m}: rho_e^o={rho}, edge_open_packings={sum(counts.values())}, maximum_sets={maxima}')
print('edge_subsets_checked =',checked)
print('all sets matched the structural classification and polynomial')
