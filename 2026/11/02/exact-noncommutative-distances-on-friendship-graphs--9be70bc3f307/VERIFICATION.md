---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On the hub with the one or two required petals, principal compression gives a lower bound for the commutator norm. Extension by the hub value achieves the same norm on F_m. In K3 the norm squared is a²+b²+(a-b)²; minimizing over the free coordinate for a fixed difference gives 3/2 times that difference squared. For a cross-petal pair, antisymmetrization by petal exchange preserves the oriented contrast and contracts the norm. For values (0,a,b,-a,-b), put δ=a-b and z=(a,b,-a,-b). The leaf block B is skew and satisfies B²=-δ²I. Schur complementation uses zᵀBz=0 and gives the polynomial λ(λ²+δ²)(λ²+δ²+‖z‖²), initially away from the block roots and hence identically, including degenerate cases. The squared norm is 8a²/3+3(b-a/3)²; contrast 2a gives the claimed optimum at b=a/3. The one- and two-petal witnesses extend sharply, and the vertex-pair orbits exhaust m≥2. Real functions suffice also under a complex convention since D is real and taking the real part after a phase rotation preserves the objective and contracts the norm. Independent spectral minimization and full-graph SVD witnesses agree for m=2–8; the all-m upper bound is analytic.

## originality

PASS

Credit earlier K3 distances and the pruning principle. The supported distinct contribution is the sharp butterfly cross-petal distance, giving a complete friendship-graph metric under that principle. None of the compared worked formulas covers this two-triangle interaction; the blade of the proof is the sharp five-vertex optimization, not the known reduction or a new general localization theorem.

## value

PASS

The two joined triangles are a canonical cyclic obstruction to replacing the adjacency-Dirac metric by a path metric. The sharp contrast across the cut vertex gives a quantitative example where concatenating exact local distances is not sharp and, with pruning, determines every orbit of a natural graph family. The exact value and attaining functions are useful benchmarks, even though the sharp new optimization is finite-dimensional.

The dated certificate retains the supplied scientific assessment, sources and limitations.
