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

Execute `python3 verify.py` using a standard Python 3 interpreter; no nonstandard packages are needed. The script independently builds divisor sets, computes the gcd-incidence graph and counts perfect matchings by an integer bit-mask dynamic program. For small cases it also enumerates all permutations independently. It then tests the theorem's squarefree-support criterion and the separately derived progression congruences.

The checked domain was \(1\le n\le180\) with \(\tau(n)\le12\), \(1\le a\le14\), and \(1\le b\le5\), plus six separate arbitrary-target-set examples. The observed output was:

```text
VERIFY_OK cases=12320 odd=220 unique=220 zero=3309 six_examples=8 arbitrary_sets=6 independent_brute=yes
SIX_EXAMPLES_FIRST [(3, 1, 1), (3, 5, 1), (6, 1, 1), (6, 5, 1), (9, 1, 1), (9, 5, 1), (12, 1, 1), (12, 5, 1)]
```

The stand-alone mathematical argument, rather than a finite bound on \(n\), establishes the theorem. The program does not prove exhaustive novelty, nor does it determine all even matching multiplicities. No independent mathematical audit has been performed.
