# Self-review: sharp relaxed-gossip sampling frontier

## Correctness — PASS

The two random protocols are encoded by exact Gram matrices, with the four equally likely independent sequences and the two equally likely permutations explicitly enumerated. The operator difference admits an exact orthogonal decomposition into the bisectors of the two unit edge normals, giving eigenvalues \(d_\pm=\omega^2(2-\omega)(1-c^2)[2-\omega(1\pm c)]/4\). For \(0<c<1\) and \(0<\omega<2\), the negative-to-positive transition of \(d_+\) occurs precisely at \(\omega=2/(1+c)\), while \(d_-\) remains positive. The path normals have \(c=1/2\); the rational counterexample follows by direct multiplication. The shipped code replayed successfully with 45 exact symbolic/rational checks, but the universal theorem is established analytically, not by tests. The excluded reflection endpoint \(\omega=2\) is expressly treated as a degeneracy.

## Originality — PASS, with residual risk

The original block-gossip work of Haddock, Jarman and Yap (2021) develops independent block selection and convergence theory; its inspected model does not state this two-step, pointwise, without-versus-with-replacement threshold. Recht and Ré (2012, Section 3.1 and Appendix B) establish a two-factor operator-norm comparison for positive-semidefinite matrices, not the full quadratic-form Loewner ranking, and their PSD assumptions fail when relaxed projection factors acquire negative eigenvalues above \(\omega=1\). De Sa (2020) constructs other failures of matrix reshuffling inequalities, but does not give this two-edge exact angular frontier. Ferreira, Acebrón and Monteiro (2024) discuss sampling-without-replacement Kaczmarz experiments but not this direction-dependent boundary. The chief residual risk is equivalent specialized work under projection ordering, randomized gossip or relaxation terminology. These differences concern statements and implications, not merely titles or numerical parameters.

## Value — PASS

The finding provides a complete, angle-sensitive, sharp directional ranking for two equal-cost sampling policies on the smallest connected gossip graph. It separates the often-favorable policy of using every edge once from pointwise reliability under nonexpansive overrelaxed updates, including exact initial states that reverse the ranking. This supplies a precise stress-test for claims that reshuffling must help every initial consensus error. It is not a claim about asymptotic execution time, longer epochs or optimal stochastic control; those remain unproved.

## Limits and closest literature

The comparison is restricted to two communications, one common relaxation, uniform independent selection versus a uniform random permutation, and squared Euclidean disagreement. The exact eigenvalue formula has a more general two-normal interpretation; it does not cover all network topologies or arbitrary scheduling correlations. The closest primary literature includes Recht and Ré (2012), De Sa (2020), Haddock et al. (2021), and Ferreira et al. (2024). Relevant results were compared at the level of operators, risk functionals, assumptions and quantifiers. Independent external priority review has not occurred.

Self-review: passed. Independent audit: not yet performed.
