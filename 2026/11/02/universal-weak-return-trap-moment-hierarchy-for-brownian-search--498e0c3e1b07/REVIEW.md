# Independent mathematical audit

## correctness

PASS

The killed search resolvent gives interruption density rho_r(x)=sqrt(r)/2(e^{-sqrt(r)|x|}-e^{-sqrt(r)(2-x)}) for x<1. Optional stopping yields p_0=e^{-sqrt r}+int_0^1 x rho_r(x)dx=H_r=int_{x<0}(-x)rho_r(x)dx=(1-e^{-2sqrt r})/(2sqrt r). The OU return from negative distance y has exact time-change law tau_k(y)=(2k)^{-1}log(1+k y²/Z²), Z standard normal, giving k^{n-1/2} E[tau_k(y)^n]→c_n y by an integrable logarithmic kernel and dominated convergence. Positive-side return durations have uniformly bounded moments on [0,1]; negative-side return alone contributes H_r c_n to the cycle n-th moment. The renewal recursion p_k M_n=E[C^n]+sum_{1≤j<n}binom(n,j)E[C^{n-j}F]M_j makes cross-cycle terms O(k^{-(n-1)}) vs leading k^{-(n-1/2)}, proving all integer n≥1 for FIXED r>0. c1=√(π/2), c2=√(2π)log2, variance leading order k^{-3/2}; at k=0 the unmodified Brownian hitting time has infinite mean. Independently integrated the killed-resolvent martingale identity at four r values and evaluated the universal constants. No numerical result substitutes for the n-induction or uniform moment bound.

## originality

PASS

The first-moment problem and OU hitting-time laws are known; the nontrivial addition is the complete all-integer moment weak-stiffness exponent hierarchy, sharp variance and cancellation of reset-rate dependence. Best-of-knowledge priority remains qualified because a more general renewal-asymptotic paper might entail this combination.

## value

PASS

The divergence of all moments at distinct half-integer powers, a universal interruption-rate-independent amplitude, and a sharply divergent coefficient of variation expose a mathematically natural singular return-to-unconfined-Brownian transition; variance alone is not fixed by prior mean formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
