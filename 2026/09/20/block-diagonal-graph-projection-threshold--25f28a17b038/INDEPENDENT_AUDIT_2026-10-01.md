# Independent audit — Threshold law for projection constants of block-diagonal graph subspaces

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **passed**.

## Correctness

**PASS.** The exact block-multiplier norm \(\|\operatorname{diag}(T_n):X_q\to X_p\|=\|(\|T_n\|)\|_{\ell_r}\) follows from Hölder and finite-support near-attainment. The explicit threshold projection gives the upper bound. For the lower bound, finite simultaneous sign averaging kills off-diagonal blocks on finitely supported inputs; finite-support graph vectors are dense also in the \(q=\infty\) case because the target is \(c_0\). The resulting block equations imply \(|\lambda_n|\|A_n\|\le K\) and \(\|(\|B_n\|)\|_{\ell_r}\le K\); on \(|\lambda_n|>2K\), one has \(|\lambda_n|\|B_n\|>1/2\), hence \(L_\lambda(2K)\le2K\). This yields \(\Theta(\lambda)/2\le\pi_Z(G_\lambda)\le2^{1/p}\Theta(\lambda)\) and the complementability criterion. Integral comparison then gives the stated power-weight phase diagram.

## Originality

**PASS.** Best-of-knowledge originality passes, with an explicit older-literature access risk. The modern full-text source confirms that the classical direct-sum line concerns splitting unconditional bases; no inspected source states the quantitative graph projection threshold.

### Equivalent formulations

The closest structural alias was checked and does not match the quantitative graph statement.

Evidence: The modern direct-sum paper describes the classical Edelstein--Wojtaszczyk theory as a splitting theorem for unconditional bases in finite direct sums. The audited theorem instead quantifies the relative projection constant of a maximal diagonal operator graph by a reciprocal-tail functional.

### Broader coverage

No inspected broader result dominates the threshold formula or the power-weight finite-section rates.

Evidence: Accessible modern exposition attributes qualitative locally convex direct-sum splitting to the older papers. The semantic archive also contains weighted block-identity results, but those concern compactness/strict singularity rather than graph complementability and projection constants.

### Exact database or table

This theorem supplies a quantitative functional and asymptotic phase table, so exact-formula searches are directly relevant.

Evidence: No exact prior formula or rate table was located.

### Claim versus prior implication

The audited theorem is not a formal corollary of the statements visible in the inspected modern source.

Evidence: Qualitative splitting of unconditional bases does not by itself produce the two-sided projection-constant estimate for arbitrary Banach blocks. The proof's sign-averaged block coefficient inequalities and reciprocal-tail bound are additional quantitative content.

### Source inspections

- **Projections and unconditional bases in direct sums of ℓp spaces** — QUALITATIVE_ANTECEDENT.
  Identifier: arXiv:1909.06829
  Material read: Full 15-page preprint, with detailed inspection of the introduction and main theorem.
  Evidence: The main theorem splits unconditional bases across finite direct-sum components and identifies the older locally convex work; it does not state the graph threshold functional.
- **On projections and unconditional bases in direct sums of Banach spaces** — ACCESS_RISK.
  Identifier: DOI 10.4064/sm-56-3-263-276
  Material read: Publisher metadata and modern full-text descriptions; the advertised free PDF returned an access error, and a lawful institutional retrieval found no verified PDF.
  Evidence: Because the article itself was not fully read, no whole-document noncoverage claim is made.
- **On projections and unconditional bases in direct sums of Banach spaces II** — ACCESS_RISK.
  Identifier: DOI 10.4064/sm-62-2-193-201
  Material read: Publisher metadata and modern citations; full text was not obtained.
  Evidence: Potential qualitative or scalar overlap remains a stated risk.

### Residual risks

- The 1976 and 1978 Studia Mathematica papers could not be fully inspected despite lawful retrieval attempts. They are plausible sources for a scalar or qualitative equivalent, so originality remains best-of-knowledge rather than certified.

## Scientific value

**PASS.** The theorem converts complementability of a broad family of unbounded diagonal graphs into a scalar threshold law with block-independent constants and yields a re-entrant power-weight phase diagram. This is a natural structural result with quantitative consequences.

## Final assessment

The final claim survives unchanged on all three scientific axes. No claim text or slogan change is proposed.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
