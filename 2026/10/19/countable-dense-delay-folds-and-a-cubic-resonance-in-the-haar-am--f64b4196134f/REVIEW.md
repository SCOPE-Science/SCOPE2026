# Scientific review

## Correctness — PASS

The precise domain is the real narrowband Haar self-ambiguity transform, with strictly overlapping positive delay \(0<\tau<2\), and multiplicity in the real frequency at fixed delay. Direct signed-interval integration gives the stated sine formula. The double-root equations imply the sharp \(r=2\) multiplicity boundary; the exact factorization handles triple and zero-frequency cases. Nonzero \(F_r\) and \(F_{TT}\) establish nondegenerate folds, prevent joint nodal singularities, and prove countability. The density proof uses an irrational linear flow on the two-torus and stability of a nondegenerate zero of a two-equation system; its Jacobian is explicitly nonzero. Finite high-precision checks from `CHECKER.py` support, but do not replace, the unrestricted proof.

## Originality — PASS, with residual risk

The overlap identity and classical ambiguity framework are not claimed as new. The inspected portions of Bonami–Garrigós–Jaming (arXiv:math/0509031v1, introduction and pulse-type Section 4), Jaming (HAL hal-00080459, statement of principal zero-free and uncertainty theorems), and Flandrin (the definition, general identities and waveform discussion) have different claims and do not imply the countable-dense fold-delay theorem. The first treats phase-retrieval partners and uniqueness of pulse signals; the second gives zero-free neighborhoods and moment estimates; the third surveys ambiguity-function properties. Searches of published mathematical findings under Haar ambiguity, Doppler-fold, two-sine double-root, and alternative pulse terminology found no statement with stronger coverage. An obscure exponential-polynomial or radar waveform null-pattern treatment remains possible; searching does not prove publication priority.

## Mathematical value — PASS

The core invariant is the set of delay values where a Doppler-frequency null loses simplicity. For the simplest signed-pulse waveform, it has the structurally surprising property of being simultaneously countable and dense below an exact threshold, with a unique cubic resonance at that threshold, while the full two-dimensional real nodal locus stays regular. The result is not a computation at selected parameters: it is a complete multiplicity and fold-stratification theorem with a global density mechanism. It separates high-frequency ill-conditioning of Doppler-null tracking from genuine singularities of the joint ambiguity map, a distinction relevant to exact delay-Doppler waveform analysis.

## Limitations

No claim is made about stability under smoothing the discontinuous Haar signal, finite-frequency practical resolution, or exhaustive enumeration of all fold delays. No independent audit or priority certification has been performed.

Self-review: passed. Independent audit: not yet performed.
