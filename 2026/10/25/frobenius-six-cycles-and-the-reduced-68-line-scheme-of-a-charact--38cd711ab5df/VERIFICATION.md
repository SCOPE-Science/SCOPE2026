---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For exact F=x0*x1^2*x2+x1^4+x1*x2^3+x0^3*x3+x0*x2*x3^2 over F2, the 68-line GF64 certificate was read and independently verified using GF(2)[z]/(z^6+z+1). The 68 RREF matrices are distinct, vanish on the quartic at five distinct affine parameters (enough for degree<=4), and every chart Jacobian has full rank: dimension/rank pairs 4/4 on 48,3/3 on 16,1/1 on 3,0/0 on 1. Frobenius squaring yields 4 fixed, 2 two-cycles, 2 three-cycles, 9 six-cycles; cusp plane has two fixed lines and one two-cycle. Independent partial derivatives localize surface singular support at [0:0:0:1]. With the cited published K3-quartic 68-line upper bound and the A3 singularity (published model classification), these 68 are all geometric lines and all local tangent spaces vanish; hence finite étale of degree 68. Orbit counting gives #=4+4*1(2|n)+6*1(3|n)+54*1(6|n) and the asserted zeta product. The GF64 list alone would not prove algebraic-closure completeness without Veniani.

## originality

PASS

The 68 geometric lines and family are classical Rams–Schütt/Veniani results. The evaluated Frobenius splitting of the exact prime-field model, full Jacobian reducedness and zeta function of its finite line scheme are the surviving specific arithmetic claims. Their novelty is qualified because Veniani’s full Section 6 could not be obtained and might tabulate the same arithmetic.

## value

PASS

The line-scheme Galois action and exact splitting field of a natural extremal characteristic-two K3 quartic provide a reproducible arithmetic invariant not determined by the geometric maximum alone. The zeta function and reducedness distinguish this finite étale model from purely geometric line counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
