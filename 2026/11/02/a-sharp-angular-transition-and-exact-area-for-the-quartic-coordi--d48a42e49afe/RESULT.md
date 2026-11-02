# A sharp angular transition and exact area for the quartic coordinate-flip numerical range

## Finding
On complex \(\ell_4^2\) let \(F(u,v)=(v,u)\). Its spatial numerical range
\[
W(F)=\left\{\overline{u}|u|^2v+\overline{v}|v|^2u:\ |u|^4+|v|^4=1\right\}
\]
is a compact **convex**, centrally and conjugate-symmetric planar body, with a non-Hilbertian curved boundary. Its support function \(h(\phi)=\max_{z\in W(F)}\operatorname{Re}(e^{-i\phi}z)\) has the exact two-branch form
\[
h(\phi)=\begin{cases}
|\cos\phi|,&\sin^2\phi\le 3/4,\\
\displaystyle[8(2\sin^2\phi-1)]^{-1/2},&\sin^2\phi\ge 3/4.
\end{cases}
\]
The maximizing elliptic orbit leaves the equal-modulus eigenvector family exactly when \(|\sin\phi|>\sqrt3/2\). In the first quadrant the outer boundary is parametrized, without overlaps, by
\[
x(s)=\frac{\sqrt{3s-2}}{(2-s)^{3/2}},\qquad y(s)=\frac{(1-s)\sqrt{s+2}}{(2-s)^{3/2}},\quad 2/3\le s\le1.
\]
The other quadrants are its reflections. The exact planar Lebesgue area and the radius of the largest disk centered at zero and contained in \(W(F)\) are
\[
\operatorname{Area}W(F)=\frac{3\sqrt3}{8}+\frac3{16}\log(2+\sqrt3),\qquad r_{\mathrm{in}}=\frac1{2\sqrt2}.
\]
For any \(a,b\in\mathbb C\), \(W(aI+bF)=a+bW(F)\); thus the formulas give the complete numerical ranges of the affine coordinate-flip family.

## Assumptions and scope
Use the standard complex \(\ell_4\) norm and its unique norming functional \(J(u,v)=(u|u|^2,v|v|^2)\) on the unit sphere, paired sesquilinearly as above. The support is for all real \(\phi\), and the boundary formula covers all \(s\in[2/3,1]\). The affine rule includes \(b=0\). The results concern the *spatial Banach-space numerical range*, not Hilbert-space quadratic numerical ranges or all \(2\times2\) operators.

## Proof
**Ellipse reduction.** Write \(u=r/(1+r^4)^{1/4}\), \(v=e^{it}/(1+r^4)^{1/4}\), initially \(0\le r<\infty\), with the omitted coordinate-zero cases taken as limits. Direct substitution gives
\[
\langle F(u,v),J(u,v)\rangle=\frac{r^3e^{it}+re^{-it}}{1+r^4}.
\]
Put \(\eta=2r/(1+r^2)\in[0,1]\), \(s=\eta^2\). Interchanging the coordinates changes only the sign of the imaginary part, so \(W(F)\) is the union of the centered ellipse curves
\[
E_s=\{a_s\cos t+i b_s\sin t:0\le t<2\pi\},\quad
 a_s=\frac{\sqrt s}{2-s},\quad b_s=\frac{\sqrt{s(1-s)}}{2-s},\quad 0\le s\le1.
\]
The endpoints are \(E_0=\{0\}\) and \(E_1=[-1,1]\). This agrees with the general two-by-two orbit formula in the 2026 reference, but further exact optimization is needed below.

**Exact support and the angular transition.** The support of \(E_s\) in direction \(\phi\) is \(\sqrt{a_s^2\cos^2\phi+b_s^2\sin^2\phi}\). With \(q=\sin^2\phi\), its square is
\[
H_q(s)=\frac{s(1-qs)}{(2-s)^2},\qquad H_q'(s)=\frac{2+s(1-4q)}{(2-s)^3}.
\]
For \(q\le3/4\), the maximum occurs at \(s=1\) and equals \(1-q\). For \(q>3/4\), it occurs uniquely at \(s=2/(4q-1)\in(2/3,1)\) and equals \(1/[8(2q-1)]\). Square roots give the displayed support function and the sharp transition. Its smallest directional support is \(1/(2\sqrt2)\) in vertical directions, establishing the centered inradius once convexity is shown.

**Actual, not just convex-hull, boundary.** Fix \(x\in[0,1)\). Since \(a_s\) strictly increases from zero to one, admissible ellipses with real coordinate \(x\) are those for \(s\) in a closed interval ending at one. Their squared ordinates are
\[
G_x(s)=(1-s)\left(\frac{s}{(2-s)^2}-x^2\right).
\]
The attainable ordinates fill the entire symmetric interval between their two extreme values, because \(s\mapsto\sqrt{G_x(s)}\) is continuous, vanishes at both interval endpoints, and all intermediate heights occur on an ellipse. Moreover
\[
G_x'(s)=x^2-\frac{3s-2}{(2-s)^3}.
\]
The function \(s\mapsto(3s-2)/(2-s)^3\) increases strictly from zero to one on \([2/3,1]\), with derivative \(6s/(2-s)^4>0\). Thus the unique maximum is achieved at a parameter \(s\in[2/3,1)\) satisfying
\[
x^2=\frac{3s-2}{(2-s)^3},\qquad
\max G_x=\frac{(1-s)^2(s+2)}{(2-s)^3}.
\]
These are the stated coordinates of the first-quadrant boundary. At \(x=1\), only \(y=0\) is attainable. Writing the upper boundary as \(y=f(x)\), differentiation at its maximizing parameter gives
\[
f'(x)=-\sqrt{\frac{3s(x)-2}{s(x)+2}}.
\]
As \(x\) increases, \(s(x)\) strictly increases and the right-hand side strictly decreases, hence \(f\) is strictly concave on \((0,1)\), with \(f'(0)=0\). Therefore \(x\mapsto f(|x|)\) is concave on \([-1,1]\), and \(W(F)=\{x+iy:|x|\le1,\ |y|\le f(|x|)\}\) is convex. This establishes that the optimized support describes the actual numerical range, not merely its convex hull.

**Area.** Symmetry and the boundary parametrization give \(\operatorname{Area}W(F)=4\int_0^1 f(x)\,dx\). Substituting \(u=\sqrt{(3s-2)/(s+2)}\) yields the rational integral
\[
\operatorname{Area}W(F)=4\int_0^{1/\sqrt3}\frac{3(1+u^2)(1-3u^2)}{8(1-u^2)^4}\,du
=\frac{3\sqrt3}{8}+\frac3{16}\log(2+\sqrt3).
\]
The affine identity follows directly from the norming-functional definition.

## Verification
Running the supplied `CHECK.py` with Python, SciPy, and standard math functions checks 421 directions against a separate bounded numerical maximization, 398 boundary parameter points against the original ellipses, and two area/inradius identities: 821 finite checks passed. The analytic proof above, rather than finite testing, establishes the full continuum statements. Reproduction command: `python CHECK.py`.

## Relationship to prior work
Müller and Tomilov (2026), Proposition 2.1 and Remark 2.2, establish a general union-of-ellipses parametrization for arbitrary complex \(2\times2\) operators on \(\ell_p^2\); their Section 2 gives nonconvex and triangular star-shaped examples. Mandal, Bhanja, Bag, and Paul (2020), Theorems 2.2, 2.6, and 2.9, give a nilpotent disk, triangular convexity, and a nonconvexity sufficient condition, respectively. These general results are the foundation and are not claimed as new. The contribution here is the fully optimized support-angle bifurcation, identification of the *actual* convex body for the nontriangular quartic coordinate flip, its explicit boundary and area/inradius. Direct specialization of the source ellipse formula alone does not state those optimizations or the area.

## Limitations
The classification is specific to the quartic exponent and an affine two-parameter family. Neither convexity for general complex matrices nor an area formula for other exponents is asserted. The general ellipse formula already covers these operators parametrically; consequently the priority of the explicit optimization should be checked against wider older numerical-range literature. Finite checks are supplementary; independent scientific review has not been performed.

## References
- V. Müller and Y. Tomilov, *Numerical and essential numerical ranges on* \(\ell_p\), arXiv:2606.22693v1, publicly submitted 21 June 2026, especially Section 2, Proposition 2.1 and Remarks 2.2–2.3.
- K. Mandal, A. Bhanja, S. Bag and K. Paul, *On the numerical range of operators on some special Banach spaces*, arXiv:2005.01288v1, publicly submitted 4 May 2020, especially Section 2.
