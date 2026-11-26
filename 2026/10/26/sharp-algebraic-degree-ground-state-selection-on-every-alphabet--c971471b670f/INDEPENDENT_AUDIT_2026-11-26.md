# Independent mathematical audit

## correctness

PASS

The restricted adjacency I+K is primitive by the directed N-cycle and the self-loops. Maximizing invariant measures are all mixtures of the N fixed Dirac measures, not just the N extremal ones. K has exactly the two intersecting simple cycles, so det(I−zK)=1−z^(N−1)−z^N. The positive right and left vectors in RESULT.md satisfy the eigen-equations by rho^N=rho+1. Their entrywise product is 1 except at the exceptional vertex where it is rho^(−N); normalizing gives the stated p and all finite-temperature vertex masses, since I+exp(−beta)K has the same eigenvectors. The Perron transition law is (1−a)I+aQ with a=q rho/(1+q rho), q=exp(−beta). Constant cylinders converge to p and nonconstant cylinders have mass at most their number of transitions times a. The exceptional mass u recovers rho by (u^(-1)−N)/(N−1), hence has degree N by Selmer's irreducibility theorem. The inspected Jenkinson–Pollicott Corollary has bound equal to the number of length-one cylinders for range two, exactly N here. Since (P_beta−I)/q tends to rho(Q−I), the corresponding matrix powers converge to the exponential and give stationary finite-dimensional distributions, not a path-space assertion. Replay: RESULT.md lines 18–74 and the cited irreducibility theorem; verify.py and VERIFICATION.md report finite samples and were not executed.

## originality

PASS

The supported contribution is the explicit saturation of the degree bound for every N>=3 subject to exactly two energies and all extremal maximizing measures fixed, with the full finite-temperature law. Neither the classical graph, its companion polynomial, Selmer's theorem, nor Perron normalization is claimed as new. The strongest inspected earlier fixed-point selection example has smaller degree and more energy values, and the same-polynomial catalogue match solves a different pressure-transition problem.

## value

PASS

This provides a sharp witness to a general algebraic bound in a restrictive class where finite-temperature marginals alone hide the concentration on fixed ground states. It turns a possibility allowed by the bound into an explicit maximal-degree example at each alphabet size, and makes the rare-jump dynamics computable without an asymptotic selection algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
