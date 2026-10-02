# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-ab11ed86de35`

## Correctness — PASS

For a stationary atomlessly marked renewal process, the mark of the next observation identifies its current block almost surely. The equilibrium age law therefore gives \(s_\zeta=\mathbb E[\min(L,\zeta+1)]/\mu\). For a complete block of length \(\ell\), direct rank-by-rank counting of the forward deletion window gives the deterministic reward \(\min(\ell,\zeta+1)\mathbf 1\{\ell\le	au+\zeta\}\); the renewal-reward theorem yields the exact fixed-window limit and hence the tail bias. For growing windows, the omitted tail reward has per-cycle second moment proportional to \(q_n=\Pr(L>	au_n+\zeta)\), so after centering its regenerative fluctuation is \(o_p(1)\) on the root-\(n\) scale as \(q_n	o0\); the deterministic center shift is exactly the stated multiple of \(\sqrt n\,q_n\). Finite second moment controls stationary boundary blocks, while \(	au_n=o(\sqrt n)\) controls the truncated final windows.

### Correctness sources

- assigned RESULT.md
- stationary renewal age law
- renewal-reward CLT
- full Chandra–Thangaraj ISIT 2024 paper

### Correctness risks

- Atomless marks are essential.
- The root-\(n\) theorem needs finite second block-length moment and the stated window-growth condition.

## Originality — PASS

The exact one-sided renewal-tail identity and its root-\(n\) threshold were not found in the current semantic search. The closest duplication-specific paper was inspected in full through authorized access: it studies missing mass under an elementary Bernoulli duplication channel, proves an \(O(1/n)\) minimax rate, and constructs a corrected estimator using singleton and adjacent-doubleton counts. It does not formulate the stationary atomless marked-renewal next-token target, the audited one-sided window reward, or the tail-probability phase transition.

### equivalent_formulations

Searches:
- Resultary: renewal-tail bias next-token surprise Good-Turing stationary marked renewal one-sided window root-n
- searches for the exact tail factor \(\Pr(L>	au+\zeta)\) in next-token/windowed Good–Turing contexts

Evidence:
- The audited theorem was the only exact published-finding match returned.

Reasoning:
Equivalent formulations through regenerative block rewards and through windowed count-surprise bias were considered.

### broader_coverage

Searches:
- Next-token functional estimation arXiv:2609.19529
- JMLR WingIt missing-mass paper
- Chandra–Thangaraj 2024 random duplications
- Chandra–Thangaraj–Rajaraman 2022 sticky channel

Evidence:
- These works supply general window estimators, minimax missing-mass theory, or duplication models, but the full 2024 duplication paper contains no theorem matching the audited stationary-renewal tail identity.

Reasoning:
General risk bounds and a different duplication channel do not imply the exact regenerative bias or the tail-based root-\(n\) phase.

### exact_database_or_table

Searches:
- current Resultary renewal/missing-mass records

Evidence:
- No exact database/table of the audited bias values was located.

Reasoning:
The theorem is distributional and asymptotic rather than a known finite table.

### claim_vs_prior_implication

Searches:
- implication comparison with duplication-channel minimax results and windowed estimators

Evidence:
- The prior full-text duplication paper estimates missing mass of an unknown discrete distribution from Bernoulli-duplicated iid inputs; the audited setting instead has atomless marks and fixed regenerative blocks and estimates a next-token count event.

Reasoning:
Neither model nor target specializes to the other in a way that mechanically yields the exact formula.

### source_inspections
- **Missing Mass under Random Duplications** — https://doi.org/10.1109/ISIT57864.2024.10619664. Trigger: Principal duplication-specific residual risk named by the package. Material read: Complete five-page primary paper obtained through authorized institutional access. Method: Full theorem, estimator, model and proof-scope comparison. Assessment: NOT COVERING: it treats elementary Bernoulli duplication missing mass and an \(O(1/n)\) minimax estimator, not the stationary renewal next-token window identity. Evidence: Its model duplicates each iid input at most once and its estimator combines singleton and adjacent-doubleton counts.
- **Next-token functional estimation** — https://arxiv.org/abs/2609.19529. Trigger: Primary source of the one-sided leave-a-window-out construction. Material read: Accessible abstract/scope material; full arXiv/OA text was not obtainable in this run and the authorized download route was unavailable. Method: Scope comparison without a whole-document novelty inference. Assessment: Motivates the estimator but leaves residual access risk for very recent details. Evidence: The accessible description concerns general next-token functionals and windowing under dependence.
- **Missing mass estimation from sticky channels** — https://arxiv.org/abs/2202.02772. Trigger: Closest geometric-repeat missing-mass predecessor. Material read: Accessible abstract/scope material. Method: Model-and-target comparison. Assessment: Different target and estimator theory; no exact audited one-sided renewal bias was located. Evidence: It studies minimax missing mass after geometric stickiness.

### checked_sources

- https://doi.org/10.1109/ISIT57864.2024.10619664
- https://arxiv.org/abs/2609.19529
- https://jmlr.org/papers/v25/24-0511.html
- https://arxiv.org/abs/2202.02772
- current Resultary renewal-tail search

### residual_risks

- The very recent next-token preprint could contain closely related regenerative examples not visible in accessible material; full text was unavailable through attempted routes.

## Scientific value — PASS

The result resolves a natural dependence model exactly rather than giving another generic mixing bound. It identifies the precise survival-tail quantity controlling finite-window bias and the exact root-\(n\) centering threshold, yielding interpretable logarithmic and polynomial window scales. Those formulas are directly useful for choosing and diagnosing one-sided window estimators.

### Value sources

- next-token window-estimation literature
- renewal-reward theory
- duplication/sticky missing-mass literature

### Value risks

- The theorem is model-specific and not minimax over a broad dependence class.

## Limitations

- Atomless block marks are required for the exact collision-free formulas.
- The root-\(n\) statement assumes finite second moment and \(	au_n=o(\sqrt n)\).
- Only the one-sided forward-window estimator is covered.
- Originality is best-of-knowledge for the recent next-token literature.

## Disposition

**PASSED**
