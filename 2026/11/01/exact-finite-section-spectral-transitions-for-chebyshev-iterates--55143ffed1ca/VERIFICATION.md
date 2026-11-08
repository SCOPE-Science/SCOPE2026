---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Chebyshev conjugacy sends F_d^n to T_m with m=d^n and invariant arcsine angular measure. Orthogonality plus the product identity yields exactly the symmetric sparse C=I-2B matrix: for positive indices one half for |i-j|=m or i+j=m; the 0-to-m entry is 1/sqrt(2). Its nonzero graph decomposes into a degree-zero path, reflected residue-class paths, and possibly the even central self-loop path. Standard Chebyshev characteristic recurrences give all-K cosine root multisets and hence the complete B spectrum. For K<=m only two-vertex reflected pairs and possibly a 1/2 central self-loop survive; K<=ceil(m/2) is scalar, ceil(m/2)<K<=m has norm gap 1/4, and K=m+1 has gap 1/(2sqrt2). Each finite path angular-grid discrepancy <=1/L and there are <=floor(m/2)+1 paths, establishing the stated empirical arcsine bound and limit regimes. Independently constructed matrices for 450 (m,K) configurations agreed with all predicted eigenvalues within 1.8e-15. Finite checks confirm, not prove, unbounded n and K.

## originality

PASS

Toeplitz-plus-Hankel Chebyshev Gram entries are established and exactly credited; the source focuses on Cholesky/fast matrix transforms rather than exact iterated-dynamics finite-section eigenvalues. Janowicz--Orlowski analyze fixed-degree entries of logistic multiplication on Lebesgue with shifted Legendre basis, not the arcsine Chebyshev variable-K spectrum. The rank-dependent thresholds, residue-block all-K diagonalization and noncommuting m,K limits are distinct from these prior statements, though unknown special Toeplitz/Hankel explicit diagonalizations remain a priority risk.

## value

PASS

A natural finite-resolution observation question for a chaotic interval map has a sharply delayed visibility threshold despite full operator norm remaining 1/2; the complete spectral classification and explicit joint dimension/frequency transition quantify an operator-compression phenomenon rather than a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
