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

The relaxation quadratic factors into the zero root and one positive root because the active modes have nonzero increments. Each step is multiplication on mode j by the complex scalar 1-gamma t_j/2+i gamma sqrt(t_j), so the squared multiplier is strictly positive and the initial active set persists. Substitution gives (1), and subtracting the two multipliers factors as (t_*-t_j)(t_*+t_j-Q)/[4(1+Q/4)^2]. For t_j<t_* it has a positive lower bound on the compact admissible Q-interval, giving a uniform lower/top ratio contraction at each fixed h>0. Equal top frequencies retain their initial ratios. Conservation yields (2) and exponential convergence of Q to t_*, so the multiplicative deviations from the positive limiting factor rho_j are summable; their positive convergent product gives (3). The recurrence divided by h^4 is the smooth simplex field in (4) times 1+O(h^2), uniformly on the simplex, and the summed local defect and discrete Gronwall give (5) on bounded slow times. The physical clock uses the actual gamma increments. For distinct initially active frequencies, the top share is strictly increasing in the limit field while the recurrence changes by at most O(n h^4) before that scale; if the active frequencies are all equal, there is no transfer. Separating the two-mode equation gives (6). Independent bounded replay (python -B /workspace/checks/bounded.py) checked the quoted share to 50-digit working precision, and direct complex midpoint increments with two tied top modes and a faster inactive mode at two base steps. These checks are not proofs of the asymptotics.

## originality

PASS

The supported distinct claim is the all-positive-step explicit-midpoint selection of the largest initially active frequency, with geometric rates and its sharp, bounded-rescaled-horizon limit. Neither the algebraic framework nor the qualitative observation of numerical coupling under one shared relaxation scalar is novel.

## value

PASS

The premise that exact conservation of total energy protects each uncoupled oscillator is refuted in a natural textbook method/model pairing. The incorrect attracting distribution, sharp per-mode decay, and physical horizon for order-one transfer quantify a structural limitation of using one constraint in a problem with many true invariants; this is not merely an observed drift in a sample simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
