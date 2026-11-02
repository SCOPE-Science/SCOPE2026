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

# Verification and reproducibility

The self-contained `verify.py` uses only Python's standard library. Run it with `python3 verify.py` from the directory containing this file and the script.

The recorded execution succeeded with:

`VERIFY_OK cube_class_levels=2..5 one_factor_cases=108 equal_unit_cases=36 normalization_pairs=6400`

It checks the cubic-unit criterion modulo powers \(3^2\) through \(3^5\); the unit-value coverage for unit-plus-three-unit forms with six choices of each unit coefficient modulo nine across three moduli; the two equal-unit alternatives modulo \(3^5\); and 6,400 exact coefficient normalization identities. The test relies on finite modular arithmetic and does **not** prove surjectivity over \(\mathbb Z_3\), the infinite Hensel lifts, or density of integer-coordinate quotients. Those steps are supplied by the mathematical proof in `RESULT.md`.

The proof's key infinite claims were separately checked from their exact expansions: \((1+3t)^3\), \(\alpha(t+3s)^3+\beta\), the surjectivity criterion for polynomials with unit derivative modulo three, the three coefficient-valuation residues, and continuity under integer approximation. The proof uses no external computational certificate beyond the two standard mathematical facts of Hensel's lemma and completeness/density of the 3-adic integers.

This is a self-review, not independent validation. The precise journal-version and bibliographic-priority questions remain unresolved.
