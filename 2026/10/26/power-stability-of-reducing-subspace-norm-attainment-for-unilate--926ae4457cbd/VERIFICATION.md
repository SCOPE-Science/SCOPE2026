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

# Verification of the new claim

Run `python verify.py` with Python 3.10 or later; it uses the standard library only. Its exact `fractions.Fraction` arithmetic checks telescoping products, both residue components of the explicit recovery example, and many finite residue reindexings. The actual packaged script reported `PASS: 11538 exact rational checks (finite examples and residue blocks).`

The full infinite-dimensional validity follows from the six proof steps in RESULT.md, particularly the commutant reduction of every reducing subspace. No finite test establishes the universal claim. All weights are assumed strictly positive and uniformly bounded. Independent audit: not performed.
