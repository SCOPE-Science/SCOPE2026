# Independent audit — 2026-09-29

**Record:** `2026/09/18/satterthwaite-transform-gaps-metric-lower-bounds--883f5d776ec4`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The cumulant, transform, and metric formulas all survive direct reconstruction. With w_i=alpha_i beta_i/A, beta=sum w_i beta_i, Gamma cumulants give the stated Jensen gap and kappa_3(S)-kappa_3(U)=2 A V_beta. The kernels g_s(x)=log(1+s x)/x and h_t(x)=-log(1-t x)/x are strictly convex integral averages; their uniform second-derivative bounds give exactly the displayed strong-convexity constants. The exponential tests have derivative or second derivative bounded by one, so they are admissible for d1 and d2, while x^3/6 gives the standardized d3-star obstruction.

## Originality

**PASS** — The September 2026 Bailly--Rapin--Swan--von Sachs preprint supplies explicit Gamma-Stein upper bounds controlled by scale discrepancies, not the signed all-parameter Laplace/MGF separation or the lower certificates stated here. Older Bock--Diaconis--Huffer--Perlman results concern majorization/tails of weighted i.i.d. Gamma sums. The most relevant residual source is Covo--Elalouf (2014), which studies single-Gamma approximation; open-access discovery did not produce inspectable full text, and an authorized Oxford retrieval returned no verified PDF. Its accessible abstract does not state the transform sandwich or smooth-metric lower certificates. On the accessible evidence, the narrowly stated combined result passes, with this source recorded as a residual originality limitation.

## Scientific value

**PASS** — The package complements current one-sided approximation upper bounds with computable lower obstructions in the same d1/d2 metrics and an exact heterogeneity statistic for the third-cumulant defect. It distinguishes unavoidable structural error from proof-dependent upper-bound slack and applies directly to weighted chi-square and Gamma-convolution settings.

## Independent checks

- Re-derived all Gamma cumulants under the moment-matched parameters alpha=A^2/B and beta=B/A and verified strict Jensen equality conditions.
- Differentiated the integral representations of g_s and h_t and checked the quantitative Jensen-gap constants, including the factor one-half in strong convexity.
- Checked admissibility of q_s=(1-e^{-s x})/s in d1, r_s=e^{-s x}/s^2 in d2, and x^3/6 in the standardized Lip(h'') metric.

## Findings

- No correctness defect was found in any displayed theorem or exactness equivalence.
- Bailly et al. cover the current upper-bound side; Bock et al. cover important majorization special cases but not the same moment-matched comparison package.
- Covo--Elalouf remains a documented full-text access limitation rather than being treated as inspected.

## Literature evidence

- https://arxiv.org/abs/2609.17880 — Bailly, Rapin, Swan and von Sachs (2026), current Gamma-Stein upper-bound paper for Satterthwaite approximation.
- https://doi.org/10.2307/3315257 — Bock, Diaconis, Huffer and Perlman (1987), tail/majorization inequalities for weighted Gamma sums.
- https://doi.org/10.1214/14-EJS914 — Covo and Elalouf (2014), single-Gamma approximation; abstract inspected, full text not obtained in this audit.

## Limitations

- Covo--Elalouf (2014) could not be inspected in full despite open-access search and authorized institutional retrieval; a related transform observation there cannot be excluded.
- The transform orders are not promoted to ordinary stochastic order or a one-crossing theorem.
- The d1/d2 transform-test lower certificates are not claimed optimal and no Kolmogorov lower bound is supplied.

## Publication consequence

The audited claim may remain at its source path. This audit does not modify the research statement; it adds only the independent-audit evidence and updates the independent-audit verification channel.
