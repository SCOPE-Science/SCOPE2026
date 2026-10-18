# Independent mathematical audit

## correctness

PASS

Every Rademacher column has exactly one of the orthogonal projective lines s_+=(1,1)/sqrt(2), s_-=(1,-1)/sqrt(2); both observed => Y rank two and post-truncation optimal error b². All columns of one line, each event probability 2^-l, give rank-one errors b²+(a²-b²)rho(1-c)/(c+rho(1-c)) or the swapped expression. With rho=(b/a)^(4q+2), summation proves the exact all-q,all-l law. Strict concavity of g(t)=t/(rho+(1-rho)t) proves extrema. At c=0/1 a sign line is exactly trailing right singular, so even q->infinity leaves excess (a²-b²)/2^l. Independently enumerated sign-line scenarios and extremal rational matrices; verified sample A=[[2,1],[1,2]], l=2 has mean squared error 3. Distinct singular values and exact range-revealing convention are essential.

## originality

PASS

Published randomized subspace-iteration theory already covers Gaussian or general non-Gaussian error bounds and rank-revealing method but not the exact rank-two rank-one-truncated Rademacher orientation distribution and nonvanishing worst-frame omission atom. The novelty is not the observation that discrete sketches can be rank deficient; it is the full exact expected risk and optimizing geometry.

## value

PASS

The obstruction shows why more power steps cannot substitute for sampling additional independent sign vectors in worst orientation, even for the smallest invertible sketching instance. The exact relative-risk necessary/sufficient width criterion is a mathematically motivated boundary for a prominent algorithmic approximation class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
