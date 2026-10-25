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

Execute `python verify.py` using Python 3.9 or later (standard library only). The script enumerates every center-neighbor outcome sequence through eight updates at three rational values of confidence and three rational intrinsic-opinion configurations. For each sequence it independently calculates the synchronous FTL agent opinions and the scalar coefficient prediction, tests the exact leaf difference and opinion range, and aggregates the resulting rational mean and variance. The program completed with 13,916 assertions passed.

The exact symbolic check at confidence \(\alpha=1/2\), predispositions \((0,1/2,1)\), and \(t=2\) is \(Y_2-Y_*=-3\xi_0/32-\xi_1/32\) with variance \(5/512\). The finite checker cannot certify almost-sure convergence, infinite cumulant sums, or Gaussian limits; the proof of those statements relies on gamma ratios, independent-series convergence, and the Lindeberg central limit theorem as given in `RESULT.md`.

External independent scientific audit has not been performed.
