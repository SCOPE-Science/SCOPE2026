---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Inverse-affine mapping proves all area maximizers are images of equilateral circle triangles. Exact side lengths s_i and tangential derivative D_i identify a vertex with |D_i| bounded below by 9 b²(a²-b²)/(16a⁴) using trigonometric range and Heron. A bounded second derivative and a chosen signed angular step give a concrete gain at least 81 b⁷(a²-b²)²/(2048a¹⁰), uniformly for each area-maximizer. Near a=1+ε,b=1 the transverse Hessian around equilateral triples is negative definite, linear εδ term is explicit and completing square yields coefficient 9sqrt(3)/16. Independent 600 numerical derivatives matched analytic first variation to <8e-15; independent multi-eccentricity global optimizations showed normalized near-circle gap increasing toward 0.974278579, not used to prove the asymptotic. Globality near circle follows compactness of circular equilateral maximizers and uniform transverse Hessian.

## originality

PASS

The full published Resultary theorem “Exact perimeter selection among maximum-area polygons inscribed in ellipses” classifies rotations only within the maximum-area family, explicitly excluding all-inscribed perimeter maximization. It cannot imply a positive gap to the unrestricted maximum or the claimed ε² coefficient. Hoehner treats many-vertex asymptotic simultaneous intrinsic-volume optimization; a fixed three-vertex quantitative inequality is not a corollary. Classical ellipse billiards only gives first-order reflection stationarity. No matching all-eccentricity bound or local coefficient found; historical elliptic-integral priority remains possible.

## value

PASS

Quantifies a natural finite-budget incompatibility of planar intrinsic volumes (area and perimeter), with strict rigidity at precisely circular ellipses and sharp small-anisotropy loss. The result is useful without solving the difficult full perimeter-optimizer classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
