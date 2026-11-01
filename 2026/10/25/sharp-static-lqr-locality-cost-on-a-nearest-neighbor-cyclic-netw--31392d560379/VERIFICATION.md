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

For A=I/2, B=I and SPD Q=9I/4+S+Sᵀ, the scalar DARE gives p(q)=[q−3/4+sqrt((q+1/4)(q+9/4))]/2 and gain k=p/[2(1+p)]. Riccati completion of squares for every stable even noncirculant F yields stationary excess 1/(2N)tr((F−K)ᵀ(I+P)(F−K)Sigma_F), at least ||F−K||_F²/(2N). The optimum Frobenius radial-band approximation is matrix entry truncation, not requiring circulant competitors. Nearest outer Laurent branch point z=-2 produces coefficients (-1)^(j-1) sqrt(3)/(2sqrt(pi)) 2^-j j^-3/2 and exact squared-tail asymptotic E_r~r^-3 4^-r/(2pi). A uniformly stable symmetric radius-r Fourier truncation gives an O(E_r) upper bound. Therefore Δ_r=Theta(r^-3 4^-r), with r fixed before N→infinity, and log-log radius inversion. Independent matrix Riccati, stationary Lyapunov performance-difference checks for r=1..3 at N=36 and FFT tail ratios at j=5..20 agreed. The optimal *leading constant* is not asserted.

## originality

PASS

Prior spatially distributed LQR work establishes gain decay and sufficient near-optimal truncation, not the sharp matching lower bound against every possibly noncirculant radius-r static controller with cubic polynomial tail for this exact cyclic Q. The Fourier symbol is a classical technique. Older spatially invariant Riccati analysis could contain an equivalent calculation, so priority is qualified.

## value

PASS

A natural networked static-controller locality constraint has a provably unavoidable cost, quantified against all noncirculant static gains, matching a constructive truncation. The exact exponential base and cubic correction sharpen qualitative upper-only exponential decay and determine a precise second-order logarithmic communication-radius requirement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
