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

# Verification of exact matrix and polynomial identities

Run `python verify_radau3.py` in an environment with SymPy at least version 1.12. This attached file contains no data dependencies. It directly checks the scalar stability function, the nonnegative elementary fractions for all two-state generators, exact three-state rational matrix entries and the irreducible reversible witness. The checker prints the two approximate positive roots, but their existence, uniqueness and signs are proved analytically using Descartes' rule and exact integer brackets.

The rigorous scope is every finite one- or two-state CTMC generator at every nonnegative step, and the complete timestep phase of the particular three-state equal-rate pure-birth generator. The reversible generator is an exact negative witness at one step. A checker run verifies identities but does not constitute independent mathematical validation or a classification of all three-state generators.
