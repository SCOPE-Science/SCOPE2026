# A unique minimax mass correction for the periodic box-kernel nonlocal Laplacian

## Finding

For the mean-zero periodic one-dimensional nonlocal diffusion operator with constant compactly supported kernel, the inverse-Laplacian-plus-mass preconditioner has a **unique condition-number-optimal positive mass coefficient** across all interaction horizons. It is not the mass-normalized coefficient.

Set
\[
a(s)=1-\frac{\sin s}{s},\qquad Q_b(s)=a(s)\left(b+\frac1{s^2}\right),\qquad s>0,\quad b>0.
\]
Extend continuously by \(Q_b(0)=1/6\) and \(Q_b(\infty)=b\). Let
\[
\mathcal K(b)=\frac{\max_{0\le s\le\infty}Q_b(s)}{\min_{0\le s\le\infty}Q_b(s)}.
\]
The unique global minimizer over \(b>0\) is
\[
\boxed{b_*=\frac{t_*}{6(t_*-\sin t_*)}-\frac1{t_*^2}=0.174777992381291\ldots},
\]
where \(t_*\in(5\pi/2,3\pi)\) is the unique zero on that interval of
\[
N(t)=t^3(t\cos t-\sin t)+12(t-\sin t)^2.
\]
Numerically, \(t_*=7.874519450912597\ldots\). At this optimum,
\[
\min Q_{b_*}=\frac16,\qquad
\max Q_{b_*}=\max_{0\le s\le2\pi}Q_{b_*}(s),
\quad
\boxed{\mathcal K(b_*)=6\max_{0\le s\le2\pi}Q_{b_*}(s)
=1.700200564562\ldots}.
\]
The kernel-mass coefficient \(b=1/2\), in the same normalization, obeys the rigorous lower bound
\[
\mathcal K(1/2)\ge6Q_{1/2}(4)=4.013552105416\ldots,
\]
so the optimally tuned robust condition number is improved by a factor exceeding \(2.36\) over that baseline. The minima and maxima are exact continuum spectral extrema; decimals are reproducibility diagnostics.

## Assumptions and scope

Work on the \(2\pi\)-periodic one-dimensional torus, restricted to mean-zero \(L^2\) functions. For any interaction horizon \(\delta>0\), let
\[
\bigl(\mathcal A_\delta f\bigr)(x)
=\delta^{-2}\int_{-1}^{1}\bigl(f(x)-f(x+\delta z)\bigr)\,dz.
\]
This corresponds to the nonnegative box kernel \(\rho(z)=\tfrac12\mathbf1_{[-1,1]}(z)\) in the convention \(\mathcal A_\delta f=2\delta^{-2}\int\rho(z)(f(x)-f(x+\delta z))\,dz\). Define the positive Fourier-diagonal preconditioner
\[
\mathcal B_{\delta,b}=(-\partial_x^2)^{-1}+b\delta^2 I,\qquad b>0,
\]
where the inverse local Laplacian is taken on the mean-zero subspace. The product \(\mathcal B_{\delta,b}\mathcal A_\delta\) has, on frequency \(k\ne0\), eigenvalue \(2Q_b(\delta|k|)\). Its spectral condition number is the supremum of the positive eigenvalues divided by their infimum. Optimize the worst-case value over **all** \(\delta>0\), with no spatial discretization. The scalar \(2\) cancels from all condition numbers.

## Proof

**1. The uniform-horizon problem is a one-variable minimax problem.** For the Fourier vector \(e^{ikx}\), direct integration gives the symbol
\[
\widehat{\mathcal A_\delta}(k)=\frac2{\delta^2}\left(1-\frac{\sin(\delta |k|)}{\delta|k|}\right).
\]
The preconditioner symbol is \(|k|^{-2}+b\delta^2\). All eigenvalues are therefore \(2Q_b(\delta|k|)>0\). Their infimum is positive for fixed \(b>0\), since \(Q_b\) is positive and continuous on the compactified half-line \([0,\infty]\). The spectrum for any fixed horizon is contained in its full range, so its condition number is at most \(\mathcal K(b)\). Conversely, for any two positive frequencies \(s_1,s_2\), taking \(\delta_j\downarrow0\) and integers \(k_{i,j}\) with \(\delta_j k_{i,j}\to s_i\) makes the spectral ratio tend to \(Q_b(s_1)/Q_b(s_2)\). The endpoints \(0\) and \(\infty\) are also attainable as limits by selecting \(k=1\) with \(\delta\downarrow0\), or \(k\to\infty\). Thus the sharp supremum over horizons equals \(\mathcal K(b)\).

**2. Locate the largest coefficient needed to keep every mode above the low-frequency limit.** Define
\[
F(s)=\frac{1}{6a(s)}-\frac1{s^2}
=\frac{s}{6(s-\sin s)}-\frac1{s^2}.
\]
Then \(Q_b(s)\ge1/6\) if and only if \(b\ge F(s)\). We show that \(\sup_{s>0}F(s)\) is achieved uniquely at \(t_*\in(5\pi/2,3\pi)\).

First, on \(0<s\le\pi\), the alternating Taylor estimate \(\sin s/s\le1-s^2/6+s^4/120\) and the elementary identity
\[
\frac6{6+y}-\left(1-\frac y6+\frac{y^2}{120}\right)
=\frac{y^2(14-y)}{120(6+y)}\ge0\quad (0\le y\le\pi^2)
\]
imply \(a(s)\ge s^2/(6+s^2)\), hence \(F(s)\le1/6\). Whenever \(\sin s\le0\), in particular on \([\pi,2\pi]\) and \([3\pi,4\pi]\), the sharper \(F(s)<1/6\) holds. On \(s\ge4\pi\), using \(\sin s\le1\) gives
\[
F(s)\le U(s):=\frac{s}{6(s-1)}-\frac1{s^2}.
\]
For \(s\ge4\pi>12\), the derivative \(U'(s)=-1/[6(s-1)^2]+2/s^3\) is negative. Direct evaluation yields
\[
F(5\pi/2)-U(4\pi)
=\frac{200\pi^3-780\pi^2+507\pi-78}
{400\pi^2(4\pi-1)(5\pi-2)}>0.
\]
For a fully elementary sign check, the cubic numerator is increasing for arguments at least \(3\) and is already positive at \(157/50<\pi\). Also \(F(5\pi/2)>1/6\), since \((5\pi/2)^2>6(5\pi/2-1)\). Thus every global maximum is inside \((2\pi,3\pi)\).

Differentiation yields the exact derivative
\[
F'(s)=\frac{N(s)}{6s^3(s-\sin s)^2},\qquad
N(s)=s^3(s\cos s-\sin s)+12(s-\sin s)^2.
\]
For \(2\pi\le s\le5\pi/2\), \(\cos s,\sin s\ge0\), so
\[
N(s)\ge-s^3+12(s-1)^2>0.
\]
The last inequality follows because \(s^3/(s-1)^2\) is increasing for \(s>3\) and its value at \(s=8\) is \(512/49<12\), whereas \(5\pi/2<8\). On \([5\pi/2,3\pi]\) set \(u=-\cos s\ge0\) and \(v=\sin s\ge0\); then \(u+v\ge1\). Differentiating \(N\) and using \(s-\sin s\le s\) gives
\[
N'(s)\le24s-s(3s^2-24)u-s^2(s^2+3)v
\le s(48-3s^2)<0.
\]
Indeed \(s^2(s^2+3)>s(3s^2-24)>0\) here. We have \(N(5\pi/2)>0\), while \(N(3\pi)=(3\pi)^2[12-(3\pi)^2]<0\). Exactly one zero \(t_*\) exists. Finally \(1/6<b_*<1/5\); the upper bound uses \(s\ge2\pi>6\) and \(\sin s\le1\) on the maximizing lobe.

**3. All maximizers for coefficients no larger than \(b_*\) lie in the first oscillation band.** For \(s\ge2\pi\),
\[
Q_b(s)\le\left(1+\frac1{2\pi}\right)
\left(b+\frac1{4\pi^2}\right)
<Q_b(\pi)=b+\frac1{\pi^2}
\qquad (0<b\le b_*<1/5).
\]
The strict difference equals \([6\pi-1-4b\pi^2]/(8\pi^3)>0\). Thus every global maximizer lies in \([0,2\pi)\). For any \(0<b<b_*\), a minimizing point must lie **beyond \(2\pi\)**: by the definition of \(b_*\), \(Q_{b_*}(t_*)=1/6\) and \(Q_{b_*}(s)\ge1/6\) for all \(s\). For every \(s<t_*\), the ratio \(Q_b(s)/Q_b(t_*)\) is strictly decreasing as a function of \(b\): for positive finite \(s\) its log-derivative is
\[
\frac1{b+s^{-2}}-\frac1{b+t_*^{-2}}<0,
\]
and at \(s=0\) the numerator is constant. Hence at \(b<b_*\), \(Q_b(s)>Q_b(t_*)\) for \(0\le s\le2\pi\). When \(b=b_*\), the minimum \(1/6\) is attained at \(s=0\) and \(s=t_*\); the latter suffices for the next comparison.

**4. Strict minimax optimality.** Fix \(0<b_1<b_2\le b_*\). Choose a maximizing \(s_2<2\pi\) for \(Q_{b_2}\) and a minimizing \(t_2>2\pi\) for it (for \(b_2=b_*\), choose \(t_2=t_*\)). If necessary \(t_2=\infty\) and \(Q_b(\infty)=b\). The ratio \(Q_b(s_2)/Q_b(t_2)\) is strictly decreasing in \(b\), since \(s_2<t_2\) and the same log-derivative comparison applies, including both endpoints. Therefore
\[
\mathcal K(b_1)\ge\frac{Q_{b_1}(s_2)}{Q_{b_1}(t_2)}
>\frac{Q_{b_2}(s_2)}{Q_{b_2}(t_2)}=\mathcal K(b_2).
\]
For \(b\ge b_*\), \(\min Q_b=1/6\), since every mode obeys \(Q_b(s)\ge1/6\) and the zero-frequency limit equals it. The maximum \(\max Q_b\) is **strictly increasing** for \(b\ge b_*\): any maximizing point has \(s>0\) (because \(Q_b(\pi)>1/6\)), and at that point \(Q_b\) increases strictly with \(b\). Hence \(\mathcal K\) increases strictly for \(b>b_*\). Combining both sides proves uniqueness. The compact expression for the optimum, the numerical values, and the \(b=1/2\) comparison follow directly.

## Verification

Run `python3 check.py` using only the Python standard library. It bisects the unique root of \(N\), checks the derivative identity against centered differences, isolates stationary points of \(Q_{b_*}\) on \([0,2\pi]\), reproduces the displayed constants, checks comparison coefficients by finite spectral samples, and tests several truncated Fourier spectra. The symbolic inequalities and strict monotonicity arguments above, rather than sampling, certify the claims for all positive frequencies, coefficients, and horizons. The computed peak is near \(s=3.752639388705\) and its value near \(0.283366760760\).

## Relationship to prior work

Lu, Nie, Zhang, and Zhang (2026) introduce the robust inverse-local-Poisson-plus-mass preconditioner for volume-constrained nonlocal finite element systems. Their mass normalization \(\beta=1/(2\mu_\rho)\), their continuous Fourier comparison, and their uniform spectral bounds motivate this exact scalar optimization. For the unit-mass box kernel, \(\mu_\rho=1\) and hence \(\beta=1/2\). Their principal results establish uniform robustness, not an exact minimax coefficient or the sharp worst-horizon condition number for this periodic box-kernel specialization. The current theorem does **not** claim the preconditioner family, Fourier symbol approach, or mesh-independent bounded conditioning as new. Other studied \(\tau\)- and Toeplitz preconditioners address distinct discrete matrix families and do not furnish the displayed scalar minimax result through the material inspected. A mathematically equivalent result in unindexed literature cannot be excluded.

## Limitations

The claim is for exact continuum Fourier multipliers on a mean-zero one-dimensional periodic domain, an even constant box kernel, all positive horizons, and the specified positive additive one-parameter preconditioners. It is **not** a result for Dirichlet volume constraints, finite element matrices, multigrid approximations, higher dimensions, other kernels, finite-precision computations, or total work including preconditioner application. The robust condition-number minimizer need not minimize iteration counts at one particular horizon. No independent external mathematical audit is asserted.

## References

1. J. Lu, Y. Nie, H. Zhang, and P. Zhang, *A mesh- and horizon-robust preconditioner for finite element discretizations of volume-constrained nonlocal diffusion problems*, arXiv:2609.24143 (first posted September 21, 2026), https://arxiv.org/abs/2609.24143.
2. J. Zhang, T. Sun, H. Sun, and J. Zhang, *Spectral analysis of τ-preconditioners for two-level Toeplitz systems with applications in nonlocal diffusion models*, Journal of Scientific Computing 106 (2026), article 21, DOI:10.1007/s10915-025-03150-2.
