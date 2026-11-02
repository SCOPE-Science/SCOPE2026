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

Run `python3 verify_modular.py` with the Python standard library and `python3 verify_independent.py` with SymPy. They compute the full 3906 parameter space and all 31 lines for each of the 800 smooth members, testing geometric smoothness by distinct methods. Both completed and produced `MODULAR_VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. `spectrum.csv` contains the full 15-row count; `extremizers.csv` contains every marked equation attaining sixteen bitangents.

The correctness of the geometric discriminant criterion and the bitangent Veronese equivalence is explained in `RESULT.md`; finite brute force does not substitute for these lemmas. The calculation does not establish anything about quartics outside the specified family or independent priority of the data. Independent audit: not performed.
