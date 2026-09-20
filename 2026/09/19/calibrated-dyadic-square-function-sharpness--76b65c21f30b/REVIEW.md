# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The review checked each algebraic and probabilistic reduction.

The exact \(A_2^d\) computation uses only the states explicitly present in Section 2 of arXiv:2609.14430v1. Reciprocal rescaling preserves the product of the two conditional averages. The Phase-I products are maximized at \(n=N\): after writing \(q=2^{N-n}\), the difference from the \(n=N\) product reduces to a positive factor times
\[
\frac A\alpha-\frac{A(q+1)}{3q}-\frac{\alpha(q+1)}3.
\]
Convexity of \(A+A/q+\alpha q+\alpha\), together with \(A\ge4\) and \(1/2<\alpha<1\), makes the endpoint check strict. Phase-II products are smaller because \(\alpha<1\). The maximizing state occurs with positive probability, so the bound is an equality rather than merely an upper estimate.

The exact \(L^2(w_N)\) formula follows by simplifying the two ordinary terminal atoms of one building block, then summing the disjoint continuation levels as a geometric series. The source's final-split expression reduces to the stated last term using the definition of \(\gamma_N\). No estimate is used in this part.

For the square-function tail, the source proves \(\eta_N\Rightarrow3/8\). Hence for every fixed \(\theta<3/8\), \(\mathbb P(\eta_N\ge\theta)\to1\). Combining this with the exact exceptional-path weighted mass and \(r_N^{2^N}\to e^{-4}\) gives the asserted liminf. The normalization was recomputed from the exact characteristic and exact input-norm asymptotics.

A compact numerical consistency script was executed successfully. It verifies the finite-\(N\) phase-product maximum for \(2\le N\le17\) and the stated convergence trends. The numerical check is supplementary and is not used as proof.

## Originality

**PASS, to the best of our knowledge.** The directly relevant source, arXiv:2609.14430v1, was inspected in full around Theorem 1.2 and Lemmas 2.1--2.5. It proves the critical logarithmic lower bound but records only
\[
\tfrac12 2^N\le[w_N]_{A_2^d}\le6\,2^N,
\qquad
\|f_N\|_{L^2(w_N)}^2\le8\,2^N,
\]
and uses the weaker event probability \(\mathbb P(\eta_N\ge1/4)\ge1/3\). It does not state the exact \(A_2^d\) characteristic, the exact geometric-series formula for the input norm, its limiting coefficient, or the resulting \(0.1065624665\ldots\) normalized lower bound.

Targeted searches were made for the source title and identifier together with terms such as exact \(A_2\) characteristic, exact constant, \(3/8\), dyadic square-function sharpness, and weighted weak type. No correction, follow-up, or equivalent calibration was located. The earlier endpoint paper of Domingo-Salazar--Lacey--Rey, the Lacey--Scurry preprint, and Osękowski's 2020 weighted square-function paper concern the surrounding weighted theory but predate this specific 2026 construction.

Residual risk remains because the source preprint is very recent, so an unindexed contemporaneous calculation could exist. The algebra is also sufficiently explicit that an equivalent unpublished observation is possible. No inaccessible paper was identified that specifically appears likely to contain this exact calibration.

## Value

**PASS.** The source settled the qualitative sharpness of the logarithmic critical factor. The present result extracts additional quantitative information from the extremizing mechanism: it identifies the exact worst \(A_2^d\) state, gives the complete weighted input-energy formula, and improves the explicit normalized lower bound for the best universal critical constant from the source's displayed \(e^{-2}/48\approx0.00281949\) to \(0.1065624665\ldots\). The result also clarifies that the limiting \(3/8\) random-sum concentration can be used without the coarse \(1/3\)-probability truncation.

## Scientific limitations

The new constant is a certified lower bound, not the optimal weak-type constant. The result does not improve the already sharp order of growth, does not determine the full square-function distribution, and is specific to the dyadic construction in arXiv:2609.14430v1. No independent validation or formal proof-assistant verification is asserted.
