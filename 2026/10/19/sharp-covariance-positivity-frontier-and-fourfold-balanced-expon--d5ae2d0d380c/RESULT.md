# Sharp covariance-positivity frontier and fourfold balanced-exponential correction

## Finding

For a constant positive-semidefinite forcing in a stable symmetric differential Lyapunov equation, the first-order matrix exponential-time-differencing (METD1) forcing term need not be symmetric. Symmetrizing it can still destroy covariance positivity at an explicitly determined time step. A square-root-balanced forcing term preserves the positive-semidefinite cone for every step and, for this constant-forcing problem, is globally second-order accurate. Its Frobenius error is no larger than the symmetrized METD1 error at **every finite step**, strictly smaller when the drift and forcing fail to commute, and its leading error constant is exactly one fourth as large.

Precisely, for a real symmetric negative-definite matrix \(L\), a real symmetric \(\Sigma\succeq0\), a real symmetric \(C_0\succeq0\), and \(h>0\), set
\[
E_h=e^{hL},\qquad D_h=\int_0^h e^{2tL}\,dt=h\varphi_1(2hL).
\]
The exact covariance step, its symmetrized METD1 counterpart, and the balanced step are respectively
\[
\begin{aligned}
 C_{j+1}^{\rm exact}&=E_h C_j^{\rm exact}E_h+\int_0^h e^{tL}\Sigma e^{tL}\,dt,\\
 C_{j+1}^{\rm sym}&=E_h C_j^{\rm sym}E_h+\tfrac12(D_h\Sigma+\Sigma D_h),\\
 C_{j+1}^{\rm bal}&=E_h C_j^{\rm bal}E_h+D_h^{1/2}\Sigma D_h^{1/2}.
\end{aligned}
\]
Each starts at \(C_0\). The balanced steps remain positive semidefinite and, for every \(n\ge1\) and \(T=nh>0\),
\[
\|C_n^{\rm bal}-C(T)\|_F\le\|C_n^{\rm sym}-C(T)\|_F,
\]
with strict inequality if and only if \([L,\Sigma]\ne0\). For fixed \(T>0\) as \(h=T/n\to0\),
\[
\begin{aligned}
 C_n^{\rm sym}-C(T)&=\frac{h^2}{6}\,\mathcal K_T+O(h^3),\\
 C_n^{\rm bal}-C(T)&=\frac{h^2}{24}\,\mathcal K_T+O(h^3),\\
 \mathcal K_T&=\int_0^T e^{tL}[L,[L,\Sigma]]e^{tL}\,dt.
\end{aligned}
\]
If \([L,\Sigma]\ne0\), both errors are nonzero for sufficiently small steps and their Frobenius-norm ratio tends to exactly four. If they commute, both discrete schemes coincide with the exact solution at all steps.

For the two-mode benchmark \(L=-\operatorname{diag}(a,b)\), \(0<a<b\), \(C_0=0\), and \(\Sigma=\begin{psmallmatrix}1&\rho\\\rho&1\end{psmallmatrix}\) with \(|\rho|\le1\), define
\[
 d_a(h)=\frac{1-e^{-2ah}}{2a},\qquad
 r_{a,b}(h)=\frac{2\sqrt{d_a(h)d_b(h)}}{d_a(h)+d_b(h)}.
\]
Then the symmetrized METD1 one-step covariance is positive semidefinite **if and only if**
\[
 |\rho|\le r_{a,b}(h).
\]
The threshold \(r_{a,b}(h)\) strictly decreases from one to \(2\sqrt{ab}/(a+b)\) as \(h\) increases from zero to infinity. Consequently, \(|\rho|\le2\sqrt{ab}/(a+b)\) gives positivity for every finite step, \(2\sqrt{ab}/(a+b)<|\rho|<1\) gives one unique sharp crossing step, and \(|\rho|=1\) yields an indefinite symmetric update for every positive step. In contrast, the exact update is positive definite for every step (including rank-one forcing), while the balanced update is always positive semidefinite and retains forcing rank.

## Assumptions and scope

The drift \(L=L^{\mathsf T}\prec0\) and the symmetric forcing \(\Sigma\succeq0\) are fixed in time, the initial covariance \(C_0\succeq0\), and matrix functions and square roots are evaluated exactly. Repeated eigenvalues are allowed. The \(2\times2\) phase diagram assumes precisely two distinct positive damping rates and a normalized covariance forcing; changing the diagonal forcing magnitudes can be reduced to the displayed correlation coefficient by positive diagonal congruence. All norms are Frobenius norms. The order assertion concerns the constant-forcing differential Lyapunov equation only; it is **not** an order claim for general nonlinear matrix equations.

## Proof

### 1. Spectral reduction and exact comparison

Orthogonally diagonalize \(L=U\operatorname{diag}(-a_1,\ldots,-a_d)U^{\mathsf T}\), where all \(a_i>0\), and express \(\Sigma\) in the same basis. The homogeneous part of each recurrence is identical. The exact, symmetrized, and balanced forcing entries are, respectively,
\[
 \Sigma_{ij}\,q_{ij}(h),\qquad
 \Sigma_{ij}\,m_{ij}(h),\qquad
 \Sigma_{ij}\,g_{ij}(h),
\]
where
\[
\begin{aligned}
 q_{ij}(h)&=\int_0^h e^{-(a_i+a_j)t}\,dt,\\
 d_i(h)&=\int_0^h e^{-2a_it}\,dt,\\
 m_{ij}(h)&=\tfrac12(d_i(h)+d_j(h)),\\
 g_{ij}(h)&=\sqrt{d_i(h)d_j(h)}.
\end{aligned}
\]
Cauchy–Schwarz followed by the arithmetic–geometric mean inequality gives
\[
 q_{ij}(h)\le g_{ij}(h)\le m_{ij}(h),
\]
and both inequalities are strict exactly when \(a_i\ne a_j\). Indeed, the functions \(e^{-a_it}\) and \(e^{-a_jt}\) are linearly dependent on \([0,h]\) only if the rates agree.

For \(T=nh\) each error entry multiplies the corresponding forcing-entry difference by the common strictly positive number
\[
 W_{ij}(n,h)=\sum_{j'=0}^{n-1}e^{-(a_i+a_j)j'h}>0.
\]
Consequently,
\[
 |(C_n^{\rm bal}-C(T))_{ij}|
 \le |(C_n^{\rm sym}-C(T))_{ij}|,
\]
strict if \(\Sigma_{ij}\ne0\) and \(a_i\ne a_j\). Squaring and summing entries proves the stated Frobenius dominance. All such strict pairs are absent precisely when \([L,\Sigma]=0\). Since \(D_h\succ0\), the balanced forcing is a positive-semidefinite congruence of \(\Sigma\), preserves its rank, and together with \(E_h C E_h\) preserves the covariance cone. Commuting \(L,\Sigma\) makes \(q_{ij}=g_{ij}=m_{ij}\) on every nonzero forcing entry, giving exactness.

### 2. Leading local and global defects

Taylor expansion at fixed rates yields
\[
 m_{ij}(h)-q_{ij}(h)=\frac{(a_i-a_j)^2h^3}{6}+O(h^4),\qquad
 g_{ij}(h)-q_{ij}(h)=\frac{(a_i-a_j)^2h^3}{24}+O(h^4).
\]
Because \([L,[L,\Sigma]]_{ij}=(a_i-a_j)^2\Sigma_{ij}\), the one-step source defects are \(h^3[L,[L,\Sigma]]/6+O(h^4)\) and \(h^3[L,[L,\Sigma]]/24+O(h^4)\), respectively. Summation of the exact homogeneous propagation weights is a Riemann sum, giving
\[
 h\,W_{ij}(n,h)\longrightarrow\int_0^T e^{-(a_i+a_j)t}\,dt.
\]
In finite dimension this establishes the two global expansions above, with matrix remainder \(O(h^3)\) at fixed \(T\). Since every coefficient integral is strictly positive and the commutator vanishes if and only if the rates agree on the nonzero forcing entries, \(\mathcal K_T\ne0\) whenever \([L,\Sigma]\ne0\). The global error-norm ratio therefore tends to four.

### 3. Complete two-mode positivity frontier

For \(L=-\operatorname{diag}(a,b)\), the symmetrized source is
\[
 S_h=\begin{pmatrix}d_a&\rho(d_a+d_b)/2\\\rho(d_a+d_b)/2&d_b\end{pmatrix},
\]
whose positive diagonal entries reduce positive semidefiniteness to \(\det S_h\ge0\), exactly \(|\rho|\le r_{a,b}(h)\). For \(a<b\), the ratio \(d_a(h)/d_b(h)\) is strictly increasing because
\[
 \frac{d}{dh}\log\frac{d_a(h)}{d_b(h)}
 =\frac{2a}{e^{2ah}-1}-\frac{2b}{e^{2bh}-1}>0.
\]
The inequality follows from strict decrease of \(x/(e^x-1)\) for positive \(x\). As \(r_{a,b}=2\sqrt r/(1+r)\) with \(r=d_a/d_b>1\), the critical correlation decreases strictly from one to \(2\sqrt{ab}/(a+b)\). The intermediate-value theorem supplies the unique crossing and all endpoint cases. For \(|\rho|=1\),
\[
 \det S_h=-\frac{(d_a-d_b)^2}{4}<0.
\]
Meanwhile the exact increment has off-diagonal \(\rho q_{ab}\), and strict Cauchy–Schwarz gives \(q_{ab}^2<d_ad_b\) when \(a\ne b\); hence the exact increment is positive definite even if the forcing is rank one. The balanced increment has determinant \(d_ad_b(1-\rho^2)\ge0\). This finishes the classification.

## Verification

The standalone file `verify.py` (Python 3 standard library, no external dependencies) evaluates the exact scalar integrals, threshold monotonicity and boundary, three covariance determinants, finite-step componentwise errors, asymptotic fourfold error ratio, and multidimensional Gram-forcing positivity. Replay with `python3 verify.py`; the deterministic run passes 18,692 checks and finds the sharp example \(a=1\), \(b=9\), \(\rho=0.8\) at \(h_c\approx0.29180387462622\). These finite checks corroborate but do not replace the inequalities and all-dimension proof.

## Relationship to prior work

Shkeir and Grafke, *Exponential time differencing for matrix-valued dynamical systems* (arXiv:2406.13761, originally public 2024-06-19), derive METD1 with forcing \(h\varphi_1(h(L+R))N\); the displayed scheme is the specialization \(R=L\), \(N=\Sigma\). Their commutator corrections and higher-order methods are acknowledged. The inspected open full-text revision does not give the rank-one PSD obstruction, the sharp two-mode correlation frontier, or the all-step balanced-vs-symmetrized error comparison.

Bertram and Faßbender, *Lyapunov and Sylvester equations: A quadrature framework* (arXiv:1903.05383), already discuss exact positive-semidefinite Gramian integrals and factorized numerical approximations. Behr, Benner and Heiland, *Solution Formulas for Differential Sylvester and Lyapunov Equations* (arXiv:1811.08327), develop operator and spectral solution formulas. Neither general framework is claimed as new. The result here concerns the concrete METD1 approximation and the exact comparative formula for a geometric-mean replacement of its forcing; general Gramian quadrature results by themselves do not state those comparison or threshold constants.

## Limitations

The method is not an accurate surrogate for the exact Lyapunov integral when drifts or forcing vary rapidly, when the drift is nonsymmetric, or for general nonlinear matrix equations without additional analysis. Computing \(D_h^{1/2}\) may be more expensive than forming the original source term, and no runtime advantage is claimed. Balanced forcing matches the exact diagonal in the drift eigenbasis but need not match off-diagonal covariances exactly; its finite-step error is generally positive on an entrywise factor basis, not an order relation between entire error matrices. Existing Gramian methods may achieve higher accuracy or lower cost. A related exact special-case formula could appear in other literature; no assertion of independent publication-priority certification is made.

## References

1. N. Shkeir and T. Grafke, *Exponential time differencing for matrix-valued dynamical systems*, arXiv:2406.13761, first submitted 2024-06-19, https://arxiv.org/abs/2406.13761 ; full text inspected at https://arxiv.org/html/2406.13761v2 .
2. C. Bertram and H. Faßbender, *Lyapunov and Sylvester equations: A quadrature framework*, arXiv:1903.05383, https://arxiv.org/html/1903.05383v1 .
3. M. Behr, P. Benner and J. Heiland, *Solution Formulas for Differential Sylvester and Lyapunov Equations*, arXiv:1811.08327, https://arxiv.org/abs/1811.08327 .
