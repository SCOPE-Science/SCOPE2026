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

# Reproducible checks

Run `python3 VERIFY.py` from the directory containing this file. It uses only Python's standard library. The verification recomputes exact Franel integers for each tested prime-power index, calculates the leading quotient modulo the prime, independently evaluates even Bernoulli numbers as exact fractions, and checks separate divisible and nondivisible index blocks. The completed run printed:

`VERIFY_OK: 32 exact prime-power comparisons; Bernoulli and residue-block checks`

The calculation covers primes through \(79\), with prime powers at most \(1000\), and five extra residue-block comparisons. It does not and cannot prove the infinite assertions; those rely on the written Jacobsthal/Lucas and Bernoulli-polynomial argument in the result. In particular the checker does not establish originality or independent audit.
