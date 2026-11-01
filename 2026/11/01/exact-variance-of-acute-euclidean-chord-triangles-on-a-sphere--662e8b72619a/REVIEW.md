# Self-review

## Correctness — PASS

The assertion concerns all triples of independently area-uniform points on \(S^2\), with planar Euclidean chord angles. Its conditional two-point calculation is exact: at a fixed central separation \(\theta\), the allowed third-point set is a probability-\(\sin(\theta/2)\) belt minus a probability-\((1-\cos(\theta/2))/2\) cap that is contained in that belt. The uniform-dot-product law and the semicircle integral give \(\mathbb E[q]=1/2\), \(\mathbb E[q^2]=(\pi-1)/8\). Independence for overlap sizes zero and one, conditional independence for overlap size two, and exact combinatorial pair counts establish the variance for every integer \(n\ge3\). Strict-angle boundary events have zero measure. Symbolic coefficient checks, finite overlap enumeration, numerical integration, and direct sampled-point diagnostics have all passed. None of the simulations is used as an infinite proof.

## Originality — PASS, provisional

The directly relevant paper by Akopyan, Edelsbrunner, and Nikitenko (arXiv:2007.07783, Lemma 4 and Theorem 6) already gives the marginal probability \(1/2\); that is prior work, not a new claim. The full primary text was examined for its triangle arguments and second moments, and its statements do not give the shared-edge joint law \((\pi-1)/8\) or the variance of acute counts over all triples. The MathOverflow tetrahedron discussion (question 498296) asks for the probability that all four faces are acute, a separate four-way event which does not imply the full second moment. No equivalent result was found through targeted literature and indexed mathematical-finding searches or accessible same-topic prior claims. The result might be derivable from more general unpublished or uninspected U-statistic formulas; historical priority remains provisional.

## Mathematical value — PASS

The acute-triangle count is an intrinsic geometric statistic of a random spherical point configuration. Its exact covariance reveals precisely which overlaps cause dependence, while the nonzero \((\pi-3)/8\) coefficient changes the variance scale from the naïve independent-triangle order \(n^3\) to the actual order \(n^4\). The theorem holds at every finite sample size and yields the variance of the acute-face count of a random inscribed tetrahedron as a natural special case. It is more than a marginal-probability recomputation or a parameter substitution.

## Scope and residual risk

The variables are flat Euclidean chord triangles, not geodesic spherical triangles, and for larger point samples the triangles are not restricted to hull facets. The statement supplies a second moment rather than a full probability distribution or limiting law. A broader theorem not located in the inspected literature could subsume this evaluation; independent priority and proof review remain open.

Self-review: passed. Independent audit: not yet performed.
