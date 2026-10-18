# Sharp small-exponent translation bifurcation for elliptical weighted perimeters

## Finding
For the ellipse \(E_\varepsilon\) with semiaxes \(1+\varepsilon\) and \(1-\varepsilon\), consider the power-weighted perimeter as a function of translation,
\[
 F_{p,\varepsilon}(z)=\int_{\partial E_\varepsilon}|x+z|^p\,ds(x),\qquad p>0.
\]
There are constants \(p_0,\varepsilon_0>0\) and a unique real-analytic curve \(\varepsilon_*(p)\) in the parameter rectangle \(0<p<p_0\), \(0\le\varepsilon<\varepsilon_0\) on which the minor-axis translational Hessian vanishes. It has the expansion
\[
 \varepsilon_*(p)=p+\tfrac32p^2+O(p^3)\quad(p\downarrow0).
\]
For \(0\le\varepsilon<\varepsilon_*(p)\) the ellipse center is a strict local translation minimum; for \(\varepsilon_*(p)<\varepsilon<\varepsilon_0\) it is a saddle. No classification of higher derivatives on the critical curve is asserted. Equivalently, for each fixed \(c\ge0\) and \(\varepsilon=cp\), with \(p\downarrow0\), the translational Hessian in major/minor axis coordinates obeys
\[
 \frac{D^2F_{p,cp}(0)}{\pi p^2}\longrightarrow
 \begin{pmatrix}1+c&0\\0&1-c\end{pmatrix}.
\]
This pinpoints how central symmetry and the weighted barycentric first-variation condition can coexist with translational instability at positive powers.

## Assumptions and scope
Work in the Euclidean plane. Set
\[
 E_\varepsilon=\left\{(x,y):\frac{x^2}{(1+\varepsilon)^2}+\frac{y^2}{(1-\varepsilon)^2}\le1\right\},\qquad 0\le\varepsilon<1.
\]
The boundary measure is Euclidean arclength. Translation varies the entire body, leaving its perimeter fixed and moving its location relative to the fixed origin; all derivatives concern \(z=0\). At \(0<p<p_0\) and \(0\le\varepsilon<\varepsilon_0\), the origin is strictly interior and all differentiations are legitimate. The constants are existential, not a claimed optimal global range.

## Proof
Write \(a=1+\varepsilon\), \(b=1-\varepsilon\), \(X(t)=(a\cos t,b\sin t)\), \(R(t)^2=a^2\cos^2t+b^2\sin^2t\), and \(w(t)=\sqrt{a^2\sin^2t+b^2\cos^2t}\). The direct second derivative of \(|X+z|^p\) at \(z=0\) gives the two diagonal entries
\[
 H_{ii}(p,\varepsilon)=p\int_0^{2\pi}
 (R^2)^{p/2-1}\left(1+(p-2)\frac{X_i^2}{R^2}\right)w(t)\,dt,\quad i=1,2.
\]
The off-diagonal entry vanishes by reflections. Divide by \(\pi p\) and write \(G_i(p,\varepsilon)=H_{ii}(p,\varepsilon)/(\pi p)\). Because \(R\) and \(w\) stay uniformly positive for \(|\varepsilon|<1\), these functions extend real-analytically to a neighborhood of \((0,0)\), including \(p=0\).

For the circle, elementary trigonometric integration gives \(G_1(p,0)=G_2(p,0)=p\). Differentiating the displayed integral with respect to \(\varepsilon\) at zero, using \(\int_0^{2\pi}\cos(2t)\sin^2t\,dt=-\pi/2\) and \(\int_0^{2\pi}\sin^2t\,dt=\pi\), yields
\[
 \partial_\varepsilon G_1(p,0)=\frac{(p-1)(p-2)}2,\qquad
 \partial_\varepsilon G_2(p,0)=-\frac{(p-1)(p-2)}2.
\]
In particular \(G_2(0,0)=0\), \(\partial_pG_2(0,0)=1\), and \(\partial_\varepsilon G_2(0,0)=-1\). The real-analytic implicit-function theorem produces a unique analytic local zero curve \(\varepsilon=\varepsilon_*(p)\) with \(\varepsilon_*'(0)=1\).

To obtain its second coefficient without an uncomputed remainder, note that at \(p=0\), \(G_i(0,\varepsilon)\) is \(1/\pi\) times the \(i\)-th diagonal derivative of \(\int_{\partial E_\varepsilon}\log|x+z|\,ds(x)\). The logarithmic kernel is harmonic in \(z\) near the origin, hence \(G_1(0,\varepsilon)+G_2(0,\varepsilon)=0\). Interchanging the ellipse semiaxes corresponds to a quarter-turn, so \(G_2(0,-\varepsilon)=G_1(0,\varepsilon)=-G_2(0,\varepsilon)\). Thus \(\partial_{\varepsilon\varepsilon}G_2(0,0)=0\). Since
\[
 \partial_\varepsilon G_2(p,0)=-1+\tfrac32p-\tfrac12p^2,
\]
Taylor's formula in two variables gives \(G_2(p,\varepsilon)=p-\varepsilon+\frac32p\varepsilon+O(p^2\varepsilon+p\varepsilon^2+\varepsilon^3)\). Substitution \(\varepsilon_*(p)=p+Ap^2+O(p^3)\) yields \(A=3/2\).

Shrinking the parameter rectangle, \(\partial_\varepsilon G_2<0\) throughout it. Also \(G_1(p,0)=p>0\) and \(\partial_\varepsilon G_1>0\) near \((0,0)\), so \(G_1(p,\varepsilon)>0\) for \(p>0,\varepsilon\ge0\) there. Accordingly the full Hessian is positive definite below \(\varepsilon_*\), indefinite above it, and has one zero eigenvalue at equality. Central symmetry makes the gradient at \(z=0\) vanish. Standard second-derivative tests prove the strict local-minimum and saddle assertions. Finally take \(\varepsilon=cp\) in the two Taylor expansions to obtain the normalized Hessian limit.

## Verification
The standalone checker `check_hessian.py` evaluates the two one-dimensional Hessian integrals with adaptive quadrature and checks the claimed asymptotic eigenvalues for several \(p\) and \(c\); it also numerically locates the zero curve and compares the coefficient \(3/2\). These finite numerical checks are secondary: analyticity, the implicit-function theorem, the harmonic-log identity, and the exact derivative integrals are the proof.

## Relationship to prior work
Csató–Giovagnoli–Roy introduce power-weighted perimeters, global shape-optimization problems, and the general first/second translation variation in their August 2026 preprint, especially §2.3 and equations (2.34)–(2.36). The present result specializes the weighted perimeter to symmetric ellipses but addresses a distinct question: the sharp *two-parameter* loss of local stability of the symmetry center under translation as the power tends to zero. The existing general Hessian identity is a starting tool, not a sign classification of the ellipse-family Hessian. Csató–Giovagnoli's October 2026 paper proves continuity and inclusion monotonicity for increasing nonnegative radial weights with the inner body containing the origin; that comparison does not order two translated copies of one ellipse. These distinctions do not establish absolute historical priority.

## Limitations
Only the small-power, near-disk parameter rectangle is classified. A zero Hessian eigenvalue at the critical curve does not decide nonlinear stability there. An earlier analytic-potential calculation could have already obtained an equivalent phase boundary; exhaustive historical priority is not established.

## References
- G. Csató, D. Giovagnoli, and P. Roy, *Weighted Perimeters and pth Moments of Inertia of Convex Curves and Surfaces*, arXiv:2608.19851v1, August 20, 2026, especially §2.3.
- G. Csató and D. Giovagnoli, *Continuity and monotonicity of weighted perimeters of convex bodies*, arXiv:2610.11677v1, October 8, 2026, especially Theorem 1.3.
