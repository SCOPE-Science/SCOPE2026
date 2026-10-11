# Strict period decrease and sharp large-amplitude laws for quintic global centers

## Finding
For the quintic system
\[
\dot x=y,\qquad \dot y=-x-\alpha x^3y^2-\beta x^5,\qquad \alpha,\beta\ge0,
\]
let \(A>0\) denote the positive turning-point coordinate of a nonconstant trajectory, i.e. its maximum value of \(x\). All trajectories other than the origin are periodic, and there is exactly one such geometric periodic orbit for each \(A\).

In the **original physical time**, its minimal period \(T_{\alpha,\beta}(A)\) is identically \(2\pi\) in the linear case \(\alpha=\beta=0\). For every other parameter pair it decreases **strictly** with amplitude and is a continuous bijection
\[
T_{\alpha,\beta}:(0,\infty)\longrightarrow(0,2\pi).
\]
Thus for every prescribed period strictly between zero and \(2\pi\) there is exactly one geometric periodic orbit. The small-amplitude expansion is
\[
T_{\alpha,\beta}(A)=2\pi\left[1-\frac{\alpha+5\beta}{16}A^4+O(A^8)\right]\quad(A\downarrow0).
\]
The following high-amplitude limits sharpen the period classification:
\[
\begin{aligned}
&\lim_{A\to\infty}\sqrt\alpha\,A^2\sqrt{1+\beta A^4}\,T_{\alpha,\beta}(A)=2\pi &&(\alpha>0,\ \beta\ge0),\\
&\lim_{A\to\infty}A^2T_{0,\beta}(A)=\frac{2\sqrt3}{3\sqrt\beta}\,\mathrm B\!\left(\frac16,\frac12\right)&& (\alpha=0,\ \beta>0).
\end{aligned}
\]
Here \(\mathrm B\) is Euler's beta function. Consequently the strictly positive mixed-parameter case has decay \(T\sim2\pi/(\sqrt{\alpha\beta}\,A^4)\), whereas either positive coordinate axis has decay proportional to \(A^{-2}\), with different constants.

## Assumptions and scope
All parameters are real and nonnegative; \(A\in(0,\infty)\); solutions are taken for all real times. Period means the *minimal return time* of the nonconstant orbit, without any change or rescaling of physical time. The result covers **every** parameter choice in the global-center locus described in Theorem 1 of da Cruz and Llibre [1], using \(\alpha=-a_{32}\), \(\beta=-a_{50}\) and setting their other four quintic coefficients to zero. It does not claim that the full six-parameter system has only these centers locally.

## Proof
**1. A global energy foliation.** Set
\[
p(x)=e^{\alpha x^4/4},\qquad V(x)=\int_0^x e^{\alpha s^4/2}(s+\beta s^5)\,ds,
\]
and
\[
H(x,y)=\tfrac12p(x)^2y^2+V(x).
\]
Direct differentiation gives \(dH/dt=0\) along the stated polynomial vector field; indeed \(p'(x)/p(x)=\alpha x^3\) cancels the velocity-squared term. The function \(V\) is even and strictly increasing on \((0,\infty)\) and tends to infinity as \(|x|\to\infty\). Its only critical point is the origin. Each positive regular energy level \(H=V(A)\) is a compact simple closed curve; the vector field never vanishes there. Therefore every such level is one periodic trajectory. Its physical period is
\[
T(A)=4\int_0^A\frac{p(x)\,dx}{\sqrt{2[V(A)-V(x)]}}. \tag{1}
\]
The integral is finite because its turning-point singularity is integrable.

**2. Rigorous strict period monotonicity.** The odd, strictly increasing global coordinate \(z=\Phi(x):=\int_0^x p(s)\,ds\) transforms the second-order equation *without changing time* into
\[
\ddot z+h(z)=0,\qquad h(\Phi(x))=p(x)x(1+\beta x^4).
\]
For \(z>0\) put \(k(z)=h(z)/z\). Define \(B(x)=\Phi(x)/p(x)\) for \(x>0\); it satisfies \(B'=1-\alpha x^3B\), \(B(0)=0\), and
\[
k(\Phi(x))=\frac{x(1+\beta x^4)}{B(x)}. \tag{2}
\]
If \(\alpha>0\), comparison with \(c(x)=x/(1+\alpha x^4)\) yields
\[
c'(x)+\alpha x^3c(x)=1-\frac{4\alpha x^4}{(1+\alpha x^4)^2}<1,
\]
whereas \(B'+\alpha x^3B=1\), with the same zero initial value. Hence \(B(x)>c(x)\) for every \(x>0\); equivalently
\[
\frac{d}{dx}\frac{x}{B(x)}=\frac{(1+\alpha x^4)B(x)-x}{B(x)^2}>0.
\]
Since \(1+\beta x^4\) is nondecreasing, (2) shows that \(k\) is strictly increasing for \(\alpha>0\). If \(\alpha=0\), then \(k(z)=1+\beta z^4\), which is strictly increasing for \(\beta>0\), or constantly 1 when both parameters vanish.

Let \(R=\Phi(A)\). With \(U(z)=\int_0^z h(w)\,dw\), the usual positive half-cycle quadrature is *exactly*
\[
T(R)=4\int_0^1\left(2\int_u^1 t\,k(Rt)\,dt\right)^{-1/2}du. \tag{3}
\]
For \(\alpha+\beta>0\), each inner integral in (3) strictly increases with \(R\), so \(T\) strictly decreases. For \(\alpha=\beta=0\), (3) is \(2\pi\) identically. The integrable endpoint bounds imply continuity; analytic dependence away from zero follows from the analytic vector field and the regular turning points.

**3. The small-amplitude coefficient.** Expanding the time-preserving coordinate change,
\[
\Phi(x)=x+\frac{\alpha}{20}x^5+O(x^9),\qquad
h(z)=z+\left(\beta+\frac\alpha5\right)z^5+O(z^9).
\]
For a conservative oscillator with force \(z+\gamma z^5+O(z^9)\), expanding its turning-point quadrature gives \(2\pi[1-(5\gamma/16)R^4+O(R^8)]\). To see the coefficient directly, \(U(R)-U(Ru)=\tfrac12R^2(1-u^2)+\tfrac\gamma6R^6(1-u^6)+O(R^{10}(1-u^{10}))\), and
\[
\frac2\pi\int_0^1\frac{1+u^2+u^4}{\sqrt{1-u^2}}\,du=\frac{15}{8}.
\]
Since \(R=A+O(A^5)\), the asserted coefficient is \((5\beta+\alpha)/16\). The expansion is uniform on compact parameter sets.

**4. Pure quintic axis.** When \(\alpha=0<\beta\), equation (1), after \(x=Au\), becomes
\[
T_{0,\beta}(A)=4\int_0^1\frac{du}{\sqrt{(1-u^2)+(\beta A^4/3)(1-u^6)}}.
\]
Multiply by \(A^2\). Dominated convergence with majorant \(\sqrt{3/\beta}(1-u^6)^{-1/2}\) yields
\[
\lim_{A\to\infty}A^2T_{0,\beta}(A)
=4\sqrt{\frac3\beta}\int_0^1\frac{du}{\sqrt{1-u^6}}
=\frac{2\sqrt3}{3\sqrt\beta}\mathrm B\!\left(\frac16,\frac12\right).
\]

**5. Positive quadratic-velocity coefficient and an exact boundary layer.** Assume \(\alpha>0\). Write \(q=\alpha A^4\), \(\theta=\beta A^4\), and use \(x=A(1-u/q)\) in (1). Define for \(0\le u\le q\)
\[
F_A(u)=2\int_0^u\exp\left[\frac q2\left((1-v/q)^4-1\right)\right]
(1-v/q)\frac{1+\theta(1-v/q)^4}{1+\theta}\,dv.
\]
Cancellation of the exponentially large factor \(p(A)\) gives the **exact** identity
\[
\frac{\sqrt\alpha\,A^2\sqrt{1+\beta A^4}}4\,T(A)=
\int_0^q\frac{\exp\{\frac q4[(1-u/q)^4-1]\}}{\sqrt{F_A(u)}}\,du. \tag{4}
\]
For each fixed \(u>0\), since \(q\to\infty\) and \(\theta\ge0\), the integrand tends to \(e^{-u}/\sqrt{1-e^{-2u}}\). This limit does not depend on whether \(\theta\) remains zero or grows without bound.

For a global domination take \(q\ge2\). On \(0\le u\le q\), \((1-u/q)^4\le1-u/q\), so the numerator is at most \(e^{-u/4}\). For \(0\le v\le\min\{u,1\}\), one has \(1-v/q\ge1/2\), \((1-v/q)^4\ge1-4v/q\), and
\[
\frac{1+\theta(1-v/q)^4}{1+\theta}\ge(1-v/q)^4\ge\frac1{16}.
\]
Thus \(F_A(u)\ge(e^{-2}/16)\min\{u,1\}\). The integrand of (4), extended by zero beyond \(q\), is bounded by the integrable function \(4e\,e^{-u/4}/\sqrt{\min\{u,1\}}\), independently of \(A\). Dominated convergence now proves
\[
\lim_{A\to\infty}\frac{\sqrt\alpha\,A^2\sqrt{1+\beta A^4}}4T(A)
=\int_0^\infty\frac{e^{-u}}{\sqrt{1-e^{-2u}}}\,du=\frac\pi2.
\]
This proves the high-amplitude limit and, with the strictly decreasing period and \(T(A)\to2\pi\) as \(A\downarrow0\), establishes the claimed range and period uniqueness.

## Verification
The companion script `verify_period.py` checks the conserved-energy derivative symbolically, the comparison-function identity, the fifth-order transformed force, the elementary trigonometric integral, representative quadratures, and the two limiting beta-integral identities. It finishes with `CHECK_OK`. Those finite and symbolic tests are auxiliary; steps 1–5 above provide the all-parameter proof. The exact high-amplitude limit uses a uniform integrable majorant rather than an extrapolated finite-amplitude computation.

## Relationship to prior work
Da Cruz and Llibre [1] establish which members of their six-parameter quintic family are global centers; specifically their Theorem 1 identifies the two nonpositive coefficients appearing here. Their classification does not itself specify the physical period map or its large-amplitude constants. The position-dependent-mass first-integral construction is a standard Jacobi-multiplier idea illustrated by Chanda, Ghose-Choudhury, and Guha [2]; its mere use is not claimed as new. The pure quintic-oscillator axis and general Liénard period-function criteria also have prior literature [3,4]. The claimed extension is the **complete, strictly monotone physical period map for the particular full two-parameter global-center locus and its sharp boundary-layer limit when \(\alpha>0\)**. No global priority claim beyond the inspected literature is made.

## Limitations
The theorem is specific to \(\alpha,\beta\ge0\), the global-center stratum; it is not a classification of the full six-parameter quintic system's other local centers. The high-amplitude asymptotic is a limit, not a uniform relative-error bound in parameters approaching \(\alpha=0\). A parameter-free closed form for each finite period is not asserted. Some relevant broad Liénard period-function papers and the final journal revision were accessible only through abstracts or metadata; possible unpublished or differently phrased coverage remains a priority risk. No stability, forced response, or perturbative limit-cycle theorem is claimed.

## References
1. L. P. C. da Cruz and J. Llibre, *Global Centers in a Class of Quintic Polynomial Differential System*, arXiv:2312.05709v1 (first public 2023-12-09), https://arxiv.org/html/2312.05709v1 ; published as *Global centres in a class of quintic polynomial differential systems*, Proceedings of the Royal Society of Edinburgh A, doi:10.1017/prm.2024.43.
2. S. Chanda, A. Ghose-Choudhury and P. Guha, *Jacobi-Maupertuis metric of Liénard type equations and Jacobi Last Multiplier*, Electronic Journal of Differential Equations 2018, no. 120, https://ejde.math.txstate.edu/Volumes/2018/120/chanda.pdf .
3. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proceedings of the Royal Society of Edinburgh A 143 (2013), 205–221, doi:10.1017/S0308210511000096.
4. A. Beléndez, E. Arribas, T. Beléndez et al., *Closed-Form Exact Solutions for the Unforced Quintic Nonlinear Oscillator*, Advances in Mathematical Physics 2017, article 7396063, doi:10.1155/2017/7396063 (exact periods on the conservative axis).
