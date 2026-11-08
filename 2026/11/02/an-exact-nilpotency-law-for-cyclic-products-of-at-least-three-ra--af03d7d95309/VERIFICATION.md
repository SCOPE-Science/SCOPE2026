---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For fixed P:V0->Vt-1 of rank r and independent uniform final B:Vt-1->V0, the product PB maps im(P) to itself and its restriction is uniform on End(im P), because the induced map Hom(im P,V0)->End(im P) is surjective with equal-size fibers. BP nilpotent iff PB nilpotent; Fine–Herstein gives probability q^{-r}, including r=0. Thus conditional P(BP nilpotent|P)=q^{-rank P}=q^{-n0}|ker P|. Each fixed nonzero starting vector survives t-1 independent uniform maps with probability s=prod_{i=1}^{t-1}(1-q^{-ni}); summing indicators gives E|ker P|=q^{n0}-(q^{n0}-1)s. Therefore for all finite q, t>=3, any positive rectangular dimensions, P(cyclic product nilpotent)=1-prod_{i=0}^{t-1}(1-q^{-ni}). The same proof actually includes t=1,2 but these are explicitly acknowledged as prior. Independent exhaustive product enumeration checked q=3,n=1,t=3: 19/27 and q=2,n=2,t=3: 37/64. Finite checks do not establish arbitrary dimensions; the kernel moment proof does.

## originality

PASS

Best-of-knowledge priority comparison on the exact final statement, allowing explicit inaccessible-primary-source risks; known related first-moment, connectivity, single-class and one/two-factor theorems are acknowledged as prior, not claimed new.

## value

PASS

The simple symmetric dimension-multiset formula gives an exact natural probability for random cyclic finite-field linear-map products of arbitrary length and rectangular shape. The move from known two-factor to all cyclic lengths uses a nontrivial rank-conditioned transfer plus kernel survival and is meaningful for random matrix semigroups; not a nilpotency-index or Jordan-type classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
