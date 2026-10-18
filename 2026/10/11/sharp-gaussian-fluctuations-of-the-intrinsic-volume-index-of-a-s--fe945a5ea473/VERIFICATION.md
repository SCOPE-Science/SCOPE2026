---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Gaussian projection KKT reduces face index to N_m(S), with H_m(S)=G0+S. At t solving m E(Z-t)_+=t, normal-tail expansion gives t^2~2 log m, lambda=m Phi_bar(t)~t^2 and lambda-2 log m=o(t). Rare-event Lyapunov for X=(N_m(t)-lambda)/t and Y=H_m(t)-t gives covariance [[1,1],[1,2]]; the root perturbation t^2(S-t)=Y-G0+o_P(1) and monotone local-count bound yield (J_m-lambda)/t=>X-Y+G0, variance 2. The checked actual McCoy–Tropp Thms 4.5 and 4.8 supply Var<=2delta and scaled exponential moments; they upgrade mean/variance convergence by uniform integrability. Independent 120 Gaussian KKT/sorted face-count checks pass but do not prove asymptotics. This claim correctly concerns conic rather than Euclidean simplex intrinsic volumes.

## originality

PASS

Full relevant Kabluchko–Seidel article gives exact finite-dimensional intrinsic volumes of this cone family, and a published same-cone Resultary paper already proves J_m/(2 log m)->1 and EJ_m~2 log m; those facts are NOT novel. Goldstein–Nourdin–Peccati general CLT uses actual (unknown here) mean and variance. The explicit normal fluctuation scale and the sharp variance 4 log m, including asymptotic saturation, are additional and not implied by concentration, exact finite tabulation, or generic standardized CLT without evaluation. An unnoticed extraction of identical limits from old explicit formulas remains possible.

## value

PASS

The cone is a canonical simplex vertex tangent cone in high-dimensional conic integral geometry. The explicit second-order Gaussian law and limiting sharpness of the universal variance inequality supply new structural information beyond the already-known leading mean; mathematically motivated phase-transition width, not a generic rephrasing or isolated finite calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
