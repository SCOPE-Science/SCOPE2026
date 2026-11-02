---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: The regular basis dx/y, dx/y^2, x dx/y^2 has pole and branch orders compatible with genus 3. Cartier semilinearity gives omega1 -> sqrt(b)*omega2+sqrt(d)*omega3, omega2 ->0, omega3 ->omega1. Smoothness forces (b,d) not (0,0), rank 2 gives a-number1. Iterated rank is zero when d=0 and two when d≠0; in d=0 the additive separable quartic L(x)=x4+a x2+b x has V4 translation action with three elliptic genus-one quotients Y^2+(b/t)Y=X^3+c, each smooth supersingular j=0, and odd-ell character decomposition induces Jacobian isogeny to their product. d≠0 gives p-rank2 and symmetry forces the remaining slope pair 1/2. In Fq, fprime=d x^2+b: d=0 requires b!=0, d!=0 excludes exactly one c per (d,a,b), producing marked counts. Independently enumerated all coefficient tuples q=2,4,8,16 and checked stable Cartier ranks.

## originality

PASS

PASS, qualified: Classical cyclic trigonal quartic normal forms and characteristic-two genus-three Newton polygon shapes are prior (Bouw et al; Nart-Ritzenthaler 2003), and V4 elliptic quotient isogenies are known tools. The explicit coefficient hyperplane d=0, uniform a-number 1 and all Fq coordinate-marked counts were not located as an implication or formula of the inspected statements; the old general isomorphism-class enumeration does not trivially give marked presentation counts.

## value

PASS

PASS: This gives an exact moduli-in-a-marked-chart p-rank/NP stratification and complete finite-field polynomial presentation counts for a natural family of Picard curves, with constant a-number and explicit supersingular divisor.

The dated certificate retains the supplied scientific assessment, sources and limitations.
