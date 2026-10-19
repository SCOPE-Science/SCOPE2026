# Conditional skewness sign transition in the Kaplan–Yorke map

## Finding
Consider the Kaplan–Yorke skew-product map
\[
T_\alpha(x,y)=(2x\bmod 1,\;\alpha y+\cos(4\pi x)),\qquad -1<\alpha<1.
\]
For every invariant Borel probability measure \(\mu\) with Lebesgue first-coordinate marginal and compact vertical support, let \(X,Y\) be the coordinate variables and let \(\kappa_3(x)=\mathbb E_\mu[(Y-\mathbb E_\mu[Y\mid X])^3\mid X=x]\). Then for Lebesgue-almost every \(x\),
\[
\boxed{\kappa_3(x)=\frac{3\alpha^5}{4}\left(\frac{1}{1-\alpha^3}+\cos(2\pi x)\right).}
\]
For \(\alpha\ne0\), the conditional variance satisfies \(v(x)\ge\alpha^4/[2(1-\alpha^2)]>0\), so the signs below are also exactly the signs of standardized conditional skewness. At \(\alpha=0\) the standardized skewness is undefined because the fibers are deterministic.

This gives a sharp *signed-contraction dichotomy*. For \(0<\alpha<1\), the conditional third centered moment is strictly positive almost everywhere. For \(\alpha=0\), it is zero. For \(-1<\alpha<0\), put \(r=-\alpha\). It is positive exactly on
\[
\cos(2\pi x)<-\frac{1}{1+r^3},
\]
negative on the complementary strict-inequality region, and zero at two boundary points (up to null-set choice of the conditional law). Its positive-fiber Lebesgue proportion is exactly
\[
\boxed{p(r)=1-\frac1\pi\arccos\!\left(-\frac1{1+r^3}\right)},\qquad 0<r<1,
\]
and increases strictly from \(0\) to the limiting value \(1/3\).

Moreover,
\[
\mathbb E[Y]=0,\quad \operatorname{Var}(Y)=\frac1{2(1-\alpha^2)},\quad
\mathbb E[Y^3]=\frac{3\alpha^2}{4(1-\alpha^3)}.
\]
Thus the pair \((\operatorname{Var}(Y),\mathbb E[Y^3])\) uniquely determines \(\alpha\in(-1,1)\), whereas the entire conditional first- and second-moment profiles are identical for the two parameters \(\alpha=r\) and \(\alpha=-r\). Even for negative \(\alpha\), the global third moment is positive while the conditional third moment is negative on a majority of fibers.

## Assumptions and scope
The base coordinate \(x\) belongs to the circle \(\mathbb T=\mathbb R/\mathbb Z\), but the fiber coordinate \(y\) is *not* reduced modulo one. For each \(|\alpha|<1\), the strip \(|y|\le (1-|\alpha|)^{-1}\) is forward invariant; a compactly supported stationary law with Lebesgue base marginal exists from the natural inverse-history construction. The theorem concerns any such invariant law, not arbitrary stationary measures whose base marginals are non-Lebesgue. A finite absolute third-moment assumption can replace compact support.

We use conditional moments as equivalence classes of functions defined Lebesgue-almost everywhere, so sign regions and their proportions are statements modulo null sets. No density or absolute continuity of the joint invariant law is assumed.

## Proof
Let \(P\) be the Perron operator for the doubling map with respect to normalized Lebesgue measure:
\[
(Pf)(x)=\tfrac12\left[f(x/2)+f((x+1)/2)\right].
\]
Write \(c(x)=\cos(2\pi x)\) and \(m_j(x)=\mathbb E[Y^j\mid X=x]\). Both inverse base branches produce the same new forcing \(\cos(4\pi u)=c(x)\). Invariance therefore implies for \(j=1,2,3\)
\[
m_j(x)=\sum_{k=0}^{j}\binom jk c(x)^{j-k}\alpha^k(Pm_k)(x),\qquad m_0=1.
\]
The operator \(P\) has norm at most one on \(L^\infty\). Hence for each \(j\), since \(|\alpha|<1\), the equation for \(m_j\) has a unique bounded solution once the lower moments are fixed.

For the first moment, \(m_1=c+\alpha Pm_1\). Since \(Pc=0\), uniqueness yields \(m_1=c\). For the second, \(m_2=c^2+\alpha^2Pm_2\). Using \(Pc^2=(1+c)/2\), \(P^2c^2=1/2\), and a Neumann series, we obtain
\[
m_2=c^2+v,\qquad v(x)=\frac{\alpha^2}{2}\left(\frac1{1-\alpha^2}+c(x)\right).
\]
The same identity gives \(\alpha^2Pm_2=v\). Expand the third-moment equation:
\[
m_3=c^3+3\alpha c^2Pm_1+3\alpha^2 cPm_2+\alpha^3Pm_3
=c^3+3cv+\alpha^3Pm_3.
\]
Set \(g=c^3+3cv\). Its Fourier-cosine expansion contains only modes of order at most three, with constant coefficient \(g_0=3\alpha^2/4\) and second-harmonic coefficient \(g_2=3\alpha^2/4\). Indeed, the odd cube \(c^3\) has only first and third harmonics, and the second harmonic in \(3cv\) comes from \(3\alpha^2c^2/2\). On Fourier cosines, \(P\cos(2\pi n x)=0\) for odd \(n\), and \(P\cos(2\pi n x)=\cos(2\pi (n/2)x)\) for even \(n\). Consequently,
\[
Pg=g_0+g_2c,\qquad P^kg=g_0\quad(k\ge2).
\]
The exact inverse of \(I-\alpha^3P\), justified by \(|\alpha|<1\), now gives
\[
Pm_3=P(I-\alpha^3P)^{-1}g
=\frac{g_0}{1-\alpha^3}+g_2c.
\]
Subtracting the conditional mean and variance terms from \(m_3\) gives
\[
\kappa_3=m_3-3m_1m_2+2m_1^3=m_3-c^3-3cv=\alpha^3Pm_3,
\]
which is exactly the boxed formula.

For \(\alpha>0\), the factor \(3\alpha^5/4\) is positive and the parenthesis is at least \(\alpha^3/(1-\alpha^3)>0\). For \(\alpha=-r<0\), the parenthesis equals \(1/(1+r^3)+c\); its sign changes at the two points with \(c=-1/(1+r^3)\). The measure of the arc where the conditional third moment is **positive** is \(1-\pi^{-1}\arccos(-1/(1+r^3))\). This fraction is strictly increasing in \(r\), with the asserted limits.

Integrating the conditional moments over the base circle gives the global moments displayed above. Given \(\operatorname{Var}(Y)\), the number \(r=|\alpha|\) is uniquely determined. If \(r>0\), then the two choices of sign have unequal third moments \(3r^2/[4(1-r^3)]\) and \(3r^2/[4(1+r^3)]\). At \(r=0\) only \(\alpha=0\) is possible. This proves identifiability.

## Verification
The self-contained `verify.py` checks the exact rational Fourier-mode recurrences for the first three conditional moments, the cubic centered-moment formula, and the global moment formulas at seven signed rational contraction factors. Its successful output is `VERIFY_OK`. These tests are finite consistency checks only; the preceding operator and Fourier argument proves the statement for every real \(|\alpha|<1\). The proof does not depend on numerical trajectories or the checker.

## Relationship to prior work
Kaplan and Yorke (1979) introduced the classical skew-product setting and studied chaos and dimensions. Liang (2015 preprint, section III.3) gives exactly the same normalization, its two inverse branches, and a Frobenius–Perron computation for information flow, but not a conditional cubic-moment law.

The publicly available result *Exact conditional variance profile of the Kaplan–Yorke stationary measure* (2026) proves the conditional mean and variance for the same invariant-law class. Those two profiles are even in \(\alpha\), and its statement leaves higher conditional moments open. The present cubic formula, the sharp sign-region measure, and the signed-parameter identifiability conclusion are not consequences of the earlier two moment values alone: distinct distributions can share the first two moments, while the third recurrence above exploits an additional exact stationarity identity.

## Limitations
The claim concerns third conditional centered moments and global third moments, not a closed-form conditional distribution, Hausdorff dimension, or arbitrary higher cumulants. The sign diagram requires nonzero contraction and the Lebesgue-base hypothesis. For \(\alpha=0\), the standardized conditional skewness is undefined; only its unstandardized third centered moment is zero.

## References
1. J. L. Kaplan and J. A. Yorke, “Chaotic behavior of multidimensional difference equations,” *Lecture Notes in Mathematics* 730, 204–227 (1979), DOI 10.1007/BFb0064319.
2. X. San Liang, “Information flow and causality as rigorous notions ab initio,” arXiv:1503.08389v1 (29 March 2015), section III.3, https://arxiv.org/html/1503.08389v1.
3. “Exact conditional variance profile of the Kaplan–Yorke stationary measure,” public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-conditional-variance-profile-of-the-kaplan-yorke-stationar--2cc33694c056.
