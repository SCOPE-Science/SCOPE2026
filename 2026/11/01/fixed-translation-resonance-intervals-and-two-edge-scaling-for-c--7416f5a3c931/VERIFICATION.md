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

The analytic proof derives all quantified conclusions from the published rational-rotation criterion and explicit algebraic calculations. It does not treat computer output as a proof of an infinite assertion.

Run `python check.py` with the Python 3 standard library. During this review the script completed: 1,493 exact coprime-parameter checks (coefficients, first missing index, and derivative identities) and nine 90-digit Decimal endpoint experiments at both parameter boundaries. It prints a two-part PASS report on success. These tests verify the computation implementation on the declared finite domain only.

The proof explicitly covers the endpoint \(p=q-1\) separately, including \(q=2\). Residual limitations are lack of denominator-uniform error bounds and lack of independent priority or scientific audit. No external validation has been undertaken.
