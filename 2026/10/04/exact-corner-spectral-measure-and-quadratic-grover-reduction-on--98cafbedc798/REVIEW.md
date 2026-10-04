# Same-model scientific review

## Correctness
PASS. The quantified statement is proved from the exact four-state matrix. Direct substitution gives eigenvalues \(0,p,2-p,2\); weighted normalization gives the corner masses \(a_p,b_p,b_p,a_p\). Tensor-product spectral resolution proves the independent-sum law. The sign-pair parametrization proves the \((d+1)^2\) bound and irrational-parameter equality. Cyclic spectral projections prove invariance under the rank-one oracle and inclusion of the constant ground state. The checker is an exact-arithmetic regression test and is not used as a substitute for the proof.

## Originality
PASS, with residual terminology risk. The motivating paper gives the source matrix, product construction, generic Green function and \(d=5\) numerical study, but not the four-atom corner measure or the quadratic cyclic reduction. The inspected spectral-decimation paper concerns edge-substitution operators, while the inspected spatial-search paper treats standard undirected Hamming and related distance-regular graphs. Targeted searches for corner spectral measures, Cartesian-product cyclic subspaces, weighted hypercubic Grover reductions and equivalent Green-function formulas found no statement covering this weighted family and conclusion.

## Value
PASS. The source studies a \(1024\)-state \(d=5\) corner-target problem numerically and motivates varying the dimension and non-homogeneity parameter. The exact reduction replaces the ambient \(4^d\) state space by at most \((d+1)^2\) active spectral states, and by exactly \(4d+1\) states in the homogeneous case. This is a structural simplification of the source's main numerical object, not an arbitrary finite invariant.

## Closest literature and limitations
The closest inspected sources are arXiv:2207.01686, arXiv:2201.05693 and arXiv:2204.04355. Generic Kronecker-sum and cyclic-subspace theory provide ingredients, so an equivalent abstract statement may exist under tensor-product Krylov or association-scheme terminology. No claim is made about the optimal search parameter, optimal time, or quantum speedup.

Same-model review: passed. Independent audit: not yet performed.
