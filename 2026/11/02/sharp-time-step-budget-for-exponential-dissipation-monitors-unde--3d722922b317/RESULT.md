# Sharp time-step budget for exponential dissipation monitors under an adjacent-ratio cap

## Finding
Let \(E(t)=E_0e^{-\lambda t}\) for \(0\le t\le T\), where \(E_0,\lambda,T>0\). Write \(D=E(0)/E(T)=e^{\lambda T}>1\). Fix a monitor exponent \(0<p\le1\), an integer \(N\ge2\), and the **unique exactly equidistributed grid** \(0=t_0<t_1<\cdots<t_N=T\) for the strictly positive monitor \(g_p(t)=|E'(t)|^p\):
\[
\int_{t_j}^{t_{j+1}}g_p(t)\,dt=\frac1N\int_0^Tg_p(t)\,dt\qquad(0\le j<N).
\]
Set \(h_j=t_{j+1}-t_j\) and \(\rho_j=h_j/h_{j-1}\) for \(1\le j<N\). Put
\[
H(x)=\log\left(1+\frac1x\right)\quad(x>0),\qquad
u=\frac{N}{D^p-1}.
\]
Then the ratios are **strictly increasing**:
\[
1<\rho_1<\rho_2<\cdots<\rho_{N-1}=\frac{H(\nu)}{H(\nu+1)}\qquad(N\ge3),
\]
with the corresponding single-ratio equality for \(N=2\). For every fixed ratio cap \(R>1\), there is a unique \(u_R>0\) such that
\[
\frac{H(u_R)}{H(u_R+1)}=R.
\]
The grid satisfies **every strict neighboring-step cap** \(\rho_j<R\) exactly when
\[
N>u_R(D^p-1).
\]
Consequently the **sharp minimum admissible grid size**, subject to \(N\ge2\), is
\[
\boxed{N_{\min}(p,D,R)=\max\left\{2,\ \lfloor u_R(D^p-1)\rfloor+1\right\}.}
\]
At the illustrative classical ratio cap \(R=1+\sqrt2\), numerical root isolation gives
\[
u_R=0.35882316342658315849372482206858\ldots.
\]
Thus, for fixed \(R>1\) as \(D\to\infty\), the exact monitor \(p=1\) requires \(N_{\min}\sim u_RD\) steps, while \(p=1/2\) requires \(N_{\min}\sim u_R\sqrt D\) steps. For \(D=100\) and \(R=1+\sqrt2\), the exact respective minima are \(36\) and \(4\); for \(D=10^6\) they are \(358823\) and \(359\). These are requirements for **exact monitor equidistribution with a stipulated ratio cap**, not an intrinsic stability limit of BDF2.

## Assumptions and scope
A scalar gradient-flow example realizing the energy is \(\dot u=-\lambda u/2\), \(E(u)=u^2\), with nonzero initial state. Only the continuous energy curve, its exact unregularized power monitor, and exact integral equidistribution are used. The result assumes \(p>0\), \(E_0>0\), \(\lambda>0\), \(T>0\), \(N\ge2\), and \(R>1\). No special BDF2 discretization is needed to form this grid. A sufficient *method-specific* ratio restriction such as \(R=1+\sqrt2\) motivates the cap, not the theorem's proof. The endpoint time is finite, so the monitor remains strictly positive throughout.

## Proof
**1. Explicit equidistribution.** Since \(g_p(t)=(\lambda E_0)^p e^{-\lambda pt}\), dividing its cumulative integral at \(t_j\) by the total gives
\[
\frac{1-e^{-\lambda pt_j}}{1-e^{-\lambda pT}}=\frac jN,
\qquad e^{-\lambda pt_j}=1-\frac jN(1-D^{-p}).
\]
Inverting this strictly increasing cumulative function establishes existence and uniqueness of every node. Write \(a=D^p-1\) and \(\nu=N/a\). Since
\[
1-\frac jN(1-D^{-p})=\frac{\nu+N-j}{\nu+N},
\]
subtraction of consecutive logarithms yields the **exact steps**
\[
h_j=\frac1{\lambda p}\log\frac{\nu+N-j}{\nu+N-j-1}
=\frac1{\lambda p}H(\nu+N-j-1),\qquad 0\le j<N.
\]
Consequently
\[
\rho_j=\frac{H(\nu+N-j-1)}{H(\nu+N-j)}\quad(1\le j<N).
\]

**2. Strict ordering of ratios.** For every \(x>0\),
\[
H(x)=\int_0^\infty e^{-xs}\frac{1-e^{-s}}s\,ds.
\]
The integral is positive and admits differentiation of any fixed order. With \(L(x)=\log H(x)\), the standard strict Cauchy–Schwarz inequality (equivalently, nonzero variance under the probability density proportional to \(e^{-xs}(1-e^{-s})/s\)) gives \(L''(x)>0\). Thus \(L'(x)<L'(x+1)\), so \(L(x)-L(x+1)\) is strictly decreasing in \(x\), and so is \(F(x):=H(x)/H(x+1)\). As \(j\) increases, the argument \(\nu+N-j-1\) decreases, hence \(\rho_j\) strictly increases. Also \(H\) strictly decreases, so every \(\rho_j>1\). Its maximum occurs at \(j=N-1\), with value \(F(\nu)\).

**3. Unique sharp threshold.** Continuity of \(F\) is immediate. As \(x\downarrow0\), \(H(x)\to\infty\) and \(H(x+1)\to\log2\), so \(F(x)\to\infty\). As \(x\to\infty\), \(H(x)\sim x^{-1}\) and hence \(F(x)\to1\). Strict monotonicity therefore gives exactly one \(u_R>0\) with \(F(u_R)=R\) for every \(R>1\). Because \(F\) decreases strictly,
\[
\max_{1\le j<N}\rho_j<R\quad\Longleftrightarrow\quad
F\left(\frac{N}{D^p-1}\right)<R
\quad\Longleftrightarrow\quad\frac{N}{D^p-1}>u_R.
\]
The smallest admissible integer \(N\ge2\) is \(\max\{2,\lfloor u_R(D^p-1)\rfloor+1\}\). When \(u_R(D^p-1)\) itself is an integer, the strictness of the cap excludes equality, explaining the floor-plus-one rather than a ceiling convention.

**4. Asymptotics.** For fixed \(p,R>0\), \(N_{\min}=u_R D^p+O(1)\), because the integer rounding and subtraction of one have bounded effect. Substituting \(p=1\) or \(p=1/2\) proves the stated contrasting exponents. No discretization-error statement is inferred from this asymptotic budget.

## Verification
The standalone `verification.py` uses arbitrary-precision arithmetic and a deterministic seed. It separately generates nodes by cumulative monitor inversion and by the derived step formula, compares all nodes and strict ratio ordering, checks strict threshold decisions against an independently located bisection root for random exponents and horizons, and evaluates the limiting budget examples. It completed **1,296 high-precision comparisons**. Numerical tests are corroboration, not the proof of the universally quantified threshold; the analytic strict log-convexity and endpoint limits above provide that proof.

Reproduce with `python verification.py` after installing the Python package `mpmath`. The reported root is numerical, not claimed as an exact elementary constant.

## Relationship to prior work
Shergill and Williams (2026), arXiv:2610.30454v1, establish energy-rate monitor equidistribution for adaptive SSAV–vBDF2, identify the monitors \(|\dot E|\) and \(\sqrt{|\dot E|}\), and use a ratio restriction \(\rho<1+\sqrt2\) in their convergence criterion. Those ingredients are prior, not new claims. The finding above instead **completely solves the minimal-step compatibility problem for exact power-monitor equidistribution on exponential relaxation**, locating the last interval as the unique worst ratio and giving an exact integer cutoff and its two cost exponents; these conclusions are not stated in the source's sections on equidistribution, algorithm constraints, or convergence.

Liao and Zhang (2019), arXiv:1912.11182, analyze adaptive BDF2 under step-ratio assumptions. Li and Liao (2022), arXiv:2201.00527, establish BDF2 stability on arbitrary time grids in a different stability framework. The latter rules out treating \(1+\sqrt2\) as a universal necessity. The present theorem is deliberately a sharp **compatibility criterion for a chosen bound**, valid for any \(R>1\). The positive-Laplace-transform argument is a classical technique; its specific use here is part of the derivation, not a claim of inventing log-convexity.

## Limitations
The result does not analyze the regularized, clamped, switched, rejected, or numerically estimated monitor used by a full adaptive solver, nor any discrete energy error or nonlinear PDE stability. A full algorithm may enforce the cap by changing the ideal mesh and need not use this many steps. Stronger stability theories can allow larger ratios; no contradiction is implied. Only a single exponentially relaxing energy mode is modeled, and claims for general multiscale dissipation curves require new work. Priority risk remains that existing general equidistributed-mesh results could imply the cutoff without stating it in this notation; the compared primary sources did not yield such a covering assertion.

## References
1. S. Shergill and JF Williams, *Energy-rate equidistribution for adaptive SSAV–BDF2 integration of gradient flows* (first public October 21, 2026), arXiv:2610.30454v1, https://arxiv.org/html/2610.30454v1 .
2. H.-L. Liao and Z. Zhang, *Analysis of adaptive BDF2 scheme for diffusion equations* (2019), arXiv:1912.11182, https://arxiv.org/abs/1912.11182 .
3. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods* (2022), arXiv:2201.00527, https://arxiv.org/abs/2201.00527 .
