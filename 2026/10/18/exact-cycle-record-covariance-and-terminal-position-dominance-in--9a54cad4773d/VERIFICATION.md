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
# Reproducible finite checks and proved limits

Run `python3 verify.py` with Python 3 and its standard library, from the same directory as this file. The included verifier completed 1,720 exact assertions: exhaustive independent enumeration of cycle counts and one-line record positions for all sizes \(2\le n\le9\), exact rational tests of the parametric derivative recurrence through size 40, and direct Ewens-weighted small-permutation enumeration for concentrations two and three. The program prints `CHECKS_OK: 1720` only after all checks pass. Its own tests do not prove universal claims; the proof in `RESULT.md` derives the unbounded formula by the exact Ewens insertion mechanism, then establishes the asymptotic bound analytically. No independent audit was requested or performed.
