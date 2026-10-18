# Independent mathematical audit

## correctness

PASS

For scalar y prime=-lambda y and x=lambda h>0, randomized RK2 multiplier p_x(t)=1-x+x² t. Pair U and 1-U with U iid Uniform[0,1] across pairs; V=U-1/2 gives product Z=(m+bV)(m-bV)=m²-b²V² for m=1-x+x²/2, b=x². Uniform moments EV²=1/12, EV⁴=1/80 yield QA=m^4-b²m²/6+b⁴/80; independent stages have QI=(m²+b²/12)². Symbolic expansion independently verified QI-QA=b²(60m²-b²)/180>0 since 4m-b=(x-2)²>=0 and m>0. Independently factored QA-1=x H(x)/30 with H=x^7-10x^6+50x^5-140x^4+250x^3-300x²+240x-120; rational Sturm variations 4 at 0 and 3 at +infinity show unique positive root alpha=1.89655306233598... . Baseline F<1 ends at beta=1.59607163798332... . Exact rational witness x=9/5: QA=2551507/3906250<1<QI=935089/390625. Consecutive stages share marginal law, so independent-pair SLLN gives same logarithmic per-step Lyapunov exponent as iid (including integrable isolated log zeros). Even-step and odd-step mean-square formulas follow from independent pair products. This does not claim nonautonomous/vector/nonlinear RK stability.

## originality

PASS

The source randomized two-stage Runge--Kutta scheme uses independent uniform stages and obtains its original iid mean-square boundary. Coupling adjacent stages antithetically preserves marginals but changes second moments; the 2024 implicit two-stage randomized RK has a different multiplier. General antithetic variates motivation alone does not derive this global strict algebraic inequality, degree-seven exact boundary, or equality of the Lyapunov exponent. No source/resultary hit proves this precise full scalar paired claim.

## value

PASS

A coupling that leaves one-step distribution and almost-sure exponential rate unchanged nevertheless creates an exact and sizable 1.596... to 1.896... mean-square stability extension. This is a sharp stochastic numerical-stability boundary with a rational witness and a design principle for dependent randomization, not a routine formula restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
