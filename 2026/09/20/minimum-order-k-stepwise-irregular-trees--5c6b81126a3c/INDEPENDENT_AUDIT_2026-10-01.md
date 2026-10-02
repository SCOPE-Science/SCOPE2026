# Independent scientific audit — 2026-10-01

Record: `SCOPE-20260920-5c6b81126a3c`

Disposition: **passed**

The claim in `RESULT.md` is accepted unchanged. This audit assesses one final claim and requires separate correctness, originality, and scientific-value passes.

## Correctness — PASS

Because a nontrivial tree has a leaf and every edge changes degree by exactly \(k\), all degrees are congruent to \(1\pmod{k}\), so \(\Delta=1+hk\). Root at a maximum-degree vertex and let a class-\(i\) branch start at a nonroot vertex of degree \(1+ik\). Such a vertex has exactly \(ik\) children, each in class \(i-1\) or \(i+1\). Strong induction on branch order is legitimate even for an upward child because its descendant branch is proper; strict monotonicity of \(F_i\) then gives the sharp recurrence \(F_i=1+ikF_{i-1}\). The root has \(1+hk\) class-\(h-1\) branches, proving the lower bound. Equality excludes every upward child and recursively forces a unique layered tree; two root branches realize diameter \(2h\). For the three-degree consequence, deleting leaves leaves a bipartite tree in which every class-2 vertex keeps all \(2k+1\) incident core edges; the tree identity gives \(|A|=2k|B|+1\) and then the leaf and order formulas. The explicit core construction realizes every positive \(|B|\). No finite enumeration is needed.

The package computations, where present, were treated as supporting checks rather than substitutes for the general proof.

## Originality — PASS

### Equivalent formulations

**Searches/source IDs**
- Published SCOPE archive query: k-stepwise irregular tree minimum order prescribed maximum degree
- Published SCOPE archive query: 2-stepwise irregular trees minimum order maximum degree
- arXiv:2411.15765

**Evidence**
- The published SCOPE search returned the audited theorem as the only direct general-\(k\) minimum-order tree match.
- The full Alizadeh--Klavžar--Langari preprint states a sharp upper bound on maximum degree at fixed order for general \(k\)-SI graphs, not the recursive tree minimum-order theorem.

**Reasoning**

The general-graph bound \(\Delta\le\lfloor(n+k)/2\rfloor\) is much weaker on trees and does not imply the factorial-type tree minimum or uniqueness.

### Broader coverage

**Searches/source IDs**
- arXiv:2411.15765 full text
- DOI:10.24200/sci.2022.57725.5388
- DOI:10.1016/j.dam.2026.06.027

**Evidence**
- The accessible general-\(k\) full text covers bipartiteness, diameter existence, maximum-degree bounds, size bounds, and degree complexity.
- The 2023 and 2026 abstracts emphasize two-stepwise/general-\(k\) maximum-degree and size extremality; no accessible statement gives the fixed-maximum-degree tree minimum.

**Reasoning**

Broader graph-class extremal bounds do not dominate the tree-specific exact inverse problem or equality classification.

### Exact database or table

**Searches/source IDs**
- OEIS A392965
- Published SCOPE semantic search

**Evidence**
- OEIS A392965 supplies the \(k=1\) minimum-order sequence only.

**Reasoning**

The sequence is genuine prior art for \(k=1\), but it does not tabulate or imply the arbitrary-\(k\) recurrence and unique extremizer.

### Claim versus prior implication

**Searches/source IDs**
- arXiv:2411.15765 Theorem 4.2
- OEIS A392965
- abstracts for the 2023 and 2026 two-/k-SI papers

**Evidence**
- Theorem 4.2 gives a general-graph linear maximum-degree/order inequality; the audited tree lower bound grows recursively in \(h\).
- The unavailable 2026 paper's abstract states maximum-degree/size extremality for 2-SI graphs, not a minimum-order tree theorem.

**Reasoning**

No inspected prior theorem mechanically specializes to the final claim; the \(k=1\) case is explicitly treated as prior and the new claim is the all-\(k\) extension.


### Source inspections

- **Extremal results on k-stepwise irregular graphs** — `https://arxiv.org/abs/2411.15765`. Trigger: Closest accessible general-\(k\) primary source. Material read: Full open preprint, including section structure and Theorem 4.2 on maximum degree. Method: Open-access arXiv/author PDF. Assessment: NOT_COVERING the tree minimum-order theorem; its sharp general-graph bound is different and weaker for this problem. Evidence: Theorem 4.2 gives \(\Delta(G)\le\lfloor(n(G)+k)/2\rfloor\); later sections bound size.
- **On k-stepwise irregular graphs** — `https://doi.org/10.1016/j.dam.2026.06.027`. Trigger: Recent primary paper on the same graph class and extremal parameters. Material read: Publisher/indexed abstract and an open conference abstract; full publisher text was not accessible without a human verification step. Method: Open-web abstract search followed by lawful institutional retrieval attempt. Assessment: INACCESSIBLE_FULL_TEXT_RISK; abstract discusses maximum-degree and size bounds and 2-SI extremals, with no visible tree minimum-order statement. Evidence: The abstract says it establishes upper bounds on maximum degree and size and characterizes 2-SI extremals.
- **On Two-Stepwise Irregular Graphs** — `https://doi.org/10.24200/sci.2022.57725.5388`. Trigger: Earlier 2-SI source. Material read: Indexed abstract/citation context; full-text institutional retrieval timed out. Method: Open-web search and lawful institutional retrieval attempt. Assessment: RESIDUAL_RISK; accessible material does not state the audited tree theorem. Evidence: Available indexing identifies the paper as foundational for 2-SI properties.

### Checked sources

- arXiv:2411.15765
- DOI:10.1016/j.dam.2026.06.027
- DOI:10.24200/sci.2022.57725.5388
- OEIS A392965
- DOI:10.1016/j.amc.2017.12.045
- published SCOPE archive search

### Residual originality risks

- The full theorem text of Das--Mishra--Rai (2023) was not obtained.
- The full theorem text of Adiyanyam et al. (2026) remained behind human verification; its abstract makes it plausible but not decisive prior art.

## Scientific value — PASS

This extends a recognized minimum-order phenomenon from ordinary stepwise-irregular trees to every \(k\), with a unique extremizer, exact geometry, and a complete three-degree order spectrum. Fixed maximum degree and degree complexity are established structural parameters in the recent \(k\)-SI literature, so the theorem fills a motivated gap rather than selecting an arbitrary invariant.

## Limitations

The theorem concerns trees. The full texts of Das--Mishra--Rai (2023) and Adiyanyam et al. (2026) were not available in this audit; their abstracts/indexed descriptions were inspected, and the latter remained behind a human-verification access step. These are residual originality risks, not evidence of coverage.

## Final assessment

Correctness: **PASS**  
Originality: **PASS**  
Scientific value: **PASS**  
Disposition: **passed**
