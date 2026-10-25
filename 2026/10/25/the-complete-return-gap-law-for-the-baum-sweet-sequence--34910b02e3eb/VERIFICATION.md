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

# Reproduction
Run `python3 verify.py`. The script uses the Python standard library only. It builds valid support values from the regular-language recursion and separately evaluates the binary zero-run predicate for all integers in every dyadic prefix of size up to \(2^{15}\). It tests exact histograms for every \(1\le K\le15\) and tests numerical convergence of individual limiting masses with a prefix of size \(2^{19}\).

Observed status: `VERIFY_OK independent_integer_predicate_vs_token_recursion K=1..15`; `VERIFY_OK exact_histogram_recurrence_and_boundary_gaps K=1..15`; `VERIFY_OK dyadic_fibonacci_limit_samples K=19, bridge_m=4..12`.

These are finite checks; the unbounded result depends on the symbolic ordered-language argument and Fibonacci limit in `RESULT.md`. Mathematical independence and external certification are not claimed.
