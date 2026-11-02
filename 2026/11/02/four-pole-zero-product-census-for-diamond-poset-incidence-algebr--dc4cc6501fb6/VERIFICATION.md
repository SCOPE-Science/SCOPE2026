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

# Verification protocol

Run `python3 verify.py` (standard-library Python 3). The implementation enumerates every first-factor element \(a\) for each test configuration, constructs the left-multiplication matrix \(L_a\) from actual incidence-path concatenations, performs finite-field Gaussian elimination, and independently sums \(q^{\dim A-\operatorname{rank} L_a}\). This uses neither the proof's additive-character formula nor its endpoint classification. The four-element field is implemented as \(\mathbb F_2[t]/(t^2+t+1)\), not integer arithmetic modulo four.

The exhaustive tested cases are all \(m=0,1,2,3,4\) at \(q=2\); \(m=0,1,2\) at \(q=3\); and \(m=0,1\) at \(q=4,5,7\), totaling fourteen. The checker prints `DIAMOND_INCIDENCE_ZERO_PRODUCT_CENSUS_OK 14` on success; the accompanying `test_results.txt` records the observed output. Exhaustive checks of finitely many pairs are not an infinite-family proof. The theorem follows from local algebra and finite-field character orthogonality for arbitrary finite fields.
