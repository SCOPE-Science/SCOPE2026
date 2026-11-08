---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For any planar convex body K and pairwise-intersecting noncollinear translates K+p_i, each normal direction gives three congruent projection intervals of length w_K(u), shifted by projections x1<=x2<=x3. Pairwise planar intersection forces range R=x3-x1<=w. Exactly one- and two-hit offset measures both equal R=w_T(u), and triple-hit equals w_K(u)-R. Integrating 0<=theta<pi via Cauchy perimeter identity gives m1=m2=P(T), m3=P(K)-P(T), total P(K)+P(T), without central symmetry or physical triple intersection. For equilateral centers and equal disks, inclusion–exclusion gives pair overlap B(q)=2(q arcsin(q)+sqrt(1-q²)-1) for q<=1 else pi q-2; triple overlap H(q)=0 for q<=sqrt3/2, 6(q(pi/6-arccos q)+sqrt(1-q²)-1/2) through q=1, else pi q-3. Exact class measures 3pi q-6B+3H, 3B-3H, H and D=3pi q-3B+H establish all q>0; H(h)=H'(h)=0,H''(h)=12 gives onset constant 6/(3+pi sqrt3/2). Independently sorted projection interval endpoints and integrated eight q values over 5000 normals each; finite quadrature checks support, not replace, the exact proof.

## originality

PASS

Cauchy perimeter and existence of transversals are classical and explicitly excluded as novelty. The claim fixes line measure and determines exact occupancy classes for three translates (including nonsymmetric K), plus full equilateral disk phase laws and onset coefficient. Heppes and Kaiser concern existence of a common stabbing line or separation thresholds, not the measures of lines hitting exactly j bodies. The formulas could be an implicit corollary of an older integral-geometric kinematic identity, which is an acknowledged residual risk.

## value

PASS

The fixed-direction equality m1=m2 and its global shape independence for arbitrary noncentrally symmetric convex K provide a natural integral-geometric conservation law for random stabbing lines. The all-ratio disk distribution quantifies a classical existence threshold and its sharp quadratic activation, giving precise line-incidence probabilities. These are coherent useful quantities, not merely re-computation of the threshold or Cauchy formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
