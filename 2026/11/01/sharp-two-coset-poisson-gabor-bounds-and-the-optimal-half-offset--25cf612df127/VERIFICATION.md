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

The exact proof is in RESULT.md, Steps 1–6; no separate external certification has been undertaken. The derivation combines unitary Zak diagonalization, the Fourier transform of a Poisson/Cauchy-profile kernel, a nonnegative rational derivative in \(\cos(2\pi x)\), and two scalar one-variable optimizations. A direct standard-library program, `verify_bounds.py`, compares finite spatial Zak sums with the closed expression and tests the reported sharp extremal values at sample \(w,\delta\). The finite test is not offered as proof for uncountable parameter sets.

The program can be replayed with `python3 verify_bounds.py` after extracting the embedded files. Its tests are expected to report `checks passed` on success. The analytical scope is limited to two distinct frequency cosets of integer translations; no claim of an independent audit or computational proof of global uniqueness is made.
