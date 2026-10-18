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

# Verification notes

The standalone `verify.py` uses exact rational arithmetic to reconstruct the full two-site generator, normalized invariant distribution, compensated Poisson equation, and tilted second cumulant of jump count, for 54 pairs of particle counts and positive rational couplings. The executable output is `PASS: 54 exact rational stationary, generator, Poisson and activity-variance tests`. All tests were actually run; no approximate eigenvalue fitting was used. The general proof in RESULT.md treats every integer \(N\ge1\) and every real \(d>0\); the program is finite corroboration only. No verification of higher cumulants or independent audit is claimed.
