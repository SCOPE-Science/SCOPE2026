# Self-review

## Correctness

PASS. Gaussian rotation reduces the sketched first pivot to the difference of two independent scaled chi-square variables. Convolution gives an exact positive density at zero, which implies the inverse-moment cutoff. For the fixed two-column input, direct sketched oblique-projection algebra gives the Schur complement \(d=v-hk/z\) and a triangular representation of the output; the two-dimensional determinant inequality bounds its condition number below by \(\sqrt{|d|/|z|}\). The joint Gaussian law of the three sketch columns is nondegenerate, and the near-orthogonality event has probability at least proportional to its pivot tolerance by a transverse-coordinate argument. This proves a \(1/t\) lower condition-number tail and therefore divergent first and higher moments. The checker supplements, but does not replace, those arguments. No undefined-pivot event has positive probability.

## Originality

PASS with residual risk. The closest primary work is Grigori--Piccinini--Simunec, arXiv:2509.04386, especially Algorithm 3.1, Proposition 4.1, and Section 6: the paper already gives a uniform **upper** Gaussian small-ball bound and discusses **typical** conditioning, but does not state a matching exact density, unconditional negative-moment phase line, or the explicit well-conditioned two-column example with infinite expected condition number. Simoncini--Wang, DOI:10.1002/nla.70022, studies a whitened Krylov basis rather than these two-sided signed pivots. Published-record searches for Gaussian Gram--Schmidt near-breakdown, negative Gaussian bilinear moments, and infinite mean condition numbers identified no statement covering the combined theorem. Classical product-normal and gamma distributions are acknowledged; this is not a novelty claim for those distributions. Older unindexed algorithmic moment results remain a risk.

## Value

PASS. High-probability avoidance of small pivots does not by itself guarantee integrability of basis norms or condition numbers, which are natural quantitative stability metrics. The sharp first-pivot threshold and the explicit two-column infinite-mean example give a substantive boundary to what numerical summaries and tail-agnostic expected-conditioning statements can establish. The input bases are orthonormal and the deterministic two-sided process remains well-conditioned, isolating randomness as the source. Finite sketch oversampling does not remove the unconditional phenomenon. It does not contradict good high-probability or safeguarded behavior.

Self-review: passed. Independent audit: not yet performed.
