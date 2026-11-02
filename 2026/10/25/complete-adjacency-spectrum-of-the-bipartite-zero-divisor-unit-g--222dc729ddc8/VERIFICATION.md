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

The graph has unit-side size M=prod m_i and zero-divisor-side N=prod(m_i+1)-M-1. For support J of z, B_{z,u}=1-prod_{i in J}(1-1_{u_i=-z_i}). Multiplication by the unit group on both sides preserves adjacency, so Gram B^T B has character eigenvectors. Fourier cancellation makes C_z(chi)=0 unless support T subset J; for proper nonempty T the squared row sum yields lambda_T=prod_{i notin T}(m_i^2-m_i+1)-prod_{i notin T}(m_i-1)^2; for T empty the row-degree squared sum yields the stated lambda_empty. Every proper-support eigenvalue is positive (row J=T), and full support is zero with multiplicity F=prod(m_i-1). Hence rank B=M-F and adjacency eigenvalues pair ±sqrt(lambda) with remaining nullity N-M+2F. Independent exact integer Gram matrices checked eight field-product support-size tuples including F_2 factors and repeated supports; these do not replace the general Fourier derivation.

## originality

PASS

The motivating 2025 full primary preprint defines this exact additive graph and explicitly asks its adjacency spectrum in Section 8; the inspected paper does not present this character-support spectral factorization. Classical multiplicative zero-divisor spectra address a different graph and do not imply it directly. Fourier and singular-value methods are standard, not claimed new.

## value

PASS

An open spectral problem for a natural additive graph on finite reduced rings is answered for all unequal field factors with the complete eigenvalue multiplicities and rank/nullity, a natural full graph invariant and tool for further spectral questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
