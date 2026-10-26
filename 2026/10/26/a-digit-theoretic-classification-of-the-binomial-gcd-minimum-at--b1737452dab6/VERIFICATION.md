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

# Reproduction and boundaries

The source `verify.py` uses only Python standard-library integer arithmetic. Execute `python3 verify.py` from the extracted package. It computes the true minimum of \(\gcd(6p,\binom{6p}{k})\) for every \(2\le k\le3p\) and every prime \(5\le p\le151\), obtaining agreement on 34 primes. Separately, for the 165 primes \(7\le p\le997\), it computes the gcd's supported prime factors using a digit-by-digit implementation of Lucas's criterion, then minimizes over the same complete finite index range. The latter is independently implemented from integer binomial arithmetic. Both compare against the theorem's ternary/binary digit prediction. The exception \(f(30)=6\) is explicitly included.

These checks are finite validation only. Unbounded correctness rests on the proof's Lucas/Kummer arguments. In particular, no finite amount of enumeration proves the density statement, which instead follows from Fibonacci-word counting and the prime number theorem. These checks and their limitations are not independent validation or an external audit.
