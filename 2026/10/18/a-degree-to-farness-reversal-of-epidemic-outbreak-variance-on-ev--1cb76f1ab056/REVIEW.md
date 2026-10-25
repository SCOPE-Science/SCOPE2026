# Independent mathematical audit

## correctness

PASS

Percolation component of seed is exactly the one-generation epidemic set on a tree. At p near 0 only one open incident edge contributes to Var at first order, giving deg(v)p. At q=1-p near 0 a single closed edge e removes s_e(v) vertices, giving Var=q sum_e s_e(v)^2+O(q^2). Edge-separation double-counting proves sum_e s_e(v)^2=nD_T(v)-W(T); finite-tree uniformity in root holds. For every internal vertex a branch size b<n/2 exists and movement into that branch increases farness by n-2b; hence farness maximizers are leaves. Maximum-degree vertices are internal for n>=3. Independent exact percolation enumeration of P3 reproduces center-minus-leaf p(p-1)(p^2+3p-1). Recomputed edge identity and leaf farness maximizers for all unlabeled trees on 3..9 vertices; these finite checks corroborate the general argument.

## originality

PASS

Percolation coupling and epidemic source selection are established; searches did not find a result implying the two opposite universal variance-optimal source rankings and the farness/Wiener leading coefficient for all finite contact trees.

## value

PASS

A universal reversal of variance-optimal seeding location for every finite tree, tied to two distinct graph invariants and a sharp minimal example, is a structural epidemic/network result; expectation-only source selection would not answer it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
