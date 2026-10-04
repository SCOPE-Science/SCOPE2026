# Review

## Correctness

PASS. The source formulas for Kendall's tau, Spearman's rho, upper-tail dependence, and directional Chatterjee correlation were independently checked in the cited full texts. Solving the Kendall equation gives an exact one-parameter fiber. Substitution reduces Chatterjee's coefficient to a rational function whose derivative has one interior zero, proving the unique minimum and sharp right-boundary supremum. The transposed-direction difference factors with sign exactly equal to the sign of \(\alpha-\beta\). The tail-identification formula follows by solving the same fixed-tau equation.

The embedded verifier uses exact rational arithmetic and replays all algebraic identities and inequalities over large rational test families.

## Originality

PASS, with a residual specialized-calibration risk. The complete 2014 Dobrowolski–Kumar article was inspected through its Marshall–Olkin definition, dependence-measure section, and tail-dependence theorem. It contains the Kendall, Spearman, and tail formulas but predates Chatterjee's coefficient.

The full 2024 Ansari–Rockel HTML was inspected through the Marshall–Olkin Appendix calculation. It supplies the directional Chatterjee formula but does not state the fixed-Kendall sharp interval, the unique minimizer, the weak-dependence order separation, or the orientation identity.

The public preprint and abstract of the later global \(\xi\)-versus-Spearman exact-region theorem were checked as a possible stronger result. That theorem optimizes over all bivariate copulas rather than resolving the conditional fiber inside the Marshall–Olkin parameter family.

Targeted semantic and web searches for Marshall–Olkin fixed-Kendall fibers, Chatterjee extrema, asymmetry recovery, and exact parameter identification did not locate an equivalent statement.

## Value

PASS. The result exposes a concrete identifiability failure and its remedy in a classical asymmetric shock copula. Two standard concordance summaries are exactly redundant on each Kendall fiber, while a directional predictive-dependence measure can still vary from quadratic to linear order in weak dependence. The theorem gives sharp calibration limits and shows precisely how directional Chatterjee coefficients recover an asymmetry that Kendall and Spearman erase.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK formula_checks=20000 fiber_checks=47840 optimizer_checks=80 direction_checks=40000 tail_checks=15880`.
