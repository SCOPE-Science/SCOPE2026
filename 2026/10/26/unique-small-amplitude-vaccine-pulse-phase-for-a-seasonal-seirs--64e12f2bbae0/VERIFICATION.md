---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For the stated homogeneous SEIRS system with one annual instantaneous susceptible-only pulse of fraction eta, no baseline vaccination and sinusoidal beta(1+epsilon*cos(omega*t)), the disease-free susceptibility return map is a contraction of slope (1-eta)e^{-kT}, with exact periodic orbit s_eta(z)=s0[1-eta*e^{-kz}/(1-(1-eta)e^{-kT})]. Its first eta derivative has Fourier coefficient -s0/[T(k+i omega)]. The infected E,I linear system reduces by elimination to u=[(alpha-gamma)^2/4+alpha beta(1+epsilon cos(omega(z+tau)))s_eta(z)]u. The periodic principal Riccati logarithmic derivative R has analytic branch at R0=g/2 because D+g is invertible on periodic functions; the mixed epsilon eta equation gives <R_epsilon_eta>=(alpha beta/g)(1-2B/(g²+omega²))<q cos> = -K cos(omega tau+atan(omega/k)). The coefficient K>0 since g²+omega²-2B=(alpha-gamma)²+2B+omega²>0. Phase-dependent terms vanish if either amplitude is zero, so analyticity yields a uniform C² remainder divisible by epsilon eta. Dividing by the nonzero mixed coefficient, the phase derivatives converge to those of a cosine, proving exactly two critical points and one strict global minimizer/mod-T at -atan(omega/k)/omega+O(epsilon+eta). Independent direct 2x2 fundamental-matrix ODE integration and mixed finite differences at four phases in three parameter sets corroborated the coefficient and predicted phase with finite-amplitude mixed difference errors <=0.00560, including an extreme fast-stage regime. Finite checks do not establish analytic uniqueness by themselves.

## originality

PASS

Best-of-knowledge PASS: full-text 2024 seasonal SEIRS study compares discrete phases for finite pulses and nonlinear case counts, and full-text earlier SEIRS/SIR vaccination literature analyzes different thresholds/controls; the claimed universal weak two-amplitude principal Floquet phase, strict uniqueness and stage-independent leading angle were not demonstrated to be consequences of those results. Prior scalar SIR timing and orbital-Floquet analysis is credited, not treated as new in itself. Highly relevant 2014 and 2019 full papers were unavailable, retained as genuine residual risks.

## value

PASS

An explicit, unique optimal annual phase was motivated by earlier simulations suggesting that vaccination timing relative to sinusoidal transmission matters. The quantified weak-amplitude SEIRS result identifies the universal demographic replenishment lag arctan(omega/(b+delta))/omega while correctly isolating latency/recovery as effects on magnitude, not phase. That is a structural distinction between local invasion and cumulative cases, useful for analytic model sensitivity and phase design; it is not a claim of clinical optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
