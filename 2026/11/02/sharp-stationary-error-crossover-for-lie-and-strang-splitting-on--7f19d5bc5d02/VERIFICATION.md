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

For rates (1,2,2) and row-stochastic E1(h)E2(h)E3(h) / E1(h/2)E2(h/2)E3(h)E2(h/2)E1(h/2), independently formed each exact stochastic matrix and solved its unique invariant row distribution. The resulting total variation deviations reduce to D_L=(1-q^2)(1+2q^2)/(2(1+q^2+2q^4)) and D_S=(1-q)^2(3q^2+2q+3)/(4(1+q^2)^2). Exact SymPy subtraction factors D_S-D_L=(q-1)P(q)/[4(1+q^2)^2(1+q^2+2q^4)], P=10q^7+2q^6+15q^5+3q^4+12q^3+4q^2+3q-1. P strictly increases on (0,1), P(0)=-1,P(1)>0, so q*=0.22049649 gives unique reversal h*=3.02374697; independent small-h expansions give 3h/8 and h²/8, large-h limits 1/2 and 3/4. For general a,b,c>0 the exact Lie stationary weights and symmetric perturbative O(h²) versus linear Lie error, plus saturated deterministic limits at a<b, prove existence not uniqueness. All-step proof is algebraic, not finite sampling.

## originality

PASS

Exact full-stepsize invariant-TV ranking crossover for uncorrected three edge exponentials is distinguishable from known operator-splitting steady-state bias and balanced corrections, positivity preservation or path-space relative entropy analysis. Qualified because the 2013 balanced-splitting PDF could not be read in full and general Markov-kernel splitting analysis might include this three-state specialization.

## value

PASS

A minimal genuine Markov chain gives a nontrivial finite step-size threshold where higher-order positivity-preserving splitting ceases to be the better stationary approximant, despite unconditional mass preservation and convergence. The threshold and exact stationary laws provide a meaningful benchmark for long-time integrator choice, not a claim about trajectory-error dominance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
