# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.** The lower-bound proof was checked at each structural step.

1. Under a hypothetical odd-characteristic length-seven realization, the known value `ASP(2,4,q)=6` and the source paper's distinct-column lemma apply.
2. Independent nonzero column scalings preserve all relevant subset spans, so repeated projective points would produce repeated columns after rescaling; zero columns can be deleted. Hence the seven columns give seven distinct points of `PG(2,q)`.
3. For each selected point, one singleton recovery set leaves six coordinates for three disjoint non-singleton recovery sets. Therefore they are three pairs partitioning the other six points, and each pair is collinear with the requested point.
4. This forces every secant to contain an odd number of selected points. A five-point secant gives an immediate contradiction using the two off-line points, so every pair lies in a unique selected triple. The seven triples form the Fano Steiner triple system.
5. The coordinate calculation in `RESULT.md` shows directly that realizing these incidences forces `1=-1`, hence characteristic two.
6. The source paper's length-eight construction supplies the matching odd-characteristic upper bound.

As finite sanity checks, `artifacts/verify_small_fields.py` exhaustively verifies the explicit length-eight batch matrix for every four-request multiset over the prime fields of orders 3, 5 and 7, and enumerates all spanning seven-point subsets of `PG(2,3)`, finding none with the matching property required of a length-seven realization. These checks are supplementary rather than part of the general proof.

## Originality

**PASS, to the best of our knowledge.** The 2026 source paper states the odd-characteristic `k=3,t=4` bounds as `7 <= ASP <= ASB <= 8`, proves the value 7 for even characteristic, and explicitly identifies exact `t=4` values and alphabet dependence as open directions. Searches under the exact `ASP(3,4,q)` and `ASB(3,4,q)` notation, all-symbol PIR/batch terminology, disjoint-repair-group terminology, and Fano/projective-geometry formulations did not locate a prior exact odd-characteristic value.

The Fano representability obstruction is classical and is not claimed as new. The originality claim is specifically the coding-theoretic reduction from a hypothetical optimal length-seven all-symbol PIR code to Fano incidence and the resulting exact odd-characteristic value.

A residual risk remains in older literature on disjoint repair groups, locality/availability, and one-step majority-logic decoding, because the all-symbol PIR notion overlaps those frameworks. The relevant modern DRGP paper by Li and Wootters was inspected and does not state this small-parameter classification. No inaccessible paper was identified whose available metadata or theorem statements gave concrete evidence that the exact result is already known.

## Value

**PASS.** The theorem closes the smallest unresolved odd-characteristic case left by a recent paper, converts a one-column uncertainty into an exact value, and together with the source paper's even-characteristic result gives a complete dimension-three classification. It also demonstrates an explicit characteristic dependence in the minimum all-symbol code length, directly addressing an open direction highlighted by the source paper.

## Limitations

The review is not independent validation or peer review. Originality is reported to the best of our knowledge. The finite verification artifact covers selected prime fields only; the proof, not the computation, establishes the result for all odd prime powers.
