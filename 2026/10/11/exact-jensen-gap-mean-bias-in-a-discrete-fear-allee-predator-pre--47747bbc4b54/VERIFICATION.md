---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

On compact invariant support in the positive quadrant, log P and log N are bounded and the two multiplicative factors are positive. Invariance gives zero integrals of log(P_next/P) and log(N_next/N). Strict log Jensen gives exp(J_P)=1+h(E N-m), and exp(J_N)=1+(h/epsilon)(E[g(N)/(1+fP)]-E P). Equality in J_P forces N=m almost surely; invariance and prey update force P=P_* uniquely, so every nontrivial invariant measure has E N>m and positive mass N<m,N>m. Completing g square gives E P< (1-theta)²/4. Computation of 0.2025 and 0.038025 is exact decimal arithmetic. No existence of chaotic measures or invariant curves proved.

## originality

PASS

Best-of-knowledge novelty after object/parameter/implication comparisons with primary literature and published Resultary findings; specific plausible residual coverage risks stated; inaccessible literature alone does not force scientific rejection.

## value

PASS

The all-amplitude compact-recurrence theorem complements a concrete two-parameter Hopf/chaos predator–prey model with a rigorous model-specific statistical obstruction: every non-equilibrium interior invariant state has shifted mean prey, necessarily crosses its equilibrium level and has a universal predator ceiling. Its proof uses standard Jensen/coboundary tools, but the precise cross-regime mean constraints and rigidity for this ecological map are useful even without proving existence or stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
