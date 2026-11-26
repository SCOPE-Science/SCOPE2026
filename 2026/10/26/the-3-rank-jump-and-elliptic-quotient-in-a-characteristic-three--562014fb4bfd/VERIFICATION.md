---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

With X+Y+Z=1 and t=X−Y, write X=Z−1−t, Y=Z−1+t. Then r=1−Z−t² and d=t−t³. Exact substitution recovers the stated quotient polynomial up to a unit, and the cycle acts by t↦t−1, with r,d invariant. Away from infinity the map is finite étale since the Artin–Schreier derivative is −1. In the chart Z=1 the line at infinity is w=0; the quartic there is −u⁴, with w derivative 1+λ at the unique point. For λ≠−1, completing the elliptic square gives the stated monic cubic, with discriminant (λ−1)/(1+λ)^5 and c4=λ²/(1+λ)². This gives the exact two singular parameters and j=λ⁶/(λ²−1). At the unique fixed point, w=u⁴/(1+λ)+O(u⁵) and the action in local parameter u satisfies σ(u)−u=(w−u²)/(1+u), of valuation two. Thus the sole lower break is one and the different has exponent four. Deuring–Shafarevich then gives f3(C)=3f3(E). Independently, on the smooth plane quartic the Hasse–Witt coefficient matrix from F² has diagonal λ²−λ and one cyclic off-diagonal −λ; its determinant is (λ(λ+1))³ and the matrix vanishes at λ=0, corroborating the full rank classification on the smooth locus. The own symbolic replay checked the affine polynomial, boundary terms, discriminant and Hasse–Witt matrix universally modulo three.

## originality

PASS

There is exact overlap for the elliptic moduli map after a parameter change, and known central-curve coverage. Neither the j-function in isolation nor the zero-rank Klein specialization carries the originality pass. The distinct result established here is the explicit wild C3-cover description for this smooth plane quartic pencil, with its ramification and the consequent rank classification of the genus-three source. The inspected other elliptic family is obtained by a different quotient from genus five; knowing its j-map does not produce this map from the quartics.

## value

PASS

The cyclic pencil through a classical quartic gives a natural test of wild ramification and ordinarity under deformation. The explicit cover and the complete geometric jump calculation locate exactly where ordinarity fails on the entire smooth pencil, rather than merely demonstrating some ordinary members. The one-branch analysis and its connection to the varying elliptic quotient are useful even though the same elliptic moduli occurs in another family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
