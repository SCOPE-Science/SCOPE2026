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

# Finite verification and analytic scope

Run `python3 verify_plane_root_degree.py` using Python 3 and the standard library. The script enumerates all Catalan preorder offspring sequences for \(2\le n\le11\), independently reconstructs their root degree and every outdegree histogram, and compares exact moments against the formulas in the theorem using rational arithmetic. It separately evaluates the sign polynomial on every feasible integer pair through \(n=300\) and tests a fixed-degree asymptotic convergence envelope. The script's successful output was `VERIFY_OK trees=23713 assertions=45489`.

These tests do not exhaust all tree sizes, do not prove the limit and do not establish historical priority. The general proof uses formal power-series differentiation, coefficient extraction by Lagrange inversion, and polynomial factorizations explicitly recorded in the result.
