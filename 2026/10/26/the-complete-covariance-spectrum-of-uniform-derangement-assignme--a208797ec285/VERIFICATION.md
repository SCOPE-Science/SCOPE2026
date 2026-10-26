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

# Verification of the exact covariance spectrum

Executing `python3 check.py` enumerated every derangement for \(n=3,4,5,6,7,8\), corresponding to \(2,9,44,265,1854,14833\) permutations respectively. Using independent edge-incidence tallies and exact rational arithmetic, the program checked each off-diagonal expectation, every unordered pair of distinct edge indicators by actual common-label pattern, each diagonal variance, and the symmetric/skew test-vector eigen-equations.

The executable ended with `ALL 3771 EXACT ASSERTIONS PASSED`. The five-vertex covariance eigenvalues were both \(15/44\); for four vertices they were \(4/9\) and \(2/3\), and for six vertices \(66/265\) and \(68/265\), in skew/symmetric order. The mathematical proof in `RESULT.md` separately establishes all \(n\ge3\) via exact inclusion-exclusion and a global covariance-operator identity.

**Limits:** This is exact finite enumeration only through \(n=8\). It does not test all sizes, prove historical originality, or constitute independent validation.
