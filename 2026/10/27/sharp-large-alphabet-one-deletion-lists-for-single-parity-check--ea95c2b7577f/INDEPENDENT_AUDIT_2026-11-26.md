# Independent mathematical audit

## correctness

PASS

For fixed y, put a vertex at each allowed insertion description. Equal-parent descriptions occupy consecutive gaps (deleting two different coordinates from the same parent gives the same y iff the intervening parent symbols are all equal). In each such class the adjacent-equality edges form a path, so counting vertices minus edges is exact. At y=0 the parents are the zero word and q−1 single-nonzero words at each zero-check coordinate. Losing even one free gap leaves at most q(z−1)+n−z descriptions, below this baseline by q+1−n≥1. Thus restrict to W perpendicular: an adjacent pair touching a zero-check coordinate always duplicates, since that gap permits every symbol and the resulting word also has the alternative description. For the other pairs the duplicate condition is exactly b_i·y=0. The nonzero restrictions b_i outside W have kernels of relative size 1/q, and at most n−1<q such kernels cannot cover W perpendicular (zero-dimensional case has no nonzero restrictions). This proves sharpness and the rank computation. In the F5 examples W is spanned by (1,1,0),(0,1,1) for h; (1,4,1) is perpendicular and its merged form evaluates nonzero. The other check's merged form is zero. For the stated binary all-ones boundary, the number of nonduplicates is the number of 1s of an even-parity received triple, or of 0s of an odd-parity triple; both are at most two and attainable. Frozen enumeration evidence was read, not used to infer the general result.

## originality

PASS

The coefficient-dependent formula for a fixed hyperplane is distinct on the evidence inspected. The closest same-code-class example is a binary list-size bound for a special check, outside the alphabet hypothesis. Neither ambient channel degrees nor stated general rate bounds determine the rank-sensitive extrema.

## value

PASS

An exact nonenumerative worst-case list size for a natural code class supports comparison of actual check vectors, not just bounds depending on length and field size. It identifies a rank obstruction and shows why support alone cannot determine the list size, with a sharp all-length theorem on the stated regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
