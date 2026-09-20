# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The source definitions and the affected statements in arXiv:2609.20512v1 were checked directly. The proposed composition is literal CDF substitution `Phi(Psi_1,...,Psi_n)`. For the FGM outer copula and product-copula inner blocks, repeated differentiation gives

\[
g_{r,s,\theta}=1+\theta(1-2^rU)(1-2^sV),
\]

not the Jacobian-product formula asserted in Proposition 3.1. Since the two factors range independently over `[-(2^r-1),1]` and `[-(2^s-1),1]`, their product has exact range `[-max(2^r-1,2^s-1),(2^r-1)(2^s-1)]`, yielding the stated necessary-and-sufficient parameter interval.

The explicit closure counterexample is robust: for `(r,s,theta)=(2,1,1)`, the full mixed derivative at `(9/10,9/10,1/10)` is exactly `-99/125`. Continuity then produces an open region with negative density and hence a rectangular increment with negative mass. This rules out 3-increasingness.

The entropy argument was checked independently. In the interior of the validity interval the density is strictly positive. Under cube Lebesgue measure, `A_r=1-2^r prod X_i` is a martingale in `r`, and `(1+theta a b) log(1+theta a b)` is strictly convex in `a` for nonzero `theta b`. Conditional Jensen therefore makes the KL divergence from independence strictly increase under any genuine block enlargement. The second derivative at independence, `-[(4/3)^r-1][(4/3)^s-1]`, agrees with direct expansion. Symbolic differentiation and numerical quadrature reproduce the formulas and the stated entropy values.

A potential failure mode was checked: nonnegative full mixed density is sufficient here because the polynomial is grounded, smooth, has the correct one-dimensional margins, and is recovered by integrating its full mixed derivative over anchored rectangles. Conversely, negativity on an open set necessarily violates multivariate increasingness.

## Originality

**PASS, to the best of our knowledge.** General nested-copula theory already warns that unrestricted nesting is invalid; McNeil (2008) gives compatibility conditions for nested Archimedean copulas. Kendall-distribution theory also already establishes that a multivariate copula CDF evaluated at a random vector is generally not uniform. No novelty is claimed for either general fact.

The source paper arXiv:2609.20512v1 was inspected through its closure proposition, operad theorem, absolute-continuity proposition, entropy theorem, claimed closed subclasses and proof structure. Targeted searches for the exact FGM/product-block threshold, equivalent formulas involving `2^r-1`, FGM nesting with product copulas, and critiques of the current preprint did not locate the displayed admissibility interval or the entropy monotonicity result.

The originality claim is restricted to the exact product-block FGM validity window, its full-density formula, the strict entropy comparison under block enlargement, and their use as explicit counterexamples to the current version's central unrestricted closure and entropy-additivity statements. A residual risk is that general high-dimensional FGM admissibility theory may imply the threshold as a straightforward specialization, or that older hierarchical-copula literature contains an equivalent formula under different notation. That would reduce the novelty of the threshold but not the direct version-specific correction or the entropy comparison unless those too are already stated.

The 2024 presentation/research-report versions by the same author were visible in search results and appear to assert the same substitution/additivity idea; they were not used to infer absence of prior corrections. No public critique matching the present explicit counterexample was located.

## Value

**PASS.** The result addresses a foundational validity issue rather than a minor constant. The unrestricted closure assertion is what supports the proposed operad, the density factorization and later entropy character. A three-variable bounded-density counterexample therefore changes the status of the framework as currently stated. The exact FGM window goes beyond merely exhibiting failure: it identifies precisely when this natural family of block substitutions remains a copula and shows that the admissible dependence collapses to independence as block arities grow. The entropy theorem is independently falsified inside the valid region, where all densities are bounded and the composition is a genuine copula.

## Limitations

The exact classification is limited to a bivariate FGM outer copula with product-copula inner blocks; it is not a classification of all valid nested copulas. General nesting restrictions are prior art. The entropy strictness statement is made for nonzero parameters in the interior of the validity window. The exact threshold may be recoverable from broader multivariate-FGM parameter theory not identified in the search. The source-specific conclusions concern arXiv:2609.20512v1 and may be changed in later versions. Independent audit has not been performed.
