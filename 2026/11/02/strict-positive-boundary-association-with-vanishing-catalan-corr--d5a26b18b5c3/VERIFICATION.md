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

Run `python check.py` with Python 3 (standard library only). The code enumerates every permutation on 2–8 labels, directly rejects occurrences of the forbidden pattern, computes the lengths of both maximal fixed boundary blocks, and compares their exact frequencies to independent Catalan formulas. All 490 exact equalities/strict inequalities pass over 2054 accepted permutations. The code separately evaluates exact rational covariance formulas at 40, 100, 200 and 400 vertices, checking positivity and reporting rescaled numerical evidence for convergence to 8/27. Direct enumeration and finite numerical estimates do not prove the all-size inequalities or asymptotic constant; these follow from the included mathematical proof. Independent validation has not been performed.
