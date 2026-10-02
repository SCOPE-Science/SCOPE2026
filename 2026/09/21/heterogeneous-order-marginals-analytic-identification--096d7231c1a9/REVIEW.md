# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **PASSED**.

## Final claim

For independent heterogeneous observations, the marginal distribution of every order statistic determines, at each threshold \(x\), the unordered multiset of parent CDF values \(\{F_i(x)\}\). Global ambiguity is therefore exactly label matching across crossings: any interval-rigid class, in particular real-analytic CDFs, is identified up to one permutation; for two continuous parents the ambiguity is componentwise swapping on \(\{F
e G\}\); and even full-support positive-density \(C^\infty\) parents can exhibit nontrivial smooth label braiding.

## Correctness — PASS

For fixed \(x\), the full rank-marginal vector gives the law of the exceedance/count variable \(N_x\); its probability generating polynomial is \(\prod_i((1-F_i(x))+F_i(x)z)\), so its roots or elementary symmetric coefficients recover the multiset \(\{F_i(x)\}\). If two collections from an interval-rigid function class have the same pointwise multisets, for each fixed candidate function the closed coincidence sets with the competing functions finitely cover \(\mathbb R\); Baire gives a coincidence interval and interval rigidity makes that identity global, after which induction matches all labels. Real-analytic CDFs therefore identify up to one permutation. For \(n=2\), the only continuous ambiguity is independent label swapping on connected components of \(\{F
e G\}\). The flat-crossing construction \(F_0\pmarepsilon q\) versus \(F_0\pmarepsilon|q|\) can be chosen with everywhere-positive smooth densities and gives a genuine \(C^\infty\) braid.

## Originality — PASS

The 2025 Cowles paper was inspected in full around Propositions 7–9: its asymmetric nonparametric identification requires stochastic ordering and distinct support endpoints, and it explicitly explains that crossings obstruct its labeling argument. It does not state pointwise recovery of the unordered parent-CDF multiset from all rank marginals, the interval-rigidity/analytic global-label theorem, the exact two-parent braid classification, or the smooth positive-density counterexample. Published-record searches found no earlier theorem with those implications.

## Scientific value — PASS

The result pinpoints the exact information content of all order-statistic marginals and separates algebraic pointwise recovery from the genuinely global label-matching obstruction. The analytic-versus-\(C^\infty\) boundary and exact two-parent braid classification are natural structural identification results with direct relevance to heterogeneous ranked-data models.

## Residual risks and limits

- Older inverse-order-statistics literature under different notation could contain equivalent functional-identification statements, but no decisive implication was found in the searches or the recent paper's literature framing.
- Independence and observation of every rank marginal are required.
- The result is structural identification and gives no finite-sample conditioning/stability guarantee.
- \(C^\infty\) regularity alone does not resolve label braiding.

This is a mathematical review, not formal proof-assistant verification or external certification.
