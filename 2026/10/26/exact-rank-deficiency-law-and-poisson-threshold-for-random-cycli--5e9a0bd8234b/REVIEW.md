# Independent mathematical audit

## correctness

PASS

C PASS: Each selected reachability column is a standard basis vector, so rank equals number of covered coordinates. At each residue s modulo n, the q independent binary choices aggregate to independent Bin(q,1/2) count C_s. A coordinate s is missing exactly if C_s=q and C_(s−r)=0, with marginal probability p=4^-q. Two missing-coordinate events sharing a binomial variable conflict exactly when their residues differ by ±r; nonadjacent sets have product probability p^j. Therefore expanding z^X yields the independence polynomial of g disjoint cycles of length d=n/g, with length-two interpreted as K2. The classic cycle count d/(d−j) binom(d−j,j), quadratic-root formula and q=1 evaluation J_d(−1/4)=2^(1−d) give all exact finite laws and 2^g shortest-horizon schedules. The bounded-degree conflict graph eliminates O_k(n^(k−1)) of n^k ordered distinct k-tuples, proving uniform factorial-moment Poisson convergence when np->lambda>0; union bound handles lambda=0, variance<=np and Chebyshev handle np diverging. Independent exhaustive direct schedule enumeration vs polynomial coefficient combinatorics passed 66 cases including d=2; finite checks are corroboration not asymptotic proof.

## originality

PASS

O PASS qualified: cycle independence polynomial, probability generating functions, occupancy limits and factorial-moment Poisson methods are classical. The asserted new synthesis is the exact distribution of rank loss for a constrained random actuator schedule, the arithmetic gcd-dependent shortest-horizon count, and uniform critical window. Prior actuator-scheduling work treats algorithmically designed or rank-guaranteed schedules with different sampling; published general occupancy limits could subsume the convergence statement, but not the exact finite PGF without identifying this conflict graph.

## value

PASS

V PASS: Rank deficiency and full controllability probability under pointwise-sparse random actuation are natural design benchmarks. The exact all-n, all-r distribution and an offset-uniform Poisson crossover near n log_4 n give useful quantitative information beyond guaranteed feasibility; the nontrivial gcd dependence at shortest horizon is meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
