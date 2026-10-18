---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed the unique u,v,w Fourier coordinates on sum-zero hyperplane and checked ||x||₄⁴=2[u⁴+v⁴+6w²(u²+v²)+2w⁴]. Convolution gives rotated/dilated B=[[a,c],[-c,a]] on (u,v), scalar b on w. The mixed term has coefficient 6b²r²; since L=||B||₄≥r, each nonnegative term is bounded by max(L,|b|)^4 times its input term, while w=0 and u=v=0 force equality, proving exact three-coordinate gluing. For (u,v)=(cos t,sin t), quotient r⁴(3+cos(4t−4θ))/(3+cos4t), whose discriminant yields the claimed radical. Independently checked algebraic equivalence to the prior ℓ₄² block expression. Finally ||K_H||₂=max(r,|b|), and k=(1/2,1/2,0,0) gives L⁴=1/2 and r²=1/2, attaining 2^{1/4}. Handles r=0, b=0 and arbitrary signed real kernels; finite checks not universal proof.

## originality

PASS

Independent statement-and-implication comparisons checked relevant original theorems rather than titles. The mirrored current record was excluded as an independent priority source. No inspected stronger theorem determines the entire audited final result; specific residual access/priority risks are retained.

## value

PASS

The mean-zero restriction of a Markov/circulant operator controls mixing beyond spectral ℓ₂ decay. Its exact ℓ₄ contraction for all real four-state kernels and a sharp non-Hilbert spectral gap are useful natural small-chain benchmarks; positive quartic gluing is a structural lemma, not merely resubstitution of prior 2×2 formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
