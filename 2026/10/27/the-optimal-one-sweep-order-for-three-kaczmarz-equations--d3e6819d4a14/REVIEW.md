# Independent mathematical audit

## correctness

PASS

For the ordered normals with correlations a,b,c, trace(M^T M)=a^2+c^2+(b-ac)^2 by inserting the last rank-one loss after the first two projections. The exterior square of each plane projection is the rank-one projection on its normal, so the exterior-square product is ac u_k u_i^T. Its squared Frobenius norm yields the product p=a^2 c^2 of the two possibly nonzero squared singular values (zero ranks included). Thus the sum is Q+p and the product p. The sweep is strictly contractive by norm equality for orthogonal projections and independence of the three normals. With 0<Q<1 the feasible p range is contained in [0,(1-sqrt(1-Q))^2]; implicit differentiation shows the larger root decreases strictly since its derivative is (lambda_+-1)/sqrt((Q+p)^2-4p), with the endpoint handled by continuity. Ordering by the largest adjacent product covers zeros and ties; all-orthogonal sweeps vanish. Trace(M)=a^2+b^2+c^2-abc and trace of the exterior square is abc; cyclic shifts and transpose reversal also independently show the six spectra agree. The quadratic identity yields lambda_+<=Q, and lambda_+>= (Q+p)/2>Q/2 for p>0; for p=0 and Q>0 one has lambda_+=Q. For the independent star family in the record the endpoints have 2t^2 and the middle order has t^2+O(t^3), which proves the sharp nonattained sqrt(2) supremum. Inspected check.py without executing it: its invariants are rational, but its separate numerical ordering tests use approximations and do not establish strict monotonicity.

## originality

PASS

Credit the exact Gram-based sweep operator to prior work and the order-invariant spectrum to elementary cyclic-permutation and transpose identities. The supported distinct claim is the exact one-sweep minimizer for arbitrary independent triples, including ties, together with the sharp global comparison of best and worst orders on the same instance. The literature and catalogue statements inspected do not give that comparison or a stronger order-selection theorem that yields it as a special case.

## value

PASS

The least-sized nonsingular setting in which a sweep has genuinely different ordering choices has an exact worst-direction optimizer that need not follow conventional low-coherence heuristics. The equality of eigenvalues explains why spectral-radius analysis misses this initial effect, and the sharp ratio quantifies the maximum benefit of changing the order on one instance. This has value for the explicitly motivated one-sweep objective, not as a general recommendation for asymptotic convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
