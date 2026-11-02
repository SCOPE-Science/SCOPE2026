# An isolated scalar positivity resonance for blended SSPRK3–Crank–Nicolson stepping

## Finding

The 2026 five-stage AdHImEx time-stepping tableau has a unique blend at which its negative-real-axis amplification has a *double* positive zero. At this blend the scalar amplification is never negative, and the longest contiguous interval on which it is also at most one is more than twice the SSPRK3 interval.

Let \(\alpha\) be the unique positive root of
\[
p(s)=1-s+\frac{s^2}{2}-\frac{s^3}{6}=0,
\qquad \alpha=1.5960716379833215231\ldots.
\]
Define \(\theta_*=2/(\alpha+2)=0.5561624465083239653\ldots\). The sharp positivity-and-contractivity radius for the real negative scalar test is
\[
L(\theta)=\begin{cases}
\min\{2/\theta,\alpha/(1-\theta)\},&0\le\theta\le1,\ \theta\ne\theta_*,\\
x_*,&\theta=\theta_*,
\end{cases}
\]
where \(2/0=\alpha/0=+\infty\). Here \(x_*=7.4504823663779645326\ldots\) is uniquely determined by the equation \(R_{\theta_*}(x_*)=1\) with \(x_*>\alpha+2\). The next-best limiting radius approaching the exceptional blend is only \(\alpha+2=3.5960716379833215231\ldots\); the exceptional point is a strict, isolated global maximizer of the radius.

## Assumptions and scope

Use exactly the five-stage tableau printed as equation (6) in the cited 2026 paper, with *spatially constant* \(\theta\in[0,1]\), exact stage solves, and the scalar linear ODE \(y'=-\lambda y\) with \(\lambda>0\) and timestep \(h>0\). Write \(x=\lambda h\). The radius \(L(\theta)\) is the supremum of all \(\ell\ge0\) such that \(0\le y_{n+1}/y_n\le1\) for every test value \(x\in[0,\ell]\), assuming a positive initial state. This is a test-equation property of the time integrator; the spatial fifth-order advection discretization, adaptive choice of \(\theta\), and optional flux-corrected transport are not part of the theorem.

## Proof

**1. Exact stage elimination.** Let \(z=-x\), \(t=\theta\), and normalize the initial value to one. From the tableau, the first four stages are
\[
Y_1=1,\quad Y_2=1+zt/2,\quad
Y_3=1+z[t/2+(1-t)Y_2],\quad
Y_4=1+z[t/2+(1-t)(Y_2+Y_3)/4].
\]
The final stage equals the completed step because the final tableau row is its weight row. Thus
\[
Y_5=\frac{1+z[t/2+(1-t)(Y_2+Y_3)/6+2(1-t)Y_4/3]}{1-zt/2}.
\]
Substitution and collection of powers give the **exact identity**
\[
R_t(x)=Y_5=\frac{2-tx}{2+tx}\,p((1-t)x),
\qquad p(s)=1-s+s^2/2-s^3/6.
\]
This identity, rather than a comparison of separately implemented methods, fixes the scheme under study.

**2. Zeros and signs.** For \(s\ge0\), \(p'(s)=-[(s-1)^2+1]/2<0\), \(p(0)=1\), and \(p(s)\to-\infty\). Hence \(p\) has exactly one positive zero \(\alpha\). The Crank–Nicolson factor has one zero at \(2/t\) when \(t>0\), while the explicit factor has one at \(\alpha/(1-t)\) when \(t<1\). The zeros coincide exactly when \(t=\theta_*=2/(\alpha+2)\). For every other parameter, the first zero is simple and the product is strictly negative immediately after it. Up to the first zero, both factors lie in \([0,1]\) and are nonincreasing. This proves the nonexceptional formula including the endpoint parameters.

**3. The resonant extension.** At \(\theta_*\), the two zeros coincide at \(x_0=\alpha+2\), yielding a double zero: both factors are positive below, negative above, and neither derivative vanishes at its zero. Therefore the product is nonnegative for all positive steps. On \([0,x_0]\) it decreases strictly from one to zero. Beyond \(x_0\), the absolute value of each factor increases strictly: for the rational factor, \((\theta_*x-2)/(\theta_*x+2)\) increases from zero to one; for the polynomial factor, \(-p((1-\theta_*)x)\) increases from zero without bound. Their positive product thus increases continuously from zero to infinity, crossing one exactly once. Denote that crossing by \(x_*\); it is strictly larger than \(x_0\).

For a purely algebraic specification, putting \(y=\alpha x/(\alpha+2)\), the nonzero crossing corresponds to the unique root \(y>\alpha\) of
\[
y^3-(\alpha+3)y^2+3(\alpha+2)y-6(\alpha+2)=0,
\qquad x_*=(\alpha+2)y/\alpha.
\]
It follows that \(L(\theta_*)=x_*\). Since for all other parameters \(L(\theta)\le\alpha+2<x_*\), this is the unique global maximum. Taking nonexceptional parameters to \(\theta_*\) yields the stated strict jump in the radius.

## Verification

A standalone Python standard-library checker independently implements all five tableau stages with exact rational arithmetic and compares the result against the factorization at 1,000 rational parameter/step pairs. It also evaluates ten nonresonant sign intervals and brackets the roots with 75-digit decimal arithmetic; its output is `CHECKS_PASS 1010`. This supports the algebra and stated decimal digits; the proof of global uniqueness and all-parameter inequalities is analytical and does not rely on finite sampling. Execute `python3 checker.py` after extracting the embedded file.

## Relationship to prior work

The source introduces the blended five-stage tableau and investigates von Neumann stability for its particular fifth-order spatial advection operator, using numerical wave-number and Courant-number samples. Classical SSPRK3 and Crank–Nicolson factors are pre-existing, and an earlier analysis of this same tableau had already observed their multiplicative factorization when studying Fourier \(\ell^2\)-stability. The present claim is different: it classifies sign-preserving scalar damping over an *entire real negative axis*, finds the unique coincident-zero resonance, and proves the exceptional maximal first-step contractivity interval. Neither the sampled spatial stability conditions nor the factorization alone state this optimization result.

## Limitations

Scalar endpoint nonnegativity is weaker than nonnegativity of a coupled semidiscrete transport update, an M-matrix property, a strong-stability-preserving coefficient, or full PDE solution monotonicity. The zero-coincidence blend is not robust to perturbations of \(\theta\): for every nonexceptional nearby blend, a narrow negative-amplification interval returns. For \(x>x_*\), the resonant factor exceeds one and grows without bound; therefore the result does not claim unconditional contractivity or A-stability. Broader historical priority within composition/SSP positivity literature remains a residual risk.

## References

1. A. J. te Winkel, H. Weller, C. Kühnlein, and J. Kent, *AdHImEx: Adaptively High-Order Implicit-Explicit Transport for Large Time Steps*, arXiv:2610.08166v1, first public 2026-10-06. https://arxiv.org/html/2610.08166v1
2. S. Gottlieb, C.-W. Shu, and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112. https://doi.org/10.1137/S003614450036757X
3. J. Crank and P. Nicolson, *A Practical Method for Numerical Evaluation of Solutions of Partial Differential Equations of the Heat-Conduction Type*, Proc. Cambridge Philos. Soc. 43 (1947), 50–67.
4. C. Macdonald, S. Gottlieb, and S. Ruuth, *A Numerical Study of Diagonally Split Runge–Kutta Methods for PDEs with Discontinuities*, Journal of Scientific Computing 36 (2008), 89–112. https://doi.org/10.1007/s10915-007-9180-6
