# Independent mathematical audit

## correctness

PASS

For F(W)=||W||_F^2/2, the gradient equals W. With strict descending positive diagonal and rank r dividing m, the exact top-r left projector at t=kT is the next contiguous r-block. Unit projected-SGD annihilates those entries in one step, leaving remaining nonzero rows orthogonal to the held projector. Therefore each nonterminal block has precisely T-1 zero compact-gradient updates even while full gradient is nonzero, and the first zero matrix is W_{(m/r-1)T+1}. Inductive proof covers every K>=2, T>=2, rank r; test cases m/r=2,3,4 show exact blind indices and termination. No stochastic or Adam conclusion follows.

## originality

PASS

Best-of-knowledge: prior GaLore defines periodic top-SVD wrapper, warns about stale projectors, and later papers show stochastic nullspace failure and deterministic convergence. The deterministic unit-step diagonal staircase with T-1 exact blind steps and closed termination time is not entailed by the compared results.

## value

PASS

A fully deterministic exact obstruction on a smooth, condition-number-one objective isolates projector staleness from gradient noise and ill conditioning. The quantified refresh-delay law is a motivated algorithmic counterexample and diagnostic for stale-subspace methods, not a broad impossibility theorem. The phenomenon does not assert practical training impact or non-convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
