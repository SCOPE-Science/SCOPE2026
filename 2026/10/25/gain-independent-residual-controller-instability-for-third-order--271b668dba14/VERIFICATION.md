---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The endpoint data yield h(u_hat′−λu_hat)=−u_n z^4 v(v−1)(vz+v−2)/6. For Re z<0, writing B=−vz and A=2−v gives 0<Re(B/(A+B))<1; differentiation under the strictly positive integral yields 4<ν_p<5 for every finite p. At z=−1+i√w, exact R polynomial arithmetic gives |R|²−1=[w(w−3)^2−32]/36; the unique w>3 root lies between 53/10 and 11/2. Exact μ=Re(zR′/R)=(w−1)^2(w−2)/12 > 5+339/4000. The determinant of the 2×2 feedback Jacobian equals 1+(βκ′(1)/4)(μ−ν_p)>1 for every positive gain and limiter slope; continuity gives a nonempty open boundary arc. Independent sympy rational arithmetic checked the root enclosure, μ lower bound and polynomial identities. Representative script tests at p=1,2,4 are corroboration only.

## originality

PASS

Best-of-knowledge, after comparing the actual theorem and its implications to retrieved Resultary records and the named published primary material. The original paper supplies the premises R and the Jacobian family but not the quantitative μ>5>ν_p proof; the latter establishes strictly stronger simultaneous gain/norm nonstabilizability under exact stated assumptions. Residual priority/access risks are explicitly retained.

## value

PASS

The cited I-controller instability plots alone permit trying other positive controller gains or norms. An exact common obstruction independent of all finite Lp choices and operating-point positive limiter slopes gives a usable sharp design-exclusion region within a motivated RK control model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
