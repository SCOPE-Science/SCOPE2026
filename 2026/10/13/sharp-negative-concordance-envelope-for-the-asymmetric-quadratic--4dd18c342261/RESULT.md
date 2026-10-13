# Sharp negative concordance envelope for the asymmetric quadratic copula scheme
## Finding
Consider the asymmetric bivariate copula construction of Bentoumi, El Ktaibi and Chesneau (2025):
\[
C_\phi(u,v)=uv\,[u+(1-u)\phi(v)],\qquad (u,v)\in[0,1]^2.
\]
The tuning function is differentiable on \((0,1)\), satisfies \(\phi(1)=1\) and \(\phi(v)\le1\), and obeys
\[
\lim_{v\downarrow0}v\phi(v)=0,\qquad
\phi(v)+v\phi'(v)\ge0,\qquad
v\phi'(v)\le1.
\]
We require that the resulting function be a **genuine continuous copula**, which entails the necessary endpoint consistency
\[
\lim_{v\uparrow1}\phi(v)=\phi(1)=1.
\]
This continuity is not formally guaranteed by the proposition's interior derivative inequalities alone: the function equal to zero for \(v<1\) and set to one at \(v=1\) satisfies those written inequalities but makes the proposed expression discontinuous at the upper boundary. The exact theorem here concerns genuine copulas, excluding such discontinuous formal expressions. No additional interior monotonicity or CDF restriction is imposed.

**The exact attainable concordance set** over all genuine continuous copulas in this differentiable class is
\[
\boxed{\left\{(\rho_S,\tau_K):\quad
\rho_S\in\left(-\frac{1-e^{-2}}2,0\right],\quad
\tau_K=\frac23\rho_S\right\}.}
\]
In particular,
\[
-\frac{1-e^{-2}}2=-0.432332358381693654\ldots
\]
is the *unattained sharp lower endpoint* for Spearman's rho, while
\[
-\frac{1-e^{-2}}3=-0.288221572254462436\ldots
\]
is the corresponding endpoint for Kendall's tau. Independence realizes the common upper endpoint zero.

The source develops twelve examples and studies four of them in its association-measure tables. The four extensively studied families have negative Spearman range only \([-1/3,0]\) and Kendall range only \([-2/9,0]\). The full differentiable scheme is strictly more expressive: smooth admissible choices realize any negative Spearman value above the sharper global lower endpoint, including values strictly below \(-1/3\). Nevertheless, no member can realize Spearman rho at or below the lower endpoint, and every member is constrained to the rank-correlation line \(\tau_K=(2/3)\rho_S\).

The Spearman–Kendall ratio itself is **not claimed as novel**: it is a known property of quadratic-section and generalized rank-one copulas. The new result is the scheme-specific *optimal negative-dependence bound and its sharpness*, which use the source's extra derivative restriction.

## Assumptions and scope
All tuning functions satisfy the stated inequalities and differentiability throughout \((0,1)\), and have \(\lim_{v\uparrow1}\phi(v)=1\) as required for the result to be a continuous copula. The value at zero is relevant only through the limit \(v\phi(v)\to0\). Mere interior differentiability and the isolated assignment \(\phi(1)=1\), without continuity, would be insufficient to guarantee a copula and are not admitted as counterexamples to this result.

The claims concern population Spearman's rho and Kendall's tau for the copula \(C_\phi\); they do not assume normal or other particular marginal distributions. The sharp lower values are infima rather than attained minima. The conclusion excludes stronger negative concordance only **inside the source's particular scheme**, not for arbitrary asymmetric or general quadratic-section copulas.

## Proof
Put
\[
D(v)=v[1-\phi(v)],\qquad C_\phi(u,v)=uv-u(1-u)D(v).
\]
Because \(v\phi(v)\to0\) and \(\phi(v)+v\phi'(v)\ge0\), the function \(v\phi(v)\) is nondecreasing from a zero boundary value. Therefore
\[
\phi(v)\ge0\quad(0<v<1).
\]
Coupled with \(\phi(v)\le1\), this yields \(0\le\phi(v)\le1\). Integrating \(\phi'(t)\le1/t\) from \(v\) to \(b<1\), then using \(\phi(b)\to1\) as \(b\uparrow1\), gives
\[
1-\phi(v)\le-\log v.
\]
Consequently
\[
\boxed{\max\{0,1+\log v\}\le\phi(v)\le1.}
\]

Set
\[
I=\int_0^1D(v)\,dv=\int_0^1v[1-\phi(v)]\,dv.
\]
Since \(0\le\phi\le1\), the integral is finite and nonnegative. With \(C_\phi=uv-u(1-u)D(v)\), direct integration yields
\[
\rho_S=12\int_0^1\int_0^1C_\phi(u,v)\,du\,dv-3=-2I.
\]
The bound above implies
\[
I\le\int_0^{e^{-1}}v\,dv+
\int_{e^{-1}}^1(-v\log v)\,dv
=\frac{1-e^{-2}}4.
\]
Hence
\[
\rho_S\ge-\frac{1-e^{-2}}2.
\]

The endpoint cannot be attained by a differentiable \(\phi\). Equality in the integral requires
\[
\phi(v)=\phi_0(v):=\max\{0,1+\log v\}
\]
for almost all \(v\in(0,1)\). Since \(\phi\) is continuous in the open interval, equality almost everywhere against the continuous function \(\phi_0\) forces equality everywhere. But \(\phi_0\) has unequal left and right derivatives at \(v=e^{-1}\), contradicting differentiability. Thus the lower bound is strict.

Next, differentiate the copula. Since \(D'=1-\phi-v\phi'\) and the source's conditions imply \(-1\le D'\le1\), the function \(D\) is absolutely continuous on \([0,1]\) with \(D(0)=D(1)=0\). Its density is
\[
c(u,v)=1-(1-2u)D'(v).
\]
Integrating first in \(u\) gives
\[
\int_0^1C_\phi(u,v)c(u,v)\,du
=\frac v2-\frac{D(v)}6+\frac{vD'(v)}6.
\]
Integration by parts, using both endpoint values of \(D\), yields
\[
\int_0^1\int_0^1C_\phi(u,v)c(u,v)\,du\,dv
=\frac14-\frac I3.
\]
Thus
\[
\tau_K=4\int_0^1\int_0^1C_\phi c\,du\,dv-1
=-\frac{4I}3=\frac23\rho_S.
\]

For sharpness, for each \(\varepsilon>0\) define
\[
\phi_\varepsilon(v)=\varepsilon\log\!\left[1+
(e^{1/\varepsilon}-1)v^{1/\varepsilon}\right],
\quad v\in(0,1],\qquad
\phi_\varepsilon(0)=0.
\]
This is a continuous increasing CDF on \([0,1]\), smooth on \((0,1)\), with \(\phi_\varepsilon(1)=1\), and
\[
v\phi_\varepsilon'(v)
=\frac{(e^{1/\varepsilon}-1)v^{1/\varepsilon}}
{1+(e^{1/\varepsilon}-1)v^{1/\varepsilon}}\in(0,1).
\]
All four source conditions therefore hold, including \(\phi_\varepsilon+v\phi_\varepsilon'\ge0\). The elementary soft-maximum limit yields, for each fixed \(v>0\),
\[
\lim_{\varepsilon\downarrow0}\phi_\varepsilon(v)
=\max\{0,1+\log v\}.
\]
Dominated convergence then gives
\[
\lim_{\varepsilon\downarrow0}\rho_S(C_{\phi_\varepsilon})
=-\frac{1-e^{-2}}2.
\]
As \(\varepsilon\to\infty\), \(\phi_\varepsilon(v)\to1\) for every fixed \(v>0\), and the resulting Spearman rho tends to zero. The integral defining rho depends continuously on positive \(\varepsilon\), so by the intermediate value theorem this one smooth family realizes every rho strictly between the lower endpoint and zero. Finally \(\phi\equiv1\), which satisfies the original Proposition 3.1 conditions, gives \(C_\phi(u,v)=uv\), achieving rho and tau equal to zero. This proves the exact attained joint range.

## Verification
The included reproducibility script symbolically recomputes the inner Kendall integral and the envelope integral, checks the soft-maximum family's exact derivative formula, and verifies the sharp constants. High-precision quadrature for a sequence of decreasing \(\varepsilon\) numerically approaches the unattained endpoint. The numerical experiments are supplementary; the proof of sharpness for infinitely many admissible functions is the analytical argument above.

## Relationship to prior work
The authors disclosed the same copula form in a conference abstract for the 20–22 February 2025 International Conference on Mathematics and Statistics, before its later complete journal publication. The primary 2025 journal article proves the copula construction in Proposition 3.1, lists twelve examples, and computes association values for four representative families in Tables 1–2. It notes the general negative-dependence ordering \(\rho_S\le\tau_K\le0\) and observes \(\tau_K=(2/3)\rho_S\) for the four tabulated examples. It does **not** determine the exact concordance range over all admissible tuning functions or exhibit the differentiable family approaching the optimal lower endpoint.

Rodríguez-Lallena and Úbeda-Flores (2010) provide a substantially broader theory of copulas quadratic in one variable. Their Corollary 3 explicitly yields \(\rho_S=(3/2)\tau_K\) for bivariate margins. This earlier result already implies the ratio for the current rank-one structure. Their Theorems 1 and 6 characterize general quadratic-section functions via bounded variation/derivative conditions, but they do not impose this 2025 paper's tuning-function restriction \(v\phi'(v)\le1\) or calculate the sharp logarithmic-obstacle bound for the 2025 subclass. Their 2008 work concerns the general quasi-copula construction, not this scheme-specific optimum.

Amblard and Girard (2011) study symmetric semiparametric generalized FGM copulas, again supplying established rank-one dependence structure, but not the asymmetric 2025 derivative-constrained sharp minimum. Nadarajah and Nawa (2025) survey dependence measures for large families of copulas; the present result supplies a constrained optimal range for a specific later copula scheme, not merely a formula for rho or tau.

Targeted source-identifier, exact-constant, quadratic-section, generalized-FGM, logarithmic-obstacle, rank-correlation equivalence, and smooth-extremizer searches did not reveal this precise sharp restriction in the checked literature.

## Limitations
The optimal bound is not a universal copula concordance bound; more negatively associated copulas exist outside the particular derivative-constrained family.

The lower endpoint is not achievable by an interior-differentiable tuning function generating a genuine copula, although it can be approximated arbitrarily closely by the explicit smooth CDF family. The endpoint's lack of attainability is sensitive to requiring differentiability at every interior point.

The result characterizes only the pair \((\rho_S,\tau_K)\); it does not claim to characterize attainable Gini gamma, Blomqvist beta, tail dependence, or the full copula in terms of rank correlations.

A recently circulated or unindexed mathematical note could have proved this exact sharp envelope without appearing in the checked sources.

## References
1. R. Bentoumi, F. El Ktaibi and C. Chesneau, “A new scheme for simple asymmetric bivariate copulas and applications,” *AIMS Mathematics* 10 (2025), 24602–24626. DOI: 10.3934/math.20251091.
2. J. A. Rodríguez-Lallena and M. Úbeda-Flores, “Multivariate copulas with quadratic sections in one variable,” *Metrika* 72 (2010), 331–349. DOI: 10.1007/s00184-009-0256-1.
3. J. A. Rodríguez-Lallena and M. Úbeda-Flores, “Quasi-copulas with quadratic sections in one variable,” *Kybernetika* 44 (2008), 879–890. Open text: https://www.kybernetika.cz/content/2008/6/879/paper.pdf.
4. C. Amblard and S. Girard, “Symmetry and dependence properties within a semiparametric family of bivariate copulas,” arXiv:1103.5953 (2011).
5. S. Nadarajah and V. Nawa, “A compendium of expressions for dependence measures of bivariate copulas,” *AIMS Mathematics* (2025). DOI: 10.3934/math.2025995.
6. R. Bentoumi, F. El Ktaibi and C. Chesneau, “Exploring a new theoretical scheme to construct simple asymmetric bivariate copulas: Application to Abu Dhabi climatological data,” *Book of Abstracts*, Fourth International Conference on Mathematics and Statistics, Sharjah, 20–22 February 2025, p. 227, American University of Sharjah, https://www.aus.edu/sites/default/files/book_of_abstracts_0.pdf.
