# Independent mathematical audit

## correctness

PASS

For every integer n>=2, hopping J>0 and terminal jump rate gamma>0, no-jump generator K=-iH-gamma P0/2 has all eigenvalues in the strictly left half-plane: any imaginary-axis eigenvector must have zero amplitude at site 0 and propagates by nearest-neighbor eigenvector recurrence to zero everywhere. Therefore absorption is certain and the unique Hermitian Gramian X solves K^*X+XK=-I. Reconstructing the proposed parity-resolved kernel X_rs=(n-max(r,s))[(min(r,s)+1)/gamma+gamma*min(r,s)/(4J^2)] for equal parity and i*sign(s-r)(n-max(r,s))/(2J) for unequal parity gives the Lyapunov commutator and correct absorbing/right-end boundary terms; exact all-n algebra underlies the proof. Its diagonal gives E_jT=(n-j)((j+1)/gamma+gamma*j/(4J^2)), and strict A/gamma+C*gamma minimization yields gamma_j=2J*sqrt((j+1)/j) for j>=1, whereas j=0 is n/gamma decreasing; tracing X/n gives uniform-initial-state expression. Independent SciPy continuous Lyapunov solves on 16 systems (n=2..9, two positive parameter pairs) matched the entire kernel with maximum absolute discrepancy 2.05e-12. Numerical bounds corroborate rather than imply the uniform identity.

## originality

PASS

PASS is for the explicit all-size endpoint-absorber Gramian and the source-localized optimum independent of remote chain size. Chia-Paterek-Kwek had the general quantum-jump moment resolvent framework; a formal inverse superoperator includes the observable but no inspected closed all-size path inversion. Varbanov-Krovi-Brun analyze Poisson-driven projective first detection, a different generator. The more recent Riberi endpoint imaginary-potential model uses a semi-infinite chain and permits incomplete absorption, not the finite-path exact mean. This is not new generic jump statistics. The tight-binding Ranjith-Kumar paper was not read in full and path-specific historical formulas remain possible.

## value

PASS

The closed full matrix X computes coherent initial-state first-jump means without a dimension-growing Liouvillian solve, including previously hidden off-diagonal coherence contributions. The exact optimal loss for a particle placed j sites from the sink is independent of additional remote sites although the mean is proportional to n-j, whereas the uniform mixture has a different length-dependent optimum. This is a natural, reusable quantitative transport/Zeno benchmark, not a trivial evaluation of one fixed small graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
