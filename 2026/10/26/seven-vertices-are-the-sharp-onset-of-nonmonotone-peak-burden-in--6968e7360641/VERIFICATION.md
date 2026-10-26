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

# Verification evidence

The actual standalone scientific files are `verify.py` and `rooted_tree_certificate.tsv`. Execute `python3 verify.py` with Python 3 in their containing directory. The program needs no third-party packages, enumerates all Prüfer codes for orders one through seven, independently computes canonical rooted tree codes, calculates every possible open-edge state and exact integer totals, checks the rational Bernstein coefficients, recomputes the attached 85-row certificate byte-for-byte, and confirms the two exceptional polynomial formulas and their negative derivative at full transmission. It also checks the Descartes polynomial transformations used for uniqueness of each interior maximum.

The computation reports 1, 1, 2, 4, 9, 20, and 48 rooted isomorphism types by size, and exactly two exceptional types on seven vertices. The closed-form calculations in `RESULT.md` independently derive the two exceptional polynomials from their elementary Bernoulli events. Complete finite enumeration is used **only** for the exact classification through seven vertices; there is no larger-order assertion. No independent audit was requested or performed here.
