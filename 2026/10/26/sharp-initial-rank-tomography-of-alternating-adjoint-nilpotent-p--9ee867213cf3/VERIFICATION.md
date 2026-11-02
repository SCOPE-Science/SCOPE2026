---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Alternate left/right SVD singular-vector bases on path vertices simultaneously diagonalize each T and T* edge, proving N_m(T) unitarily equivalent to direct sum_i s_i J_m even with repeated and zero singular values. The Hermitian part of e^{i theta}J_m has sine eigenvalues cos(j pi/(m+1)) independent of theta; Li–Sze half-plane intersection gives all disks/empty at ordered values h_k. For K=(d-1)q+1, any i-th largest singular value times c1 appears among the first (i-1)q+1 products. Greedy peeling with multiplicities recovers all values; if the next radius is zero the remaining singulars vanish. Inputs diag(1,...,1,t) and diag(1,...,1,tprime) with 0<t<tprime<c_q/c1 have identical first (d-1)q ranges, proving optimality. I independently diagonalized real symmetric parts and recovered spectra for 36 parameter sets. This tests only bounded m,d; the SVD/Jacobi/peeling argument covers all.

## originality

PASS

Compared exact statements, not shared terminology. The disk portion follows from established Li–Sze theory plus direct-sum decomposition, but no examined statement gives the new optimal initial-prefix inverse recovery cutoff for arbitrary input singular spectra. A larger universal initial sample count does not imply the strictly shorter family-specific K=(d-1)floor(m/2)+1, nor show it is sharp. The claim is a parameter-uniform inverse theorem, not recovery of a finite lookup table. Failure to locate an index is only supporting context. Rank-one radius cannot recover all singular values when d>1. Known general disk and Kippenhahn results, even combined with the path split, require a new ordered-product peeling and lower bound to establish exact K.

## value

PASS

The known rank-one radius detects only ||T||. The theorem obtains all singular values from a provably minimal number of structured compression measurements, an exact information threshold for a natural alternating block operator. The matching indistinguishability construction is a substantive sharp lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
