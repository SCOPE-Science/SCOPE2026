---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For every m>=3 and spoke length t>=1/2, the anchored wheel metric gives exactly the 2m signed spoke and 2m signed unit rim inequalities. At t<=1/sqrt(2), covariance t^2 I meets spoke constraints and has rim variance 2t^2<=1. For larger t, the unique monotone cyclic inverse parameter q in (0,1) gives A=alpha I+beta L, positive alpha,beta, alpha t^2+beta=1, and exact covariance diagonal t^2 and adjacent-difference variance 1. Summing weighted inequalities for an arbitrary centered or translated competing ellipsoid yields tr(AS)+c^T Ac<=m; determinant AM–GM establishes the claimed ellipsoid as the unique unrestricted volume maximizer. Cyclic Fourier determinant gives the exact volume. Strict concavity of log det in beta and the cycle spectral first/second moments give F(tau-)=-2m and F(tau+)=-10m; first derivatives agree. The root equation yields the fixed-t large-m volume rate. Independently recomputed cyclic eigenvalue sums, feasibility, contacts and normalization for m=3,4,7,13 and t=0.5,1/sqrt(2),0.8,1.1,3 without using supplied verifier. Numerical spectra supplement analytic proof; m=3 cycle neighbor convention was included.

## originality

PASS

Best-of-knowledge PASS for the entire one-parameter spoke-weight transition and curvature jump; explicit prior unweighted wheel enclosing-ellipsoid result at t=1 is acknowledged as covered.

## value

PASS

The largest-volume inscribed ellipsoid is a canonical normed-space invariant of a natural weighted family of metric graph Lipschitz balls. The theorem resolves all spoke lengths, identifies a universal contact-orbit transition, a genuine non-C2 volume response with exact jump -8m, and an all-dimensional limiting rate. A single unweighted solution neither supplies nor trivializes this parameter-dependent geometric phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
