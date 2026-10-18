---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For each N≥2 and coprime a, the parity-adjusted chirp is N-periodic and has vanishing nonzero shift autocorrelations. Let d=∏p^floor(v/2), m=N/d, with d|m. Grouping correlations by j mod d proves ALL d-periodic phases remain exact CAZAC; for shifts divisible by m the modulation cancels. The first variation of each shifted autocorrelation is iγ_s(e^(−2πia s²/N)−1)√N \hat h(−as), so the energy quadratic term is 4N Σ_{s≠0}sin²(π a s²/N)|\hat h(−as)|² and the Hessian eigenvalues are 8Nsin²(πa^{-1}k²/N). Its null modes satisfy N|s², i.e. m|s and frequency k multiple m, exactly the d-dimensional periodic phase subspace. The transverse Hessian has gap 8Nσ; continuity and line integration give E≥2Nσ dist(θ,T_d)² locally, eliminating all other nearby CAZAC branches. Independently computed correlations and FFT Hessian quadratic form for every coprime a at N=2,4,8,9,12,16,18,25; finite checks confirm coefficients only, not infinite quantifiers.

## originality

PASS

Best-of-knowledge comparison of exact statements, aliases and mathematical implications in primary sources; original general methods and previously known components are explicitly acknowledged. There is no decisive prior theorem covering the full surviving claim in the material actually read. Inaccessible priority sources and failed Resultary check remain material residual risks and are not evidence of novelty.

## value

PASS

The local moduli and rigidity of Zadoff–Chu/Gaussian CAZAC solutions are natural signal-analysis and Fourier geometry questions. The exact number-theoretic dimension d−1, the full Hessian multiplier spectrum and coercive normal energy bound can be reused to distinguish truly local continuous families from isolated squarefree chirps, not just to recompute a known finite CAZAC table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
