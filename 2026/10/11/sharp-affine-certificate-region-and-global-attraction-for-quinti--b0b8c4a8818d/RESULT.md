# Sharp affine-certificate region and global attraction for quintic Liénard flows

## Finding
For the real polynomial system
\[
\dot x=y-F(x),\qquad \dot y=-x,\qquad
F(x)=a_1x+a_2x^2+a_3x^3+a_4x^4+x^5,
\]
assume \(a_1>0\) and \(a_2,a_3,a_4\in\mathbb R\). Write \(H(x)=F(x)/x=a_1+a_2x+a_3x^2+a_4x^3+x^4\), interpreted polynomially at the origin.

**Theorem.** An \(\alpha\in\mathbb R\) satisfying \(\alpha x+2H(x)\geq0\) for every \(x\in\mathbb R\) exists **if and only if**
\[
a_3\geq \frac{a_4^2}{4}-2\sqrt{a_1}.
\]
For every coefficient tuple in this precisely characterized region, the origin is globally asymptotically stable: all initial conditions give complete, bounded forward solutions tending to \((0,0)\). In particular there are no nonconstant periodic orbits. The displayed inequality characterizes the **affine-certificate method**, not all parameters with globally stable dynamics.

The criterion permits every real \(a_2\), and can succeed where \(xF(x)\) changes sign. For instance \((a_1,a_2,a_3,a_4)=(1,5,-1,0)\) meets the criterion, although \(H(-1/2)=-27/16\) and hence the ordinary quadratic energy grows at some states. This example does not satisfy \(8a_3-3a_4^2>0\), a requirement of the sufficient conditions in the motivating source's Corollary 7.6.

## Assumptions and scope
The coefficients are constant real numbers; \(a_1>0\) is essential here for a hyperbolic local sink. Solutions are classical for the smooth polynomial vector field on \(\mathbb R^2\). The affine-certificate quantifier ranges over all \(\alpha\in\mathbb R\); its inequality must hold for **every** real \(x\). The statement does not assert nonexistence of cycles outside the certificate-feasibility region, and does not classify the boundary \(a_1=0\).

## Proof
**1. Exact elimination of the certificate parameter.** Put \(s=\sqrt{a_1}>0\), \(b=a_4/2\), and \(\beta=a_3-a_4^2/4+2s\). Direct expansion gives for any \(\alpha\)
\[
\frac{\alpha x+2H(x)}2
=\bigl(x^2+bx-s\bigr)^2+\beta x^2+\gamma x,
\quad \gamma=a_2+\alpha/2+a_4s.
\]
If \(\beta\geq0\), choose \(\alpha_0=-2a_2-2a_4s\), making \(\gamma=0\). The expression is a sum of two nonnegative squares (the second term is \(\beta x^2\)), establishing sufficiency, including equality in the coefficient threshold.

Conversely, the quadratic \(q(x)=x^2+bx-s\) has two real zeros of opposite sign because its constant term is negative. Denote them \(t>0\) and \(-u<0\), where \(u>0\). If \(\beta<0\) and a certificate were globally nonnegative, evaluation at \(t\) would force \(\gamma\geq-\beta t>0\), while evaluation at \(-u\) would force \(\gamma\leq\beta u<0\). This contradiction proves necessity for **every** possible \(\alpha\).

**2. Exclusion of periodic orbits.** In the feasible region take \(\alpha_0\) as above and write \(P(x)=\alpha_0x+2H(x)\geq0\). If \(\alpha_0\ne0\), direct differentiation of
\[
G(x,y)=\bigl(2-2\alpha_0y-\alpha_0^2x^2\bigr)e^{\alpha_0y}
\]
along the system yields the exact identity
\[
\frac{dG}{dt}=\alpha_0^2x^2e^{\alpha_0y}P(x)\geq0.
\]
The zero set is a finite union of vertical lines because \(P\) is a nonzero quartic. A nonconstant periodic orbit cannot remain in that set: its continuous \(x(t)\) would have to be constant, which together with \(\dot y=-x\) and \(\dot x=y-F(x)\) forces the equilibrium. Hence every nonconstant periodic orbit would make \(G\) strictly increase over a circuit, impossible. If \(\alpha_0=0\), then \(H(x)=P(x)/2\geq0\). The ordinary energy \(E=(x^2+y^2)/2\) obeys \(\dot E=-x^2H(x)\leq0\); because \(x^2H(x)\) is a nonzero polynomial, the same finite-zero-set argument excludes periodic orbits. Thus the possible zero-parameter edge case is covered without invoking a degenerating nonzero-parameter identity.

**3. Global boundedness and convergence.** The quintic leading term gives a globally proper trapping function even when the quadratic energy is not decreasing. Define \(\phi(x)=\int_0^x(1+s^2)^{-3}\,ds\), which is bounded, and
\[
W(x,y)=\tfrac12(x^2+y^2)-y\phi(x).
\]
Since \(\phi\) is bounded, \(W\) is proper and bounded below. Differentiation, followed by \(yF\leq (y^2+F^2)/2\), gives
\[
\dot W=-xF(x)+x\phi(x)-\phi'(x)y^2+\phi'(x)yF(x)
\leq -xF(x)+x\phi(x)+\tfrac12\phi'(x)F(x)^2-\tfrac12\phi'(x)y^2.
\]
As \(|x|\to\infty\), the first term is \(-x^6+O(|x|^5)\), while \(x\phi(x)=O(|x|)\) and \(\phi'(x)F(x)^2=O(x^4)\). The upper bound is strictly negative for \(|x|\) sufficiently large, uniformly in \(y\). On any fixed bounded \(x\)-interval, \(\phi'(x)>0\), so the negative quadratic term dominates for \(|y|\) large. Therefore \(\dot W<0\) outside a compact set. Every forward solution is bounded and forward complete by the standard coercive trapping-sublevel argument.

The only equilibrium is \((0,0)\); its Jacobian has characteristic polynomial \(\lambda^2+a_1\lambda+1\), so it is a hyperbolic sink for \(a_1>0\). A bounded planar omega-limit set not equal to a single equilibrium would, by the Poincaré–Bendixson alternatives, contain a periodic orbit or a nontrivial connecting graph. The former has been excluded; the latter cannot be formed with a unique hyperbolic sink, which has no nontrivial outgoing trajectory. Hence every forward orbit tends to the origin. Lyapunov stability follows from the local sink property, proving global asymptotic stability.

## Verification
The polynomial identity and the two opposite-sign evaluations are exact. A standalone standard-library checker, `check.py`, evaluates the identity over rational coefficient and state samples and checks the concrete sign-changing-damping example. These finite checks corroborate the algebra but do not replace the quantified proof. The proper-function estimates establish boundedness for all real initial conditions, rather than just a finite numerical sample.

## Relationship to prior work
Gasull and Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, Proposition 7.3, prove a general no-periodic-orbits implication from a constant-sign affine expression \(\alpha x+2H(x)\), and their Corollary 7.6 gives a more restrictive discriminant-based sufficient region for this exact quintic family. Those results and the underlying generalized-invariant-curve method are prior work. The contribution here is an exact **if-and-only-if algebraic description of the feasible certificate region**, an explicit optimizing coefficient, and the global-attraction consequence throughout that region, without a sign condition on the unoptimized damping polynomial. General earlier work on polynomial Liénard equations and quintic perturbations does not, in the inspected accessible material, supply this explicit optimized locus.

## Limitations
The sharpness is **only for the specified affine-certificate family**, not for actual existence or nonexistence of periodic orbits outside it. The restriction \(a_1>0\) is imposed for asymptotic stability. The derivation of global attraction uses classical planar dynamics; it does not provide an optimal rate of convergence. The principal published general criterion already supplies the no-cycle mechanism once a suitable certificate is found; a claim of priority for the mechanism itself would be incorrect. Earlier equivalent algebraic optimizations could exist under alternative terminology, and an independent audit has not been performed.

## References
[1] A. Gasull and H. Giacomini, *Number of limit cycles for planar systems with invariant algebraic curves*, arXiv:2210.15803v1 (public October 27, 2022); *Qualitative Theory of Dynamical Systems* 22, 44 (2023), DOI 10.1007/s12346-023-00746-7, especially Proposition 7.3 and Corollary 7.6. Primary MSC 34C07.

[2] R. Roussarie, *Putting a boundary to the space of Liénard equations*, *Discrete and Continuous Dynamical Systems* 17 (2007), 441–448, DOI 10.3934/dcds.2007.17.441 (general parameter-space and limit-cycle background).

[3] L. Li and J. Yang, *On the number of limit cycles for a quintic Liénard system under polynomial perturbations*, *Journal of Applied Analysis & Computation* 9 (2019), 2464–2481, DOI 10.11948/20190221 (different perturbative setting).
