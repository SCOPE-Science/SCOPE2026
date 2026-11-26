# Independent mathematical audit

## correctness

PASS

On a hypothetical successful draw path, the post-draw survival exposure is n(n−1)/2 plus the sum of m times the repeat count at state m. The ordinary independent stage counts therefore tilt by a product; normalizing gives continuation r_{m,n}=(1−m/n)s^m (the first draw is necessarily new). Positivity follows already from a successful path with no repeats. Under common independent continuation trials, the discrepancy probability for geometric continuations r≤q is (q−r)/(1−r)≤(q−r)/(1−q), giving the stated coupling estimate with q=s^m and a geometric tail. For the sharp limit, the normalizing product A_n^* satisfies n log A_n^*→α_s by dominated convergence over the coordinates, with exponentially small missing tail. In the likelihood's remaining product B_n, the deficit satisfies n(1−B_n)≤M (a product deficit bound, or M>n when there is a forbidden coordinate); it converges pointwise to M after scaling. Since E[M]=α_s, this proves n(A_n^*B_n−1)→α_s−M in L¹ on the full partition law. Coefficient extraction from the Euler product and differentiating the k-part weight sum gives h_k=E[M|K_s=k]. The pushforward is an L¹ contraction and its limiting norm is strictly positive at k=0, proving the exact TV coefficient with the factor 1/2. The geometric moment formulas and mean difference follow directly, with a summable bound m s^m/(1−s^m)^2 and exponentially small omitted tail. This is fixed s, not an endpoint-uniform limit. Inspected but did not run the supplied verify.py. Own replay (python /workspace/branches/independent_math_checks.py, section 4) checked 144 exact finite coefficients and C_(1/2)=1.007312449002664228713563 with truncation at 100; the coefficient tail is bounded by (1/2) sum_{k>100} 2^(-k)(k+8), with exponentially small errors in the products and in α_s. None of these finite checks substitutes for the density argument.

## originality

PASS

The distinct result is the signed first-order ℓ¹ expansion and exact positive TV constant for the fixed-survival conditional model. Prior stage/exposure decompositions already imply its independent tilted geometrics by elementary conditioning, and the partition probabilities are classical. The closest indexed Euler-product collector has the identical limiting law with an order-sharp convergence rate, but for a different finite perturbation; an atom correction there cannot determine the signed whole-law derivative here.

## value

PASS

Conditioned success is the natural regime in which a completion time exists for this fragile model. The result identifies a tight delay law instead of the ordinary collector's large delay. The precise signed coefficient quantifies approximation error for each delay count and the whole distribution, which a finite factorization or an O(1/n) inequality does not determine. This is a meaningful fixed-survival refinement of the motivating conditional-time problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
