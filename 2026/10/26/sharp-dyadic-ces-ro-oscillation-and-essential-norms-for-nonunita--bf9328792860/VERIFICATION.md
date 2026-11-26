---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For p_n(z)=-(1-z^n)^2/[2n(1-z)], von Neumann's inequality gives the contraction upper bound and multiplication by a maximizing scalar gives equality. A unit vector in ker(V*) produces an orthonormal orbit; normalized phase-modulated blocks on indices L through 2L-1 are weakly null and have (V-zI) residual sqrt(2/L) for |z|=1. Compact operators annihilate these vectors in norm in the limit, giving the full circle-supremum lower bound for distance to compacts and hence for all finite-rank distances (including k=1). On [pi/n,pi] the numerator of the modulus is at most 1 and the denominator is nondecreasing; a negative derivative at pi/n puts the maximum strictly in the first lobe for n>=2. There the logarithmic derivative is strictly decreasing from +infinity to a negative value, by sin(nu)<=n sin(u). This verifies the root equation and uniqueness on the stated interval (the two opposite phases are equivalent on the full circle). Uniform convergence after rescaling and a simple limiting root give x_n-x_*=O(n^-2); stationarity removes its first-order effect on the value. The expansion of x/(2n sin(x/(2n))) gives the displayed positive n^-2 coefficient with O(n^-4) remainder. Strong convergence follows by the mean ergodic theorem, or telescoping on ran(I-V) and density on the orthogonal complement of Fix(V).

## originality

PASS

Best available evidence supports the explicit finite dyadic norm, first-lobe optimizer and correction as the distinct content, not the standard shift/Toeplitz norm reduction, general ergodic convergence or polynomial contraction inequality. No equivalent statement or dominating exact result was found in the bounded comparisons.

## value

PASS

This canonical difference of consecutive dyadic Cesàro scales tends strongly to zero while retaining a nonzero sharp universal norm. Evaluating that norm, its finite-scale correction and the same obstruction after arbitrary compact perturbations gives a quantitative answer beyond standard qualitative mean ergodicity. The exact scalar reduction is standard, but the evaluated invariant is useful as a sharp bound and benchmark for comparisons of averaging schemes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
