# Ten-vertex small-step positivity barrier and oscillatory lattice kernel for two-stage Radau IIA

## Finding

Let \(C_n\) be the undirected cycle with \(n\ge3\) vertices and nearest-neighbor heat generator \(Q_n=S_n+S_n^{-1}-2I=-L(C_n)\), where \(S_n\) is the cyclic permutation matrix. The end-step map of the two-stage, order-three Radau IIA Runge–Kutta method is
\[
R(z)=\frac{1+z/3}{1-2z/3+z^2/6}=\frac{6+2z}{6-4z+z^2},\qquad T_n(h)=R(hQ_n).
\]
Here a numerical step preserves nonnegative vectors exactly when its real matrix \(T_n(h)\) is entrywise nonnegative.

**Theorem.** The following assertions hold in exact arithmetic.

1. For each fixed \(3\le n\le9\), there exists \(\varepsilon_n>0\) such that \(T_n(h)\) is *strictly entrywise positive* for every \(0<h<\varepsilon_n\).
2. For each fixed \(n\ge10\), there exists \(\varepsilon_n>0\) such that \([T_n(h)]_{0,5}<0\) for every \(0<h<\varepsilon_n\). In particular, ten vertices is the smallest cyclic heat grid on which arbitrarily small positive Radau IIA steps fail positivity.
3. On the infinite one-dimensional nearest-neighbor heat lattice \(\mathbb Z\), the convolution kernel of \(R(-hL_{\mathbb Z})\) has infinitely many strictly negative entries for **every** fixed \(h>0\). Consequently, for each fixed \(h>0\) there exist arbitrarily large finite cycles \(C_n\) on which \(T_n(h)\) has a strictly negative entry: no fixed positive step size preserves nonnegativity simultaneously for all cycle sizes.
4. For each fixed finite \(n\ge3\), \(T_n(h)\to\mathbf1\mathbf1^{\mathsf T}/n\) entrywise as \(h\to\infty\). Hence \(T_n(h)\) is strictly entrywise positive for all sufficiently large \(h\). On every \(n\ge10\), the small-step positivity failure is thus eventually reversed at large step sizes.

For every \(n\) and \(h\ge0\), the matrix \(T_n(h)\) is real symmetric, circulant, well-defined and has every row sum equal to one. The theorem concerns entrywise positivity rather than spectral stability, convergence order, or positivity of the Runge–Kutta internal stages.

## Assumptions and scope

One uses the unit-rate, symmetric nearest-neighbor cycle diffusion \(\dot u=Q_nu\) on \(\mathbb R^n\), \(n\ge3\), with periodic indices modulo \(n\), and the standard two-stage Radau IIA Butcher tableau
\[
A=\begin{pmatrix}5/12&-1/12\\3/4&1/4\end{pmatrix},\qquad b=\begin{pmatrix}3/4\\1/4\end{pmatrix}.
\]
The dimensionless step parameter \(h\) includes the unit edge rate. With diffusion edge rate \(\kappa>0\), substitute \(\kappa h\) throughout. For the infinite lattice, \((L_{\mathbb Z}u)_j=2u_j-u_{j-1}-u_{j+1}\) acts on absolutely summable vectors; the rational map is a bounded convolution operator. No mesh-dependent PDE time scaling is assumed.

## Proof

**1. A sign change in the stability-function coefficients.** Write the Maclaurin series \(R(z)=\sum_{m\ge0}c_mz^m\), valid near zero. Multiplication by the denominator gives
\[
c_0=1,\quad c_1=1,\quad c_m=\frac23c_{m-1}-\frac16c_{m-2}\quad(m\ge2),
\]
and in particular
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)
=\left(1,1,\frac12,\frac16,\frac1{36},-\frac1{108},-\frac7{648}\right).
\]
For distinct vertices at graph distance \(d\), all matrix coefficients \((Q_n^m)_{ij}\) vanish for \(m<d\), whereas \((Q_n^d)_{ij}>0\), because precisely the walks of \(d\) genuine off-diagonal transitions contribute, with no negative diagonal factors. Consequently,
\[
[T_n(h)]_{ij}=c_d(Q_n^d)_{ij}h^d+O_n(h^{d+1})\quad(h\downarrow0).
\]
Every pair on a cycle of size at most nine has graph distance at most four. The five coefficients \(c_0,\ldots,c_4\) are positive (for diagonal entries use \(1+O(h)\)), hence every entry is positive for all sufficiently small \(h>0\). Because each finite matrix has finitely many entries, the neighborhoods may be intersected to obtain a common \(\varepsilon_n\). Conversely, on every \(n\ge10\), vertices zero and five have distance exactly five, and \(c_5<0\). More explicitly,
\[
[T_n(h)]_{0,5}=
\begin{cases}
-\dfrac1{54}h^5+O(h^6),&n=10,\\
-\dfrac1{108}h^5+O_n(h^6),&n>10.
\end{cases}
\]
For \(n=10\) there are two shortest paths; for \(n>10\) there is exactly one. This proves the sharp ten-vertex small-step barrier.

**2. Explicit infinite-lattice Green kernel.** Fix \(h>0\) and set
\[
\alpha=\frac h3\left(1+\frac{i}{\sqrt2}\right),
\qquad A=\frac12-i\sqrt2.
\]
The scalar rational identity
\[
R(-hx)=\frac{A}{1+\alpha x}+\frac{\overline A}{1+\overline\alpha x}
\]
holds identically in \(x\). For \(\operatorname{Re}\alpha>0\), define the principal square root with positive real part and
\[
q=\frac{1+2\alpha-\sqrt{1+4\alpha}}{2\alpha}
=\frac{2\alpha}{1+2\alpha+\sqrt{1+4\alpha}},\qquad
C=\frac{A}{\sqrt{1+4\alpha}}.
\]
The nearest-neighbor resolvent equation
\[
(1+2\alpha)g_m-\alpha(g_{m-1}+g_{m+1})=\mathbf1_{m=0}
\]
uniquely has the summable solution \(g_m=q^{|m|}/\sqrt{1+4\alpha}\). The decaying characteristic root satisfies \(0<|q|<1\): for real \(\lambda\ge0\), \(1+\alpha\lambda\ne0\), so no characteristic root lies on the unit circle, and the branch decaying at \(\alpha\to0\) is the unique root inside the unit disk. Partial fractions therefore give the exact *real* convolution kernel
\[
\boxed{\quad k_m(h)=2\operatorname{Re}\bigl(Cq^{|m|}\bigr),\quad m\in\mathbb Z.\quad}
\]
Here \(q\ne0\) and \(q\notin\mathbb R\): otherwise \(\alpha=q/(1-q)^2\) would be real, contradicting \(\operatorname{Im}\alpha>0\). Also \(C\ne0\). Write \(q=\rho e^{i\theta}\), \(C=|C|e^{i\phi}\), where \(0<\rho<1\) and \(\theta\not\equiv0,\pi\pmod {2\pi}\). Hence
\[
k_m(h)=2|C|\rho^m\cos(m\theta+\phi),\qquad m\ge0.
\]
If \(\theta/(2\pi)\) is irrational, the angles are dense modulo \(2\pi\), so the cosine is strictly negative for infinitely many \(m\). If it is rational, the orbit has period at least three; its cosine values sum to zero, and at least one value is strictly negative (they cannot all be zero for three or more distinct equally spaced angles). Periodicity then yields infinitely many negative values. This proves the infinite-lattice assertion for **all** \(h>0\), not just sampled steps.

**3. Transfer of a negative coefficient to large finite cycles.** Because \(|k_m(h)|\le2|C|\rho^{|m|}\), the infinite sequence is absolutely summable. Its periodization
\[
k_j^{(n)}(h)=\sum_{\ell\in\mathbb Z}k_{j+\ell n}(h),\qquad 0\le j<n,
\]
solves the cyclic rational resolvent equation and equals \([T_n(h)]_{0,j}\). Choose any positive integer \(m\) with \(k_m(h)<0\). Keeping \(m\) fixed and letting \(n\to\infty\), the tail \(\sum_{\ell\ne0}k_{m+\ell n}(h)\) tends to zero exponentially. Thus \([T_n(h)]_{0,m}<0\) for every sufficiently large \(n\), proving the fixed-step, uniform-in-size obstruction.

**4. Eventual finite-grid positivity.** Each \(Q_n\) is real symmetric with one zero eigenvalue (the constant eigenvector) and all other eigenvalues strictly negative. The rational multiplier obeys \(R(0)=1\) and \(R(-x)\to0\) as \(x\to\infty\), while its denominator has no zeros on the negative real axis. Spectral decomposition yields
\[
\lim_{h\to\infty}T_n(h)=\frac1n\mathbf1\mathbf1^{\mathsf T}.
\]
Every limit entry is strictly positive, so for each fixed finite \(n\) all entries are positive beyond a finite threshold. Also \(T_n(h)\mathbf1=\mathbf1\) since \(Q_n\mathbf1=0\). This completes the proof.

## Verification

The accompanying independent-of-symbolic-algebra checker `verify.py` uses Python standard-library exact rational matrix inversion. It evaluates the stated rational matrix on \(C_n\) for \(3\le n\le14\) at \(h=1/10000\) and \(h=10^6\), checks all row sums, symmetry, circulant invariance, strict positive entries at small \(h\) through nine vertices, a negative offset-five entry for ten through fourteen vertices, and strict positivity at the large sampled timestep for all twelve sizes. The run evaluated 2,020 matrix entries exactly and passed. It additionally checks the Taylor coefficient recurrence and numerically samples the explicitly derived complex-root kernel at five positive timesteps, confirming negative coefficients at distances five, five, eight, sixteen and forty-seven. Numerical sampling of infinitely many distances or timesteps is not claimed: the universal sign result is proved by the rotation argument above.

Reproduce with `python verify.py` (Python 3.9+ standard library). All floating-point calculations in the checker are diagnostic only; rational matrices and their signs use `fractions.Fraction`.

## Relationship to prior work

Horváth's 1998 positivity framework and 2004-online/2005 paper analyze Runge–Kutta positivity and sharp universal step-size restrictions. The latter explicitly reports the two-stage Radau IIA method with a zero universal all-data positivity threshold for Dirichlet heat semi-discretizations (Table 1, p. 351) and proves general results using absolute monotonicity. Those results do not classify finite **periodic** nearest-neighbor cycle grids, identify ten as the exact first failing grid size, or derive the complex-conjugate-resolvent oscillation forcing negative entries at arbitrarily large distances for every positive step.

The published eight-state Padé–Gauss Markov example uses a different, order-four stability function and a directed pure-birth generator. Published backward-Euler-filtered Crank–Nicolson lattice positivity concerns a distinct rational map whose convolution kernel is positive. The negative fifth Taylor coefficient alone does not imply the all-step oscillatory kernel or the finite-cycle size barrier for symmetric nearest-neighbor diffusion. These distinctions are mathematical comparisons, not claims of exhaustive historical priority.

## Limitations

The assertion is for the **two-stage, third-order** Radau IIA end-step map, standard one-dimensional **symmetric** nearest-neighbor diffusion, exact arithmetic, and periodic finite grids or the full lattice. It does not provide complete positivity intervals for each finite \(n\), quantify the eventual positivity threshold, analyze intermediate-stage values, or extend to arbitrary weighted graphs, Dirichlet boundaries, nonlinear dynamics, or nonnormal generators. The infinite-lattice kernel has negative entries at arbitrarily large distances, which may be exponentially small; their existence is a sign/monotonicity statement, not an accuracy or practical significance estimate. Historical equivalence outside the inspected primary literature remains an originality risk; independent audit has not been performed.

## References

1. Z. Horváth, “Positivity of Runge–Kutta and diagonally split Runge–Kutta methods,” *Applied Numerical Mathematics* **28** (1998), 309–326. DOI: 10.1016/S0168-9274(98)00050-6.
2. Z. Horváth, “On the positivity step size threshold of Runge–Kutta methods,” *Applied Numerical Mathematics* **53** (2005), 341–356; first available online **2004-10-27**. DOI: 10.1016/j.apnum.2004.08.026.
3. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, “Essentially negative news about positive systems,” *Linear Algebra and its Applications* **436** (2012), 3425–3442. DOI: 10.1016/j.laa.2011.12.021.
4. “Eight-state barrier for Markov positivity of the [2/2] Padé map,” public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.
5. “Unconditional lattice positivity from backward-Euler-filtered Crank–Nicolson,” public mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-backward-euler-filtered-cn-lattice-positivity--1f6f56bd0eac.
