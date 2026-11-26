# Independent mathematical audit

## correctness

PASS

This pass is for /workspace/repairs/4/RESULT.md. The exact cluster formula was correct, but the frozen Finding's unqualified lift of the lower envelope is false as a strict claim: b1=2, b2=3 have irrational log ratio, yet m_3<m_2. The corrected claim gives the exact criterion. In fact L'_b=alpha(1-1/b-log b)/(b-1)^2<0 and x^alpha exp(-x) is increasing for x<alpha, hence m_b decreases strictly with b. For the core proof, orthogonality gives the supremum over source data as the maximum of the positive weights f_k=b^(-alpha k)exp(-n b^(-k)), which tend to zero. The ratio f_(k+1)/f_k is at least one exactly when n b^(-k)>=b L_b, so the floor index stated in the theorem maximizes, including the boundary tie when n b^(-k)=L_b and k>0. The phase endpoints agree by (b-1)L_b=alpha log b; L_b<alpha<bL_b makes the interior maximum unique and both endpoints minima. Nearest integers to L_b b^(j+t) realize every limiting phase modulo one. For the direct sum the norm is the larger component norm. To replay density on the two-torus, fix the first logarithmic phase by choosing real times log n=log L_b1+(j+u1)log b1 before rounding; the second phase changes by the irrational rotation log b1/log b2 and visits each neighborhood at arbitrarily large positive j. Rounding n to an integer perturbs log n by o(1). The torus is compact and connected, so the continuous maximum has a full interval as range, with minimum max(m_b1,m_b2) achieved by setting both phases at their minima and maximum M_alpha achieved by maximizing either one. Dominated convergence of the diagonal terms proves strong stability, but the operator norm stays one because the eigenvalues approach one. All small enough vectors have bounded forward orbits by contractivity, so this gives asymptotic expansivity without its uniform version under the cited definitions. The packaged numerical checks were read, not executed, and do not establish infinite-dimensional optimization or density.

## originality

PASS

For the repaired claim, credit the exact geometric-grid profile, its dependence on arbitrary alpha and the incommensurate two-ladder cluster interval; do not credit generic spectral functional calculus, qualitative expansivity, or the alpha=1 one-ladder asymptotic as an unrelated phenomenon to the nearby Ritt result. The correction to strict lift follows by elementary monotonicity and is not a novelty claim.

## value

PASS

The natural fractional source ball quantifies precisely where smoothness restores uniform convergence lost on the full unit ball. The full cluster set is stronger than a decay rate or a uniform bound: it distinguishes improved lower-envelope behavior from unchanged upper behavior and resolves whether optimizing on two ladders can align their minima at arbitrarily large integer times. The repaired strict-lift criterion keeps this interpretation valid for either order of the two ratios.

The dated certificate retains the supplied scientific assessment, sources and limitations.
