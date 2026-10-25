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

# Reproducible verification

Run `python3 verify_pseudo134.py`. Only Python standard-library modules are used. Expected terminal line begins `PSEUDOPERIOD_134_ENTROPY_ZETA_PASS`.

The script reconstructs the four forbidden words by all binary five-word enumeration and reconstructs the sixteen-by-sixteen de Bruijn adjacency matrix. It checks the degree-sixteen characteristic polynomial by exact integer traces and Newton identities, checks all strongly connected components, and confirms positivity of the eighth power on the twelve-state component. It tests all binary period-\(n\) configurations through \(n=12\) by direct cyclic-window enumeration, and all finite binary words through length \(14\) by direct forbidden-factor enumeration.

These are complete finite checks of the finite-state reductions used in the mathematical proof. They do not replace the exact graph-presentation, determinant, and Perron--Frobenius arguments establishing all lengths. Independent audit has not been performed.
