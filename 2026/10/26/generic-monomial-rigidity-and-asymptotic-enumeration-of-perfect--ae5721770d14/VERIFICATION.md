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

# Reproducibility

Run `python3 check_generic_evolution.py` with Python 3 standard library. This independently enumerates invertible structure matrices over the prime fields of orders 2 and 3, computes every monomial stabilizer by direct entrywise algebra identities, calculates the stabilizer distribution, and checks the exact Burnside count through orbit–stabilizer. Tested cases are \(q=2\) with dimensions \(2,3,4\), and \(q=3\) with dimensions \(2,3\). The final line must read `VERIFY_OK`. The script does not test extension fields, large dimensions, or the limiting asymptotic; their scope relies on the universal algebraic argument in the proof. All computations are exact integer/finite-field calculations. Independent audit has not been performed.
