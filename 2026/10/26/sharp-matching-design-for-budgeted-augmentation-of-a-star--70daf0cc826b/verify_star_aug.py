"""Finite numerical checks for a sharp star-augmentation coherence theorem.

The infinite-family proof is analytic; these checks only test examples.
Requires Python 3 and NumPy. Run: python verify_star_aug.py
"""
import itertools
import math
import numpy as np


def compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for x in range(1, total - parts + 2):
        for rest in compositions(total-x, parts-1):
            yield (x,) + rest


def trace_pseudoinverse(n, edge_weights):
    # Vertices are hub 0, leaves 1..n; base spoke conductance 1.
    mat = np.zeros((n+1, n+1), dtype=float)
    for j in range(1, n+1):
        mat[j,j] += 1
        mat[0,0] += 1
        mat[j,0] -= 1
        mat[0,j] -= 1
    for (a,b), weight in edge_weights:
        mat[a,a] += weight
        mat[b,b] += weight
        mat[a,b] -= weight
        mat[b,a] -= weight
    eigenvalues = np.linalg.eigvalsh(mat)
    assert abs(eigenvalues[0]) < 1e-8
    return sum(1/x for x in eigenvalues[1:])


def optimal_value(n,k,w):
    return n-1+1/(n+1)-2*w*k/(k+2*w)


def run():
    total_cases = 0
    strict_nonmatch = 0
    for n in range(2,8):
        for k in range(1, min(n//2,3)+1):
            edges = list(itertools.combinations(range(1,n+1),2))
            for budget_units in (k,k+2):
                W = budget_units / 2
                optimum = optimal_value(n,k,W)
                for subset in itertools.combinations(edges,k):
                    matching = len({v for edge in subset for v in edge}) == 2*k
                    for parts in compositions(budget_units,k):
                        weights = [((a,b),t/2) for (a,b),t in zip(subset,parts)]
                        observed = trace_pseudoinverse(n,weights)
                        assert observed >= optimum-2e-10, (n,k,W,subset,parts,observed,optimum)
                        # Uniformly strong concavity yields a certified nonnegative gap.
                        all_w = [t/2 for t in parts]
                        overlap = sum(all_w[i]*all_w[j] for i in range(k) for j in range(i+1,k) if set(subset[i]) & set(subset[j]))
                        numerator = 4*sum((t-W/k)**2 for t in all_w) + 2*overlap
                        guaranteed_gap = numerator/(1+2*W)**3
                        assert observed-optimum >= guaranteed_gap-2e-10, (n,k,W,subset,parts,observed,optimum,guaranteed_gap)
                        predicted_equality = matching and len(set(parts)) == 1
                        if predicted_equality:
                            assert math.isclose(observed,optimum,abs_tol=2e-10)
                        else:
                            assert observed > optimum+1e-10, (n,k,subset,parts)
                            strict_nonmatch += 1
                        total_cases += 1
    print(f"PASS: {total_cases} candidate supports and weight allocations checked; "
          f"{strict_nonmatch} strict non-optimal examples.")
    print("An example: 6 leaves, 3 disjoint unit-weight leaf links:",
          trace_pseudoinverse(6,[((1,2),1),((3,4),1),((5,6),1)]))

if __name__ == "__main__":
    run()
