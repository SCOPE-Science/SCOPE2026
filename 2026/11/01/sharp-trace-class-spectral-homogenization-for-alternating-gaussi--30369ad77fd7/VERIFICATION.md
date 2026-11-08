---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

In the analytic one-variable Bargmann–Fock space e_n=z^n/√n! diagonalizes the indicator of annuli 2j≤|z|²<2j+1, with λ_n=1/n!∫_0∞b(t)e^{-t}t^n dt. For |w|<1 the Laplace transform of the period-two square wave gives Σλ_n w^n=1/[(1-w)(1+exp(w−1))]. Integrating bounded Fejér sine approximants against each gamma density, then summing absolutely over odd harmonics, gives λ_n−1/2=(2/π)Σ_{k odd≥1}(1/k)Im(1−iπk)^{−n−1}. The k=1 term is (2/π)ρ^{n+1}sin((n+1)θ), ρ=(1+π²)^−1/2, θ=arctan π, while k≥3 is O(ρ_3^{n+1}) for ρ_3=(1+9π²)^−1/2<ρ; absolute geometric summability proves T−I/2 is trace class and σess(T)={1/2}. Abel limit from the generating function is Tr(T−I/2)=1/4. If θ/π rational, exp(2iθ) is algebraic so tan θ would be algebraic, contradicting transcendence of π; hence the normalized leading sine is dense through ±1 and the two sharp limsup/liminf are ±2/π, with infinitely many eigenvalues on either side. Independent high-precision mpmath annulus-gamma integrations and Fourier partial sums agreed to ~10^−10 at n=1 and ~10^−42 by n=12 (the n=0 Fourier cutoff retains a ~2.5×10^−4 tail, correctly not mistaken for a failed equality). All asymptotic claims follow from absolute harmonic bounds, not the finite check.

## originality

PASS

Best-of-knowledge originality judgment for the exact scoped final claim, after mathematical prior-work implication comparison. Standard radial Toeplitz gamma eigenvalue representation is credited; no inspected primary theorem establishes the precise infinite periodic mask trace and signed asymptotic.

## value

PASS

The natural infinite-area checkerboard radial mask oscillates forever at macroscopic phase-space scale, yet its analytic Gaussian Toeplitz localization differs from 1/2I by a trace-class operator with a nonzero exact total trace and sharp alternating spectral deviation. This is a concrete useful model for noncompact periodic localization and high-mode homogenization, not merely a fixed-index numerical calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
