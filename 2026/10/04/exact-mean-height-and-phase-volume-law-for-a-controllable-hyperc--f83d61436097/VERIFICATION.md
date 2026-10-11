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

Direct differentiation of R=m y^2+(z-c)^2 gives 2my x(z-c)+2(z-c)(-b-mxy)=-2b(z-c). Integrating proves the finite-time mean formula. On bounded forward trajectories R(T)/T tends to zero; compact support justifies integrating the generator against an invariant probability measure. The Jacobian trace is exactly -z, so Liouville gives the determinant identity and the standard determinant/Oseledets relation gives Lyapunov-sum -c whenever the spectrum is defined. The periodic-orbit statement is the finite-time identity with R(T)=R(0).

## originality

PASS

Originality passes. The complete introducing article prints the exact ODE and divergence -z, reports numerical spectra, and discusses geometric control numerically. It does not state the cohomological identity for R, an exact stationary z-mean, the finite-time determinant boundary term, or the exact Lyapunov-sum theorem. Fresh Resultary comparison found only the present same-object record and balance laws for different flows.

## value

PASS

The theorem upgrades the paper's geometric-control observations into an exact stationary constraint valid across every bounded recurrent regime and simultaneously gives an exact phase-volume and Lyapunov-sum diagnostic. That is a natural structural law tied to the controller parameter, not a cosmetic recalculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
