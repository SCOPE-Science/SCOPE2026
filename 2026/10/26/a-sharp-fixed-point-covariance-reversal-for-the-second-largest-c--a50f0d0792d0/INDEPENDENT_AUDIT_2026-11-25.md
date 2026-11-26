# Independent mathematical audit

## correctness

PASS

Conditioning on one designated fixed point adds a singleton to a uniform permutation of n−1 and increases its second length precisely in the one-cycle case, which has probability 1/(n−1). Since E[F_n]=1, this gives the covariance identity. Uniform insertion uses m existing arrows and the singleton option. Insertion at an existing arrow increases the second-ranked length only when a strictly larger cycle already exists and the chosen arrow is in a second-ranked cycle. Thus the arrow contribution is B_m C_{B_m} with the stated strict-rank indicator, giving (1−T_m)/(m+1). The disjoint cycle types (a,b) and (a,b,1) with the stated restrictions each contribute 1/a. Their harmonic sum has strictly positive two-step difference in each parity by comparing its four positive fractions with the smallest fraction, and the bases 841/840 and 6527/6435 exceed one. I recomputed those bases and the full finite boundary table by a separate exact recurrence: condition on the length j of the cycle containing label 1, uniform on 1 through n, insert j into the top-two length pair of the remainder, and update the fixed-point-weighted mass by adding ordinary mass if j=1. It reproduced all ten entries, including +1/30 at 5 and −1/36 at 6; the harmonic argument covers the rest. For the limit, one can avoid any small-second-cycle estimate: pointwise the absolute difference of the insertion statistic and B_m is bounded by the sum of j C_j(C_j−1) over j. Counting pairs of disjoint labelled cycles gives E[C_j(C_j−1)]=1/j² for 2j≤m and zero otherwise. The resulting O(log m) error suffices, with Shepp–Lloyd's mean limit, to get −γ₂. The original long-cycle tie proof is also valid.

## originality

PASS

The distinct contribution is the all-size dependence classification: the sign is positive through n=5 and strictly negative at every n≥6. The ranked-cycle insertion recurrence and the value of γ₂ are classical. The covariance identity is an elementary fixed-point marking reduction, and the asymptotic covariance is a short consequence of that reduction, classical ranked-cycle ingredients and tie control. Neither alone is the basis for passing originality. The inspected prior passages and related catalogue statements do not give the decisive finite sign boundary with permanence.

## value

PASS

An all-size sign boundary for a natural local statistic and a macroscopic rank gives information unavailable from marginal moments. The proof identifies the precise finite crossover and excludes later reversals or zeros, which is stronger than a numerical observation or a limiting negative covariance. The harmonic argument makes the cutoff uniform, rather than a cutoff chosen for computational convenience.

The dated certificate retains the supplied scientific assessment, sources and limitations.
