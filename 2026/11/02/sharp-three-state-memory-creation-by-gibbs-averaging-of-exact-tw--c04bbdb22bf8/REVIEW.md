# Scientific review

## Correctness — PASS

The statement is exact, with finite-state domains, every positive integer time, and both sharp endpoints specified. The proof reconstructs the trace/determinant characterization of two-step stationarity on the centered two-dimensional subspace, checks the full three-parameter stochastic parameterization, obtains a necessary AND sufficient nonnegativity condition, and supplies an explicit realizing family. The scalar projection identity gives all powers and exact distances. Independent algebraic cross-checks within the supplied standalone Python script passed 3,714 exact assertions, including 48 positive rational examples. The substantive infinite-quantifier step is the closed-form inequality argument, not exhaustive enumeration.

Scientific risk: symbolic verification is not independent proof certification. Its successful tests cannot rule out an unnoticed expository or algebraic error; the complete derivation is provided for direct checking.

## Originality — PASS (provisional historical priority)

The motivating Choi--Wang 2026 paper, arXiv:2610.39239v1, proves its all-time Frobenius comparison explicitly for reversible chains. Inspection of its Sections 2--4, particularly Theorem 4.1 and the self-adjointness step in the proof, shows that the positive-power statement does not directly cover a nonreversible, nonzero nilpotent example. The predecessor by Choi--Lim--Wang, arXiv:2512.13067v2, Section 3 / Proposition 3.2, likewise explicitly assumes self-adjointness in its spectral-gap comparison. Related literature and mathematical-record searches on finite-time mixing, stochastic square roots, nilpotent transition kernels, group averaging, lumping, and two-block Gibbs compression identified no result stating or implying this sharp three-state interval. One-step compression identities and partition reduction are already known and expressly not claimed as new.

Residual risk: a classical stochastic-matrix theorem may imply the exact extremal interval under an alternative parametrization; database search does not prove novelty. No independent historical-priority audit has occurred.

## Mathematical value — PASS

This is a motivated structural boundary of a freshly proved reversible mixing-improvement theorem. It does more than exhibit a single failure: it characterizes all possible residual eigenvalues for the smallest eligible state space, proves the optimum at every time, constructs strictly positive examples attaining every interior rate, identifies boundary witnesses, and explains why two states are immune. Sharp finite-time distance constants are intrinsic invariants relevant to sampling and block-averaging design, rather than arbitrarily chosen entries or cheap normalization checks.

Scope risk: the theorem's sharpness is only for the fixed partition type and uniform three-state two-step mixers, not general nonreversible chains.

Self-review: passed. Independent audit: not yet performed.
