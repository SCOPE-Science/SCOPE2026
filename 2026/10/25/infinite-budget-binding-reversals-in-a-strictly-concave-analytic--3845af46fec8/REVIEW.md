# Independent mathematical audit

## correctness

PASS

u(x)=log(1+x)+(1-cos(log(1+x)))/4 is real analytic, u_prime=e^-t(1+sin(t)/4)>0, u_doubleprime=e^-2t[-1+(cos(t)-sin(t))/4]<0 for t=log(1+x). Price lambda(t) decreases, clipped demand min(e^t-1,1/lambda) increases, hence Theta=lambda/d is continuous strictly decreasing from infinity to zero and each Theta>0 has unique equilibrium. Binding inequality is sin t>4/(e^t-1). On every I_k=(2k*pi,(2k+1)*pi), k>=1, h has negative endpoints, positive midpoint and h_doubleprime= -sin t-4 e^t(e^t+1)/(e^t-1)^3<0, so two simple roots and a binding interval; negative-sine half-periods slack. Endpoint offsets asymptotic to 4e^-m*pi, and at equality Theta=(e^t-1)^-2, so consecutive cost threshold ratio tends to e^-2pi. Independently computed first five positive half-period crossings at high precision, first roots 6.2906136333,9.4244550324, and the last threshold ratio 0.00186744273170826 against e^-2pi=0.00186744273170799. Numerical roots cannot certify infinite alternation, which follows from analytic concavity.

## originality

PASS

Perkins–Zhang 2026 prove general budgeted equilibrium existence/uniqueness and demand clipping and show quadratic/square-root examples with one or two crossover thresholds. The explicitly increasing analytic strictly concave utility here has infinitely many endogenously ordered budget crossings with geometric cost accumulation, not forced by their comparison theorems. Unindexed oscillatory examples remain a priority risk.

## value

PASS

An explicit analytic strictly concave counterexample to any universal finite budget-switch count is a meaningful boundary of single-commodity comparative statics. The exact geometric accumulation rate is mathematically informative beyond a hand-drawn oscillation; it does not claim economic empirical realism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
