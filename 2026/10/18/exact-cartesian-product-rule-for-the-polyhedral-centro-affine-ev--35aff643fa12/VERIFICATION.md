---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

For each facet a from factor i, direct orthogonal product geometry gives m_(ia)(P)=m_a(P_i)V/V_i. Same-factor ridge conductance scales by V/V_i; distinct-factor ridge conductance is m_a(P_i)m_b(P_j)V/(V_i V_j) because normals are perpendicular. Divergence theorem gives Σ_a m_a(P_i)=d_iV_i, hence (L_P f)_(ia)=(L_i f_i)_a+Σ_(j≠i)d_j(f_(ia)−bar(f_j)). The mass-orthogonal even facet space decomposes into centered even factor modes with eigenvalues shifted n-d_i and a k-dimensional block-constant space with eigenvalues zero and n of multiplicity k-1. This covers all eigenvalues and multiplicities even for segment factors. Cross-polytope facets give a Boolean cube network with c/m=(d-1)/2, eigenvalues r(d-1), even Walsh r; the segment×C_d prism has single first eigenvalue d+1 for d≥3 and dimension-four example {0,4,5,5,5}. An independent symbolic product-network derivation and comparison with fully inspected cross-polytope/parallelotope original proofs corroborate. The finite supplied verify.py checks only selected products, not all dimensions.

## originality

PASS

The general dimension-uniform product decomposition and non-parallelotope equality examples are not implicit in earlier published standalone factor spectra without the new mixed-ridge geometric identity. The fully read Resultary related RESULT.md works cover separate factor calculations; the initiating primary Hu–Ivaki full text could not be accessed here, and older weighted-join formulations remain a priority risk.

## value

PASS

This structural spectral product rule reduces entire even spectra and dimension-level gap questions for arbitrary decomposable symmetric polytopes to constituent spectra; non-parallelotope prisms attain the baseline. It is mathematically useful beyond a small parameter census and does not require indecomposable gap conjecture resolution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
