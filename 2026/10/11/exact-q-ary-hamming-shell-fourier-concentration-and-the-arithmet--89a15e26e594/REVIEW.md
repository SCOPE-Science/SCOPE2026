# Independent mathematical audit

## correctness

PASS

PASS: With normalized characters for q>=3, n>=2 and 1<=k<=n-1, decompose each one-coordinate Fourier space into its normalized occupancy indicator u_i=(1_{x_i !=0}-p)/sqrt[p(1-p)] and transverse (q-2)-space. Conditioned on a uniformly random shell point, indicators form uniform k-subset, covariance is hypergeometric, transverse directions have conditional squared norm a/p. The conditional Gram has R=1+n(a-p)^2/[p(1-p)] (one), U=na(1-a)/[(n-1)p(1-p)] (n-1), T=a/p (n(q-2)), plus one zero; multiplying by shell mass w gives the full spectrum. Unique zero direction is sum 1_{x_i!=0}-k. Let z=qk-(q-1)n; independent SymPy simplification verifies R-T=z(z-1)/(n(q-1)), R-U=(z-1)(z+q-1)/[(n-1)(q-1)], T-U=qk(z-1)/[n(n-1)(q-1)]. Hence all positive eigenvalues agree iff z=1, i.e. n≡1 mod q and k=((q-1)n+1)/q. Independent construction and Hermitian eigendecomposition of full character Gram was checked for q=3,4,5, n=3, k=1,2 (6 examples); this corroborates, but the covariance calculation proves all n,q.

## originality

PASS

PASS best of knowledge: multivariate Krawtchouk and Hamming relative-design results use related harmonic tools but generally occupancy/symmetric polynomial spaces or binary combinatorial tight designs, rather than the full unsymmetrized first Fourier band restricted to a single nonbinary Hamming shell. The exact wR,wU,wT,0 spectrum and integer tightness congruence are not found as a covered statement in the inspected primary sources; remains possible an association-scheme representation theorem entails the formula, as acknowledged.

## value

PASS

PASS: Exact singular-value spectrum and complete arithmetic classification of when the shell restriction becomes a tight frame after its necessary one-dimensional quotient are natural finite harmonic-analysis sampling invariants. A researcher studying shell sampling or stable reconstruction needs precisely the nonzero singular values and the congruence condition; this goes beyond standard shell cardinality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
