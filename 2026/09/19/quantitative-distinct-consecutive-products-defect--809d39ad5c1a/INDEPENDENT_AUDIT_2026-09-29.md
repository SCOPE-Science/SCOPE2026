# Independent Audit — 2026/09/19/quantitative-distinct-consecutive-products-defect--809d39ad5c1a

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `2f4a2591b989bf797453108f059e2aa17a2d0f72`
- Disposition: **PASSED**

## Correctness

**PASS** — The quantitative re-optimization checks. Chojecki's witness-forest estimates are algebraic in the short-gap exponent theta: the raw short-root count is X^(1/2+6 theta+o(1)), a short child has at most Z^(3 theta+o(1)) children, unequal edges contract scale with rho=(2-theta)^(-1), and maximal equal strings contribute at most the stated theta-loss. Substituting these bounds gives the raw-root path exponent E_t whose rho^t coefficient (6 theta^2+3 theta-1)/(2(theta-1)) is positive on 1/24<theta<1/16, so the maximum is E_0=1/2+8 theta. The long-parent path coefficient is likewise positive and its t=1 value is strictly below E_0 in this interval. Runbo Li's almost-all short-interval theorem supplies O(Y log^{-B}Y) exceptional integers for intervals of length Y^(1/24+eta); every prime gap longer than p^theta contains, after discarding a negligible endpoint strip, a disjoint set of such exceptional integers of cardinality comparable with the gap length. Dyadic summation therefore gives the claimed long-gap contribution. Taking theta down to 1/24 yields every exponent above 5/6, and for fixed B the polynomial term is eventually dominated by X(log X)^(-B).

## Originality

**PASS** — Chojecki's source fixes theta=1/20 and records the corresponding 9/10 short-gap loss while its main conclusion is only density one. Li's later 1/24 almost-all prime-interval theorem supplies a stronger external input but does not apply it to distinct consecutive products. Targeted searches of the problem, the 5/6 exponent, the 9/10 source exponent and the new prime-interval result did not locate the optimized 5/6+epsilon short-loss or the all-fixed-log-powers global defect bound. The claim is therefore a quantitative refinement of a specific recent construction, not a new construction or a new prime-gap theorem.

## Scientific value

**PASS** — The result upgrades a qualitative density-one theorem for the canonical greedy set to an explicit complement bound that is smaller than X/(log X)^B for every fixed B, and improves the structured short-gap exponent from 9/10 to every exponent above 5/6. The parameterized calculation also makes clear how improvements in almost-all prime intervals propagate through the witness forest, so it has value beyond the single numerical exponent.

## Sources

- **Distinct Consecutive Products** — Przemek Chojecki. https://arxiv.org/abs/2609.17543 — Primary construction and witness-forest source; uses the fixed short-gap exponent 1/20 and obtains the 9/10 short-gap loss in the density-one proof.
- **Primes in almost all short intervals III** — Runbo Li. https://runbolicarey.com/assets/downloads/Primes_in_almost_all_short_intervals_III.pdf — Provides the 1/24+eta almost-all short-interval theorem with arbitrarily strong fixed logarithmic exceptional-set saving used for long gaps.
- **The dimension growth conjecture, polynomial in the degree and without logarithmic factors** — Wouter Castryck; Raf Cluckers; Philip Dittmann; Kien Huu Nguyen. https://doi.org/10.2140/ant.2020.14.2261 — Underlying integral-point estimate used in the source's split-product curve count.

## Limitations

- The theorem quantifies Chojecki's canonical greedy construction and does not optimize over all possible density-one sets with distinct consecutive products.
- The 5/6 threshold is not claimed optimal; it is the current output of the witness-forest loss combined with the 1/24 almost-all prime-interval exponent.
- The full complement has an all-fixed-log-powers bound but no unconditional global polynomial power saving because the long-gap input is only logarithmically exceptional.
- The proof inherits the source's uniform integral-point estimate and Li's recent prime-interval theorem; near-simultaneous work remains a residual originality risk.

## Independent checks

```json
{
  "source_witness_forest_full_text_checked": true,
  "li_pdf_theorem_checked": true,
  "pdf_screenshot_checked": true,
  "parameter_interval": "1/24 < theta < 1/16",
  "raw_path_coefficient_positive": true,
  "long_path_coefficient_positive": true,
  "max_short_exponent": "1/2+8 theta",
  "theta_limit_exponent": "5/6",
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive source remained inaccessible, so Oxford Download was not required.
