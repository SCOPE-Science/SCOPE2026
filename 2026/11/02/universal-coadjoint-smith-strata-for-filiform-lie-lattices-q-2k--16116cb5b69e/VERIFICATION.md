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

`check.py` is a standalone Python 3 checker requiring no nonstandard packages. Run `python3 check.py` alongside this file and compare its standard output to `CHECK_OUTPUT.txt`.

The program derives the commutator matrix from the stated brackets and checks the original matrix, not the asserted normal form. Over integer quotient rings it computes the matrix's Smith valuations by modular row and column reduction; over equal-characteristic truncated polynomial rings it expands the full matrix over the prime field and computes rank independently. It iterates every functional in each listed finite test configuration, verifies the predicted elementary-divisor list where applicable, and verifies every coefficient of the finite-ring enumerator.

There are 17 exhaustive configurations. Checked integer quotients include prime fields, lengths two through four over residue characteristic two, and length two over residue characteristic three. Equal-characteristic quotients include both length two and length three, plus genuine residue-field extension arithmetic over \(\mathbb F_4\). The last output line is `FILIFORM_Q_CHAIN_KIRILLOV_OK 17`.

The checks do not enumerate arbitrary chain rings, arbitrary dimensions, or all irreducible group representations. Generality is established by the algebraic reduction and counting proof. No external or independent validation has been performed.
