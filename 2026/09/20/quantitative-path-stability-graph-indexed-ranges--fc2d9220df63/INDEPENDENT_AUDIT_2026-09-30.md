# Independent Audit — 2026/09/20/quantitative-path-stability-graph-indexed-ranges--fc2d9220df63

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `5afa73ee0cb4bb083298f97e5fe020cc30df4e6b`
- Disposition: **PASSED**

## Correctness

**PASS** — The constants and reductions are consistent with the quantitative estimates used from Zhu's 2026 proof. Restricting the J_d integral to [d/(d+1),1] gives J_d>=1/(pi sqrt(2) sqrt(d+1)). For a branching vertex, the triangle rank surplus Delta>=1/4 combined with epsilon_{d,1/2}<J_d/(2d) yields at least J_d/12 for d>=3, with the d=2 margin handled exactly, hence more than 1/(60 sqrt n). For even cycles, direct conditioning of the lazy increment representation gives Delta_m=(3m-1)/(2(2m-1))-2^m/binom(2m,m)>=2/5; inserting this in the same comparison gives the asserted standard gap. For the fork tree, coupling the shared spine and the two terminal increments yields exactly one half of P(M_{n-3}=1), whose reflection-principle formula and Stirling asymptotic give the sharp n^{-1/2} order. In the lazy case the submitted arithmetic 2/7-37125/131072=2269/917504 is exact, yielding the 1/(2000 n^{3/2}) cyclic bound, while the event that three branch edges survive zero-edge contraction has probability 8/27 and transfers the standard bound to 2/(405 sqrt n) for nonpath trees.

## Originality

**PASS** — Zhu's September 2026 paper establishes the qualitative path extremum for all connected bipartite graphs and the lazy corollary, with the quantitative rank estimates needed by this extraction, but its public statement does not give the audited dimension-explicit stability gaps or the sharp fork scale. Wu-Xu-Zhu 2016 proves the two expectation conjectures for trees, and later special-class work treats unicyclic graphs and range distributions. The accessible 2016 full-text endpoint timed out during this audit, so the tree-specific priority comparison cannot be called exhaustive; however, even a hidden tree refinement would not cover the record's all-bipartite standard theorem or universal lazy cyclic bound. Targeted searches found no matching stability theorem.

## Scientific value

**PASS** — The result reveals a genuine separation scale behind a newly proved extremal theorem, proves n^{-1/2} to be the best possible standard order through an exact near-extremizer, and supplies explicit lazy-model separations. This is meaningful stability information beyond uniqueness, while the weaker n^{-3/2} lazy cyclic exponent is correctly not advertised as optimal.

## Sources

- **Paths maximize the expected range of graph-indexed random walks** — Yinfeng Zhu. https://arxiv.org/abs/2609.19728 — Primary 2026 qualitative extremal theorem; its abstract explicitly highlights the quantitative zero-edge-rank estimate and contraction mechanism used here.
- **Average Range of Lipschitz Functions on Trees** — Yaokun Wu; Zeying Xu; Yinfeng Zhu. https://zhuyinfeng.org/Data/Preprints/MJCNT16.pdf — 2016 tree case of the two expectation conjectures; open-access endpoint was found but timed out on full-document retrieval during this audit.
- **On the Distribution of Range for Tree-Indexed Random Walks** — Anna Berger; Chao Ji; Eyal Metz. https://arxiv.org/abs/1808.04261 — Prior distributional results for trees and spiders; distinct from the audited all-graph expectation stability constants.
- **Graph-indexed random walks on pseudotrees** — Jan Bok; Jaroslav Nesetril. https://doi.org/10.1016/j.endm.2018.06.045 — Prior unicyclic expectation theorem and cycle formulas.

## Limitations

- The constants are convenient rather than optimized.
- The universal lazy n^{-3/2} exponent is not shown sharp.
- The argument depends on quantitative comparison/rank lemmas from Zhu 2026 rather than reproving those lemmas.
- The 2016 tree paper's full document timed out during this audit; its abstract and bibliographic record were available, leaving residual tree-specific originality risk.
- The result concerns expected range, not full stochastic domination.

## Independent checks

```json
{
  "J_d_lower_bound_reconstructed": true,
  "cycle_rank_surplus_algebra_checked": true,
  "fork_coupling_and_reflection_formula_checked": true,
  "lazy_constant_fraction_checked": "2/7-37125/131072=2269/917504",
  "tree_contraction_probability_checked": "8/27",
  "zhu_2026_scope_checked": true,
  "wu_xu_zhu_open_access_attempted": true,
  "wu_xu_zhu_full_text_status": "timeout; abstract/indexed first page available",
  "open_access_first": true,
  "oxford_used": false,
  "decisive_inaccessible_comparison": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first. No decisive comparison remained inaccessible; where a nondecisive full-document retrieval timed out, that limitation is stated explicitly rather than treating the paper as read.
