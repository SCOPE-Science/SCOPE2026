# Review of the cross-polytope-prism section theorem

## Correctness
**PASS (same-model).** Each generic section vertex is in one-to-one correspondence with a sign-changing original edge. The base graph is a complete graph minus an antipodal perfect matching, giving the exact count \(g_d(s)\). The vertical contribution is \(k-\ell\) and the maximum follows from explicit completed-square inequalities. Four integer-valued constructions realize every ordered layer-count pair, so the spectrum is exact. The standard vertex-avoiding perturbation lemma extends the upper bound to all hyperplanes. The Python checker independently rebuilds the graph and tests thousands of exact-integer examples; it is corroborative, not a replacement for the general proof.

## Originality
**PASS relative to examined evidence, with residual historical risk.** Ziegler provides classical polytope background. Khovanskii (2006) studies broad section combinatorics, including an example of a polygonal prism's average face degrees. De Loera et al. (arXiv:2412.12419) give a general upper bound, generic perturbation and vertex spectra mainly for cyclic polytopes and hypercubes. Birkemeyer et al. (arXiv:2609.16195), Proposition 3.6, give a general prism-to-slab reduction; this is the nearest structural antecedent, but its inspected statement does not give the exact cross-polytope-prism count, realizability or generic spectrum. The absence of a matching indexed theorem is not a proof of priority; unindexed sources and the unavailable complete text of Ziegler remain risks.

## Mathematical value
**PASS (same-model).** The result determines an all-dimensional sharp extremal invariant and complete generic vertex-number set for the cross-polytope-prism family, exhibiting systematic gaps and a quantitative deficit from the unrestricted graph maximum cut. Those are natural geometrically constrained slicing invariants.

## Limits
The full vertex spectrum is generic only, while the maximum covers all affine hyperplanes. Face vectors and section volumes are not classified. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
