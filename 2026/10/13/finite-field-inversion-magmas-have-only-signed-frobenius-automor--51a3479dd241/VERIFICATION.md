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

For y≠0, interior P_y(x)=y/[x(y-x)] has collision pairs x and y-x except when x/y is in B={r:r(1-r)=1}, |B|<=2; boundary fiber x=0,y has y^-1. Every pointed automorphism sends good paired fibers to good paired fibers, yielding F(y-x)=F(y)-F(x) outside B. In fields q>=7, at most six excluded auxiliary choices give negation/additivity, while q5 has B empty; q2,3,4 are directly small additive-inversion cases. From F◦ι=ι◦F get c=F(1), c²=1. G=cF is additive, fixes one, preserves inversion, and Hua identity x²y=x-(x^-1+(y^-1-x)^-1)^-1 gives multiplicativity, hence Frobenius. Each ±Frobenius conversely preserves star. For socle nonzero u, the rational condition on α=t/u yields α²+α+1=0 (or 4=1) for all admissible α, impossible for q>=5. Independent complete pointed-permutation checks q2,3,5,7 recovered 1,2,2,2 automorphisms. Universal proof does not rely on those finite checks.

## originality

PASS

The construction and finite order-five example are explicitly known from Byott–Jasko; the new all-prime-power class of inversion-magmas and signed-Frobenius automorphisms requires reconstructing addition from P_y collision fibers, not just applying Hua. Source full text could not be independently accessed, creating a significant—not automatically failing—best-of-knowledge priority risk. If an unseen broad lemma proves automatic additivity, originality would need revisiting.

## value

PASS

The inversion permutation is a canonical family of the pointed magma construction. Exact automorphism rigidity across every finite extension field and socle collapse at q>=5 settle substantive structure that a finite table or applying a field automorphism definition would not supply. Reconstruction of field addition from collision fibers is a key lemma, and the precise signed-Frobenius group is a natural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
