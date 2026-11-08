---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For each degree d>=1, the endpoint-minimum-L2 polynomials h0,h1 are orthogonal to bubbles and have Gram H=R_d^-1 with a=1/[d(d+2)], b=(-1)^(d+1)/[(d+1)d(d+2)]. The global nodal Gram on unit metric K_(p,q) is [aq I_p,b J;b J,ap I_q]; its inverse row at a vertex of the p-side yields kernels K_incident=(A+B/p)/q and K_nonincident=B/(pq). For the p-leaf star q=1, every corresponding K_(p,q) edge kernel is precisely 1/q the star kernel, so summed L1 evaluation norm V_d(p)=∫|A+B/p|+(1-1/p)∫|B| is q-independent, increases with p by triangle inequality, and tends to ∫(|A|+|B|). Constant reproduction fixes negative excursion=(V_d(p)-1)/2. Independently inverted rational nodal mass matrices at d=1 and (p,q)=(2,3),(3,2),(1,5) verifying coefficient identities; supplied exact checker covers degrees 1..8 and p,q<=6. All-degree part follows from Legendre endpoint identity, not finite tests.

## originality

PASS

The Legendre endpoint Gram and block Schur-complement machinery are standard, and linear FEM/spline stability formulas precede the claim. Inspected Kayumov and Arioli–Benzi results do not state arbitrary-degree pointwise per-edge cloning between K_(p,q) and p-leaf stars or the q-invariant sharp evaluation norm. Historical unindexed metric-graph identities are an explicit residual risk.

## value

PASS

This is an exact operator-kernel equality across nonisomorphic graphs for every polynomial degree, not merely a bound; it determines actual extremal inputs, monotonicity and a sharp positivity overshoot in natural numerical projections. Restriction to vertices is mathematically motivated by finite-element nodal stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
