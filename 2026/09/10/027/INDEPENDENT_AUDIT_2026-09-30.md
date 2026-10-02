# Independent scientific audit — SCOPE-20260910-027

Audited: 2026-09-30 UTC

Disposition: **repaired**

## Correctness

**PASS** — For the cited beta=1/4 envelope, fresh integration gives M(t)=R0^7/7 for t<=R0^-2 and M(t)=(R0^6/6)t^-1/2-(1/42)t^-7/2 for t>R0^-2. Thus M(t)t^alpha is uniformly bounded exactly for alpha<=1/2 in alpha in [0,4], yielding s>=7/2 and failure at s=3. The package overgeneralized the auxiliary beta formula: for general beta the Q-2beta rule has the stated form only for 0<beta<7/4; beta=7/4 has a logarithmic endpoint and beta>7/4 saturates at t^-7/2. The repaired RESULT qualifies this without changing the beta=1/4 theorem.

## Originality

**PASS** — The cited Raani-Singh paper supplies the high-frequency coefficient decay, while the inspected source states a positive-upper-density large-distance theorem rather than this compact-set envelope-closure threshold. No prior source located states the 7/2 obstruction for this bookkeeping.

## Value

**PASS** — The exact closure boundary is a motivated methodological cutoff: it diagnoses why a proposed Falconer threshold cannot follow from the available decay and quantifies the decay improvement needed. Such a sharp route obstruction is a meaningful structural result even without proving the positive theorem.

## Sources and residual risk

- https://arxiv.org/abs/2507.14917 — Primary abstract and indexed proof excerpt around the n=1 high-frequency estimate. Assessment: Supports the beta=1/4 decay input; does not state the 7/2 closure lemma.
- https://github.com/Resultary/2026/tree/main/2026/9/10/SCOPE027 — Published title and summary from semantic search. Assessment: Same finding.

Residual risks:
- Full source comparison was limited by the available indexed representation; an independently phrased route obstruction could exist.

The detailed machine-readable audit is in `INDEPENDENT_AUDIT_2026-09-30.json`.
