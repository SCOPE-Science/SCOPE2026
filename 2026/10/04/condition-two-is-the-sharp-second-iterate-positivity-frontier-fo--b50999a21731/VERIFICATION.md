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
The verification artifact uses exact rational arithmetic.

It solves the \(2\times2\) normal equations defining the second residual-minimizing Krylov approximation
\[
x^{(2)}=c_0b+c_1Ab
\]
and checks the closed formulas for \(c_0\) and \(c_1\).

For rational diagonal spectra it independently evaluates both moment expressions and the pairwise sums
\[
m_1m_3-m_2^2
\]
and
\[
m_1m_4-m_2m_3
\]
to verify the spectral-barycenter identity exactly.

It checks the sharp three-mode family on both sides of its analytic threshold and reconstructs the complete \(\kappa=4\) witness.

The universal condition-number theorem and the two-dimensional exact-termination argument are analytic proofs in RESULT.md, not finite enumeration claims.
