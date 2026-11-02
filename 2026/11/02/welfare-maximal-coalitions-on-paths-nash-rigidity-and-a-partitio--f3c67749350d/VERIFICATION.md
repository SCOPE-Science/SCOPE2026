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

# Mathematical and reproducibility verification

The standalone `verify.py` uses integer arithmetic for all finite welfare scores, with negative infinity for disconnected induced coalitions. It enumerates all set partitions, evaluates all finite-coalition pair distances, and independently checks both the maximum welfare and the number of maximizing partitions. It tests each maximizing partition for every unilateral deviation to every existing other coalition and to a new singleton. Reported finite comparisons: 105880 direct welfare evaluations, 271 maximizing-partition stability checks, 140 parameter-profile maxima/count comparisons (\(2\le n\le8\), \(1\le p\le5\), \(1\le q\le4\)). The critical-regime recurrence and formula are also checked at integer critical ratios with \(L=2,\dots,6\) and \(n\le100\).

To reproduce: `python3 verify.py`, requiring Python 3.10+ with only standard-library dependencies. Finite checks do not establish all-order correctness or literary novelty; the mathematical proof in `RESULT.md` establishes the universal conclusions. No external independent audit has been performed.
