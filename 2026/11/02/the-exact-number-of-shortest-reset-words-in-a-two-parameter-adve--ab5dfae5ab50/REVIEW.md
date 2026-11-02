# Scientific review: shortest reset-word multiplicities

## Correctness: PASS
For each integer \(m\ge1\), \(k\ge2m-1\), the argument first proves that a shortest word requires and attains \(k+m\) successful kills and \(m\) high-to-low demotions. It then establishes both directions of a complete bijection with distinct labeled permutations satisfying \(C_h\prec H_h\) and \(D_{k-j+1}\prec C_{(j)}\), including the nonstandard no-low-token-at-state-\(k\) lemma at every cycle. Its bounds explicitly use \(k\ge2m-1\). Independent finite subset-DP and event-decoding checks are replayable, but the infinite assertion rests on the proof. Potential risk: unlike a brute-force enumeration, the argument depends critically on the precise cycle orientation and distinct indexed alphabet; both were compared against the original definition.

## Originality: PASS, with residual priority risk
The main source [1] already gives the reset-length behavior of the same family, which is not claimed as new. Its construction does not enumerate every length-minimizing word. Direct comparison with its section describing \(\mathcal L_m^k\), the standard shortest-word algorithms [2], and the factor-minimal language framework [3] found no equivalent event-order classification or factorial-over-six formula. Relevant indexed mathematical results count shortest words of other transition families; different automaton names alone are not the reason for distinction—the map structures and claimed implications differ. Risk remains of unpublished or unindexed equivalent enumeration. The related CiE 2026 proceedings treatment (DOI 10.1007/978-3-032-31348-5_24) could only be checked through metadata and abstract, not its full text.

## Value: PASS
For a published family with nontrivial reset-threshold behavior, an exact two-parameter count of shortest witnesses distinguishes reset length from geodesic multiplicity. The token-event bijection gives a reusable, structured explanation for the combinatorial \(6^{-m}\) factor and quantifies the factorial number of optimal alternatives. This is a natural complete invariant rather than an arbitrary finite slice or a one-off computation.

## Limitations and sources
The proof does not cover \(k<2m-1\) and does not enumerate longer reset words or game-winning strategies. Primary reference: [1] Anton E. Lipin and Mikhail V. Volkov, *Adversarial Synchronization* (2026), https://arxiv.org/abs/2601.18362 . Additional comparisons: [2] https://doi.org/10.1007/s10878-013-9682-0 , [3] https://arxiv.org/abs/1708.04864 . Only finite checks were independently implemented, not external mathematical validation.

Self-review: passed. Independent audit: not yet performed.
