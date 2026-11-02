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

A standalone standard-library Python verification source is included as `verify.py`.

Run: `python3 verify.py` in the directory containing the file. The program independently builds the Cartesian graph adjacency, all-pairs distances, mutually maximally distant vertex pairs, all independent sets for small cases, and (for up to fifteen vertices) the original strong-resolution predicate on every subset. It checks the polynomial formulas coefficientwise, basis counts and minimum cardinalities, and forcing subsets for the smaller instances. Nine graph instances are covered: (3,3), (4,3), (5,3), (3,4), (4,4), (3,5), (4,5), (3,6), and (3,7). On the packaged source the checks succeeded and printed `VERIFY_OK`.

The exact formulas for all larger parameters are proved combinatorially in RESULT.md. Exhaustive finite validation is not an infinite proof, and the work has not undergone independent mathematical audit or complete publication-priority certification.
