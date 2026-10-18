# Review of the centrally lossy-chain impurity result

## Correctness
PASS. The dissipative imaginary-part identity forces each real eigenvector to vanish at the lossy center. The unaffected half-chain fixes its allowed energy, while the rank-one determinant evaluated at that energy gives a necessary and sufficient nodal condition for exact survival, yielding the gcd count for every nonzero real detuning. The parity-resolved bright block is invertible at each unperturbed odd-mode energy; its exact optical resolvent identity and elementary second-order perturbation produce the explicit linewidth. Direct finite-matrix checks and symbolic small-size calculations independently test constants and normalization. These computations supplement, rather than replace, the proof.

## Originality
PASS on the targeted published-literature and prior-claim comparisons, with residual priority risk. Dutta and Cooper's 2020 central-loss paper recognizes reflection-odd loss-free modes and discusses generic symmetry-breaking and first-order steady-state robustness, but does not establish the all-amplitude gcd survival count or the explicit one-particle quadratic imaginary-eigenvalue coefficient. Their 2020/2021 arbitrary-drive paper analyzes different steady-state observables and geometric resonances rather than this impurity-width classification. Other compared published findings concern different Hamiltonian or spectral objects; none of the inspected result statements implies both new claims. General matrix perturbation theory supplies a method, not this evaluated arithmetic and quartic-position law. Uninspected equivalent formulations remain possible.

## Value
PASS. Exact decoherence-free-mode survival under site-selective fabrication error is a natural design question for centrally dissipative arrays. The \(\gcd\) criterion produces a sharp distinction between defect positions that remove every protected mode and positions that preserve a calculable subspace at arbitrarily large defect amplitudes. For unprotected modes, a fully explicit quadratic linewidth shows the precise dependence on mode index, location, hopping, and loss strength, including unexpectedly quartic suppression at near-nodes and fixed-rate linearity in \(\gamma\). It provides a nontrivial quantitative boundary to the previously qualitative robustness statements.

## Scope and risks
This is the one-excitation no-jump spectrum, not a full bosonic many-body Lindbladian gap. The perturbation expansion is nonuniform as the dissipation rate tends to zero or infinity. A wider literature inspection or independent mathematical audit may revise the novelty assessment. Numerical tests alone do not establish arbitrary-size assertions.

Self-review: passed. Independent audit: not yet performed.
