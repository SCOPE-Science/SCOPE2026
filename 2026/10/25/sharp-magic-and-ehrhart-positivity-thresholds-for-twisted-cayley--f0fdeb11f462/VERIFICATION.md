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

# Verification

Run `python3 check_twisted.py` using Python 3 standard library only. The program independently counts lattice points at integer heights, reconstructs the cubic with exact rational finite differences, computes the magic basis by triangular inversion, and verifies the formulas, thresholds, and first-volume examples for 3,600 ordered parameter pairs and multiple larger dilations. Observed output:

`TWISTED_RECTANGULAR_CAYLEY_OK cases= 3600  min_magic_failure= (97, (1, 8))  min_ehrhart_nonpositive= (141, (1, 10))`

The finite domain does not replace the symbolic proof of all positive integral parameters in RESULT.md. The smoothness and complete positivity results are proved there. Independent mathematical auditing and external certification have not occurred.
