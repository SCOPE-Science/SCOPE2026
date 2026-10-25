# Independent mathematical audit

## correctness

PASS

For uniform admissible N-prefixes of X={x in {0,1}^N: x_j x_(2j)=0}, unique dyadic decomposition j=2^r i with odd i splits configurations into independent length L_i(N)=1+floor(log2(N/i)) golden-mean chains. Chain log-PF recurrence Z0=1,Z1=1+exp(t),Zk=Z(k-1)+exp(t) Z(k-2) yields exact first two moments. Since d_k(N)=N/2^(k+1)+O(1), convergent series define alpha~0.366541662066731 and sigma²~0.148936034454920>1/16, with mean alpha N+O(log²N), variance sigma² N+O(log³N). Independent-chain triangular-array Lindeberg, with max chain length O(log N), establishes the asserted normal law. Perron–Frobenius ratios give fixed-cylinder local Markov limit with initial (1/phi,1/phi²) and transition [[phi^-1,phi^-2],[1,0]]; its almost-sure digit density beta=2/(4+sqrt5)~0.320714913 follows q_(r+1)=phi^-2(1-q_r) and independent-chain Hoeffding. The bound sum_i L_i²<=6N yields TV>=1−4exp(−(alpha−beta)² N/48) for sufficiently large N, proving local and bulk separation. Independently enumerated legal words N=5,10,14 (20,288,2880 words) and checked series and moment recurrences. Finite cases are corroboration, not CLT/TV proof.

## originality

PASS

Kenyon–Peres–Solomyak already study the multiplicative golden mean shift, independent dyadic-chain decomposition and dimension/the variational principle, and Peres–Solomyak special infinite product measures. The newly assessed law compares UNIFORM finite-prefix ensembles to their distinct boundary-biased local limit, proves quantitative global total variation separation, and gives a Gaussian digit-count CLT with explicit mean/variance series. The dimension formulas alone do not imply this pair of measure-specific probabilistic limits. Risk remains of a generic multiplicative shift CLT or boundary ensemble theorem that implicitly specializes.

## value

PASS

The observable discrepancy between local weak convergence and exponentially maximal growing-volume total variation in a canonical multiplicative subshift is a mathematically substantive boundary-versus-bulk phenomenon; the explicit Gaussian density and variance describe natural finite-volume digit statistics, beyond classical Hausdorff dimension of the same space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
