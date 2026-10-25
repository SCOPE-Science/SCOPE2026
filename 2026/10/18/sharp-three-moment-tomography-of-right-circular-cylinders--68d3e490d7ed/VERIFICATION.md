---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Using T=|U·e|~Uniform(0,1), Minkowski support additivity gives W=d sqrt(1-T^2)+hT. Direct integrals give m1=pi*d/4+h/2; m2=(2d^2+2dh+h^2)/3; m3=3pi*d^3/16+3d^2h/4+3pi*d*h^2/16+h^3/4. Fix m1=m: h=2m-pi*d/2, and m2 becomes a strictly convex quadratic in d with candidate root sum P=8m(pi-2)/(pi^2-4pi+8). The m3 divided difference [G_m(d)-G_m(P-d)]/(2d-P) has leading coefficient pi(pi^2-12)/64<0 and negative discriminant for m>0: discriminant proportional to -(pi^2-12)*Q(pi), Q(z)=z^4-6z^3+4z^2+36z-64, Q strictly increasing on z>=3 yet Q(22/7)=-104/2401<0. Thus two distinct m2-candidates have distinct m3. The scale-free R(h/d)=m2/m1^2 decreases then increases with minimum at lambda*=(4-pi)/(pi-2), yielding two-moment collisions. Immersion at the quadratic fold follows from nonzero m3 derivative; injective C1 immersion plus compactness implies compact-set Lipschitz inverse. Independently verified integral m3 and divided-difference symbolic coefficients/discriminant with SymPy, plus finite positive collision; these do not replace the all-cylinder algebra.

## originality

PASS

Best-of-knowledge original claim: the mathematical implication and same-object comparisons below show no identified covering result. The decisive proof and quantitative classification are distinct from established background; incomplete primary sources are named as priority risks, not cleared without reading.

## value

PASS

The first two or three unlabeled spherical width moments are minimal low-data inputs in integral geometry/inverse stereology; a sharp cutoff strictly stronger than entire-law identifiability and a stability assertion are motivated exact tomography facts. The nontrivial quadratic fold resolved by a strict cubic moment is useful for reconstruction without direction labels, not routine cylinder-volume substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
