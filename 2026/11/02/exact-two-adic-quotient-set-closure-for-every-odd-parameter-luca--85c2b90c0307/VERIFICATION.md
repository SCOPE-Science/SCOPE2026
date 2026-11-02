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

# Reproducible verification and limits

The proof is a closed symbolic argument: companion-matrix trace, valuation cases, scalar lifting, binary-digit coverage, and a topological shell argument. No numerical extrapolation is used.

Run `python3 verify.py` with the embedded script. It checks sixteen odd parameters from \(-15\) through \(15\), all odd residue classes for eleven dyadic moduli per parameter, the universal scalar matrix congruence for \(2\le k\le12\), and 510 recurrence-term valuations per parameter. Expected marker: `VERIFY_OK: 176 finite modular unit-coverage cases; 8160 valuation checks; matrix lifts through k=12 for all 16 odd parameters.`

These are finite diagnostics only; they do not prove claims for all integers or arbitrary precision. The full proof and source-priority qualifications appear in RESULT.md and REVIEW.md. No independent audit has been performed.
