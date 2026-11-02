---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For centrally symmetric convex K, the exact chord formula w*t-area_loss = 2 int_0^t (h-z_s) ds uses short-chord level sets. At theta=lambda*t^3, the upper support graph rescales to f_lambda(u)=u^4/4+lambda*u and its minimum is -3|lambda|^(4/3)/4. Equal-height endpoints spaced by r give the unique cubic midpoint m^3+(r^2/4)m+lambda=0. Uniform strict-convex localization supports integration of the rescaled support deficit and produces the F integral. The implicit-derivative positivity proves strict monotonicity; expansion of the cubic solution gives -7/480, and axial slicing F(0)=1/160. Independently implemented actual two-dimensional overlap quadrature with all thin endpoint intervals separated agreed with F at lambda=0,0.2,1 as t decreased, and checked F(1)=0.236019362175881.

## originality

PASS

Best-of-knowledge comparison of actual final mathematical implications with primary sources and relevant published semantic records. Relevant predecessor results were credited; no inspected full-theorem statement covers the final claim, with explicit residual priority risks.

## value

PASS

The quartic norm ball is a canonical convex body with zero curvature at coordinate supports. The cubic-angle scaling and explicit monotone fifth-order profile quantify a singular transition that fixed nonzero-curvature t^3 overlap formulas fail to describe uniformly; the exact coefficient is a meaningful covariogram boundary-layer invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
