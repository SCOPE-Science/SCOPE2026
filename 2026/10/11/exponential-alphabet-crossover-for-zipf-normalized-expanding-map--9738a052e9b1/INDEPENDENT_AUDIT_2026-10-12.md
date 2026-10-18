# Independent mathematical audit

## correctness

PASS

PASS. Actual RESULT.md blob c100b8c3404ab4c772fa56b3d8f1671cc3541968 inspected. For 0<lambda<1, q>1, inverse branches have strictly separated intervals I_n and contraction ratios r_n=lambda*n^(-q)/zeta(q). Finite N>=2 similarity dimension is the unique root of sum_{n<=N}r_n^s=1; full countable dimension equals the root c(q)^s zeta(qs)=1, rigorously by finite-subsystem lower bounds and arbitrarily deep cylinders for the upper bound, without assuming compact finite alphabet. Uniform integral comparison for N=floor(exp(tau/epsilon)), q=1+epsilon and bounded a yields epsilon*sum_{n<=N}n^(-1-(1-a-a*epsilon)*epsilon)=integral_0^tau exp((a-1)t)dt+O(epsilon). With c(q)^(1-a epsilon)=lambda*epsilon*(1+O(epsilon*abs(log epsilon))), pressure error O(epsilon*abs(log epsilon)); the phase derivative lambda*integral_0^tau t*exp((a-1)t)dt>0 transfers to dimension error O(epsilon^2*abs(log epsilon)). Laurent expansion at zeta pole gives full-slope 1-lambda. Evaluate phase at a=1 and 1-lambda for strict crossover and positive gap. Fixed N root tends 0; infinite root tends 1. Independent 65-digit mpmath/Hurwitz-zeta root tests at lambda=.3,.65, tau=.8,1.8 and epsilon=.015 reproduced predicted signs and trend; not proof of limit. Threshold tau=1/lambda correctly excludes a second-order sign.

## originality

PASS

PASS on inspected evidence, not exhaustive priority certification. The pressure/dimension principle is established by Mauldin-Urbanski (1996), and arbitrary subsystem dimension spectra are studied by Das-Simmons (2022), but those general results do not state the normalized zeta-pole double scaling for a jointly varying exponent and exponentially growing finite alphabet. Cunha-Novaes-Ponce 2026 studies other countable-branch maps and an Appendix B.1 geometric-block affine model, not the Zipf harmonic pole/finite cutoff law. Thus the substantive first-order phase and noncommuting-order quantification are separately proved rather than credited to standard pressure. Resultary was unavailable, not evidence of novelty.

## value

PASS

PASS. A naturally motivated critical boundary q downarrow 1 of a normalized infinite-alphabet similarity model has a singular normalization and nonuniform finite-alphabet approximation. The explicit dimension crossover on scale N~exp(tau/(q-1)), sharp crossing tau=1/lambda, and positive first-order truncation bias are nontrivial uniform asymptotic data potentially needed for symbolic approximations. This goes materially beyond restating the classical pressure equation or reporting a finite experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
