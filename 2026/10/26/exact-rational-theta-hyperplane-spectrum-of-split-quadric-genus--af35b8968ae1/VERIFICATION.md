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

# Reproduce the exact finite computation

Place all seven computational attachments in the same directory, install Python 3 with SymPy, and run `python verify_all.py`. This reconstructs all 1,075 group orbits, sums 65,535 nonzero equations, independently checks the 15 hyperplane incidences by two implementations for each representative, recomputes every four-chart geometric-smoothness test, and checks invariance under the 72 projective transformations. The recorded output is in `verification_output.txt`.

The smooth weighted counts must be `0:5208, 1:8076, 2:2556, 3:120, 4:60`; the maximal orbit representatives must be `(10723,18)`, `(11750,36)`, `(30857,6)`. Check both the bitset and the count of qualifying planes; the checker asserts both. The certificate includes all 1,075 orbit representatives, not only the smooth subset.

The two incidence implementations share the smoothness and orbit data. This is exact computational verification of one finite domain, not independent human verification, and not a claim about curves outside that domain.
