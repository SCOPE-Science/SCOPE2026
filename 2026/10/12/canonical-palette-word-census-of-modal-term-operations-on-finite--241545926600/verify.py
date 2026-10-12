#!/usr/bin/env python3
"""Exact tests of modal types and term-operation counts on finite cluster chains."""
from itertools import product, combinations


def reduced(palettes):
    out = ()
    for current in reversed(palettes):
        current = frozenset(current)
        if not out or not current.issubset(out[0]):
            out = (current,) + out
    return out


def rooted_types_from_colorings(sizes, q):
    out = set()
    n = sum(sizes)
    for assignment in product(range(q), repeat=n):
        supports = []
        k = 0
        for a in sizes:
            supports.append(frozenset(assignment[k:k+a]))
            k += a
        for i in range(len(sizes)):
            word = reduced(supports[i:])
            for c in supports[i]:
                out.add((c, word))
    return out


def eligible_types(sizes, q):
    h = len(sizes)
    palettes = [frozenset(c) for m in range(1, q+1)
                for c in combinations(range(q), m)]
    out = set()
    for t in range(1, h+1):
        for positions in combinations(range(h-1), t-1):
            locations = positions + (h-1,)
            allowed = [[a for a in palettes if len(a) <= sizes[i]]
                       for i in locations]
            for word in product(*allowed):
                if all(not word[i].issubset(word[i+1])
                       for i in range(t-1)):
                    for c in word[0]:
                        out.add((c, word))
    return out


def bisimulation_partition_all(sizes, q):
    """Build ONE disjoint union of all valuations; independently refine types."""
    n = sum(sizes)
    levels = []
    for i, a in enumerate(sizes):
        levels.extend([i]*a)
    valuations = list(product(range(q), repeat=n))
    vertices = [(v, w) for v in range(len(valuations)) for w in range(n)]
    c = [valuations[v][w] for v,w in vertices]
    successors = []
    for v, w in vertices:
        successors.append([v*n+j for j in range(n) if levels[j]>=levels[w]])
    part = c
    for _ in range(2*n+3):
        signatures = [(c[z],frozenset(part[j] for j in neighbors))
                      for z,neighbors in enumerate(successors)]
        names = {x:i for i,x in enumerate(dict.fromkeys(signatures))}
        next_part = [names[x] for x in signatures]
        stable = (len(set(next_part)) == len(set(part)))
        part = next_part
        if stable: break
    else:
        raise AssertionError('finite modal refinement did not stabilize')
    assoc = {}
    reverse = {}
    for index,(v,w) in enumerate(vertices):
        colors = valuations[v]
        supports = []
        k = 0
        for a in sizes:
            supports.append(frozenset(colors[k:k+a]))
            k += a
        typ = (colors[w], reduced(supports[levels[w]:]))
        p = part[index]
        if p in assoc: assert assoc[p] == typ
        else: assoc[p] = typ
        if typ in reverse: assert reverse[typ] == p
        else: reverse[typ] = p
    return len(assoc),len(vertices)


def modal_closure_count(sizes, r):
    """Directly enumerate full truth tables of Boolean/modal terms."""
    n=sum(sizes)
    levels=[]
    for i,a in enumerate(sizes):levels.extend([i]*a)
    q=2**r
    vals=list(product(range(q),repeat=n))
    assignments=len(vals)
    width=assignments*n
    universe=(1<<width)-1
    gens=[]
    for bit in range(r):
        x=0
        for v,colors in enumerate(vals):
            for w,col in enumerate(colors):
                if (col>>bit)&1:x|=1<<(v*n+w)
        gens.append(x)
    successors=[tuple(j for j in range(n) if levels[j]>=levels[w]) for w in range(n)]
    def diamond(x):
        result=0
        for v in range(assignments):
            block=(x>>(v*n))&((1<<n)-1)
            for w in range(n):
                if any((block>>j)&1 for j in successors[w]):
                    result |= 1<<(v*n+w)
        return result
    seen=set([0,universe]+gens)
    while True:
        before=len(seen)
        current=list(seen)
        for x in current:
            seen.add(universe ^ x)
            seen.add(diamond(x))
        current=list(seen)
        for i,x in enumerate(current):
            for y in current[i:]:seen.add(x&y)
        if len(seen)==before:return len(seen)
        assert len(seen)<=8192, 'test deliberately kept small'


def main():
    cases=[(1,),(2,),(3,),(1,1),(1,2),(2,1),(2,2),
           (1,1,1),(1,2,1),(2,1,1),(1,1,2),(2,2,1),
           (1,1,1,1),(3,1,2)]
    language_checks=0
    combined_refinements=0
    total_refinement_worlds=0
    closures=0
    for sizes in cases:
        for q in (1,2,3):
            if q**sum(sizes)>1000:continue
            expected=eligible_types(sizes,q)
            actual=rooted_types_from_colorings(sizes,q)
            assert actual==expected,(sizes,q,actual^expected)
            language_checks+=1
            if q>1 and q**sum(sizes)*sum(sizes)<=3200:
                count,num_worlds=bisimulation_partition_all(sizes,q)
                assert count==len(expected),(sizes,q,count,len(expected))
                combined_refinements+=1
                total_refinement_worlds+=num_worlds
    for sizes in [(1,),(2,),(3,),(1,1),(1,2),(2,1),(1,1,1),(1,1,1,1)]:
        r=1
        e=len(eligible_types(sizes,2**r))
        count=modal_closure_count(sizes,r)
        assert count==2**e,(sizes,count,2**e)
        closures+=1
    for q in range(1,6):
        for h in range(1,8):
            e=len(eligible_types((1,)*h,q)) if h<=4 and q<=3 else None
            formula=q*sum((q-1)**j for j in range(h))
            if e is not None:assert e==formula
    assert len(eligible_types((2,1),2))==8
    assert len(eligible_types((1,2),2))==6
    print('VERIFY_OK language_cases',language_checks,
          'cross_model_bisimulations',combined_refinements,
          'bisimulation_worlds',total_refinement_worlds,
          'direct_term_closures',closures,
          'orientation_example', (2**8,2**6))

if __name__=='__main__':main()
