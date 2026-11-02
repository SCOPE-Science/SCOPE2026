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

# Reproduction and proof boundary

Run `python3 verify_conference_reduct.py` with a standard Python 3 installation; compare its standard output with `verify_conference_reduct_output.txt`. The script builds finite fields from explicit irreducible polynomials, constructs each quadratic-residue conference graph, verifies signed pair orthogonality and enumerates **all** compatible fourth-point requests at the stated sample orders. It checks the formula, attained minimum, the small-order separating configurations, and sharp deletion examples. Tested orders: \(5,9,13,17,25,29\). The output is included verbatim.

The mathematical proof of the unrestricted-depth and arbitrary-order statements is the signed-matrix extension calculation and the indefinite pebble-game strategy in `RESULT.md`. Finite output does not establish the theorem alone; in particular no unenumerated conference graph is covered by a computer certificate. Historical novelty remains qualified by access to older two-graph literature. Independent mathematical audit has not been conducted.
