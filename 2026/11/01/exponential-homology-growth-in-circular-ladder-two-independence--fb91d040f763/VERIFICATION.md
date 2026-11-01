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

# Reproducibility of the stated theorem

`python3 verify_prism.py` uses the standard library to reconstruct the signed sixteen-state transition matrix, derive its characteristic polynomial using exact integer arithmetic, and verify the recurrence, initial values, and strict rational root inequalities. It independently exhausts all labelled vertex subsets for each of the six cases \(3\le n\le8\) and compares the signed face sums with the transfer traces. The complete reference output is in `verification_output.txt` and ends with `ALL_CHECKS_PASS`.

The infinite nonvanishing result additionally depends on the stated transfer-bijection proof, the analytic root-separation argument, and the Euler--Poincaré inequality. Finite brute force alone is not a proof beyond eight rungs. Homology degrees, integral torsion, full homotopy classification and publication priority are not certified here. Independent mathematical audit has not been performed.
