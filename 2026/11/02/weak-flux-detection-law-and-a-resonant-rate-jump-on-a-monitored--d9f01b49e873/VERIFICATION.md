---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The survival norm is ||K_alpha^n d||^2 for K the compression of U to the undetected sites. Fourier decomposition has a uniform mode of phase u and a two-dimensional sector with phases w exp(±i beta). The symmetric undetected vector has squared uniform-mode weight 2/3, while the antisymmetric vector is entirely in the latter sector. Projecting the rotation gives the diagonal entries (2u+w cos beta)/3 and w cos beta, and opposite off-diagonal entries ±w sin beta/sqrt(3). Off revival the dark eigenvalue is simple and the other squared modulus is (5+4 cos(3t))/9<1. The second-order dark-amplitude coefficient has real part −3t^2/2 + (3t^2/2) Re[1/(exp(3it)-1)] = −9t^2/4; squaring gives the required rate 9t^2/2. The dark spectral projector tends to the initial-state projector. At revival, after removing the common phase and dividing K−I by alpha, the leading matrix is the skew rotation with simple eigenvalues ±it and orthogonal eigenspaces. The average of the diagonal second-order terms in either eigenvector is −t^2. Squaring 1±it alpha−t^2 alpha^2 gives loss t^2 alpha^2 to leading order. Both channels have this decay, their initial norm weights sum to one, and the oscillating cross term vanishes because the projected directions become orthogonal. Bounded projectors and strict positive scaled losses give a uniform C exp(−c alpha^2 n) survival bound at each fixed positive t; this gives eventual detection and uniform integrability for every scaled integer moment, with limit m!/Lambda^m. This holds for either sign of alpha, requires sufficiently small nonzero alpha, and has no uniformity in t near a revival. A fresh full-Hamiltonian, finite-parameter calculation at /workspace/branches/9e580f8c-17c6-4c50-80ed-6c02e76f847a/full_hamiltonian_check.py corroborated spectral losses, survival at one point and scaled means at t=1 and 2pi/3; e.g. at alpha=0.005 the scaled means were 0.222240057147 and 0.227987937706. This is not a proof of all moments. Supporting verification files were read, not executed.

## originality

PASS

Wang et al. give exactly the same model, stroboscopic protocol and zero-phase dark state, and explicitly study phase coincidences and slow survival eigenvalues. Those are not claimed as new. The inspected strongest related formulas do not give the initially dark, fixed-t weak-flux limit with unit limiting survival weight, the two distinct exact coefficients, or the all-moment limit. The distinction between a simple long-lived mode and a two-mode revival at fixed t is substantive, not a change of normalization.

## value

PASS

The same three-site experiment has different sharp escape rates depending on whether the sampling interval lands exactly on a revival. Determining the factor 9/2 and the entire distribution with moment convergence distinguishes real long-lived dynamics from a small-probability return tail. The result is a checkable exact benchmark for monitoring protocols and for the nonuniform limits near revival; it does not claim the joint crossover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
