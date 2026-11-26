# Independent mathematical audit

## correctness

PASS

For a triangular block map T, im(T)∩U=im(A)+B(ker D) inside the preserved subspace U. A regularity witness S must lift im(T)∩U through A. Conversely, if im(T)∩U=im(A), take preimages in U for a basis of the intersection, arbitrary T-preimages for a basis extending it in im(T), then extend S to preserve U by using a basis adapted to U and im(T). Thus regularity is precisely vanishing of the independent restriction/projection B↦(ker D→coker A). The map on B is onto (lift a basis of the cokernel and extend the kernel basis), so its zero fiber has q^(ab−ij) elements. The count of rank r comes from the product of two full-rank rectangular counts divided by |GL_r|, giving the stated p and the exact joint law under uniform sampling. For the limit, 0≤Φ_t−Φ_∞≤∑_{h>t}q^(−h); the finite/limit mass ratio differs from 1 by O_q(q^(−n+k)) for k≤n. Since ∑_k q^k π_q(k)<∞, this bounds the total error including the k>n tail by O_q(q^(−n)). Product, restricted weighting, and normalization (denominator ≥Φ_∞) give the claimed uniform two-block rate. For i₂>i₁ the conditional expectations differ by Cov(g(J),q^(−(i₂−i₁)J))/E[q^(−(i₂−i₁)J)] evaluated at i₁; the covariance is strictly negative for nonconstant nondecreasing g by the independent-pair identity. Apply the identity again to f and the decreasing conditional expectation. Supports are full for all admissible defects, and the same proof holds in the limit with the stipulated integrability. L_q<1 because the pair (1,1) has positive unweighted mass and receives weight <1. Numerical replay at q=2: use 60 product factors and sum i,j=0,…,15, obtaining approximately 0.6998513223055354; product tails are bounded by 2^(−60), omitted masses by 4∑_{k≥16}2^(−k²) per coordinate (Φ_∞>1/4). This was a floating-point corroboration, not a proof of the law. Read checks/check_parabolic_regular.py and the frozen 6574-matrix output, including 163 witness searches; the checker is prime-field only and was not rerun.

## originality

PASS

The image-intersection criterion, one-block exact law and nullity convergence are prior inputs, not contributions. Credit is for the two-block conditional regularity law and the resulting strict negative dependence in finite dimensions and in the limit. The strongest indexed overlap completely encodes the regular stratum and its normalization and gives L_q, but bears a later catalog date than this frozen record and does not expressly give strict negative association. The evidence does not establish an earlier covering statement for the combined claim.

## value

PASS

The exact count concerns a natural constrained monoid and explains a nontrivial effect of conditioning: two independently sampled nullities become strictly negatively dependent with a persistent nonregular fraction as both dimensions grow. The strength is the full per-stratum selection factor and quantitative limiting dependence law, not the independently known criterion or individual nullity formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
