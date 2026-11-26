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

Under the stated normalization, row 1 stays iff its independent |N(0,1)| exceeds all n-1 copies of W=||(Y_1,Y_2)||_p/sqrt(2); ties have probability zero. Gaussian polar integration gives survival at sqrt(u) equal to the angular average of exp(-u h_p), where h_p=(|cos|^p+|sin|^p)^(-2/p). For p<2 its four diagonal minima have value lambda and curvature 2lambda(2-p); for p>2 the four axis minima have value 1 and quadratic coefficient 1, including p=infinity. Laplace's method gives the stated C_p in survival asymptotic C_p u^(-1/2) exp(-lambda u); the Euclidean survival is exactly e^(-u). With b=(log n-0.5 log log n+log(C_p sqrt(lambda)))/lambda and v=lambda(u-b), the centered survival times n tends to e^(-v), and the chi-square density contributes gamma(1/(2lambda)) e^(-b/2)/(lambda sqrt(2 pi b)). For u≥b/2 and v≤0, the survival times n is bounded below by a constant times e^(-v); below b/2 monotonicity gives a superpolynomially small contribution. For v≥0 the rescaled density has an integrable exponential bound. This establishes the exact prefactors, including pi^(1/4)/2 above two. Rotation yields the exact p=1 identity; centering the Euclidean integral at log n gives 1/sqrt(2n log n). In the critical window the derivative of log h_p at two is H(cos² theta)/2 uniformly, and bounded second derivatives yield a uniform O(1/(log n)^2) error, including at the axes. Thus at u=log n+v the survival times n tends to M(beta)e^(-v). The uniform bound |h_p-1|=O(1/log n) supplies the same integrable tail bounds and the limiting integral equals 1/sqrt(2M(beta)) with normalization sqrt(n log n). Entropy is positive almost everywhere, so M is strictly decreasing, with M(0)=1. The extra nP_n divergence follows in all stated fixed cases p>1. This is solely a first-column result; no quadrature is needed for its asymptotic proof.

## originality

PASS

Pass is for the general coordinate-norm first-pivot comparison and especially the explicit varying-exponent crossover. The p=1 and p=2 GUE endpoints are published. The fixed-p off-diagonal Gaussian norm tail asymptotics are also already covered by a more general fixed-p Gaussian result, even though the pivot transfer constants are not stated there. The fixed-p law is a close application of those tails and a separate scalar-versus-maximum transfer, not a new Gaussian tail theorem. In the inspected sources the near-two triangular array and its entropy profile are not covered.

## value

PASS

The fixed-coordinate comparison norm changes the probability of no row swap even for the same random matrix ensemble. The transition from four minimizing directions to a continuum leads to different logarithmic powers, and the explicit entropy average resolves the crossover where neither fixed-p approximation is uniform. This explains endpoint sensitivity without extrapolating to later pivots or numerical stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
