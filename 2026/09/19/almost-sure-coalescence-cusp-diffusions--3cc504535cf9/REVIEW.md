# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The quantitative refinement uses the same Lyapunov identity as Larsen's proof, but stops when midpoint local time reaches a variable level \(a\). This changes only the final Markov inequality and gives an error proportional to \(d^{1-2\beta}/a\). The DDS representation and the standard exponential law for Brownian local time accumulated before exit from \((-1,1)\) give the \(e^{-a}\) term. The time estimate follows from \(\langle M\rangle_t\ge t\), Levy's identity for Brownian local time, and an elementary optimization in \(a\).

The global argument was checked separately. The gap is a nonnegative continuous local martingale. If it converged to a positive value, midpoint recurrence would repeatedly place the pair near a state \((0,d_*)\) where the two diffusion coefficients differ by a fixed amount, forcing infinite gap quadratic variation; this contradicts convergence of a continuous local martingale. Hence on noncollision the gap tends to zero. Recurrent zero returns of the midpoint then produce arbitrarily small symmetric pairs, and the strong Markov property together with the local collision probability tending to one makes perpetual noncollision have probability zero.

The proof does not rely on simulation or on a numerical surrogate.

## Originality

**PASS, to the best of our knowledge.** arXiv:2609.19389v1 was inspected at the theorem and proof level relevant to the collision construction. It states positive-probability collision for sufficiently small gaps and supplies the unit-threshold Lyapunov/local-time argument; the stronger shrinking-gap probability, collision-time upper scale, and global almost-sure coalescence conclusion were not found there.

Repository searches for the source identifier, cusp collision/coalescence, and synchronous-diffusion coalescence found no overlapping SCOPE record. External searches included exact source-title queries and synonymous formulations involving strict comparison, non-confluence, synchronous coupling, and coalescing one-dimensional diffusions.

Barlow--Burdzy--Kaspi--Mandelbaum (2001) was inspected and explicitly proves almost-sure coalescence for skew Brownian motions driven by the same Brownian motion. That classical result is prior art for the phenomenon of synchronous coalescence, but its local-time SDE is different from the continuous uniformly elliptic cusp coefficient family here, so no originality is claimed for the general idea of almost-sure coalescence.

The accessible abstract/bibliographic records of Yamada (1986) and Ouknine--Rutkowski (1990) concern non-confluence and strong comparison. Their complete texts were not directly inspected. They are the most plausible residual sources for an older general criterion that could subsume part of the conclusion; this residual risk is recorded rather than treated as evidence of novelty.

## Value

**PASS.** Larsen's theorem establishes that strict comparison can fail. The present refinement shows the failure is much stronger for the exhibited cusp models: collision becomes overwhelmingly likely at vanishing initial gap and unavoidable in finite time for every fixed pair. The tunable threshold also exposes a quantitative time scale \(d^{2-4\beta}\) on the upper side.

## Limitations

The time scale is not shown sharp. Constants inherited from the source Lyapunov construction are not optimized. The almost-sure statement is for each fixed deterministic pair and does not claim simultaneous coalescence for all uncountably many starting points. Later revisions of the source preprint could change the comparison baseline.
