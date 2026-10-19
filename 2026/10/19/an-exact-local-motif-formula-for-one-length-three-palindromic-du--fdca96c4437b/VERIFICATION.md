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

Run `python3 verify.py` using Python 3 standard libraries. The program constructs every exact-one length-three palindromic descendant directly, checks the four-motif count, independently compares the consecutive equal-descendant site edges, and verifies uniform-alphabet means as exact rational numbers.

Exhaustive coverage: alphabets of size 2 at lengths 3–14, size 3 at lengths 3–11, size 4 at lengths 3–9, and size 5 at lengths 3–7; total 745,596 tested words.

Observed output: `PALINDROMIC_LENGTH3_FORMULA_PASS words=745596 q=2..5 ranges=(14,11,9,7)`.

The finite checker cannot by itself certify the all-length theorem; the all-length reasoning is in RESULT.md. Independent mathematical audit has not been performed.
