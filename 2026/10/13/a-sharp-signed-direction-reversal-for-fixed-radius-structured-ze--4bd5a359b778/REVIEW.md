# Independent mathematical audit

## correctness

PASS

For f(x)=lambda||x||^2/2, exact forward differences give x_next=(I-beta PP^T)x-(beta h r/2)P1, where beta=alpha lambda and r=d/ell. With iid frames, R^2=rR, Ru=ru, ||u||^2=d, ER=I, the mean evolves by 1-beta and the second moment by rho=1-2beta+beta^2r, both contract for 0<beta r<2. Solving gives h^2 r^2 [beta d+2(1-beta r)||Eu||^2]/[4(2-beta r)]. Directional Cauchy Schwarz plus isotropy gives 0<=q=||Eu||^2<=ell; signed, positive and globally sign-biased coordinate frames realize each q. Therefore sign of 1-beta r is exactly the global minimizer reversal. Independently enumerated coordinate-frame one-step distribution with exact fractions at (d,ell,beta,h)=(4,1,1/4,1) gives E x1=(3/4,3/2,-3/4,0) and E||x1||^2=11/2, agreeing with both recurrences. Universal law is algebra, not sample-based.

## originality

PASS

The two stochastic structured-direction papers establish the update and convergence estimates, but an upper bound in their step/radius setting is not the equality for fixed positive radius nor minimax orientation reversal. The nearby Haar subspace-moment result concerns derivative-based sampling, not the finite-difference affine drift; the Resultary KGSM mean-square stability result concerns another algorithm. No searched stronger published exact fixed-radius variance law implied this reversal.

## value

PASS

Sharp global parameter-selection transition for a published optimization method; in particular an unbiased symmetric signed estimator may give greater stationary error than a biased unsigned estimator above beta r=1. The scalar invariant q classifies every admissible law, a motivated analytical boundary rather than a tiny numerical check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
