---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Over C and every m>=4, ∂e3/∂xi=e2−s xi+xi² and ∑∂e3=(m−2)e2, so J=(xi²−s xi) with s=∑xi. In B=C[s,xi]/(xi²−sxi) all squarefree monomials x_A form a free C[s] basis; quotient by L=∑xi−s gives M=S/J. Specialize s=1: B_d realizes degree<=d multilinear functions on {0,1}^m, and multiplication by L acts diagonally as |A|−1. Its kernel supports singleton subsets; expansion ∑c_i zi ∏_{j≠i}(1−z_j) shows K_d=0 for d<=m−2, standard (m−1)-dimensional for d=m−1, permutation V1 for d>=m. Exact graded sequence then gives M_d≅V_d for 0<=d<=m−1 and V1 beyond. On chart xi≠0, Boolean equations and characteristic zero imply precisely one reduced coordinate singular point, so saturated ideal I=(xi xj:i<j), quotient (S/I)_d≅V1 for d>=1. Subtracting V1 from V_d using Young’s rule produces precisely ∑_{j=2}^{min(d,m−d)} S^(m−j,j), multiplicity one for 2<=d<=m−2 and zero otherwise. Check dimensional identity binom(m,d)−m and length 2^m−m²+m−2; independently verified representation dimensions across m=4..15. These checks supplement the unrestricted symbolic argument.

## originality

PASS

Prior Dimca–Sticlaru results cover non-equivariant Jacobian Hilbert functions and the Cayley cubic m=4 numerical series; their compared passages do not state the complete uniform S_m-isotypic decomposition of I/J. The two-row Young decomposition supplies more than scalar dimensions, and each layer is shown multiplicity-free for all m; best-of-knowledge priority assessment, with risk of an unindexed equivariant formulation.

## value

PASS

The full degree-by-degree representation structure of a natural symmetric cubic Jacobian saturation defect is a structural invariant that controls characters and absence of trivial/standard components, not just a recomputation of known Hilbert numbers. Its uniform all-m classification is mathematically motivated by S_m-equivariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
