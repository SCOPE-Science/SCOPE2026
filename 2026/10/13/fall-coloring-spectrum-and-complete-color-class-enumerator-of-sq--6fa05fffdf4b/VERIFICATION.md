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

# Reproducibility and scope

Run `python3 verify.py` from the directory containing this file. The code requires no third-party modules and reconstructs the 48-state transfer matrix from the displayed adjacency conditions. It computes exact traces, independently reconstructs the determinant by Newton identities, and compares its 48 polynomial coefficients with the displayed factored polynomial. It also brute-force enumerates normalized proper cyclic palette words of every length 7 through 16, checks base-word constructions and verifies the first 64 trace values.

Expected output: `VERIFY_OK states=48 characteristic_degree=48 matrix_trace_orders=1..64 independently_bruteforced_orders=7..16 exceptional_orders=7,11 witnesses=8,9,10,15`.

The code is a finite exact verification of a fixed matrix identity and initial checks, not an exhaustive search over all graph orders. The unrestricted theorem follows from the explicit state-space bijection, finite determinant identity, and proof by insertion of four-letter distinct blocks. It establishes no analogous theorem for higher powers of cycles. Independent mathematical audit has not been performed.
