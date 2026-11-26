---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The module-isomorphism relation is simultaneous GL₂(k)-conjugacy, so fixing a representative X leaves precisely its invertible centralizer acting on Y. For X=0, rational similarity gives q scalars, q nontrivial Jordan classes, q(q−1)/2 split regular classes and (q²−q)/2 irreducible classes. For a nonzero scalar only Y=0 is possible in odd characteristic. For the nonzero nilpotent block the compatible Y has diagonal (a,−a), lower-left zero, and free upper-right b; conjugation fixes a and shifts b by an arbitrary amount if a≠0, giving q+(q−1) orbits. For split nonzero trace zero, X has eigenvalues ±a and diagonal centralizer, with compatible off-diagonals (b,c) classified by the two nonzero axes, the origin and nonzero bc. For nonsplit trace zero, X=mθ on F_{q²}, θ^q=−θ; each linear map is uniquely z↦Az+Bz^q (evaluate at 1 and θ for uniqueness). Anticommutation sets A=0; the image of s↦s^(1−q) is the norm-one group (order q+1), giving one orbit per nonzero norm and the zero orbit. For nonzero trace and singular X, use diag(t,0) giving the q fixed Y=diag(0,b). For simultaneous nonzero trace and determinant the spectra of X and −X are disjoint, so the Sylvester map is invertible even for nonscalar Jordan X. Each allowable characteristic polynomial has exactly one nonscalar class, including the Jordan class when its roots repeat. These disjoint cases yield 4q²+q−2 for every odd prime power. A fresh enumeration using all of GL₂ in each tested field yielded 417 labeled pairs in 37 orbits for q=3 and 4705 in 103 for q=5 (replay: /workspace/branches/2c2c50d7-c13d-405a-ac11-d7ca67201f77/independent_orbit_bruteforce.py). The supplied verify.py was inspected, not run; both finite checks are restricted to prime fields and the general conclusion rests on the algebraic argument.

## originality

PASS

The supported distinct result is an explicit unweighted rational orbit census and its split/nonsplit classification in dimension two at deformation parameter −1. The known labeled count, complex geometric components and GIT-closed orbits are not credited as new. No inspected source supplies the full rational classification or unweighted invariant, and the assessment is bounded.

## value

PASS

Dimension two is the first where nonzero anticommuting operators and nonsplit rational similarity occur; it is a natural base case for unweighted module enumeration at the sign parameter. An exact orbit count answers a different question from a weighted or point count and is accompanied by class invariants, in particular the norm rather than a split eigenbasis for nonsplit X. It provides an exact benchmark for rational classifications and distinguishes nonsemisimple classes that a GIT quotient loses. Neither an extension to larger dimensions nor a novel method of rational canonical forms is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
