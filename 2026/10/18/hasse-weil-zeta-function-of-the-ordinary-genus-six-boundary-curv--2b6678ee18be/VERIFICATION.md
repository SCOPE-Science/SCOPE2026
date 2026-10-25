---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The rational function x+1/(x^3-x) has four rational simple poles on P1 over F3; the Artin--Schreier cover is geometrically connected and totally ramified over each, giving genus six by Riemann--Hurwitz and ordinary p-rank six by the standard Artin--Schreier p-rank formula. Translation x->x+1 satisfies f(x+1)=f(x)+1, and for 3 not dividing n cycles the three possible absolute traces; hence N_n=3^n+1 outside multiples of three. Independently built F_(3^n) as integer-coefficient quotient rings for n=1,...,6 and enumerated all y^3-y fibers for every nonpole x, obtaining EXACT N=(4,10,76,82,244,670), including N3=76, N6=670. Newton sums are (0,0,-48,0,0,60) and give a3=16, a6=118; genus-six Weil symmetry recovers a9=432, a12=729. Independently checked the entire numerator factors as (1-T+3T^2)^2(1+T-2T^2+3T^3+9T^4)^2 and P(1)=1296. Rational quartic reciprocal has no rational linear or quadratic factor by coefficient comparison, hence a simple abelian-surface isogeny factor. Explicit finite arithmetic plus Weil functional equation proves all extension counts rather than extrapolating a finite list.

## originality

PASS

Tafazolian Proposition 8.7--8.8 identifies the same c-dependent genus-six ordinary family and its geometric automorphisms (order 72), but its relevant section does not compute zeta numerator over F3 at c=1. Bouw--Ho--Malmskog--Scheidler--Srinivasan--Vincent compute zeta functions for Artin--Schreier y^p-y=xR(x), R additive, whose curves are supersingular and generally one-pole, unlike this four-pole ordinary model. General computational algorithms and Weil-isogeny tables do not by themselves identify the square product for this specific model. An equivalent finite-field equation/earlier point-count table remains a plausible priority risk.

## value

PASS

The genus-six ordinary curve is a distinguished geometric boundary member with unusually large automorphism group; identifying its exact F3 Weil polynomial, Jacobian isogeny type/order and all point counts is a natural arithmetic invariant of an independently motivated named curve. Even one exact prime-field model can be useful for comparisons in arithmetic geometry, unlike an arbitrary unmotivated random polynomial example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
