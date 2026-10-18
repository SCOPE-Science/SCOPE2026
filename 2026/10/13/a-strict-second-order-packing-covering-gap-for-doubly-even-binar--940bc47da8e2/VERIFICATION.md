---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For a minimum support 2-dimensional binary subcode D, its nonzero projective generator-column multiplicities a,b,c satisfy a+c,b+c,a+b divisible by four, hence all a,b,c even. Splitting each projective column class in equal halves creates a test matrix X. If d2>=2R2+2, covering supplies Y with support less than d2; M-Y also has support less than d2. Both are rank one. Because their row spaces span the row space of rank-two M, Y=PM, M-Y=(I-P)M with complementary rank-one 2x2 maps. Over F2 P is an idempotent of trace 1; its image and kernel are distinct nonzero binary column types, so X-Y vanishes on at most d2/2 support positions. This contradicts its covering radius. Thus d2<=2R2+1, and parity sharpens to d2<=2R2. Independently checked modular half-split and an explicit doubly-even [6,2] code with (d2,R2)=(6,4).

## originality

PASS

Yu–Schwartz establish the order-two general inequality d2<=2R2+2, and Alfarano et al. establish the corresponding all-orders universal bound. Neither implies d2<=2R2 even when doubly-evenness forces d2 even. Essayag–Zabokritskiy give a conditional +1 inequality for q>=R, insufficient for arbitrary binary covering radii. Best-of-knowledge PASS after comparison, but full recent source text was not newly accessible in this run.

## value

PASS

The generalized packing–covering inequality was an active exact question in coding theory. A global strict one-unit packing-radius gap for the infinite natural class of 4-divisible binary linear codes refines the universal solved inequality in a structural, application-relevant subclass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
