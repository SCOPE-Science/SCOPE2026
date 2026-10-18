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

# Reproducibility checks

Run `python VERIFY.py` with Python 3 standard library. The script builds complete disjoint orbit decompositions of primitive vectors for two independent example companion matrices, checks each length against the projective-prime-power period, and obtains means and variances by exact rational arithmetic. It verifies reduction matrix orders and nonscalar first lifts using modular matrix exponentiation.

For the cubic Padovan matrix, checked moduli are \(3^k\) for \(1\le k\le4\), and \(29\). For the degree-five companion matrix, checked moduli are \(3\) and \(9\). No random sampling is used. `VERIFY_OK` means all assertions passed; the finite tests do not establish the universal theorem, which is proved by exact incidence counts in `RESULT.md`.

The irreducible reductions and projective orders are explicit hypotheses of the theorem. The example cubic and quintic reductions have no proper field-degree factor, and the modular order tests rule out smaller orders dividing \(L\). No independent mathematical audit has been performed.
