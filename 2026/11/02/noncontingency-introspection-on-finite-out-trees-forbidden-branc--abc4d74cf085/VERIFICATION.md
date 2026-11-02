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

# Verification of finite-tree noncontingency result

The complete proof and its unrestricted quantifiers are in `RESULT.md`. The attached `checker.py` uses only the Python standard library. Run `python3 checker.py` in the folder containing the files; expected final line: `ALL_CHECKS_OK`.

The checker generates every labelled undirected tree by Prüfer sequences and independently roots it at every vertex. It compares the forbidden-branching condition against explicit evaluation of every Boolean valuation for all rooted trees with up to six vertices. It also compares the rooted-tree count with a separate labelled-set recurrence for all sizes up to seven and prints the recurrence up to twelve vertices. On the verified replay, counts of validating rooted labelled trees for sizes one through seven were \(1,2,9,64,565,6036,77749\), against totals \(1,2,9,64,625,7776,117649\). The first failure is therefore exactly \(60\) five-vertex objects.

The enumeration and singularity asymptotics for arbitrary \(n\) are mathematical consequences of the full structural proof and the standard implicit-function transfer method, not extrapolations from finite checks. The displayed singularity constants are numerical approximations and have not been interval certified. Historical priority remains subject to older sources that were not accessible in full. Independent scientific assessment has not been performed.
