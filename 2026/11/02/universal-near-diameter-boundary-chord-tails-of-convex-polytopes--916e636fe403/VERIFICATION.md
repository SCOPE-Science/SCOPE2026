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

Every diametral pair of a compact convex polytope comprises vertices, since Euclidean squared norm is strictly convex separately in endpoints. For a fixed ordered diametral (v,w), e=(w-v)/L has positive pairing with every nonzero inward tangent direction at v; the diameter inequality yields strict positivity. Boundary facets near v are exact k=d-1 homogeneous cones, so the normalized axial deficit cap is exactly B(v,w)*t^k for small t. Two independent axial deficits convolve via a beta integral to (k!)^2/(2k)! B(v,w)B(w,v)*t^(2k). Euclidean chord deficit differs by O((norm h+norm j)^2), and strict axial positivity forces both of order epsilon, leading to O(epsilon^(2k+1)) correction. Finiteness of diametral ordered vertices permits summation and positive universal exponent 2d-2. Facet simplex cone computation yields for regular simplex d(d+1)4^(d-2)((d-1)!)²/(2d-2)! and cube 2^(d-2)d^(d-1)/(2d-2)!, with d3 constants 8 and 3/4. Independently evaluated exact factorial constants d=3,4,5 and source verify.py, which contains exact cone diagnostics and Monte Carlo importance tests. The all-polytope theorem rests on geometric cone proof, not simulations.

## originality

PASS

Best-of-knowledge comparison against stronger and equivalent claims, not titles alone; primary texts and known antecedents acknowledged. A general maximal interpoint distance theorem cannot produce a specific facet coefficient from its own assumption; new local cone calculation and beta convolution are needed. Unresolved historical-priority possibilities are explicitly retained; unsuccessful searches are not proof of novelty.

## value

PASS

Near-diameter distance tails of independently surface-sampled points are natural inputs to random-sample diameter extreme-value theory, while arbitrary polytopes exhibit anisotropic vertex cones. Universal exponent and explicit ordered-diametral facet coefficient constitute an exact geometric classification usable for simplex/cube benchmarks; distinct from random line chord and interior sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
