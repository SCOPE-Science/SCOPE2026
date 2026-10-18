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

The eight trilinear NDB basis checks for [t,x]=x reduce to b+c=0 and 2d=0, so for char(k)!=2 the nondegenerate matrix is [[a,b],[-b,0]], b!=0. Lie automorphisms t->t+beta x, x->lambda x preserve a and multiply b by lambda. Pairing the induced product against t,x gives t*t=-t-(a/b)x, t*x=0, x*t=-x, x*x=0; its commutator recovers [t,x]=x and its left-multiplication commutator satisfies the pre-Lie identity. A product isomorphism requires s=r lambda, so exactly the zero and nonzero parameter classes; the nonzero-idempotent locus distinguishes them. Independent GF(3) form enumeration yielded precisely six matrices (3 choices of a and 2 nonzero b), checking a non-real boundary; the algebraic proof, not the finite census, establishes all fields char!=2.

## originality

PASS

Kato proves the NDB criterion and gives two selected aff(R) examples, but his complete scholarly text does not classify every NDB bilinear form or the many-to-one map from form-orbits to LSA product-orbits. Medina–Saldarriaga–Giraldo classify broader real affine structures, but not which products are induced by all NDB forms, nor their form orbit parameter a. Thus the claimed complete fiber description is not an immediate reformulation of the two examples. Best-of-knowledge PASS with older low-dimensional classification risk.

## value

PASS

The complete fiber map for a natural 2D nonabelian Lie algebra is an exact structural moduli calculation: infinitely many form classes map to two pre-Lie classes, with an internal idempotent separator. The point is the phenomenon and classification, not simply listing a known two-class answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
