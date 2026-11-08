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

Every face of Δ_{n,k} fixes disjoint I,J coordinates at 1,0; positive-dimensional free remainder has m=n−a−b, 0<r=k−a<m. The stabilizer S_I×S_J×S_M preserves both the face and excluded-vertex hull, so averaging closest pairs reduces to the symmetric face point and outsider characterized by total fixed-one loss s and fixed-zero gain v. Every outsider vertex violates at least one fixed coordinate, hence s+v>=1. Squared distance is s²/a+v²/b+(s−v)²/m, with empty-group terms omitted. Strict convexity and homogeneity reduce minimization to s+v=1; its minimizer s=a(m+2b)/[m(a+b)+4ab], v=b(m+2a)/[...] yields n/[m(a+b)+4ab]. Both (1,0) and (0,1) rays are attained by actual one-swap outside vertices whenever relevant, making the relaxation exact. Vertex face case separately gives n/[k(n−k)]. For n>=3 maximize D(a,b)=n(a+b)−(a−b)² over nonvertex faces: increasing in a gives a=q−1, then integer concavity in b gives breakpoint n=4q−1 and D pieces exactly as claimed. Vertex bound never lower; n=3 ties, n=2 is segment sqrt2. Independently checked 2,275 exact rational face-type quadratics/optimizer cases through n=15 and n=2 boundary, with code reproduction not extrapolated to arbitrary n.

## originality

PASS

Best-of-knowledge PASS for exact facewise uniform-matroid base-polytope distances and sharp n/q optimizer transition. The full Peña–Wirth primary manuscript was read via lawful public OA (Optimization Online), including simplex-like bound §6.7; it does not state a hypersimplex exact formula. Deza et al. abstract discusses global ratio and Birkhoff exact values, not a hypersimplex expression, but inaccessible full text leaves a specific unclosed priority risk.

## value

PASS

PASS: pyramidal width is a natural Frank–Wolfe geometric condition measure, and hypersimplices are uniform-matroid base polytopes; exact facewise separation, integer minimizing face classification and sharp quarter-density transition answer a nontrivial natural invariant question. No new algorithm-rate theorem is required for the exact geometric value to be substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
