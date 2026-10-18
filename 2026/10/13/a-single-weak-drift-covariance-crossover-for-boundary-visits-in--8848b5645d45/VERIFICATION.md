---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: Exact transient Green matrix identity Cov_i(T,N_1)=G_i1(t_1-t_i)+(G²)_i1-G_i1 follows by ordering the two occupation-time indices. The biased walk potential kernel and mean duration satisfy the discrete boundary-value equation. Fixed-i weak-drift expansions and bounded Riemann sums lead to the displayed F_i(b); an independent sympy b→0 limit equals 2-2i/3. The numerator H_i has H_i''=exp(-b)[4(1-exp(-b))-(i+1)b], proving all sign regimes, with a unique positive crossing only at i=2 (b*=1.49888421886734). Finite m covariance need not share the limit's sign uniformly.

## originality

PASS

PASS best of knowledge: classical gambler's-ruin Green kernels and durations are credited, and de Vos–Vervaat 1988 treats joint local-time generating functions. Those may encode the finite mixed moments, so the identity is not asserted novel. The full fixed-start weak-drift covariance scaling and unique start-site-specific sign diagram were not located in inspected material. de Vos–Vervaat full 1987 manuscript inaccessible, retained as serious priority risk.

## value

PASS

PASS: The exact sign reversal of absorption-time/local-time covariance under weak right drift is a natural stochastic process dependence question. The sharp location of a single critical drift and the exceptional starting position i=2 materially refine known marginal Green and moment formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
