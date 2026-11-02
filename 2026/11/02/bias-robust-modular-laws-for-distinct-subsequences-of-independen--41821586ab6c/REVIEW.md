# Scientific review

## Correctness — PASS

The fully specified recurrence \((X,Y)\mapsto(X+Y,Y)\) or \((X,X+Y)\) with \(X=1+c_0,Y=1+c_1\) implies that the number of **nonempty** patterns is \(X+Y-2\). This normalization was checked directly against literal distinct-subsequence sets; all residue formulas therefore use \(r+2\), not the empty-inclusive offset. Positive coprime lifts and subtractive Euclidean reachability establish strong connectivity of primitive residue pairs for every modulus, not only the finite tested moduli. The self-loop at \((1,0)\) gives an exact common path length and valid Doeblin bound for arbitrary independent inhomogeneous source biases. The arithmetic count follows from inclusion-exclusion of common prime divisors.

Independent finite checks enumerate 8191 binary strings and verify the recurrence; construct all primitive graphs and exact modular fibers for 23 moduli; and compare exact rational source-word enumeration with finite-state DP in 45 distinct \((m,n)\) test combinations. Infinite coverage depends on the written proof, not extrapolation.

## Originality — PASS, with risk

Reznick's 2006 full text proves the equal-probability Stern-pair residue limit: the fair-source specialization is covered, not novel. Żak's 2022 full text gives the coprime-pair/subsequence connection, and weighted-source expected counts appear in Biers-Ariel, Godbole and Kelley (2017). None of these inspected works was found to claim a modulus-uniform quantitative convergence law valid simultaneously for every **nonidentically distributed** independent binary source with a common ellipticity lower bound. Four semantic literature-index searches returned results on universality indices, distinct substring expectations, and other modular Bernoulli problems, without a logical implication for the new source/class/invariant theorem. The distinguishing assertion is precisely bias-schedule robustness with an explicit finite-modulus rate, not fair-source equidistribution nor generic Markov minorization. Residual risk: a general theorem about varying products of Stern/Calkin–Wilf transition kernels or finite doubly-stochastic random walks might imply this result, and the quantitative method is elementary once its primitive state space has been identified.

## Mathematical value — PASS

The count of *distinct* subsequence patterns is a natural string-complexity statistic, but its arithmetic residues are nonuniform for a structural reason. The theorem exhibits and quantifies a bias-invariance principle that survives deterministic changes of the source distribution at each coordinate; it gives exact arithmetic limiting masses at all moduli and a concrete boundary showing independence alone does not guarantee convergence. The result supplies a reusable finite-state technique for symbolic sources, rather than an arbitrary small table or a mere restatement of the known fair-source count.

## Scope and risks

The rate is conservative, no optimal exponent is claimed, and independence and a fixed positive lower bound on letter probabilities are assumed. Classical fair-source modulo results and the general minorization method are excluded from the novelty claim. An unindexed stronger theorem remains a meaningful coverage risk. Exact finite checks do not substitute for the infinite proof.

Self-review: passed. Independent audit: not yet performed.
