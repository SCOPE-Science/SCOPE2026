# Independent mathematical audit

## correctness

PASS

The density equals the stationary probability that consecutive windows choose different two-mer positions, determined by exactly w+2 bits. Independently enumerated all 24 strict priority orders for every width 2≤w≤9, all 2^(w+2) contexts. After p=u/(1+2u), every order comparison against A has nonnegative integer coefficients for w≤8 and all but B,C at w9; zero polynomials give 4 ties at w2, A,A′ only for w3..8. Independently recovered A weight counts (1,2,10,37,85,127,127,85,37,11,3,1), B (1,2,11,38,77,109,131,126,84,36,9,1), dA−dB=p²(p−1)H(p), and C−B=p(1−p)^10>0. Transforming H via p=u/(1+2u) gives coefficient signs ++++---++ (two changes); exact rational signs in (257/1000,258/1000) and (346/1000,347/1000) show two simple roots by Descartes and IVT. Exactly eight optimal orders at p=1/2 attain 263/1024; bit-complement determines p>1/2. This is an exhaustive finite combinatorial certificate proving all real p through polynomial inequalities, not a mere finite-p sample.

## originality

PASS

Shur Theorem11 is directly relevant and stronger in window range, but optimizes only uniform random-string density; its equality at p=1/2 is acknowledged as old. Zheng dissertation charged-context expectation also explicitly uniform and its dataset-specific optimization is a different distribution. The 24-priority all-real-p phase switches at w9 do not follow from these uniform theorems.

## value

PASS

Locates the first bias-driven bifurcation of a natural globally optimal minimizer ordering with exact algebraic boundaries and equality cases. This answers a structural sensitivity question that uniform-source analyses cannot detect; small absolute density gains do not erase the value of the phase-change classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
