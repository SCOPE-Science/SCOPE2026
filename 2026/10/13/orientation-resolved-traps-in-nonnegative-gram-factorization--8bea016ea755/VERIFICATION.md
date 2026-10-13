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

# Reproduction and boundaries

Run `python verify.py` with Python 3. No third-party libraries, downloads, randomness from external sources, or auxiliary inputs are required. The deterministic pseudorandom test generator has a fixed seed. The script prints `VERIFY_OK 1141 exact-rational tests; boundary quartic escape identity` on success.

The checker independently evaluates both sides of the exact block identity with rational matrices; it also checks one-row perturbation coefficients and the quantitative nonnegative lower bound on diverse finite instances. It checks the critical quartic escape identity by exact rational arithmetic in squared coordinates. These finite tests do **not** establish universal nonnegativity, local optimality, or absence of covering prior work; those assertions rely on the proof and the separate literature comparison.

The theorem's full domain consists of integers \(m,k,r\) with \(m,k\ge1\), \(r\ge k+1\), and all positive unit vectors \(a\in\mathbb R^r\). The sign classification includes equality, for which second-order optimality is insufficient. The margin is a sufficient entrywise certificate, not a globally maximal basin measurement.
