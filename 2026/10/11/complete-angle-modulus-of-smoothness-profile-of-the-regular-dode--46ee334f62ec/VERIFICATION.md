---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

For the displayed six-pair-of-facets norm on R^2, its unit sphere has twelve edges. D12 symmetry reduces x to E0. For y on relative edges E0..E5, signed support-functional certificates yield lower bounds 2, 2-(2-sqrt3)d, (4-d)/sqrt3, 1+sqrt3-d, 4-sqrt3*d and (2+sqrt3)(2-d) for s=||x+y|| at d=||x-y||. The two split certificates for edges E1 and E5 are nonnegative on the respective triangles a+b<=1 and >=1; linear ones are exact on E2..E4. The lower envelope is the claimed 3-branch M, j=6 forces d=2, and edges E7..E11 reduce by y->-y because M is a strictly decreasing involution. Three explicit affine edge families realize each branch and all endpoint values, giving m(epsilon)=M(epsilon) and rho^a=1-M^2/2. I independently reconstructed all signed facets from exact Q(sqrt3) geometry, checked edge certificate identities and signs on their complete triangles, all 18 envelope comparisons by interval endpoints, and all sharp-family norm equalities by every signed facet and affine endpoints. No numerical sampling is used as the continuum proof.

## originality

PASS

Best-of-knowledge novelty survives the strongest located same-norm and stronger-parameter comparisons: the 2022 source defines angle smoothness and relates it to the constrained minimum chord but does not supply this dodecagonal 3-branch evaluation; the public dodecagonal angle-convexity result controls the opposite maximum chord; the P-angle exact result gives a non-sharp lower-bound description of the chord feasible region; and an all-even-regular-polygon theorem controls Day's unconstrained scaled smoothness rather than the fixed-separation minimum. A published octagonal unit-separation result is on a nonisometric norm and single epsilon. Actual full published mathematical files were read for four closest results, and the primary 2022 accessible indexed source was inspected; no blanket novelty certification is claimed.

## value

PASS

The source defines a natural geometric modulus measuring the worst P-angle at every prescribed separation. The regular dodecagon is a canonical non-smooth normed plane with enough face classes to create genuinely different optimizer regimes. The result computes the entire continuous epsilon-profile exactly and shows two nontrivial, sharp transitions at 1 and sqrt3, plus an involutive minimal-chord envelope. This is substantially more informative than one epsilon value and complements, without being implied by, the opposite extremal dodecagonal convexity profile. A researcher studying polygonal moduli and normed-circle chord geometry could use the exact function for comparison or optimal estimates, despite its elementary finite-facet proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
