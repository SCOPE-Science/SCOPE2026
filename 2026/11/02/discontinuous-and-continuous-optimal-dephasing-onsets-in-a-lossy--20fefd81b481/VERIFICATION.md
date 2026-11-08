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

For pulse initial state |1><1| and an absorbing sink at site 3, the Lindblad integrated density M=-L^{-1}(|1><1|) has finite trace: no invariant nondecaying positive state exists under kappa>0 by support elimination. Reconstructed 9x9 complex Liouvillian numerically independently and verified T(gamma)=3gamma/2+(kappa^2+6)/(2kappa)+delta^2*kappa*(6gamma+kappa)/(2P), P=2kappa gamma^2+(kappa^2+8)gamma+2kappa, including gamma=0. Symbolically checked T(gamma)-T(0)=gamma(6P-delta^2 kappa S)/(4P), S=kappa^2+2kappa gamma-4, and T'= [3P^2-delta^2 kappa^2 Q]/(2P^2), Q=12gamma^2+4kappa gamma+kappa^2-4. The G(gamma)=6P/(kappa S) derivative has upward quadratic K with constant kappa^4-32; hence interior coexisting gamma_c only when kappa<32^(1/4). R'=12kappa Q on Q>0 proves a unique positive local minimum wherever it beats zero. Four independently constructed Liouvillian inverses and exact symbolic factor identities passed. At equality high kappa the unique minimizer remains zero; no thermodynamic transition claim.

## originality

PASS

Best-of-knowledge qualified originality: the exact published model/theorem comparisons below do not establish an earlier dominating theorem for the narrow stated new remainder. Related prior methods and components explicitly credited; uninspected specialized literature risks remain.

## value

PASS

Sharp globally optimized mean first-capture time for a naturally minimal detuned chain exhibits a mathematically meaningful first-order-versus-continuous optimizer onset boundary, with a nonzero coexistence jump. Distinguishes the physical choice of local dephasing and pulse capture from the established steady-current/uniform dephasing setting, making a useful exact benchmark for environment-assisted transport.

The dated certificate retains the supplied scientific assessment, sources and limitations.
