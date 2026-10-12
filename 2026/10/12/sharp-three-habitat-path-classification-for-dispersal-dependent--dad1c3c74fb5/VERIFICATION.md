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

Run `python3 verify.py` with Python 3 and SymPy installed. The script performs exact symbolic checks of the two general determinant identities; verifies the two swapped arrangements for rates 6, 5, 1; checks that 5 is the largest eigenvalue at the claimed threshold 4/3; and uses rational root-isolating intervals at dispersal rates 1 and 2 for the opposite strict rankings. It also checks rate-swap conjugation on a two-vertex path.

The mathematical proof of uniqueness, sharp parameter inequality, and universal ranking for every real positive dispersion rate is contained in RESULT.md. Symbolic finite checks corroborate algebraic steps but do not provide a separate infinite-domain theorem. The result has not undergone independent audit.
