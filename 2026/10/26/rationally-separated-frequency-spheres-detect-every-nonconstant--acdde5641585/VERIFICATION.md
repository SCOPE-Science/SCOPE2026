---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For spherical Bessel j_l(x), l≥1, its finite reverse-Bessel-polynomial representation gives at each positive zero x an exact phase e^{2ix}=R_l(x), with R_l a rational function over Q(i), analytic, equal to 1 at zero, nonconstant. Suppose positive zeros x/y=p/q rational with p,q distinct positive coprime integers, so x=pz and y=qz. Then R_l(pz)^q=R_l(qz)^p; the rational difference is not identically zero because a nonconstant rational function with R(0)=1 cannot have log R(z) purely linear, and the first nonlinear Taylor term produces different p/q powers. Thus z is algebraic, contradicting Hermite–Lindemann: e^{2ipz} is transcendental but equal to the algebraic R_l(pz). Therefore each l≥1 has no rationally commensurate distinct positive zero pair. The Funk–Hecke spherical harmonic decomposition implies a finite complex measure on S² annihilated by Fourier observations at radii r and (p/q)r has zero harmonics of degree l≥1, so is constant surface measure; its l=0 mode vanishes too unless the two radii are both nπ, which requires 2r∈q N_+ for coprime p,q. Hence injectivity on zero-total-mass measures and exact 1D kernel exception for general measures. Independently checked exact rational phase identities and polynomial nonidentity for l=1..5 and several integer ratios plus phase at positive zeros. These finite checks do not establish the all-order transcendence argument.

## originality

PASS

Qualified PASS primarily for the new arithmetic theorem on rational ratios of zeros of each half-integer spherical Bessel order. The complete 2020 Chattopadhyay–Ghosh–Giri–Srivastava Theorem 13 already gives an if-and-only-if nonuniqueness criterion for two concentric Fourier spheres in terms of common zeros of the same Bessel function. The 2012 González Vieli paper already gives the single-sphere Bessel-root criterion. Those theorems become the proposed rational-sphere dichotomy if the new rational zero-ratio fact is supplied; the Fourier observation part is therefore a corollary of published general criteria and should not be advertised as wholly independent. No inspected primary source asserted irrationality of all distinct spherical-Bessel zero ratios, but older special-function arithmetic results may be unindexed.

## value

PASS

The arithmetic assertion answers a natural exact question about locations of all spherical Bessel nodes, not an arbitrary finite selection. The combination with previously known Fourier criteria yields a clean unconditional two-frequency uniqueness design for every rational separation, with an exact and unavoidable degree-zero exception. The proof uses a nontrivial phase rationality/transcendence argument; this is mathematically more than a table or elementary rescaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
