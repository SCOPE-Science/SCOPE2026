---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Integrating the three frozen ODE components gives an exact nonsingular linear system for the finite-time averages \(X_T,Y_T,Z_T\), with only endpoint differences divided by \(T\) on the right. Boundedness makes those terms vanish, so convergence follows to the unique stated vector without ergodicity. The same three generator identities hold for every compactly supported invariant probability measure, and one-period integration gives the periodic-orbit case. Exact rational substitution independently reproduced both reported parameter specializations and the equilibrium squared magnitudes.

## originality

PASS

The 2024 Almatroud--Rajagopal--Pham--Grassi article is the exact-system primary source and analyzes equilibria, stability, bifurcation, Lyapunov spectra, basins and multistability. Its full public article record and same-system searches did not state coordinate time-average identities, invariant-measure second moments, or the consequence that the chaotic and period-three branches share the same RMS vector. Resultary surfaced analogous coboundary/moment laws for other flows, not this system.

## value

PASS

The three exact second moments are natural dynamical invariants of the published multistable system, not arbitrary statistics. They hold for every bounded forward trajectory and every compact stationary state and force nominally very different coexisting branches to have identical RMS amplitudes. That structural rigidity is useful for checking simulations and separating amplitude information from temporal/chaotic organization despite the short proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
