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

# Reproducibility

The standalone \(\texttt{checker.py}\) uses only Python's standard library. From the directory containing it, run \(\texttt{python3 checker.py}\). It generates finite Cantor substitution iterates and enumerates literal substrings for substitution levels \(1\) through \(7\), compares every observed Abelian-class size with the exact formula, checks the distinct-factor counts and the two family-overlap pairs, and verifies the gaps between successive ones. It also calculates exact rational normalized means and checks the limiting variance identity.

This finite enumeration does not certify infinitely many instances. The full proof for arbitrary \(k\ge1\), including the unique long-run argument and limiting-mass tail bound, is in RESULT.md. No independent audit has been performed.
