---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For fixed complex dimension d>=2, recalculated radial monomial moments with weight (1-|z|)^t and unnormalized Euclidean volume. The coefficient of s^m is Gamma(m+d)Gamma(t+2m+2d+1)/(2 pi^d m!Gamma(2m+2d)Gamma(t+1)), valid for all real t>0. Substituting s=u/t^2 and h=1/t gives the finite product prod_{j=1}^{2m+2d}(1+jh). The ratio test yields normal convergence uniformly on compact polydisks |u|<=R, |h|<=h0 with R*h0^2<1, justifying a genuine O_R(h^2) expansion, not a formal termwise expansion. At h=0, duplication gives the 0F1( ;d+1/2;u/4) limit with constant sqrt(pi)/(2^{2d}pi^d Gamma(d+1/2)). Differentiating the finite product gives the correction (D+d)(2D+2d+1). The ODE uFdoubleprime+(d+1/2)Fprime−F/4=0 reduces this correction at each simple zero u_k=−j_{d−1/2,k}^2 to 2(d+1)u_k Fprime(u_k). Implicit function/Rouché gives a single simple near-root u_{k,t}=u_k(1−2(d+1)/t)+O(t^{-2}), real and negative by conjugation and uniqueness, and the local zero count on bounded zero-avoiding domains. Physical s=u/t^2 lies in (−1,0) for fixed k at large real t. Independently computed high-precision roots for d=2,3, k=1, t=150,300,600, with numerical relative t-drift converging toward 6 and 8. Such finite checks corroborate, but normal convergence and complex perturbation prove the all-real asymptotic.

## originality

PASS

Directly inspected the earlier published Resultary RESULT.md on the identical Euclidean-distance ball kernel: it gives an exact Jacobi-polynomial numerator and negative-real scalar zeros for integer exponents t>=0. That result substantially covers the integer geometry and, with classical Mehler–Heine asymptotics, likely the leading integer-subsequence Bessel pattern. It does not state a locally uniform expansion for arbitrary large noninteger real t nor the exact common first-order drift −2(d+1)/t. Marinescu–Xing study regularity in real parameters for finite weights, not the high-t ball microzero law. A separate disk d=1 result is outside d>=2. Therefore the assessed new claim is the all-real two-term microscopic asymptotic and first-order drift, NOT the known integer zero count. A published higher-order Jacobi or kernel asymptotic may still imply the first drift; explicitly retained as risk.

## value

PASS

The exact Euclidean boundary-distance weight differs from classical (1-|z|^2)^t and genuinely creates kernel zeros. The universal high-power Bessel scaling identifies the microscopic location of actual scalar zeros in each fixed higher-dimensional ball; the first-order drift makes the leading universal convergence quantitatively useful and extends beyond integer Jacobi polynomials. This is a natural deformation/spectral-zero invariant, with explicit noninteger weighting relevance; no claim of all-root census at finite exponent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
