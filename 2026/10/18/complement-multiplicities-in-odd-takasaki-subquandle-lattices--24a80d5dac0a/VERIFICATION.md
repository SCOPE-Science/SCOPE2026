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

# Reproduction and limitations

Run `python3 verify.py`. The checker uses only the Python standard library and independently enumerates cosets, subgroup closures, disjointness, and generated joins for representative odd cyclic and finite abelian groups. It compares those counts with the two polynomial formulas and the prime-support closed formula. Expected final line: `CHECKER_OK`.

The complete infinite-family statement follows from the symbolic coset classification, cyclic quotient criterion, and primewise summation in RESULT.md. The finite tests do not establish the infinite result, the absence of a published equivalent, or independent certification.
