# Independent mathematical audit

## correctness

PASS

H_n is the trailing block of leaf labels, not a depth statistic. For a=n-m, the event H_n>=m restricts exactly the independent parent draws at times a+1 through n to the first a labels. Multiplying their probabilities gives the factorial tail; conditional on the event these parents are iid uniform on the first a labels and independent of the induced tree. Each old leaf survives all m draws with probability (1-1/a)^m, and the leaf recurrence gives mean a/2 for a>=2. If a=1 the old root is hit with certainty. This proves the threshold regression, not a conditional formula for H_n=m. Subtracting n/2 and summing the indicator representation of H_n gives the covariance formula. The excess is half the expected duplicate draws in m draws on a labels; it is zero at m=1 and positive at every m>=2. Expanding the logarithmic product for m on the sqrt(n) scale gives the Rayleigh tail. The leaf recurrence agrees with the Eulerian descent-count recursion. Uniform permutation descents are 1-dependent when generated from iid continuous ranks and give Var(L_n)=n/12 for n>=3 and the stated normal limit. To check the joint step, write Y_k=L_k-k/2, and Y_(k+1)=(1-1/k)Y_k+D_(k+1) with bounded, orthogonal martingale differences. Thus Y_n-Y_a=-m Y_a/(n-1)+sum from k=a to n-1 of k D_(k+1)/(n-1), which is o_P(sqrt(n)) for m=O(sqrt(n)). The early count is exactly independent of the threshold event, so survival/leaf rectangles factor in the joint limit. The conditional mean excess converges to x²/4 at m near x sqrt(n), uniformly on bounded x ranges; at x=0 use m=1. For m<=n/2 the duplicate-draw bound is m(m-1)/(4a) for the excess, and the product tail is bounded by exp(-m(m-1)/(2(n-1))). For m>n/2 the trivial bound m/2 and the same tail are sufficient. These bounds give dominated Riemann sums and the limit sqrt(pi/2)/4 for the scaled covariance.

## originality

PASS

The uniform recursive-tree leaf count, Eulerian marginal and its normal limit are not new. The supported distinct contribution is the trailing birth-label extreme jointly with the total leaf count, in particular the exact threshold regression and residual covariance constant despite limiting independence. The strongest same-model age result concerns the earliest surviving leaf, and fixed-set leaf erasure does not supply the mixed claims. Older leaf-run work could not be inspected beyond its abstract and is not treated as ruled out.

## value

PASS

The statistic locates the most recently born vertex that has already become a parent, a natural age observable distinct from depth. Its Gaussian/Rayleigh separation by itself would miss the positive mixed effect: the exact threshold regression and nonzero sqrt(n)-scale covariance quantify what the independent leading limit hides. Both pieces are useful in comparing local age extremes to global degree counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
