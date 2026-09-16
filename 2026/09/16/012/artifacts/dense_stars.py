"""Exhaustive dense-core search, with vertex 0 fixed up to isomorphism.

Uses the link classification in Observation 5.2 of arXiv:2502.17686v1:
links have at most four edges, or are K4-minus-an-edge or K4.
Every emitted witness is independently verified using matching.
"""
from itertools import combinations
from small_stars import is_saturated
import argparse
import json


def search(n, deficit, top_degree):
    triples = list(combinations(range(n), 3))
    bits = {e: 1 << i for i, e in enumerate(triples)}
    incident = [sum(bit for e, bit in bits.items() if v in e) for v in range(n)]
    domains = []
    for v in range(n):
        pairs = list(combinations([x for x in range(n) if x != v], 2))
        pb = {p: bits[tuple(sorted((v,) + p))] for p in pairs}
        options = [sum(pb[p] for p in sub)
                   for k in range(5) for sub in combinations(pairs, k)]
        for four in combinations([x for x in range(n) if x != v], 4):
            six = [pb[p] for p in combinations(four, 2)]
            whole = sum(six)
            if top_degree >= 5:
                options.extend(whole ^ b for b in six)
            if top_degree == 6:
                options.append(whole)
        domains.append(options)
    initial = sum(bits[(0,) + p] for p in combinations(range(1, 5), 2)
                  if top_degree == 6 or p != (3, 4))
    target = 2 * n - deficit
    nodes = 0
    witnesses = []

    def visit(chosen, decided, pending, domains_left):
        nonlocal nodes
        nodes += 1
        if chosen.bit_count() > target:
            return
        filtered = {}
        maximum_sum = 0
        minimum_sum = 0
        for v in pending:
            fixed = decided & incident[v]
            value = chosen & incident[v]
            opts = [x for x in domains_left[v] if x & fixed == value]
            if not opts:
                return
            filtered[v] = opts
            degs = [x.bit_count() for x in opts]
            maximum_sum += max(degs)
            minimum_sum += min(degs)
        done_sum = sum((chosen & incident[v]).bit_count()
                       for v in range(n) if v not in pending)
        if done_sum + maximum_sum < 3 * target or done_sum + minimum_sum > 3 * target:
            return
        if not pending:
            edges = [e for e, b in bits.items() if chosen & b]
            if len(edges) == target and is_saturated(n, edges):
                witnesses.append(edges)
                print(json.dumps({"n": n, "deficit": deficit,
                                  "top_degree": top_degree, "witness": edges}), flush=True)
            return
        v = min(pending, key=lambda u: len(filtered[u]))
        rest = pending - {v}
        # Complete five-vertex components are excluded from the residual core.
        for option in filtered[v]:
            new = chosen | option
            complete_five = False
            if option.bit_count() == 6:
                support = {v}
                for e, b in bits.items():
                    if option & b:
                        support.update(e)
                if len(support) == 5:
                    complete_five = all(new & bits[e] for e in combinations(sorted(support), 3))
            if not complete_five:
                visit(new, decided | incident[v], rest, filtered)

    visit(initial, incident[0], set(range(1, n)), domains)
    return {"n": n, "deficit": deficit, "top_degree": top_degree,
            "nodes": nodes, "witnesses": len(witnesses)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("deficit", type=int)
    args = parser.parse_args()
    for degree in (5, 6):
        print(json.dumps(search(args.n, args.deficit, degree)), flush=True)
