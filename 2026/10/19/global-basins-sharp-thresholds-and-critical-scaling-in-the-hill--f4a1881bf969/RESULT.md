# Global basins, sharp thresholds, and critical scaling in the Hill-feedback four-cycle

## Finding

Consider the positive planar discrete map
\[
T_{b,m}(x,y)=\left(y,\frac{b}{1+x^m}\right),\qquad (x,y)\in(0,\infty)^2,\quad b,m>0.
\]
Put \(g(z)=b/(1+z^m)\). There is a unique \(w>0\) satisfying \(g(w)=w\), equivalently \(b=w(1+w^m)\). For \(m>1\) define
\[
w_*=(m-1)^{-1/m},\qquad b_*=m(m-1)^{-(m+1)/m}.
\]

**Theorem (global phase portrait and sharp transition).** For \(0<m\le1\), all positive trajectories converge to \((w,w)\). For \(m>1\), the same conclusion holds when \(0<b\le b_*\), and convergence is exponential when \(b<b_*\). Exactly at \(b=b_*\), each initial coordinate \(z_0\ne w_*\) obeys the **sharp** asymptotic law
\[
\boxed{\lim_{n\to\infty}\sqrt n\,[h^n(z_0)-w_*]
=\operatorname{sgn}(z_0-w_*)\,w_*\sqrt{\frac{3}{m^2-1}},\qquad h=g\circ g,}
\]
where \(h^n\) denotes the \(n\)-fold iterate. Consequently the formula describes each coordinate of \(T^{4n}(x_0,y_0)\); a coordinate initially equal to \(w_*\) remains equal to it at these return times.

For \(m>1\) and \(b>b_*\), there is exactly one positive primitive two-cycle \(0<u<w<v\) of \(g\): \(g(u)=v\), \(g(v)=u\). Every positive orbit of \(T\) converges to precisely one of three periodic sets: the fixed point \((w,w)\), the attracting four-cycle
\[
(u,u)\to(u,v)\to(v,v)\to(v,u)\to(u,u),
\]
or the saddle four-cycle
\[
(w,u)\to(u,w)\to(w,v)\to(v,w)\to(w,u).
\]
The fixed point attracts only itself; **the exact basin boundary** between phases of the attracting cycle is \(\{x=w\}\cup\{y=w\}\). Starting on either of these lines, apart from their intersection, the orbit converges to the saddle four-cycle; all other initial points converge to the attracting four-cycle. The map has **no other periodic points of any period**. More precisely, \(T^4\) has exactly nine fixed points when \(b>b_*\) and exactly one when \(b\le b_*\).

The multipliers of \(T^4\) at the attracting four-cycle are \((q,q)\), at the saddle four-cycle \((\rho,q)\), and at \((w,w)\) are \((\rho,\rho)\), where \(\rho>1\) and \(0<q<1\). If \(r=v/u=e^{2t}>1\), then
\[
\boxed{q=\left(\frac{m\sinh t}{\sinh(mt)}\right)^2<1,\qquad
\rho=\left(\frac{m w^m}{1+w^m}\right)^2>1.}
\]
There is also a sharp square-root amplitude for the birth of the two-cycle: as \(b\downarrow b_*\), with \(w=w(b)\),
\[
\boxed{\frac{v-w}{\sqrt{b-b_*}}\longrightarrow
\sqrt{\frac{6(m-1)w_*}{m(m+1)}}\,,\qquad
\frac{w-u}{\sqrt{b-b_*}}\longrightarrow
\sqrt{\frac{6(m-1)w_*}{m(m+1)}}\,.}
\]

For the representative case \(m=2\), \(b_*=2\) and, when \(b>2\),
\[
\boxed{u=\frac{b-\sqrt{b^2-4}}{2},\qquad
v=\frac{b+\sqrt{b^2-4}}{2},\qquad q=\frac4{b^2}.}
\]

## Assumptions and scope

All parameters \(b,m\) and initial coordinates are strictly positive real numbers; \(m\) need not be an integer. The map acts in discrete time without noise or finite-step approximation. Global attraction refers to convergence in Euclidean distance to the relevant finite invariant orbit, not convergence to one fixed phase of that orbit under every integer time. Under \(T^4\), every coordinate has a specific phase determined by its initial side of \(w\). For the critical limit, \(n\) counts blocks of four original iterations and the sign is fixed by the initial coordinate. No uniform error bound near \(m=1\) or as \(b\) varies jointly with \(n\) is asserted.

## Proof

**1. Exact reduction and trapping.** For all positive \(x,y\), direct substitution gives
\[
T^2(x,y)=(g(x),g(y)),\qquad T^4(x,y)=(h(x),h(y)),\quad h=g\circ g.
\]
The scalar \(g\) is strictly decreasing and maps \((0,\infty)\) into \((0,b)\). Since \(z\mapsto z(1+z^m)\) is strictly increasing from zero to infinity, its sole positive fixed point is \(w\). The function \(h\) is strictly increasing, continuous, and maps \((0,\infty)\) into a bounded positive interval. Therefore each orbit \(h^n(z)\) is monotone from its first comparison \(h(z)\gtreqless z\), remains bounded and bounded away from zero after its first iterate, and converges to a fixed point of \(h\). Moreover, a monotone scalar map has no periodic points of period greater than one. Consequently every periodic point of \(T\) must satisfy \(T^4(x,y)=(x,y)\).

**2. At most three scalar fixed points.** For \(m>1\), the Schwarzian derivative of \(g\), computed directly, is
\[
Sg(z)=\frac{g'''(z)}{g'(z)}-\frac32\left(\frac{g''(z)}{g'(z)}\right)^2
=-\frac{m^2-1}{2z^2}<0.
\]
The chain rule gives \(Sh(z)=Sg(g(z))g'(z)^2+Sg(z)<0\). As \(h'>0\), set \(\psi(z)=1/\sqrt{h'(z)}\). Differentiating shows \(\psi''(z)=-\frac12 Sh(z)\psi(z)>0\). Thus \(\psi\) is strictly convex, and the equation \(h'(z)=1\) has at most two solutions. By Rolle's theorem, \(h(z)=z\) has at most three solutions on \((0,\infty)\).

**3. Sharp existence threshold, uniqueness, and global basins.** At the scalar fixed point,
\[
g'(w)=-\frac{m w^m}{1+w^m},\qquad h'(w)=\rho=\left(\frac{m w^m}{1+w^m}\right)^2.
\]
Therefore \(\rho\gtreqless1\) exactly when \(b\gtreqless b_*\). If \(b>b_*\), the function \(h(z)-z\) is negative just left of \(w\) and positive just right of it, while \(h(0)>0\) by continuous extension and \(h(z)-z<0\) when \(z>b\). Thus it has roots \(u<w<v\), and Step 2 makes them unique. A root of \(h\) other than \(w\) is interchanged with a second root by \(g\); since \(g\) decreases, \(g(u)=v\) and \(g(v)=u\). Conversely, for \(b<b_*\), the presence of two further roots would force them to be a \(g\)-interchanged pair. Step 4 gives \(h'(u)=h'(v)=q<1\), so both are strict downcrossings of \(h(z)-z\); the middle root \(w\) must then be an upcrossing, contradicting \(h'(w)<1\). At equality, \(h'(w)=1\); two further roots would, by Rolle, force three solutions of \(h'(z)=1\), contradicting Step 2. Hence there is only \(w\) when \(b\le b_*\).

For \(b>b_*\), the sign sequence of \(h(z)-z\) on \((0,u),(u,w),(w,v),(v,\infty)\) is \((+,-,+,-)\). This follows from the boundary signs and exactly three distinct roots (which are simple at \(w\)); the outer roots have strict negative derivative, as is also verified in Step 4. Monotonicity of \(h\) preserves each side of every fixed point. Scalar convergence from Step 1 now yields
\[
\lim_{n\to\infty}h^n(z)=
\begin{cases}
u,&z<w,\\ w,&z=w,\\ v,&z>w.\end{cases}
\]
Here \(u\) is the smaller two-cycle coordinate defined above. Applying this separately to both coordinates under \(T^4\), then applying \(T\) for the three other residues modulo four, yields the exact global basins and the two four-cycles stated above. The nine grid points \(\{u,w,v\}^2\) are the complete fixed-point set of \(T^4\), split into the fixed point and two four-cycles. When \(b\le b_*\), the same reasoning gives global attraction to \((w,w)\). For \(m\le1\), write \(z=e^s\); the derivative of \(\log g(e^s)\) with respect to \(s\) is \(-m e^{ms}/(1+e^{ms})\), of magnitude at most \(m\). All scalar trajectories enter the compact interval \([g(b),b]\), on which this derivative has supremum strictly below one when \(m\le1\). The contraction principle gives geometric convergence to \(w\). For \(m>1,b<b_*\), \(0<h'(w)=\rho<1\) and convergence to its unique fixed point implies eventual exponential convergence, hence also under \(T\).

**4. Hyperbolicity.** At a scalar two-cycle,
\[
q=h'(u)=h'(v)=g'(u)g'(v)=\frac{m^2(uv)^m}{(1+u^m)(1+v^m)}.
\]
Writing \(r=v/u=e^{2t}>1\), the two cycle equations imply \(u^m=(r-1)/(r^m-r)\). Simplification gives
\[
q=\frac{m^2r^{m-1}(r-1)^2}{(r^m-1)^2}
=\left(\frac{m\sinh t}{\sinh(mt)}\right)^2.
\]
For \(m>1,t>0\), strict convexity of \(\sinh\) on the positive half-line yields \(\sinh(mt)>m\sinh(t)\), so \(q<1\). The matrix \(D(T^4)=\operatorname{diag}(h'(x),h'(y))\) at all grid points gives the stated eigenvalues. Thus the outer roots of \(h(z)-z\) are simple with negative slope \(q-1\), justifying the strict interval signs in Step 3. At \(b=b_*\), \(\rho=1\) and these hyperbolic conclusions do not apply.

**5. Critical time law.** Fix \(m>1,b=b_*\) and write \(z=w_*+s\). The identities \(g'(w_*)=-1\) and \(h=g\circ g\) give \(h'(w_*)=1\), \(h''(w_*)=0\). By the Schwarzian chain rule, \(Sh(w_*)=2Sg(w_*)=-(m^2-1)/w_*^2\). Since \(h''(w_*)=0\), this means \(h'''(w_*)=-(m^2-1)/w_*^2\). Consequently
\[
h(w_*+s)-w_*=s-cs^3+O(s^4),\qquad c=\frac{m^2-1}{6w_*^2}>0.
\]
Step 3 implies \(s_n=h^n(z_0)-w_*\to0\) without changing sign. If \(s_0\ne0\), no iterate can equal zero because \(h\) is strictly increasing and fixes \(w_*\). The Taylor expansion yields
\[
\frac1{s_{n+1}^2}-\frac1{s_n^2}=2c+O(|s_n|)\longrightarrow2c.
\]
Cesàro summation therefore proves \(1/(ns_n^2)\to2c\), while the preserved sign gives \(\sqrt n\,s_n\to\operatorname{sgn}(s_0)/\sqrt{2c}\), the claimed coefficient.

**6. Square-root splitting.** As \(b\downarrow b_*\), the two additional roots \(u,v\) converge to \(w_*\): they lie in a bounded positive interval, cannot have zero as a limit because \(h(0)>0\), and every limit is a fixed point of \(h\) at \(b_*\), whose only fixed point is \(w_*\). Let \(w=w(b)\), \(\delta=b-b_*>0\), and \(s=z-w\). Differentiating \(b=w(1+w^m)\) and \(\rho(b)\) at \(b_*\) gives
\[
\rho(b)-1=K\delta+O(\delta^2),\qquad K=\frac{(m-1)^2}{m w_*}>0.
\]
Smoothness of \(h_b\) near \((b_*,w_*)\) and Step 5 give, uniformly for small \(\delta,s\),
\[
\frac{h_b(w+s)-w-s}{s}=K\delta-cs^2+O(\delta^2+\delta|s|+|s|^3),\qquad s\ne0.
\]
For \(s=u-w\) or \(s=v-w\), this expression vanishes. Because \(s\to0\), the error is negligible relative to \(\delta+s^2\), proving \(s^2/\delta\to K/c\). The negative and positive signs determine the two limits, and \(K/c=6(m-1)w_*/[m(m+1)]\). The explicit quadratic-power formulas follow by solving \(g(u)=v,g(v)=u\) at \(m=2\), which yield \(uv=1\) and \(u+v=b\).

## Verification

The standalone `checker.py` uses standard-library exact rational arithmetic for \(m=2\) and numerically probes distinct noninteger exponents, all three hyperbolic regimes, critical trajectories, and the square-root limit. Run `python3 checker.py` in the directory containing the files. It outputs `PASS: 208 exact rational, finite-iteration, and numerical diagnostics`. These finite tests are not used as substitutes for the global existence, uniqueness, and infinite-time proof in Steps 1–6.

## Relationship to prior work

Ohmori and Yamazaki (2023, arXiv:2305.05908v1, Section 3, equation (8)) introduce this exact rational map as the infinite-time-step limit of a positive tropical negative-feedback discretization. They explore Neimark–Sacker and max-plus dynamics; their formula for two periodic cycles and return maps belongs to the *different* piecewise-linear max-plus limit. Yamazaki and Ohmori (2023, arXiv:2306.00733v1, Section 3) additionally report eight noncentral fourth-iterate fixed points numerically for the rational limit (especially \(m=2\)), consistent with the cycles found here; these numerical periodic points and qualitative stable/unstable observations are acknowledged as prior information, not claimed as new. The present theorem instead proves the **global positive-quadrant basins and exact saddle separatrices for every real \(m>1\)**, the sharp threshold and complete period exclusion, the explicit critical \(n^{-1/2}\) coefficient, and the rigorous parameter square-root amplitude. Classical one-dimensional negative-Schwarzian and monotone-iteration principles are used as standard methods.

Gibo and Ito (2015) introduced closely related tropical/ultradiscrete biological feedback models and established bifurcation conditions. Their abstract was accessible, but the full text was not; thus possible earlier coverage of particular claims in this paper remains an explicit priority risk, rather than being asserted absent. The result concerns the exact rational limit and should not be read as a global classification of its finite-step discretizations or its max-plus limit.

## Limitations

The theorem concerns autonomous positive real dynamics only; it does not cover finite tropical step \(\tau\), the nondifferentiable max-plus limit, or stochastic perturbations. The proof is self-contained modulo elementary Schwarzian calculus and compactness. The critical coefficient is asymptotic at each fixed initial point, not uniform over initial data, and the square-root law holds for each fixed \(m>1\). A plausible earlier model paper (Gibo–Ito 2015) was not fully accessible, so independent historical priority verification remains worthwhile. Finite computations cannot substitute for the proof or determine historical priority.

## References

1. S. Ohmori and Y. Yamazaki, *Dynamical properties of discrete negative feedback models*, arXiv:2305.05908v1 (first publicly posted 2023-05-10), especially Sections 2–3, equations (2), (8), and (9). https://arxiv.org/pdf/2305.05908
2. Y. Yamazaki and S. Ohmori, *Emergence of ultradiscrete states due to phase lock caused by saddle-node bifurcation in discrete limit cycles*, arXiv:2306.00733v1 (first publicly posted 2023-05-13), especially Section 3 and equation (10). https://arxiv.org/pdf/2306.00733
3. S. Ohmori and Y. Yamazaki, *Types and stability of fixed points for positivity-preserving discretized dynamical systems in two dimensions*, arXiv:2304.01573v1 (2023-04-04), for general fixed-point local stability, not global basins. https://arxiv.org/pdf/2304.01573
4. S. Gibo and H. Ito, *Discrete and ultradiscrete models for biological rhythms comprising a simple negative feedback loop*, Journal of Theoretical Biology 378 (2015), 89–95, DOI: 10.1016/j.jtbi.2015.04.024 (abstract inspected; full text unavailable).
