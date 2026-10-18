# Independent mathematical audit

## correctness

PASS

In row sum/difference orthobasis the random update has diagonal entries 1-alpha p and 1-alpha r and off-diagonal -alpha sqrt(pr) xi with E xi=0, E xi^2=1/q. This closes expected squared-coordinate moments under the symmetric nonnegative T with entries ((1-alpha p)^2, alpha^2 pr/q, (1-alpha r)^2). Every nonzero deterministic initial squared-coordinate vector pairs strictly positively with the Perron eigenvector, making rho(T) necessary/sufficient. Independent exact-rational evaluations confirmed det(I-T)=alpha^2 pr[4-2alpha+alpha^2 pr(1-q^-2)] across c=1/3,3/5,5/13 and q=1,2,3,6, and confirmed the growth-but-convergence witness q=2,c=3/5,alpha=9/4: one-step gain 209/200 and det(I-T)=3483/40000. The two principal minors prove the global boundary. Mean-square rate is a strictly convex simple top eigenvalue; derivative sign changes between alpha=1 and alpha=2 give unique optimizer, with a perturbative Schur expansion as c approaches 1 giving the stated sqrt(1-c) coefficient. Finite evaluations supplement analytic exactness.

## originality

PASS

Moorman et al define the same simultaneous averaged RK update; their theorem/corollary give a ONE-STEP spectral error guarantee, and its optimizer targets that guarantee. The inspected full author-hosted 2019 version does not give the two-row exact infinite-time Perron stability frontier, including stable transient expansion. Resultary hits concern cyclic Kaczmarz and greedy/coherence Kaczmarz, not the same independent uniform minibatch covariance. The general stochastic linear-system literature is broad; a spectral mean-square specialization remains possible but not demonstrated.

## value

PASS

The sharp strict gap between guaranteed stepwise monotonicity and true long-run mean-square stability is a structural quantitative boundary for simultaneous row averaging; the exact rate optimizer and fixed-q near-coincident-row asymptotic are useful for tuning and for understanding transient amplification in a natural minimal correlated system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
