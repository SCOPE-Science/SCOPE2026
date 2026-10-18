---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For a bounded T fixing a hyperplane with S=I-T rank one, S²=lambda S and ||S||>=1. If lambda<=1/5, the polynomial expression for T^4 and norm reverse triangle contradict ||T||<=1+r²/10^6. Otherwise P=I-S/lambda is a projection. The bounded-power Cesaro mean B_m=beta I+(1-beta)P with m=ceil(200/r) yields |beta|<r/19 and ||B_m||<1+r/2000, forcing ||P||<1+r<=c, contradicting the seed lower bound. For an l_infinity sum of finite seeds, choose a maximal coordinate of a nonzero kernel vector x, a norming functional on that coordinate, and the isometric graph embedding U with U(x_i)=x; the compressed map pi_i R U fixes a hyperplane and annihilates x_i. Indeed this compressed map is itself a hyperplane projection, yielding the stronger direct estimate ||R||>=min_i c_i and independently checking the weaker displayed uniform epsilon bound. Kobos 2015 Cor 1.2 proves alpha_j=(8(j+3)^5)^(-30(j+3)^2) for explicit E4 and E5, and Epperlein 2025 Thm 1.2 certifies c3>=1.01. The dimensions n>=6 split as 3a+4b, while n3,4,5 are seeded. Inspected exact-rational checker and independently verified the underlying algebra and parameter comparisons; no claim that the prior computer-assisted seed certificate was independently reproduced.

## originality

PASS

The 2015 Kobos corollary provides an effective lower bound that depends and decays on dimension n; 2025 Epperlein provides explicit n=3 seed only. Kobos Oct-2026 establishes uniform positive qualitative existence but the publicly accessible statement gives no explicit absolute rational value. Constructing explicit models for all n by finite l_infinity sums and deriving a numerical absolute floor is a distinct effective assertion, subject to a substantial source-comparison risk because the complete 2026 paper could not be read. The compression/graph argument is elementary once found, but no inspected previous source states the current all-dimensional rational bound.

## value

PASS

Effective dimension-free projection separation addresses a motivated quantitative strengthening of a known uniform existence theorem in finite-dimensional Banach geometry. Its explicit rational constant is small and nonoptimal, but the universal, constructive numerical certificate and explicit fixed-hyperplane transfer settle a real effective version rather than selecting arbitrary slices. The much sharper direct projection-compression observation does not invalidate the stated weaker theorem, and is documented as a value/optimality limitation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
