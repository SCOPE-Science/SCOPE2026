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

# Reproducible checks

Run `python3 verify.py` with Python 3 and its standard library. The code constructs all \(32\) sign-cube evaluation points and all \(10\) unordered vertex pairs, checks that the generator columns have Gram matrix \(32I_{10}\) over the integers, and enumerates all \(3^{10}=59049\) coefficient vectors.

The direct evaluation and the logically separate two-point-fiber computation agree on every word. They reproduce the full weight distribution, the \(172\) nowhere-zero words, and its support-of-coefficients decomposition \(20+120+32\). A breadth-first traversal by the nine signed-graph generators obtains \(62\) classes, and a second calculation using all \(3840\) group elements gives a Burnside fixed-point sum of \(238080\), hence \(62\) as well. The script prints `VERIFY_OK` only after every assertion succeeds.

The structural proof of the zero-free classification is included in `RESULT.md` and does not depend upon finite exploration. The numerical exhaustive enumeration certifies only this \([32,10,8]_3\) code. Independent audit is not performed.
