---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The actual integral Lie algebra has [e1,e2]=e3 and [e1,e3]=2e4. A pair bracket gives a_i b_j-a_j b_i and 2(a_i c_j-a_j c_i), with central d unconstrained. When 2 is invertible, a=0 yields a linear component dim 3m; when a !=0, b,c must each be proportional to a, giving rank(a;b;c)<=1 times A^m of dim 2m+2. Intersection is a=0,rank(b;c)<=1 times A^m (dim2m+1). Standard rank-one determinantal geometry makes every component smooth off intersection and singular at rank zero; the reduced union singular locus is intersection and dimensions coincide iff m=2. When p=2, only rank(a;b)<=1 remains and c,d are free; irreducible dimension 3m+1 and singular locus a=b=0 dimension 2m. Rank-one matrix count D_{r,m}=1+(q^r-1)(q^m-1)/(q-1) and inclusion-exclusion yield q^{3m}+q^{m+2}(q^m-1) for odd q and q^{2m}(1+(q+1)(q^m-1)) even q. Bundle stratification justifies motivic substitution by L. Independent full-element checks give 160 commuting pairs over F2 and 1377 over F3; not an extrapolation. The unreduced bracket scheme is not claimed reduced.

## originality

PASS

PASS, with explicit prior carve-outs: Goodwin–Röhrle 2012 already gave characteristic-zero m=2 two-component case, Farnsteiner 2018 good-characteristic pairs, and the characteristic-two all-arity formula is a specialization of known Heisenberg commuting-tuple determinantal cases. The remaining arbitrary odd-characteristic m>=3 classification, inequivalent dimensions, singular strata and arithmetic/motivic census are not asserted by the inspected sources. No novelty is claimed for known pair or Heisenberg specializations.

## value

PASS

The B2 nilradical is the smallest non-simply-laced positive-root Lie algebra where a Chevalley constant dies in characteristic two. The complete all-arity reduced commuting-locus geometry and its point counts exhibit a meaningful bad-prime component-collapse and the non-equidimensional shift at m>=3. This is a natural canonical model, not a random low-dimensional slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
