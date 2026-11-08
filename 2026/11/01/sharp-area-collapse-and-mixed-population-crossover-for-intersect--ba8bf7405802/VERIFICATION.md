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

For m+n>=1 independent standard unit-time planar Brownian motions/bridges, convex intersections containing 0 have min radial function. Polar area and Tonelli imply exact A_{m,n}=2pi integral_0^infty r S_K(r)^m S_B(r)^n dr without independence over angles. Checked radial Gaussian/arcsine and Rayleigh/uniform mixture derivatives against c/2 exp(-r^2/4) K0(r^2/4) and 2r exp(-r^2) K0(r^2). Small-r expansion K0(z)=-log(z/2)-gamma gives FK=cr(log(1/r)+dK)+O(r^3 log) and FB=r^2(2log(1/r)+dB)+O(r^4 log), constants as RESULT.md. At r=(cm log m)^-1 x, powers converge to exp(-x - pi^3 lambda x^2/4) if n/(m^2 log m)->lambda finite. Expanding logarithms to first relative order and integrating x e^-x or x e^-x² yields precisely the two loglog corrections shown. For tails, cutoff x<=12loglog m or sqrt(12loglog n), a fixed small-radius survival lower bound and exponentially decaying two-copy tail imply uniform integrability; origin contributes negligibly. Independently compared the two Bessel derivative formulas at multiple nonzero radii. Finite numerics are not an infinite proof, and random-area concentration is not claimed.

## originality

PASS

Best-of-knowledge mathematical implication comparison of actual primary material and published records. Novelty is provisional, with explicit unresolved historical-source risks. 

## value

PASS

The natural expected common territory of independent random convex hulls has fundamentally different m^-2(log m)^-2 and n^-1(log n)^-1 collapse rates depending on pinning. The nontrivial critical mixed population n~m²log m, limiting interpolation Φ and explicit second-order pure corrections quantify an unaddressed phase transition, beyond individual-hull coverage statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
