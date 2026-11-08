---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Actual RESULT.md uses the unique contractive periodic disease-free state of dot S=mu(1-S) with instantaneous strengths p,q,r in (0,1). For two pulses, deficit J satisfies J_A=p+(1-p)E J_B/x and J_B=q+(1-q)xJ_A, giving mean bar S=1-[(p+q)(1-E)+2Epq-pq(x+E/x)]/(mu T D). The positive curvature x+E/x is uniquely minimized at x=sqrt E, hence tau=T/2 for all unequal strengths. Peak equals 1-min{A(x),B(x)}, with A increasing and B decreasing and exactly one intersection x*=[E(p-q)+sqrt(E²(p-q)²+4pqE)]/(2p). Half spacing coincides with minimax iff p=q. For three pulses, cyclic J recurrences and constraint xyz=E yield constrained gradient components p(q-r)(u-1)/D3 and r(q-p)(u-1)/D3 at x=y=z=u, which vanish jointly iff p=q=r; hence unequal strengths make equal spacing nonstationary, NOT a global three-pulse minimizer classification. Independently recalculated both symbolic gradients with SymPy and exact witness F_equal=257/253 versus F_unequal=2573/2530 (positive difference 3/2530). The scalar infected Floquet multiplier exp[T(beta bar S-delta)] is monotone in mean S only under constant beta,delta.

## originality

PASS

The exact two-pulse equal-gap rigidity under unequal per-campaign fractions and explicit divergence from minimax timing, together with the three-pulse first-variation boundary, differ in control constraints from regional pulse-synchronization and dose-budget/effort optimal-control work. Prior SIR pulse dynamics and affine recurrence are not new. Literature may contain stronger impulse-interval optimization theorems; the best-of-knowledge positive assessment retains that risk.

## value

PASS

Scheduling pulses to reduce cumulative invasion potential versus worst instantaneous susceptibility is a natural epidemiological optimization tradeoff. The theorem establishes a sharp two-to-three intervention change: two heterogeneous campaigns optimally split mean-risk time equally, while three heterogeneous campaigns cannot be stationary at equal gaps. These exact phase and constraint boundaries can guide model comparison even without nonlinear epidemic predictions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
