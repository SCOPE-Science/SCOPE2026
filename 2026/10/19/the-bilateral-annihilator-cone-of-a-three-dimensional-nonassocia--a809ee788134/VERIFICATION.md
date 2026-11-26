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

The two witnesses are independent: bilateral annihilation is exactly singularity of L_x and R_x. Expanding the columns from the multiplication table gives D_L=aS+tc(a²+c²-bc) and D_R=aS+tb(a²+b²-bc) for S=a²+b²+c², whose difference is -t(b-c)S. On b=c the remaining equation is a(a²+tab+2b²)=0; when b=c=0 only zero remains. On S=0 it is -tbc(b+c)=0, giving the axes and antidiagonal root directions after scaling a nonzero b or c to one. Both tests are reversible. The directions are disjoint away from zero after the explicit characteristic-two deduplication, since distinct roots give distinct normalized coordinates and t≠0. The quadratic-character counts include discriminant zero, and for q=9,t=1 the three arguments lie in the square subgroup. For a common inverse, the commutation condition ce=bf forces any inverse of a nonscalar x to have imaginary part proportional to that of x; the two imaginary equations then force bc(b-c)=0. Thus the inverse, if any, lies in the same quadratic plane. Its existence is equivalent to nonzero norm, by the determinant of multiplication in that plane or the quadratic conjugate. This leaves exactly the nonzero diagonal line in odd characteristic and nothing in characteristic two. The arbitrary-field proof, including inseparable roots in characteristic two, is decisive; verify.py is only a finite determinant/kernel census, not an independent check of inverse counts, and was inspected without execution.

## originality

PASS

The supported distinction is the simultaneous-singularity locus over all fields and parameters, its arithmetic enumeration, and its intersection with the existing unit locus. Prior sources determine major ingredients, even the same component directions in characteristic two as a subalgebra classification, but the inspected claims do not establish the bilateral property of those directions or exclude all others. No novelty is credited for the separate real base determinant cubics or classification of the quadratic planes or units.

## value

PASS

Bilateral annihilation is a natural invariant independent of invertibility in this nonassociative family. Resolving two cubic equations into at most nine rational directions, with the arithmetic variation and characteristic-two collapse explicit, gives a usable classification not supplied by separate one-sided determinant equations or by a unit count. The identification of exactly the inverse-bearing part explains concretely how the two properties coexist.

The dated certificate retains the supplied scientific assessment, sources and limitations.
