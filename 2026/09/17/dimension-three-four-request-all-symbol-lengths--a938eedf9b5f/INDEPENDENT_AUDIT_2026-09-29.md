# Independent Audit — dimension-three-four-request-all-symbol-lengths--a938eedf9b5f

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `bfb52bc41afb31d5f313bf29fd4050f9bdc103e2`  
**Audited current source tree:** `bfb52bc41afb31d5f313bf29fd4050f9bdc103e2`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA. No intervening source change required a stale-source re-audit.

## Correctness — PASSED

PASS. The odd-characteristic lower bound is sound. A hypothetical rank-three length-seven 4-all-symbol PIR realization can be normalized to seven projectively distinct points: zero columns would delete to an impossible length six, and proportional columns can be independently rescaled without changing any subset span, contradicting the source's distinct-column lemma. For each selected point, one singleton recovery set leaves six coordinates for three disjoint non-singleton recovery sets, so the other six points are paired on three secants through it. Hence every secant meets the seven-point set in an odd number of points; a five-point secant is impossible, so the selected triples form the Steiner triple system STS(7), i.e. the Fano incidence structure. The displayed coordinate calculation then forces 1=-1, excluding odd characteristic. The source's length-eight construction supplies the matching upper bound. Independently, I exhaustively checked the displayed length-eight matrix for all 210 four-request multisets over each of F_3,F_5,F_7 and enumerated all 1,716 spanning seven-point subsets of PG(2,3), finding zero with the required local matching property.

## Originality — PASSED

PASS, TO THE BEST OF THE SEARCHED PUBLIC LITERATURE. Boruchovsky--Gruica--Niemann--Yaakobi's 2026 paper introduces the all-symbol framework, gives the odd-characteristic t=4 bounds and the even-characteristic exact cases, and states that exact values remain undetermined in general. Targeted searches for ASP(3,4,q), all-symbol/Fano formulations, and older disjoint-repair-group terminology did not locate the odd-characteristic dimension-three classification. The Fano representability obstruction itself is classical; the original part is the coding-theoretic reduction from an optimal length-seven all-symbol PIR matrix to Fano incidence.

## Scientific value — PASSED

PASS. The theorem closes the one-column odd-characteristic gap in the smallest unresolved dimension-three t=4 case and, together with the source's characteristic-two result, gives a complete characteristic-dependent classification for k=3. It is a concrete exact parameter result with a transparent finite-geometric obstruction.

## Independent checks

- reconstructed the projective-distinctness and recovery-set matching argument step by step
- checked the secant parity and five-point-line contradiction and the Fano coordinate obstruction
- independently enumerated all four-request multisets for the explicit length-eight construction over F_3,F_5,F_7
- independently enumerated all 1,716 spanning seven-subsets of PG(2,3), finding no admissible set
- checked the 2026 source's Lemma 22, Theorem 23, Proposition 24, and statement that exact t=4 values remain open in general
- verified the current main record tree exactly equals the assigned tree SHA and contains no 2026-09-29 independent-audit marker

## Limitations

- The finite computations are supplementary; the all-odd-prime-power conclusion depends on the general Fano representability proof, which was independently checked.
- Older locality/availability and one-step majority-logic literature remains a residual originality risk because of overlapping recovery-set language, but no prior exact ASP(3,4,q) classification was located.
- No claim of novelty is made for the classical fact that the Fano matroid is representable exactly in characteristic two.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/17/dimension-three-four-request-all-symbol-lengths--a938eedf9b5f
- https://arxiv.org/abs/2601.04041
- https://doi.org/10.4230/LIPIcs.APPROX-RANDOM.2019.38
- https://doi.org/10.1016/j.laa.2015.01.023
