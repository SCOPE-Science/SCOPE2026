# Independent mathematical audit

## correctness

PASS

On the budget simplex the trace inverse on 1-perp gives n tr(L+) and diverges when the algebraic connectivity tends to zero. Its second directional derivative is strictly positive for every nonzero symmetric Laplacian direction (trace of a nonzero positive semidefinite square against a positive definite matrix). The simple-edge weights map injectively to Laplacians; the connected domain is convex. Thus the unique optimizer must respect the two edge orbits. Independently diagonalizing on core zero-sum, peripheral zero-sum and part-constant subspaces gives ra+sb (r−1), rb (s−1), nb (1). In x=ra+sb the linear budget is (r−1)x/2+s(r+1)b/2=B. Minimizing A/x+D/b gives x/b=H by Cauchy–Schwarz when feasible; otherwise the unique optimum is x=sb (the other endpoint b=0 has infinite objective). The inequality for H>s is strictly monotone in s with opposite strict signs at s=r,r+1. The resulting substitution yields both value branches, including a=b at s=1. Spot checks at B=1 give 11+6√2 for (r,s)=(2,2), with positive core weight, and 46 for (2,3), with zero core weight. Inspected verify_split.py and the finite recorded output without executing the supplied script; the proof, not the sampled asymmetric comparisons, establishes global uniqueness.

## originality

PASS

General resistance minimization, uniqueness and use of edge orbits are prior; the finding supported here is the particular exact positive-weight solution, integer deletion boundary and minimum for all complete split sizes. The same-day clique-book result is a real conductance-design overlap in mechanism, not equivalent family coverage. Fixed unit weights and walk optimization on the same underlying graph are not this objective or feasible region.

## value

PASS

An exact solution of a standard electrical-network design objective on a natural graph family is independently useful: it determines when all edges in an existing orbit should be removed, and identifies the unique allocation and its cost without solving a numerical program. The sharp one-vertex change across s=r and s=r+1 is not supplied by generic convexity, by knowing the optimum is orbit-constant, or by the unit-weight index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
