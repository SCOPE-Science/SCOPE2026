#!/usr/bin/env python3
"""Standalone exact finite checks for sparse-approval SJR/SSJR claims.

No external libraries are required. All profile and committee enumerations are exact.
"""
from itertools import combinations, product
from collections import defaultdict


def raw_groups_sjr(approval, m, k, W):
    """Reference definition, enumerating all cohesive voter coalitions."""
    n = len(approval)
    for mask in range(1, 1 << n):
        if mask.bit_count() * k < n:
            continue
        common = (1 << m) - 1
        for i in range(n):
            if mask >> i & 1:
                common &= approval[i]
        if common and not (common & W):
            return False
    return True


def raw_groups_ssjr(approval, m, k, W):
    """Reference definition, enumerating all cohesive voter coalitions."""
    n = len(approval)
    for mask in range(1, 1 << n):
        if mask.bit_count() * k < n:
            continue
        common = (1 << m) - 1
        for i in range(n):
            if mask >> i & 1:
                common &= approval[i]
        if common:
            for i in range(n):
                if mask >> i & 1 and not (approval[i] & W):
                    return False
    return True


def sjr_component_formula(approval, m, k):
    """Compute the optimal number of satisfied cohesive candidates.

    Each approval set has size at most 2. Graph edges are the non-singleton
    intersections over supporters of cohesive candidates. Connected components
    are stars; select their centers in decreasing order of total requirements.
    """
    n = len(approval)
    parents = list(range(m))

    def find(a):
        while parents[a] != a:
            parents[a] = parents[parents[a]]
            a = parents[a]
        return a

    def union(a,b):
        a,b = find(a),find(b)
        if a != b:
            parents[a] = b

    needs = {}
    edges = set()
    for c in range(m):
        s = [A for A in approval if A & (1<<c)]
        if len(s)*k < n:
            continue
        intersection = (1<<m)-1
        for A in s:
            intersection &= A
        assert intersection & (1<<c)
        assert intersection.bit_count() <= 2
        needs[c] = intersection
        if intersection.bit_count()==2:
            d = (intersection ^ (1<<c)).bit_length()-1
            a,b = sorted((c,d))
            edges.add((a,b))
            union(c,d)

    # Every connected nontrivial component must have a common hub.
    neighbor = [set() for _ in range(m)]
    for a,b in edges:
        neighbor[a].add(b)
        neighbor[b].add(a)
    for component_root in {find(i) for i in range(m)}:
        verts = [i for i in range(m) if find(i)==component_root]
        if len(verts)>1:
            assert any(all(v==hub or v in neighbor[hub] for v in verts)
                       for hub in verts), (approval,m,k,verts)

    weights = defaultdict(int)
    for c in needs:
        weights[find(c)] += 1
    reps = {}
    for root in weights:
        requirements = [mask for c,mask in needs.items() if find(c)==root]
        vertices = [i for i in range(m) if find(i)==root]
        good = [v for v in vertices if all(mask & (1<<v) for mask in requirements)]
        assert good, (approval,m,k,root,requirements)
        reps[root]=good[0]
    highest=sorted(weights, key=lambda root:(-weights[root],root))[:k]
    W=sum(1<<reps[root] for root in highest)
    for v in range(m):
        if W.bit_count()==k:
            break
        if not (W & (1<<v)):
            W |= 1<<v
    assert W.bit_count()==k
    claimed=sum(weights[root] for root in highest)
    achieved=sum(bool(mask & W) for mask in needs.values())
    assert achieved==claimed, (approval,m,k,W,claimed,achieved)
    return claimed, len(needs)


def check_profiles(m, n):
    ballots = [sum(1<<x for x in S) for size in (1,2)
               for S in combinations(range(m),size)]
    committees = {k:[sum(1<<x for x in S) for S in combinations(range(m),k)]
                  for k in range(1,m+1)}
    profiles = 0
    committee_checks = 0
    for A in product(ballots,repeat=n):
        profiles += 1
        for k in range(1,m+1):
            actual = 0
            # An independent directly-computed score from full-supporter groups,
            # not the component construction.
            supporters = []
            for c in range(m):
                S = [a for a in A if a&(1<<c)]
                if len(S)*k < n:
                    continue
                intersection=(1<<m)-1
                for a in S:
                    intersection &= a
                supporters.append(intersection)
            for W in committees[k]:
                score = sum(bool(s&W) for s in supporters)
                if score>actual:
                    actual=score
                # Verify the full coalition definition on the first profiles,
                # over all k and all committees.
                if profiles<=min(25,len(ballots)**n):
                    assert (score==len(supporters)) == raw_groups_sjr(A,m,k,W)
                    committee_checks+=1
            predicted, total = sjr_component_formula(A,m,k)
            assert predicted==actual and total==len(supporters), (m,n,A,k,predicted,actual)
    return profiles,committee_checks


def cubic_examples():
    # Complete graph K4: minimum vertex cover size 3.
    vertices = list(range(4))
    examples = [('K4',4,list(combinations(vertices,2)),2),
                ('K4',4,list(combinations(vertices,2)),3)]
    # Cube Q3: bipartition is a vertex cover of size four.
    cube = [(x,y) for x in range(8) for y in range(x+1,8)
            if (x^y).bit_count()==1]
    examples.append(('Q3',8,cube,4))
    for name,m,edges,k in examples:
        assert len(edges)*2==3*m and m//2 <= k <m
        A = [1<<u | 1<<v for u,v in edges]
        assert all(sum(bool(x&(1<<c)) for x in A)*k >= len(A)
                   for c in range(m))
        possible_s = False
        possible_v = False
        for choose in combinations(range(m),k):
            W=sum(1<<x for x in choose)
            ssjr = raw_groups_ssjr(A,m,k,W)
            cover = all((1<<u | 1<<v)&W for u,v in edges)
            assert ssjr==cover
            possible_s |= ssjr
            possible_v |= cover
        assert possible_s==possible_v
        if name=='K4': assert possible_s==(k>=3)
        if name=='Q3': assert possible_s
    return len(examples)


def main():
    profile_count=0
    direct_group_checks=0
    for m in range(1,5):
        for n in range(1,5):
            p,d=check_profiles(m,n)
            profile_count+=p;direct_group_checks+=d
    for n in range(1,5):
        p,d=check_profiles(5,n)
        profile_count+=p;direct_group_checks+=d
    example_count=cubic_examples()
    print(f'PASS exhaustive_profiles={profile_count} independently_checked_committees={direct_group_checks} cubic_cases={example_count}')

if __name__=='__main__': main()
