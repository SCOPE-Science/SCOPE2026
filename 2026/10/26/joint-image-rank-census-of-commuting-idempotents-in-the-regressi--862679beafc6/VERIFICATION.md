---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For commuting idempotents e,f the product g=ef=fe is itself idempotent; eg=ge=fg=gf=g and both preserve each g-fiber. Each fiber B has a unique fixed root c=g(x)=min B because g is regressive. Non-root e-fixed set E and f-fixed set F are disjoint. Every point in E is f-sent to c, every point in F e-sent to c, and every other point chooses e-image independently from earlier E∪{c} and f-image from earlier F∪{c}; these are both necessary and sufficient to make ef=fe=c on that block. Building an ordered fiber induces u+v+(1+u∂u)(1+v∂v) on its fixed-point rank polynomial. Labeled set partitions of the product fibers then give the exponential formula, including n=0 identity. Independently enumerated every regressive idempotent and all ordered commuting pairs at n=1..6, comparing every three-rank coefficient with the independent weighted partition recurrence, yielding totals 1,4,21,139,1114,10465. The finite check does not establish the all-n EGF; the bijection does.

## originality

PASS

PASS, qualified by same-object inaccessible primary literature. Zhao–Hu (2024) study exactly D_n, but their publisher abstract identifies maximal/idempotent-generated subsemigroups and abundance, not the joint commuting-rank census; the complete text was not obtained via OA/arXiv or authorized Oxford (VPN disconnected), so no definitive NOT_COVERING claim is made. Zhao–Hu (2025) treat partial regressive monoids; Fernandes (2024) covers the narrower order-preserving interval-image case. General full-transformation or monotone commuting-pair enumerations do not immediately yield the position-sensitive regressive three-rank distribution. The full natural family and all rank triples appear new on inspected evidence, with a clearly stated historical priority risk.

## value

PASS

Commuting idempotent pairs are a canonical invariant of the entire regressive transformation monoid, with each image rank and product rank motivated by projection structure. The complete all-n joint enumeration and differential fiber recurrence solve the natural classification rather than computing a tiny unmotivated slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
