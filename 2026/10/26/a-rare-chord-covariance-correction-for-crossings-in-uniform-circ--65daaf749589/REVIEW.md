# Independent mathematical audit

## correctness

PASS

Reconstructed actual 8182-byte source proof for integer n>=2. Fix candidate chord e whose arcs have 2r and 2(n-1-r) interior endpoints. Condition e present and isolated: match independently within both arcs with probability p_n,r=(2r-1)!!(2n-2r-3)!!/(2n-1)!!. A crossing pair in a k-chord uniform matching has probability 1/3, hence its conditional crossing mean is (binom(r,2)+binom(n-1-r,2))/3 versus unconditional binom(n,2)/3. Difference =-[n-1+r(n-1-r)]/3. Summing over all candidate chords with precise oriented-to-unoriented multiplicity n per r proves exact EI and covariance formulas. Cyclic simple chords are r=0,n-1 with p=1/(2n-1), giving the simple Cov term; rare remaining r=1,n-2 contribute covariance -2n/[3(2n-1)] and expectation 2n/[(2n-1)(2n-3)], while p_n,r+1/p_n,r=(2r+1)/(2n-2r-3) bounds all inner tails by O(1/n) covariance and O(1/n^2) expectation. Therefore EI and Cov asymptotics and Markov J->0 probability are correct. Independently exhaustively enumerated all 3, 15, 105, 945 and 10,395 matchings for n=2..6 with exact rational arithmetic, comparing both covariance values; each agreed. Finite tests corroborate, not prove asymptotic tail estimates.

## originality

PASS

Best-of-knowledge PASS for exact mixed isolated-chord/crossing covariance and the nonzero nonsimple isolated-chord correction. Reviewed relevant original full papers on chord diagram components and crossing marginals and the 2023 simple-chord and crossing limit rate paper. Those inspected theorems give separate Poisson/normal laws and moments, not the joint covariance with all crossing-free chords. Even though the simple-chord covariance itself follows easily by conditioning, the nonsimple -1/3 constant needs an additional all-chord conditioning and tail argument.

## value

PASS

The statistic is a natural joint dependency question for random chord-intersection graphs: isolated chords form a Poisson-like fringe, and the vanishing-probability non-simple part nonetheless contributes a finite nonzero covariance with total crossings. The exact finite formula and -1/3 rare-chord correction are qualitatively invisible from separate marginal limits, providing useful quantitative information for mixed diagram statistics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
