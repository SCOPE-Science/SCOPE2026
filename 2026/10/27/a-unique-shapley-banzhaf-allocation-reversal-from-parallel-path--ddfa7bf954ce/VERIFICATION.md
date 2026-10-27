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

# Reproducibility and verification

Run `python3 verification.py` from this directory; its entire JSON standard output should match `verification_certificate.json` byte-for-byte. Python standard library only. The verifier directly enumerates **all** coalitions of the edges for nine finite networks and computes critical-edge events from the winning-coalition predicate, without using the product formulas for that calculation. Both power indices are computed as exact fractions.

It checks \(3680\) coalitions, performs \(17040\) edge/coalition pivotal-event checks and \(12320\) rational recurrence comparisons across \(154\) parameter pairs. Its checks include the two-network reversal \((a,b,m)=(2,3,1)\) versus \((2,3,2)\), and a boundary tie at \((a,b,m)=(2,4,2)\).

The finite program does **not** exhaust unbounded parameters. The all-parameter theorem is proved analytically in `RESULT.md` by conditioning on edge-arrival times, an exact independent-coalition pivot count, an affine one-step ratio sign, and the gamma-function asymptotic. No independent audit has been performed.
