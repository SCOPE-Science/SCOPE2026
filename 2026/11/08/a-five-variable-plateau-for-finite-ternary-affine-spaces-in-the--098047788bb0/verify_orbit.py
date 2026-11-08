"""Exact orbit-bisimulation check for low-width ternary affine structures.

For a k-tuple, its affine dependence kernel is a subspace of F_3^(k-1)
(the last coefficient is minus the sum of the others). Every such kernel
with codimension at most d occurs in affine dimension d. Replacing tuple
coordinate i preserves precisely the subspace of dependencies with zero
coefficient at i. Atomic predicates are equality and a-b+c-e=0.
The code computes greatest bisimulation of the resulting finite orbit system.
"""
from itertools import product

def subspaces(n):
    vs=list(product(range(3),repeat=n))
    idx={v:i for i,v in enumerate(vs)}
    plus=[[idx[tuple((a+b)%3 for a,b in zip(x,y))] for y in vs] for x in vs]
    twice=[idx[tuple(2*x%3 for x in v)] for v in vs]
    seen={frozenset([0])}
    todo=[frozenset([0])]
    for S in todo:
        for x in range(3**n):
            if x not in S:
                T=frozenset(list(S)+[plus[a][x] for a in S]+[plus[a][twice[x]] for a in S])
                if T not in seen:
                    seen.add(T);todo.append(T)
    return vs,tuple(sorted(seen,key=lambda s:(len(s),tuple(sorted(s)))))

def classes(k,max_dim=5):
    n=k-1
    vs,spaces=subspaces(n)
    idx={v:i for i,v in enumerate(vs)}
    # For each coordinate i, intersect the affine dependence kernel
    # with the subspace of relations having coefficient zero at i.
    forget=[[frozenset(x for x in S if
             ((vs[x][i] if i<n else sum(vs[x]))%3)==0)
             for i in range(k)] for S in spaces]
    atom_vectors=set()
    for a,b,c,e in product(range(k),repeat=4):
        coeff=[0]*k
        for i,t in ((a,1),(b,-1),(c,1),(e,-1)):
            coeff[i]=(coeff[i]+t)%3
        atom_vectors.add(idx[tuple(coeff[:-1])])
    for a,b in product(range(k),repeat=2):
        coeff=[0]*k
        coeff[a]=(coeff[a]+1)%3
        coeff[b]=(coeff[b]-1)%3
        atom_vectors.add(idx[tuple(coeff[:-1])])
    atom_vectors=tuple(sorted(atom_vectors))
    signatures=[tuple(x in S for x in atom_vectors) for S in spaces]
    states=[(d,i) for d in range(max_dim+1)
            for i,S in enumerate(spaces) if 3**n//len(S) <= 3**d]
    ids={s:j for j,s in enumerate(states)}
    by_survivors={}
    for d,i in states:
        for coordinate in range(k):
            by_survivors.setdefault((d,coordinate,forget[i][coordinate]),[]).append(ids[(d,i)])
    successors=[tuple(by_survivors[(d,coordinate,forget[i][coordinate])]
                 for coordinate in range(k)) for d,i in states]
    def colorize(values):
        mapping={}
        return [mapping.setdefault(v,len(mapping)) for v in values]
    colors=colorize([signatures[i] for d,i in states])
    rounds=0
    while True:
        new=colorize([(colors[j],tuple(frozenset(colors[t] for t in row)
                           for row in successors[j])) for j in range(len(states))])
        if new==colors:break
        colors=new;rounds+=1
        assert rounds<=50
    top=spaces.index(frozenset(range(3**n)))
    profile=tuple(colors[ids[(d,top)]] for d in range(max_dim+1))
    threshold={2:1,3:2,4:3,5:3}[k]
    for d in range(max_dim+1):
        for e in range(max_dim+1):
            assert (profile[d]==profile[e]) == (min(d,threshold)==min(e,threshold)), (k,d,e)
    print(f'k={k} orbit_kernels={len(spaces)} states={len(states)} stable_classes={len(set(colors))} refinement_rounds={rounds}')
    print('  dimension_profile='+str(profile))
    print('  predicted_threshold='+str(threshold)+' PASS')

for width in (2,3,4,5):
    classes(width)
print('ORBIT_BISIMULATION=PASS')
