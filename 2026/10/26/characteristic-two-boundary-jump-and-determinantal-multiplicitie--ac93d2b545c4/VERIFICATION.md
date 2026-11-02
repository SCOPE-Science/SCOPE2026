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

Exact toric reconstruction from the six lattice vertices confirms that every corner chart is unimodular and has the same six monomials in local coordinates a,b. The second Hasse-principal-parts matrix has a unit 3x3 block and residual B=[[b,0,b^2],[2a,2b,4ab],[0,a,a^2]]. An independent SymPy determinant and all 9 two-minor computation gives determinant identically zero, minor ideal (a^2,ab,b^2) whenever 2 is invertible, and (ab) in characteristic 2; entries give (a,b). These are universal polynomial identities, not evaluations at sample points. Thus rank <=4 scheme is six disjoint length-three infinitesimal points in characteristic !=2 (total length 18) and the reduced union of six toric boundary components in characteristic 2; rank <=3 is the reduced six torus-fixed points in all characteristics. The torus rank is 5 and scheme boundary interpretation follows by chart overlap.

## originality

PASS

Qualified PASS: the 2001 Lanteri–Mallavibarrena Proposition 4.3 describes precisely the same six-cubic projection, with rank five off six vertices and rank three at those vertices over the complex numbers. It does not determine scheme multiplicities or characteristic-two ranks. Perkinson 1996 gives general toric principal-parts tools; his 2000 Inflections of Toric Varieties is highly relevant but inaccessible in full after lawful route and authorized institutional attempt, so an older implicit proof cannot be excluded. The explicit all-characteristic determinantal scheme statement remains an apparent new contribution, not a novelty certificate.

## value

PASS

This is a motivated scheme-theoretic refinement of the classical projected Togliatti example. A support/rank table is insufficient to determine local nilpotent thickness or reducedness. The exact characteristic-two degeneration changes the dimension of the natural Hasse-jet degeneracy locus from a finite length-18 scheme to a reduced anticanonical boundary cycle, while the next stratum stays reduced.

The dated certificate retains the supplied scientific assessment, sources and limitations.
