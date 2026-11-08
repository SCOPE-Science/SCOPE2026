---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For invertible Euclidean-monotone M, L=||M||2 and gamma>=2, the exact recurrence has C=gamma L M^-1 b, D=-gamma(gamma-1/2)L^2 M^-2 b and E=gamma(gamma-1/2)(gamma-1)L^3 M^-3 b. The three identities MC/L=gamma b, MD/L=-(gamma-1/2)C, ME/L=(1-gamma)D cancel the s^-1, s^-3/2 and s^-2 coefficients of a formal C s^-1/2 +D s^-1 +E s^-3/2 approximation. Residual defect O(s^-5/2). Monotonicity gives ||B_s||<=sqrt((1-gamma/s)^2+1/s)=1-(gamma-1/2)/s+O(s^-2). Discrete convolution yields O(s^-3/2 log s) when gamma=2 and O(s^-3/2) for gamma>2; this is o(s^-1). Neumann expansion of (M+gamma L s^-1/2 I)^-1 then gives universal nonzero lag s(u_k-v_k)->gamma L^2 M^-2 b/2. Independent exact coefficient checks and finite-step simulations on SPD, skew and nonnormal accretive 2x2 matrices corroborated signed coefficients; asymptotics rest on contraction proof, not sampled sequences.

## originality

PASS

Cai and Zheng (2026) give the anchored schedule and O(k^-1/2) tangent-residual upper bound; Surina et al. give analogous squared-gradient upper rate; Chen (2026) explains operator-side Tikhonov regularization and an upper rate at gamma=4. Exact two-term vector coefficients and nonzero discrete tracking lag for every invertible monotone M are not given by these upper bounds: an upper rate permits zero leading constant. Best-of-knowledge, with risk from general asymptotic expansions for vanishing regularization.

## value

PASS

The theorem gives sharp unavoidable residual bias and the sign/magnitude of the first discrete tracking error for a standard anchored algorithm, including strongly convex quadratics and bilinear skew saddle problems. It distinguishes discretization lag from the target regularization bias, an independently useful quantitative limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
