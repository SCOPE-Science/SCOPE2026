---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Independently reconstructed the entire finite domain: [10 choose 2]_2=174251, generated GL4(F2) with adjacent coordinate transpositions and an elementary transvection, enumerated all pencils and traversed their 54 actual orbits; size sum 174251. For each of 54 orbit seeds, an independently implemented SymPy characteristic-two Gröbner calculation used both defining quadrics and all six 2x2 Jacobian minors on each of four projective affine charts; precisely eight seeds have unit ideals on every chart, totaling 40320 smooth pencils with sizes 2520 twice, 5040 five times and 10080 once. Complete intersection adjunction gives degree four and genus one; over F2 all smooth elliptic curves have rational points. Independent direct 15-point evaluations returned every mask, N=1,2,2,3,4,4,4,5, and each sorted 5/7/9 quadric-point profile. Local power-series solution through order three at every rational point verified the 4P osculating-plane counts 1,0,2,1,0,4,0,1; explicit GF2 Groebner elimination for (20,609), x0=0, x2=1 gave (x1+x3^3+x3^2,x3^4) with no points at x2=0, length four. Direct enumeration of all 15 planes verified coplanarity unique to (20,842) among N=4. All seven-/five-/nine-point member types were separately checked by exact F2 gradients and rational counts. The exact finite algorithm is a proof of this finite classification; neither finite experiments nor logs are invoked as infinite-field proofs.

## originality

PASS

The result is mathematically equivalent to a degree-four polarization classification of elliptic curves over F2. The eight-orbit headline and contact/coplanarity distinction are substantially classically implied by Husemöller’s five curve classes and Picard/automorphism facts; these are not counted as novel by themselves. However the actual final claim contains a complete per-embedding joint profile of all three rational defining quadrics (split, nonsplit, cone), explicit binary masks, smooth pencil counts and finite orbit multiplicities. Searches and full relevant source passages found no directly covering table; this incremental exact census is accepted best of knowledge with explicit unindexed-prior-table risk.

## value

PASS

A smooth degree-four elliptic normal curve and its unique 2D defining space of quadrics are canonical basic embedded genus-one models. Over the smallest field, the finite classification is a natural complete moduli question rather than a parameter slice. The joint arithmetic type of its THREE rational pencil quadrics (nonsplit 5-point, singular cone 7-point, split 9-point) is an informative embedded invariant not implied by the unpolarized point-count classification and not seen as an exact preexisting table. The per-type multiplicities, rational contact and coplanarity distinguish naturally polarized models. Eight-orbit counts and some contact features follow classical Picard theory, so they do not alone justify value; the complete exact binary quadric-profile atlas and reproducible finite geometric smoothness certificates provide the nontrivial remaining standalone fact, with meaningful potential use as small-field test cases in arithmetic geometry and finite projective geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
