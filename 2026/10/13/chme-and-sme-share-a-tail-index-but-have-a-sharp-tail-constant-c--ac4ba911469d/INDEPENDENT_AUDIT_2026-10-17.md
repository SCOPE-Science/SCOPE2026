# Independent mathematical audit

## correctness

PASS

For common Y~Gamma(2,beta), CHME X=Y/(2Z) with Z~Beta(q,q) and SME X=Y/U with U~Beta(q,1). A small-Z beta density z^(q-1)/B(q,q) gives K_C=E[Y^q]/(q 2^q B(q,q))=(q+1)2^-q beta^q Gamma(2q)/Gamma(q); SME gives K_S=E[Y^q]=beta^q Gamma(q+2). Thus R=2^-q Gamma(2q)/(q Gamma(q)^2). For q<=1, q B(q,q)>=1, so R<1. For q>=1, dlog R/dq=log2-int_0^inf exp(-qt)/(1+exp(t/2))dt>log2-1/(2q)>0; R(2)=3/4 and R(3)=5/4 yield a unique crossing q*=2.578543315125812... . Positive density asymptotics integrate to survival, giving hazards q/x, moment cutoff r<q, and quantile ratio R^(1/q). At q=1 the two denominators are identically distributed uniforms, so X_C= X_S/2 in distribution. Independent high-precision gamma/beta arithmetic reproduced the root and q=1,2,3 ratios.

## originality

PASS

The 2026 CHME source states heavier-tail motivation and derives a Pareto-type exponent for CHME, but the inspected full paper does not compute its matched-parameter survival leading constant relative to SME, prove a unique crossing, or identify the exact q=1 contraction. The 2017 SME full paper supplies the older marginal model/density. Generic regular-variation and beta-mixture results are inputs, not the same applied comparison. Best-of-knowledge acceptance; an unindexed equivalent comparison remains possible.

## value

PASS

The CHME publication explicitly motivates its new symmetric-beta construction through heavier tails than SME. Its exact regular-variation constant, sharp unique reversal in the direction of extreme-tail probabilities, and exact q=1 stochastic contraction are therefore a scientifically motivated correction to an actual interpretation of the model. The strict crossover, not merely generic shared tail exponents, supplies an actionable mathematical comparison in heavy-tail model choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
