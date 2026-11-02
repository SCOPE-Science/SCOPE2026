---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

On S³ the degree-l reproducing Gram equals (l+1)K_l, K_l(x,y)=U_l(<x,y>), and is PSD. At allowed nonantipodal angles the trigonometric formula gives U_{l+L}=U_l, U_{L-2}=-1 and U_{L-1}=0. Diagonal and antipodal endpoint values combine to K_{l+L}=K_l+L(I+(-1)^l P), K_{L-2}=L(I+P)-J, and K_{L-1}=L(I-P). The parity involution decomposition makes the K_{L-2} constant-vector eigenvalue 2L-N, hence N<=2L by PSD; other compatible eigenvalues equal 2L. K_{L-1} is 2L on the odd-parity sample space, so onto for degree L-1. For l=r+kL>=L, the positive 2kL parity-block shift plus PSD K_r gives full rank N/2. N=2L has the unique degree L-2 null vector, yielding sharp eventual threshold L-1. Binary dihedral Dic_n even n has 4n=2L points with exponent L=2n; the 600-cell binary icosahedral group has N=120,L=60. Independent Q8 exact-arithmetic Chebyshev matrix check confirms the degree-2 rank 3, degrees 3..23 rank 4 and 22 periodic recurrence checks.

## originality

PASS

The spherical harmonic addition theorem, binary polyhedral point sets and known 600-cell harmonic index are prior work. The statement under *angle-only* hypotheses for arbitrary finite antipodal X, its universal N<=2L bound, exact Gram recurrence and sharp all-higher-degree interpolation threshold are additional results in the reviewed evidence.

## value

PASS

This sharp, elementary kernel-spectral theorem resolves a natural exact interpolation threshold for antipodal quaternionic point designs. It gives a universal maximal sample count and infinitely many sharp realizations, not just a repackaged 600-cell table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
