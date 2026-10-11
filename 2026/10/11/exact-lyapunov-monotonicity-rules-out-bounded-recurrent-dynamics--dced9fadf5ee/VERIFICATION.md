---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

`verify.py` performs the following dependency-free checks with exact rational arithmetic where applicable:

1. It verifies that the source parameter values give \(g(1+m)/(2r)=126/61\).
2. It expands the derivative of \(H=z+(126/61)x^2\) from the differential equations and verifies exact cancellation of the mixed term, leaving \(\dot H=-12x^2\).
3. It constructs \(\lambda I-J\) for the source's line-equilibrium parameters at the origin and computes the determinant as a polynomial over rational numbers, obtaining
\[
\lambda^5+\frac{41}{5}\lambda^4+\frac{61}{10}\lambda^3+610\lambda^2
=\frac{\lambda^2}{10}(10\lambda^3+82\lambda^2+61\lambda+6100).
\]
4. It solves the nonzero cubic numerically by an independent Durand–Kerner iteration and checks the roots against \(-11.9566842997\) and \(1.87834214986\pm6.89124944793i\).

Run `python verify.py`; successful replay prints `VERIFY_OK`.

The script checks algebraic and finite-dimensional spectral calculations. It does not replace the analytic arguments that bounded forward trajectories converge or that invariant probability measures are supported on the equilibrium line. Those conclusions follow from the exact monotonicity identity, uniform continuity of \(x\), omega-limit invariance, and the invariant-measure generator identity. No claim is made that all forward trajectories are bounded.
