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

# Reproducibility and verification

Run `python3 verify.py` using Python 3.9 or newer. The script requires only standard-library modules and exits successfully with `VERIFY_OK` if its finite checks pass.

Checks actually made include: the exact \(m\)-fold multiplicity of ternary centered signs at diagonal level \(m\) through level 12; exact rational verification of the triple-angle extremum \(-9/16\) and the rational comparison \(256>243\); independent finite product grouping at resonances \(t_N=(\pi/2)3^{N+1}\) for five \(N\)-values; positivity of \(A,B\) and the strict inequality \(3A>1\) in their finite approximations; and nonvanishing on neighboring frequency samples.

The proof's infinite claims do not depend on numerical convergence. Strict \(3A>1\) follows analytically from \(A>(4/9)\). The \(L^2\) conclusion follows from a geometric-scale upper bound with exponent \(\kappa>1/2\). The non-BV conclusion follows from the exact geometric subsequence, the finite-measure Fourier bound for distributional derivatives, and the divergence of \((3A)^N\). The high-Sobolev exclusion uses uniform lower bounds on intervals around each resonant frequency, not isolated samples. Neither the uniqueness of historical priority nor an optimal Sobolev threshold is certified here.
