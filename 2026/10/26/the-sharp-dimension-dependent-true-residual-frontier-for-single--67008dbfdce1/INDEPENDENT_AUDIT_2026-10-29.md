# Independent mathematical audit

## correctness

PASS

For real SPD A with mu I<=A<=L I in n>=2, a one-dimensional, nonoversampled, DEIM-selected GMRES step uses a largest-magnitude coordinate i and alpha=r_i/(Ar)_i for nonzero sampled denominator. For u=r/||r||, c=|u_i|>=n^-1/2, s=(1-c^2)^1/2, Au=a u+v, p=||v|| and h=w^T v, exact ratio squared=(s^2h^2+c^2p^2)/(ca+sh)^2. The matrix inequality (A-mu I)(LI-A)>=0 gives p/a<=q=(kappa-1)/(2sqrt(kappa)). Thus the maximum is sqrt(n)q/(1-sqrt(n-1)q) for q below the pole; a rank-one SPD two-direction construction attains it. At/above the pole a sequence of nonsingular sampled scalars tends to 0 and gives unbounded residual, with arbitrarily near unique pivots. Hence universal nonexpansion iff q<=sqrt(n)-sqrt(n-1). Independently evaluated the rank-one extremizer for four (n,mu,L) cases and verified ratio matches exact formula; inspected source verification code and exact n=2 rational example. q=0, ties, c=1, and singular-limit interpretation explicitly handled.

## originality

PASS

The one-row bound arises from the classical Kantorovich angular estimate, which is correctly treated as prior work, combined with the DEIM data-dependent maximum-coordinate pivot. Bergermann Algorithms 4.1 and 5.2 specify the underlying deterministic DEIM sketch, not the exact dimension-dependent Euclidean true-residual supremum. Randomized subspace-embedding GMRES and flexible stabilization require different assumptions and do not establish this unoversampled sharp pole. Best-of-knowledge new sharp minimax formula and exact nonexpansion boundary.

## value

PASS

Provides an exact sharp finite/unbounded instability frontier for a natural deterministic sketching algorithm even with SPD systems. It separates convergence guarantees for full GMRES from true residual spikes of one sampled row and gives a concrete dimension/conditioning design boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
