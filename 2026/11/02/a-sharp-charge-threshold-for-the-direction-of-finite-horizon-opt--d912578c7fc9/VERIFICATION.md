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

The analytical steps and all assumptions are in `RESULT.md`. The included standard-library program `verify.py` is executed by running `python3 verify.py` alongside the document. It checks the closed-form two-state transition probability against the net-counting-work identity; the unique optimizer's stationary equation against numerical maxima; optimal-load positions and monotonicity across a deterministic grid; the tilted truncated-exponential variance inequality; and the exact charging and storage threshold crossings.

A local replay completed successfully with 6636 bounded checks covering 108 parameter families. Illustrative values with \(\beta=E=k=1\) for discharge durations \(T=0.01,1,20\): at prepared occupation \(p=0.65\), optimal loads are approximately \(0.7872562,0.7986934,0.8035373\); at \(p=0.75\), all equal \(1\); at \(p=0.9\), they are approximately \(1.4195253,1.3431205,1.3176680\).

These finite checks do not certify the strict all-parameter inequality, uniqueness, infinitely many horizons, or publication priority. Those statements rely on the displayed exact calculation and the separately described literature comparison. No independent audit has been performed.
