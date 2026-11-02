# Self-review

## Correctness — PASS

The stated domain includes all nonnegative triples with positive total weight, including degenerate boundary cases. The numerical radius of the infinite shift equals the Perron root of a three-by-three weighted triangle, by residue-class Cauchy–Schwarz and long periodic test blocks. Its characteristic cubic depends on fixed first and second weight moments only through a fixed coefficient and the product of the three weights. The positive root increases with the product. Constrained minimization is exact: up to permutation it gives two equal large weights for normalized variance below one half, then a zero coordinate above it. Both branch formulas and all equality cases follow; the monotonicity of two displayed quotient formulas proves the best variance coefficient. The zero-weight and uniform endpoints were checked separately.

The included standard-library checker successfully ran 4,912 integer triples and eight boundary diagnostics. Floating-point results support but do not replace the infinite-dimensional and all-real-parameter argument.

## Originality — PASS, qualified

Sharif (arXiv:2303.00876, first public 2023-03-02), whose complete accessible text was inspected, gives the arithmetic-mean lower bound and finite-period variational formula; no fixed-second-moment sharp envelope is stated. Chien–Sheu (2013, complete eight-page paper examined) computes other weighted-shift families, especially a single exceptional edge, and does not optimize a three-periodic triangle at fixed sum and variance. An accessible complete research statement on strict convexity and smoothness of graph-edge numerical-radius norms identifies the three-periodic norm but concerns global norm geometry and support smoothness, not the constrained minimization or its sharp coefficient. Stout (1983) and Ridge (1976) provide important classical formulas; only accessible summaries and subsequent reproductions were compared, leaving a residual indirect-coverage risk. Search comparisons examined characteristic-polynomial reductions and equivalent weighted-triangle formulations, not just title overlap.

## Mathematical value — PASS

The source gives a qualitative arithmetic-mean bound, but does not quantify how much a genuinely three-periodic pattern improves it. Fixing a natural squared-difference moment produces a complete sharp classification, a nontrivial change of extremizing support at normalized variance one half, and a best universal quadratic stability constant. The zero-weight extremizers identify the exact boundary of positive-weight stability. This is a natural finite-parameter spectral optimization, not a mere restatement of the known cubic.

## Scope and residual risks

Only three-periodic Hilbert shifts are covered; no claim is made about arbitrary periods or alternate variance normalizations. Classical papers contain broader periodic spectral formulas, and a differently parametrized earlier moment-optimization inequality could exist. Independent assessment is outstanding.

Self-review: passed. Independent audit: not yet performed.
