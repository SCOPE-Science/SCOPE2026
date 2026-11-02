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

# Reproducible checks

Run `python3 checks/check_spin_prime.py` and `python3 checks/check_spin_gf9.py` from the extracted package root. Both use only the Python standard library. The prime-field program exhaustively enumerates all unit-vector partners for sixteen small nondegenerate diagonal forms in dimension three or four over fields with \(q=3,5,7,11\). The extension-field program similarly checks three forms over \(\mathbb F_9\), using explicit component arithmetic in \(\mathbb F_3[t]/(t^2+1)\). For each case the program computes product matrices and their actual multiplicative orders rather than relying on eigenvalue classification, then asserts equality with the formula's predicted histogram. Passed markers are `SPIN_FACTOR_Miyamoto_ORDER_SPECTRUM_OK` and `GF9_EXTENSION_OK`.

These are complete finite tests for the stated small spaces, not an exhaustive check of arbitrary finite fields or dimensions. The all-fields argument is in the proof, using quadratic Gauss sums, orthogonal decompositions, finite torus structures and the explicit nilpotent bound. No independent audit has been performed.
