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
# Verification of the stated classification

The included `verify.py` uses only Python's standard library. It reconstructs \(G_s\) directly and computes characteristic polynomials by exact-rational Newton identities, without using the quotient determinant formula as an input. It independently computes exact nullity by rational Gaussian elimination for \(1\le s\le20\), checks the integer-root identity and candidate roots over \(1\le s\le2000\), and checks the \(s=6\) relation-parity parameterization on an integer coefficient grid.

Observed result from executing the included script:

`VERIFY_OK exact_graph_charpolys=20 exact_nullities=20 integer_root_scope=2000 exceptional_roots=[(6, 3)] exceptional_integer_relations=1681`

Reproduction: `python3 verify.py` in the directory containing the extracted files.

**Proof boundaries.** The infinite graph-family classification is established in `RESULT.md` by a complete quotient decomposition, the rational-root theorem, the irreducible-cubic Galois argument, exact treatment of \(s=6\), and continuous Kronecker phase approximation. Finite enumerations are corroboration only. No claim of independently certified correctness, exhaustive literature uniqueness, or quantitative transfer time is made. Independent audit has not been performed.
