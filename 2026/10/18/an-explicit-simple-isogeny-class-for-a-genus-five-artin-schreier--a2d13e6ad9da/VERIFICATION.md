---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The rational function has just the poles 0,1,infinity of orders 1,1,2. An additive coboundary h^3-h can only have pole orders divisible by 3, even after extending the constant field, so the cover is geometrically connected. These prime-to-3 orders yield full ramification and different exponents (3-1)(order+1). Riemann–Hurwitz gives 2g-2=8, and Deuring–Shafarevich yields 3-rank 4. The three branch points each contribute one rational point over every extension. Elsewhere the map y to y^3-y has kernel of size three and image the trace-zero hyperplane. As an independent recheck, I used separately selected irreducible field moduli and evaluated the equation after multiplying by x(x-1), directly counting all affine (x,y) outside the two finite poles, with no traces or inversions; the totals are 6,18,24,66,291. Expanding exp(sum_(n=1)^5 (N_n-3^n-1)T^n/n) gives the first half (1,2,6,8,10,15); the genus-five functional equation gives the remaining (30,72,162,162,243). The sum is 711=9*79. Independent factorization over F_5 returned one factor of degree ten, the monic T^10-T^9-T^8-T^7+T^3+2T^2-T+2, times the unit -2. The original polynomial is primitive with leading coefficient not divisible by 5, so this establishes rational irreducibility, also for its reciprocal Frobenius characteristic polynomial. A proper nonzero abelian subvariety over F_3 would give a proper characteristic factor via the rational Tate module; thus the Jacobian is F_3-simple. The minimal geometric automorphism assertion used as background is the same model and parameters in the originating Proposition 5.5, Case 2.

## originality

PASS

The distinct result is the realized curve-to-class association: the exact curve of Tafazolian–Kazemifard has Jacobian in the already catalogued isogeny class 5.3.c_g_i_k_p. The original paper provides the model and geometric automorphism result. LMFDB gives the identical abstract numerator, class properties, and virtual point counts, but does not identify this model and specifically says a non-hyperelliptic Jacobian was unknown there. Neither discovery of a new abstract class, nor novelty of the class's simple flag or arithmetic data separated from this model, is credited.

## value

PASS

The curve is a singled-out exact example from a minimal-automorphism construction, not an arbitrary equation picked for tabulation. Identifying its entire zeta function supplies a concrete Jacobian realization of a known class where the inspected database lacked a non-hyperelliptic example (the curve has no geometric involution). This arithmetic realization, independently certified by finite counts and the functional equation, has value beyond recomputing the table's abstract class invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
