# Independent mathematical audit

## correctness

PASS

The square-one equation for a partial bijection forces its image to equal its domain, so the calculation is on automorphism groups of induced subgraphs, not on partial isometries. On r ordered runs, a fixed component admits one orientation at length 1 and two at larger lengths. An exchanged pair must have equal lengths and has one or two choices for the first isomorphism, the second being its inverse. These give A and B with the indicated exponents. Choosing j disjoint exchanged pairs gives the coefficient in J_r; placing the runs after reserving r−1 mandatory gaps gives the binomial factor. The empty map contributes 1. An independent bounded check over 125,672 subset/permutation candidates verified all coefficients for 1≤n≤8; replay: python3 /workspace/branches/fe709d21-dd54-4146-a3d8-e3d9776a4775/check_profiles.py. The asymptotics are proved separately: for m=ceil(n/2), alternating vertices give lower bounds i_m and m! for U_n and T_n, respectively; counting subsets or ordered subset pairs and allowing all component permutations with at most two choices per component gives upper bounds 2^(n+m)i_m and 4^n 2^m m!. Here i_m is the symmetric-group involution count, with log i_m=(m/2)log m+O(m) by its pairing sum. A rank deviation forces r≤(1/2−ε)n+1 via r≤min(k,n−k+1); the same counting bound with this cap proves the domain tail, and the component lower tail follows directly. The component upper tail is eventually empty for each fixed ε because of the deterministic cap; no finer fluctuation law is verified.

## originality

PASS

The supported distinct contribution is the rank series for square-one partial automorphisms of the undirected path and their logarithmic abundance and domain/component concentration. Total path-monoid enumeration and the component-wreath-product method are not new. The closest prior fixed-point/two-cycle enumeration is for alternating fence posets and does not give these path-graph coefficients or the square-one concentration. This is not an assertion of absolute priority.

## value

PASS

The square-one locus is a natural subset of this inverse monoid. The rank profile distinguishes it from ordinary partial automorphisms; the same analysis quantifies the rarity of square-one maps among all maps and shows why their domains must be near half-full and mostly separated into runs. This is more than evaluating a usual involution polynomial on a small graph. The total-monoid scale on its own is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
