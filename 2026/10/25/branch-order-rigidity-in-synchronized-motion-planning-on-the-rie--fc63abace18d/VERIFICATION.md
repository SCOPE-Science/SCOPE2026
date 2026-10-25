---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Direct reproducibility checks and their scope

The mathematical verification uses exact symbolic equalities and topological arguments, not computational experiments.

1. For any finite solution to \(u^a=v^b\), calculate \((t^b u)^a=t^{ab}u^a=t^{ab}v^b=(t^a v)^b\). The reciprocal path connects the unique infinite fibre point to \((1,1)\). Both projections are onto, hence synchronized paths exist for every endpoint pair.
2. On the endpoint slice \((x,0)\), continuity of a purported planner supplies \(h(x)^b=x^a\). On a sufficiently small loop around the origin, winding forces \(b\mid a\). The other slice \((0,y)\) supplies \(k(y)^a=y^b\) and forces \(a\mid b\). Together they force equal positive exponents; any unequal pair lacks even a single local planner around the branch-value endpoint.
3. At equal exponents, duplicate an ordinary sphere motion-planning path in both coordinates. Three open domains suffice in the reduced convention.
4. The rational cohomology ring of the endpoint space is \(\mathbb Q[u,v]/(u^2,v^2)\), with degree-two generators. The class \(a u-b v\) has nonzero square \(-2ab\,uv\). Since it restricts to zero on every open set where the endpoint-comparison maps are homotopic, the relative cup-product argument requires at least three sets. Pulling back the usual three-set sphere planner provides an upper bound of three, so normalized homotopic distance equals two.

The evaluation-map continuity follows from compact-open path topology. Infinite strict complexity means no finite open cover by local planners; the local contradiction is stronger. The result is not a calculation of the strict complexity of all degree-matched sphere maps, nor evidence of an independent audit or exhaustive literature coverage.
