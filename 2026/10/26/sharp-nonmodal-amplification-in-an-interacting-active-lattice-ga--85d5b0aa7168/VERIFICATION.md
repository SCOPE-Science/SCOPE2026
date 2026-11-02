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

PASS: Linearizing the displayed hydrodynamic PDE gives the exact 2x2 Fourier matrix with off-diagonal entries -i Pe k(1-r), -i Pe k(1-2r). Its Hermitian part has maximal eigenvalue -k²-1+sqrt(1+(Pe k r/2)²), so semigroup contractivity in every nonzero Fourier mode is equivalent to Pe²r²<=4(k_1²+2); positive numerical abscissa at k_1 produces strict norm gain for an arbitrarily small real zero-mean perturbation. Direct squared-matrix computation gives spectral eigenvalues and the independent stability condition for r>1/2; difference of two Pe² thresholds is Q(3r-2)²/[r²(1-r)(2r-1)]. At r=2/3 Fourier matrices are Hermitian and the window collapses; for r<=1/2 spectrum remains left-half-plane for all finite Pe. At r=1/2 the triangular semigroup yields Pe C_L<=G_L(Pe)<=Pe C_L+1 with C_L the attained positive maximum of an explicit decaying Fourier-mode envelope. Independent symbolic Hermitian/spectral identities and finite-time singular-value witnesses passed (C5_OK).

## originality

PASS

PASS, qualified: Kourbane-Houssene et al already derive the exact hydrodynamic PDE and spinodal spectral criterion. Agranov et al use the same linearized Fourier propagator for steady-state fluctuation covariances. General numerical-range and pseudospectral semigroup theorems imply the contractivity test for an arbitrary given matrix, but the explicit density–activity phase diagram, density 2/3 exceptional Hermitian locus and all-Fourier-mode high-activity gain constant were not found in inspected primary materials. Earlier specialized transient-growth analysis remains possible.

## value

PASS

PASS: Nonnormal transient amplification despite spectral stability is physically meaningful for the exact interacting active exclusion hydrodynamics and is measured in an explicitly motivated species norm. Sharp coexistence window, exceptional density and unbounded large-activity gain separate modal from nonmodal mechanisms; not claimed as microscopic or nonlinear amplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
