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

# Reproducible verification

Run `python verify.py` with Python 3 and the five accompanying program/data files in the same directory. All operations are exact GF(2) or GF(4) arithmetic. The standalone run reconstructs all 683 projective orbits, computes exact algebraic smoothness, and directly tests both classes of rational tritangents on all 27,060 smooth coefficient vectors. It compares the 33 joint-stratum counts against `expected.json`, checks every row of `orbit_certificate.tsv`, all six extremal orbits, and the rational-point/tritangent profile.

A separate computer-algebra Gröbner computation and independently varied parametrizations of all plane sections corroborated the reported criteria on the orbit representatives, but these are not needed for self-contained replay. This is self-review, not independent audit or proof of bibliographic priority.
