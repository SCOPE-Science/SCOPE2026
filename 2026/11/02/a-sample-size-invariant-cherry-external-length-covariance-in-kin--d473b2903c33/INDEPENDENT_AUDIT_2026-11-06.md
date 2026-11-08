# Independent mathematical audit

## correctness

PASS

Under pair-merger rate one per unordered lineage pair, holding times T_k are independent Exp(binomial(k,2)), independent of merger topology, so L_n=Sum S_k T_k. Direct survival probabilities for r specified tips give E(S_k)_r=(k)_r(k-1)_r/(n-1)_r for r=1,2,3; a joint reward recurrence for cherries A_k and S_k gives E[C_n S_k] and subtracting (n/3) E[S_k] yields the claimed negative quartic profile -k(k-1)(n-k)(n-k-1)/[3(n-1)(n-2)(n-3)]. Summing with means 2/[k(k-1)] gives Cov(C_n,L_n)=-2/9 for every n>=4; n=2,3 cherries are constant, covariance zero. Independently enumerated all ranked merger histories (n=4:18, n=5:180, n=6:2700) and computed levelwise covariance exactly using rational arithmetic; all matched. The universal result is proved by factorial moments and finite sum, not by checking up to a sample size. For pair rate lambda the covariance scales -2/(9lambda).

## originality

PASS

McKenzie–Steel supplies a distribution and marginal moments of cherry counts; Dahmer–Kersting and Janson–Kersting supply external branch-length and surviving-lineage statistics; none of these marginal facts by itself implies their exact joint covariance or its remarkable n-independent value. Alimpiev–Rosenberg analyzes covariances among branch lengths, not this particular cherry-count/topology mixed covariance. Frost–Volz treats phylogenetic cherries and dynamic rates but full article sections were not fully inspected, so a possible mixed-moment implication is a named historical risk. The self-contained recurrence gives a defensible best-knowledge original result; no claim of absolute literature exhaustion.

## value

PASS

Number of cherries and external total branch length are two natural distinct summaries of genealogy, linked respectively to recent branching structure and singleton mutations. Their *exact constant negative covariance*, with stage-by-stage explanation and sharp n boundary, is an independently useful natural joint statistic even if no asymptotic theorem follows. The result is neither a mere marginal rephrasing nor an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
