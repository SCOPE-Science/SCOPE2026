# Uniform singular crossover for quintic global-center periods

## Finding
For the global-center quintic system
\[
\dot x=y,\qquad \dot y=-x-\alpha x^3y^2-\beta x^5,
\qquad \alpha\ge0,\ \beta>0,
\]
let \(T_{\alpha,\beta}(A)\) be the minimal period, in original physical time, of the periodic trajectory whose positive turning point is \(x=A>0\). For \(\lambda\ge0\) and \(0\le u<1\) define
\[
I_j(u,\lambda)=\int_u^1 v^j e^{\lambda v^4/2}\,dv,
\qquad
\Psi(\lambda)=2\sqrt2\int_0^1
\frac{e^{\lambda u^4/4}}{\sqrt{I_5(u,\lambda)}}\,du.
\]
Then the following **uniform finite-amplitude enclosure** holds simultaneously for all \(\alpha\ge0,\beta>0,A>0\):
\[
\boxed{\frac{\Psi(\alpha A^4)}{\sqrt{1+3/(\beta A^4)}}
\le A^2\sqrt\beta\,T_{\alpha,\beta}(A)
\le\Psi(\alpha A^4).}
\]
In particular its relative discrepancy from the crossover profile is at most \(1-(1+3/(\beta A^4))^{-1/2}\le3/(2\beta A^4)\), **independent of \(\alpha\)**. The positive continuous profile \(\Psi\) is strictly decreasing, with sharp opposite endpoint laws
\[
\Psi(0)=\frac{2\sqrt3}{3}\mathrm B\!\left(\frac16,\frac12\right),
\qquad \lim_{\lambda\to\infty}\sqrt\lambda\,\Psi(\lambda)=2\pi.
\]
Consequently, if \(A_n\to\infty\), \(\beta>0\) is fixed, and \(\alpha_n A_n^4\to\lambda_0\in[0,\infty)\), then
\[
A_n^2\sqrt\beta\,T_{\alpha_n,\beta}(A_n)\to\Psi(\lambda_0).
\]
The uniform estimate and the \(\lambda\to\infty\) limit also cover all sequences with \(\alpha_n A_n^4\to\infty\). This identifies the precise transition scale \(\alpha\asymp A^{-4}\), joining the pure-quintic and fixed-positive-\(\alpha\) period asymptotics.

## Assumptions and scope
All parameters and amplitudes are real in the stated ranges. The center is global, each nonzero energy level is a periodic oval, and \(A\) is its positive maximum coordinate (not its energy or a rescaled coordinate). The curve \(\Psi\) is dimensionless and does not depend on \(\beta\). At \(\alpha=0\) the lower/upper bounds remain valid; at \(\beta=0\) the normalization becomes undefined and no such claim is made. The first public version of the originating classification is dated 2023-12-09 [1].

## Proof
**1. Energy foliation and exact scaling.** Set
\[
H(x,y)=\tfrac12 e^{\alpha x^4/2}y^2+
\int_0^x (s+\beta s^5)e^{\alpha s^4/2}\,ds.
\]
Differentiating along the flow gives \(\dot H=0\) identically: the derivative of the kinetic exponential contributes \(\alpha x^3 e^{\alpha x^4/2}y^3\), which cancels the velocity-squared force. The potential is even, strictly increasing on positive coordinates, and coercive. Thus each positive regular energy level is a smooth compact oval free of equilibria, with period
\[
T(A)=4\int_0^A \frac{e^{\alpha x^4/4}}{\sqrt{2\int_x^A(s+\beta s^5)e^{\alpha s^4/2}\,ds}}\,dx.
\]
With \(u=x/A\), \(\lambda=\alpha A^4\), \(\varepsilon=1/(\beta A^4)\), the exact identity becomes
\[
A^2\sqrt\beta\,T(A)=2\sqrt2\int_0^1
\frac{e^{\lambda u^4/4}}{\sqrt{I_5(u,\lambda)+\varepsilon I_1(u,\lambda)}}\,du.
\tag{1}
\]
Both integrals in the denominator vanish linearly as \(u\uparrow1\); every displayed improper integral is finite.

**2. The uniform envelope.** For each fixed \(u\in[0,1)\), the ratio
\(R_u(\lambda)=I_1(u,\lambda)/I_5(u,\lambda)\) is the mean of the decreasing function \(v^{-4}\) under the probability density proportional to \(v^5 e^{\lambda v^4/2}\) on \([u,1]\). Differentiation under the integral gives
\[
R_u'(\lambda)=\tfrac12\operatorname{Cov}_\lambda(v^{-4},v^4)\le0.
\]
Indeed the covariance of an increasing and a decreasing function of the same real variable is nonpositive, as follows by symmetrizing two independent copies. Therefore
\[
0<R_u(\lambda)\le R_u(0)
=\frac{3(1-u^2)}{1-u^6}
=\frac3{1+u^2+u^4}\le3.
\]
Substitution into (1) sandwiches its integrand between the \(\varepsilon=0\) integrand and \((1+3\varepsilon)^{-1/2}\) times that integrand. Integration proves the enclosure without any restriction on \(\lambda\). The relative error bound follows from \(1-(1+t)^{-1/2}\le t/2\) for \(t\ge0\).

**3. Strictly decreasing crossover.** At each \(u<1\), logarithmic differentiation of the integrand defining \(\Psi\) gives
\[
\partial_\lambda\log\left(e^{\lambda u^4/4} I_5(u,\lambda)^{-1/2}\right)
=\frac14\left(u^4-\mathbb E_\lambda[v^4\mid u\le v\le1]\right)<0.
\]
Since \(v>u\) on a positive-measure integration interval, this is strict; continuity follows from locally uniform endpoint domination by \(C(1-u)^{-1/2}\). At \(\lambda=0\), \(I_5(u,0)=(1-u^6)/6\), and the substitution \(t=u^6\) proves
\[
\Psi(0)=4\sqrt3\int_0^1\frac{du}{\sqrt{1-u^6}}
=\frac{2\sqrt3}{3}\mathrm B(1/6,1/2).
\]

**4. The large-crossover endpoint.** Put \(t=\lambda(1-u)\) and divide the \(I_5\) denominator by \(e^{\lambda/2}/\lambda\). Then
\[
\sqrt\lambda\,\Psi(\lambda)=2\sqrt2\int_0^\lambda
\frac{\exp\{\tfrac\lambda4[(1-t/\lambda)^4-1]\}}
{\sqrt{J_\lambda(t)}}\,dt,
\]
where
\[
J_\lambda(t)=\int_0^t(1-w/\lambda)^5
\exp\{\tfrac\lambda2[(1-w/\lambda)^4-1]\}\,dw.
\]
For fixed \(t>0\), the numerator tends to \(e^{-t}\) and \(J_\lambda(t)\to(1-e^{-2t})/2\). For \(\lambda\ge2\), \((1-z)^4\le1-z\) for \(z\in[0,1]\) bounds the numerator by \(e^{-t/4}\). Restricting the integral defining \(J_\lambda\) to \(0\le w\le\min(t,1)\) and using \(1-w/\lambda\ge1/2\) and \((1-w/\lambda)^4\ge1-4w/\lambda\) yields
\[
J_\lambda(t)\ge\frac{e^{-2}}{32}\min\{t,1\}.
\]
Thus the integrand, extended by zero past \(\lambda\), has a global integrable majorant \(16 e\,e^{-t/4}/\sqrt{\min(t,1)}\). Dominated convergence gives
\[
\lim_{\lambda\to\infty}\sqrt\lambda\Psi(\lambda)
=4\int_0^\infty\frac{e^{-t}}{\sqrt{1-e^{-2t}}}\,dt
=2\pi.
\]

**5. Joint limit.** For fixed \(\beta>0\), the comparison factor tends uniformly to one whenever \(A\to\infty\), independently of \(\alpha\). Continuity of \(\Psi\) gives the finite-\(\lambda_0\) assertion; the endpoint calculation gives the divergent-\(\lambda\) matching. No unproved interchange of two limits is used.

## Verification
The standalone script `verify_crossover.py` checks the first-integral derivative by exact symbolic simplification, verifies 42 integral-ratio comparisons and 28 period enclosures across seven crossover scales, and compares \(\Psi(0)\) with the beta-function expression. It also checks strict decrease at those sample scales. Execute with Python 3, SymPy, and SciPy by `python verify_crossover.py`. It prints `CHECK_OK`. Its numerical quadratures check implementation consistency only; the universal assertions and infinite limits are proved in steps 1–5.

## Relationship to prior work
Da Cruz and Llibre [1] established the global-center parameter locus. The closely related published study [2] already gives the exact period quadrature, global strict monotonicity, and fixed-parameter large-amplitude asymptotics, including the two distinct endpoint constants; those are **not claimed as new**. In fact [2] explicitly notes that its high-amplitude estimate is not uniform as \(\alpha\to0\). The new result supplies a **dimensionless singular crossover for all joint approaches** to that parameter boundary and a **global explicit multiplicative error uniform over the entire nonnegative-\(\alpha\) half-line**. The needed stochastic-order comparison and uniform majorant are additional estimates not obtained by simply fixing parameters in [2]. General Jacobi-multiplier and Liénard period-function methods [3,4] provide background, not an established value for this profile.

## Limitations
This statement applies to \(\beta>0\), not the pure quadratic-velocity axis \(\beta=0\), and it supplies a sharp-order upper estimate for the relative error rather than a complete all-parameter expansion in inverse powers of \(\beta A^4\). The limiting large-crossover coefficient is inherited from existing fixed-parameter research, not an independently new numerical constant. The contribution is its uniform crossover and bound. An unindexed or more general published inequality could exist, so historical priority remains subject to independent checking. This is a self-review, not an independent audit.

## References
1. L. P. C. da Cruz and J. Llibre, *Global Centers in a Class of Quintic Polynomial Differential System*, arXiv:2312.05709v1, first public 2023-12-09, https://arxiv.org/html/2312.05709v1.
2. *Strict period decrease and sharp large-amplitude laws for quintic global centers*, public mathematical result, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-strict-period-decrease-and-sharp-large-amplitude-laws-for-quinti--ffe383da977f/RESULT.md .
3. S. Chanda, A. Ghose-Choudhury and P. Guha, *Jacobi-Maupertuis metric of Liénard type equations and Jacobi Last Multiplier*, Electronic Journal of Differential Equations 2018, 120, https://ejde.math.txstate.edu/Volumes/2018/120/chanda.pdf .
4. L.-J. Yang and X.-W. Zeng, *The period function of Liénard systems*, Proceedings of the Royal Society of Edinburgh A 143 (2013), 205–221, doi:10.1017/S0308210511000096.
