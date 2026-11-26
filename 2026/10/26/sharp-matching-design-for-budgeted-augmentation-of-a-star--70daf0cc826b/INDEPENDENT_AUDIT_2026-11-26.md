# Independent mathematical audit

## correctness

PASS

The star Laplacian has the constants, the hub-against-leaves vector and the leaf-zero-sum space as mutually orthogonal eigenspaces with eigenvalues 0, n+1 and 1. The added Laplacian vanishes on the first two and has trace 2T and rank at most k on the last. Padding with zeros, the improvement is the sum of f(mu)=mu/(1+mu) at k spectral values. Jensen and strict monotonicity in T give the optimum and require T=W and mu_i=2W/k for every i. Thus exactly k edges are positive and the incidence Gram matrix must be (2W/k)I: its diagonals require equal weights and its off-diagonals force disjointness. Such a matching exists by 2k<=n, including n=2. The curvature lower bound for -f on [0,2W] gives an objective deficit at least the spectral squared deviation divided by (1+2W)^3. The latter squared deviation is the squared Frobenius deviation of the Gram matrix even when rank is deficient; its diagonals give 4 times the weight variance sum, and the two orientations of each off-diagonal give twice the stated overlap sum. Multiplying by n+1 gives the stated Kirchhoff index.

## originality

PASS

The general joint cardinality-and-budget problem and the unweighted one-added-edge case have documented coverage. The supported distinct finding is the complete uniform-star solution for variable W and all admissible k, including every extremizer and the explicit quantitative gap. The strongest general formulation inspected uses optimization and approximation machinery, not a theorem that can be specialized directly to this closed form.

## value

PASS

A hub-and-spoke network with sparse new links and fixed conductance resources is a natural instance of a nonconvex design problem. The solution specifies when the continuous budget and the combinatorial optimum can be realized simultaneously, and turns strict inequality into a directly interpretable penalty for support overlap and unequal weights. This is useful beyond the known one-unit-link calculation or restating the general design objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
