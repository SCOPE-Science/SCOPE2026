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

## Reproduction
Run `python3 verify_crown.py` with Python 3.10 or later and SymPy. The supplied `verify_crown_output.txt` is the recorded successful result from the same packaged script.

## Actual finite checks
Exact enumeration exhausts normal fan active-facet rank tests for every nonempty polytope face at cycle sizes \(6\) and \(8\), with \(403\) and \(3075\) faces respectively. All subsets of vertices are then checked for the predicted component-incidence relations. Exact Ehrhart finite differences and direct alternating-permutation counts match for path lengths \(1,3,5,7\).

## Limits
These finite checks do not prove the infinite statement. The symbolic argument establishing all-parameter correctness appears in `RESULT.md`. The analytical transverse cones follow from integer-unimodular ray identifications, not a numerical regression. Independent mathematical audit has not been performed.
