# Independent mathematical audit

## correctness

PASS

The covariance 2a I and angular radius 2 pi |xi| give the stated transform. On a negative lobe, u=ar^2+log(-J_0) tends to minus infinity at both ends. The Bessel ODE gives u''=4a-1-4a^2 r^2 at every stationary point, strictly negative by completing the square and r>1. Two maxima would force an intervening minimum, so there is exactly one stationary point, and its curvature gives the exact zero orders. The energy J_0^2+(J_0')^2 has derivative -2(J_0')^2/r, so at a=0 the negative-lobe heights strictly decrease. The envelope derivative of the log-height ratio is rho_l^2-rho_k^2>0, and comparison with a fixed interior point of I_l and the right endpoint of I_k makes the ratio diverge as a grows. In the endpoint proof, first bracket the critical point at s-x/s with fixed x on opposite sides of 1/(2a): the Bessel ODE and Taylor expansion normalized by J_0'(s) give J_0(s-h)/J_0'(s)=-h+O(h^2/s+h^3), J_0'(s-h)/J_0'(s)=1+O(h/s+h^2), hence u'=s(2a-1/x)+O_a(1/s). Within this bracket the critical equation gives h=1/(2as)+O_a(s^-3). The exponent loses exactly 1 in the limit and J_0'(s)~sqrt(2/(pi s)), giving the stated prefactor. Two roots per sufficiently late negative lobe yield the count by the Bessel zero locations. For the first root, |J_0|<=1 gives the lower bound sqrt(log(lambda)/a) and a negative antinode within bounded distance to the right of sqrt((1+epsilon)log(lambda)/a) gives the upper asymptotic. Independent bounded SciPy replay (independent_checks.py circle) reproduced all three stated crossover values and tested the endpoint scaling in log form. The frozen prose reports 45 sampled lobes, but its displayed loop/output has 15 distinct fold-sampling parameter pairs, plus further solver calls and six root-pair cases. No universal claim relies on the numerical count.

## originality

PASS

The exact transform and asymptotic Bessel ingredients are classical. The distinct contribution is the complete real fold census, strict ordering reversal for each pair of lobes, and sharp fold-height/mass asymptotic for this mixture. The strongest inspected archive radial-zero results concern a different transform and do not imply this fold law.

## value

PASS

This canonical planar radial probability mixture adds a smooth strictly positive Fourier term to an oscillatory one. The natural question is how zero circles are born and ordered as the two independent mixture parameters change. The theorem gives the entire real zero set and exactly which pairs of folds exchange order, with explicit asymptotic size of the arbitrarily small masses needed in distant lobes. The fold comparison provides more information than the leading density alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
