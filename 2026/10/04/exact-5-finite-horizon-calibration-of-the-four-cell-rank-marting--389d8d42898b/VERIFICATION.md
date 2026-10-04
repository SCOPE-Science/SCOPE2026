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

The standalone `verify.py` reconstructs the four-cell martingale with exact factorial ratios. It performs four checks:

1. It verifies the first nontrivial martingale values, including \(M_2=8/5\) after two observations in one cell and \(M_2=4/5\) after observations in two distinct cells.
2. It compares the symmetry-compressed dynamic program against exhaustive enumeration of all \(4^8\) labeled paths at a nontrivial boundary.
3. It enumerates every partition of each \(n\le128\) into at most four parts and certifies that no martingale support value lies strictly between the stated lower and calibrated boundaries.
4. It computes both horizon-\(128\) crossing probabilities as exact rational numbers and checks that the lower boundary has size greater than \(0.05\) while the calibrated boundary has size at most \(0.05\).

A clean replay from the embedded script prints `VERIFY_OK`. The verification is finite and exact for the specified \(d=2\), \(N=128\), \(\alpha=0.05\) claim. It does not verify other test variants or establish literature originality.
