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

Read the complete pinned RESULT.md, verify.py, exact source tree and package metadata. Monomial orthogonality and independent gamma(|alpha_i|+1,1) radial powers give block beta(k+ell,m-k+d-ell) tail = Bin(m+d-1,tau) CDF at k+ell-1. Block weak compositions reproduce w_{m,k} and sum to dim H_m. Reconstructed uniform left-tail method-of-types sandwich exp[-NI]/(N+1)<=CDF<=exp[-NI] for j/N<=tau, CDF>=1/(N+1) otherwise; changing j/N to k/m costs O(log m) uniformly by endpoint entropy continuity. Uniform binomial polynomial multiplicity expansion and bounded-variation Riemann sum give m^d integral with claimed O(m^(d-1)log m), not a finite extrapolation. Independent exact beta/binomial checks 1,215 index cases and symbolic d=3,ell=2,tau=1/2 integral log2/6-5/48 agree. m=0 handled separately by exact eigenvalues; n,m growing only at fixed d,ell,tau.

## originality

PASS

Best-of-knowledge PASS for the particular fixed-degree two-block cap singular logdet law; prior monomial diagonalization and general Toeplitz spectral windows are credited, not claimed novel. Compared statements and mechanisms, not just titles; residual possibility of implicit general large-deviation coverage remains.

## value

PASS

The negative log determinant measures global concentration of a natural finite homogeneous Fock sector on a toric angular cap. Exact small-eigenvalue tails encode information not captured by regular Toeplitz trace laws; the explicit positive weighted relative-entropy rate and error are useful for angular concentration and gap probabilities, beyond routine diagonalization. A natural observable, not arbitrary special numeric gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
