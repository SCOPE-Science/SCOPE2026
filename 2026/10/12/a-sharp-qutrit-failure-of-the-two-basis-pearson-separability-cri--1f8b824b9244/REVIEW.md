# Scientific review: the qutrit Pearson separability boundary

## Correctness — PASS

The displayed qutrit state is a normalized convex mixture of two mutually orthogonal product preparations. The two chosen bases are exactly mutually unbiased by the cubic Fourier-matrix construction; all local variances are positive. Direct first- and second-moment computations give the exact positive excess \(5449/46002\), independently replayed by an exact nine-by-nine symbolic-matrix verifier. The all-separable-qubit protection inequality follows from a full Bloch-vector decomposition and weighted Cauchy–Schwarz, including the pure-marginal boundary. Adding \(1/100\) white noise preserves classical-classical structure and yields an explicit full-rank violating state. No finite experiment is used to infer the dimension-uniform qubit theorem.

## Originality — PASS, with residual literature risk

Maccone–Bruß–Macchiavello, *Complementarity and correlations* (arXiv:1408.6851), explicitly stated the general Pearson sum bound as an unproved conjecture, not as a theorem. Jebarathinam–Home–Sinha (arXiv:1909.01372) analyzed specified noisy qutrit families rather than the two-branch separable state here; Sadana–Kanjilal–Home–Sinha (arXiv:2201.06188) still called the general inequality conjectural and proved restricted positive results. The more recent Wang–Wang–Chen work (arXiv:2608.03828) concerns complementary **mutual-information** sums and other metrics, not this exact Pearson threshold according to accessible descriptions; its complete text was unavailable. No exact or dominating Pearson counterexample was located in targeted literature and research-record searches. Absence of a search hit is not itself a novelty proof, and an unindexed equivalent or an inaccessible passage remains possible.

## Value — PASS

This is a counterexample to a natural, widely used proposed high-dimensional entanglement witness, using a state with no quantum discord. Its exact false-positive value, the proof that qubits cannot exhibit such a failure, and full-rank robustness establish a meaningful sharp dimension boundary rather than a parameter-specific arithmetic curiosity. The result has direct consequences for interpreting two-basis Pearson data without prior state assumptions. It does not determine optimal violation sizes for arbitrary dimension or contradict the separate mutual-information theorem.

## Literature and limitations

The decisive comparison is between the universal 2014 conjecture and the present product-mixture construction. Later qutrit calculations on isotropic, Werner and colored-noise families do not imply a statement over all separable states. Results about nonadditive Shannon mutual-information correlation scores are not logically equivalent to Pearson correlation constraints. An inaccessible plausible 2026 primary manuscript has been listed as a residual priority risk rather than silently treated as ruled out. All computational checks use finite exact matrices and the analytic qubit proof carries the universal quantifier.

Self-review: passed. Independent audit: not yet performed.
