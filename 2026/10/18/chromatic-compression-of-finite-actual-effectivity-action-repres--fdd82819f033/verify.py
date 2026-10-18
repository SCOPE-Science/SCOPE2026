"""Finite computational checks for chromatic compression of actual-effectivity frames.

Only the Python standard library is required.  Run with python verify.py.
"""
from itertools import product, combinations
from random import Random


def nonempty_subsets(n):
    return tuple(frozenset(i for i in range(n) if mask >> i & 1)
                 for mask in range(1, 1 << n))


def neighborhood_families(n):
    subs = nonempty_subsets(n)
    for mask in range(1, 1 << len(subs)):
        yield tuple(subs[j] for j in range(len(subs)) if mask >> j & 1)


def admissible(families):
    unions = [frozenset().union(*family) for family in families]
    if len(set(unions)) != 1:
        return False
    return all(set.intersection(*map(set, choice)) for choice in product(*families))


def conflict_graph(families):
    colorsets = tuple(set.intersection(*map(set, choice)) for choice in product(*families))
    vertices = sorted(set().union(*families[0]))
    edges = {frozenset((u,v)) for I in colorsets for u,v in combinations(sorted(I), 2)}
    return vertices,edges


def chromatic_coloring(vertices, edges):
    # Exhaustive proper coloring, lexicographic and minimal palette.
    for d in range(1,len(vertices)+1):
        for t in product(range(d),repeat=len(vertices)):
            c=dict(zip(vertices,t))
            if all(c[u]!=c[v] for u,v in (tuple(e) for e in edges)):
                return c,d
    raise AssertionError('nonempty graph should admit coloring')


def residue_signature(labels, multiplicities):
    p=max(range(len(multiplicities)),key=lambda i:multiplicities[i])
    return tuple((labels[j]-labels[p])%multiplicities[j]
                 for j in range(len(labels)) if j!=p)


def construct_and_check(families, multiplicities):
    assert admissible(families)
    vertices,edges=conflict_graph(families)
    c,d=chromatic_coloring(vertices,edges)
    assert all(__import__('math').prod(multiplicities[j] for j in range(len(families)) if j!=i)>=d
               for i in range(len(families)))
    p=max(range(len(multiplicities)), key=lambda i:multiplicities[i])
    all_signatures=list(product(*(range(multiplicities[j]) for j in range(len(families)) if j!=p)))
    mapcolor={sig:i%d for i,sig in enumerate(all_signatures)}
    assert set(mapcolor.values())==set(range(d))
    A=[[(S,t) for S in family for t in range(b)] for family,b in zip(families,multiplicities)]
    action_outputs={a:set() for i, actions in enumerate(A) for a in [(i,j) for j in range(len(actions))]}
    for indices in product(*(range(len(actions)) for actions in A)):
        chosen=[A[i][z] for i,z in enumerate(indices)]
        I=set.intersection(*(set(S) for S,_ in chosen))
        assert I
        sig=residue_signature([t for _,t in chosen],multiplicities)
        wanted=mapcolor[sig]
        suitable=[u for u in I if c[u]==wanted]
        assert len(suitable)<=1
        out=suitable[0] if suitable else min(I)
        for i,z in enumerate(indices):action_outputs[(i,z)].add(out)
    for i,actions in enumerate(A):
        for z,(S,_) in enumerate(actions):
            if action_outputs[(i,z)] != set(S):
                raise AssertionError(('wrong output set',families,multiplicities,i,z,S,action_outputs[(i,z)]))
    return d


def main():
    assert construct_and_check(((frozenset({0,1}),),(frozenset({0,1}),)),(2,2))==2
    for n in (2,3,4,5):
        families=tuple(frozenset({0,i}) for i in range(1,n))
        assert construct_and_check((families,families),(2,2))==2
    # Unbounded reachable range, but every joint neighborhood intersection is a singleton.
    for n in range(1,7):
        allout=frozenset(range(n))
        fam=((allout,),tuple(frozenset({i}) for i in range(n)))
        assert construct_and_check(fam,(1,1))==1
    for n in (2,3,4):
        whole=frozenset(range(n))
        assert construct_and_check(((whole,),(whole,),(whole,)),(1,n,n))==n
        assert construct_and_check(((whole,),(whole,),(whole,)),(n,1,n))==n
    triple_star=tuple(frozenset({0,i}) for i in (1,2,3))
    assert construct_and_check((triple_star,)*3,(1,2,2))==2
    count=0
    F=list(neighborhood_families(3))
    for f1 in F:
        for f2 in F:
            fam=(f1,f2)
            if admissible(fam):
                d=construct_and_check(fam,(3,3))
                count+=1
    print('ALL_TWO_AGENT_THREE_OUTCOME_FRAMES_OK',count)
    rng=Random(873219)
    sample=0
    # Three agents and asymmetric action multiplicities, including singleton coordinates.
    for _ in range(1000):
        fam=tuple(rng.choice(F) for i in range(3))
        if admissible(fam):
            c,d=chromatic_coloring(*conflict_graph(fam))
            for b in ((d,d,d),(1,d,d),(d,1,d),(d,d,1)):
                construct_and_check(fam,b)
            sample+=1
    assert sample>0
    print('THREE_AGENT_ASYMMETRIC_SAMPLES_OK',sample)
    print('CHROMATIC_EFFECTIVITY_COMPRESSION_OK')

if __name__=='__main__':main()
