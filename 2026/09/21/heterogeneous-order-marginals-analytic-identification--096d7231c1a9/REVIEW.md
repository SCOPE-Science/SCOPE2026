# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The central reconstruction is exact: for fixed x, the order-statistic CDFs are tail probabilities of the Poisson-binomial count N_x. Differencing them recovers the full count distribution; its probability-generating polynomial, recentered at z=1, has the elementary symmetric polynomials of F_1(x),...,F_n(x) as coefficients. The resulting monic polynomial therefore has exactly those CDF values as roots, including multiplicities.

The global identification proof was checked against the main possible failure mode: pointwise root recovery does not itself label roots across x. The interval-identity argument handles this separately. For each candidate CDF G_i, the finitely many closed equality sets {G_i=F_j} cover the real line; Baire category forces one to contain an interval, and the identity property then makes that equality global. Induction handles multiplicities.

For two parents, the complete continuous ambiguity classification was checked in both directions. A continuous selector cannot switch branches inside a connected component of {F != G}; conversely, switches at component boundaries preserve continuity because the parent CDFs agree there, and monotonicity follows from monotonicity of each branch plus equality at the switching boundary.

The smooth counterexample was checked for the hidden hypotheses most likely to fail. The perturbation and its absolute value are C-infinity because they are flat at the crossing and support boundaries. Choosing the perturbation amplitude below an explicit derivative bound preserves strict positivity of all four densities. The perturbation is compactly supported, so full support and logistic tails are preserved. The two pointwise multisets coincide exactly while the side-dependent swap rules out a global permutation.

The verification artifact passed 4,848 exact or numerical checks. Numerical checks support, but do not replace, the analytic proof.

## Originality

PASS, with a deliberately narrow claim.

Classical forward formulas for heterogeneous order statistics are excluded from the novelty claim. David (1956), Maurer and Margolin (1976), and Bapat and Beg (1989) are cited for that background. The 2025 Espín-Sánchez–Hodgson–O'Neill paper was inspected at theorem level: its equations (1)-(2) explicitly express rank CDFs through symmetric products, Proposition 8 identifies the asymmetric model from all ranks under stochastic ordering and endpoint restrictions, and its discussion/Proposition 9 records nonidentification when ordering assumptions are removed in the broader nonparametric class.

The claimed contribution is restricted to four linked points not located in the checked literature: (i) the exact equivalence class given by pointwise CDF multisets, (ii) complete componentwise label-braiding for two continuous parents, (iii) identification under an interval-identity principle, including real analyticity, without dominance or endpoint separation, and (iv) a full-support strictly positive C-infinity counterexample showing that smoothness alone cannot replace unique continuation.

Residual risk remains because the Bapat-Beg 1989 and David 1956 full texts were not directly inspected. Their accessible descriptions are forward-distribution results, but an inverse observation could appear inside. Searches also covered heterogeneous/nonidentical order statistics, all-rank identification, anonymous/unlabeled ranked data, crossing CDFs, analytic identification, reliability, and current econometric order-statistic identification. No equivalent theorem was located. The originality assessment is therefore only to the best of current knowledge.

## Value

PASS.

The result separates two information questions that are often conflated. All rank marginals already determine the unordered parent CDF values at every threshold; failure of identification comes from globally matching those values into parent curves. The two-parent braid theorem describes that ambiguity exactly, and the analytic/C-infinity contrast gives a sharp conceptual regularity frontier: finite or infinite smoothness does not prevent hidden relabeling, whereas unique continuation does. The discriminant formula also exposes a practical stability warning near crossings.

## Concrete scientific limitations

The theorem assumes independence and all rank marginals. It is a population identification result rather than an estimator or finite-sample rate. Real-analytic CDFs on the whole real line are a strong subclass, though the interval-identity formulation is broader. Near crossings, root recovery is ill-conditioned. External semantic labels remain unidentified even when the set of parent laws is recovered up to permutation.
