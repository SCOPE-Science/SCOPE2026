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
The standalone `verify_howe5.py` checker runs using the Python standard library. It recomputes each degree-index coefficient of the Hasse–Witt matrix in every \(\mathbb F_5\) coefficient specialization and enumerates all smooth marked pairs in the finite fields of orders \(5\), \(25\), and \(125\). Actual successful results: rank counts \((3,6,4)\), \((3,60,490)\), and \((3,366,14884)\), respectively (ranks \(1,2,3\)). Each of the three Hasse components meets the smooth parameter space in \(4\), \(22\), and \(124\) points, respectively, and each pair has one rational intersection in all three fields. The exact polynomial identities, boundary divisor intersections and all-extension point-count formulas are justified in `RESULT.md`, not by extrapolating these finite checks. Independent audit and external validation have not been performed.
