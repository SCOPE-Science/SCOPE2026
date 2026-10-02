# Independent mathematical audit — SCOPE-20260921-f7e2a68c2439
Audit date: 2026-10-01 (UTC) UTC.
Disposition: **passed**.

## Final claim
For positive definite \(2\times2\) \(A\), invertible Hermitian \(2\times2\) \(B\), and real exponents \(k,p\), the determinant gap \(\det(A^k+|AB|^p)-\det(A^k+|BA|^p)\) has the sign of \(kp\) when \(kp\ne0\) and \(A,B\) do not commute, with equality exactly at the stated zero-exponent or commuting boundary; the source gives an explicit divided-difference formula for the gap.

## Correctness
Status: **PASS**.

After unitary diagonalization \(A=\operatorname{diag}(a,b)\), the positive matrices \(X=BA^2B\) and \(Y=AB^2A\) are respectively \((AB)^*(AB)\) and \((AB)(AB)^*\), so they have the same two eigenvalues. In dimension two, \(T^{p/2}=\alpha_pT+\beta_pI\) for either matrix with the same divided difference \(\alpha_p\). A direct determinant expansion then gives exactly \(\alpha_p|z|^2(b^2-a^2)(b^k-a^k)\). Fresh numerical checks on noncommuting Hermitian examples with positive and negative exponents reproduced both the formula and the sign law to floating-point precision. The equality analysis also closes: spectral degeneracy together with the explicit \(X-Y\) formula forces commutation unless \(A\) is scalar.

## Originality
Status: **PASS**.

The primary determinant literature proves the \(k=2\) Hermitian inequality and several restricted exponent ranges. Ghabries’s 2022 thesis treats these questions and leaves the broader comparison conjectural, while the 2026 normal-matrix log-majorization extension proves a different higher-dimensional inequality. Targeted searches and the published-record corpus did not locate the exact two-dimensional all-real-exponent phase formula or a theorem implying it. The two-dimensional affine functional calculus is the key extra step, not a title-level reformulation of the known \(k=2\) result.

### Equivalent formulations
- Search/source: Published-record semantic query: 2x2 determinant phase law AB BA matrices determinant trace orientation complex phase.
- Search/source: M. M. Ghabries, H. Abbas, B. Mourad, On some open questions concerning determinantal inequalities, Linear Algebra and its Applications 596 (2020).
- Evidence: No inspected exact source or database entry states the audited final claim in an equivalent formulation.
- Reasoning: The primary determinant literature proves the \(k=2\) Hermitian inequality and several restricted exponent ranges. Ghabries’s 2022 thesis treats these questions and leaves the broader comparison conjectural, while the 2026 normal-matrix log-majorization extension proves a different higher-dimensional inequality. Targeted searches and the published-record corpus did not locate the exact two-dimensional all-real-exponent phase formula or a theorem implying it. The two-dimensional affine functional calculus is the key extra step, not a title-level reformulation of the known \(k=2\) result.

### Broader coverage
- Search/source: M. M. Ghabries, H. Abbas, B. Mourad, On some open questions concerning determinantal inequalities, Linear Algebra and its Applications 596 (2020).
- Search/source: M. M. Ghabries, Contributions to Matrix Inequalities and Some Applications, PhD thesis (2022).
- Search/source: M. M. Ghabries, A log-majorization inequality for normal matrices with applications to determinantal inequalities and geometric means, arXiv:2607.21163.
- Evidence: The closest broader sources cover ingredients, restricted parameter regimes, or background models but do not imply the audited final claim.
- Reasoning: The primary determinant literature proves the \(k=2\) Hermitian inequality and several restricted exponent ranges. Ghabries’s 2022 thesis treats these questions and leaves the broader comparison conjectural, while the 2026 normal-matrix log-majorization extension proves a different higher-dimensional inequality. Targeted searches and the published-record corpus did not locate the exact two-dimensional all-real-exponent phase formula or a theorem implying it. The two-dimensional affine functional calculus is the key extra step, not a title-level reformulation of the known \(k=2\) result.

### Exact database or table
- Search/source: Published-record semantic corpus
- Evidence: No decisive exact database/table coverage was found; where the claim is theorem-level, the primary literature comparison is the controlling check.
- Reasoning: The primary determinant literature proves the \(k=2\) Hermitian inequality and several restricted exponent ranges. Ghabries’s 2022 thesis treats these questions and leaves the broader comparison conjectural, while the 2026 normal-matrix log-majorization extension proves a different higher-dimensional inequality. Targeted searches and the published-record corpus did not locate the exact two-dimensional all-real-exponent phase formula or a theorem implying it. The two-dimensional affine functional calculus is the key extra step, not a title-level reformulation of the known \(k=2\) result.

### Claim versus prior implication
- Search/source: M. M. Ghabries, H. Abbas, B. Mourad, On some open questions concerning determinantal inequalities, Linear Algebra and its Applications 596 (2020).
- Search/source: M. M. Ghabries, Contributions to Matrix Inequalities and Some Applications, PhD thesis (2022).
- Evidence: The closest broader sources cover ingredients, restricted parameter regimes, or background models but do not imply the audited final claim.
- Reasoning: The inspected prior statements do not mechanically imply the audited final claim; the additional argument identified in the correctness reconstruction is substantive enough for this claim.

### Primary-source inspections
- **Contributions to Matrix Inequalities and Some Applications** (HAL thesis tel-03936351 / PhD thesis, 2022): trigger — same determinant comparison family and closest comprehensive primary source; material read — full thesis text around the determinant conjectures, Hermitian cases, exponent ranges, and open comparison statements; method — lawful full-text inspection; assessment — NOT_COVERING; evidence — The thesis records the broader determinant problem and partial ranges but not the audited all-real-exponent \(2\times2\) phase identity.
- **A log-majorization inequality for normal matrices with applications to determinantal inequalities and geometric means** (arXiv:2607.21163): trigger — recent plausible broader coverage; material read — abstract and theorem-level description of the normal-matrix extension; method — lawful arXiv inspection; assessment — DIFFERENT_IMPLICATION; evidence — The normal-matrix result addresses a different determinant comparison and does not imply the exact \(2\times2\) phase law for arbitrary real \(k,p\).

## Scientific value
Status: **PASS**.

The theorem gives a sharp equality/sign boundary for a concrete open determinant-comparison family and resolves both positive and negative exponent regimes in dimension two. A complete low-dimensional boundary theorem for a live matrix inequality is mathematically motivated and useful even though it does not settle higher dimensions.

## Checked sources
- M. M. Ghabries, H. Abbas, B. Mourad, On some open questions concerning determinantal inequalities, Linear Algebra and its Applications 596 (2020).
- M. M. Ghabries, Contributions to Matrix Inequalities and Some Applications, PhD thesis (2022).
- M. M. Ghabries, A log-majorization inequality for normal matrices with applications to determinantal inequalities and geometric means, arXiv:2607.21163.
- Published-record semantic query: 2x2 determinant phase law AB BA matrices determinant trace orientation complex phase.

## Limitations and residual risks
- The theorem is genuinely two-dimensional and does not settle the higher-dimensional conjecture.
- Older low-dimensional determinant-inequality literature could contain an equivalent formula under different notation; no such implication was found.

This audit reports the mathematical assessment only. It is not a formal proof-assistant certificate or a guarantee of priority.
