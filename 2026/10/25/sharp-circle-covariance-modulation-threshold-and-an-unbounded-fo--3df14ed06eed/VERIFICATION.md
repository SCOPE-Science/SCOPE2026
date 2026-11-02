---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The exact Fourier transform c_n=a(1-(-1)^n exp(-pi a))/(pi(a^2+n^2)) is positive; the cosine factor shifts by one index, so Herglotz positivity reduces exactly to b>=-min_n 2c_n/(c_{n-1}+c_{n+1}). Algebra yields R_n=h^(+/-1)F_A(n) and excludes n=0. Differentiating F_A(sqrt y) gives one positive critical y=s_A^2 and strict unimodality, proving the <=4 parity candidates. At b=-B only finitely many modes vanish; all sufficiently large consecutive modes are strictly positive, and a Vandermonde argument makes every distinct-point Gram matrix positive definite. Taylor/scale estimates justify both asymptotics and the n-asymptotic; taking s_A=n yields a polynomially separated unique minimum dominating exponentially small parity splitting. Independent Sympy identities and 11-parameter/40-index checks support, not prove, the universal claims.

## originality

PASS

Qualified original signed cosine-modulation cutoff and active-frequency staircase. Gneiting establishes sphere/circle Fourier criteria and unmodulated exponential classes; Feragen establishes geodesic Laplacian positivity, Porcu et al. covariance baselines. These general premises do not deliver this negative-b modulation boundary, finite candidate rule, boundary strict PD and unbounded active-mode succession. Gneiting 1998 simple-circle-tests complete text unavailable remains potential equivalent inequality risk.

## value

PASS

Exact permissible negative first-harmonic modulation is a natural covariance-model admissibility boundary; four-candidate evaluation replaces infinitely many spectral inequalities, identifies strict positive-definiteness on the boundary and a nontrivial unbounded critical-mode staircase. These are reusable spectral and statistical design facts, not textbook positivity of the exponential baseline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
