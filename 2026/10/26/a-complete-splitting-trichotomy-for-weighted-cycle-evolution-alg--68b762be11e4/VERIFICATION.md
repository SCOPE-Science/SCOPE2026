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

# Reproducible finite-field checks

Run `python3 verify.py` and `python3 direct_f4_check.py`, with no external dependencies. Both scripts completed successfully in the checked execution and printed `VERIFY_OK` and `DIRECT_F4_OK` respectively.

The exponent-arithmetic checker exhaustively checks all \(3^n\) weighted cycles in dimensions \(1\le n\le6\), class membership and representative isomorphisms; it computes all automorphisms and their composition for both normal forms in dimensions \(1,2,3,4,5,6,8,10,12,18\). Its unbalanced six-, twelve- and eighteen-dimensional automorphism groups have orders \(9,18,27\), respectively, each cyclic. The separate direct-field checker implements multiplication in \(\mathbb F_4\) as two-bit polynomial arithmetic modulo \(t^2+t+1\), rather than using the recurrence to decide compatibility, and checks every monomial map over dimensions \(2,4,6\). For the unbalanced six-cycle all three lifts of the even rotation have order nine.

Finite checks do **not** establish an all-dimensions theorem or independence of the mathematical assessment. The complete proof is the monomial recurrence, alternating-exponent obstruction, explicit lift and group-theoretic splitting argument in RESULT.md.
