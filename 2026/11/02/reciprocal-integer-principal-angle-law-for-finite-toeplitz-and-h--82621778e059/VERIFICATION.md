---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The normalized diagonal D_d and anti-diagonal E_s bases are orthonormal for Frobenius norm, and their cross inner product is a single normalized cell if parity and index bounds match. Two parity blocks embed isometrically as kernel step functions on meshes 2/n; boundary squared Hilbert–Schmidt mass is uniformly O(delta), while bounded interior kernels converge by dominated convergence, yielding both blocks to the same Hilbert–Schmidt limit. Reflecting x→±u and y→t,2−t turns its nonzero action into Kf(u)=(1−u)^−1/2 ∫_u^1 f(t)/sqrt(t)dt. For F_k(t)=t 2F1(1−k,k+1;2;t), f_k=sqrt(1−t)F_k′, one has ((1−t)F_k′)′=−k²F_k/t; K*K identities imply KK* f_k=k^−2 f_k. The polynomial eigenfunctions span a dense subspace, so positive singular values of K are precisely 1/k; both parity blocks give every 1/k twice, converging in ℓ² and HS norm squared π²/3. For n>=3, checkerboard/constant matrices span the 2-dimensional intersection and give exactly two unit singular values; hence after orthogonally removing both common components the sharp squared-norm constant is 1−s3(G_n)→1/2. Independent finite matrix checks corroborate the first singular values and HS convergence; they do not establish the continuum limit.

## originality

PASS

Babbar–Majee–Maji arXiv:2610.35897 treats algebraic truncated Toeplitz+Hankel operators, intersection and ambiguity in Theorems 5.5/6.1, without computing the Frobenius cross-Gram spectrum. Bhuia–Majee arXiv:2606.09370 likewise discusses algebraic model spaces and checkerboard ambiguity. General principal-angle and projection-product theory identifies singular values of a cross Gram with cosines but does not assert the reciprocal-integer law for these two concrete growing subspaces. The limiting Volterra spectrum may be separately known (classical) and is not asserted new in isolation; the two-copy Toeplitz/Hankel limit and stability constant are assessed original best knowledge.

## value

PASS

Toeplitz+Hankel representation ambiguities are a natural structured-linear-algebra problem. Beyond identifying the two-dimensional overlap, this theorem gives the entire asymptotic principal-angle spectrum in ℓ² and the sharp limiting conditioning constant 1/2 for stable decompositions. The nontrivial weighted Volterra reduction is exact enough to support further approximation and numerical stability analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
