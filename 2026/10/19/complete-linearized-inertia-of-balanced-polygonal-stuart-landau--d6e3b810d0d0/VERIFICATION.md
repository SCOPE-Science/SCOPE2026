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

# Verification record

The complete mathematical proof is in `RESULT.md`. Its critical independently reconstructed steps are: (i) the rotating-frame vector field and exact symmetric Jacobian; (ii) the rank-two positive and rank-\(M\) negative decompositions for noncollinear polygons; (iii) the surjectivity needed to obtain both extremal indices and the \(M-2\)-dimensional smooth kernel; and (iv) the collinear longitudinal/transverse splitting with the rank-one Sylvester inertia test, including \(\tau=1\).

The accompanying `verify.py` is standalone Python 3 standard-library code. Its exact-rational congruence elimination tests signatures, while direct polynomial vector-field differences independently check the Jacobian entries, including the analytically determined cubic finite-difference error. It also checks that all generated examples are balanced equilibria. Actual execution: `python3 verify.py` produced `VERIFY_OK: exact rational polynomial/Jacobian/inertia/closure assertions = 3504`.

Finite example tests do not prove the theorem for unbounded \(M\), arbitrary positive real parameters, or every polygon shape; the proof does. The theorem is restricted to all-active, purely dissipative coupling. Independent scientific validation has not been performed.
