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

# Reproducibility and mathematical limits

Run `python3 verify.py` from this directory using Python 3's standard library. The verifier executes the actual exact integer inclusion--exclusion formula for ordered nontrivial factorization counts and the positive Stirling transform of the published sum-system formula. It checks all positive integer compositions of total exponent sum from two through twelve, in all support sizes, and all legal one-unit exponent transfers; each factorization length from two up to the total and each sum-system dimension from two up to the total must increase strictly. It also enumerates bounded exponent-allocation matrices directly in 279 small cases and checks strict inequalities under prime-exponent splitting. The known test value of fourteen ordered two-part sum systems for an integer with exponent shape \((2,1)\) is included.

The packaged check is expected to print `VERIFY_OK balancing_transfers=16422 strict_factor_comparisons=169910 strict_sum_system_comparisons=169910 strict_split_comparisons=13053 direct_matrix_checks=279`. The checks test the combinatorial implementation, not all possible integers.

The proof's infinite assertions rely on the exact prime-exponent assignment interpretation, the Pieri rule and Young/Kostka dominance criterion for complete homogeneous symmetric polynomials, an explicit strictly positive two-variable Schur coefficient, the injection under prime support splitting, and the published identity between ordered sum systems and factorization-length counts. No computational output is used to infer an infinite statement, and no independent audit has been performed.
