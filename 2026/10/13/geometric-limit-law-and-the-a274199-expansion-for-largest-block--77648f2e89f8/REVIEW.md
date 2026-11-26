# Independent mathematical audit

## correctness

PASS

The shortest border is unbordered, since a border of it would be a shorter border of the original; it cannot overlap its copy, since a nonempty overlap would border it. Conversely an unbordered v in v z v is the shortest border, so each r-layer event counts uniquely by the r lengths and blocks and arbitrary center. Its probability is the r-fold product sum restricted by total peeled length at most n. Monotone passage to the unrestricted sum gives s_q^r. The first two exact terms plus the geometric tail give a strict bound below one (at q=2, at most 7/8; the bound decreases thereafter). Empty-center probabilities are summable over positive even half-lengths, since each complete peel has a unique positive length composition and the sum over layers is s_q/(1-s_q). The limiting width and its mean then follow, the mean by summable domination of the tail probabilities. For the series, the first-part recurrence for constrained compositions gives H_m=F_m/(1+B) with the same triangular recurrence and initial term as a_m; therefore B=S/(1-S) formally. To justify evaluation, for any 0<rho<1 the sum of absolute coefficient norms at radius rho of the a_m is at most product_{j>=1}(1+rho^j)-1, by the triangular recurrence. Thus S is continuous there. The coefficient series B converges for 0<=x<1/2 by the unrestricted composition bound; the identity (1−S)B=S there, together with nonnegative coefficients and S(1/2)=s_2<1, permits passage to the endpoint by monotone convergence. Finally splitting constrained compositions by last part K+1 gives the A274190 recurrence after setting d=N−K; take counts to be zero for negative d, with the empty composition counted for d=0. The reverse row then stabilizes at d once K+1>=d. The b_0 offset accounts for the separate constant 1 in the mean.

## originality

PASS

Credit the known greedy factorization, finite-width recurrence, existence of the limiting mean, the conjectured coefficient sequence, and the already recorded composition model. The distinct contribution supported by the comparison is the proof linking the unbordered-word renewal series to A274199 and hence resolving Conjecture 5. The explicit geometric law and mean formula are useful consequences of the recurrence mechanism, not an independently new mechanism; the distribution is not itself part of Conjecture 5.

## value

PASS

The proof settles a published all-alphabet expansion conjecture and explains the coefficients by an exact transformation of the shortest-border law. It gives actual limiting probabilities, not just approximate means or fitted coefficients. The value assessment rests on the normalization/composition argument, not on reproducing the existing table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
