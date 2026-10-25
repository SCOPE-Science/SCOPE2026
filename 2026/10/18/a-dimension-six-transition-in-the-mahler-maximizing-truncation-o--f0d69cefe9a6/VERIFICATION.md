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

For d≥3, 0≤t≤2, the slab |sum x_i|≤d−t cuts exactly two disjoint corner simplices of volume t^d/d! from [-1,1]^d. The polar is conv(±e_i,±(1,…,1)/(d−t)); exactly the positive/negative cross-polytope facets are visible for 0<t<2, adding two equal pyramids of volume t/[d!(d−t)]. Hence Q_d=(1−t^d/(2^(d−1)d!))(1+t/[2^(d−1)(d−t)]). Independently verified symbolically in SymPy that derivative Q′=d/[2^(d−1)(d−t)^2]*(1−H_d(t)/d!) with H_d=t^(d−1)*[(d−t)^2+t(d−t+1)/2^(d−1)]. H′_d positive for t∈(0,2), d≥3; H_d(2)=2^(d−1)(d−2)^2+2(d−1) exceeds d! at d=3,4,5 and falls below d! at d=6, with elementary factorial induction for all larger dimensions. Thus exactly one interior optimum in d3..5 and strictly increasing Q for d≥6; independently checked exact Q_6(2)=4667/4608. Source verify.py checks rational nodes and facet signs but analytic induction supplies all dimensions. No theorem for t>2 or arbitrary convex bodies.

## originality

PASS

The exact four-dimensional small-cut product is already published and NOT new; the accepted claim is the complete all-dimension maximizing-depth classification with a strict d=6 boundary. The all-sign cube–cross-polytope intersection uses a different constraint. Shen–Dubovski 2026 facet-apex optimization has different original body/optimization but its full text remains a real priority risk.

## value

PASS

Two antipodal cube-corner truncations form a canonical centrally symmetric deformation of the cubic Hanner body, with t=2 the natural combinatorial boundary where further cube vertices would be removed. The optimal Mahler cut depth changes sharply from a unique interior value in dimensions 3–5 to the boundary in all d≥6. Proving the exact global one-parameter optimizer across every dimension is a motivated complete phase classification not supplied by the known 4D local expansion or broad Mahler inequalities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
