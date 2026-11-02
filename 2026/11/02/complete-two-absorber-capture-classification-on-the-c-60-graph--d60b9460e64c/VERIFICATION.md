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

The reproducibility package contains `verify.py` (pure Python standard library), `CERTIFICATE.tsv` (all 23 graph-symmetry orbit representatives and exact ranks), and `CHECKER_OUTPUT.txt` (observed output). The checker was executed successfully against its packaged source content. It proves an explicit degree-15 adjacency-polynomial annihilation by integer arithmetic on every basis vector, checks an exhaustive 120-element symmetry action and all 1770 unordered pairs, and calculates all 23 representative matrix ranks with rational Gaussian elimination. It also verifies the intrinsic shortest-path and antipode placement rule.

The analytic proof of the long-time loss law is given in `RESULT.md` and is not inferred from the checker. The exact rank classification is a complete finite computation on the specified 60-vertex graph, not a numerical extrapolation to larger graphs. No claims are made concerning nonuniform hopping, finite-time performance, experimental validity, or external independent certification.
