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

Run `python3 verify.py` using Python 3 standard library. Its reference output is `verification_output.txt` and begins with `VERIFY_OK`.

The program factors integers exactly, compares the finite criterion with divisor counts across the first 100 positive terms in each predicted universal progression with \(1\le A\le60\), checks the square-class formula at each odd prime less than \(200\), and checks the \(p=109\) discrepancy against the numerical prediction of Conjecture 2 in Merca (2022). These computations were executed against the embedded file's bytes.

The infinite argument is mathematical rather than computational: the fixed-valuation product gives sufficiency; an explicit square times a prime in a CRT class defeats the odd-product case; and the unique modulo-four factor reduces the remaining case to \(p t^2\equiv B\pmod A\). Dirichlet's theorem provides the prime in the CRT class. No upper cutoff in the code is used as a theorem hypothesis.

No independent audit or validation has been performed.
