# Independent audit — Half-Sobolev law for truncated diagonal Hilbert eigenstrips

Audit date: 2026-10-01 (UTC) UTC

Scientific disposition: **repaired**.

## Correctness

**PASS** — Plancherel and the same-sign quadrant multiplier give the exact kernel identity. Since \(0\le J(s)\le s\) and \(J(s)/s\to1\), dominated convergence gives the finite half-Sobolev limit and Fatou gives divergence outside the half-Sobolev class. For finitely many jumps, the distributional derivative has a finite atomic part; diagonal atomic terms contribute the logarithmic coefficient and off-diagonal terms are oscillatory lower order. The constants reduce correctly to the hard interval cutoff.

## Originality

**PASS** — Originality passes only for the repaired arbitrary-cutoff half-Sobolev theorem and finite-jump law; the hard-strip leading constant is prior coverage.

### Equivalent formulations
The repaired claim removes the hard-strip constant from novelty and retains the arbitrary \(L^2\) cutoff kernel, iff threshold and general jump law.

Evidence: A published 2026-09-18 record already gives the exact hard-strip leading constant and a convergent expansion. The inspected source abstract introduces the approximate-eigenvector construction but does not state the arbitrary-cutoff half-Sobolev law.

### Broader coverage
No earlier inspected result dominates the arbitrary-cutoff half-Sobolev characterization.

Evidence: The 2026-09-18 prior is narrower in cutoff profile but covers the motivating indicator exactly. A 2026-09-20 record has broader transverse-cutoff/perimeter information but postdates the audited record.

### Exact database or table
This check forced a substantive originality repair.

Evidence: Exact archive search found prior coverage of the \(2/\pi\) hard-strip constant, which is explicitly treated as prior in the repair.

### Claim versus prior implication
The surviving functional law requires its own Fourier/Fatou and jump-asymptotic proof.

Evidence: An exact computation for one indicator does not imply the integral kernel for arbitrary cutoff functions, nor the if-and-only-if half-Sobolev threshold or general finite-jump coefficient.

### Source inspections

- **Sharp logarithmic defect for a truncated double-Hilbert strip** — PARTIAL_COVERAGE.
  Identifier: https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-sharp-logarithmic-defect-truncated-double-hilbert-strip--867a0fef0943
  Material read: complete result and proof.
  Evidence: It proves the exact hard-strip asymptotic and constant \(2/\pi\), so those cannot be claimed as new here.
- **Invariant sets of the double Hilbert transform** — SUPPORTING.
  Identifier: https://arxiv.org/abs/2609.15155
  Material read: abstract and accessible paper preview.
  Evidence: The accessible text confirms finite-measure approximate eigenvectors and the surrounding invariant-set program; full text was not retrievable through the text interface during this audit.

### Residual risks

- The very recent primary preprint full text was not accessible in the available text interface; overlap beyond the visible source description remains a stated risk.

## Scientific value

**PASS** — The repaired result identifies the exact regularity threshold governing an entire natural cutoff family and explains the jump logarithm structurally. This is a reusable analytic law, not a recomputation of the already-known single indicator constant.

## Final assessment

The original framing required a substantive originality repair. The corrected research files state only the surviving correct, original, and valuable claim; all three axes were reassessed on that final claim.

This review does not constitute formal verification or a guarantee against undiscovered prior art.
