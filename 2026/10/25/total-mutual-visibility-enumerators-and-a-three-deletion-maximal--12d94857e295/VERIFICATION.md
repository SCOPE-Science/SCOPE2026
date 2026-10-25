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

The accompanying standalone Python 3 program `verify.py` uses only the standard library. It builds each tested graph from its defining deleted matching, computes all shortest distances and geodesic internal-vertex sets independently, and enumerates every possible vertex subset. It tests both the total mutual-visibility definition and inclusion maximality, compares full bivariate coefficient dictionaries, and tests the derived omitted-vertex membership rule separately. All \(41\) trials with \(3\le p,q\le5\) and \(0\le t\le\min(p,q)\) pass; instances outside the theorem are boundary controls. Reproduce by running `python3 verify.py`; exit status zero and a final `PASS` message indicate agreement.

The general proof rests on the two-part geodesic characterization and the classification of inclusion-minimal allowable omitted subsets. Exhaustive finite tests do not certify unbounded values, published priority, or independent correctness. No independent audit has been performed.
