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

# Reproduction and limits

Run `python3 verify.py` with Python 3 and no third-party dependencies. The script implements direct floor recursion, a separate divisor-convolution computation, and independent exact convolution inversion. Its completed output is embedded as `verification_output.txt`. The source code does not access external data or services.

The direct recurrence is compared with the independently computed divisor recurrence at the first 700 terms. The Liouville-sign/zero-threshold, parity, and exact prime-fiber predictions are checked at each index from 2 through 100000. A separate inverse for the arithmetic function \(2\varphi-\delta\) is computed for indices through 12000 and compared with the nonnegative formula for the Liouville twist and with the recovered recurrence. All checks in the embedded output passed.

The infinite theorem is established by a formal coefficient-positivity proof, not extrapolated from the finite checks. A separate external/independent audit has not been performed.
