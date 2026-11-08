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

The 2n-vertex cubic GP(n,2) shortest-path metric is defined for every n≥5. For a distinguished vertex, B_ij=d(x0,xi)+d(x0,xj)−d(xi,xj) satisfies c^T D c=−v^T B v for zero-sum c; B/2 is the squared-Euclidean Gram matrix. On the two-layer cyclic cover, exact displacement distances f_uu=min(|s|,2+ceil(|s|/2)), f_uv=1+ceil(|s|/2), f_vv=|s|/2 for even s and 2+ceil(|s|/2) for odd s, followed by minimization over windings, reconstruct finite distances. Independent BFS+exact symbolic characteristic polynomials verified all four factorizations for n=5,6,9,10 and ranks 5,7,9,10; all real nonzero roots are positive because their monic factors have strictly alternating signs and B is symmetric. Independent BFS checked the listed zero-sum witness quadratic values n=7..17 and for n=18,20,50. The universal c(v_i)=1,c(u_i)=−1 on i=0,2,5,7 has exact quadratic value 2 for all n≥18 by |s+mn|≥n−7≥11; all other n are finitely excluded by explicit witnesses. Schoenberg gives exp(−tD) PSD for all t exactly for the four, strictly PD since embedded points are distinct; excluded witnesses imply negative quadratic form for all sufficiently small t by Taylor expansion. No finite-n extrapolation proves the infinite exclusion.

## originality

PASS

No inspected general negative-type classification covers GP(n,2). Sánchez gives criterion only; Kutnar et al classify a different strong distance-balanced property, Gera–Stănică adjacency spectra, Kratica et al strong metric dimension, Shaheen et al distance polynomials, all insufficient to infer the signs of centered distance quadratic forms. Resultary search found no same-family CND classification. Exact 4-order result requires nontrivial infinite uniform obstruction and finite Gram spectra.

## value

PASS

A complete all-orders classification of when a standard cubic cyclic family carries a squared-Euclidean shortest-path metric is a natural negative-type and positive-kernel invariant. The isolated four orders, minimal embedding dimensions and one uniform eight-vertex obstruction illuminate structure unmeasured by adjacency spectra or distance enumerators; it is not arbitrary finite slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
