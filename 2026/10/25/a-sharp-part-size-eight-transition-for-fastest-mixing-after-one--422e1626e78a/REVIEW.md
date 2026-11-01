# Independent mathematical audit

## correctness

PASS

Averaging over the defective K_{n,n} graph automorphism group is valid because SLEM=||P-J/(2n)||2 is convex. Edge orbits reduce to two weights x,y. Exact invariant subspaces give eigenvalues 1-nx, the two eigenvalues of a 2x2 antisymmetric block M, and d=1-x-(n-1)y with multiplicity 2n-4. The block column lower bound g(x)>=1/sqrt(n) is attained through n=7 with y=(2-nx)/(2(n-1)). For n>=8 the smaller root of the specified quadratic yields g(x)=d=(n-2)x/2; an explicit nonnegative convex combination of the active eigenvalue gradients vanishes, certifying the global convex minimum. Independently built the full 2n x 2n matrices for n=3,4,6,7,8,9,10,20,30; their SLEM matches the formula to 1.7e-15 and five high-regime subgradient residuals vanish to numerical precision. The asymptotic 4/(9n²) edge-loss penalty follows by Taylor expansion, not finite testing.

## originality

PASS

Boyd, Diaconis and Xiao (2004) and Boyd, Diaconis, Parrilo and Xiao (2007/2009) develop the exact SLEM/SDP formulation and give the intact complete bipartite graph formula. The symmetry paper also treats two complete cliques connected by a bridge, which is the complement of the defective biclique, but its off-diagonal support constraint is the opposite graph and does not preserve fastest-mixing SDP. The inspected published paper does not imply the all-n two-parameter defective-biclique optimum or transition at n=8. General numerical SDP solvability cannot substitute for the exact closed-form family; best-of-knowledge residual unknown edge-failure formulas.

## value

PASS

Deleting one allowed link from an extremally symmetric graph is a canonical robustness question for fastest mixing. The exact global optimum, transition at part size eight and leading spectral failure penalty quantify how one edge changes optimizer structure, beyond an arbitrary small finite case or a reproduction of the intact graph answer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
