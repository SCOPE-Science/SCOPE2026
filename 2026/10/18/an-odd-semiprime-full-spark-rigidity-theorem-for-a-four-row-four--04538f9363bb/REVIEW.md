# Scientific review: odd-semiprime four-row Fourier full-spark rigidity

## Correctness — PASS
The generalized Vandermonde identity reduces each maximal minor to its nonzero Vandermonde factor times a complete homogeneous symmetric polynomial of degree two. Linear disjointness of third- and \(p\)-th cyclotomic fields yields an exact coefficient criterion, including the normalization of the coefficient vector by its coordinate minimum. The ten-term length constraint then leaves precisely three arithmetic cases: \(p\ge11\), \(p=7\), and \(p=5\). The directly enumerated, elementary three-residue histograms eliminate the first two possibilities and force a single ternary residue class in the last. A fifth-root generating identity proves all fifteen converses. The first three Vandermonde rows prove exact rank three for exceptional minors. No probabilistic inference or finite extrapolation is used.

The standalone all-integer checker independently examines \(130521\) column sets across \(p=5,7,11,13\), with singularity counts \(15,0,0,0\) and no disagreement. The proof covers all primes \(p\ge5\); finite tests are reproducibility aids only.

## Originality — PASS, best knowledge
The nearest classical theorem is the prime-power Fourier-row full-spark equivalence of Alexeev, Cahill and Mixon (arXiv:1110.3548, Theorem 9). That theorem does not imply sufficiency for the squarefree composite orders \(3p\); the same paper documents insufficiency of divisor-uniformity for general composite orders. Garcia, Karaali and Katz (arXiv:1807.07648) prove prime-field symmetry-based nonvanishing results, not the present four-row/nonprincipal squarefree classification. Malikiosis and Oussa (arXiv:1909.06223) establish algebraic full-spark constructions and generic Schur-factor techniques, not the fixed cyclic root-of-unity classification here. Caragea and Lee (arXiv:2409.09793) address principal minors, not arbitrary four-element column sets with a prescribed row pattern.

Other relevant results treat the distinct row patterns \(\{0,1,2,4\}\) and \(\{0,1,3,4\}\), or the same row pattern at **prime-power** order. None of these conclusions implies the exact squarefree classification or its rank/count statement. A specialist prior equivalent in root-of-unity minor literature remains possible, so the review does not establish independent priority.

## Mathematical value — PASS
For composite Fourier groups, divisor-uniform row patterns are not automatically full spark. The theorem identifies a concrete, near-consecutive four-row family for which divisibility by three creates **no** additional maximal-minor losses, even at the potentially resonant first squarefree cases \(3\cdot5\) and \(3\cdot7\). The single order-five obstruction has an exact fifteen-set classification and sharp rank statement. This supplies a deterministic erasure-robust frame on infinitely many odd squarefree orders and a nontrivial boundary between the prime-power full-spark theorem and general composite counterexamples. It is not merely a rearrangement of the known prime-power result.

## Limits and closest literature
The theorem covers exactly \(N=3p\) with \(p\ge5\) prime and the four rows \(\{0,1,2,5\}\). It neither covers arbitrary Fourier row patterns nor proves a lower singular-value bound. The older equivalent-result risk is not eliminated by accessible bibliographic searches. All zero certificates are exact integer-arithmetic statements, not numerical tolerance tests.

Self-review: passed. Independent audit: not yet performed.
