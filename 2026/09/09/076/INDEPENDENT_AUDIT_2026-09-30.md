# Independent mathematical audit — SCOPE-20260909-076

Outcome: **REPAIRED**.

## Correctness
**PASS** — A fresh independent construction of the 9460-by-9453 interpolation matrix over F_251 at the first stated ten-point specialization was eliminated through all 9453 columns with no missing pivot, proving full column rank. A nonzero 9453-minor mod 251 is a nonzero integer minor, hence the specialized characteristic-zero system has h^0=0; upper semicontinuity then gives emptiness for general points. The auxiliary shifted C source has an out-of-bounds falling-factorial stride bug, so that secondary log is removed and the source is repaired; it is not needed for the proof.

## Originality
**PASS** — Ciliberto-Miranda prove expected dimension only for d/m at least 174/55, Dumnicki proves the homogeneous Harbourne-Hirschowitz statement for multiplicities at most 42, and Petrakiev proves emptiness only below 2280/721. The ratio 136/43 lies strictly between sqrt(10) and 174/55 and is not implied by those results. Targeted Resultary and literature searches found no prior resolution of this exact cell.

## Value
**PASS** — This is the first homogeneous multiplicity-43 cell immediately beyond the published m<=42 range and the unique degree at m=43 in the narrow classical ten-point interpolation strip. It is a natural boundary instance of a long-standing interpolation problem, not an arbitrary finite slice.

## Source inspections
- **Ciliberto-Miranda, Homogeneous interpolation on ten points, arXiv:0812.0032 / J. Algebraic Geometry 20 (2011)** — Primary abstract/full-text search inspected; theorem covers d/m >= 174/55. Consequence: does not cover 136/43, which is smaller
- **Dumnicki, Cutting diagram method for systems of plane curves with base points, Ann. Polon. Math. 90 (2007)** — Full theorem excerpt inspected. Theorem 32 proves the homogeneous Hirschowitz-Harbourne conjecture for multiplicities bounded by 42. Consequence: m=43 is immediately outside the proved finite range
- **Petrakiev, Homogeneous Interpolation and Some Continued Fractions, arXiv:1211.6380** — Primary abstract/full text inspected; emptiness is proved for d/m < 2280/721. Consequence: does not cover 136/43
- **Resultary mathematical research search** — Targeted searches for the exact system and stronger ten-point homogeneous interpolation results returned the present record but no prior exact resolution of L(136;43^10). Consequence: no database hit implying the exact cell; unsuccessful search alone is not used as novelty proof

## Residual risk
See the accompanying JSON audit for the explicit residual-risk record.
