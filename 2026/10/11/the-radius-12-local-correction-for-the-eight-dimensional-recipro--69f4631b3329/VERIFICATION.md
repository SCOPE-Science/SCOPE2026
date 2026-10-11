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
The exact finite verification is contained in `verify_cutoff.py`. It reconstructs the focal rational edge field from the displayed polynomials, verifies every local \(R=12\) inequality using the 26 published integer values, evaluates the fixed \(|x|^2=11\) obstruction for \(R\le10\), constructs the 23-orbit \(R=11\) matrix, checks its symmetry by orbit detailed balance, and evaluates the negative rational quadratic certificate. All arithmetic is exact.

The script reports the smallest finite \(R=12\) local margin as \(3/2019151\), a positive exact deficit at the norm-11 obstruction, and a strictly negative exact quadratic form for the \(R=11\) matrix. The infinite exterior statement for \(|x|^2\ge13\) is the symbolic Proposition 6.2 of arXiv:2610.05421v1; its displayed polynomial proof was inspected and is not replaced by finite enumeration.

No independent audit has been performed.
