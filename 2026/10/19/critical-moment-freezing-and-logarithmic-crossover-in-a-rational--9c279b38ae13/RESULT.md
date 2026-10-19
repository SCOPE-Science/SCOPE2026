# Critical moment freezing and logarithmic crossover in a rational Chebyshev family

## Finding
For every integer \(N\geq2\), the rational Chebyshev interval map defined below has a stationary probability measure whose concentration at the fixed point \(x=1\) obeys a universal, sharp moment-response transition. Let \(\varepsilon=N-\alpha\downarrow0\), where \(\alpha\) is approached along the invariant-density parameter branch, and put \(K_N=N(N^2-1)/3\). If \(G=1-X\) for a stationary random state \(X\), then \(K_NG/\varepsilon\) converges to the square of a standard positive half-Cauchy variable. Yet the stationary moments \(M_q=\mathbb E[G^q]\), for every real \(q>0\), exhibit three distinct regimes:

\[
M_q\sim\begin{cases}
\displaystyle\frac{(\varepsilon/K_N)^q}{\cos(\pi q)},&0<q<\frac12,\\[4pt]
\displaystyle\frac{\sqrt{\varepsilon/K_N}}{\pi}\log\!\frac{K_N}{\varepsilon},&q=\frac12,\\[4pt]
\displaystyle\frac{\Gamma(q-\frac12)}{\sqrt\pi\,\Gamma(q)}\sqrt{\varepsilon/K_N},&q>\frac12.
\end{cases}
\]

The boundary at \(q=1/2\) has a full *double-scaling crossover*: with \(L=\log\beta\), \(q=1/2+s/L\), and fixed real \(s\),
\[
\lim_{\beta\to\infty}\frac{\pi\sqrt\beta}{\log\beta}\,\mathbb E[G^{\frac12+s/\log\beta}]
=H(s):=\begin{cases}(1-e^{-s})/s,&s\ne0,\\1,&s=0,\end{cases}
\]
uniformly for \(s\) in every compact real interval. These are quantitative statements about *spatial stationary observables*, not mixing-time or entropy asymptotics.

## Assumptions and scope
Write \(T_N\) for the first-kind Chebyshev polynomial and define, for \(x\in[0,1]\), \(\alpha>0\),
\[
F_{N,\alpha}(x)=\frac{\alpha^2T_N(\sqrt x)^2}{1+(\alpha^2-1)T_N(\sqrt x)^2}.
\]
For \(\beta>0\) define the positive parameter
\[
\alpha_N(\beta)=\frac{\displaystyle\sum_{j\ge0:\,2j+1\le N}\binom N{2j+1}\beta^{-j}}{\displaystyle\sum_{j\ge0:\,2j\le N}\binom N{2j}\beta^{-j}}.
\]
The invariant probability \(\mu_{N,\beta}\) has the density, already given in the originating work [1],
\[
\rho_\beta(x)=\frac{\sqrt\beta}{\pi\sqrt{x(1-x)}\,[\beta+(1-\beta)x]},\qquad0<x<1.
\]
Here \(N\) is fixed, \(\beta\to\infty\), \(\alpha=\alpha_N(\beta)\), and hence \(\alpha\uparrow N\) from below. The claim makes no assertion about uniqueness of invariant measures at the boundary \(\alpha=N\), nor about time-correlation decay. The same density for all degrees is known; the exact concentration, complete moment regime classification, and uniform crossover are the present claims.

## Proof
**(1) Independently recover stationarity and its exact probabilistic coordinate.** Let \(U\) have the standard positive half-Cauchy density \(2/[\pi(1+u^2)]\), \(u>0\), and put
\[
X=\frac\beta{\beta+U^2},\qquad G=1-X=\frac{U^2}{\beta+U^2}.
\]
Changing variables gives precisely \(\rho_\beta\); this proves normalization. For a direct invariance argument, let \(V\) be a symmetric Cauchy variable of scale \(\tau=\beta^{-1/2}\), and set \(Z=(1+iV)/(1-iV)\). Its circle distribution is Poisson harmonic measure with real pole \(p=(1-\tau)/(1+\tau)\): in particular \(\mathbb E[Z^k]=p^k\) for all integers \(k\ge0\). Consequently \(Z^N\) has Poisson harmonic measure with pole \(p^N\), so \(\tan(N\arctan V)\) has the symmetric Cauchy law of scale
\[
\tau_N=\frac{1-p^N}{1+p^N}.
\]
The binomial identity \(\tau_N/\tau=\alpha_N(\beta)\) follows immediately. Since \(F_{N,\alpha}\) acts on \(Y=\sqrt{(1-X)/X}\) by \(Y\mapsto\alpha^{-1}|\tan(N\arctan Y)|\), the Cauchy calculation proves invariance of the half-Cauchy coordinate, hence of \(\mu_{N,\beta}\) for every \(N\ge2\), \(\beta>0\). No ergodicity assertion is needed.

**(2) The degree-dependent parameter scale and exact excursion law.** Taylor expansion of the finite binomial sums, using \(\binom N3/N-\binom N2=-(N^2-1)/3\), gives
\[
\alpha_N(\beta)=N-\frac{K_N}{\beta}+O_N(\beta^{-2}),\qquad K_N=\frac{N(N^2-1)}3.
\]
Thus \(\beta\varepsilon\to K_N\). The same coupling \(U\) for all \(\beta\) yields \(\beta G\to U^2\) almost surely, hence \(K_NG/\varepsilon\Rightarrow U^2\). The limiting density is \(z^{-1/2}/[\pi(1+z)]\), \(z>0\). Exactly, for any \(0<r<1\),
\[
\Pr\{G>r\}=\frac2\pi\arctan\sqrt{\frac{1-r}{\beta r}}.
\]
Thus for fixed \(r\), \(\sqrt\beta\Pr\{G>r\}\to(2/\pi)\sqrt{(1-r)/r}\), whereas for windows \(r=t/\beta\), \(\Pr\{G>t/\beta\}\to(2/\pi)\arctan(t^{-1/2})\). These formulas explicitly separate fixed-distance rare mass from the concentrating boundary layer.

**(3) Complete moment regimes.** For real \(q>0\), the exact representation reads
\[
M_q(\beta)=\frac2\pi\int_0^\infty\frac{\bigl(u^2/(\beta+u^2)\bigr)^q}{1+u^2}\,du.
\]
If \(0<q<1/2\), dominated convergence applied after multiplication by \(\beta^q\) gives \(\beta^q M_q\to\mathbb E[U^{2q}]=1/\cos(\pi q)\). If \(q>1/2\), substitute \(u=\sqrt\beta\,v\) and use dominated convergence to obtain
\[
\sqrt\beta\, M_q\to\frac2\pi\int_0^\infty\frac{v^{2q-2}}{(1+v^2)^q}\,dv
=\frac{\Gamma(q-\frac12)}{\sqrt\pi\,\Gamma(q)}.
\]
At \(q=1/2\), the intermediate interval \(1\le u\le\sqrt\beta\) has leading integrand \(2/(\pi\sqrt\beta\,u)\), so \(M_{1/2}\sim(\log\beta)/(\pi\sqrt\beta)\). Substituting \(\beta\sim K_N/\varepsilon\) proves the displayed three regimes.

**(4) Uniform critical crossover.** Let \(L=\log\beta\) and \(q=1/2+s/L\), with \(s\) ranging over a fixed compact set. Split the exact moment integral at \(u=1\) and \(u=\sqrt\beta\). The outer intervals contribute \(O(\beta^{-1/2})\) uniformly. On the middle interval, replacing \((1+u^2)^{-1}\) by \(u^{-2}\), and \((1+u^2/\beta)^{-q}\) by \(1\), incurs total error \(O(\beta^{-1/2})\), uniformly: the two errors are respectively bounded by constant multiples of \(\beta^{-q}\int_1^\infty u^{2q-4}du\) and \(\beta^{-q-1}\int_1^{\sqrt\beta}u^{2q}du\). The remaining integral is **exactly**
\[
\frac2\pi\beta^{-q}\int_1^{\sqrt\beta}u^{2q-2}\,du
=\frac{\log\beta}{\pi\sqrt\beta}\,H(s).
\]
The uniform error is smaller by a factor \(\log\beta\); this establishes the claimed crossover, including \(s=0\).

**(5) A sharp stationary-response consequence.** Direct integration gives \(M_1=1/(1+\sqrt\beta)\) exactly. Therefore
\[
1-\int x\,d\mu_{N,\beta}(x)\sim\sqrt{\frac{N-\alpha_N(\beta)}{K_N}}.
\]
The stationary mean has a square-root cusp on approach to the fixed-point parameter: its one-sided derivative does not have a finite limit. In particular the leading rate for a smooth observable is not captured by the central-scale limit alone.

## Verification
Run `python check.py` using Python, SymPy, and mpmath. It checks the binomial Taylor coefficient **exactly** for degrees \(2\) through \(12\), tests the exact \(q=1\) moment formula, computes positive-half-Cauchy integrals in both sides of the \(q=1/2\) transition, and checks the published invariance identity for degrees \(2,3,5\) against polynomial test observables. All finite tests reported `VERIFY_OK`. The infinite-degree, infinite-parameter and uniform-crossover claims rest on the preceding analytic proof, **not** on those tests.

## Relationship to prior work
Jafarizadeh, Behnia, Khorram and Naghshara [1] introduced \(F_{N,\alpha}\), derived the stationary density and its parameter relation, and computed entropy. Jafarizadeh and Behnia [2] studied compositions and associated entropy universality classes. All of those facts are attributed, not claimed new. The statements here quantify stationary concentration along the neutral endpoint through the exact excursion law, the sharp \(q=1/2\) moment transition, and its locally uniform logarithmic crossover. The linear-response work of Baladi and Smania [3] concerns parameter deformations with different dynamical hypotheses, not this loss-of-acim endpoint.

## Limitations
This is a one-sided stationary result for a specific exactly solvable interval-map hierarchy, not a generic theorem for maps near an indifferent fixed point. The density and the parameterization originate in [1]. The moment laws follow from a nontrivial *combined* parameter-and-observable scaling of that known density, so originality concerns those asymptotic classifications, **not** the density or the underlying Cauchy distribution. General beta-prime moment identities provide a possible prior mathematical equivalent at the distribution level; they do not by themselves specify the dynamical parameter correspondence. Independent historical priority assessment has not been performed. All asymptotics hold with \(N\) fixed; no joint limit \(N\to\infty\) is asserted.

## References
[1] M. A. Jafarizadeh, S. Behnia, S. Khorram, H. Naghshara, *Hierarchy of Chaotic Maps with an Invariant Measure*, arXiv:nlin/0003036v1, publicly posted 14 March 2000; equations (2-1), (3-3), (3-4).

[2] M. A. Jafarizadeh, S. Behnia, *Hierarchy of Chaotic Maps with an Invariant Measure and their Compositions*, Journal of Nonlinear Mathematical Physics 9 (2002), 26–41; arXiv:nlin/0210043v1.

[3] V. Baladi, D. Smania, *Linear response for smooth deformations of generic nonuniformly hyperbolic unimodal maps*, Ann. Sci. Éc. Norm. Supér. 45 (2012), 861–926, doi:10.24033/asens.2179.
