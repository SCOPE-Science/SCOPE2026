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

# Arithmetic verification

Run `python3 verify.py` with `CERTIFICATE.json` in the same directory. This uses Python 3 standard library `json`, `array`, `fractions`, and `math` and prints `VERIFY_OK` only when every exact check succeeds. The checker reconstructs the 1771 indexed monomials and Hadamard transform from the displayed matrix, checks admissible-variable count 686, recomputes all 85 base equality coefficients and 427 selected joint constraints, and checks the Farkas combination's exact negative right-hand side and strictly positive coefficient for each allowed nonnegative variable.

The certificate rows were selected numerically, but proof validity depends solely on the independent finite exact rational identity reconstructed here. This verification does not construct a distance-6 code, certify a general-parameter statement, or substitute for independent scholarly audit.
