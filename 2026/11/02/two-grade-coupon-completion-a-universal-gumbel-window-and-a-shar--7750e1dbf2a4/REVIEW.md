# Independent mathematical audit

## correctness

PASS

For n even and m=m_n→∞ with n/2 types needing m coupons and n/2 needing m+1, Poisson thinning turns the two rescaled group completion times into independent Gamma(m,1) and Gamma(m+1,1) maxima. Their exact CDFs are (1−Q_m(u))^(n/2),(1−Q_(m+1)(u))^(n/2); center u_n uniquely solves (n/2)(Q_m+Q_(m+1))=1, scale b_n=u_n/(u_n−m). The density Mills bounds with error m/(u_n−m)^2→0 (Gamma CLT implies u_n−m≫√m) give Q_j(u_n+xb_n)/Q_j(u_n)→exp(−x) for both j. Thus Gumbel limit without restriction on growth of m. The Poisson-clock de-Poissonization is valid uniformly because u_n/b_n² <= 2 log n+O(1), bounding count fluctuations versus n b_n. Tail ratio Q_(m+1)/Q_m ~u_n/m and Gamma rate function I(r)=r−1−log r prove the three last-class competition regimes: r∞=1, r0=∞, finite alpha: I(r)=1/alpha, winner probability r/(1+r). Checked independent finite numerical gamma tails/center, ratio and group maximum CDF in four regimes, including m≫n; these illustrate, not prove, asymptotic conclusions. The alpha=0 joint CDF has an escaping coordinate, correctly not claimed as R² weak convergence.

## originality

PASS

Qualified best-of-knowledge PASS: Russell May (2008) gives an arbitrary-quota finite exact generating function—this broad model coverage is explicitly acknowledged but does not state the growing-quota n→∞ last-group crossover. Long (2026) treats evolving single quota and varying arrival rates, not two adjacent quotas assigned to equal-sized groups; Castro–Marinho gives the homogeneous growing-quota Gumbel law, not the winner phase diagram. The combination may be implicit in generic nonidentically distributed Gamma-maxima extreme-value theory; no novelty certification.

## value

PASS

A one-copy quota difference is the minimal natural heterogeneity in coupon collection, yet produces a nontrivial sharp crossover in the identity of the last finishing group at m~log n while the total completion stays universally Gumbel. Explicit last-class probabilities and joint class maxima quantify a motivated reliability/coverage bottleneck rather than merely recomputing a finite coupon formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
