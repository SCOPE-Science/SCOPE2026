# A sharp negative-parameter bistability window in the ETM-3D quadratic flow

## Finding
Consider the real-parameter polynomial flow
\[
\dot x=-2x-\rho y+yz,\qquad
\dot y=x-y+\rho z-2xz,\qquad
\dot z=\rho y-5z+xy.
\]
Define the degree-eight polynomial
\[
\begin{aligned}
H(r)={}&594r^8-2076r^7-5948r^6+20050r^5+25505r^4\\
&-66100r^3-63325r^2+77500r+75000.
\end{aligned}
\]
Let \(r_f\) be the **unique** zero of \(H\) in \((-1.308661,-1.308660)\), and set
\[
r_t=\frac{5-\sqrt{105}}4=-1.311737691489899\ldots.
\]
Then \(r_f=-1.30866054409146\ldots\), with \(r_t<r_f<0\). The following statements hold.

1. For every \(r_f<\rho\leq0\), the origin is globally exponentially attracting. At \(\rho=r_f\), a nonzero equilibrium appears, so global attraction of the origin does not extend to that endpoint.
2. **Exactly for \(r_t<\rho<r_f\) among negative parameters**, the origin is a hyperbolic sink and a second, distinct hyperbolic sink coexists with it. There is exactly one additional nonzero equilibrium, a hyperbolic saddle with one unstable dimension. Thus there are precisely three equilibria on this interval.
3. At \(\rho=r_f\) the two nonzero equilibria meet in a nondegenerate saddle-node while the origin remains a hyperbolic sink. At \(\rho=r_t\), the saddle branch crosses the origin in a generic transcritical bifurcation; the origin has a simple zero eigenvalue and is no longer a hyperbolic sink. For every \(\rho<r_t\), the origin is linearly unstable.

The exact width of the **two-sink coexistence window** is
\[
\boxed{r_f-r_t=0.00307714739844\ldots}.
\]
The result concerns equilibria and their local stability. It makes no assertion about basin volumes or additional periodic or chaotic invariant sets in the coexistence window.

## Assumptions and scope
The vector field is considered on \(\mathbb R^3\), with \(\rho\in\mathbb R\). The new bifurcation classification concerns the negative-parameter branch \(\rho<0\), outside the nonnegative benchmark branch studied in the motivating paper. The source establishes global ultimate boundedness for arbitrary real \(\rho\), and supplies the quadratic vector field and equilibrium reduction used here. “Sink” means that all three eigenvalues of the equilibrium Jacobian have strictly negative real parts. All stated critical values are algebraically defined, not numerically fitted.

## Proof
**1. Reduction and exact discriminant.** For any nonzero equilibrium in the range \(-1.312\le\rho\le0\), put
\[
D(x,\rho)=2x^2+\rho x+5-\rho^2,
\qquad y=\frac{5x}{D},\quad z=\frac{x(\rho+x)}D.
\]
In the rectangles used below, \(D>29/10\). More generally, if \(x=0\) and \(\rho^2\ne5\), the only equilibrium with first coordinate zero is the origin. Substitution into the first equation gives
\[
-\frac{xP(x,\rho)}{D(x,\rho)^2}=0,
\]
where
\[
\begin{aligned}
P(x,r)={}&8x^4+8rx^3+(-6r^2+10r+35)x^2\\
&+(-4r^3+5r^2+15r)x\\
&+2r^4-5r^3-20r^2+25r+50.
\end{aligned}
\]
The exact identities
\[
\operatorname{disc}_xP=12000H(r),\qquad
P(0,r)=(r^2-5)(2r^2-5r-10)
\]
follow by polynomial arithmetic. A rational Sturm computation isolates all four real roots of \(H\) in
\[
\begin{gathered}
(-2.011935,-2.011934),\quad(-1.308661,-1.308660),\\
(2.188758,2.188759),\quad(3.355161,3.355162).
\end{gathered}
\]
Each interval contains exactly one root; there are no other real roots. At the exact test value \(r=-131/100\), the quartic has precisely two real zeros, isolated respectively in \((0.034,0.035)\) and \((0.173,0.174)\). At \(r=-13/10\) it has no real zero. The only discriminant zero between these parameters is \(r_f\), and no zero can pass through \(x=0\), since \(r_t<-131/100\). Thus the two positive equilibria coalesce at \(r_f\).

**2. Uniform shape and generic fold.** On \(-1.312\le r\le-1.308\) and \(0\le x\le1/4\), direct exact bounds give
\[
P_{xx}=96(x+r/4)^2+70+20r-18r^2>12,
\qquad P_r>28.
\]
Also \(P(1/4,r)>P(1/4,-1.312)>0\). Because the double root at \(r_f\) is approached by two roots in \((0,1/4)\), it lies there, and \(P_{xx}>0\) and \(P_r>0\) at this double root. The scalar equilibrium equation therefore has a nondegenerate fold. Its first-coordinate double root lies in \((0.10,0.11)\); the remaining two directions of the full flow are strictly contracting by the estimates in Step 3. This is a genuine codimension-one saddle-node of the vector field.

For \(r_t<r<r_f\), the fixed double-root location \(x_f\) satisfies \(P(x_f,r)<P(x_f,r_f)=0\), by the positive lower bound for \(P_r\). Meanwhile \(P(0,r)>0\) and \(P(1/4,r)>0\). Strict convexity gives exactly two simple roots
\[
0<x_-(r)<x_f<x_+(r)<1/4,
\qquad P_x(x_-,r)<0<P_x(x_+,r),
\]
and no other real roots. They yield exactly two nonzero equilibria.

**3. Stability of the two branches.** At a nonzero equilibrium \(E(x,r)=(x,5x/D,x(r+x)/D)\), the Jacobian is
\[
J=\begin{pmatrix}
-2&-r+z&y\\1-2z&-1&r-2x\\y&r+x&-5
\end{pmatrix}.
\]
Its trace is \(-8\); the determinant identity at roots of \(P\) is
\[
\det J=-\frac{xP_x(x,r)}D.
\]
Write the characteristic polynomial as \(\lambda^3+8\lambda^2+a_2\lambda+a_3\). In the full rectangle above, \(D>29/10\), \(0<y<1/2\), \(-1/8<z<0\), and direct principal-minor bounds imply \(a_2>12\). The same rational bounds give \(|P_x|<70\), so \(|a_3|=|xP_x|/D<7\). At the larger root, \(a_3>0\), and
\[
8>0,\quad a_2>12>0,\quad a_3>0,\quad8a_2>a_3.
\]
The cubic Routh–Hurwitz criterion therefore proves that \(E(x_+,r)\) is a hyperbolic sink. At the smaller root, \(a_3<0\): its characteristic polynomial has exactly one positive real root (Descartes' rule), while the other two have negative real parts, so it is a hyperbolic saddle with one unstable dimension. At \(r=r_f\), the nonzero double equilibrium has one zero eigenvalue and two eigenvalues with negative real parts.

At the origin,
\[
p_0(\lambda)=\lambda^3+8\lambda^2+(17+r-r^2)\lambda+(10+5r-2r^2).
\]
For \(r_t<r<r_f\), its non-leading coefficients are positive and \(8(17+r-r^2)-(10+5r-2r^2)=126+3r-6r^2>100\). Hence the origin is also a hyperbolic sink. At \(r=r_t\), the constant term vanishes simply. Since \(P_x(0,r_t)\ne0\) and \(P_r(0,r_t)\ne0\), the nonzero equilibrium branch crosses the origin transversally as \(r\) passes through \(r_t\); the origin's simple eigenvalue crosses zero. This is a generic transcritical bifurcation. For all \(r<r_t\), \(10+5r-2r^2<0\), so \(p_0\) has a positive real root and the origin is linearly unstable.

**4. Sharp global attraction to the right of the fold.** The quadratic nonlinearity \(N=(yz,-2xz,xy)\) cancels identically in the derivative of
\[
V_u=\tfrac12\bigl(ux^2+y^2+(2-u)z^2\bigr),\qquad0<u<2.
\]
By a two-endpoint Schur complement, \(\dot V_u<0\) for every nonzero state if and only if
\[
\Phi(u,r)=\frac1{8u}-\frac r4+r^2\left(\frac{3u}{40}+\frac15+\frac1{20(2-u)}\right)<1.
\]
For every \(r<0\), \(\Phi\) has a unique minimizing \(u\in(0,2)\), since
\[
\Phi_{uu}=\frac1{4u^3}+\frac{r^2}{10(2-u)^3}>0.
\]
Moreover \(\Phi_r<0\) at every negative \(r\). The minimum \(m(r)=\min_{0<u<2}\Phi(u,r)\) therefore decreases strictly as \(r\) increases through the negative half-line. At \(r=-131/100\), the verified nonzero equilibrium rules out strict global quadratic decay, so \(m(r)\ge1\). At \(r=-13/10\), \(\Phi(4/5,-13/10)=7433/7500<1\). There is consequently a unique crossing \(m(r)=1\) inside \((-1.31,-1.3)\). Eliminating \(u\) from \(\Phi=1\) and \(\Phi_u=0\) yields, up to a nonzero constant, \(r^4H(r)\). The Sturm count shows exactly one root of \(H\) in \((-1.31,-1.3)\), namely \(r_f\); hence the crossing occurs exactly at the equilibrium saddle-node. For every \(r_f<r<0\), some positive definite \(V_u\) satisfies a strict global quadratic dissipation inequality and proves exponential convergence of **every** solution to the origin. At \(r=0\), \(u=1\) gives the same conclusion.

Combining Steps 1–4, the origin and a separate hyperbolic nonzero sink coexist exactly on \((r_t,r_f)\) within the full negative parameter half-line. The strict endpoints follow from the nonhyperbolicity of the saddle-node and the origin crossing.

## Verification
The accompanying `verify_negative_etm.py` performs exact symbolic reconstruction of the equilibrium reduction, discriminant and Jacobian-determinant identities, rational Sturm isolations of every real root of \(H\), rational endpoint root counts, the Lyapunov resultant, and the stated uniform derivative and Routh–Hurwitz inequalities. Execute it with Python and SymPy. The script checks identities and finite exact algebraic certificates; no numerical iteration is treated as proof of the interval-wide claims.

## Relationship to prior work
Khalili-Amirabadi and Jalaeian-Farimani, arXiv:2610.04768v1 (first publicly submitted 2026-10-03), introduce the flow and prove global boundedness for real parameters. Their studied bifurcation region is explicitly \(\rho\ge0\), with positive saddle-node values and a positive-parameter transcritical crossing; they leave the negative branch for future study. The present claim is the exact *negative* coexistence window, including sink indices, a transcritical endpoint, and a sharp global-stability boundary.

The published mathematical result “Exact global-stability threshold at the first ETM-3D saddle-node” treats \(\rho\ge0\) and derives the positive critical value \(2.1887586269517\ldots\) from the same degree-eight discriminant. Its positive-domain theorem does not imply the two-sink window on the negative half-line, where the origin's linear constant term and the nonzero-root ordering differ. The polynomial and energy-cancelling technique are acknowledged as existing background. Goyal, Pontes Duff and Benner's energy-preserving quadratic-system framework supplies general quadratic stability criteria but no parameter-specific negative ETM-3D equilibrium census or stability partition.

## Limitations
The classification is for coexistence involving the **origin** and an additional **hyperbolic equilibrium sink** at negative \(\rho\). It is not a full classification of all attractors, basin boundaries or periodic trajectories elsewhere on the negative branch. The second, more negative fold at about \(-2.0119345\) lies outside the window. Generic normal-form labels describe local equilibrium bifurcations, not global heteroclinic connections. Scientific priority has not been independently verified.

## References
1. R. Khalili-Amirabadi and M. Jalaeian-Farimani, “ETM-3D: A One-Parameter Multistable Quadratic Flow with an Explicit Absorbing Set and Intermittent Chaos,” arXiv:2610.04768v1, 2026; https://arxiv.t3mt.com/html/2610.04768v1.
2. “Exact global-stability threshold at the first ETM-3D saddle-node,” published 2026-10-11; https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-global-stability-threshold-at-the-first-etm-3d-saddle-node--997f2098aca6.
3. P. Goyal, I. Pontes Duff and P. Benner, “Guaranteed Stable Quadratic Models and their Applications in SINDy and Operator Inference,” arXiv:2308.13819, 2023.
