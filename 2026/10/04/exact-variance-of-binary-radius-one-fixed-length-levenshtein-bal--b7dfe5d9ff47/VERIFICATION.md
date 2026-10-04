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

The proof is symbolic and valid for every \(n\ge1\). The attached `artifacts/verify.py` provides two independent finite checks of the critical identities.

1. Literal channel check: for every binary word of lengths \(1\) through \(10\), construct every output obtained by one deletion followed by one insertion, deduplicate outputs, and compute the exact rational mean and variance. This covers 2,046 centers.
2. Moment-recurrence check: independently iterate the exact \((R,Q)\) moment recurrences through \(m=200\), sum the covariance formula directly from all-zero intervals, and compare the assembled variance with the closed form.

Expected replay command:

`python artifacts/verify.py`

Expected terminal line:

`VERIFY_OK direct_binary_words=2046 n<=10 recurrence_m<=200`

The finite checks do not establish the infinite statement; they corroborate the all-length proof and catch algebraic or normalization errors. No central limit theorem, exact tail law, higher-radius result, or nonbinary variance formula is verified or claimed.
