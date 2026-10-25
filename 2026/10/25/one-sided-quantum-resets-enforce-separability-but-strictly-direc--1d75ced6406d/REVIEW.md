# Mathematical review

## Correctness

**PASS.** The Lindblad generator acts invariantly on five specified Pauli strings, yielding four explicit coefficient equations. Direct solution gives the stationary matrix and the strict positivity identity \(1-k^2=\Omega_1^2(r^2+\Omega_2^2)/\Delta>0\). The carré-du-champ argument with a faithful invariant state proves the adjoint kernel contains only scalars, establishing uniqueness among all states. An explicit convex product-state decomposition proves separability and zero second-party discord; noncommuting independent Pauli factors prove strictly positive first-party discord. The exact spectrum verifies the mutual-information formula. The independent finite-matrix program passed all 256 parameter samples, but no numerical experiment is used as a proof over the infinite parameter domain.

## Originality

**PASS, with bounded literature risk.** The closest primary paper [1] examines reset of both interacting spins and establishes nonzero entanglement, not a marginal-preserving reset of just one spin. Global resetting in a noninteracting spin ensemble [2] and discrete-time full resetting [3] do not imply this local, driven Ising stationary-state theorem. General discord zero-set characterizations are prior mathematical tools [4]; their use alone is not claimed as new. Semantic comparisons of similar Gibbs-state, Ising-dephasing and Bell-diagonal discord results concern distinct generators or equilibrium objects. Residual risk: an equivalent selective-erasure fixed point could appear in unindexed quantum master-equation literature.

## Value

**PASS.** This determines the qualitative quantum-correlation fate of a physically meaningful modification of an established entanglement-generating reset protocol for **every** nondegenerate coupling, drive and reset rate. The sharp directional distinction is more than a positivity or normalization check: selective erasure forbids all stationary entanglement while retaining strictly one-way nonclassical correlations and positive mutual information. The closed form, explicit separable decomposition, and global uniqueness together allow precise model comparison.

## Limitations

The model is a two-qubit ideal selective-reset process with nonzero couplings and finite Poisson rate; it does not address other Hamiltonians, reset channels, transients or experimental imperfections. Literature indexing is incomplete. This review does not constitute independent validation.

Self-review: passed. Independent audit: not yet performed.
