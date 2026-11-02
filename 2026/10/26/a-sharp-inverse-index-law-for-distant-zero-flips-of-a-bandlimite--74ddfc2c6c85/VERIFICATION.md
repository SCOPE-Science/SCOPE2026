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

For fixed B,y>0, f_{B,y}(z)=sin(pi B(z-iy))/(pi(z-iy)) has Fourier transform e^(2 pi y xi) on [-B/2,B/2], is in PW_{B/2}, and has genuine zeros a_n=n/B+iy. Set x=n/B. The unit-modulus multiplier splits as R_x(t)exp(2iyt/(x²+y²)) with R_x(t)-1=-2iyt/[conj(a)(a-t)]. For the t=x+s layer, x²|f(x+s)|² tends [sin²(pi Bs)+sinh²(pi By)]/pi² and m tends (s+iy)/(s-iy); integrating yields 2y/pi[cosh(2pi By)-exp(-2pi By)]. On the t=x²u scale away from zero, the oscillatory numerator averages to cosh(2pi By)/2 and the exponential contributes 2y/pi cosh(2pi By). Cutoff bounds rule out other order-x^-2 scales. Since Im⟨m f,f⟩=O(log x/x²), optimized phase changes squared distance only o(x^-2). Thus n² coefficient = B² times sum of two terms. Independently numerically evaluated both limiting integrals for three distinct (B,y), with finite truncation tolerances; these checks do not prove the two-scale convergence.

## originality

PASS

Qualified originality concerns the exact leading order and positive constant for a canonical genuine-zero flip moving to infinity, including a nontrivial far-field exponential contribution, not the zero-flip operation or generic phase retrieval bounds.

## value

PASS

The profile gives a concrete sharp high-index instability/stability rate in an infinite-dimensional phase retrieval problem. Both boundary-layer and long-range phase terms contribute at leading order, and the exact nonzero coefficient supplies a useful sharp benchmark against general modulus-of-continuity bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
