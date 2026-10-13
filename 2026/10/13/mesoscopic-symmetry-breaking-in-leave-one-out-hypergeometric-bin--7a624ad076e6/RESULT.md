# Mesoscopic symmetry breaking in leave-one-out hypergeometric/binomial divergence
## Finding
For integers \(N\ge 3\) and \(1\le K\le N-1\), let \(Q_{N,K}=\operatorname{Hyp}(N,K,N-1)\) and \(P_{N,K}=\operatorname{Bin}(N-1,K/N)\). Define
\[
D_N(K)=D_{\mathrm{KL}}(Q_{N,K}\|P_{N,K}).
\]
With \(p=K/N\) and binary entropy \(H(p)=-p\log p-(1-p)\log(1-p)\),
\[
D_N(K)=-\log\binom NK+(N-1)H(p).
\]
If \(K_N\) is any maximizer over \(1\le K\le N-1\), then
\[
\frac{|K_N-N/2|}{\sqrt N}\longrightarrow\frac12.
\]
The maximal divergence has the sharper expansion
\[
\max_K D_N(K)=\frac12\log\!\left(\frac{\pi N}{8}\right)+\frac1{4N}+\frac1{6N^2}+o(N^{-2}).
\]
The worst population composition therefore breaks exact balance only at the mesoscopic square-root scale.

## Assumptions and scope
The result concerns the standard hypergeometric law obtained by sampling \(N-1\) objects without replacement from a population of \(N\) objects containing \(K\) successes, compared with the matching binomial law for \(N-1\) draws with success probability \(K/N\). Natural logarithms are used. Both colors are required to be present, so \(1\le K\le N-1\). The statement optimizes information divergence over the population composition; it does not optimize other discrepancies such as total variation or maximal density ratio.

## Proof
Omitting one uniformly chosen population item leaves only two possible hypergeometric counts. With \(p=K/N\) and \(q=1-p\),
\[
Q_{N,K}(K-1)=p,\qquad Q_{N,K}(K)=q.
\]
Both matching binomial probabilities are equal to the same binomial-at-its-mean mass:
\[
P_{N,K}(K-1)=P_{N,K}(K)=\binom NKp^Kq^{N-K}.
\]
Indeed, \(\binom{N-1}{K-1}=p\binom NK\) and \(\binom{N-1}{K}=q\binom NK\). Substitution into the definition of relative entropy gives the exact identity
\[
D_N(K)=-\log\binom NK+(N-1)H(p).
\]
It is symmetric under \(K\leftrightarrow N-K\).

For the asymptotics, write \(p=1/2+u\). Stirling's formula with its standard remainder, uniformly for \(|u|\le1/4\), gives
\[
D_N(K)=\frac12\log(2\pi N)+F(u)+\frac{G(u)}N+O(N^{-3}),
\]
where
\[
F(u)=\frac12\log\!\left(\frac14-u^2\right)-H\!\left(\frac12+u\right),
\qquad
G(u)=\frac1{12}\left(\frac1{1/2+u}+\frac1{1/2-u}-1\right).
\]
The power series valid for \(|2u|<1\) is
\[
F(u)-F(0)=-\sum_{m=2}^{\infty}\frac{m-1}{m(2m-1)}(2u)^{2m},
\]
so \(F\) has its unique global maximum at \(u=0\), and locally its first nonzero loss is quartic. Standard two-sided Stirling bounds also give, uniformly for all integer \(K\),
\[
D_N(K)=\frac12\log(2\pi Np(1-p))-H(p)+O\!\left(\frac1K+\frac1{N-K}\right).
\]
Comparison with a central composition shows first that any maximizing sequence has \(p\) bounded away from \(0\) and \(1\); the strict global maximum of \(F\) then forces \(p\to1/2\).

In the central region,
\[
F(u)-F(0)\le-\frac83u^4,
\qquad
G(u)-G(0)=\frac{4u^2}{3(1-4u^2)}.
\]
Comparing a maximizer with the nearest central lattice point yields \(u=O(N^{-1/2})\). Put \(y=\sqrt N\,u\). Uniformly for bounded \(y\),
\[
N^2\left[D_N(K)-\left(\frac12\log(2\pi N)+F(0)+\frac{G(0)}N\right)\right]
=\frac43y^2-\frac83y^4+o(1).
\]
The limiting profile \(\frac43y^2-\frac83y^4\) has exactly two maximizers, \(y=\pm1/2\), each with value \(1/6\). The lattice spacing in \(y\) is \(N^{-1/2}\), so comparison with lattice points converging to either maximizer gives
\[
|y_N|\to\frac12.
\]
Finally, \(F(0)=-2\log2\) and \(G(0)=1/4\), which gives the displayed expansion for the maximal divergence.

## Verification
A standalone regression script accompanies this result. It checks the exact two-point relative-entropy identity against direct probability calculations for many finite parameter pairs and displays the maximizing compositions and their normalized displacement for increasing \(N\). Those finite checks are not used to infer the asymptotic theorem; the infinite claim follows from the analytic localization and uniform Stirling expansion above.

## Relationship to prior work
Harremoës and Matúš study information divergence from hypergeometric to matching binomial laws and prove general upper/lower bounds and asymptotics. Their asymptotic theorem treats a regime in which the unsampled fraction has a fixed limiting scale; the leave-one-out endpoint \(n=N-1\) is not resolved at the composition-sensitive scale by that theorem, and their paper does not state the exact two-point reduction, optimize this endpoint over \(K\), or identify the square-root displacement and \(N^{-2}\) gain reported here. Dümbgen, Samworth, and Wellner study the same hypergeometric/binomial approximation under maximal density ratio, a different discrepancy. At the leave-one-out endpoint that criterion has a different composition geometry, so it does not imply the relative-entropy maximizer described here.

## Limitations
The result is specific to leave-one-out sampling \(n=N-1\) and binary populations. It gives an asymptotic location of all global maximizers, not a closed finite-\(N\) formula for the maximizing integer. It does not claim an analogous square-root law for other sample deficits, multicolor populations, or other discrepancy measures. The literature search did not locate an equivalent statement, but older finite-population approximation literature could contain the same endpoint calculation under different terminology.

## References
Peter Harremoës and František Matúš, “Bounds on the Information Divergence for Hypergeometric Distributions,” Kybernetika 56 (2020), 1111–1132. arXiv:2002.03002v1. DOI: 10.14736/kyb-2020-6-1111.

Lutz Dümbgen, Richard Samworth, and Jon Wellner, “Bounding distributional errors via density ratios,” arXiv:1905.03009v1.
