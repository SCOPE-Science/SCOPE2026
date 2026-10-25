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

# Exact arithmetic verification

The source code and captured outputs in this package are complete and directly runnable in C99 and Python 3. The C program uses independently implemented small-characteristic finite-field arithmetic and divisibility checks. The Python program independently constructs all reducible quintic coefficient patterns as products and tests closed-point gradients with bit-linear algebra. Both yield 67,608 valid coefficient forms with the singular center fixed and agree on each local singularity type and the rational point count histogram. The Python computation records 75 arithmetic splitting profiles of the three rational fibres and explicit witnesses for all 34 realized unordered triples; these sum exactly to 67,608. Its complete table is included in CSV form.

Finite exhaustive computation certifies the stated bounded coefficient-domain facts only. The geometric assertion that this domain describes the smooth normalization and its degree-three map relies on the genus formula, local node/cusp criteria, and uniqueness of the trigonal pencil as explained in RESULT.md. No independent audit has occurred.

Reproduce using `cc -O3 -std=c99 source_checker.c -o source_checker && ./source_checker` followed by `python3 independent_checker.py`.
