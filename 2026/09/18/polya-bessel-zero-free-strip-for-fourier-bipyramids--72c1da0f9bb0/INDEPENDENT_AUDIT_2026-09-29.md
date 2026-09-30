# Independent audit — A Pólya–Bessel zero-free strip for Fourier bipyramids

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/polya-bessel-zero-free-strip-for-fourier-bipyramids--72c1da0f9bb0`
**Audited tree:** `4a9c3fd691cfc8f675bb70ed5fe7168e8e93ab0e`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** The Bessel differentiation identity correctly identifies the second derivative of the slice kernel with H_nu(st), so the first positive zero r_d gives convexity on the full strip. Extending the kernel by zero preserves convexity and C1 regularity for d>=3. The half-wave pairing argument makes the cosine transform strictly positive for every real u. Therefore any Fourier zero has |eta|/alpha>r_d, giving kappa>=alpha r_d. The equal-volume ball scaling and threshold A_d are algebraically correct, and the elementary d=3 inequalities rigorously imply A_3<100.

### Independent checks

- Differentiated t^nu J_nu(st) twice using the standard Bessel recurrence and reproduced H_nu(st).
- Checked H_nu is positive near zero and negative at j_{nu-1,1}, so its least positive zero exists and gives positivity throughout (0,r_d).
- Verified the convex extension by zero and the strict sine half-wave pairing argument, including u=0, s=0, and s=r_d endpoints.
- Recomputed the equal-volume ball radius and the threshold A_d from the alpha scalings.
- Numerically cross-checked r_3=1.2557837117945935..., j_{3/2,1}=4.493409457909064..., and A_3=91.6248852570052....
- Checked the rational proof r_3>5/4 and j_{3/2,1}<23/5, which yields A_3<99.672064<100 without floating-point dependence.

## Originality

**PASS.** PASS to the best of current searchable knowledge. Gomez-Serrano--Levitin--Platt--Polterovich prove only existence of a dimension-dependent zero-free strip and explicitly leave fixed-pair rigorous certification as a future interval-arithmetic task. The general convex-kernel positivity principle is classical, but no located source identifies this bipyramid slice with the explicit Bessel combination H_nu or gives the resulting all-dimensional threshold and analytic (100,3) certificate.

### Literature and chronology checked

- https://arxiv.org/abs/2609.10517 — Gomez-Serrano--Levitin--Platt--Polterovich, An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies, submitted 2026-09-09.
- https://www.emergentmind.com/open-problems/rigorous-interval-certification-high-dimensional-bipyramids — Indexed statement of the source paper's fixed-pair certification problem: rigorous certification for prescribed (alpha,d) is left to future interval arithmetic.
- https://doi.org/10.1017/S0004972700047511 — E. O. Tuck, On Positivity of Fourier Transforms (2006), background for the classical convex-kernel positivity mechanism.

## Scientific value

**PASS.** The theorem converts a qualitative compactness strip into a concrete one-dimensional Bessel-root certificate, gives an explicit sufficient counterexample threshold in every dimension d>=3, and rigorously certifies the highlighted numerical pair without two-variable interval arithmetic.

## Limitations

- The Bessel-root strip is sufficient, not claimed optimal, and need not locate the first Fourier zero.
- Loss of slice-kernel convexity beyond r_d does not imply a Fourier zero appears there.
- The motivating preprint is very recent, so unindexed parallel work remains a residual priority risk.

## Publication guard

The current source tree on `main` matched the assignment tree `4a9c3fd691cfc8f675bb70ed5fe7168e8e93ab0e` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
