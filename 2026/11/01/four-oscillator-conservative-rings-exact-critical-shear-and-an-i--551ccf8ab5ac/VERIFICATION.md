---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Differentiate bond phases y_j=θ_{j+1}−θ_j to obtain dot y_j=F(y_{j+1})−F(y_{j−1}), conserving y1+y3=a. Torus coordinates u,v yield dot u=A(a)sin v, dot v=B(a)sin u and H=B cos u−A cos v. Solving B=0 and A=0 gives exactly two leaves a_±; independently differentiated AB at a_- and verified |(AB)'|=4cd, nonzero shear κ=4cd/sqrt(c²+d²). On a shear leaf the moving angle rotates with speed κ sin(frozen angle), primitive P=2π/(κ|sin w|), whose exact Haar distribution gives inverse-time tail and divergent mean. Otherwise H is Morse with 2 centers and 2 saddles; by coarea E[P] reduces to integral P(E)² dE, locally finite because saddle period diverges logarithmically. Center period 2π/sqrt(|AB|) therefore tends to π/sqrt(cd)|a−a±|⁻½. Assumption is conditional Haar on leaf and reduced modulo overall phase; no full-space claim.

## originality

PASS

Pikovsky 2026 develops general conservative nearest-neighbor phase differences and Burylko et al 2018 present four-oscillator periodic foliation and integrals in a specialized model. Neither inspected result computes the location of the two mixed-coupling shear leaves or this conditional Haar primitive-period law and its moment contrast. These exact quantitative laws are plausibly new; older specialized integrable oscillator work remains a priority risk.

## value

PASS

The exact exceptional-shear probability tail reveals infinite mean periods on codimension-one conserved leaves despite almost-everywhere finite mean periods on regular neighboring leaves. Coupling-dependent locations and universal power-law coefficient quantify a real degenerate integrable bifurcation, beyond known integrability statements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
