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

# Reproducibility

Execute `python3 verify_cyclic_septic.py` (Python standard library, no external dependencies). It constructs the exact bivariate polynomials over \(\mathbb F_5\), checks all six source-character calculations by two distinct expansions, checks the permutation's rank drops, and checks the invariant-coordinate identities. On success it prints six `CARTIER_COEFFICIENT_OK` lines, a `STRATA_OK` line, and a `MODULI_OK` line.

The symbolic coefficient identities imply the corresponding Cartier formulas over \(\overline{\mathbb F}_5\); the finite combinatorial checks concern all six possible characters, not a limited sample of branch parameters. The local valuations, genus, and semilinear interpretation are mathematical steps presented in RESULT.md and should be checked along with the program. This verification does not inspect historical literature exhaustively or provide independent external certification.
