# Independent mathematical audit

## correctness

PASS

After appending b the entire set of distinct subsequences ending in b is exactly {wb: w is an old subsequence, possibly empty}: old words ending in b are included in this image, not counted a second time. Words ending in the other symbol are unchanged. Thus the two shifted coordinates start at (1,1), add one to the other, and sum to H_n, not C_n. The expectation matrix has eigenvalues 1±sqrt(t) and output values 2,3 at n=0,1, giving the mean. Expanding the three quadratic monomials gives the stated positive matrix T_p. In λ−1 coordinates its characteristic polynomial is (λ−1)^3−5t(λ−1)−2t. Cayley–Hamilton gives the moment recurrence, whose first values are 4,9,16+18t (the n=2 outcomes are H=4 or 5); multiplying the OGF by its denominator gives numerator 4−3z+(1−2t)z². At λ=(1+s)^2 the characteristic polynomial is s²(s⁴+6s³+7s²−2s−2); the parenthesis is strictly convex on [0,1/2] with endpoint values −2 and −7/16, hence is negative. This gives a larger real root; for interior p strict positivity gives a simple dominant Perron root and a positive scalar projection onto it. It exceeds the squared-mean exponential rate, so subtracting the squared mean leaves the leading second-moment growth. In the fair case symmetry eliminates the antisymmetric eigenmode at 1/2 and the remaining two eigenvalues have sum 5/2 and product 1/2; initial M_0,M_1 give the stated coefficients. The endpoints p=0,1 are deterministic C_n=n+1. The growth is asymptotic for fixed interior p, not a finite-n strict monotonicity statement, not uniform near the endpoints, and not a result about convergence in probability. Independent replay `python3 /workspace/reproduce_reviews.py 1` explicitly enumerated index-subset outputs through length 9 and matched 70 exact bias/length cases, including deterministic endpoints and the fair quadratic recurrence. The frozen verifier was read, not executed.

## originality

PASS

The distinct supported contribution is the all-interior-bias second-moment law and the strict all-bias relative L² growth, not the known mean or the covered symmetric Stern power sums. The strongest later fair-bit joint-moment result substantially overlaps at p=1/2 but does not give the claimed biased law in its stated scope. No earlier exact biased formula or domination of the strict comparison was established in the inspected material.

## value

PASS

A complete second moment for the total distinct count answers a naturally motivated fluctuation question beyond the known mean. The strict rate separation throughout the nondegenerate bias range gives a quantitative obstruction to relative L² concentration, not a single numerical instance or a claim about typical deviations unsupported by moments. The rational law can also be used to evaluate finite biased variances exactly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
