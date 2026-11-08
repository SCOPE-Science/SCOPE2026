# Independent mathematical audit

## correctness

PASS

The exact multinomial factorial moments give normalized coincidence R_{m,n} and Cov=E[X_r]E[X_s](R−1). Cancellation yields a strictly decreasing-in-n exact ratio R_{m,n+1}/R_{m,n}=m(m−2)/(m−1)^2 (1+rs/((n+1)(n+1−r−s))), which makes the positive n-set one contiguous finite interval. Uniform fixed-r,s expansion on compact t=n/m>0 gives logR=F(t)/m+G(t)/m²+O(m⁻³), F=−t+(r+s−1)−rs/t, G=−2t+[3(r+s)−1]/2−rs(r+s−1)/(2t²). For r=a²,s=(a+1)², lambda=a(a+1), the double-root identity F=−(t−lambda)²/t and G(lambda)=1 yield m²logR→1−z²/lambda, and E[X_r]E[X_s]/m²→exp(−2lambda)lambda^(r+s)/(r!s!). The signed limits on either side of ±sqrt(lambda) and one-interval property trap endpoints lambda m±sqrt(lambda m)+o(sqrt m). Independently checked symbolic G(lambda)=1, direct exact multinomial enumeration across 12 (m,n) pairs totaling 584260 allocations, 680 exact one-step recurrences, and 45 80-digit finite-scaling approximations. These bound/finite checks support, not replace, the proof for arbitrary fixed a,m→∞. The theorem correctly leaves z=±sqrt(lambda) signs open and excludes a growing with m.

## originality

PASS

Best-of-knowledge statement/implication comparison found the classical factorial moments and known sparse/infinite-box occupancy frequency results, but no identified theorem yielding the fixed-density consecutive-square double-zero m^{-2} expansion with order-one signed profile and sharp sqrt(m) covariance-window endpoints. Full inspected published Resultary records instead treat Cov(occupied richness,X_r) and covariance/precision of nonempty-box indicators. General exact mixed-factorial moments can make the argument short, so historical priority remains provisional, particularly older finite-urn expansions and a 2013 factorial-cumulant treatment.

## value

PASS

The discriminant degeneracy (r+s−1)²=4rs has a natural exact-integer classification: r and s must be consecutive positive squares, making the parameter family canonical rather than arbitrary. It produces a genuinely unresolved leading-covariance double zero in an intrinsically important occupancy frequency statistic. The new signed order-one limit and sharp sqrt(m)-width sign window resolve the natural critical region that first-order asymptotics cannot determine. The result is useful in dependence and frequency-count calculations without requiring any broader general theorem or paper-sized extension; not merely another log-concavity observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
