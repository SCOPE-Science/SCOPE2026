# Independent mathematical audit

## correctness

PASS

The first-attempt killed diffusion has potential w_s(x)=E[e^{-sY}; first termination is a negative reset], satisfying D w''=0 on (0,L), D w''-r w=-r e^{s x} on x<0, boundary w(L)=0, bounded at -infinity and C1 matching at 0. Solving yields w_s(0)=q*kappa/(kappa+s) with kappa=sqrt(r/D), q=kappa L/(1+kappa L); independently checked exact symbolic residuals and both matching conditions, including s=kappa by continuous extension. It follows that failure probability q, conditional mark Exp(kappa), success p. Strong Markov and independent Poisson increments provide iid attempts and conditional iid reset marks, so P(N=n)=p q^n and joint PGF/Laplace p/(1-q z kappa/(kappa+s)). Summed Gamma densities give mass p at C=0, positive density p q kappa exp(-p kappa c), N-1|C=c>0 ~ Poisson(q kappa c), mean L, variance L²+2L/kappa, and exact weak limits. These are exact all D,r,L>0, not sample-based or an assertion at r=0.

## originality

PASS

Tal-Friedman–Keidar–Reuveni–Roichman 2024/2025 *same model* already gives mean energy F0 L and negative-position integrated occupation kernel ~p(x,0)=(L/D)e^{kappa x} (SI Eq S22), which is an important strong precursor. It yields the expected spatial reset intensity and is compatible with the claimed exp mark law, but a first-moment occupation density alone does not establish independence of successive reset depths or the *joint path-level count/cost law*. Their main article/SI compute average costs and first-passage statistics, not these full joint laws or posterior Poisson count. Sunil et al. derive more general renewal transforms for resets at every clock time, a different state-dependent mechanism. The new statement is the one-sided reset-specific joint law and risk/weak-rate asymptotics, with an explicit risk that it may be an algebraically short corollary of a broader uninspected cost-functional theorem.

## value

PASS

The source's reset-rate-independent *mean* hides a sharply rate-dependent full cost law: positive zero-cost atom, exponential positive tail, variance diverging as r^{-1/2}, weak convergence to zero as r->0 despite fixed mean L, and an exactly identified conditional count distribution. These are naturally motivated experimentally relevant fluctuations and a non-uniform-integrability phenomenon, not a re-expression of the previously published average cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
