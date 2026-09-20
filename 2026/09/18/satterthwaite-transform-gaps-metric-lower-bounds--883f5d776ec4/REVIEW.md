# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.**

The moment-matched parameters were checked directly:
\[
\beta=B/A,\qquad \alpha=A^2/B,
\]
so the approximating Gamma has mean \(A\) and variance \(B\).

The cumulant formula follows from Gamma cumulants and independence. Reweighting by
\(w_i=\alpha_i\beta_i/A\) makes the matched scale exactly the weighted mean
\(\beta=\sum_iw_i\beta_i\), after which strict Jensen convexity of
\(x^{r-1}\) gives every higher-cumulant inequality. The third-cumulant gap simplifies exactly to \(2A V_\beta\).

Both transform inequalities were independently reduced to Jensen inequalities using
\[
\frac{\log(1+sx)}x=\int_0^s(1+ux)^{-1}du
\]
and
\[
\frac{-\log(1-tx)}x=\int_0^t(1-ux)^{-1}du.
\]
The second derivatives are positive on their respective domains. The quantitative constants follow from uniform lower bounds on those second derivatives and the standard strong-convexity Jensen gap.

The \(d_1\) lower certificate uses \((1-e^{-sx})/s\), whose derivative is bounded by one. The \(d_2\) certificate uses \(e^{-sx}/s^2\), whose second derivative is bounded by one. These are valid members of the exact smooth test classes used in the recent Gamma-Stein paper. The third-order smooth lower bound follows from the admissible cubic test after centering and variance normalization.

No tail-order claim is made: transform ordering alone is deliberately not promoted to ordinary stochastic ordering.

## Originality

**PASS, to the best of our knowledge.**

The September 2026 paper of Bailly, Rapin, Swan and von Sachs was inspected in searchable full text. It develops explicit upper bounds for Satterthwaite's moment-matched Gamma approximation in Wasserstein \(d_1\), second-order Zolotarev \(d_2\), and Kolmogorov distance, with scale discrepancies as controlling quantities. Searches in that paper and externally did not locate a lower-bound theorem based on Laplace-transform test functions, the signed transform sandwich stated here, or the exact size-biased scale-variance identity for the third-cumulant defect.

Bock, Diaconis, Huffer and Perlman (1987) study Schur-convexity and tail inequalities for linear combinations of Gamma variables. Kochar's later survey reviews stochastic comparisons of weighted Gamma sums. Those results make majorization-based special cases an important prior-art risk, but the searched descriptions concern changing coefficient vectors within weighted-sum families rather than comparison with a Gamma law whose shape and scale are simultaneously changed to match the first two moments.

Covo and Elalouf (2014) is the prior source most plausibly capable of overturning part of the originality claim: it specifically studies single-Gamma approximations to sums of independent Gamma variables and discusses the usual same-mean-and-variance approximation from an infinitely-divisible viewpoint. Its abstract and multiple bibliographic descriptions were inspected, but the full text was not accessible through the source inspected here. The available material does not state the transform inequalities or metric lower certificates. Because this source could contain a related transform observation, the originality claim is intentionally narrow and qualified.

Searches included combinations of `Satterthwaite`, `moment matched gamma`, `Laplace transform`, `MGF`, `lower bound`, `Wasserstein`, `Zolotarev`, `gamma convolution`, `weighted gamma`, `stochastic order`, `majorization`, `third moment`, and `skewness`. No source was located stating the complete package of: all-order cumulant domination, global two-sided transform separation, quantitative size-biased scale-variance gaps, and explicit \(d_1/d_2\) lower certificates for the Satterthwaite match.

## Value

**PASS.**

The recent literature supplies explicit upper guarantees but not a matching structural obstruction. The present result identifies what Satterthwaite necessarily loses under heterogeneous scales: every higher cumulant is too small, the Laplace and positive-MGF discrepancies have fixed signs, and the exact transform gap can be inserted directly into the same \(d_1\) and \(d_2\) test classes to produce computable lower certificates. The third-cumulant identity gives a particularly transparent heterogeneity statistic and explains why third-moment matching methods can improve on a pure two-moment Satterthwaite fit.

The result is reusable for weighted chi-square statistics, variance-component combinations, Wishart trace reductions, and other settings already covered by Satterthwaite approximation.

## Sources inspected

- Bailly, Rapin, Swan, von Sachs, *Explicit Gamma-Stein Bounds for Satterthwaite's Approximation*, arXiv:2609.17880 (searchable full text).
- Bock, Diaconis, Huffer, Perlman, *Inequalities for linear combinations of gamma random variables* (publisher abstract/metadata and surrounding literature description).
- Kochar, *Stochastic Comparisons of Weighted Sums of Random Variables* (chapter abstract/metadata).
- Covo, Elalouf, *A novel single-gamma approximation to the sum of independent gamma variables, and a generalization to infinitely divisible distributions* (abstract and bibliographic descriptions only; full text not inspected).

## Scientific limitations retained

No ordinary stochastic order, one-crossing property, Kolmogorov lower bound, or optimality of the transform-test lower certificates is claimed. Older majorization theory may subsume special cases. Covo-Elalouf (2014) remains the principal uninspected source capable of containing a related transform statement.