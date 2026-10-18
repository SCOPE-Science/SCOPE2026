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

# Reproducibility checks

Execute `python3 verify.py` in the extracted package directory. The program computes the largest prime factor exactly by an independent sieve, starts trajectories from every prime \(p\le k+2\) for odd \(1\le k\le5000\), and evaluates five consecutive map steps. It compares all closed orbits of five distinct states with the formula proved in `RESULT.md`.

The expected parameters and the corresponding \((k,q,m)\) triples are \((5,3,3)\), \((21,11,5)\), \((51,13,6)\), \((59,5,6)\), and \((1365,683,11)\). Successful execution prints two `PASS` lines and a reminder that the finite check does not prove the general theorem.

The formal reason a search over bounded starting primes can locate every period-five cycle in this particular tested parameter range is stronger than the calculation: the theorem proves every such odd-parameter cycle contains the prime \(2\). For the theorem over unbounded parameters, verification rests on the full symbolic proof and its explicit five-state construction, not on enumerated data. No independent audit has been performed.
