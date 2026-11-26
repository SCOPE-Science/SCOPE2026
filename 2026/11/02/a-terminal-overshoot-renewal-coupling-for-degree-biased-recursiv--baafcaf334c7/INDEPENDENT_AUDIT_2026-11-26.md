# Independent mathematical audit

## correctness

PASS

The cited recursive-tree splitting property and kernel apply to exactly the stated parent-endpoint rule. Telescoping the harmonic mass gives Q_m=(H_(m-1)+1)/m and Q_2=1. The acceptance b_m/Q_m is in [0,1] and, after a rejected overshoot and conditional redraw below m, the mass at k<m is q_k(1-b_m)/(1-Q_m)=m q_k/(m-1). The m=2 redraw branch is unused. Before first crossing n-1, every jump is copied. A terminal jump m-1 leaves one vertex; a strict overshoot ends the cut count in the same step if accepted. Rejection can only delay the cut count, not make it earlier; even a rejection can leave exactly one vertex, so the error bound is an upper bound. The small residual event forces a renewal visit at one of n-M+1 through n-2. The renewal mass vanishes by the infinite-mean lattice renewal theorem; this can also be seen directly: along a subsequence where u(n) approaches its limsup L, the renewal recursion and q_k>0 for k>=2 force each fixed lag u(n-k), k>=2, to approach L, since all other fixed-lag limsups are at most L and the contribution of the tail of q is uniformly small. The last-renewal identity sum from k=0 to n of u(n-k)Pr(zeta>k)=1 thus forces L=0 by the divergent tail sum. Fixing M and then increasing M gives vanishing coupling error and total variation. At j=floor(2cn/log^2 n), the truncated sum divided by n has expectation tending to c and variance O(1/log n); above-truncation jumps have probability O(1/log n). Monotone inversion gives the stated weak law for the first-passage time and transfers it to the cut count.

## originality

PASS

The distinct contribution is the exact terminal overshoot correction for the specified degree-biased chain, its vanishing count-disagreement bound, and the resulting weak law for the actual cuts. The harmonic decrement formula is prior work, as is an asymptotic for a different barrier walk. The inspected primary statements do not imply the new count approximation.

## value

PASS

This resolves the natural first-order scale for the actual cut count rather than only its previously analyzed upper comparison. It turns the problematic full-deletion atom into an acceptance correction and obtains the stronger count-level total-variation statement with a model-specific finite bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
