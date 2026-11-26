# Independent mathematical audit

## correctness

PASS

Condition on uv being the entire doubleton: the conditional isolation probability at either endpoint is zero, at an outside neighbor it is q^(d_w-1) because exactly one incident edge is forced shut, and elsewhere it is unchanged at q^d_w. Multiplying the conditional-minus-unconditional differences by p q^(d_u+d_v-2) and summing recovers the local identity. On the star the resulting bracket is k-1-kq-q^k, strictly decreasing from k-1 to -2. On the once-subdivided star the two edge classes give the stated B_k. At k=2 it factors as q²(1+q)(1-3q), giving the P5 crossing. For k>=3, the two positive terms after division by q² are 2q^(k-2)(1-q) and (k-1)q^(k-1)(1-q); the first is at most 1/2, and maximizing the second at (k-1)/k gives ((k-1)/k)^k<1/e. Together they cannot offset the constant -1, irrespective of the other negative terms. The p=1/2 examples are 9/64 and -45/128. The archived Fraction verifier's independent edge-state calculation and finite case coverage were inspected; the recorded 2882 labeled-tree trials are corroborative evidence, not a fresh rerun or a proof. The opening comparison should not be read as opposite signs at every p: below its crossing the ordinary star has negative covariance too.

## originality

PASS

The same statistic and essential indicator-overlap calculation are already present for regular graphs in Resultary 2c5facc9a2eb. Replacing constant degrees with local degrees in that proof readily recovers the tree identity; that identity and the calculation method are not the basis for a priority claim. The distinct result is the sharp all-p branching obstruction under uniform arm subdivision, together with the P5 and ordinary-star comparisons. The older regular theorem neither applies to these hosts nor implies that sign classification by parameter substitution.

## value

PASS

The first two cluster counts give a natural dependence probe. Comparing a hub with and without one extra edge on each arm shows that the ability to produce positive association at high retention disappears sharply at three subdivided arms, with a genuine path exception. The quantified structural sign barrier, rather than the routine overlap computation or a fixed numerical example, is the useful result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
