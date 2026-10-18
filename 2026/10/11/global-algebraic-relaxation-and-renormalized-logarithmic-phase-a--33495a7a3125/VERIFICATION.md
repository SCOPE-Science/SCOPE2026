---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Recomputed the nonproper but positive Lyapunov function H_mu and verified dH/dt=-exp(-2 mu y)x^4 by independent SymPy differentiation. To obtain global boundedness, the proof separately uses finite one-sided excursion integrals (cubic drift) to bound y and then inward x drift; invoking Lyapunov properness alone would be false. LaSalle forces convergence to zero. Independently integrated the polar perturbation jets, obtaining return-radius coefficient -3pi/4 and physical period coefficient pi*mu^2/3. Reciprocal squared section radii grow (3pi/2)n+O(sqrt n), so the O(n^-3/2) errors are summable and summing the physical period yields the exact log phase (2mu^2/9), not just a leading-order frequency. Within-turn differences vanish because rho_n tends to zero. mu=0 follows by smooth specialization and its Euclidean energy.

## originality

PASS

Prior qualitative global portraits and no-cycle results for the same cubic Liénard family do not establish the combined physical-time amplitude and finite renormalized-phase theorem. Earlier local focus and period constants are explicitly credited; originality concerns their rigorous global orbit-to-origin application, summable error control and full-time limit for arbitrary initial data.

## value

PASS

The critical zero-linear-damping weak focus is a canonical degenerate oscillator; precise algebraic relaxation and finite logarithmically renormalized phase provide sharp dynamical invariants directly in physical time. The global-uniform orbit statement is not a trivial local normal-form coefficient or a renamed no-cycle corollary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
