# Independent mathematical audit

## correctness

PASS

RESULT.md begins with exact marked-Poisson identity S(z)=(1-F_b(z))exp(-R A_b(z)), where F_b(z)=∫0^z e^{-bu}g(u)du, A_b(z)=∫0^z(z-u)e^{-bu}g(u)du and g(u)=exp(-1/(4u))/(2sqrtπu^(3/2)). The Laplace transform q_b=exp(-sqrt b) and mean successful transit delay 1/(2sqrt b) follow from the one-dimensional Brownian hitting law. For c<1, z=x/L yields a strictly decreasing endpoint phase φ_c(y)=1/(4y)+c²y near h_c, and the vanishing (x-y) factor gives the L^(-5/2) normalization with coefficient x^(-3/2)/(2sqrtπ[-φ_c'(x)]²). The correct expansion at x=h_c+[(5/2)logL-logC+w]/(a_c L) gives R A_b→exp w and F_b→0. For c>=1 the inequality 0<=z-A_b/q_b<=1/(2sqrt b) supplies the exponential limits on their stated scales, including η. Independent numerical integration verified exact Laplace-transform normalization and the hazard near the proposed window at finite L; convergence is visibly slow, especially c close to one, and this was not used to infer the limit.

## originality

PASS

The motivating Gutiérrez et al. paper proves the same marked-Poisson survival formula and asymptotic exponential tail for fixed mortality/recruitment; the subject of this audit is the noncommuting coupled fast-recruitment/fast-mortality transition. Tung and Lawley prove a general fast-immigration Gumbel theorem for a fixed successful-arrival law with fixed short-time asymptotics; that hypothesis does not directly cover mortality b growing like log²R, nor the switch to Exp at c>=1. The two papers were read in relevant complete sections, not merely matched by title. Related DRM 2026 primary has only its abstract accessible; material priority risk remains.

## value

PASS

A sharp competition boundary answers when particle injection ceases to overcome exponential mortality, distinguishes logarithmically quick first arrival from growing waits, and provides the full critical-window law. The unusual 5/2 loglog centering arises from an endpoint integral with a vanishing linear factor, supplying quantitative distributional information absent from fixed-mortality mean estimates.

The dated certificate retains the supplied scientific assessment, sources and limitations.
