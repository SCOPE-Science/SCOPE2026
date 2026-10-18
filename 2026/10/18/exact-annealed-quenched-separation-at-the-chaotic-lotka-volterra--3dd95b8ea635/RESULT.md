# Exact annealed–quenched separation at the chaotic Lotka–Volterra boundary

## Finding
Consider the Sharkovskiĭ Lotka–Volterra map
\[
F_c(x,y)=\bigl(x(4-x-y),\;cxy\bigr),\qquad c>0,
\]
whose original form has \(c=1\). On the invariant line \(y=0\), initialize the prey coordinate with the invariant density \(d\mu(x)=dx/[\pi\sqrt{x(4-x)}]\), \(0<x<4\). Let \(x_{j+1}=x_j(4-x_j)\) and let
\[
M_{n,c}=c^n\prod_{j=0}^{n-1}x_j,\qquad n\ge1,
\]
be the **transverse linearized multiplier** of \(F_c^n\) at \((x_0,0)\). All statements below are with respect to the initial-state distribution \(\mu\), and the almost-sure statements exclude its measure-zero singular/preperiodic exceptions.

For every integer \(n\ge1\), the exact ordinary and second moments are
\[
\mathbb E M_{n,c}=(2c)^n,\qquad
\mathbb E M_{n,c}^{2}=c^{2n}u_n,
\]
where \(u_0=1\), \(u_1=6\) and \(u_{n+2}=2u_{n+1}+16u_n\). Equivalently,
\[
u_n=\frac{5+\sqrt{17}}{2\sqrt{17}}(1+\sqrt{17})^n
+\frac{\sqrt{17}-5}{2\sqrt{17}}(1-\sqrt{17})^n.
\]
In particular, at the **zero transverse Lyapunov exponent** \(c=1\), one has \(M_{n,1}^{1/n}\to1\) almost surely, despite \(\mathbb E M_{n,1}=2^n\); moreover
\[
\frac{\operatorname{Var}(M_{n,1})}{(\mathbb E M_{n,1})^2}
\sim \frac{5+\sqrt{17}}{2\sqrt{17}}
\left(\frac{1+\sqrt{17}}4\right)^n.
\]
Thus relative mean-square amplification is **exponentially intermittent** while the almost-sure exponential transverse growth rate is zero.

For the logarithmic transverse amplification \(Z_n=\log M_{n,1}\), all finite-horizon covariances are explicit:
\[
\mathbb E Z_n=0,\qquad
\operatorname{Var}(Z_n)=\frac{\pi^2}{3}\bigl(3n-4+2^{2-n}\bigr).
\]
Consequently \(Z_n/\sqrt n\Rightarrow N(0,\pi^2)\). In the sharp near-neutral window \(c_n=\exp(\kappa/\sqrt n)\), for every fixed real \(\kappa\),
\[
\lim_{n\to\infty}\mu\{x_0:M_{n,c_n}>1\}=\Phi(\kappa/\pi),
\]
where \(\Phi\) is the standard normal distribution function. The angle-doubling CLT used here is a known general theorem; the explicit first/second moment spectrum, exact finite-horizon covariance coefficient, and their joint interpretation for this transverse cocycle are the specific calculation in this finding.

## Assumptions and scope
The initial prey state is distributed according to the invariant arcsine law, **not** uniformly in \(x\). The orbit lies on \(y=0\); \(M_{n,c}\) is the derivative of the predator coordinate of \(F_c^n\) with respect to its initial predator coordinate, evaluated at this boundary orbit. A comparison of multipliers is not an assertion about nonlinear predator invasion from finite, nonzero density. For \(c\ne1\), no global forward-invariance claim about the original triangle is made. The parameter \(c>0\) is a transverse local-growth perturbation of the cited original map.

## Proof
**Boundary reduction.** At \(y=0\), the Jacobian is upper triangular with transverse diagonal entry \(cx\), so the transverse derivative after \(n\) steps is the claimed product. The substitution \(x=4\sin^2(\pi\theta)\) pushes uniform measure on \([0,1]\) to \(\mu\), and the logistic boundary dynamics is semiconjugate to \(D\theta=2\theta\pmod1\). Write \(X(\theta)=4\sin^2(\pi\theta)=2-2\cos(2\pi\theta)\).

**Exact moments via a finite weighted transfer.** The Lebesgue transfer operator of \(D\) is
\[
(Pf)(t)=\tfrac12\bigl(f(t/2)+f((t+1)/2)\bigr).
\]
It satisfies \(PX=2\). Repeated conditional integration therefore yields \(\mathbb E\prod_{j<n}X(D^j\theta)=2^n\). For second moments use \(R f=P(X^2f)\) and \(C(\theta)=\cos(2\pi\theta)\). Direct trigonometric multiplication gives \(R1=6+2C\) and \(RC=-4-4C\). Hence \(R\) preserves \(\operatorname{span}\{1,C\}\), with coefficient matrix
\[
A=\begin{pmatrix}6&-4\\2&-4\end{pmatrix}.
\]
The constant coefficient of \(R^n1\), equal to \(\mathbb E\prod_{j<n}X(D^j\theta)^2\), is \(u_n\). Since \(\det A=-16\) and \(\operatorname{tr} A=2\), Cayley–Hamilton gives the exact recurrence and the two roots \(1\pm\sqrt{17}\). The initial coefficients are \(u_0=1,u_1=6\). The leading root \(1+\sqrt{17}>4\) establishes the positive exponential relative-variance rate.

**Exact logarithmic fluctuations.** Let \(\phi(\theta)=\log X(\theta)\). In \(L^2([0,1])\),
\[
\phi(\theta)=-2\sum_{k\ge1}\frac{\cos(2\pi k\theta)}{k}.
\]
Fourier orthogonality implies \(\int\phi=0\) and, for every integer \(m\ge0\),
\[
\int_0^1\phi(\theta)\phi(D^m\theta)\,d\theta
=\frac{\pi^2}{3\,2^m}.
\]
Summing the \(n\) diagonal and \(2(n-m)\) off-diagonal covariance terms gives the finite-horizon variance formula. Ergodicity of \(D\) and \(\phi\in L^1\) give \(Z_n/n\to0\) almost surely. For the CLT, either apply the established angle-doubling theorem of Kac in the form recalled by Bhar, Mukherjee and Patil (Fourier decay \(O(k^{-1})\), positive limiting variance \(\pi^2\)), or observe directly that \(d=2\phi-\phi\circ D=2\log|\tan(\pi\theta)|\) obeys \(Pd=0\), \(\int d^2=\pi^2\), and \(Z_n=\sum_{j<n}d\circ D^j+\phi\circ D^n-\phi\). The first sum is a stationary ergodic reverse martingale-difference sum; the last two terms are \(O_{L^2}(1)\), so the reverse martingale CLT yields the same limit.

**Near-neutral crossover.** Since \(\log M_{n,c_n}=Z_n+\kappa\sqrt n\), the CLT and continuity of the normal distribution give \(\Pr\{M_{n,c_n}>1\}\to\Phi(\kappa/\pi)\). No conclusion about nonlinear persistence follows without further analysis.

## Verification
The bundled standalone `check.py` performs exact integer Laurent-polynomial Fourier calculations for the first nine horizons: it verifies both moment sequences and the covariance-sum identity in rational coefficients. Those calculations are finite cross-checks, not substitutes for the preceding infinite-horizon algebra and limit-theorem proof. A separate grid quadrature check at up to eight steps agreed with the exact moment values \((2,4,8,16,\ldots)\) and \((6,28,152,752,\ldots)\).

## Relationship to prior work
Gasull and Mañosa (2018, Section 4) introduce this Lotka–Volterra map into a study of exact interior period-five and period-six orbit counts. They note the logistic boundary but do not analyze its transverse multiplier moment spectrum. Kac's classical doubling-map CLT, recalled and strengthened in Bhar–Mukherjee–Patil (2024), already implies the **Gaussian limit once its variance is known**; that generic CLT is **not** claimed as new. Löbbe (2014) proves a general lacunary CLT for bounded finite-variation observables; the logarithm here is unbounded. The present model-specific two-dimensional weighted-transfer calculation and its exact variance/moment contrast are not given by these results. An earlier treatment of the same weighted product under a different cocycle/thermodynamic-formalism name remains possible.

## Limitations
The asymptotic measure statements apply to the invariant arcsine ensemble on the invariant predator-free boundary, not to arbitrary ensembles or positive two-dimensional orbits. The unperturbed map \(c=1\) has neutral average **linearized** transverse exponent, but the result does not decide its nonlinear attraction or repulsion. The second-moment formula does not provide a full large-deviations principle; no such principle is asserted. Literature priority is assessed against inspected material but not independently certified.

## References
1. A. Gasull and V. Mañosa, *Periodic orbits of discrete and continuous dynamical systems via Poincaré–Miranda theorem*, arXiv:1809.06208v1 (17 September 2018), Section 4. https://arxiv.org/abs/1809.06208
2. S. Bhar, R. Mukherjee and P. Patil, *Kac's Central Limit Theorem by Stein's Method*, arXiv:2405.06881v2 (9 October 2024), Theorem 2.1 and Section 2. https://arxiv.org/abs/2405.06881
3. T. Löbbe, *Limit Theorems for Multivariate Lacunary Systems*, arXiv:1408.2202v1 (10 August 2014), Theorem 1.1. https://arxiv.org/abs/1408.2202
