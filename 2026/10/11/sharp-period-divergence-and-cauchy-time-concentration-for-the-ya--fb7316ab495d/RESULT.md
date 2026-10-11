# Sharp period divergence and Cauchy time concentration for the Yablonskii oval

## Finding

Fix real parameters \(0<a<b<3a\). Consider the quadratic Yablonskii system
\[
\begin{aligned}
\dot x={}&-4abcx-(a+b)y+3(a+b)cx^2+4xy,\\
\dot y={}&(a+b)abx-4abcy
+\bigl(4abc^2-\tfrac32(a+b)^2+4ab\bigr)x^2\\
&+8(a+b)cxy+8y^2.
\end{aligned}
\]
Write \(d=b-a\), \(s=a+b\), \(h=3a-b\), and \(H=3b-a\), all positive, and define
\[
 c_*=\frac{\sqrt{hH}}{2d},\qquad
 x_*=\frac{6ab-a^2-b^2}{2s},\qquad
 R(x)=\sqrt{(x-a)(b-x)},\qquad m(x)=4x-s.
\]
For every \(0<c<c_*\), the smooth oval
\[
 \Gamma_c:\quad (y+cx^2)^2+x^2(x-a)(x-b)=0,\qquad a\leq x\leq b,
\]
is a periodic orbit. Its minimal period \(T(c)\), measured in the unrescaled physical time of the displayed system, is
\[
 \boxed{T(c)=2\int_a^b
 \frac{m(x)}{xR(x)\bigl(m(x)^2-16c^2R(x)^2\bigr)}\,dx.}
\]
This is finite and strictly increasing in \(c\). It has a finite zero-parameter limit
\[
 \boxed{\lim_{c\downarrow0}T(c)=\frac{2\pi}{s}
 \left(\frac4{\sqrt{hH}}-\frac1{\sqrt{ab}}\right).}
\]
At the opposite endpoint it diverges with an exact coefficient:
\[
 \boxed{\lim_{c\uparrow c_*}\sqrt{c_*-c}\,T(c)
 =\frac{\pi}{x_*\sqrt d\,(hH)^{1/4}}.}
\]
A more precise dynamical description holds. Define
\[
 R_* =R(x_*),\quad F(x)=\frac{m(x)}{4R(x)},\quad
 F''(x_*)=\frac{s}{4R_*^3},\quad
 \ell_c=\sqrt{\frac{2(c_*-c)}{F''(x_*)}}.
\]
Choose time \(t\) uniformly on one minimal period of \(\Gamma_c\). Then the rescaled position has the universal weak limit
\[
 \boxed{\frac{x(t)-x_*}{\ell_c}\ \Longrightarrow\ 
 \text{the standard Cauchy law with density }\frac1{\pi(1+v^2)}.}
\]
Moreover, the physical-time occupation measure on the oval converges weakly to a point mass at
\[
 p_*=(x_*,-c_*x_*^2-x_*R_*).
\]
At \(c=c_*\), this point is an equilibrium on the previously periodic oval. The periodic orbit therefore disappears by a one-point velocity arrest, not by shrinkage of its algebraic support. The existence of this classical algebraic oval and its parameter range are prior results; the contribution here is its original-time period law, sharp arrest coefficient, and normalized occupation law.

## Assumptions and scope

The parameters \(a,b\) are fixed throughout, with \(0<a<b<3a\). The parameter \(c\) varies over \((0,c_*)\), so the source's nonzero-parameter condition is respected. All periods and occupation measures use the original \(t\) in the polynomial system, **not** a new time coordinate obtained from a birational transformation. The continuous extension at \(c=0\) is a period limit; no isolation assertion is made for that endpoint. No theorem for \(c>c_*\) is asserted.

On \((a,b)\) the oval is parametrized by two graphs
\[
 y_\pm(x)=-cx^2\pm xR(x).
\]
The endpoints agree and are smooth turning points, because the \(y\)-velocity is nonzero there: \(\dot y(a,-ca^2)=a^2dh/2>0\) and \(\dot y(b,-cb^2)=-b^2dH/2<0\). A uniform phase is obtained by normalizing Lebesgue time \(dt/T(c)\) over one full traversal. Weak convergence is against every bounded continuous test function on \(\mathbb R\), for fixed \(a,b\), as \(c\uparrow c_*\).

## Proof

**1. Invariance and branch velocities.** Put
\[
 f(x,y)=(y+cx^2)^2+x^2(x-a)(x-b).
\]
Direct expansion of the displayed polynomial vector field verifies, identically for all real \(a,b,c,x,y\),
\[
 \dot f=4\bigl(-2abc+3c(a+b)x+4y\bigr)f.
\]
Consequently \(f=0\) is invariant. Substitution of \(y=y_\pm(x)\) into \(\dot x\) yields the **exact** original-time relation
\[
 \dot x\big|_{y=y_\pm(x)}=xR(x)\bigl(4cR(x)\pm m(x)\bigr).
\]
Since \(m(x)\ge h>0\), the upper branch is traversed from \(a\) to \(b\). To determine the lower branch, use the next step to show \(4cR(x)<m(x)\). Its velocity is then negative. Thus the smooth invariant oval is one closed, nonstationary periodic orbit. As it is traversed exactly once, the branch-time sum is its minimal period.

**2. Exact minimum and threshold.** Define \(F(x)=m(x)/(4R(x))\) on \((a,b)\). Differentiating, using \(R(x)^2=(x-a)(b-x)\), gives
\[
 F'(x)=\frac{s(x-x_*)}{4R(x)^3},
 \qquad x_*=\frac{6ab-a^2-b^2}{2s}=a+\frac{dh}{2s}.
\]
Thus \(F\) decreases to its unique global minimum at \(x_*\) and then increases, diverging at both endpoints. Its critical values satisfy
\[
 R_*^2=\frac{d^2hH}{4s^2},\qquad
 F(x_*)=\frac{\sqrt{hH}}{2d}=c_*,\qquad
 F''(x_*)=\frac{s}{4R_*^3}>0.
\]
For \(c<c_*\), the lower-branch speed has fixed negative sign. At \(c=c_*\), the lower branch has a single interior zero at \(x_*\); smoothness of the invariant oval forces the full vector field to vanish there. In particular, this is a genuine equilibrium and not merely a point with vanishing horizontal speed.

**3. Period quadrature and monotonicity.** The upper- and lower-branch positive time elements are
\[
 dt_+=\frac{dx}{xR(x)(m(x)+4cR(x))},\qquad
 dt_-=\frac{dx}{xR(x)(m(x)-4cR(x))}.
\]
Adding them gives the stated integral. Both endpoint singularities are integrable square roots, and the denominators are positive on the compact interior when \(c<c_*\). Differentiation under the integral on each compact subinterval of \([0,c_*)\) gives
\[
 \frac{dT}{dc}=64c\int_a^b
 \frac{m(x)R(x)}{x\bigl(m(x)^2-16c^2R(x)^2\bigr)^2}\,dx>0.
\]
For the zero-parameter limit put \(x=(s-d\cos\theta)/2\), so \(dx=R(x)\,d\theta\), \(m=s-2d\cos\theta\), and \(0\leq\theta\leq\pi\). Then
\[
 T(0)=2\int_0^\pi\frac{d\theta}{x(\theta)m(\theta)}
 =\frac{2\pi}{s}\left(\frac4{\sqrt{s^2-4d^2}}-
 \frac2{\sqrt{s^2-d^2}}\right).
\]
The identities \(s^2-4d^2=hH\) and \(s^2-d^2=4ab\) yield the displayed expression.

**4. Sharp arrest asymptotic.** Set \(\delta=c_*-c\downarrow0\). The upper-branch time remains bounded as \(\delta\to0\), because \(m+4cR\ge m\ge h>0\). On the lower branch, a cancellation-free exact expression is
\[
 dt_-=\frac{dx}{4xR(x)^2\bigl(F(x)-c\bigr)}.
\]
The unique nondegenerate minimum satisfies
\[
 F(x)-c=\delta+\frac{F''(x_*)}{2}(x-x_*)^2
 +O\bigl(|x-x_*|^3\bigr)
\]
uniformly on a sufficiently small fixed neighborhood of \(x_*\). Away from that neighborhood the lower-branch time is uniformly bounded, including the integrable endpoint pieces. Dominated rescaling on the neighborhood gives
\[
 \lim_{\delta\downarrow0}\sqrt\delta\,T(c_*-\delta)
 =\frac{\pi}{4x_*R_*^2}\sqrt{\frac2{F''(x_*)}}
 =\frac{\pi}{x_*\sqrt d\,(hH)^{1/4}}.
\]
The last equality uses the displayed exact formulas for \(R_*\) and \(F''(x_*)\). Neither a numerical extrapolation nor an assumed generic bifurcation normal form is used.

**5. Universal occupation law.** Let \(\ell_c=\sqrt{2\delta/F''(x_*)}\) and set \(x=x_*+\ell_c v\) in the lower-branch time measure. For each fixed \(v\),
\[
 dt_-=\frac{\ell_c}{4x_*R_*^2\,\delta}
 \left(\frac{1}{1+v^2}+o(1)\right)dv.
\]
The neighborhood contribution is asymptotic to the full period in step 4. The strict global minimum of \(F\) supplies a quadratic lower bound for \(F(x)-c\) near \(x_*\); consequently the normalized mass outside \(|v|\le M\) has a bound proportional to \(\int_{|v|>M}(1+v^2)^{-1}dv\), plus an error vanishing with \(\delta\). The upper-branch mass tends to zero. These bounds imply tightness and justify passage from compactly supported to arbitrary bounded continuous test functions. Dividing the scaled local density by its \(\pi\)-integral gives \(1/[\pi(1+v^2)]\). Since \(x\to x_*\) in physical-time probability and the dominant mass is on \(y_-(x)\), the full planar occupation measure converges to \(\delta_{p_*}\).

## Verification

The bundled standard-library program `verify.py` checks the full multivariate polynomial identity \(\dot f=kf\) by exact rational-coefficient polynomial arithmetic in the five variables \(a,b,c,x,y\); this check is an identity verification, not sample testing. Independent original-time quadrature, performed with an endpoint-regular angle variable, reproduces the closed form for \(T(0)\), exhibits increasing periods at four positive parameters, and tests the sharp endpoint constant for \(a=1,b=2\). For that example \(c_*=\sqrt5/2\), \(x_*=7/6\) and the predicted limiting constant is \(\pi/[x_*5^{1/4}]\approx1.800779682234\). At \(c_*-c=10^{-5}\), the numerical value of \(\sqrt{c_*-c}\,T(c)\) is approximately \(1.799926802072\). The normalized time within one scaled unit \(|(x-x_*)/\ell_c|\le1\) is approximately \(0.50024067\), compared to the Cauchy limit \(1/2\).

Run `python3 verify.py` in a directory containing this document and the adjacent checker. Finite quadratures are diagnostic only. The global monotonicity, precise critical coefficient, and weak limit are proved analytically above.

## Relationship to prior work

The invariant Yablonskii quartic oval and its admissible coefficient discriminant originate with Yablonskii (1966). Their canonical equations are reproduced in Gasull and Giacomini (2022), Case 2 of the proof of Theorem 1.2; this paper supplies a mechanism excluding additional limit cycles, **not** an original-time period law. Alberich-Carramiñana, Ferragut and Llibre (2019/2021), Proposition 2 and Section 7.1, characterize the same family and explicitly give a Cremona transformation into a subfamily of Qin's circular-oval system. That relation includes a nontrivial time change: geometric birational equivalence alone does not imply the displayed physical-time period, its endpoint coefficient, or its normalized occupation law. Giacomini and Grau (2005) study the hyperbolicity of known algebraic limit cycles and explicitly include the Yablonskii example; that stability calculation does not evaluate the period or a Cauchy occupation limit. The new theorem concerns exactly these three quantitative observables and deliberately does not claim rediscovery of the oval, its parameter range, uniqueness, or hyperbolicity.

## Limitations

The theorem fixes \(a,b\) and addresses only \(0<c<c_*\), with a continuous \(c\downarrow0\) period limit. It does not classify the post-arrest flow for \(c\ge c_*\), establish any stability variation of the oval, or give a convergence rate for the weak occupation limit. Exact source equivalences are considered only with their original-time normalization. Earlier papers by Yablonskii (1966) and Chavarriga–Llibre–Sorolla (2004) were not fully accessible for all-text comparison; an equivalent older evaluation or transformed period formula remains a scientific priority risk. No independent external validation of the present proof is claimed.

## References

1. A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803v1 (public 2022-10-27), https://arxiv.org/abs/2210.15803 . Section 4, Case 2; primary MSC 34C07.
2. M. Alberich-Carramiñana, A. Ferragut, and J. Llibre, *Quadratic Planar Differential Systems with Algebraic Limit Cycles via Quadratic Plane Cremona Maps*, arXiv:1906.10171v1 (2019), https://arxiv.org/abs/1906.10171 . Proposition 2 and Section 7.1.
3. H. Giacomini and M. Grau, *On the stability of limit cycles for planar differential systems*, arXiv:math/0505027v1 (2005), https://arxiv.org/abs/math/0505027 . Section 3, Yablonskii example.
4. J. Chavarriga, J. Llibre, and J. Sorolla, *Algebraic limit cycles of degree 4 for quadratic systems*, Journal of Differential Equations 200 (2004), 206–244, https://doi.org/10.1016/j.jde.2004.01.003 .
5. A. I. Yablonskii, *On the limit cycles of a certain differential equation*, Differential Equations 2 (1966), 164–168 (translated publication); original discovery credited through references 1–4.
