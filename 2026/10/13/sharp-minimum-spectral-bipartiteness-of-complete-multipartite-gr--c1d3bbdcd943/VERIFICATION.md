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
# Verification

The all-parameter proof is analytic. Its critical steps are:

1. the nonzero adjacency spectrum of a complete multipartite graph equals the spectrum of the symmetric quotient \(B=uu^\top-D\);
2. rank-one interlacing yields \(\theta_i\le -n_{i-1}\) for \(2\le i\le r\);
3. trace zero converts the target sum into \(-\sum_{i=2}^{r-1}\theta_i\);
4. equality forces \(-1\) with multiplicity at least \(r-2\), and solving \((B+I)x=0\) shows this happens only when at least \(r-1\) parts are singletons;
5. the complete-split quotient has \(-1\) with multiplicity \(r-2\) and two remaining roots whose sum is \(r-2\).

`verify.py` independently stress-tests the statement for every nondecreasing positive multipartition with \(3\le r\le7\) and \(r\le N\le18\). It uses a pure-Python Jacobi eigensolver and checks both the inequality and uniqueness of equality.

Replay output:

`ALL CHECKS PASSED; parameter_cases=70; partition_cases=1077; equality_cases=70; max_order=18; max_parts=7; max_split_root_error=1.6e-14`

The computation is finite and is not used as proof of the infinite theorem. Numerical tolerance is used only in the finite stress test. No independent audit has been performed.
