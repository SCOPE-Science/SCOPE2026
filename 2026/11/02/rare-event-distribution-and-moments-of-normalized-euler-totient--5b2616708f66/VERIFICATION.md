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

## Reproducibility

Run `python3 verifier.py` using a standard Python 3 interpreter. The program computes Euler's totient and the sum of the \(p-1\) values of distinct prime divisors for all positive integers at most \(250000\), tests the threshold inequalities using only exact integers, and evaluates independent finite prime-counting sums. Its reported first and second moments are finite numerical sanity checks.

Theoretical verification rests separately on: the unique largest-prime decomposition; the elementary bound \(\varphi(m)\ge\sqrt{m/2}\); exclusion of repeated highest prime powers in fixed-threshold tails; the prime number theorem for the exact finite-prime-family asymptotic; and a dominated-convergence argument for all fixed positive integral moments. No finite calculation establishes the unrestricted theorem. Independent mathematical audit has not been performed.
