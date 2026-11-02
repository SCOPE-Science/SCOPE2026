# Independent mathematical audit

## correctness

PASS

With the orthonormal basis z^k/sqrt(k!) the diagonal entries of any positive sampler are positive mixtures b_j exp(-t_j)t_j^k/k!. Every truncated Poisson string has l1/l-infinity width at most 3e sqrt(N+1), including t>N, so summing A<=L_k<=B over k gives r_N>=A sqrt(N+1)/(3eB) with no angular hypothesis. For the constructive radii j=0..ceil(sqrt N), M=N+1 root-of-unity angular sites diagonalize the complete sampling Gram operator. The eigenvalue lambda_k=sum_j(2j+1)p_{j^2}(k) is >1/5 by a nearest-square-root node and a Stirling/Poisson large-deviation inequality, and <8 by the Gaussian envelope exp(-(j-sqrt(k))^2) integrated over unit intervals. The one-point center term is correct at k=0. The theorem asserts radius order, not optimality of total sample sites or sharp constants. Independent check: An independently written Poisson-eigenvalue implementation evaluated every diagonal eigenvalue for N=1,2,3,9,16,57,100,302,1024 and all observed values remained in [0.2,8]; the all-N proof is the separate analytic bound, not these finite checks. The exact full Git RESULT.md, checker.py identity, metadata and tree were inspected.

## originality

PASS

The paired universal lower bound for arbitrary positive discrete point samplers and explicit O(sqrt N)-radius angularly discrete construction is not logically implied by known infinite-dimensional sampling trajectories or general MZ sampling theorems, as inspected. Prior concentric-circle sampling is explicitly acknowledged; literature search cannot certify first priority, especially early radial Gauss-Laguerre discretization.

## value

PASS

Stable positive polynomial sampling has two distinct costs, angular sites and number of independent radii. The lower bound proves no amount of angular oversampling can replace the intrinsic radial budget; the matched construction identifies the correct order and gives a concrete uniform algorithm. This is a motivated design law for finite Gaussian/Hermite-Gabor polynomial subspaces.

The dated certificate retains the supplied scientific assessment, sources and limitations.
