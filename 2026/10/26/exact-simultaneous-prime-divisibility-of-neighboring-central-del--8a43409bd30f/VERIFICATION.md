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

# Reproducible checks and limits

Execute `python3 verify.py` with the Python standard library. The verifier first constructs \(D_0,\ldots,D_{2401}\) by the integral three-term recurrence, independently of the Lucas formula. It compares its first 45 entries against the binomial-square sum and then tests nineteen full prime-power counting blocks: \(p=7\) through four digits; \(p=11\) through three digits; and \(p=13,17,19,23,31,43\) through two digits. Every tested block is enumerated directly over all indices, and the modular digit product is checked at every index including the endpoint \(p^L\). Midpoint congruences are checked independently using binomial-square sums for primes \(p\equiv3\pmod4\), \(7\le p\le199\).

Actual local execution returned `VERIFY_OK: 45 independent binomial-square identities; 19 complete consecutive-pair blocks; full Lucas checks; prime-3-mod-4 midpoint checks through 199.` The exact counts for \(p=7\), \(L=2,3,4\), were \(6,84,846\). These are finite tests; the proof of the universal count and density-one conclusion is provided in `RESULT.md`.
