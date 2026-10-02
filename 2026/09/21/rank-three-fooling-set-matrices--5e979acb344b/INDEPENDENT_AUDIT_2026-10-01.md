# Mathematical audit — 2026-10-01

## Final claim assessed

Exact maximum size of rank-three fooling-set matrices

## Correctness — PASS

PASS on the repaired proof. The original result had a genuine gap before the projective-coordinate normalization: the tournament construction allowed both off-diagonal entries of a pair to vanish, so extra point-line incidences were not excluded. The repair supplies the missing lemma. In an order-seven rank-three equality case every compatible tournament is 3-regular; reversing a doubly-zero pair remains compatible but would create endpoint outdegrees 2 and 4, impossible. Hence every pair has exactly one zero direction, the seven point-line incidences are exactly the Fano plane, a non-block triple is noncollinear, and the determinant obstruction \(-2=0\) is valid. The general tournament bound and explicit order-six/order-seven constructions also check exactly.

## Originality — PASS

PASS to the best of current knowledge. Resultary search under fooling-set, rank-three, Fano and tournament terminology returned the assigned theorem as the only exact match. The complete accessible Friesen--Hamed--Lee--Theis preprint was retrieved; its introduction states the classical quadratic bound, the rank-three size-six seed, and asymptotically quadratic characteristic-dependent constructions, but not an exact rank-three upper theorem or Fano equality classification. The repaired no-double-zero step is part of the new upper-bound argument rather than a restatement of those constructions.

### equivalent_formulations

Searches: Resultary: rank three fooling set matrix exact maximum characteristic two Fano plane tournament; web: fooling-set rank 3 characteristic 2 Fano

Evidence: No earlier exact theorem matching \(f_{\mathbb F}(3)\) was located; the primary preprint discusses the size-six rank-three seed and asymptotic constructions.

Reasoning: Cross-free-matching and projective-incidence aliases were considered; the exact seven-vertex upper classification was not found in inspected sources.

### broader_coverage

Searches: Friesen--Hamed--Lee--Theis arXiv:1208.2920 complete ten-page preprint; Dietzfelbinger--Hromkovič--Schnitger quadratic rank bound

Evidence: The primary preprint proves asymptotic constructions and recalls \(n\le r^2\), but neither supplies the field-sensitive exact rank-three upper bound.

Reasoning: The repaired theorem sharpens broad asymptotic theory at a specific natural first low-rank frontier and is not mechanically implied by the quadratic bound.

### exact_database_or_table

Searches: Resultary exact low-rank fooling-set search

Evidence: No exact low-rank database or prior published table establishing the field-dependent optimum was found.

Reasoning: The result is an extremal theorem with a proof of completeness, not a finite lookup.

### claim_vs_prior_implication

Searches: arXiv:1208.2920 introduction and constructions; repaired tournament/Fano proof

Evidence: Known size-six and characteristic-two size-seven constructions give only lower bounds. The new compatible-tournament and exact-incidence argument supplies the missing upper bound.

Reasoning: The final theorem is not a corollary of the known constructions or the general quadratic inequality.

## Scientific value — PASS

PASS. Rank three is the first nontrivial exact low-rank case where known lower constructions differ by characteristic. Closing the extremal value, proving optimality of both known witnesses, and identifying exact Fano representability as the equality obstruction are natural structural results rather than a small table computation.

## Source inspections

- **Fooling sets and rank** — https://arxiv.org/abs/1208.2920. Material read: Complete ten-page preprint was retrieved; the introduction and construction context were inspected, including the classical quadratic bound, the rank-three size-six seed, and the positive-characteristic construction program. Assessment: CLOSEST_PRIMARY_SOURCE_NOT_EXACT_RANK_THREE_COVERAGE. Evidence: It gives asymptotic lower constructions and records the size-six rank-three seed, not the exact rank-three maximum or Fano upper obstruction.
- **A comparison of two lower-bound methods for communication complexity** — https://doi.org/10.1016/S0304-3975(96)00062-X. Material read: The established \(n\le r^2\) result as quoted and cross-checked in the later primary fooling-set paper. Assessment: BROADER_BUT_NOT_SHARP_LOW_RANK. Evidence: The quadratic inequality allows nine positions at rank three and does not determine the claimed optimum.

## Checked sources

- Complete assigned RESULT and status files and the full frozen/current Git tree.
- Exact construction artifacts for the rank-two, universal order-six and characteristic-two order-seven matrices.
- Independent proof reconstruction including the repaired no-double-zero lemma and Fano determinant.
- Resultary and primary literature searches.

## Limitations and residual risks

The theorem is exact only through rank three and does not classify all extremal matrices. The general \(2^r-1\) tournament bound is not asymptotically competitive with the classical quadratic bound.

- Older sign-pattern, minimum-rank, cross-free-matching or projective-incidence literature may contain the same seven-vertex classification under different terminology.

## Disposition

**repaired**
