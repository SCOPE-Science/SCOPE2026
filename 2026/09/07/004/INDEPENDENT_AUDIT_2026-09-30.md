# Independent audit — 2026-09-30

## Final claim assessed

The displayed 20-point subset of the 12-by-12 integer lattice has minimum doubled triangle area exactly 2 (so minimum area 1), with no collinear or unimodular triples and the stated small-determinant counts; its largest empty convex subset has size six.

## Correctness — PASS

Independent integer enumeration of all 1140 triples in the displayed coordinate list reproduced minimum doubled area 2, zero determinants 0 or 1, 34 triples of doubled area 2, 42 of doubled area 3, and maximum doubled area 100. A separate exact-orientation convex-hull enumeration found no empty convex 7-subset and verified the listed six-point empty convex witness. These checks establish the lower-bound configuration and the H=6 secondary claim without relying on the stochastic search history.

Evidence inspected:
- RESULT.md
- artifacts/S_star.txt
- artifacts/verify_S_star.py
- independent determinant and convex-hull enumeration

Residual risks:
- No upper bound for the lattice extremum is proved, and the stochastic failure to find doubled area at least three is not a nonexistence result.

## Originality — PASS

The no-three-in-line literature supplies 24-point 12-by-12 configurations but controls only zero area, while continuous Heilbronn literature optimizes a different unrestricted placement problem. Searches for the stronger determinant-at-least-two condition and the exact 20-point/12-by-12 parameters found no prior table or matching configuration. Published-record search likewise returned no duplicate.

Sources inspected:
- no-three-in-line problem literature and OEIS A272651/A000755
- Cohen-Pohoata-Zakharov, arXiv:2305.18253
- Friedman Heilbronn square tables

Residual risks:
- Computational geometry configurations are often circulated outside indexed papers; an unpublished or hobbyist table could contain an equivalent set.

## Scientific value — PASS

Eliminating both collinear and unimodular triples is the first quantized area threshold strictly stronger than no-three-in-line on an integer lattice. An explicit exactly verified 20-point witness is a meaningful finite benchmark even without an optimality proof, and the empty-convex-subset statistic adds a natural structural certificate.

Context checked:
- RESULT.md
- no-three-in-line and Heilbronn literature

Residual risks:
- The result is an existence benchmark, not an exact value of M(12,20), and does not improve the unrestricted continuous Heilbronn record.

## Outcome

All three acceptance axes pass for the final claim as stated. Conjectures, heuristic search observations, and explicitly excluded broader regimes remain outside the accepted claim.
