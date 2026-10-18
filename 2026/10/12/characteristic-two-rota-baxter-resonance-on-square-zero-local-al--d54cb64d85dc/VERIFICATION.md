---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Reconstructed the weight-zero identity for A=K⊕V with V²=0 and finite dim V=n≥1. Writing P(1)=a+u, P(v)=f(v)+L(v), scalar parts at (v,v) give f(v)²=2f(v)², forcing f=0 over any field; similarly (1,1) forces a=0. Then (1,v) gives L²=0; (1,1) gives 2L(u)=0. Conversely xP(y)+P(x)y∈V and P of this equals 2abL(u), so both constraints suffice. Thus P²(a+v)=aL(u), P³=0; characteristic two admits index 3 iff L(u)≠0; other characteristics require P²=0. Square-zero maps of rank r correspond to im U⊂ker W of dimensions r,n-r and an isomorphism V/W→U, proving M_q(n,r); each u-stratum follows from im L⊂ker L. Independent brute force over F2,n=2 enumerated all 2^9 linear maps, checked all basis-pair identities, found 16 RB maps with index counts 1,9,6. Full source result and verify.py were inspected, not merely log outputs.

## originality

PASS

The char2 resonance adds u not in ker L and exact q-even rank/index counts absent from the directly comparable characteristic-zero theorem. Full available Farooq text explicitly assumes characteristic zero and states P²=0 (Theorem 3.4); char2 contradicts a naive extension. Nearby exterior-algebra F2 classification has radical square nonzero and different multiplication, so its finite enumeration does not imply the split square-zero universal classification. Published search is nonexhaustive, with alias risk explicitly retained.

## value

PASS

This is a motivated sharp characteristic boundary of a standard operator identity on the natural universal radical-square-zero local algebra. The general all-fields structural equivalence and all-finite-fields rank/index census exhibit a genuine new nilpotency phenomenon and give exact data for arbitrary embedding dimension; this is more than a tiny numerical check or renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
