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

# Verification and limitations

The included `verify.py` computes complete positive divisor sums through 250000 by a divisor sieve and independently compares all 274 prime-square candidates against the strict criterion. It reports exactly 98 abundant and 176 deficient candidates, no mismatches. The same program rederives exact prime-counting values at 12 larger input scales and computes the stationary phase and boundary constants.

Observed console prefix:

`EXACT_CLASSIFICATION_OK bound=250000 tested=274 abundant=98 deficient=176 first=[18, 36, 72, 100, 144, 196, 200, 288, 392, 400, 576, 784]`

`PHASE_CONSTANTS smin=2.745166004061 liminf=16.196691106368 limsup=16.684681757896 boundary=16.684681757896/16.684681757896`

The finite tests and decimal approximations do not prove the asymptotic or originality. The unbounded mathematical step is the uniform prime number theorem combined with elementary geometric-tail estimates. No independent audit or validation has been performed.
