# Independent audit — 2026-09-29

Record: `2026/09/11/083`  
Audited tree: `3dfbbbce9ab6d026446a43b413b3636489fd4c5e`  
Disposition: **repaired**

## Correctness

Independent reconstruction from the filed 65 bipartitions gives N=208, 3851 edges, 4916 triangles, zero K4s, and zero internal edges among all 595 pairs of the explicit 35-vertex witness. Thus alpha>=35>26=N/8 is certified. The research result survives; the staged SLOGAN removes the unverified six-extra-seed typicality inference.

## Originality

The Mattheus-Verstraete construction is asymptotic and its Section-3 pseudorandomness theorem assumes q>=2^40; it does not determine this seeded q=4 instance. No exact published alpha evaluation for this filed instance was located.

## Scientific value

The explicit 35-set rigorously refutes the proposed upper side for the q=4 seeded Section-3 instance and calibrates how far the finite instance can be from the large-q pseudorandom regime.

## Limitations

- Only alpha>=35 is certified; exact alpha is not determined.
- The statement applies to seed 20260911, not all random instances.
- The filed graph is K4-free but not triangle-free; it has 4916 triangles.
- The six-extra-seed typicality sentence was not independently replayed and is removed from the staged slogan.

## Sources

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/083
- https://arxiv.org/abs/2306.04007
