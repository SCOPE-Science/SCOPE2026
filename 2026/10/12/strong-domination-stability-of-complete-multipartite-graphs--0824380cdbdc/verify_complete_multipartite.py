from __future__ import annotations

import itertools
import math
from collections import Counter


def graph_from_parts(parts):
    vertices=[]
    part_of={}
    for i,n in enumerate(parts):
        for j in range(n):
            v=(i,j)
            vertices.append(v)
            part_of[v]=i
    adj={v:set() for v in vertices}
    for u,v in itertools.combinations(vertices,2):
        if part_of[u] != part_of[v]:
            adj[u].add(v)
            adj[v].add(u)
    return vertices, adj, part_of


def gamma_strong_bruteforce(parts):
    vertices, adj, _ = graph_from_parts(parts)
    degree={v:len(adj[v]) for v in vertices}
    for k in range(1,len(vertices)+1):
        for tup in itertools.combinations(vertices,k):
            D=set(tup)
            ok=True
            for v in vertices:
                if v in D:
                    continue
                if not any((u in adj[v]) and (degree[u] >= degree[v]) for u in D):
                    ok=False
                    break
            if ok:
                return k
    raise AssertionError("no strong dominating set found")


def gamma_formula(parts):
    a=sorted(x for x in parts if x>0)
    if len(a)==1:
        return a[0]
    s=a[0]
    q=a.count(s)
    if s==1:
        return 1
    if q==1:
        return s
    return 2


def stability_formula(parts):
    a=sorted(parts)
    s=a[0]
    q=a.count(s)
    if s==1:
        return q
    if s==3 and q>=2:
        return 2
    return 1


def deletion_profile(parts, deleted_vertices):
    vertices, _, part_of = graph_from_parts(parts)
    removed=set(deleted_vertices)
    counts=Counter(part_of[v] for i,v in enumerate(vertices) if i not in removed)
    return [counts[i] for i in range(len(parts)) if counts[i]>0]


def stability_bruteforce(parts):
    vertices, _, _ = graph_from_parts(parts)
    base=gamma_strong_bruteforce(parts)
    n=len(vertices)
    # Proper deletions only; the theorem excludes complete graphs and every
    # claimed optimum occurs strictly before all vertices are removed.
    for k in range(1,n):
        for deleted in itertools.combinations(range(n),k):
            profile=deletion_profile(parts, deleted)
            if not profile:
                continue
            if gamma_strong_bruteforce(profile) != base:
                return k
    return math.inf


def integer_partitions(n, minimum=1, prefix=()):
    if n==0:
        if len(prefix)>=2:
            yield prefix
        return
    for x in range(minimum,n+1):
        yield from integer_partitions(n-x,x,prefix+(x,))


def main():
    profiles=0
    gamma_checks=0
    stability_checks=0
    for order in range(2,9):
        for parts in integer_partitions(order):
            if all(x==1 for x in parts):
                # Complete graphs are outside the theorem's noncomplete domain.
                continue
            profiles += 1
            g_direct=gamma_strong_bruteforce(parts)
            g_formula=gamma_formula(parts)
            assert g_direct==g_formula, ("gamma",parts,g_direct,g_formula)
            gamma_checks += 1
            s_direct=stability_bruteforce(parts)
            s_formula=stability_formula(parts)
            assert s_direct==s_formula, ("stability",parts,s_direct,s_formula)
            stability_checks += 1
    print(
        "ALL CHECKS PASSED; "
        f"profiles={profiles}; gamma_checks={gamma_checks}; "
        f"stability_checks={stability_checks}; order_range=2..8"
    )


if __name__ == "__main__":
    main()
