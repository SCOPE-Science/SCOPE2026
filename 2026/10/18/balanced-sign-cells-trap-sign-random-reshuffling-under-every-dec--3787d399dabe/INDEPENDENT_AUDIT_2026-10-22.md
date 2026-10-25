# Independent mathematical audit

## correctness

PASS

In the fixed sign cell each coordinate has at most p positive and p negative component signs; every permutation prefix sum has absolute value at most p. Abel summation for an epoch with nonincreasing gamma bounds its displacement by p(gamma_nt-gamma_{n(t+1)}). Telescoping over all epochs gives total variation <=p gamma_0, and weighted within-epoch displacement <=p gamma_nt. The closed radius-2p gamma_0 ball stays in U, bootstrapping the assumption and proving convergence of *all* iterates, with endpoint distance <=p gamma_0; p=0 gives fixed trajectory. For f1=(x-5)^2/2, f2=(x+5)^2/2 at x0=2 and gamma0=1, the sign cell (-5,5) contains [0,4] and each limit lies in [1,3], hence |F'(limit)|>=1 and objective gap>=1/2. Uniform independent permutations give an absolutely convergent Rademacher series with harmonic variance pi^2/6-2 log2. Independently recomputed 40 harmonic increments and their variance 0.2586393863 toward 0.2586397057; finite checks corroborate but telescoping proves the infinite result.

## originality

PASS

PASS on the *quantified all-permutation and all-positive-nonincreasing-vanishing-stepsize trapping theorem* and its exact random-series law; qualitative smooth/strongly-convex SignRR nonconvergence was established earlier and is not new. Qin–Liu–Xu Proposition 3.5 already provides a strongly convex failure under one schedule; their result does not quantify every permutation/schedule or the harmonic limiting variance. Broader signSGD failures are known; no covering statement found in the inspected mathematical comparisons. An equivalent older cancellation/trapping theorem remains possible.

## value

PASS

The gap is operationally meaningful: nonzero error terms or a single counterexample schedule do not establish robust failure under every diminishing schedule and every reshuffling order. The balanced-sign structural lemma supplies a portable failure criterion even under Robbins–Monro nonsummable square-summable steps, and the limiting variance isolates the randomized order effect. No larger performance theory is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
