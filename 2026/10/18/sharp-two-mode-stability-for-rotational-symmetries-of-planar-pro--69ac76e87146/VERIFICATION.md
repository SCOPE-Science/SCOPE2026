---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Verified the exact spectrum, constants and endpoints in RESULT.md lines 26–65. On the reference equator, the j-th positive Fourier coefficient of Y_lm selects m=j, with amplitude √[(2l+1)(l−j)!/(4π(l+j)!)] P_l^j(0). Probability Haar orthogonality divides its square by 2l+1 and kills distinct-degree cross terms. Rodrigues' formula gives the stated equatorial double-factorial value when l−j is even and zero otherwise; factorial cancellation gives λ_lj=c_((l−j)/2)c_((l+j)/2)/(4π), c_k=4^(−k)binom(2k,k). This counts one positive Fourier order, not both signs. The pullback of area-null sets along rotated circles is null for Haar times circle measure, by rotational invariance; Cauchy–Schwarz gives bounded extension from polynomials on area-L² and the a.e.-orientation Fourier interpretation. Exactly one mode survives for each l≥2. In the ratios s_lj=(l+1/2)λ_lj the central-binomial recurrence gives the stated two-degree ratio: its denominator minus numerator is 4j²−1>0. Stirling gives the common limit 1/(2π²), and the initial ratios are 15/(64π) and 35/(128π), with the latter larger. Thus the lower constant is approached but not attained apart from the kernel; every nonkernel equality for the upper bound has degree 3 only, modulo degrees 0 and 1. Independently on a rotated equator write u₃=A cos(t−t₀) with A²=1−C², C uniform on [−1,1]. The degree-two and degree-three zonal test energies are then 45 E[A⁴]/(256π)=3/(32π) and 175 E[A⁶]/(1024π)=5/(64π), confirming the low-degree normalization. The support-function restriction to a plane gives its orthogonal projection; r+εY has positive spherical support Hessian for sufficiently small ε, so both sharpness sequences are admissible among smooth strictly convex bodies. The high-degree energy λ~const/l rules out every stronger H^(−s) norm with s<1/2 even on these perturbations. Inspected VERIFICATION.md and check_frame.py, without executing the supplied script. The spectral recurrence and Stirling are the infinite-degree proof, not the saved 2,006 finite checks. This gives no finite-plane or Hausdorff stability claim.

## originality

PASS

The qualitative kernel and tools for obtaining the exact equatorial amplitudes have prior coverage. The supported distinct content is the sharp two-sided comparison in the specified shifted Sobolev norm, including the exact upper extremal degree and geometric sharpness. This is a bounded comparison, not a determination of historical priority.

## value

PASS

The two modes are selected by an existing qualitative projection-rigidity problem, not arbitrary test frequencies. The result gives quantitative recovery in the natural shifted order −1/2 norm (l+1/2 is the square root of the l-th eigenvalue of −Δ+1/4), resolves both extremal regimes, and shows the same obstruction for actual smooth strictly convex bodies. The added sharp information is the degree-three energy maximum and exact high-degree loss, not a change of measure convention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
