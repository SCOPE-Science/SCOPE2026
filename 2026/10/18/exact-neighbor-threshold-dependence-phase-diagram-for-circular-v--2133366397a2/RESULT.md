# Exact neighbor threshold-dependence phase diagram for circular Voronoi cells

## Finding

Fix an integer \(n\ge2\). Sample \(n\) independent uniform sites on a circle of circumference one, order them cyclically, and let \(L_i\) be the arclength of the Voronoi cell of site \(i\). For a common threshold \(0<t<1/2\), set \(I_i(t)=\mathbf1\{L_i>t\}\) and \(q=2t\in(0,1)\). A pair of cells is *adjacent* when their cyclic indices differ by one; otherwise it is *nonadjacent*.

**Complete strict-sign classification.** The adjacent covariance is zero for \(n=2\) (both indicators are deterministic), strictly negative for \(n=3\), nonnegative for \(n=4\) with its unique interior zero at \(t=1/4\), and strictly positive for every \(n\ge5\). For every \(n\ge4\), all nonadjacent cell pairs have strictly negative indicator covariance at every such threshold. In particular, at four sites and the mean-cell threshold \(t=1/4\), neighboring indicators are independent; away from that unique threshold they are positively correlated. The corresponding nonadjacent indicators are always negatively correlated.

For \(n\ge3\), define the marginal survival probability

\[
p_n(q)=(1-q)^{n-2}\bigl(1+(n-2)q\bigr).
\]

For neighboring cells the joint survival probability is

\[
J_n^{\mathrm{adj}}(q)=2(1-q)^{n-1}-(1-2q)_+^{n-1},
\]

where \(z_+=\max\{z,0\}\). Consequently,

\[
\operatorname{Cov}(I_i(t),I_{i+1}(t))=J_n^{\mathrm{adj}}(q)-p_n(q)^2.
\]

For any pair of nonadjacent cells (necessarily \(n\ge4\)), their joint survival probability is

\[
\begin{aligned}
J_n^{\mathrm{non}}(q)={}&(1-2q)_+^{n-1}
 +2(n-1)q(1-2q)_+^{n-2}\\
&+(n-1)(n-2)q^2(1-2q)_+^{n-3}.
\end{aligned}
\]

Their covariance is exactly \(J_n^{\mathrm{non}}(q)-p_n(q)^2<0\).

At the local Poisson scale \(q=x/n\), with each fixed \(x>0\), the limiting adjacent covariance is positive while the nonadjacent covariance is negative but smaller by a factor of order \(n\):

\[
\begin{aligned}
\lim_{n\to\infty}\operatorname{Cov}(I_i(x/(2n)),I_{i+1}(x/(2n)))
&=e^{-2x}(2e^x-2-2x-x^2)>0,\\
\operatorname{Cov}(I_i(x/(2n)),I_j(x/(2n)))
&=-\frac{x^4e^{-2x}}n+O_x(n^{-2}),\quad i,j\text{ nonadjacent}.
\end{aligned}
\]

## Assumptions and scope

The circle has normalized circumference one and the distance is intrinsic geodesic arclength. Sites have an iid continuous uniform distribution; almost surely they are distinct. The cyclic indexing is arbitrary because the law is rotationally invariant. A Voronoi cell is bounded by the midpoints of the two successive gaps adjacent to its site. For \(n=2\), both cells have length exactly \(1/2\). Thresholds \(0<t<1/2\) are the nondegenerate range; at or above \(1/2\), every indicator is zero almost surely.

For \(n\ge3\), let \(S_1,\ldots,S_n\) denote the consecutive clockwise spacings. Their vector is \(\operatorname{Dirichlet}(1,\ldots,1)\), and \(L_i=(S_{i-1}+S_i)/2\), with indices interpreted cyclically. The assertions concern the joint law induced by this *finite fixed-size* sample, not independent gaps or a Poisson sample with random cardinality.

## Proof

**1. Dirichlet representation and one-cell law.** The spacings of iid uniform points around a circle are uniform on the \((n-1)\)-simplex. Aggregating any two spacings gives \(A=S_i+S_{i+1}\sim\operatorname{Beta}(2,n-2)\). Integrating its density \((n-1)(n-2)a(1-a)^{n-3}\) over \(a>q\) yields \(p_n(q)\).

**2. Neighboring joint survival.** Write the two adjacent sums as \(X+Y\) and \(X+Z\), where \(X,Y,Z\) are three distinct Dirichlet components. Conditional on the shared spacing \(X=x\), which has density \((n-1)(1-x)^{n-2}\), both sums exceed \(q\) automatically if \(x\ge q\). For \(0\le x<q\), their conditional probability is \(((1-2q+x)_+/(1-x))^{n-2}\). Therefore

\[
\begin{aligned}
\Pr(X+Y>q,\ X+Z>q)
={}&\int_q^1(n-1)(1-x)^{n-2}\,dx\\
&+\int_{\max\{0,2q-1\}}^q(n-1)(1-2q+x)^{n-2}\,dx\\
={}&2(1-q)^{n-1}-(1-2q)_+^{n-1}.
\end{aligned}
\]

**3. Nonadjacent joint survival and strict negativity.** Two nonadjacent cells use four disjoint spacing components. Their doubled lengths \(A,B\), together with the remaining mass, have a \(\operatorname{Dirichlet}(2,2,n-4)\) aggregation when \(n>4\). Translating \(A=q+u\) and \(B=q+v\) in the two-dimensional Dirichlet integral gives the displayed polynomial \(J_n^{\mathrm{non}}(q)\). For \(n=4\), \(B=1-A\), and direct integration of the \(\operatorname{Beta}(2,2)\) density yields the same expression.

For strictness, suppose \(n\ge5\). Given \(A=a\), write \(B=(1-a)Z\), where \(Z\sim\operatorname{Beta}(2,n-4)\) is independent of \(A\). The conditional tail \(f(a)=\Pr(B>q\mid A=a)\) is strictly decreasing on \(0<a<1-q\), and zero when \(a\ge1-q\). Because \(A\) has an everywhere-positive beta density on \((0,1)\), a high value of \(A\) strictly lowers the conditional probability of \(B>q\). Thus \(\operatorname{Cov}(\mathbf1\{A>q\},f(A))<0\). For \(n=4\), the identity \(B=1-A\) gives covariance \(-(1-p_n(q))^2\) for \(q\le1/2\), and \(-p_n(q)^2\) for \(q\ge1/2\); both are strictly negative.

**4. Neighboring signs in dimensions three and four.** Direct expansion gives, for \(n=3\),

\[
J_3^{\mathrm{adj}}(q)-p_3(q)^2=
\begin{cases}
-q^4,&0<q\le1/2,\\
-(1-q)^2(q^2+2q-1),&1/2\le q<1.
\end{cases}
\]

Both branches are strictly negative on their stated ranges. For \(n=4\), the corresponding exact factorization is

\[
J_4^{\mathrm{adj}}(q)-p_4(q)^2=
\begin{cases}
q^3(2-q)(1-2q)^2,&0<q\le1/2,\\
(1-q)^3(1+q)(2q-1)^2,&1/2\le q<1.
\end{cases}
\]

Hence its sole nontrivial zero is \(q=1/2\), equivalently \(t=1/4\). At this threshold \(p_4=1/2\), and joint probability \(1/4\) gives independence of the Bernoulli indicators.

**5. Neighboring strict positivity for all \(n\ge5\).** Put \(r=n-2\ge3\) and

\[
F(q)=(1-q)^{r-1}(1+rq)^2,
\qquad
G(q)=\left(\frac{1-2q}{1-q}\right)^{r+1}
\quad(0\le q\le1/2).
\]

For \(0<q\le1/2\), the adjacent covariance equals \((1-q)^{r+1}[2-F(q)-G(q)]\). Now \(F(0)+G(0)=2\), and differentiating yields

\[
\frac{F'(q)+G'(q)}{r+1}
=(1-q)^{r-2}(1+rq)(1-rq)
-\frac{(1-2q)^r}{(1-q)^{r+2}}.
\]

For \(q\ge1/r\), this derivative is plainly negative. If \(0<q<1/r\), its negativity is equivalent to

\[
\left(1+\frac{q^2}{1-2q}\right)^r(1-r^2q^2)<1.
\]

Indeed, since \(r\ge3\) and \(q<1/r\), we have \(r/(1-2q)<r^2\). With \(u=q^2/(1-2q)\) and \(z=r^2q^2\in(0,1)\),

\[
(1+u)^r\le e^{ru}<e^z<\frac1{1-z}.
\]

Thus the last strict inequality follows, so \(F+G\) is strictly decreasing from \(2\). This proves positivity when \(q\le1/2\).

For \(1/2\le q<1\), the adjacent covariance instead equals \((1-q)^{n-1}[2-F(q)]\). Since

\[
F'(q)=(n-1)(1-q)^{n-4}(1+(n-2)q)(1-(n-2)q)<0,
\]

and \(F(1/2)=n^2/2^{n-1}<2\) for every integer \(n\ge5\), this covariance is also strictly positive. This completes the finite-sample classification.

**6. Local-scale limits.** With \(q=x/n\) and fixed \(x>0\), the exact survival formulas give \(p_n\to e^{-x}(1+x)\), \(J_n^{\mathrm{adj}}\to2e^{-x}-e^{-2x}\). The positive difference is \(2e^{-2x}(e^x-1-x-x^2/2)\). For nonadjacent pairs, first-order Taylor expansion yields

\[
\begin{aligned}
p_n(x/n)&=e^{-x}\left[(1+x)+\frac{3x^2-x^3}{2n}+O_x(n^{-2})\right],\\
J_n^{\mathrm{non}}(x/n)&=e^{-2x}\left[(1+x)^2+\frac{3x^2+2x^3-2x^4}{n}+O_x(n^{-2})\right].
\end{aligned}
\]

Subtracting the square of the first expansion proves the stated negative \(n^{-1}\)-order term.

## Verification

Run the standalone file `verification/check_voronoi.py` with `python3 verification/check_voronoi.py` from the extracted package root. It uses only the Python standard library and checks the joint-survival formulas by separately integrating exact rational polynomials, checks the complete sign table on broad finite grids, verifies three- and four-point factorizations, and independently checks local-scale limits at high precision. The executed version reported 1,829 exact integration identities, 1,209 strict-sign checks, 36 linear moment-sign checks, and eight asymptotic comparisons. None of these finite checks replaces the proof for unbounded sample size or all real thresholds.

## Relationship to prior work

Devroye, Györfi, Lugosi, and Walk study the measure of a typical Voronoi cell, and identify the one-dimensional rescaled Gamma limit; their results concern one-cell moments and asymptotic laws, not the all-threshold finite-sample pair-dependence classification for iid sites on a circle. Gabrielli and Torquato determine the joint size law for cells of a **shuffled lattice** in one dimension; in their model, displacements from lattice locations are independent, and their nonzero correlations occur at separation two rather than in the finite iid circular Voronoi model. Neither result implies the four-point independence exception or the complete neighbor-versus-nonneighbor threshold sign theorem here. The beta and Dirichlet aggregation identities used in this proof are classical and are not claimed as new.

## Limitations

The theorem assumes iid uniform sites on a circle and a *common* threshold for both cell indicators. It does not classify arbitrary unequal thresholds, nonuniform sampling densities, higher-dimensional Voronoi tessellations, or random sample cardinalities. The joint-survival formulas are consequences of simplex integration; the assessed new contribution is their exact finite-size dependence classification and the exceptional independence threshold. Earlier specialized finite circle calculations may implicitly contain this conclusion; historical priority has not been independently verified. Mathematical correctness and originality have not undergone independent scientific audit.

## References

1. A. Gabrielli and S. Torquato, *Voronoi and Voids Statistics for Super-homogeneous Point Processes*, publicly posted 2004-05-06, arXiv:cond-mat/0405115, https://arxiv.org/abs/cond-mat/0405115 (relevant: Sections IV–V, shuffled-lattice model and joint law).
2. L. Devroye, L. Györfi, G. Lugosi, and H. Walk, *On the Measure of Voronoi Cells*, publicly posted 2015-12-14, arXiv:1512.04267, https://arxiv.org/abs/1512.04267 (relevant: Sections 1–3, dimension-one typical-cell law). Journal of Applied Probability 54 (2017), primary MSC 60D05.
