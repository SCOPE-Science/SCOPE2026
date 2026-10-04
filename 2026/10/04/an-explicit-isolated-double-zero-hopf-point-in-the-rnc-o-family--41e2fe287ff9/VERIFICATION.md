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

The primary vector field was reconstructed from the source's displayed system. For the stated rational coefficients, the equilibrium equations were reduced symbolically to \(z=-y\), \(w=-10y\), \(x=39y/4\), and \(\mu-39y^2/4=0\). This proves the equilibrium count without numerical root finding.

The Jacobian at the origin was reconstructed from the same vector field. Substitution into the general characteristic coefficients gives the exact factorization
\[
\lambda^2\left(\lambda^2+rac{1769}{1904}ight).
\]
Thus the nonzero eigenvalues are purely imaginary and the zero eigenvalue has algebraic multiplicity two.

The bundled `verify.py` uses exact rational arithmetic to replay the linear cancellation, the equilibrium reduction, and every coefficient of the characteristic polynomial. It is intended as an arithmetic check of the proof, not as a numerical dynamics experiment.

Limits: no claim is made that the point satisfies all generic normal-form or transversality hypotheses of a particular zero-Hopf bifurcation theorem, and no periodic-orbit existence theorem is asserted here. Independent audit has not been performed.
