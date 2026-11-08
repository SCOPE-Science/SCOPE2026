# Independent mathematical audit

## correctness

PASS

On the lift to Z, visited positions form [m_t,M_t], so C_n first becomes covered precisely when its range reaches n-1; final new vertex is the newly reached end. Positive drift ensures finite attained global minimum -J, after which all large-cycle cover events are new maximum H_{n-1-J}. Gambler ruin gives P(J>=j)=(q/p)^j. The ladder increments H_b-H_{b-1} are iid with mean 1/(p-q), variance 4pq/(p-q)^3 and an exponential moment. The CLT for H_n transfers to T_n because a geometric-tight random terminal offset changes time only O_P(1). To show independence, truncate J to its finite-time minimum J_m, invoke the Markov property for the future long first passage, and let m grow after n. Independently tested cycle cover/range identity on 100 deterministic path-cycle pairs; not a proof of the infinite statement.

## originality

PASS

The source 2026 cycle-walk paper already gives finite-cycle last-vertex geometric marginals and range-based methods. The assessed contribution is an eventual all-n sample-path coupling and jointly independent Gaussian/geometric limit, not the known marginal. Older first-passage CLTs and ruin formulas are credited. Same-object full-text inaccessibility is a documented priority risk, not an inferred failure.

## value

PASS

The almost-sure shared-path stabilization is sharper than a one-dimensional weak marginal limit and couples two naturally dependent statistics. Joint asymptotic independence answers a meaningful refinement of biased cover-time theory and can be reused to analyze terminal locations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
