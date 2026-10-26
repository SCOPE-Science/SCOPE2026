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
# Reproducibility checks

Execute the accompanying `verify.py` using Python 3's standard library, without dependencies or network access.

The verifier performs two independent enumerations of all strictly ordered primitive positive triples with order at most \(80\), compares the enumerated sets, computes the conjectured period by exact integer greatest common divisors, checks its evenness, computes the recurrence forward from its prescribed initial data through \(N+m\), and verifies the \(m\) affine-shift equalities for every triple.

Observed output: `VERIFY_OK`; 11,052 triples; 10,977 outside the \((p,q)=(1,2)\) family; sum of candidate periods 84,412,414; maximal-period tuple `(13, 26, 41, 36556)`; checkpoint digest `d95345c93044969f924f10fe37245a3424b72994f639951da7ff37365777058c`.

The infinite-period assertions follow by deterministic recurrence induction from those finite equalities. The least positive period follows from integer-valued differences and divisibility. The result is finite in its parameter coverage (order at most \(80\)) and infinite only in its iteration quantifier. These checks are not an independent external audit.
