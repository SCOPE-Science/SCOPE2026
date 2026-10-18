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

The exact proof is the oriented fixed-chain calculation and cancellation in `RESULT.md`, valid for all integers in its stated domain. As a reproducibility check, run `python3 verify_transpose.py` with Python 3 and no third-party dependencies. The delivered `verification_output.txt` is the output of a successful local run; a reader should reproduce it by executing the script.

The script exhaustively checks \(2^{n^2}\) subsets for \(2\le n\le4\), in each case verifying the row/column cap and calculating the orientation sign by inversions of the transformed ordered simplex. This tests the left-hand side of the theorem without using the regular-graph correspondence. Separately, it enumerates all labeled undirected graphs on the same vertex set, tests regularity, and calculates the right-hand side. It also computes the cycle decomposition sequence by a recurrence and checks it against direct enumeration for \(3\le n\le6\).

Checks cover \(n=2,r=1\); \(n=3,r=1,2\); and \(n=4,r=1,2,3\). The verified signed Lefschetz numbers are respectively \(1;0,1;-3,-3,-1\). The two-factor sequence is \(1,3,12,70,465,3507\) for \(n=3,\dots,8\). The large-parameter theorem follows from exact symbolic cancellation, **not** from extrapolating these numbers. No independent mathematical audit has been performed.
