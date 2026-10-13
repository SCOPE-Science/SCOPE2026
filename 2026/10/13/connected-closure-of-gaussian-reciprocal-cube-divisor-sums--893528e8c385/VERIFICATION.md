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

# Reproducible checks and proof boundary

Run `python3 verify.py`. The checker uses standard-library integer square roots, exact rational fractions, and deterministic trial division to verify all seventy-three primes congruent to \(1\pmod4\) and their spacing ratios, covering each integer norm from \(29\) through \(8\cdot10^9\). It also proves the five exceptional overlap inequalities below norm \(29\), using rational enclosures for \(n^{-3/2}\) based on \(\lfloor\sqrt{10^{16}n}\rfloor\).

Observed result:

`EXACT_CERTIFICATE_OK witnesses=73 start=37 last=8856541433 small_cases=5 initial_norms=13`

The all-larger-norm step is proved separately by Theorem 1.2 of Bennett--Martin--O'Bryant--Rechnitzer, *Explicit bounds for primes in arithmetic progressions*, applied to \(\theta(x;4,1)\) for \(x\ge8\cdot10^9\). The interval-filling lemma and the Gaussian Euler-product identity are mathematical proof steps in RESULT.md, not outputs of finite enumeration. No independently executed or independently authored audit is represented here.
