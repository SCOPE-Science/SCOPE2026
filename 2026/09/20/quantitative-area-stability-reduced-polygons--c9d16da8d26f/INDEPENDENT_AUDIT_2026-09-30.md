# Independent Audit — 2026/09/20/quantitative-area-stability-reduced-polygons--c9d16da8d26f

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `b00fac00a523eb2221cc384e95c16bd011f63ada`
- Disposition: **PASSED**

## Correctness

**PASS** — The scalar stability argument is correct. Direct differentiation gives -f''(x)=tan(x/2)+4tan^3(x/2)+3tan^5(x/2), which is strictly increasing. The one-sided integral formulas for the tangent deficit therefore yield constants c_n=(f(mu)-mu f'(mu))/mu^2 below the mean and h_n=-f''(mu)/2 above it, with c_n<=h_n. Splitting negative and positive deviations and using equality of their first-moment sums gives V_2>=S^2/(n-1)>=U_2/(n-1), hence V_2>=(U_2+V_2)/n and the stated coefficient C_n=c_n+(h_n-c_n)/n. Lassak's butterfly-area inequality then transfers this scalar deficit to polygon area. Independent symbolic expansion gives c_n=pi/(6n)+13pi^3/(120n^3)+O(n^-5) and h_n=pi/(4n)+13pi^3/(48n^3)+O(n^-5), reproducing the displayed C_n expansion. The one-coordinate-to-zero test also gives the claimed first two sharp asymptotic terms for the unrestricted angle-sum constant.

## Originality

**PASS** — Lassak's 2005 paper supplies the canonical angles, their sum pi, the butterfly bound and the qualitative Jensen maximization by the regular polygon. Later surveys and recent reduced-polygon work located in the search remain qualitative or concern other geometries. No prior explicit angle-variance deficit, inverse stability estimate, or two-term scalar sharpness statement matching this record was found. The novelty claim is appropriately restricted to quantifying Lassak's strict concavity step, not to the underlying area theorem.

## Scientific value

**PASS** — The theorem converts a qualitative extremal result into a dimension-explicit stability estimate and identifies the correct first two asymptotic terms for the underlying angle problem. It is directly useful for near-extremizer analysis even though it does not yet control Hausdorff distance or prove the optimal coefficient over the geometrically realizable polygon class.

## Sources

- **Area of reduced polygons** — Marek Lassak. https://doi.org/10.5486/PMD.2005.3159 — Primary qualitative source for the canonical-angle butterfly estimate and regular-polygon area maximization.
- **Reduced convex bodies in Euclidean space—a survey** — Marek Lassak; Horst Martini. https://doi.org/10.1016/j.exmath.2011.01.006 — Survey of reduced-body results; no matching quantitative angle-variance refinement was located.
- **Reduced polygons in the hyperbolic plane** — Marek Lassak. https://doi.org/10.1007/s00013-024-02009-6 — Recent reduced-polygon work in a different geometry, useful as a novelty comparison.

## Limitations

- The stability distance is the variance of Lassak's canonical angles, not Hausdorff or vertex-coordinate distance.
- C_n is not proved globally optimal on the actual reduced-polygon realization space.
- Targeted searches cannot exclude an equivalent unindexed quantitative Jensen refinement in older convex-geometry literature.

## Independent checks

```json
{
  "minus_f_second_derivative_symbolically_checked": true,
  "deviation_balance_inequality_checked": true,
  "series_expansions_recomputed": true,
  "two_term_upper_test_checked": true,
  "lassak_qualitative_source_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first. No decisive comparison remained inaccessible; where a nondecisive full-document retrieval timed out, that limitation is stated explicitly rather than treating the paper as read.
