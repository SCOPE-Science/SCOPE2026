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

# Reproducible checks

Run `python3 verify.py` with Python 3 and only its standard library. The script independently enumerates circular length-one-through-eight DNA words for caps one through three, constructs rotation orbits, tests reverse-complement fixedness and minimal period, then checks every GC-weight cell against both exact formulas. It also independently verifies the bivariate run-transfer identity coefficientwise to length twelve for caps one through four, and evaluates extended nonnegativity and integrality checks through length eighty.

Expected final marker: `VERIFY_OK`.

The proof of the infinite formulas is in RESULT.md, not inferred from this finite check. The local-limit asymptotic uses a finite-state aperiodicity argument; the code does not claim to establish this asymptotic by finite sampling. An independently executed scientific audit has not been performed.
