---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification record

The proof was checked symbolically from the normalized partial-sum definition of the dual-Hahn norm, including the inverse coordinate map, the exact weighted-shift iterate, the compactness of the shift defect, and the convergence of the absolutely summable series in operator norm.

The sharp lower-bound witness uses disjoint coordinate blocks of fixed coefficient cutoff; for each chosen cutoff the total ignored coefficient tail is bounded by its \(\ell_1\) norm independently of the number and sizes of the blocks. The resulting closed block space is isometric to \(\ell_\infty\), so it simultaneously witnesses every finite Bernstein number and the strictly singular distance. The approximation and Gelfand equalities follow by rank-nullity and dimension intersection, not by numerical enumeration.

The Fredholm calculation uses an explicit rank-one perturbation factorization of the one-sided shift for interior points and analytic Wiener algebra factorization. On the unit circle, infinitely many disjoint finite tent vectors are unit-norm, weakly null and approximate eigenvectors; a compact parametrix would force them to converge to zero in norm, a contradiction. Boundary and zero-symbol cases have been checked.

A finite-support phase-alignment sanity check for coefficients \(1,-1/2,i/5\) at output index \(1000\) gives \(1.6991008991008991\) against the coefficient sum \(1.7\). This is not used as an infinite-dimensional proof.

The exact operator norm and ordinary spectrum are credited as prior results. Full-text access to a related weighted-Hahn paper remained incomplete and is an explicit originality risk. Independent auditing was not performed.
