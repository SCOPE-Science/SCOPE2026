# Independent mathematical audit

## correctness

PASS

The frozen mathematics is correct. In the orthonormal biased coordinate basis the affine kernel is 1 plus the sum of the normalized coordinate products. The i-th term in an evaluation row has law C_i/s_i−1, with s_i the probability of that evaluation bit and C_i independent Bernoulli(s_i). Conditioning on the other terms reduces rare-row maximization and rare-probability monotonicity to (1−s)|a|+s|a+1/s|, a nonincreasing function of s. Kernel symmetry yields weighted endpoint duality, and choosing row signs attains the bound. At the unbiased values of the other n−1 probabilities the conditioning variable a takes −1 (even n) or −2 (odd n≥3) with positive probability, giving the strict fair minimum when one probability changes, and monotonicity handles the rest. The mean-one kernel variable is bounded below by −(n−1), strictly above that on a positive-probability success event; its negative part tends in expectation to n−1 as all rare probabilities tend to zero. The corrected claim uses the established formula only as a premise. In four coordinates with p_i≤1/2, no outcome with at least two successes contributes a negative part. Splitting zero and one success gives the corrected closed expression. Exact evaluation gives 77/27, 371/128 and 6213/2048, with signed gaps 161/3456 and 277/2048, and both nonconstant vectors majorize the constant vector of the same sum. Hence the repaired non-Schur assertion follows. The corrected scientific notes match the retained verification code and the frozen JSON front matter is preserved.

## originality

PASS

Original headline originality FAIL: the general heterogeneous affine formula, rare norming vertex, equality of endpoints and coordinatewise monotonicity are an exact specialization of Resultary 40f4b54b28c0, which the frozen priority comparison omitted. This conclusion is based on mathematical coverage, not on dating or attribution of discovery. The fair and sparse extremum arguments are direct consequences plus a one-coordinate strictness check and are not retained as contributions. Repaired originality PASS for the separate two-sided fixed-mean Schur obstruction only. The replacement expressly credits the general formula and uses it to prove and explain an explicit order reversal, not to reclaim it under a different name.

## value

PASS

The repaired result answers a natural optimization question about averaging coordinate biases while keeping the expected total number of successes fixed. It supplies explicit witnesses to both failures of ordering, and the change of sign of the one-success residual explains why the familiar product-maximization argument need not survive beyond the threshold. This is a motivated negative result with consequences for bias-balancing heuristics, not novelty attributed to individual computed constants or a covered headline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
