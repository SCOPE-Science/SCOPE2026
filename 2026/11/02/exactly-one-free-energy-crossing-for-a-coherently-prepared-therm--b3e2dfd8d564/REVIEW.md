# Scientific review: uniqueness of the thermal-qubit free-energy crossing

## Correctness — PASS
The two-jump Davies generator gives longitudinal decay \(e^{-\Gamma t}\) and transverse decay \(e^{-\Gamma t/2}\). The exact squared-Bloch-radius gap is \((R-z)(R+z+2b)p(1-p)\). An integral formula for the binary-entropy difference reduces the normalized free-energy difference to a positive quadratic-resolvent integral. Its derivative has a strictly negative numerator bounded by \(-[1-s^2R^2]\), so the normalized free-energy difference is strictly monotone. Opposite endpoint signs prove exactly one crossing for positive coherence. The diagonal and maximally mixed boundaries are treated separately. Symbolic identities and an independently implemented two-by-two Lindblad semigroup agree for mixed and pure inputs. Finite diagnostics are not substituted for the global proof.

## Originality — PASS, qualified
The closest source is Moroder et al., arXiv:2403.16959 (2024): its main-text single-qubit example and Appendix A give the exact population-inversion construction and demonstrate a crossing, but do not supply its global uniqueness, normalization monotonicity, or asymptotic coefficient. Summer et al., arXiv:2507.16976 (2025), reuse the Davies qubit and plot crossover times for Rényi divergences without giving this all-state theorem. Chatterjee et al., arXiv:2311.01347 (2023), describe observed single relative-entropy crossings for a distinct driven dissipative qubit. Mathematical-record searches using model, observable, equality and monotonicity aliases found no direct covering finding. General qubit entropy calculus may allow an independent derivation, so publication priority requires further examination.

## Mathematical value — PASS
For a natural, experimentally motivated thermal Davies model and an established coherent-to-inverted-state preparation, the result settles exactly how many thermodynamic crossings occur for every admissible initial state. This rules out reentrant free-energy orderings in the precise model, identifies a sharp coherence/no-coherence boundary and provides a useful monotonic quantity and quantitative late-time tail. It strengthens qualitative existence and example plots into a global dynamical classification, not a numerical fit.

## Limitations and nearest literature
The result needs a faithful Gibbs state, exactly the two energy-exchange jumps and a comparison chosen by maximal inversion. Pure dephasing, non-Davies dynamics, alternative comparators and multilevel systems are not covered. The exact crossing time is determined implicitly. Publication-priority risk includes unindexed specialized theorems on the generalized amplitude-damping channel and qubit relative-entropy ordering.

Self-review: passed. Independent audit: not yet performed.
