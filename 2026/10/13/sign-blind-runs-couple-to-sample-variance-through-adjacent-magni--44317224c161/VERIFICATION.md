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
The proof was checked algebraically by conditioning on the magnitude vector and expanding the centered quadratic form. For each adjacent run indicator, every quadratic sign product is orthogonal except the product on that same adjacent pair; its covariance is exactly \(-1/2\), which yields the stated formula after the factor from sample-mean centering.

`verify.py` performs exact rational-arithmetic replay. It reports `VERIFY_OK` after 27 deterministic sign-order checks over 3,968 sign vectors, 4 unconditional checks over 9,324 joint magnitude/sign states (including tied magnitudes with sign-independent tie-breaking), 999 uniform order-moment checks through sample size \(1000\), and 8 chronological specialization checks. It also verifies zero covariance with the uncentered second moment in the enumerated cases.

The computation is supportive rather than a substitute for the general proof. It does not establish any claim outside the stated symmetric sign--magnitude setting, does not test asymmetric parent laws, and does not imply a full joint-distribution or positive-association theorem.
