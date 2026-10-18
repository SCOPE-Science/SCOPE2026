# Two-end root collapse at a singularly tilted Liénard switching line

## Finding

For a planar harmonic oscillator with polynomial Liénard damping and a univariate polynomial force switched across an oblique line, the exact first-order radial average is
\[
M_s(r)=rF(r^2)+sG(s^2r^2),\qquad s=\sin\phi,
\]
where \(F\) and \(G\) are explicit polynomials. Although coefficient optimization at each fixed nonzero angle permits \(p+q+1\) simple positive zeros when \(\deg F=p\) and \(\deg G=q\), holding the coefficients fixed and letting \(s\downarrow0\) leaves only the simple positive roots of \(F\), potentially one vanishing-radius root, and potentially one diverging-radius root. The inner and outer roots have exact leading exponents and coefficients. In particular the total number of roots for sufficiently small positive \(s\) is \(k+I_{A_0B_0<0}+I_{q>p,\,A_pB_q<0}\), where \(k\) is the number of simple positive roots of \(F(r^2)\). The result quantifies a nonuniform collapse of the first-order cycle mechanism at the vertical switching orientation.

## Assumptions and scope

Consider the piecewise-smooth planar vector field
\[
\dot x=-y,\qquad
\dot y=x+\varepsilon\left[f(x)y+\operatorname{sgn}(x\cos\phi+y\sin\phi)g(x)\right],\qquad |\phi|<\pi/2.
\]
Take arbitrary real polynomials \(f,g\). Only their even coefficients enter the first-order radial average: write \(f(x)=\sum_{j\ge0}a_{2j}x^{2j}+f_{\rm odd}(x)\) and \(g(x)=\sum_{j\ge0}b_{2j}x^{2j}+g_{\rm odd}(x)\), where the sums are finite. Set
\[
A_j=\frac{a_{2j}}2\frac{\binom{2j}{j}}{4^j(j+1)},\quad B_j=\frac{2b_{2j}}{\pi(2j+1)},\quad
F(u)=\sum_{j=0}^{p}A_ju^j,\quad G(u)=\sum_{j=0}^{q}B_ju^j.
\]
Here \(p,q\ge0\), \(A_p B_q\ne0\). For the singular-angle conclusion assume also \(A_0B_0\ne0\) and **every positive root of \(F\) is simple**. Let \(k\) count these roots. All root statements concern finite positive \(r\) for each fixed \(s=\sin\phi>0\), and all limit-cycle statements concern first-order bifurcations on compact positive-radius annuli with \(|\varepsilon|\) sufficiently small after fixing \(s\). No uniformity in \(\varepsilon\) as \(s\to0\) is asserted.

## Proof

**Angular average.** On an unperturbed circular orbit, put \(x=r\cos\theta\), \(y=r\sin\theta\). Then \(\dot\theta=1+O(\varepsilon)\), and the first-order radial displacement divided by the unperturbed period is
\[
M_s(r)=\frac1{2\pi}\int_0^{2\pi}\left[r\sin^2\theta f(r\cos\theta)+\sin\theta\operatorname{sgn}(\cos(\theta-\phi))g(r\cos\theta)\right]d\theta.
\]
Odd monomials in either polynomial integrate to zero (for the forcing, pair opposite angles and then reflect across the switching diameter). The smooth integral obeys
\[
\frac1{2\pi}\int_0^{2\pi}\sin^2\theta\cos^{2j}\theta\,d\theta
=\frac12\frac{\binom{2j}{j}}{4^j(j+1)}.
\]
The switched integral obeys
\[
\int_0^{2\pi}\sin\theta\cos^{2j}\theta\operatorname{sgn}(\cos(\theta-\phi))d\theta
=\frac{4\sin^{2j+1}\phi}{2j+1}.
\]
One can verify the latter by integrating the derivative of \(-\cos^{2j+1}\theta/(2j+1)\) over the semicircle \(\phi-\pi/2<\theta<\phi+\pi/2\) and subtracting the complementary semicircle. Thus the claimed exact polynomial formula follows, including the complete forcing cancellation at \(s=0\).

**Fixed nonzero angle.** The polynomial \(M_s(r)\) has at most \(p+q+2\) nonzero monomials, of the distinct degrees \(1,3,\ldots,2p+1\) and \(0,2,\ldots,2q\). Descartes' rule gives at most \(p+q+1\) positive zeros counted with multiplicity. Attainment is elementary: choose \(p+q+1\) distinct positive locations \(u_1,\ldots,u_{p+q+1}\). The homogeneous linear constraints \(M_s(u_i)=0\) on \(p+q+2\) monomial coefficients admit a nonzero solution; by the Chebyshev property of strictly increasing real monomials, its null space is one-dimensional, all coefficients are nonzero, and these prescribed zeros are simple with no additional positive zeros. Each monomial coefficient can be independently realized by an even coefficient of \(f\) or \(g\) at any fixed \(s\ne0\). At \(s=0\), exactly the positive roots of \(F(r^2)\) survive in the first-order average; the optimized maximum is \(p\), when \(F\) is chosen with \(p\) distinct positive roots.

**Fixed coefficients and singular tilt: finite roots.** Let \(s\downarrow0\). Every simple positive root \(R\) of \(F(r^2)\) persists uniquely near \(R\) by the implicit-function theorem; its derivative is nonzero since \(2R^2F'(R^2)\ne0\). On compact subsets of the positive half-line avoiding those roots, \(M_s(r)\to rF(r^2)\) uniformly, so there are no additional roots there.

**Inner boundary layer.** If positive roots \(r_s\to0\), the identity \(0=r_sF(r_s^2)+sG(s^2r_s^2)\), with \(A_0B_0\ne0\), forces \(r_s/s\to-B_0/A_0\). Such roots occur if and only if \(A_0B_0<0\); substituting \(r=su\) gives the limiting equation \(A_0u+B_0=0\), whose simple positive root lifts uniquely. Consequently
\[
r_{\mathrm{in}}(s)=-\frac{B_0}{A_0}s+o(s).
\]
No inner root exists if \(A_0B_0>0\).

**Outer boundary layer.** Suppose a root \(r_s\to\infty\). If \(sr_s\) remained bounded, then \(sG(s^2r_s^2)=O(s)\) while \(r_sF(r_s^2)\sim A_pr_s^{2p+1}\), an impossibility. Thus \(sr_s\to\infty\). Comparing the leading terms gives
\[
0=A_pr_s^{2p+1}(1+o(1))+B_qs^{2q+1}r_s^{2q}(1+o(1)).
\]
This is impossible if \(q\le p\) and, if \(q>p\), requires \(A_pB_q<0\). Put \(d=2(q-p)-1>0\), \(\gamma=(2q+1)/d\), and \(r=s^{-\gamma}u\). After division by \(s^{-\gamma(2p+1)}\), the equation converges locally in \(C^1\) on \(u>0\) to \(A_pu^{2p+1}+B_qu^{2q}=0\), which has exactly one simple positive root
\[
u_* =\left(-\frac{A_p}{B_q}\right)^{1/d}.
\]
Hence a unique outer branch exists and
\[
r_{\mathrm{out}}(s)=u_*s^{-(2q+1)/[2(q-p)-1]}(1+o(1)).
\]
Any additional root sequence would have a subsequence converging to zero, to a finite positive number, or to infinity. The three mutually exclusive cases above put it into one of the uniquely identified local branches, yielding a contradiction. Therefore the list is exhaustive. All roots remain simple for sufficiently small positive \(s\).

**Realizing cycles.** For any fixed nonzero \(s\), all zeros counted above are simple and their unperturbed circles cross the switching line transversely twice. The standard first-order averaging persistence theorem for crossing piecewise-smooth systems then produces one hyperbolic limit cycle near each circle for sufficiently small nonzero \(\varepsilon\), with the stability sign determined by \(\varepsilon M_s'(r)\). This existence statement is not uniform as the angle approaches zero.

## Verification

A standalone Python 3 standard-library program `verify.py` numerically cross-checks the exact integral reduction for seven even monomial degrees at several angles, and checks root brackets and two-scale asymptotics in concrete coefficient families. Running `python3 verify.py` returns `PASS 204 diagnostic assertions; universal statements rely on analytical proof`. These sampled diagnostics are not substitutes for the proof.

For a concrete example, take \(f(x)=1\), \(g(x)=-1-x^{2q}\), \(q\ge1\). Then
\[
M_s(r)=\frac r2-\frac{2s}{\pi}-\frac{2s^{2q+1}r^{2q}}{\pi(2q+1)}.
\]
For every sufficiently small positive \(s\), it has exactly two simple positive zeros:
\[
r_{\mathrm{in}}(s)\sim\frac4\pi s,\qquad
r_{\mathrm{out}}(s)\sim\left[\frac{\pi(2q+1)}4\right]^{1/(2q-1)}s^{-(2q+1)/(2q-1)}.
\]
For positive \(\varepsilon\), the inner cycle is repelling and the outer cycle attracting, according to their radial averaged derivative signs. At exact zero tilt, the univariate switched force has zero first-order effect.

## Relationship to prior work

Álvarez and Sierra-Ortiz (arXiv:2609.14140, first submission 2026-09-12) establish the parity obstruction for switching on the vertical line and sharp first-order bounds with bivariate forcing. De Abreu and Martins (arXiv:2307.09599, later journal publication) study the complementary horizontal switch with univariate forcing and its sharp coefficient-optimized count. Consequently neither extreme-angle cancellation nor the fixed-nonzero-angle optimized count is asserted as a new theorem in isolation: that count can also be inferred by rescaling known horizontal-switch averaged coefficients. The assessed contribution is the **fixed-coefficient singular orientation limit**, its exact inner/outer scale exponents, and the proof that at most two root branches live outside the smooth positive roots. Li and Llibre (2021) treat broader non-regular piecewise switching geometry, but the inspected material did not establish this coefficient-fixed angular two-end classification.

## Limitations

This is an exact theorem about **first-order averaged positive simple zeros** and their nearby crossing limit cycles at each separately fixed tilt. It does not bound all limit cycles for finite perturbations, exclude higher-order bifurcations at zero tilt, determine global basins, or give a simultaneous limit in the perturbation size and tilt. The origin lies on the switching line, so the collapsing inner branch needs perturbation magnitudes chosen after fixing its positive radius. General piecewise switching literature may implicitly contain equivalent asymptotic analyses, and bibliographic priority is not independently certified.

## References

1. C. F. Álvarez and A. Sierra-Ortiz, *Estimates for the Number of Limit Cycles in Discontinuous Generalized Liénard Systems with Bivariate Perturbation*, arXiv:2609.14140 (first submission 2026-09-12), https://arxiv.org/abs/2609.14140.
2. T. M. P. de Abreu and R. M. Martins, *Sharp estimates for the number of limit cycles in discontinuous generalized Liénard equations*, arXiv:2307.09599, https://arxiv.org/abs/2307.09599.
3. T. Li and J. Llibre, *Limit cycles in piecewise polynomial systems allowing a non-regular switching boundary*, 2021, https://ddd.uab.cat/pub/artpub/2021/239778/LiLli2020d.pdf.
4. J. Llibre, A. C. Mereu and D. D. Novaes, *Averaging theory for discontinuous piecewise differential systems*, Journal of Differential Equations 258 (2015), DOI:10.1016/j.jde.2015.01.022.
5. J. Llibre and M. A. Teixeira, *Limit cycles for m-piecewise discontinuous polynomial Liénard differential equations*, 2013 preprint, https://www.ime.unicamp.br/sites/default/files/pesquisa/relatorios/rp-2013-2.pdf.
6. Z. Jiang, *Limit cycles in an m-piecewise discontinuous polynomial differential system*, AIMS Mathematics 9 (2024), DOI:10.3934/math.2024177.
