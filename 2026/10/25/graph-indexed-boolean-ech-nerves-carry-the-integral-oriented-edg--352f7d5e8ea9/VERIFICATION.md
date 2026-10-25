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
# Reproduction

Run `python3 verify.py` using Python 3.8 or later, no third-party libraries. The program directly builds all Čech simplices from Hamming-radius-one witness balls, checks the cone and the asserted relative two-simplices, independently computes exact mod-two homology for bounded graph sizes, and compares signed fixed-simplex Lefschetz traces with the oriented-edge trace for explicit automorphisms.

Expected success counts from the embedded program are 121 graph instances, 121 cone/relative-face tests, 115 independent reduced-homology calculations, and 293 signed Lefschetz comparisons. The all-size theorem is proved separately by a uniform relative-chain argument. Passing bounded tests neither establishes uniqueness in the literature nor constitutes independent scientific validation.
