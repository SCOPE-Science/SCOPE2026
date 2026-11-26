# Independent mathematical audit

## correctness

PASS

Independently, set p=2a and let W_n be the walk whose up steps are bit pushes and down steps bit pops, with probabilities p,q. Under Lebesgue measure the branch itinerary is independent of the initial binary digits; inserted bits are independent fair bits conditional on the push/pop itinerary. If m_n=min(0,W_1,...,W_n), the number of original bits removed is K=-m_n and the number of inserted bits still on top is L=W_n-m_n. For each surviving original bit i counted from 1, its contribution is (1/4)2^{-(K+i)}2^{-(L+i)}; all other cross terms vanish. Thus c_n=E[2^{-K-L}]>0, including c_0=1. The nonnegative excursion series B satisfies B=1+pq z^2 B^2. Decompose a walk at first descents to new minima (each block qzB), then decompose the remaining meander ending at L by last exits from lower heights (weight B(pzB)^L). Summing with 2^{-K-L} gives B/((1-qzB/2)(1-pzB/2)). Substitution r=pzB gives precisely H_a(r). At the positive branch endpoint r=sqrt(p/q); the two denominator factors first vanish before the edge exactly when q>4p or p>4q, giving the two pole rates. Using z=r/(p+qr^2), the coefficients of (1-z/z_p)^{-1} are (1-10a)/(1-4a) and 2(5a-2)/(4a-1), respectively. At equality the remaining denominator factor is 3/4 and the vanishing factor has leading sqrt(2(1-4z/5)); B=2 there, giving the stated collision coefficient. In between, only the two branch points contribute at the radius: a positive denominator root could only have a positive real z, and neither root is attained on the principal branch before or at that edge. The signed square-root expansions give the two stated parity constants; the derivative numerators at r=±sqrt(p/q) are 48aqr, and the positive-root denominator is smaller, so neither parity cancels. Stationarity follows from the inverse-strip densities. The normalized sum converges even at neutrality by n^{-3/2}; evaluating the smaller root at z=1 gives G=2/(1-3a) or 4/(6a-1). The variance limit is (2G-1)/12, with the unique maximum 5/4 and derivatives +16 and -16 at a=1/4.

## originality

PASS

The supported distinct claim is the exact off-neutral covariance and pole–branch transition law, with its integrated variance cusp, not the known symmetry, general off-neutral exponential mixing or neutral exponent. The strongest indexed comparator exactly subsumes the covariance series and transitions, and mechanically implies the cusp, but it is cataloged after the frozen result. Earlier primary passages read do not supply that off-neutral exact law. This is a bounded assessment of prior coverage, not certification of independent discovery or firstness.

## value

PASS

The center coordinate is the observable already singled out numerically in the heterochaos literature. Its exact series exposes two thresholds away from zero drift that qualitative mixing and the neutral exponent cannot distinguish. The parity amplitudes and explicit variance cusp quantify the observable's memory in ways an upper bound cannot; the series offers a reproducible benchmark for other observables, parameter scaling and generalized branch counts. The distinct value is this parameter-dependent exact result, not the already known change from neutral to off-neutral mixing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
