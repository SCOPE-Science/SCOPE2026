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
# Verification record

The proof is self-contained for the infinite theorem: (i) the terminal first-appearance coupon forces the exact range \(1\le U_j^N\le N\); (ii) a geometric waiting time with success \(c/j\) converges on the scale \(j\) to an exponential law; (iii) conditional occupancy variance decreases as \(O(1/j)\) for each fixed common type; (iv) the chance of needing further draws after the first rare coupon tends to zero; (v) the absence of a threshold atom yields a two-point law; and (vi) boundedness transfers it to mean and variance. Combining with the range bound proves the exact asymptotic supremum.

The accompanying `checker.py` was executed directly using Python 3 and completed with `Exact finite sibling-deficit certificate: PASS`. It uses rational finite-state dynamic programming, cap \(j\), to handle self-loops without truncating the stopping time. In the \(N=j=3\) comparison, the exactly checked uniform variance is \(707/1296\), the exactly checked nonuniform variance is \(416326091/590490000\), and the difference is \(5887451/36905625>0\). A two-category instance was also checked.

The finite code is not a computer proof of any asymptotic, and the analytic theorem does not identify finite-index global optimizers or rates. Priority comparison with two highly relevant full texts was incomplete because those texts were inaccessible; statements available from their abstracts and accessible summaries are compared in the review. No independent scientific audit is asserted.
