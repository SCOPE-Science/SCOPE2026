# Independent mathematical audit

## correctness

PASS

For 1≤k<m, every top-k set of a strict single-peaked ranking is precisely a length-k interval containing its peak, and conversely all such intervals are realizable. If m<2k−1, all length-k intervals share at least two points so a unique approval winner is impossible. For a putative winner w at distance d≥k from median peak h, no voter peaking at or right of h can approve w; two left voters must both approve w, with intervals intersecting only at w, otherwise the winner is tied. The other three length-k intervals must be mutually disjoint and disjoint from the two-winner union, forcing m≥5k−1 and d≤m−3k. For d<k the bound is k−1; explicit five-ballot intervals attain k−1 whenever m≥2k−1 and m−3k for m≥5k−1, including the k=1 boundary. Independent exhaustive enumeration of interval-and-peak multisets for (m,k)=(4,1),(5,2),(6,2),(7,2),(9,2),(7,3),(9,3) yielded maxima 1,1,1,1,3,2,2, matching the piecewise formula. These finite checks only corroborate the infinite parameter proof.

## originality

PASS

Targeted source and implication comparisons did not identify prior coverage of the precisely scoped final theorem; best-of-knowledge PASS with named residual risks, not a priority certificate.

## value

PASS

Top-k approval on an axis is a standard restricted voting rule and the median peak is a natural Condorcet benchmark. The precise feasibility cutoff and second 5k−1 distance transition measure how a uniquely victorious approval candidate may deviate from that benchmark. The result is not merely a parameter substitution: disjoint interval packing produces a new sharp two-regime law and explicit extremizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
