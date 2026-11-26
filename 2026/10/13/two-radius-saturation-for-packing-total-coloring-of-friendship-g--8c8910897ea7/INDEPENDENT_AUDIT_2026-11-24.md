# Independent mathematical audit

## correctness

PASS

In T(F_n), hub and spokes form a clique and are all within two steps of every element. The three peripheral elements of each triangle are a clique. Across distinct triangles, peripheral vertices are distance 2, while each rim edge is distance 3 from the other triangle's peripheral vertices and rim edge (via the endpoint formulas). Hence diameter is 2 at n=1 and 3 otherwise; maximum color-1 packing has n+1 elements, attained by hub plus all rims, and any radius-2 packing has at most n elements, attained by all rims. For n=1 only color 1 can repeat, giving 5. For n>=2, at q=0 count at most n+1 in color 1 and one in each other label, and realize equality. At q=1 the additional cap of n in color 2 gives 3n+2, realized by color 1 on s_1 and all b_i and color 2 on all rims. For q>=2, the 4n+1 hub, spokes and peripheral vertices are pairwise within two steps, so only color 1 can repeat on them and at least 3n+1 labels are needed. Keeping the q=1 color-1 set and using {a_1,r_2,...,r_n} and {a_2,r_1} for colors 2 and 3 attains that bound with the remaining labels singleton; this also works at n=2. The savings statement is for n>=2; all labels beyond 1 remain singleton at n=1. The frozen verify_friendship.py and verification_output.txt were inspected, not executed; they report finite BFS, construction checks, and packing-size search, ending ALL_CHECKS_PASS. The analytic argument proves all n,q, and the original attestation/audit/Lean fields were not_performed.

## originality

PASS

The general notion, its total-graph formulation, and the ordinary packing-total regime are established. The supported distinction is the exact friendship-graph classification, including the second radius-2 class giving exactly one additional saving and the obstruction to any further saving. The directly relevant founding preprint was accessible and its strongest related statements were checked.

## value

PASS

Friendship graphs are a natural diameter-three total-graph family, where the distinction between radius 2 and radius 3 has an exact operational effect. The theorem gives the full tradeoff: a first reusable radius-2 label saves n-1, a second saves only one, and an intrinsic diameter-two obstruction shows why no later label helps. The exact boundary and explicit optimal allocations provide a benchmark beyond the ordinary or no-reuse cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
