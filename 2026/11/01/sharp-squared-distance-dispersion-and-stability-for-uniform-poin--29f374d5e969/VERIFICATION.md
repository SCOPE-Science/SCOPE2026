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

Fix n=d+1 affinely independent vertices d≥2 and independent Dirichlet(1,…,1) barycentric samples. Reconstructed the four-point Dirichlet contraction yielding Q=(1+c)/2+(1+c)H/T²+3cW/T² where C is the centered vertex second-moment matrix, T=tr C, H=tr C², W=∑||w_i||⁴ and c=n(n+1)/((n+2)(n+3)). Inequalities H≥T²/d and W≥T²/n yield exactly the asserted nonnegative stability sum and regular-simplex rigidity from AAᵀ∝I with A1=0. The zero-sum scalar fourth-moment bound is k_n=(n²−3n+3)/(n(n−1)); its Lagrange multiplier cubic and three-coordinate perturbation reduce global maxima to the one-versus-rest two-level shape (n=3 identity handled separately). Coordinate Cauchy–Schwarz gives W≤k_nT², and rank(C)=d≥2 ensures H<T², yielding strict upper bound; axial collapse reaches it and interpolation covers every intermediate value. Inspected exact Dirichlet rational checker and the proof separately; its finite diagnostics do not establish the d-uniform assertions.

## originality

PASS

Primary Bäsel 2021 computes moments for *regular* planar polygons, including the equilateral triangle, not a universal optimization over all simplex shapes or d≥2. Wang 2026 develops Brunn–Minkowski properties of distance CDFs for general convex bodies and does not state the shape-normalized fourth-moment interval. The published Resultary beta gauge-distance theorem is for difference-body gauge, not Euclidean Q. A previously known zero-sum ℓ4 moment bound is used as an ingredient and is not claimed original. Unlocated older simplex distance shape inequalities remain a residual risk.

## value

PASS

Normalized fourth interpoint-distance moment Q equals one plus squared coefficient of variation of squared distance, a natural shape-dispersion statistic. The full sharp interval over *every* Euclidean simplex shape/dimension and sum-of-squares rigidity give a meaningful multidimensional optimization and stability result, beyond an isolated numeric regular-triangle value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
