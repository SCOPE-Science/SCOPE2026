# Independent mathematical audit

## correctness

PASS

The affine factor Gram matrix in barycentric coordinates is (I+11^T)/((d+1)(d+2)), whose inverse gives the vertex kernel (d+1)(d+2)U-(d+1). Independence makes centered factorwise affine spaces orthogonal; adding them and the shared constant yields the sum of factor kernels minus k-1. The product kernel is affine in its evaluation point, so its L1 mass is convex and cannot exceed the maximum over product vertices; barycentric symmetry makes their masses equal. The sign of the chosen vertex kernel attains the norm: the resulting projected function is continuous, so its vertex value is bounded by the essential supremum on the full-support domain. At a product vertex the U_i are independent Beta(1,d_i). For d_i/N→w_i>0, d_i U_i tends in law to a unit exponential and the scale multiplier tends to w_i; zero proportions vanish in L1 by expectation (d_i+2)/N, including bounded dimensions. Independence gives joint convergence, and E[K^2]=1+sum_i d_i(d_i+2) gives uniform integrability after dividing by N. To prove strictness for a pair of weights with sum s>0, swap the two iid exponentials and average, obtaining max(|R+s(X+Y)/2-1|, |a-b||X-Y|/2). For any two distinct imbalance magnitudes there is positive probability that the first term is smaller than the larger imbalance term and X≠Y: take R<1 and unequal positive X,Y with sum near 2(1-R)/s, then use the positive density on an open neighborhood. This proves strict balancing even with zero weights, and the usual characterization by balancing transfers gives the stated equality cases. At a vertex, the positive excess over one gives 2/e. At equal weights, the derivative of z^k exp(-z) integrates the gamma positive excess to 2k^k exp(-k)/k!; Stirling gives the iterated large-k law. For k=2 the two-exponential convolution and positive-excess integral give the divided difference, including continuous limits. Independently replayed all three rational norm examples.

## originality

PASS

The one-simplex result, the exact two-factor product law and the two-exponential divided difference have material coverage and are not credited as distinct on their own. The added result is a single projection theorem for arbitrary fixed k, including exact independent-beta norm, limits for all weight proportions and the strict balancing and equality structure. The general symmetric convex expectation heuristic supplies non-strict majorization but not the strict nonsmooth claim or the projection result. The inspected narrower results and general bounds do not cover the combined theorem.

## value

PASS

Uniform-volume least-squares projection onto total-degree-one polynomials is a natural operator on product cells; the exact L∞ norm measures worst-case amplification and is not the easier tensor-product norm. The supported arbitrary-factor law distinguishes all limiting aspect profiles via strict balancing and gives the precise best and worst cases. It unifies the known lower-factor examples and quantifies how the optimal amplification changes with the number of factors. This is a sharp, potentially useful benchmark, not a claim of any solver-performance improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
