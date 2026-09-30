# Independent audit — 2026-09-29

Record: `2026/09/11/057`  
Audited tree: `132c6a63fe51fee1beb69e40dcc34309e8e43356`  
Disposition: **repaired**

## Correctness

From the 14 listed facets I independently reconstructed the full subcomplex on vertices
`{0,1,6,7}`: its edges are exactly `01,07,16,67`, with missing diagonals
`06,17` and no 2-simplex, so it is an induced `C4`. The two missing-edge
Hochster classes therefore multiply to the nonzero reduced `H^0(C4)` class.
This alone rules out Golodness. Independently computing the automorphism
orbits of facets of the stacked 6-vertex sphere gives exactly three facet
orbits; checking all six gluing bijections for each orbit gives 18 complexes,
and every one contains an induced `C4`.

The scientific claim is correct. The staged repair changes the misleading title
"9-sphere" to the mathematically unambiguous "9-vertex 2-sphere" and softens a
categorical literature-absence statement. It also avoids relying on the historical
Berglund–Jöllenbeck implication that was later corrected; the nonzero product itself
already suffices.

## Originality

The hollow-cycle/non-Golod mechanism is standard. The contribution is an explicit
certificate for this named gluing family, not a new general Golodness criterion.

## Scientific value

The result is useful as a concrete falsification of a universal-vanishing target and
as a small reproducible example; its broader conceptual mechanism is known.

Sources: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/057 ; https://arxiv.org/abs/1506.08970 ; https://arxiv.org/abs/1511.04883
