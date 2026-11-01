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

The proof derives each matrix entry from the normalized Bergman monomial basis and the generating series for the differential Hilbert kernel. Positivity permits Tonelli's theorem in the reduction to a single Euler-type integral. The log/Beta sandwich is valid for every degree at least one and fixed \(-1<\alpha<0\); the finite degree-zero row is absorbed into the uniform error constant.

Uniform gamma-ratio bounds on the compact parameter interval \(0\le\delta\le1/2\) imply the row expansion with a uniformly summable \(O((n+1)^{-2-\delta})\) remainder. Elementary integral tests give both the critical harmonic sum and the \(1/\delta\) mass singularity. A separate uniform floor estimate yields the Kolmogorov bound for *every* \(s\ge0\), including \(s=0\) and arbitrarily large \(s\).

Run `python verify.py` using Python's standard library to reproduce finite row-integral checks. The checker establishes no new infinite-dimensional claim: analytic steps in RESULT.md provide the proof. The conclusions concern output-monomial Hilbert--Schmidt row energies, not singular values or global parameter uniformity. Independent validation remains not performed.
