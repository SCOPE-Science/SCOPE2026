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
The exact combinatorial and analytic proof is in RESULT.md. To verify finite independent instances, extract `verify.py` alongside this file and run `python verify.py` with Python 3.9+ and NumPy installed. The verifier constructs pure Dicke vectors and computes actual two-site partial traces before damping, applies all four two-qubit Kraus products, reconstructs concurrence from spin-flip eigenvalues, and compares every result to the formula. It also checks binomial polynomial identities using exact fractions for all \(2\le N\le64\) and selected asymptotic cases. Finite sampled values are not certificates for all dimensions; all-N monotonicity and scaling are established independently in the proof.
