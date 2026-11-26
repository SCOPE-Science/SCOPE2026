# Independent mathematical audit

## correctness

PASS

The nested images of the square have compact connected intersection containing distinct fixed points (0,0) and (2/3,2/3); projection onto a line joining them gives the dimension lower bound. Each of at most 2^n sign cylinders is convex and has an affine image in the square. The derivative sends |u|≤|v| into itself while expanding |v| by at least 2(1−2δ)>1; applied to (0,1) this bounds the largest singular value below by [2(1−2δ)]^n. Dividing the determinant (2δ)^n by it gives a least singular value at most q^n, q=δ/(1−2δ). The image fits in a bounded-length rectangle of width ≤√2q^n, coverable by O(q^(−n)) balls of radius q^n. Combining cylinders and interpolating between geometric scales gives the asserted upper box bound, strictly below two because q<1/2. This is an upper bound, not a dimension formula. For the distance, the direct image lies within 2δ of the graph by Lipschitz continuity. The displayed two-cycle solves the rising and falling branch equations; both inputs are valid since they equal b/2 and 1−a/2 with a,b∈(0,1). At (a,b) the vertical discrepancy is 4δ/(5−8δ), implying graph distance ≥4δ/((5−8δ)√5). Conversely every dyadic monotonicity interval of τ^m has a fixed point of τ^m. Aside from the zero orbit, the cyclic coordinates have odd denominator ≤2^m+1, leaving a gap ≥1/(2(2^m+1)) from 1/2 and double that from 0 and 1. The inverse affine cyclic equations contract in sup norm by (1/2+δ)/(1−δ), giving coordinate displacement ≤2δ/(1−4δ) and input error <4δ. With m=floor(log₂(1/(16δ))) and δ≤1/64, δ(2^m+1)≤5/64<1/8 keeps every branch and coordinate valid. The perturbed cycles are in every forward image. Their distance to the graph points on the dyadic net is at most 2√2δ/(1−4δ); including the net mesh contributes √5·2^(−m)<32√5δ. Their sum is less than 80δ. Thus the rate has sharp order only, on the stated small-memory range, for the full core and not for an SRB measure support.

## originality

PASS

The closest same-map work gives stable-direction estimates and invariant-measure results, not the finite-scale state-space cover or the two-sided collapse of the full forward core. The targeted catalogue results describe different maps or statistical observables. Novelty is supported to the extent of the compared statements, not established by a keyword miss.

## value

PASS

The set of all points with arbitrarily long prehistories is a natural object distinct from typical orbit statistics. The one-step inclusion alone would allow much of the limiting graph to be absent from the perturbed core. A uniform reverse inclusion with matching lower order addresses that gap, and the explicit spatial covering estimate explains degeneration to dimension one independently of the known SRB behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
