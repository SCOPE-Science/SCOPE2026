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

An idempotent fixes its image U≤W and is uniquely specified by its complementary kernel. Complements are the graphs of the q^{r(k+m−r)} maps from a fixed complement to U, which gives equation (1) with the Gaussian coefficient. The finite-product factor is uniformly bounded between positive constants for fixed q, since Φ∞>0, and tends to Φ∞^−1 when r and k−r both diverge. Completing the square gives c=(2k+m)/4 and weights q^{−2(h−θ_k)^2}, up to that factor and the finite interval. The distances c and k−c diverge in the interior regime since m≥0 and m−2k→−∞. On bounded h-windows the product converges uniformly; both phases and tails are controlled by a common summable envelope. The normalizers of the moving Gaussian are bounded below by the h=0 term, so unnormalized ℓ¹ comparison gives the stated total-variation result without selecting a phase subsequence. With r=k−j and t=m−2k, division by q^{km} gives q^{−2j²−tj}Φ_k/(Φ_{k−j}Φ_j). For fixed integer t the summable bound with |t| in place of −t and pointwise convergence give the defect law; the j=0 and j=1 limiting weights show its full-image mass is strictly between zero and one. For t→+∞ the nonzero-defect mass relative to j=0 is bounded by Φ∞^−2 times q^{−t}/(1−q^{−t}). For m/k→α, the logarithmic weight per k² tends uniformly on the grid to x(2+α−2x); its uniquely maximizing position is min(1,(2+α)/4), the maximal value is as claimed, and the gap outside each neighborhood gives concentration. The free energy is C¹ and has the stated one-sided second derivatives. At k=0 only the zero map occurs; the formula also applies at m=0. Frozen verify.py tests literal matrix idempotence and rank in finite prime-field cases, product arithmetic for extension-field parameters, and the critical full-image mass numerically; it was inspected, not executed, and none of those cases proves the limits.

## originality

PASS

The finite projection count, including the exact full-image stratum, is classical or expressly prior and is not counted as new. The inspected comparisons do not cover the area of novelty: the joint fixed-field asymptotic laws for a single uniform restricted-range projection, particularly the m=2k+t transition profile with the Φ_j factor. The discrete-Laplace methods are standard; no novelty is attributed to those methods or to the macroscopic maximization in isolation.

## value

PASS

Ordinary image dimension is a natural statistic of a uniform idempotent in an established transformation semigroup. The interior lattice phases and the nondegenerate critical defect law quantify when a projection onto all of W is typical. The limiting fraction and free energy alone cannot resolve full-image probability at m/k=2 or the critical lattice shape; the explicit fixed-offset distribution adds information a researcher using that ensemble could need. The classical count and elementary maximization alone would not meet this value claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
