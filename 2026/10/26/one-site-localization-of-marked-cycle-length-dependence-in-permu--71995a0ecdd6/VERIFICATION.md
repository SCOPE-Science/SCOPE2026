---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Marked-cycle count (n-1)! proves K uniform. Adjacent-label conjugation fixing 1 pairs interior descents and ascents; its only failures have two specified image pairs whose conditional probabilities match on the complementary permutation when both labels avoid the marked cycle and vanish otherwise. The first successor A=Pi(1) is uniform on labels 2..n; split A=2 and A>2 and use marked predecessor and complementary fixed-point events to derive the 4-case formula; sum against uniform K for covariance. Separate exhaustive exact enumeration of every permutation n=3..8 reproduced each k-conditional indicator probability and covariance. Does not claim joint independence of later indicators.

## originality

PASS

Fixed-point/descent localization (K=1 slice) and Elizalde–Troyka single-cycle descent-set law (K=n portion) are known. Gessel–Reutenauer and Fulman treat unmarked cycle structure, which by itself cannot distinguish the unique cycle containing label 1. The intermediate K-conditioned first-site formula and all-position individual independence were not implied by inspected sources; older full text of Diaconis–McGrath–Pitman 1995 remains unread.

## value

PASS

A global orbit statistic displays exact dependence localized at the left boundary of the one-line word, with four distinct conditioning regimes and a nonzero 1/4 limiting covariance. The result gives a sharp full n,k structural dependence classification not obtainable from the unconditional Eulerian marginals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
