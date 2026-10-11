# Independent mathematical audit

## correctness

PASS

For a diagonal spatial observable, only the two-step displacements in \(W=\Lambda^{-1}SCSC\Lambda\) contribute to the commutator. Along the right maximal path the middle coin contributes \(P_+C(x+1)P_+=-b_{x+1}P_+\), while the left path contributes the corresponding \(P_-\) factor. At a fixed arrival site the two contributions land in orthogonal \(\Lambda^{-1}P_\pm\) coin subspaces, giving the upper bound by the largest \(b_{x+1}|a_{x+2}-a_x|\). Choosing a state localized at the left endpoint with the saturating coin direction kills the opposite path and attains that bound, so the seminorm identity is exact. The admissible observables are therefore precisely weighted one-Lipschitz functions on each parity graph. Standard finite-graph duality then gives the weighted shortest-path state transport formula, with edge length \(2\epsilon/b_{x+1}\). The homogeneous specialization matches the primary source exactly, and the assigned finite-matrix checker confirms the inhomogeneous edge law on periodic lattices.

## originality

PASS

The 2026 primary paper derives the homogeneous exact formula but explicitly says that the reduction breaks for spatially varying \(c(x)\); it then solves the inhomogeneous distance by finite-dimensional convex optimization at each time step. Its numerical-method appendix states that those solves are only to finite precision and do not by themselves establish global optimality. The audited commutator factorization converts that unresolved inhomogeneous convex problem into an exact weighted graph metric and transport law. Classical one-dimensional spectral-distance results make shortest paths natural once a weighted Lipschitz seminorm is known, but they do not supply the plastic-walk-specific exact commutator weights \(b_{x+1}\).

## value

PASS

The result replaces repeated numerical convex optimization in the motivating paper by an exact closed weighted-transport law for every admissible inhomogeneous profile. It identifies the precise local lattice cost \(2\epsilon/b_{x+1}\), recovers the simulated continuum line element, and gives a reusable analytical benchmark for geometry-sensitive quantum-walk spread. This is a motivated structural simplification of the model rather than a toy special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
