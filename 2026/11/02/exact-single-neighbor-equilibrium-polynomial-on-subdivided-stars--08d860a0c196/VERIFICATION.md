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

# Verification of the mathematical statement

The claimed equilibrium polynomial follows for every positive arm-length vector from the degree-two XOR recurrence, the three leaf residue constraints and the exhaustive hub-action dichotomy in RESULT.md. The formula has no unspecified regularity condition. The coefficients are nonnegative because the product-minus-singletons counts only subsets with sizes other than one; the extra monomial counts an independent hub-active case.

Running `python3 verify_spiders.py` uses only the Python standard library. Its direct brute-force equilibrium predicate evaluates the strict single-neighbor response at every vertex of every candidate profile; its independent generator constructs the polynomial from the proposed expression. The actual successful check reports `PASS 704 spider instances; 4468176 binary profiles exhaustively checked`. This is a finite corroboration, not proof for infinitely many arm lengths.

The manuscript explicitly distinguishes the already known path modulo-three recurrence from the all-spider counting identity. Independent external audit is not performed.
