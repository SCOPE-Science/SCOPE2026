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

# Reproduction of the exact coefficient proof

Run `python3 verify_hartogs.py` using a standard Python 3 interpreter in the directory containing `RESULT.md`, `verify_hartogs.py`, and `BERNSTEIN_CERTIFICATE.json`. The program compares the exact diagonal numerator coefficients supplied by the kernel formula of Edholm–Mathew with the asserted cubic polynomial formula at four nodes in each residue class and verifies the entire interval-positivity certificate with rational arithmetic.

The infinite parameter extension uses the independent mathematical argument that, for fixed remainder modulo five, every numerator coefficient is a polynomial of degree at most three in the quotient parameter. Its proof is the floor-block decomposition and power-sum formulas in `RESULT.md`, not an assumption inferred from finitely many calculations.

The Bernstein positivity test uses the eight rational subdivisions of the closed interval and confirms 384 strictly positive rational coefficients. The certificate is self-contained and does not require third-party data or installed mathematical libraries. Root counts follow from reciprocal polynomial symmetry, not numerical root enumeration. The source Bergman-kernel formula is taken as established in the cited paper, not reproved here. Independent validation has not been performed.
