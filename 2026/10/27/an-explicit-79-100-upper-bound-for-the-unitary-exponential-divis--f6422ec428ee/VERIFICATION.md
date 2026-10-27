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
# Reproducibility and limits

Run `python3 verify_upper_079.py` using Python 3.9+ and the standard library. It uses only exact integer and rational arithmetic. It prints the 26 rational-bin frequencies and conservative moment-failure bounds, then checks the strict inequality \(\operatorname{dens}\{\sigma^*<\sigma^{(e)}\}>21/100\) at the level of an integer numerator and denominator. An actual replay printed `VERIFY_OK`; the exact stdout is supplied in `certificate_output.txt`.

The program verifies the finite arithmetic certificate; it does not certify the analytic passage to all primes. The latter is proved in `RESULT.md` by multiplicativity, prime-power inequalities, the integral test for a convergent prime sum, and a limiting density argument. It does not evaluate the unknown density exactly. Independent audit has not been performed.
