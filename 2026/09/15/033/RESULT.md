# A dimension-16 cutoff obstruction inside Dodson's Section 10 bootstrap

## Context

Dodson proves minimal-mass rigidity for the focusing mass-critical NLS in dimensions 2 through 15. This record does **not** extend or refute that theorem. It isolates one exponent in the Section 10 truncated-energy bootstrap and records why the same arrangement ceases to absorb at dimension 16.

## Result

For the literal term-B residual exponent extracted in the original package,
\[
R_{\mathrm{lit}}(d)
=\left(\frac8d-\frac{3}{5d}-\frac{7}{10d^2}\right)\frac{2d}{d-8},
\]
one has
\[
R_{\mathrm{lit}}(15)>2,\qquad R_{\mathrm{lit}}(16)<2,
\]
and the values continue to decrease for the dimensions checked beyond 16. Numerically,
\[
R_{\mathrm{lit}}(15)\approx2.10095,\qquad
R_{\mathrm{lit}}(16)\approx1.83906.
\]
Thus this literal absorption step closes at d=15 but not at d=16.

A separate one-parameter model in the original record inserts a nonnegative cutoff deficit \(\delta\) through
\[
R_B(d,\delta)=
\left[\left(\frac8d-\frac1{5d}\right)
\left(1-\frac1{10d}-\delta\right)-\frac2{5d}\right]
\frac{2d}{d-8}.
\]
For **this formula**, the exact condition \(R_B(d,\delta)\ge2\) is
\[
\delta\le \frac{77-5d}{39}-\frac1{10d}.
\]
In particular the right-hand side is negative at d=16, so no admissible \(\delta\ge0\) of this monotone-deficit form can repair that modelled term.

The two displayed residual formulas differ in their \(d^{-2}\) coefficient. The earlier version blurred them together and described the discrepancy as a small correction. They are now kept separate.

## What is and is not proved

- The calculation identifies a genuine **method-local barrier** in the filed Section 10 cutoff/Young arrangement.
- Increasing the particular deficit \(\delta\ge0\) only worsens the generalized residual, so that knob cannot cure d=16 in that model.
- This does **not** prove that no different truncation, interpolation, commutator decomposition, or Young/Hölder organization could extend the PDE argument to higher dimensions.
- The term-A feasibility check in the supplied verifier remains positive in the tested range, so the recorded failure is localized to term B within this bookkeeping.

## Reproducibility

Run `artifacts/check_barrier.py`. It prints both the literal exponent and the generalized deficit model, verifies the exact algebraic cutoff bound, and writes no files. The companion `artifacts/barrier_check.json` contains the audited values.

## References

- B. Dodson, *A determination of the blowup solutions to the focusing NLS with mass equal to the mass of the soliton*, arXiv:2106.02723; Ann. PDE 9 (2023), Paper No. 3.
