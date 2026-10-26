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

# Reproducible checks

Run `python verify_defect.py` with Python 3.10 or later after installing the dependency from `requirements.txt` (SciPy). The script uses no files outside this package. Its successful outcome is `PASS 250 finite rational and analytical comparisons`.

The script computes exact rational greedy-matching probabilities on finite paths with 7, 9, 11 and 13 edges, using the earliest-first-clock recursion. It tests reflection, exact probability ranges, and alternating response signs against an equal-rate finite path. On a separate 25-edge path it compares four defect rates and five distances against independently evaluated infinite-line integrals. It checks factorial bounds and stable normalized triangular-integral ratios at increasing distances for three nontrivial rates.

The finite-path rational recursion and floating-point quadratures are independent implementations of the model; they are not an infinite proof. The infinite construction, cavity equation, monotonicity and triangular concentration argument are in RESULT.md. The calculation does not establish independent certification of originality or of the mathematical proof. The main originality limitation is an inaccessible highly related 1998 full text about heterogeneous dimer adsorption; no claim of exhaustive priority is made.
