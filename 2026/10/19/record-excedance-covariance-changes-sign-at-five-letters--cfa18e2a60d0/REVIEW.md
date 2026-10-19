# Scientific review

## Correctness — PASS

For a fixed prefix size, the record event depends only on relative order; conditioning on it turns the last prefix value into the maximum of a uniform unordered subset. The remaining prefix positions are symmetric among the nonmaximum values. This supplies a fully evaluated mixed record/threshold covariance for every index and threshold; future values depend on the subset, not its relative order, so they are independent of the record event. Summation produces the excedance-position profile and the aggregate reciprocal-binomial covariance. Elementary Pascal identities imply its recurrence and strict sign threshold. The `verify.py` program exhaustively checks permutations through eight letters and additional exact finite-algebra formulas through order 399. The unrestricted proof is combinatorial/algebraic, not extrapolated from the verifier.

## Originality — PASS (provisional historical priority)

Gnedin (2006) studies record statistics of permutations; Ehrenborg–Steingrímsson (2000) counts permutations with prescribed excedance sets; Brändén–Claesson (2011) expands both statistics into mesh-pattern occurrences; and Baril (2012/2013) explicitly treats record and weak-excedance sets under a bijection. Primary text sections of each were examined. Their relevant claims concern marginal enumeration, general expansions, and bijective preservation, rather than evaluated threshold-position cross-covariances and a strict covariance sign reversal at order five. A general joint generating function might imply these formulas without stating them. That residual risk is material but no directly dominating published claim was identified in the inspected sources and index comparisons. The novelty claim is limited to the evaluated mixed kernel, profile, and transition.

## Mathematical value — PASS

Record counts and excedance counts are classical, natural statistics encoding distinct features of random rankings. Their covariance changes sign at an unexpectedly low finite dimension despite an entirely monotone-in-order aggregate dependence profile. The exact threshold kernel explains the source of the reversal through cancellation of a single negative initial position and positive later contributions. The result also quantifies a striking separation between asymptotically vanishing correlation and positive limiting covariance. It is a complete finite-order dependence theorem, not a computation for an arbitrary slice.

## Limitations and priority risk

The law must be uniform, and only second-order dependence is classified. Published joint enumerators for related permutation statistics may yield the result implicitly; exhaustive historical priority is not independently established. Verification is finite, whereas the theorem follows from its unrestricted proof.

Self-review: passed. Independent audit: not yet performed.
