# Independent mathematical audit

## correctness

PASS

Independently expanded diag(1−2p)+ppᵀ on Σp=1 to obtain det M=2p₁p₂p₃; the Gram identity gives positivity. On p₃=0 the first 2×2 block is the outer product of (p₂,p₁) and the third eigenvalue is 1, so even at the axes rank is two. The row sums 1−pᵢ give λmax≤1 and λmin≥det M. Off fixed axis caps, the second-largest |uᵢ| has a positive lower bound, so the small-eigenvalue event is confined to O(√t)-width coordinate bands. In a cap parameterized by (x,y), the two large eigenvalues are 1+O(ρ²) by the entrywise perturbation bound, and λmin/(2x²y²)=1+O(ρ²). Bounding the disk by two squares gives area 4a log(1/a)+Oρ(a) for |xy|<a. With a=√(t/2), area density tending to 1/(4π), and six caps, the resulting coefficient is 3/(π√2). The condition-number event has the same cap asymptotic because λmax tends uniformly to 1 there; the complement is again lower order. Integration gives the moment cutoff, including divergence at equality (the truncated critical moment grows as a squared logarithm). The determinant moment follows by integrating the Dirichlet(1/2,1/2,1/2) density. Reviewed frozen proof and finite verification evidence; no uploaded scripts executed.

## originality

PASS

Best-of-knowledge pass for the sharp Haar spectral/conditioning laws. The normal-equation matrix is published, and the determinant moment is a Dirichlet beta integral once its polynomial is known; neither is the basis of the originality pass. The closest matrix and random-tail comparisons do not cover the sharp eigenvalue or condition-number statement.

## value

PASS

This is a natural small-dimensional normal-equation matrix from a published tangent solve, not an arbitrary random Gram example. The sharp logarithmic term isolates intersecting rank-loss loci rather than merely locating singular directions, and the infinite mean despite almost-sure invertibility is relevant to amplification in the intermediate solve. The result does not claim the full tangent projector or final covariance is ill-conditioned.

The dated certificate retains the supplied scientific assessment, sources and limitations.
