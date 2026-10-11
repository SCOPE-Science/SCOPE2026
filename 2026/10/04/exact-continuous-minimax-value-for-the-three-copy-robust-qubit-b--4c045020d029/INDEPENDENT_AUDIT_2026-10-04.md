# Independent mathematical audit

## correctness

PASS

Both three-copy states lie in the four-dimensional symmetric subspace, where a two-outcome POVM is represented by a Hermitian contraction \(B\) and success is \(1/2+(1/4)\operatorname{Tr}(\Delta(\theta)B)\). Averaging over the stated three-point prior gives the displayed Hermitian matrix with spectrum \(\{-\lambda,0,0,\lambda\}\), \(\lambda=\sqrt{2114}/104\); the Helstrom trace-norm bound therefore gives the global minimax upper bound \(1/2+\sqrt{2114}/208\). The proposed kernel correction preserves contraction, with eigenvalues \(-1,-4/39,4/39,1\). Direct algebra yields the success excess \(\frac{\sqrt{2114}}{219856}(1-\cos\theta)(2\cos\theta-1)(246\cos\theta+713)\), nonnegative on \(|\theta|\le\pi/3\) and zero exactly at \(0,\pm\pi/3\), matching the upper bound over the full continuum. The inspected verifier independently reconstructs the averaged matrix, kernel correction, contraction spectrum, active-point values, and numerical agreement with the closed profile; the continuum guarantee is the analytic factorization.

## originality

PASS

Fujiki--Tanaka formulate exactly the common-unitary nuisance problem and state a finite-discretization least-favorable-prior SDP with numerical binary-qubit demonstrations. The accessible primary abstract does not state a continuous analytic solution, exact algebraic value, three-point rational least-favorable prior, or closed success profile. Targeted Resultary search found no published SCOPE record covering this benchmark exactly. Full-text access to the very recent source failed through the arXiv HTML route and the authorized institutional fallback was unavailable in this run, so a specific source-access residual risk is retained rather than converted into a failure.

## value

PASS

This closes a natural continuous version of a freshly published numerical benchmark: it replaces grid-dependent evidence by an exact saddle certificate, identifies the least-favorable nuisance support and weights, and gives a closed success profile proving the global continuum guarantee. The result is narrow but strongly motivated by the source benchmark and supplies a reusable analytic test case for robust quantum discrimination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
