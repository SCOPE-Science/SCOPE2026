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

# Computational verification and reproducibility

Run `python3 verify.py` from this directory, using the Python standard library. The captured deterministic transcript is `verification_output.txt`. The checker is standalone and contains the definitions, path-block formula, recurrence, and extrema it tests; no external files or network resources are required.

The direct oracle explicitly constructs every vertex and edge of the triangular graph \(T_n=L(K_n)\). It tests the edge-open-packing relation by searching for a distinct third edge meeting both selected edges at endpoints. It enumerates every feasible edge set for each \(2\leq n\leq8\), without using the short-path classification as a feasibility test, then checks that the represented selected edges decompose uniquely into disjoint original \(P_3\) and \(P_4\) paths and matches each polynomial coefficient against the closed formula. This checks 21,517 valid packings across those values of \(n\).

Separate exact integer calculations compare the coefficient sum, exponential-formula recurrence, degree, and maximum-set coefficient for every \(0\leq n\leq60\). The final output contains `VERIFY_OK` and enumerates the case results. This is finite corroboration, not a formal infinite proof or independently authored validation. The infinite claim is proved by the bijection and combinatorial counting in `RESULT.md`.
