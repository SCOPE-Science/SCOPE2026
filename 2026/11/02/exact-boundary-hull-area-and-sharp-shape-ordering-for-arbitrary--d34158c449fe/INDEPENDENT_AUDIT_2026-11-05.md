# Independent mathematical audit

## correctness

PASS

For n≥3 arclength-uniform iid boundary samples from a nondegenerate triangle with side proportions p_i>0, p_i<1/2, sum=1, condition on multinomial side occupancies m. Independent uniform-order statistics give expected corner missing area from each occupied side as 1/((m_j+1)(m_k+1)). Summing gives an exact trinomial expectation; integrate reciprocal counts using x^m to derive Q_n=1−[1−Σ(1−p_i)^(n+2)+Σp_i^(n+2)]/[(n+1)(n+2)∏p_i]. Triple finite difference yields 1−Q_n=n E[(Σp_i U_i)^(n−1)]. For n≥3, strict convexity under nontrivial coordinate averaging gives Schur-convex missing area, maximizing Q uniquely at p=(1/3,1/3,1/3) and minimizing Q in the limit p→(1/2,1/2,0). The fixed-p quadratic missing-area limit and triangular-degeneration nq_n→τ limit follow by exponential decay and dominated convergence. Independently checked exact multinomial expectation against formula for 21 (p,n) cases across n=3..9, including near-degenerate proportions. This is an all-n proof not an extrapolation of numerical tests.

## originality

PASS

Best-of-knowledge qualified PASS. The closest Reitzner–Schütt–Werner work gives general simple-polytope boundary-sampling asymptotics, not the closed finite-n three-side expression, strict all-shape Schur order, sharp equality/infimum or nq_n crossover. Interior-sampling Efron-type random hull results have a different sampling measure. Other historical polygon boundary sampling calculations might contain the specialized triangle formula; retain risk.

## value

PASS

PASS. The theorem classifies the entire natural family of triangles and every n≥3, with a strict optimal shape, unattained degenerate extremal and quantified transition from n^-2 to n^-1 missing-area scales. Sharp shape ordering and singular asymptotics are meaningful beyond an isolated numerical coefficient or known fixed-shape rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
