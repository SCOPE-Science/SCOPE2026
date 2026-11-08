# Independent mathematical audit

## correctness

PASS

For finite S, strictly positive destination law pi and positive survival k bounded below, the positive Feller operator K_tau has the exact product Feynman-Kac path representation under iid destination marks. Finite Gibbs duality and entropy chain rule give the upper bound via marginal averaging: each generated coordinate contributes total coefficient <=1, and old-history coefficient fraction b_n=E[min(T+1,n)]/n tends to zero by Cesaro for EVERY lag distribution, without moment assumptions. Jensen yields log norm(K_tau^n)/n<=max_q{log(m(q)+kmax b_n)-D(q||pi)}, hence r<=B=max_q m(q)e^{-D}. A product-q tilted law lower bounds log r by E_q log(sum tau_i k(X_i))-D(q||pi), with the prehistory error vanishing by the same b_n. Variance exactly Var_q(k)sum tau_i² and Taylor log curvature >=-1/kmin² yields the quantitative lower envelope at the unique strict-concavity optimizer q*. Point-mass tau=delta_L yields independent eventually generated factors and spectral radius m(pi). The two-state finite transfer tests agree for four distributions, including both point masses; no finite computation supplies the universal heavy-tail claim.

## originality

PASS

Best-of-knowledge PASS. Bertoin and Minchev arXiv:2605.29030 discuss preferential relocations and explicitly pose a universal upper Perron-tilt envelope after Corollary 5.2. Their dispersion lower-bound result does not settle a pointwise upper bound for every memory law; the present proof answers it in the strictly positive rank-one subclass with a quantitative collision lower envelope and arbitrary heavy tails. Bertoin 2025 provides a weaker bound; his 2026 uniform-ancestor process uses generation-dependent ancestry, not a fixed lag law. Direct application of their statements does not supply this theorem.

## value

PASS

A mathematically motivated partial solution of a documented general open spectral-rate question in a structurally important rank-one case. It gives both a universal sharp upper envelope and a quantitative collision-probability stability estimate, separates arbitrarily remote concentrated lag from truly dispersed memory, and requires no tail restrictions. This is a structural result, not recomputation of a known constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
