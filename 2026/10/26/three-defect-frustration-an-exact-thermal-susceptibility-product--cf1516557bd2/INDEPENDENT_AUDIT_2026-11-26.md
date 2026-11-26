# Independent mathematical audit

## correctness

PASS

Let u_i=ε_i σ_i σ_(i+1). In the frustrated sector the joint law of u is independent bond spins of mean t conditioned on product −1; each allowed edge configuration has two preimages. For an arc of length d the conditional mean of its u-product is (t^d−t^(n−d))/(1−t^n). After a seam gauge, the physical pair sign flips exactly on pairs between the middle block and either outside block. For two consecutive blocks of lengths u,v the forward distance distribution is symmetric under d→u+v−d, so the complementary-arc sum is t^w times the forward sum, where w=n−u−v; the forward sum is t(1−t^u)(1−t^v)/(1−t)^2. This verifies both factors of the two-interface correction and the baseline from the unweighted seam pairs. Strict concavity of log(1−t^u) on positive u gives strict Schur convexity up to permutations, not a total order on incomparable triples. The least and most majorized feasible triples are balanced and (1,1,n−2); n=3,4 have only one placement type. Taking the limit at t=1 yields (n²+2)/(3n)−8abc/n², where log u gives the same strict ordering, and the quoted extreme expansions and ninefold limit follow. At t=0 the ordering degenerates; at a fixed finite β the positive factor β leaves placement comparisons unchanged, but the stated zero-temperature limit is for X, not βX. Read the frozen checker without executing it. `python3 /workspace/branches/independent_checks.py` (section 1) corroborates the formulas by independently grouping the exact bond ensembles by the odd number of unsatisfied bonds: 84 zero-temperature and 252 positive-temperature checks, not the universal proof.

## originality

PASS

The exact finite-ring and two-arc correlation machinery is not original. The supported distinct claim is the closed three-gap product for the uniform physical magnetization variance and its strict placement law, including the zero-temperature contrast. The strongest inspected same-day path-correlation formula covers the pair step, not the all-pairs classification. No inspected prior statement gave the full gap result; historical completeness is not claimed.

## value

PASS

Three defects are the first odd-sign sector allowing a genuine placement problem. The entire strict majorization comparison and sharp integer extremizers provide an exact geometric response law, not just values for a few rings. At zero temperature identical sign inventories can differ macroscopically in magnetization variance by a factor approaching nine, giving a concrete reason to distinguish defect placement from the net frustration sign.

The dated certificate retains the supplied scientific assessment, sources and limitations.
