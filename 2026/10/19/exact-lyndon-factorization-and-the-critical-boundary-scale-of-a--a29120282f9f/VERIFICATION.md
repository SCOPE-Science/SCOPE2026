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

The proof is symbolic and covers all integers \(q\ge2,r\ge1,j\ge0\). Independently, run `python3 verify_lyndon.py`. The script implements finite substitutions and Duval's algorithm separately, comparing the full Lyndon factor lists, factor starts, strict descending order, and the two-case closed boundary formula over its declared parameter grid. Each finite test that exceeds its stated length limit is skipped with no inference about the skipped instance. Finite runs are corroboration rather than exhaustive evidence for the infinite quantifiers.

The principal internal deductions can be reproduced without software: \(W_{j+1}=W_j0^{rq^j}W_j\); the longest internal zero run of \(W_j\) equals \(rq^{j-1}\) for \(j\ge1\); and therefore every suffix of \(B_j=0^{rq^j}W_j\) has a shorter leading zero run than \(B_j\). The generating-function identity follows by formal summation, valid coefficientwise.

No independent audit or external certification has been performed.
