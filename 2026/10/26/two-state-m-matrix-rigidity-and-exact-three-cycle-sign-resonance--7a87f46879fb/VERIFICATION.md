---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For Q=[[-a,a],[b,-b]], a,b>=0, Q²=-(a+b)Q, and phi1(tQ)^-1=I-γQ, γ=(tr/(1-exp(-tr))-1)/r>0 for r>0 (Q=0 separately); Z-matrix with nonnegative inverse F_t follows. For C3, the integral of a stochastic semigroup is invertible since nonzero eigenvalues z=-3t/2±i sqrt3 t/2 have Re<0 and phi1(z)≠0. Its circulant coefficients a0>a1>a2>0 follow the equation tFQ=e^{tQ}-I and strict positive Poisson coefficients; Fourier inversion gives exact b2 formula. Expansion cosh(sqrt3 h)-cos h-2h sin h=Σ_{k>=2}[3^k+(-1)^k(4k-1)]h^(2k)/(2k)! has strictly positive coefficients (for odd k>=3, 3^k>4k-1). Adjugate gives b0>0, b1<0. Resonance zeroes exactly sin h=0 with positive denominator; decay from hyperbolic asymptotics. Nine direct independent matrix exponential/inversion checks tested signs and formula; all-t property is analytic.

## originality

PASS

Inverse phi1 matrix functions, reciprocal Bernoulli expansions, and rational numerical approximations are prior (Gemignani 2023, Boito–Eidelman–Gemignani 2018). The accessible primary full paper of Gemignani discusses efficient inversion, not an all-t Markov-generator Z-matrix criterion or an explicit global 3-cycle sign/resonance classification. The first nonzero positive two-jump coefficient is an elementary Bernoulli consequence and is not claimed new. The combination of minimal dimension and infinite exact sign resonances is the evaluated contribution.

## value

PASS

Sharp structural warning: a strictly positive time-averaged Markov transition matrix can have inverse with positive off-diagonal entry already in minimal dimension three, with exact all-time sign and infinitely many damped crossings around its limit. Useful for positivity of inverse semigroup averages and matrix-function algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
