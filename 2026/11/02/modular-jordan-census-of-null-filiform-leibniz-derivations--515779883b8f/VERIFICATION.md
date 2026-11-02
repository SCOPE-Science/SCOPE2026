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

# Verification protocol

Run `python3 verify_jordan.py` in a directory containing the code. It requires only a Python 3 standard library and does not retrieve external data. Its final expected line is:

`NULL_FILIFORM_MODULAR_JORDAN_CENSUS_OK 20`

The program independently constructs derivation matrices from the basis multiplication table, calculates ordinary finite-field ranks of shifted matrix powers, derives Jordan partitions from their kernel dimensions, and compares profile frequencies conditional on the first diagonal parameter against the proposed closed expressions. It also checks the combined nullity distribution and tests genuine extension fields of cardinality four and nine.

The file `check_output.txt` records each exhaustive finite configuration and its nullity counts. Finite exhaustive checks are restricted to the tested dimensions and fields, and do not establish the general theorem without the proof in `RESULT.md`.

The mathematical argument relies on the triangular unit-polynomial similarity over characteristic \(p\), using divisions only by \(uj\) with \(u\ne0\) and \(p\nmid j\), and then on the Jordan kernel structure of powers of the nilpotent shift. No numerical approximation or probabilistic primality calculation is needed. No independent mathematical audit has been performed.
