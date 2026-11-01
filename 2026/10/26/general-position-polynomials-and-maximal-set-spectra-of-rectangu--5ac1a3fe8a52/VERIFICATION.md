---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Two distinct cells of a rook graph with different row and column have exactly two length-two geodesics, through the opposite corners of their 2×2 rectangle. Three selected cells are collinear on a geodesic iff the corresponding three bipartite incidence edges form a P4. A bipartite P4-free graph has every nonisolated component a star, proving a biconditional for every p,q≥2. Exponential-label component counting gives Ψ=p!q![x^py^q]exp(x e^{zy}+y e^{zx}−xyz); the subtraction removes double counting the single-edge component. Maximality forces either all row and column vertices covered, or isolates on only one shore with all nontrivial stars centered on the opposite shore with degree at least two and every opposite vertex covered; summing these mutually exclusive component families gives the claimed maximal enumerator. A spanning forest with k≥2 components has p+q−k edges; one-shore-isolated types yield exactly sizes p or q. Thus the support is precisely {p,q}∪{p+q−k:2≤k≤min(p,q)}. For p=2, Ψ=(1+2z)^q+qz² and maximal counts q at size2, 2^q at size q (combine if q=2). Independently checking every subset on 2x2, 2x5, 3x4, 3x5 and 4x4 boards matched all formulas, while the unbounded quantifier proof uses the structural star-forest decomposition.

## originality

PASS

Best-knowledge scientific comparison: For p,q≥2, every general-position set of K_p □ K_q is exactly the edge set of a bipartite star forest in K_{p,q}; this yields a complete bivariate exponential generating formula for its all-size polynomial, a three-case classification of all inclusion-maximal sets, their enumerator and exact maximal-cardinality spectrum {p,q}∪{p+q−k:2≤k≤min(p,q)}. The entire general-position polynomial and all inclusion-maximal cardinalities on the natural two-factor Hamming/rook graph family are motivated by the establis

## value

PASS

The entire general-position polynomial and all inclusion-maximal cardinalities on the natural two-factor Hamming/rook graph family are motivated by the established graph-polynomial research programme. Beyond previously known minimum and maximum cardinalities, the result specifies the actual extremizers and finds unbounded internal gaps in maximal spectra on K_2 □ K_q; the enumerator is useful and nontrivial, not a mere known-table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
