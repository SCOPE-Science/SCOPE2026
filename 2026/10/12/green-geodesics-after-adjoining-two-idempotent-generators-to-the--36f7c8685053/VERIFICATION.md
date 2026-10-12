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
# Reproducible checks and limits

Run `python3 verify.py` from the extracted package. The checker enumerates all words in the four-letter alphabet through length nine, calculates their actual Munn rooted intervals directly, and checks (i) full minimum-word sets for R classes, (ii) D minimal words, (iii) L by inverse/reversal and (iv) first ten generating-series coefficients. The symbolic lower-bound and language-complexity proofs in RESULT.md, not these experiments, justify the infinite statements. No external mathematical certification is asserted.
