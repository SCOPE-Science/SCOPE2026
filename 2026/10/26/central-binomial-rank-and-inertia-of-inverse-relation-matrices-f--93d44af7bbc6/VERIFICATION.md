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

The general proof establishes the interval-partition/image-set encoding of the monoid, the reciprocal-transversal characterization of semigroup inverses, the exact operator identity \(X\mapsto M X^{\mathsf T}M\), full row rank of \(M\) by polynomial induction, and inertia through singular-value decomposition. These are infinite-parameter arguments for every integer \(n\ge1\).

Run `python3 verify.py` in the same directory. The included standard-library script enumerates all monotone maps for \(1\le n\le5\), tests every ordered pair for mutual-inverse identities, checks the transversal factorization and the incidence matrix rank exactly, and ends with `VERIFY_OK`. It additionally checks known inverse-degree and idempotent counts, which are not claimed as original here. Run `python3 verify_eigensigns.py` with NumPy installed to reproduce numerical eigenvalue-sign checks on all blocks through \(n=5\); it prints `SPECTRAL_VERIFY_OK`. These finite checks are not an all-parameter certificate.

The material inspected from the directly relevant October 2026 preprint was limited to its public abstract and bibliographic data. No independent audit has been conducted.
