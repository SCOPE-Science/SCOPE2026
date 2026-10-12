# Review of the commuting conditional-subentropy inequality

## Correctness — PASS

The source definition of subentropy and the Jozsa–Mitchison half-axis integral agree with the normalized formula used here. The central new lemma is verified directly: the integrand difference for a split \(w\mapsto(w-a,a)\) is nonnegative; the log-convex product form proves concavity along the split; and the right derivative at \(a=0\) is at most one. These facts give \(0\le\Delta Q\le a\) with all endpoint and zero-probability cases included. Telescoping over the conditional outcome masses yields \(Q(X|B)\le1-p_{\mathrm{guess}}(X|B)\). For \((1-\varepsilon,\varepsilon)\) the derivative is exactly one, proving uniform optimality of the coefficient. The computation validates 48 rational instances, not the universal claim.

## Originality — PASS, with residual literature risk

Datta–Dorlas–Jozsa–Benatti, arXiv:1310.1312, §2.5, prove nonnegativity and an analytically restricted case, but leave the general min-entropy upper bound conjectural. Jozsa–Mitchison, arXiv:1404.7694, equation (14) and Property 9, already prove the integral formula and monotonicity under marginalization. Those known contributions are credited, not treated as novel. The exact sharp mass-splitting rate and the posterior-maximum Bayes-error upper bound were not found in searched related formulations or in the two inspected full-text sources. A differently named decision-theoretic or refinement result could supply equivalent coverage, so this review does not assert an exhaustive literature census.

## Value — PASS

This settles a mathematically natural, complete class of the original conditional-subentropy conjecture: all finite ensembles with mutually commuting signal states, with no binary, purity, or uniformity constraints. The linear estimate is strictly sharper than the conjectured logarithmic one away from certainty and has an optimal universal constant. It also supplies a bound on optimal classical guessing directly from the conditional subentropy and a usable structural proof mechanism.

## Limits and provenance of evidence

No general result for noncommuting signal ensembles is established. The subentropy formula and earlier marginal nonnegativity are from the cited literature; the linear conditional upper estimate is the new claim. Numerical checks do not independently establish universal correctness. An independent mathematical review has not yet taken place.

Self-review: passed. Independent audit: not yet performed.
