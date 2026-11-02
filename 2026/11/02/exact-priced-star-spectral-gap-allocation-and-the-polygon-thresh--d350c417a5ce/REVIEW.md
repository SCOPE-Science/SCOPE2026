# Scientific assessment: exact priced-star spectral-gap allocation

## Correctness — PASS

The zero-sum Rayleigh quotient for a weighted star is exactly the generalized eigenproblem \((\operatorname{diag}(w),I-\mathbf1\mathbf1^{\mathsf T}/(m+1))\). The target-gap constraint is therefore a diagonal positive-semidefinite majorant, with no approximation. Gram duality reduces its optimum to the minimum achievable resultant length of vectors having prescribed lengths \(\sqrt{c_i}\); the polygon inequality and the reverse triangle inequality establish that length exactly. The proposed primal edge rates satisfy the matrix inequality by a weighted Cauchy–Schwarz identity, and their cost equals the dual bound. Complementary slackness forces each individual optimal rate in both phases; the same quadratic identity proves the eigenspace dimension. These steps establish the full real-positive parameter range; the 13,940 finite exact-rational assertions are secondary consistency checks, not an infinite proof.

## Originality — PASS on material inspected, with residual risk

Sun–Boyd–Xiao–Diaconis (2006) provide the unrestricted-graph, arbitrary-linear-cost SDP and its geometric dual, so the abstract optimization framework and dual correspondence are already known. Their worked examples are a small network, paths and cycles, not the explicit heterogeneous-price star rule. Göring–Helmberg–Wappler (2007, Example 6) give the uniform-price star, which our theorem explicitly excludes as independent novelty. Their 2008 arbitrary-edge-length formulation subsumes the optimization model, but the inspected structural theorems concern embedding dimensions and separators rather than exact cost-optimal conductances and the polygon phase transition. Ghosh–Boyd (2006) derive convex graph-family bounds and do not settle the fixed-star heterogeneous-price problem. Direct searches of published mathematical work and prior mathematical findings did not identify the same explicit all-price formula, uniqueness and multiplicity classification. Absence from these searches does not prove uniqueness in the literature. Residual risks include implicit derivability within the general 2006 SDP, specialist nonindexed graph-embedding literature and the uninspected full 1990 Fiedler tree article.

## Mathematical value — PASS

The price vector may be arbitrary and nonuniform, yet the optimizer is completely explicit for every positive budget. The polygon inequality is a sharp and unexpected no-reallocation region; across its boundary the same model moves into a unique nonuniform allocation and its gap eigenspace changes dimension. This supplies an exact design-and-sensitivity rule without numerical semidefinite optimization, with practical relevance to continuous-time diffusion and Markov rates. The result is not the earlier equal-price star calculation or a purely finite table.

## Scope and limitations

Only stars, positive linear edge prices, and the unnormalized continuous-time Laplacian are covered. Publication-level novelty is not guaranteed by these comparisons; independent validation is pending. The self-review evaluated the mathematical claim, proof and reproducibility, not the completeness of all historical mathematics.

Self-review: passed. Independent audit: not yet performed.
