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

# Reproducible verification

Execute `python verify.py` with Python 3.9+ from the same directory. The checker independently computes the forward birth-death distribution for the number of incorrect nonsources and the convolution of pure-death geometric holding times. For each of 55 pairs \((n,z)\) with \(2\le n\le11\) and \(1\le z<n\), it compares the exact CDF at times \(0,1,\ldots,13\) and independently reconstructs the finite spectral-survival expression. These make 770 rational-number comparisons of each identity. It additionally tests the claimed telescoped leading coefficient for all 55 pairs. The script prints `PASS` only after all assertions succeed.

The verification relies on exact fractions, not floating-point tolerance. Computations are finite and do not prove the limiting law; analytic proofs and explicit quantifiers are in RESULT.md. The full 2014 zealotry article was inaccessible for complete comparison; originality is not independently certified.
