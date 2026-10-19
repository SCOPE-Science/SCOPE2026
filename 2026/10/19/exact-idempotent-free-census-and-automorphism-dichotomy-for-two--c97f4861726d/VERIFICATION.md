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

Execute `python3 verify.py` with Python 3; no dependencies beyond the standard library are needed. The verifier independently builds arithmetic tables for the finite fields of orders 2, 3, 4, 5, 7, 8, 9, 11, 13 and 16 using explicitly specified irreducible moduli. It then exhausts each four-parameter structure-table space, restricts to nonsingular matrices, checks the cubic-root condition and the exact proportion, and reconstructs every orbit under the full monomial basis-change group. In the cases of field order at most nine it additionally exhausts all nonzero elements of each perfect table and checks their idempotency. The terminal output is `VERIFY_OK`.

The exact integer class counts found were 1, 2, 4, 5, 10, 12, 15, 22, 31 and 46 for the listed fields in order, with precisely one automorphism-order-three class for field orders 4, 7, 13, and 16 and no such classes in the other tested fields. The proof of the general formulas is mathematical, using the projective fixed-point equivalence, irreducible cubic census, monomial basis rigidity and Burnside's lemma. Finite runs cannot alone prove the arbitrary-field theorem.

Scientific provenance and limitations are given in RESULT.md and REVIEW.md. The complete open Wei–Zou arXiv manuscript was materially compared; the journal text was not independently checked. No independent mathematical audit has been performed.
