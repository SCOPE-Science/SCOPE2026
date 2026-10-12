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
# Verification and limits
The file `verify.py` uses only Python's standard library. Its smallest-prime-factor sieve is independent of the factor-ratio proof: it reconstructs the prime-power factorization of each positive integer \(n\le10^6\), multiplies \(p^{a-1}(p-1)\) for the totient and \(p^a+1\) for the unitary sum, and checks both sides as exact integers.

Observed output:

```text
VERIFY_OK limit=1000000 omega_le2_checked=367461 omega_le2_hits=[3, 35, 99] all_hits_count=29 first_support3=1045 all_hits_first=[3, 35, 99, 1045, 4743, 8307, 8613, 24871, 29029, 50065, 58435, 64285, 87685, 110691, 137885]
```

The unrestricted proof is the local-ratio argument in RESULT.md, including all prime powers and the \(q=5\) congruence restriction. The finite search is limited to the displayed range; it neither establishes asymptotics for larger support sizes nor serves as a substitute for the proof. Independent external validation has not been performed.
