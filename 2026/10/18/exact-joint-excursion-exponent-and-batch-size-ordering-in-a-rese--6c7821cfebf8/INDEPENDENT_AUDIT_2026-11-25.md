# Independent mathematical audit

## correctness

PASS

Uniform marks hit a given j-set with probability q_j, so each label has finite stationary age and independent Brownian increments conditional on the ages with variances 2DA_i. The marked-Poisson void exponent for arbitrary age thresholds is r times the mean over marks of the maximum touched threshold. Convexity and exchangeability give the lower bound rq_j/j times the sum of thresholds; exchangeable hit-count increments q_j−q_{j−1}=q_1 (N−m)_{j−1}/(N−1)_{j−1} (falling factorials) are nonincreasing, so the bound with c=rq_k/k applies for each subset of tags. Expanding the exponential moment into nonnegative orthant integrals gives finiteness for 0<θ<c, with nonpositive θ automatic. The event of no tagged hit for s/k units has probability exp(−cs) and implies the age sum exceeds s up to a null boundary, so the moment diverges at and above c. Independently, scanning backward until the next hit of the j unresolved labels gives a waiting time Exp(rq_j), independent of the hit mark, and adds j times that wait to the age sum before removing hit labels. This recursion also gives finiteness exactly when θ<min_{j reachable}rq_j/j=c; initial j=k is always present. It reproduces the stated pair transform, with rates for hitting one particular label only λ₂−λ₁ and for hitting both 2λ₁−λ₂. For the excursion, conditional Gaussian tails plus Cauchy–Schwarz bound the probability by 2^k E exp(−k²z²/(4DS_k)); the finite age moment and AM–GM give exponential rate at least k sqrt(c/D). With a common age floor az, the probability is bounded below by exp(−rq_kaz) times erfc(sqrt(z/(4Da)))^k. Optimization of rq_ka+k/(4Da) matches the upper probability bound on the logarithmic scale. This uses fixed N,m,k,r,D and no first-passage interpretation. Finally the exact falling-factorial sum for q_k/q_1 has nonincreasing terms in m and a strictly decreasing j=1 term for k≥2; it gives precisely the endpoint ratios k and sqrt(k). An independently written rational calculation using literal subset marks and the backward-cover recursion (`python3 -B /workspace/branches/bounded_review_checks.py 5`) checked hit counts, strict normalized order and age transforms for N=2 through 10; the frozen floating-point and quadrature script was inspected, not executed. The finite checks are not used to prove the asymptotics.

## originality

PASS

Best-of-knowledge pass for the equal-threshold fixed-finite-N all-k excursion rate and the strict normalized comparison for uniform partial batches. The marked-age law itself is a classical shock-model law and the positional hierarchy and exact two-point distribution are prior work. The claimed Gaussian-mixture logarithmic orthant asymptotic and its batch ordering are not stated by those results in the inspected material; in particular a positional Fourier recursion or the domain of its exponential moments does not by itself provide the matching joint lower tail bound. The auxiliary moment threshold is an exact extraction from the known shock-age structure, not a claim to have introduced that structure or its fully synchronized endpoint.

## value

PASS

The result isolates a large-excursion observable whose marginal-normalized rate orders every batch size even though covariance amplitude may behave differently. It identifies the common reset hiatus as a sharp mechanism for simultaneous rare displacements and provides a precise diagnostic for all k at finite N, not just a fit at one threshold. It does not claim a prefactor, a first-passage law or a large-N uniform limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
