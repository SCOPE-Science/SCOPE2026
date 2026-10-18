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

Run `python3 verify_ellipsoid.py` with Python 3 and its standard library only. Each rational test at \(t=p/q\) enumerates every feasible potential on the \(1/q\)-grid, normalized to minimum zero, and computes both orthogonal squared projections using exact fractions. Every vertex is in this grid because its graph of tight difference constraints is connected and the right-hand sides are integral multiples of \(1/q\). Thus these thirteen finite configurations check exact ellipsoid containment and contact counts on the full polytope, not on a random sample. The output terminates `EXACT_ELLIPSOID_PASS: 13`.

The main argument uses a separate global endpoint-rounding proof, exact support inequalities, an analytic circumradius identity, and explicit positive log-determinant certificates. The finite configurations are consistency checks and do not certify arbitrary large dimensions or irrational parameters. Independent scientific audit has not been performed.
