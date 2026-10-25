# Independent mathematical audit

## correctness

PASS

For a fixed real (p0,q0) in (0,1)^2, the finite-state chain has stationary distribution pi=( (1-q)/(2-p-q), (1-p)/(2-p-q) ) and second eigenvalue p+q-1 of modulus below one. The cited full-middle lemma identifies the limiting sign probabilities with limits of finite fringe-score probabilities F_K. For each finite K these are rational functions of p,q. On a sufficiently small complex polydisk about the real point, all transition and stationary factors are nonzero and their ratios to the real base-point factors are bounded by e^epsilon, while stationary ratios are bounded by 2. The finite-energy bound delta=m^8/8 for one or two coordinates, conditioned on all others, gives P(Delta_K != Delta_(K-1))<=3(1-delta)^floor((K+1)/2), since a changed increment requires at least one of the three relevant sums to be missing. The complex weight comparison then gives |F_K-F_(K-1)|<=12 exp(2 epsilon K)(1-delta)^floor((K+1)/2). Choosing epsilon < -1/4 log(1-delta) makes this geometric. Local uniform convergence of rational holomorphic F_K yields a holomorphic extension near each real point, hence real analyticity of each limit. The stored finite verifier checks only selected values; it is not used for the infinite analytic conclusion.

## originality

PASS

The 2026 Markov-MSTD paper proves existence and positivity of limiting sign probabilities by the fringe-middle method but does not establish analytic dependence; the full text contains no analytic/complex-parameter argument. Do et al. prove continuity for a different pair-of-correlated-sets model and explicitly leave further analytic properties open. The present result proves real analyticity for the stationary self-correlated two-state Markov model using local complex uniform convergence. Resultary searches returned no exact analytic theorem.

## value

PASS

Real analyticity is a meaningful regularity upgrade for a natural two-parameter stochastic-combinatorial limit and directly supports future derivative and local-parameter analysis of MSTD, difference-dominant and balanced probabilities. The result supplies a substantive local complex-convergence argument beyond numerical estimates or the known existence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
