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

# Reproducibility and verification

Run `python3 verify.py` from this package, with the Python 3 standard library and no third-party dependencies. All tree and polynomial calculations are exact integers or fractions. The complete Prüfer enumeration gives counts 1, 1, 2, 3, 6, 11, 23 for unlabelled trees of orders 2 through 8. The script checks an exact polynomial coefficient nonnegativity certificate for every universal-optimality assertion; in the two exceptions it independently certifies disjoint rational-parameter optimal sets and both threshold witness polynomials.

The checker was run successfully against the packaged source. Its finite exhaustive checks prove only the stated first-eight-vertex classification. No claim beyond eight vertices, independent validation, or publication-priority certification is made.
