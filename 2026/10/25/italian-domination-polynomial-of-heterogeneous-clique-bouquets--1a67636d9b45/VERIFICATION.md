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
# Verification of the Italian domination polynomial
The standalone `verify.py` computes two independent weight arrays: one enumerates all \(3^{1+\sum_i m_i}\) vertex labelings and tests each zero vertex's actual graph-neighborhood label sum; the other performs integer polynomial multiplication of the displayed central-label factors. It checks the arrays coefficient-by-coefficient for every tested blade profile. The verified range contains \(112\) profiles and \(3{,}402{,}756\) total examined assignments, with \(2\le r\le4\), \(1\le m_i\le3\), \(\sum_i m_i\le10\). One-vertex blades are included only as extra boundary tests; the theorem concerns \(m_i\ge2\). The test program handles such boundary cases separately.

The output saved as `verify_output.txt` was produced from the included program. The critical lemma is a direct exhaustive case split on the center label with no unverified computational assumption. Finite checks do not establish the unbounded theorem and no independent mathematical audit is asserted.
