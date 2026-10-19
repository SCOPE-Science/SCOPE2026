# Quadratic-irrational quantization of sharp cubic maximal norms on complete graphs

## Finding

For every integer \(n\ge2\), equip the complete graph \(K_n\) with normalized counting measure and define the centered maximal operator
\[
 (M_nf)(j)=\max\left\{|f(j)|,\frac1n\sum_{i=1}^n|f(i)|\right\}.
\]
This is also the positive maximal operator of the heat semigroup \(e^{-t}I+(1-e^{-t})P\), where \(P\) projects onto constants. Put
\[
 \Lambda=\frac{613+16\sqrt7}{513},\qquad
 \alpha=\frac{32-4\sqrt7}{57},\qquad
 \kappa=1-\frac{\sqrt7}{14},\qquad
 \|u\|_{\mathbb Z}=\min_{j\in\mathbb Z}|u-j|.
\]
Then the sharp uniform cubic inequality is
\[
 \sum_{j=1}^n(M_nf(j))^3\le\Lambda\sum_{j=1}^n|f(j)|^3,
\]
with strict inequality for every nonzero function on every finite \(K_n\). Its constant is nevertheless optimal uniformly over all \(n\) and is attained on an atomless probability space by precisely the two-level distributions specified below. More sharply, the *optimal* finite-graph constants have the arithmetic asymptotic
\[
 \boxed{\displaystyle
 \Lambda-\|M_n\|_{\ell^3\to\ell^3}^{3}
 =\kappa\frac{\|n\alpha\|_{\mathbb Z}^{2}}{n^{2}}
 \left(1+O\left(n^{-1}\right)\right)}\qquad(n\to\infty).
\]
The implicit constant is absolute and the relative error is uniform even when \(n\alpha\) is exceptionally close to an integer. Consequently, the gap has order \(n^{-2}\) along infinitely many graph sizes and order \(n^{-4}\) along another infinite sequence. In particular every finite size lies strictly below the sharp uniform constant.

## Assumptions and scope

The operators act on complex or real signals, with modulus taken before averaging; nonnegative signals suffice for their norms. The cubic power refers to \(\|M_n\|_3^3\), not \(\|M_n\|_3\). The sharp uniform constant is over all finite complete graphs or all atomless probability spaces, not a claim of finite-size attainment. The assertions are for all integers \(n\ge2\) and the limiting formula as \(n\to\infty\). The leading coefficient \(\kappa\) is exact. Define
\[
 y=\frac32,\qquad z=\frac{1+2\sqrt7}{9},\qquad
 \alpha=\frac{1-z}{y-z}.
\]
The equality distribution on an atomless probability space has the values \(y\mu\) on a set of measure \(\alpha\) and \(z\mu\) on its complement, with arbitrary scale \(\mu>0\). All its moduli have this form; complex phases do not affect the operator.

## Proof

**1. Global cubic certificate.** Direct algebra gives the two exact identities
\[
 (\Lambda-1)y^2=\Lambda z^2,\qquad
 \Lambda z^2(3-2z)=1.
\]
For \(x\ge0\), set
\[
 S(x)=\Lambda x^3-\max\{x,1\}^{3}-3\Lambda z^2(x-1).
\]
Polynomial factorization supplies the *exact nonnegative identity*
\[
 S(x)=\begin{cases}
 \Lambda(x-z)^2(x+2z),&0\le x\le1,\\
 (\Lambda-1)(x-y)^2(x+2y),&x\ge1.
 \end{cases}
\]
The zero set is exactly \(\{z,y\}\). For any nonnegative integrable \(g\) of positive mean \(\mu\), apply this identity to \(x=g/\mu\), average it, and use \(\mathbb E(x-1)=0\). One obtains the *deficit identity*
\[
 \Lambda\mathbb E(g^3)-\mathbb E\max\{g,\mu\}^3
 =\mu^3\mathbb E S(g/\mu)\ge0.
\]
Equality forces \(g/\mu\in\{z,y\}\) almost surely. Its mean must be one, hence the mass on the high level is uniquely \(\alpha=(1-z)/(y-z)\). This is an attainable law in every atomless probability space. The number \(\alpha\) is a quadratic irrational, so equality cannot occur under equal weights \(1/n\) for any finite \(n\).

**2. Finite-dimensional two-level reduction.** Let \(g_j=|f(j)|\), \(\mu=n^{-1}\sum g_j\), and divide the vertices into levels above and below \(\mu\). With their respective arithmetic means fixed, Jensen's inequality minimizes each group's sum of cubes when its entries are equal. Equalizing the lower group decreases the denominator \(\sum g_j^3\) without changing \(\sum (M_ng_j)^3\). Equalizing the upper group decreases its cube sum in both numerator and denominator by the same quantity, thereby increasing their quotient whenever the lower group is nonempty. Thus every nonconstant maximizer is two-valued, with a high value \(1\), a low value \(t\in(0,1)\), and high-level fraction \(a=k/n\) for some \(1\le k<n\). Its cubed norm quotient is
\[
 F(a,t)=\frac{a+(1-a)[a+(1-a)t]^3}{a+(1-a)t^3}.
\]
For each fixed \(0<a<1\), direct differentiation yields
\[
 \partial_tF(a,t)=
 \frac{3a(1-a)}{[a+(1-a)t^3]^2}
 \bigl[(1-a)[a+(1-a)t]^2(1-t^2)-t^2\bigr].
\]
The sign-changing bracket has a unique zero in \((0,1)\): after division by \(t^2\), the positive term is \((1-a)(a/t+1-a)^2(1-t^2)\), strictly decreasing from infinity to zero. Denote that unique maximizing root by \(t(a)\) and let \(G(a)=F(a,t(a))\). The implicit-function theorem makes \(G\) smooth near every interior \(a\).

**3. Nondegenerate mass-fraction maximum.** By step 1, \(G(a)\le\Lambda\), with equality only at \(a=\alpha\), where \(t(\alpha)=z/y\). In particular this is the unique continuous mass-fraction maximum. Its exact quadratic curvature can be reconstructed directly from the certificate. Normalize the two values so that the mean is one. For \(a=\alpha+\delta\), write the high and low values as \(y+u\delta+O(\delta^2)\) and \(z+v\delta+O(\delta^2)\). The mean constraint at first order reads
\[
 \alpha u+(1-\alpha)v=-(y-z).
\]
Using the two factorizations in step 1, the first nonzero deficit coefficient equals
\[
 3\alpha(\Lambda-1)y\,u^2
 +3(1-\alpha)\Lambda z\,v^2.
\]
Minimizing this positive quadratic form under the displayed linear constraint and dividing by the optimal denominator
\[
 D=\alpha y^3+(1-\alpha)z^3
 =\frac{322-31\sqrt7}{162}
\]
gives the normalized curvature
\[
 \begin{aligned}
 \kappa
 &=\frac{(y-z)^2}{D\left[\alpha/(3(\Lambda-1)y)+(1-\alpha)/(3\Lambda z)\right]}\\
 &=1-\frac{\sqrt7}{14}>0.
 \end{aligned}
\]
The scalar maximizing variable is smooth by step 2, so Taylor's theorem provides the *two-sided local estimate*
\[
 \Lambda-G(a)=\kappa(a-\alpha)^2\bigl(1+O(|a-\alpha|)\bigr).
\]
To exclude distant competing maximizers, note that \(F(a,t)\to1\) as \(a\to0\) or \(a\to1\) uniformly for \(0\le t\le1\). Consequently, compactness plus the unique equality case shows that \(\Lambda-G(a)\) is bounded away from zero outside every fixed neighborhood of \(\alpha\).

**4. Arithmetic quantization.** For the graph with \(n\) vertices,
\[
 \|M_n\|_3^3=\max_{1\le k<n}G(k/n).
\]
A grid point nearest \(\alpha\) lies within \(1/(2n)\), so the maximizing grid point approaches \(\alpha\) and, by the nondegenerate local expansion, lies within \(O(1/n)\). Comparing every nearby grid point with the nearest one using the uniform local bounds proves
\[
 \Lambda-\max_kG(k/n)=\kappa\min_k|k/n-\alpha|^2(1+O(n^{-1})),
\]
which is the claimed formula. The polynomial identity
\[
 57\alpha^2-64\alpha+16=0
\]
shows that \(\alpha\) is quadratic irrational, and for rational \(k/n\in[0,1]\) the corresponding integer polynomial is nonzero. Factoring at the two quadratic roots gives \(|\alpha-k/n|\ge c/n^2\) for a fixed positive \(c\). Conversely, continued-fraction convergents provide infinitely many \(k/n\) with \(|\alpha-k/n|\le1/n^2\). The formula therefore yields \(\Theta(n^{-4})\) along their denominator sequence. Density of the fractional parts \(\{n\alpha\}\) supplies infinitely many \(n\) with \(\|n\alpha\|_{\mathbb Z}\ge1/4\), giving \(\Theta(n^{-2})\) along a different sequence.

## Verification

The standalone script `checks/verify_cubic.py` checks the exact algebraic equalities, both piecewise factorizations, the two-level derivative, and the Schur-complement second-variation coefficient using exact symbolic arithmetic. It also performs finite-grid numerical stress tests for selected graph sizes. The symbolic identities directly support the proof; the numerical tests are additional corroboration rather than an exhaustive proof for all \(n\).

## Relationship to prior work

The 2026 study by Ciccone, Hormozi, Madrid, Niksiński and Wróbel proves sharp \(L^p\) maximal semigroup constants in an essentially nonatomic, local-compactness setting; this finite-atomic complete-graph semigroup is outside the nonatomic hypothesis. González-Riquelme and Madrid determined complete-graph norms at \(p=2\), and established the general two-value structure of finite complete-graph extremizers for \(p>1\), but do not report this cubic irrational occupancy and the corresponding arithmetic two-rate convergence. Their later paper with Kovač concerns \(p\)-variation, not the \(\ell^3\) operator norm. The earlier two-level principle is credited and reproved here only to make the quantization argument self-contained.

## Limitations

The result concerns the cubic exponent and complete-graph (rank-one equilibrium) semigroup, not arbitrary Markov chains or the sharp constant for every exponent. No independent audit has been conducted. Historical equivalence through a more general Bellman-function estimate or an unindexed result is a residual originality risk, although the relevant close sources identified in the bibliography do not state the arithmetic asymptotic.

## References

1. V. Ciccone, M. Hormozi, J. Madrid, J. Niksiński, B. Wróbel, *On \(L^p\) norms of maximal operators*, arXiv:2610.10247v1, first posted 2026-10-07. https://arxiv.org/html/2610.10247v1
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630, first posted 2020-11-05. https://arxiv.org/abs/2011.02630
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146, first posted 2020-05-06. https://arxiv.org/html/2005.03146v3
4. C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462v1, first posted 2026-03-12. https://arxiv.org/html/2603.12462v1
5. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204, first posted 2014-10-22. https://arxiv.org/abs/1410.6204
