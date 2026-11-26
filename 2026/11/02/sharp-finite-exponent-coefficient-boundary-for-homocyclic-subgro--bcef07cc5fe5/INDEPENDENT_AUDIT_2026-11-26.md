# Independent mathematical audit

## correctness

PASS

Each Delsarte summand has degree sum h_i(r-h_i): the Gaussian degree contributes (h_i-h_{i+1})(r-h_i), which adds to the explicit p-power. The maximum is attained by a constant middle chain and cannot cancel, giving the stated degree and reversal. Writing (t;t)_j for the finite product, the reversed Gaussian factors telescope to (t;t)_r divided by the product of (t;t)_gap over consecutive height drops, including the top anchor r and bottom anchor 0. For even rank, a chain with central height s has an upper and a lower Durfee chain; recursively removing the top square from a partition of width <=s and its right-hand rectangle proves each bounded chain sum equals 1/(t;t)_s. In the absence of s, insertion splits one strictly positive crossing gap (including a possible anchor gap) and multiplies the contribution by a Gaussian with constant and linear coefficients 1. Every noncentral entry has defect >=1, so patterns of length <a cancel, length a contribute E-N, and lengths >=a+1 contribute E. All differences are coefficientwise nonnegative. At codegree a+1 only deviations ±1 can occur: a+1 length-a patterns contribute from the first insertion coefficient and a+2 length-(a+1) patterns contribute from constant factors. This proves the universal deficit 2a+3 even when the finite polynomial has no coefficient at that codegree. For odd rank, noncentral entries have defect >=2; at fixed k and a>=k+2, each contributing noncentral pattern has a central run of length L>=2. Both constant-height choices are independent of L, while the L-1 interior switch choices have identical Gaussian factors, giving affine dependence. For k=0,1 only central chains contribute; the a+1 terminal Gaussians and a-1 interior switches each have linear coefficient 1, for 2a. In even rank one terminal factor and the two unit deviations give 3. The recorded finite checks and support code were inspected, not executed; they do not prove the formal or all-rank statements.

## originality

PASS

The limiting product, leading terms, Delsarte sum, and central insertion and Durfee methods are existing work. Coefficientwise nonnegativity is obtainable by reading the known insertion factor formally. The distinct finite results are the sharp, all-rank first disagreement with its universal count and the exact odd-rank eventual affine dependence at fixed codegree, not independent novelty of the product or insertion inequality.

## value

PASS

The first codegree at which the finite exponent changes the limiting coefficient is a natural precision question for the homocyclic enumeration. A rank-independent exact deficit, and a contrasting finite affine law rather than stabilization for odd rank, are useful structural information, not isolated coefficient recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
