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

# Verification of the exact divisor-lattice pencil

Run `python verify_gcd_lcm_sum.py` after installing the pinned `requirements.txt`. The independent test routine forms matrices entry by entry from integer gcd and lcm, computes exact determinants using symbolic arithmetic, and compares the results with the proposed factorization.

Observed run with SymPy 1.14.0:

```
VERIFY_OK: 241 independent exact t=1 determinants; 272 additional integer pencil determinants; 14 exact symbolic characteristic polynomials
```

The tests include \(n=1\), prime powers, squarefree integers, arbitrary mixed exponents, and odd-support perfect-power cases where singularity occurs. The mathematical proof establishes all \(n\ge1\); finite test coverage is not exhaustive over positive integers. The published prime-power formula is prior literature, not an independently discovered local lemma. An external mathematical audit has not been performed.
