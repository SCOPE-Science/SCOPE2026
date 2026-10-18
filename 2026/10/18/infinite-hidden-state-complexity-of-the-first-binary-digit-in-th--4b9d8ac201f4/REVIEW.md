# Scientific review: infinite hidden-state complexity of a Pelikan binary observation

## Correctness

**PASS.** The domain is the stationary annealed process for \(1/2<p<1\). The model-specific Markov property follows by conditional uniformity of dyadic shells, including the geometric redistribution from the upper shell under doubling. The positive return transform follows by the strong Markov property and a nearest-neighbor hitting-time decomposition. Quadratic conjugation proves the transform is nonrational for every parameter in the domain; the finite-matrix resolvent proves that a finite-state hidden Markov output always has rational word-gap transform. Standard local singularity expansions account for both parity branches below \(p=4/5\), the colliding branch/pole at equality, and the simple positive pole above. An independent absorbing-chain recurrence matches the algebraic coefficients in \(300\) exact positive/coefficient comparisons; \(12\) additional exact side-condition checks and \(6\) finite asymptotic diagnostics pass. Finite calculations supplement rather than establish the infinite proofs.

## Originality

**PASS, with material priority qualification.** Yan et al. (arXiv:2308.09269) establish the same random maps, densities and position correlations, and discuss their global noncommutativity, not finite-state representations of the leading digit. Monthus (arXiv:2409.19999) supplies the exact countable-shell Markov kernel, general propagator and related first-passage transforms; the return generating function can be recovered from that stronger source and is **not** claimed as a novel independent probability law. Monthus also already observes the \(4/5\) spectral crossover for another observable. The specific added result is an exact algebraic obstruction ruling out **every** finite-state hidden Markov realization of the natural single-digit stationary process despite its full binary support; the published sources inspected do not state or directly imply that representation-class conclusion without a separate rationality/rank argument. Related existing Pelikan investigations and relevant mathematical-record queries did not reveal that conclusion. Residual risk: an unindexed older symbolic-process treatment might have made an equivalent finite-state obstruction explicit; same-source resolvent formulas do encode much of the return-time mathematics.

## Mathematical value

**PASS.** A random interval map with two elementary branches and an exact countable-shell Markov extension could conceivably admit a finite-state symbolic factor. The natural first-bit observation does not: the theorem establishes an infinite-rank obstruction that rules out all exact finite-order Markov and finite hidden-state stochastic descriptions simultaneously, although every binary word is possible. This separates topological symbolic simplicity from intrinsic metric-process complexity and determines a concrete boundary for finite-state reductions of this canonical intermittent model. The sharp return-time regimes give independent operational manifestations of the hidden depth distribution. No claim is made about finite-precision implementations or quenched path laws.

## Closest literature and remaining risk

The principal closeness is the exact time-Laplace shell propagator and first-passage analysis in Monthus (2024), Section IV and Appendix A: it already covers the underlying probability mechanism; no novelty is attributed to its kernel or to the mere existence of the \(4/5\) threshold. Yan et al. (2023), Sections II–IV, consider position autocorrelations rather than a finite-state generator criterion. The critical new comparison is that neither inspected source gives an algebraic nonrationality argument for first-symbol gap law **as a finite hidden-state impossibility theorem**. Earlier work could contain that conceptual observation without searchable phrasing, so independent priority verification is appropriate.

## Limitations

The theorem assumes the annealed stationary absolutely continuous law with uniform conditional density on dyadic shells and \(1/2<p<1\). The deterministic endpoint \(p=1\) is excluded, the critical point has no such finite invariant density, and no universal crossover asymptotic across \(p=4/5\) is claimed. These are self-review assessments and not independent certification.

Self-review: passed. Independent audit: not yet performed.
