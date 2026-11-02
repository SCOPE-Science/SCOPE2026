---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For λ=1,2 in F3 the displayed quartics are smooth: ∂F/∂x3=x0^3 forces x0=0 and remaining partials contradict projective nonzero coordinates. The λ fibers are F3-projectively isomorphic by swapping x1/x2 and negating x3; thus one arithmetic isomorphism class, not two distinct surfaces. Veniani Example5.1 establishes *exactly* 58 geometric lines for nonzero parameter, while the package provides 27+27+3+1 explicit lines. For the A family substituting line coordinates into quartic reduces to t^9+λt^3-t=0 (similarly B to u^9-λu^3-u=0); separability of these linearized polynomials, Frobenius minimal quadratics and order-8 roots yield ten fixed lines and six Frobenius 8-orbits. The explicit incidence formula makes an intersection Gram matrix with self-intersection -2 and simple meeting pairs +1. Independent exact-rational Gaussian elimination of the 58x58 Gram for each λ gives rank 22 and 357 edges, degree sequence 3×2,12×54,30×2; orbit sums for Frobenius powers 1,2,4,8 give invariant Gram ranks (8,10,14,22). Since geometric K3 b2=22 and the intersection pairing on line classes is nondegenerate of rank22, these classes span all twisted H2; finite-order Frobenius fixed-space dimensions force characteristic polynomial (T-1)^6(T^8-1)^2. Untwist by factor3 and apply Lefschetz trace/exponential to get Z(t)=1/[(1-t)(1-9t)(1-3t)^6(1-3^8t^8)^2], N_n=1+3^(2n)+3^n(6+16 1_{8|n}), geometric Picard22, arithmetic rank8. This is cohomological proof for all n, not finite point-count extrapolation. The independent Gram calculation assumes the explicitly stated incidence rules; finite-field line identities are also proved algebraically and checked by the inspected package verifier.

## originality

PASS

Veniani 2016/2021 Example5.1 already supplies the 58-line quartic family and exact geometric line count, with supersingularity; Degtyarev supplies broader line-configuration constraints. The line Frobenius orbit cycle pattern 1^10 8^6 is also prior information and cannot be represented as new. The assessed result is the *full finite-field surface zeta function*: determining rank22 of a Frobenius-marked intersection lattice and fixed ranks (8,10,14,22), which is not logically implied merely by line counts or orbit lengths. The very relevant Veniani primary example was read and no equivalent zeta formula located, but unsearched finite-field zeta tables and alternative isomorphic quartic models remain a real historical risk.

## value

PASS

A complete Hasse–Weil zeta function, rather than a bounded point table or line count, gives all extension counts and the arithmetic Picard rank of a geometrically supersingular K3 surface. Showing how the explicit 58 geometric lines fill H2 and recover Frobenius is a natural arithmetic-geometric question with a fully determined answer. The two λ values are correctly treated as the same isomorphism class, avoiding inflated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
