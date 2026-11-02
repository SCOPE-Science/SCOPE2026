# Scientific review

## Correctness — PASS

The final result concerns finite-dimensional (dimension at least two) unitary renewal resetting with strictly positive finite-time survival. The last-renewal expansion and invertibility of the averaged channel lead to a unique propagator. Its positivity is **exactly** the positive-semidefiniteness of the excess unnormalized last-reset operator: a negative eigenvector can be tested against a pure state rotated to its orthogonal complement. If this operator is positive, the propagator is manifestly a convex combination of a unitary channel and a replacement channel, so it is completely positive. The adjacent reset-hazard expansion has positive coefficients for nondecreasing hazards. For a bit-flip qubit and a pure reset, the second-step test has exact negative eigenvalue \(p(q-p)\) whenever \(0\le q<p<1\). These are universal analytic arguments; 13,298 finite numerical checks provide only reproducibility tests. The result excludes sure finite-time resets and nonunitary between-reset maps.

## Originality — PASS, qualified best knowledge

The principal comparison is Carollo–Wald, arXiv:2601.13367, including its main text and supplemental renewal/divisibility calculations. They develop the channels and use numerical witnesses and a special divisible periodic process, but do not identify the model-wide matrix-order equivalence, increasing-hazard guarantee or explicit decreasing-hazard obstruction. Their displayed linear ramp is an instance of our guarantee, not a source of a claimed new renewal formula. Settimo et al., arXiv:2506.08103, establish picture inequivalence but not the present criterion. Megier–Smirne–Vacchini (2020) handle semi-Markov master equations and an always-divisible diagonalizing jump model; Megier et al. (2021) consider trace-distance properties. None of those inspected statements dominates the claimed all-unitary noncommuting-reset theorem. Related indexed mathematical records on quantum resetting, restart detection, and qubit divisibility were searched and compared by claims. Residual risk: general results on affine replacement maps or semi-Markov positivity might implicitly yield the order characterization; the search does not certify worldwide novelty.

## Value — PASS

The result closes a natural testability gap in the motivating analysis: an exact necessary-and-sufficient criterion for all time pairs and all dimensions in the unitary-reset model, replacing merely sampled nondivisibility witnesses. A simple monotone-hazard design rule guarantees CPTP propagators even for noncommuting reset states, and the sharp decreasing-hazard counterexample reveals positive-indivisibility invisible to two-state trace-distance tests. The guarantee also applies directly to the motivating paper's entanglement-enhancing ramp, separating one-time CP-divisibility from broader temporal memory. This is structural and operational, not an arbitrary finite enumeration.

## Residual limitations

The result is not a characterization of Heisenberg divisibility or process-tensor Markovianity, and the rising-hazard condition is sufficient rather than necessary for fixed systems. Wider nonunitary and sure-reset cases remain outside scope. No independent literature-wide validation or external certification has been performed.

Self-review: passed. Independent audit: not yet performed.
