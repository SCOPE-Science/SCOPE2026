# Independent mathematical audit

## correctness

PASS

An entrance appending i requires that the overlap contain exactly the other types and the outgoing draw differ from i, giving the factor p_i(1-p_i). For coverage, condition on positions reserved for a pair and on the remaining letters; the conditional chance of both pair symbols, for K≥2 reserved positions, strictly increases on balancing an unequal positive pair, with positive probability of a configuration covering the other symbols. For flux at M=n,n+1, permutations and one duplicated type give the two stated products; for M=n+1 balancing increases z(C−2z) on 0<z≤s²/4, with C≥s² for fixed sum s. Boundary vectors have zero flux. In the binary case the displayed derivative numerator starts at 1, ends at 0, and its derivative strictly changes sign once from minus to plus for k≥3, giving exactly one interior maximizer on the half interval. At M=4 the maximum is at pq=1/6; for large k the root is between 1/(k+1) and 2/(k+1) and its equation gives (k+1)t_k→1. Independently reconstructed the curvature: with r=n−1, the contributions from differentiating p_i(1−p_i) twice and from the mixed terms give −2B and −2(r−1)LB/r, after scaling by n^L; the latter uses r H_{r,r−1}(L−1)=B. Fixing two overlap slots occupied by a perturbed letter leaves H_{r,r−1}; using both perturbed letters leaves H_{r,r−2} with opposite sign. Summing gives r L(L−1)[r H_{r,r−1}−(r−1)H_{r,r−2}]. Its eventual positive leading term is (r/n)^L L²/r before scaling; permutation symmetry makes this direction certify the tangent Hessian, while n=2 follows separately. The choice p_1=1/M gives the stated lower bound by its i=1 term; uniform overlap conditioning gives the upper bound. Inspected proof and exact finite checker without executing the packaged code; the infinite conclusions do not depend on sample checks.

## originality

PASS

The supported distinction is variational: optimality over the sampling simplex, including the exact binary threshold and eventual all-alphabet local reversal. Uniform flux is directly prior, and coverage maximization is a comparator, not the distinctive claim. Later indexed findings overlap and in places strengthen the result; the later records checked do not establish a prior independent covering theorem.

## value

PASS

Shows that maximizing time spent in coverage and maximizing the frequency of entering it have different solutions for the same model. The exact binary threshold and optimum, together with eventual local reversal and exponential separation for every fixed alphabet, give a useful baseline for nonuniform sliding-window analysis without asserting a nonuniform waiting-time result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
