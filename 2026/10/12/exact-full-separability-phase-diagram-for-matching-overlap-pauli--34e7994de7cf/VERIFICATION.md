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

The universal arguments are analytic and appear in `RESULT.md`.

The proof distinguishes local mismatch number \(d(P,Q)\), not only global commutation. A pair with \(d=0\) is locally diagonal, while \(d=1\) reduces to positive one-qubit conditional blocks. For even \(d\ge2\), the global strings commute and the Gibbs expansion has Pauli coefficients with absolute sum \(s+t+st\). A one-site partial transpose has an eigenvalue
\[
2^{-k}(1-s-t-st).
\]
This certifies necessity as well as the Pauli-mixture sufficiency.

For odd \(d\ge3\), global anticommutation yields
\[
\rho=2^{-k}\left(I-\tanh(\beta r)(aP+bQ)/r\right),\qquad r=\sqrt{a^2+b^2}.
\]
The sum of the absolute two Pauli expectations is \((|a|+|b|)\tanh(\beta r)/r\). It cannot exceed one in any fully separable state because two incompatible sites already enforce the sharp two-site Cauchy–Schwarz bound. Together with the Pauli-mixture construction this proves both directions.

The three-qubit witness \(H=-J(XXX+ZZZ)\) is unchanged by partial transposition on any subset, since \(X\) and \(Z\) are real symmetric at every site. Nevertheless its two Pauli expectations violate the full-separability bound above the claimed critical inverse temperature.

The bundled verifier replays explicit matrices in representative two- and three-/four-qubit cases and the exact scalar boundaries. It does not infer infinite-size results from finite experiments. It requires Python 3 with NumPy for numerical matrix checks.

No theorem is claimed for higher-overlap interaction graphs, or for bipartition-specific entanglement of the all-cut-PPT example.
