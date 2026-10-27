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

# Verification record

Run `python3 verify.py`. The standalone script directly enumerates ordered divisors of \(2^a p^b\) over \(11{,}323\) distinct parameter cases, comparing actual gap closure against the theorem; it also exercises long exponent ranges, four known Fermat primes and the first failing adjacent pair \(27,32\).

The universal proof uses explicit symbolic ordering of divisor layers and shells, plus an induction for all \(b\) in the \(a\le4\) branch. Tests cannot certify infinitely many parameters or literary novelty. The review reported here is not an independent audit.
