# Review of the Wiener-index parent-age theorem

## Correctness — PASS

The parent choices are independent and uniform; the new-leaf equation \(W_{m+1}=W_m+m+S_{P_{m+1}}\) gives the mean Wiener recurrence. The vertex-age distance regression \(s_v(m)=m(H_m+H_{v-1}-3+2/v)\) follows by a one-step recursion and its exact birth boundary. Conditioning on one parent then propagates the mean perturbation by \(n(n+1)/(i(i+1))\). The strictly increasing harmonic kernel yields the threshold; the limit \(1+\log a\) proves the ratio \(e^{-1}\). Independence gives the root-degree mixed moment and the exact telescoping sum. All boundary cases \(n=2,3\) and \(v=1\) were checked; the proof is for all \(n\ge i\ge2\), not extrapolated from finite examples. A standalone exact checker verifies 46,233 trees, 120 conditional identities, 8 aggregate covariances and 3,689 additional rational identities.

## Originality — PASS, with residual risk

The full text of Neininger (2002) covers the Wiener index jointly with internal path length but not with a specified parent label or root degree. Full arXiv text of Grübel and Michailow (2014) covers Wiener strong limits, and Holmgren and Janson (2014) covers degree and fringe-tree statistics, without the claimed mixed harmonic regression. The closest previously recorded related directions concern the *root path length* in recursive trees, leaf counts, or Wiener statistics in a different uniform-tree model. Those statements do not imply the Wiener/parent-choice regression: total distances are not determined by internal path length, root degree, or leaf count separately. Searches for both exact parent-location formulas and alternative age-response and mixed-moment terminology found no equivalent assertion. Dobrow's 1996 recursive-tree distance paper was identified as a plausible older source but its complete text was inaccessible; equivalence concealed in classical bivariate generating functions remains a real risk. No absolute novelty guarantee is claimed.

## Value — PASS

The Wiener index is the canonical global pair-distance measure of a tree, while each parent decision is its local growth mechanism. The exact regression reveals a sharp, non-obvious sign reversal at the fraction \(e^{-1}\) of possible parent ages, rather than merely another marginal expectation. Summing the response establishes that the root's degree is negatively associated with total tree spread, with the exact finite-size law and a zeta-value asymptotic. These outcomes give a structural explanation that is useful when comparing preferential attachment by age with uniform growth; no implication for a different growth model is asserted.

## Scientific limits and closest sources

Neininger, *The Wiener Index of Random Trees* (2002), DOI `10.1017/S0963548302005321`: mean and Wiener/internal-path-length covariance. Grübel–Michailow, arXiv:`1406.7614v1`: almost-sure Wiener limits. Holmgren–Janson, arXiv:`1406.6883v1`: fringe-tree and degree structure. Dobrow (1996), DOI `10.2307/3215356`: older distance-distribution source, full text not inspected. No claim is made for weighted or nonuniform attachment, pathwise sign monotonicity, or independent expert certification.

Self-review: passed. Independent audit: not yet performed.
