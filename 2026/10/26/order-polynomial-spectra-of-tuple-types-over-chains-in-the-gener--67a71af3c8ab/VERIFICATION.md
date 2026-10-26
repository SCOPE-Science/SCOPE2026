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

# Reproducibility and limits

Use a standard Python 3 interpreter. Execute `python3 verify.py`; its expected complete output is embedded as `verification_output.txt`.

The checker lists all labelled strict posets up to four points and builds the associated endpoint posets. For each, it computes surjective isotone-map coefficients through strict chains of order ideals (no symbolic algebra dependency), and evaluates the resulting integer binomial polynomials. It verifies all coefficients at arities \(1,2,3,4\), then checks the displayed closed formulas for arities \(1,2,3\) at eleven chain lengths each.

A distinct exhaustive procedure enumerates all possible ternary pair relations on the enlarged vertex set, closes each under transitivity, rejects cycles or any new comparability inconsistent with its prescribed ternary matrix, and counts the remaining labelled extensions. This direct method does not consult the endpoint representation. It matches the polynomial count on \(15\) configurations and individually checks the incomparable/ascending/descending counts for \(6\) parameter sizes (\(18\) comparisons).

Expected terminal indicator: `ALL_TESTS_PASS`. The finite checks support the formulas but do not establish the theorem for unbounded arity or chain length; that depends on the written combinatorial proof. No external or independent validation has been undertaken.
