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

Execute `python3 verify_square_zero_poe.py` using only Python's standard library. It outputs one row per \(1\le n\le10\), finishing with `VERIFY_OK_SQUARE_ZERO_POE_BIVARIATE_TREE`.

For all \(1\le n\le10\), the implementation enumerates every partial domain, every weakly nondecreasing image tuple, and rejects tuples violating extensiveness or having an image value in the domain. It compares the resulting exact counter \((d,r)\) with the theorem. It independently enumerates queue words by a three-integer state (unassigned sources, domain count, target count), including every admissible sink-consumption size, and compares all coefficients. It checks Narayana marginals and Catalan totals. For \(11\le n\le100\) it performs integer-arithmetic consistency checks of the formula's marginals and totals, without claiming exhaustive transformation enumeration in that range.

Direct square-zero totals for \(n=1,\ldots,10\): \(1,2,5,14,42,132,429,1430,4862,16796\). The tests completed successfully. These checks are finite and do not constitute an independent assessment of the all-degree tree-bijection proof, which remains the source of the universal claim.
