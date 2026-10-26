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

Execute `python3 verify.py` with Python 3.9+ standard library. The checker performs the following exact operations: re-evaluates every witness in the ten-element bridge; tests that 1001 does not appear among all ordered sixfold sums via a bounded bitset; reconstructs both fractional-part candidate sets via integer square-root comparisons; confirms two sixfold polynomial coefficients vanish; and independently enumerates Lucas-index subsets to identify 171 ambiguous integers through 1006. The observed output is:

```text
VERIFIED: Lucas ambiguity prefix 171 integer witnesses 997..1006,
exact sixfold gap 1001 by independent bitset and radical coefficient tests
```

The proof of all-integer coverage follows from the exact ten-number bridge and the gap alphabet {4,7}; the proof that no smaller fixed summand count is an asymptotic basis follows from a counting bound. Computations certify only the stated finite intervals and exceptional point. The Lucas ambiguity parametrization is a cited theorem, not independently reproved by the script. Independent external verification has not been performed.
