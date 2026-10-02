# Independent mathematical audit — SCOPE-20260921-8a0ca297bd59
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
For every odd prime \(p\), the unordered equal-sum divisor bipartitions of \(2^a p\) are in bijection with positive odd \(r\) satisfying \(pr\le 2^{a+1}-1\), giving the exact count \(Z(2^a p)=\lfloor(2^{a+1}-1+p)/(2p)\rfloor\); the resulting fibers have explicit prime intervals, a limiting fixed-count distribution, and an aggregate identity with \(\omega\) over odd integers.

## Correctness
Status: **PASS**.

The signed-binary proof is complete. With \(M=2^{a+1}-1\), every sign choice on \(1,2,\ldots,2^a\) produces a unique odd integer in \([-M,M]\), because it equals twice a unique binary subset sum minus \(M\). An equal-sum divisor partition gives \(A+pB=0\); orienting the unordered partition by \(B>0\) makes it equivalent to one positive odd \(r=B\) with \(pr\le M\), and both sign vectors are then unique. Fresh brute-force subset enumeration for small \(a,p\) matched the formula in every tested case. The prime-interval fibers, prime-number-theorem limit, double-count identity with \(\omega\), and Mertens asymptotic follow algebraically from this bijection.

## Originality
Status: **PASS**.

Rao–Peng’s full primary paper gives the existence criterion \(p\le2^{a+1}-1\) for \(2^ap\) but does not count the partitions. Mahanta–Saikia–Yaqubi later characterize two-prime-support existence, again not multiplicity. OEIS A083206 gives a generic coefficient/subset-sum formula for the counting function and A083209 records the unique-partition slice; searches of those entries and the published-record corpus did not locate the arbitrary-\(k\) closed form, its bijective odd-parameter description, or the distribution identities. The generic coefficient formula still requires the special signed-binary uniqueness argument to collapse to this closed form, so it does not by itself state the audited parametric theorem.

### Equivalent formulations
- Search/source: Published-record semantic query: Zumkeller exact partition count \(2^a p\) equal-sum divisor bipartitions odd r.
- Search/source: K. P. S. Bhaskara Rao and Y. Peng, On Zumkeller Numbers, arXiv:0912.0052; Journal of Number Theory 133 (2013), 1135–1155.
- Evidence: No inspected exact source or database entry states the audited final claim in an equivalent formulation.
- Reasoning: Rao–Peng’s full primary paper gives the existence criterion \(p\le2^{a+1}-1\) for \(2^ap\) but does not count the partitions. Mahanta–Saikia–Yaqubi later characterize two-prime-support existence, again not multiplicity. OEIS A083206 gives a generic coefficient/subset-sum formula for the counting function and A083209 records the unique-partition slice; searches of those entries and the published-record corpus did not locate the arbitrary-\(k\) closed form, its bijective odd-parameter description, or the distribution identities. The generic coefficient formula still requires the special signed-binary uniqueness argument to collapse to this closed form, so it does not by itself state the audited parametric theorem.

### Broader coverage
- Search/source: K. P. S. Bhaskara Rao and Y. Peng, On Zumkeller Numbers, arXiv:0912.0052; Journal of Number Theory 133 (2013), 1135–1155.
- Search/source: P. J. Mahanta, M. P. Saikia, D. Yaqubi, Some properties of Zumkeller numbers and k-layered numbers, Journal of Number Theory 217 (2020), 218–236.
- Search/source: OEIS A083206, A083209, and A378652.
- Evidence: The closest broader sources cover ingredients, restricted parameter regimes, or background models but do not imply the audited final claim.
- Reasoning: Rao–Peng’s full primary paper gives the existence criterion \(p\le2^{a+1}-1\) for \(2^ap\) but does not count the partitions. Mahanta–Saikia–Yaqubi later characterize two-prime-support existence, again not multiplicity. OEIS A083206 gives a generic coefficient/subset-sum formula for the counting function and A083209 records the unique-partition slice; searches of those entries and the published-record corpus did not locate the arbitrary-\(k\) closed form, its bijective odd-parameter description, or the distribution identities. The generic coefficient formula still requires the special signed-binary uniqueness argument to collapse to this closed form, so it does not by itself state the audited parametric theorem.

### Exact database or table
- Search/source: Published-record semantic corpus
- Search/source: OEIS A083206/A083209/A378652
- Evidence: OEIS gives the generic counting formula and the unique-partition slice, not the arbitrary-count family theorem.
- Reasoning: Rao–Peng’s full primary paper gives the existence criterion \(p\le2^{a+1}-1\) for \(2^ap\) but does not count the partitions. Mahanta–Saikia–Yaqubi later characterize two-prime-support existence, again not multiplicity. OEIS A083206 gives a generic coefficient/subset-sum formula for the counting function and A083209 records the unique-partition slice; searches of those entries and the published-record corpus did not locate the arbitrary-\(k\) closed form, its bijective odd-parameter description, or the distribution identities. The generic coefficient formula still requires the special signed-binary uniqueness argument to collapse to this closed form, so it does not by itself state the audited parametric theorem.

### Claim versus prior implication
- Search/source: K. P. S. Bhaskara Rao and Y. Peng, On Zumkeller Numbers, arXiv:0912.0052; Journal of Number Theory 133 (2013), 1135–1155.
- Search/source: P. J. Mahanta, M. P. Saikia, D. Yaqubi, Some properties of Zumkeller numbers and k-layered numbers, Journal of Number Theory 217 (2020), 218–236.
- Evidence: The closest broader sources cover ingredients, restricted parameter regimes, or background models but do not imply the audited final claim.
- Reasoning: The inspected prior statements do not mechanically imply the audited final claim; the additional argument identified in the correctness reconstruction is substantive enough for this claim.

### Primary-source inspections
- **On Zumkeller Numbers** (arXiv:0912.0052): trigger — primary source of the known \(2^a p\) existence theorem; material read — full arXiv PDF, including the definition, generic partition criteria, and the stated sufficient/existence result for \(2^a p\); method — lawful arXiv full-text inspection with page screenshot; assessment — EXISTENCE_ONLY; evidence — The paper states that \(2^ap\) is Zumkeller when \(p\le2^{a+1}-1\) but does not enumerate equal-sum divisor bipartitions.
- **OEIS A083206** (https://oeis.org/A083206): trigger — canonical exact table/counting database for the invariant; material read — current sequence entry including comments, coefficient formula, examples, links, and cross-references; method — direct database inspection; assessment — GENERIC_COUNT_FORMULA_NOT_CLOSED_FAMILY_FORMULA; evidence — The entry gives the general coefficient/subset-sum count and small values, while A083209 records only the one-partition slice; no arbitrary-\(k\) formula for \(2^ap\) is stated.

## Scientific value
Status: **PASS**.

Exact partition multiplicity is the natural refinement of Zumkeller existence, and this family already has a published two-prime classification. The result completely determines every multiplicity fiber and yields a nontrivial prime-parameter limiting law and additive-function aggregate identity. That is a motivated exact invariant rather than an arbitrary finite recomputation.

## Checked sources
- K. P. S. Bhaskara Rao and Y. Peng, On Zumkeller Numbers, arXiv:0912.0052; Journal of Number Theory 133 (2013), 1135–1155.
- P. J. Mahanta, M. P. Saikia, D. Yaqubi, Some properties of Zumkeller numbers and k-layered numbers, Journal of Number Theory 217 (2020), 218–236.
- OEIS A083206, A083209, and A378652.
- Published-record semantic query: Zumkeller exact partition count \(2^a p\) equal-sum divisor bipartitions odd r.

## Limitations and residual risks
- The result is restricted to the exponent-one odd-prime family \(2^a p\).
- The unique-partition slice was already recorded in OEIS A083209 and is not treated as new.
- Older informal sequence notes or the Clark et al. announcement could contain an equivalent count formula; no such source was located.

This audit reports the mathematical assessment only. It is not a formal proof-assistant certificate or a guarantee of priority.
