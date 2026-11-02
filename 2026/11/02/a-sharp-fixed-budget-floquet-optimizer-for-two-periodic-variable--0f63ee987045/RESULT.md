# A sharp fixed-budget Floquet optimizer for two-periodic variable-step BDF2

## Finding
For the scalar decay test equation \(y'(t)=-\lambda y(t)\), \(\lambda>0\), run standard interpolation-based variable-step BDF2 on a grid repeating two strictly positive step lengths \(h_1,h_2\). Fix the dimensionless time budget per two-step period \(s=\lambda(h_1+h_2)>0\), and let \(r=h_2/h_1>0\). The spectral radius \(\rho(s,r)\) of the two-step amplification matrix is strictly below one for every \(s,r>0\), and its global infimum over \(r>0\) has the following complete classification:
\[
\inf_{r>0}\rho(s,r)=
\begin{cases}
\dfrac{5-s+4\sqrt{1-s}}{(s+3)^2},&0<s\le1,\\[2mm]
\dfrac{|s-2|}{s^2+s+2},&s>1.
\end{cases}
\]
For \(0<s\le1\), equality holds uniquely at \(r=1\). For \(s>1\) with \(s\ne2\), equality holds precisely at the two reciprocal positive ratios satisfying
\[
r+r^{-1}=q_*(s):=\frac{2(s^2+4s-4)}{(s-2)^2}>2.
\]
At these ratios the two Floquet multipliers coalesce into the same real number (positive for \(1<s<2\), negative for \(s>2\)). At the isolated budget \(s=2\), the infimum is zero and is never attained by positive finite step lengths. Instead, \(\rho(2,r)\sim\sqrt r/2\) as \(r\downarrow0\) (and symmetrically \(\sim1/(2\sqrt r)\) as \(r\to\infty\)). Thus equal steps cease to be rate-optimal at the sharp boundary \(s=1\), and the singular \(s=2\) budget has arbitrarily rapid asymptotic two-period damping under sufficiently imbalanced steps.

## Assumptions and scope
The numerical recurrence, with \(h_n>0\), \(r_n=h_n/h_{n-1}\), and \(n\ge2\), is
\[
[1+2r_n+(1+r_n)\lambda h_n]y_n-(1+r_n)^2y_{n-1}+r_n^2y_{n-2}=0.
\]
Here \(h_{2j-1}=h_1\), \(h_{2j}=h_2\), repeated indefinitely after two arbitrary starting values. The objective being minimized is the spectral radius of the monodromy on \((y_n,y_{n-1})^{\mathsf T}\), not its one-period operator norm, transient gain, truncation error, or accuracy at finite physical time. Strictly positive finite steps are required; the zero-infimum statement is a limiting statement only. The fixed \(s\) means that each compared schedule advances the same physical time per pair using two implicit BDF2 solves.

## Proof
**1. Transfer matrix and symmetric invariants.** Write \(T(r,z)\) for the map from \((y_{n-1},y_{n-2})^{\mathsf T}\) to \((y_n,y_{n-1})^{\mathsf T}\), with ratio \(r\) and instantaneous dimensionless step \(z=\lambda h_n\):
\[
T(r,z)=\begin{pmatrix}
\dfrac{(1+r)^2}{1+2r+(1+r)z}&-\dfrac{r^2}{1+2r+(1+r)z}\\
1&0
\end{pmatrix}.
\]
Set \(q=r+r^{-1}\ge2\). For the two alternating steps use \(T(r,sr/(1+r))\) and \(T(r^{-1},s/(1+r))\). Direct multiplication shows that the two-step matrix \(M\) (in either starting phase) has
\[
\operatorname{tr}M=\frac{(2-s)q+6}{B},\qquad
\det M=\frac1B,\qquad
B=(s+2)q+(s+2)^2+1.
\]
The matrix's characteristic polynomial is \(\xi^2-(N/B)\xi+1/B\), with \(N=(2-s)q+6\). Inverting the starting phase exchanges the two invertible factors; the resulting products are similar and have the same eigenvalues.

**2. Unconditional scalar strict spectral stability.** The real quadratic Schur inequalities reduce to
\[
B-N+1=s(2q+s+4)>0,\quad
B+N+1=4q+s^2+4s+12>0,\quad
B-1>0.
\]
They imply both eigenvalues lie strictly inside the unit circle for all \(s>0\), \(q\ge2\). These are statements for each fixed finite ratio; no ratio-uniform transient-norm bound is claimed.

**3. Discriminant and complex-root region.** The numerator of the quadratic discriminant factors exactly:
\[
N^2-4B=(q+2)\{(s-2)^2q-2(s^2+4s-4)\}.
\]
For \(0<s\le1\) it is nonnegative for every \(q\ge2\) (strict for \(q>2\)). For \(s>1\), \(s\ne2\), it is negative on \(2\le q<q_*(s)\), zero at \(q_*\), and positive beyond. For \(s=2\) it is \(-16(q+2)<0\) for every finite \(q\). Whenever it is negative, the conjugate multipliers have common modulus \(B^{-1/2}\), a strictly decreasing function of \(q\).

**4. Monotonicity beyond real-root onset.** In a region of distinct real roots, let \(R\) be the larger modulus. The trace \(N\) has the sign of \(2-s\) in this region (and is positive throughout when \(s<2\)). Hence \(R\) is the larger positive root of
\[
B R^2-(d q+e)R+1=0,
\]
where \(a=s+2\), \(d=|2-s|>0\), and \(e=6\) for \(s<2\) or \(e=-6\) for \(s>2\). Put \(\ell=d/a\). Evaluation at \(\ell\) gives the positive, \(q\)-independent quantity
\[
B\ell^2-(d q+e)\ell+1=
\begin{cases}
\dfrac{s^4}{(s+2)^2},&s<2,\\[2mm]
\dfrac{[(s+2)^2+1](s-2)^2+6(s+2)(s-2)+(s+2)^2}{(s+2)^2},&s>2.
\end{cases}
\]
For \(s>1\), \(s\ne2\), at \(q=q_*\) the double multiplier has modulus \(d/(s^2+s+2)<\ell\), so continuity and the strictly positive evaluation show \(R(q)<\ell\) for all \(q\ge q_*\). For \(0<s\le1\), at \(q=2\) the vertex of the real-root polynomial lies below \(\ell\) because
\[
\ell-\frac{5-s}{(s+3)^2}=
\frac{8-3s^2-s^3}{(s+2)(s+3)^2}>0;
\]
combined with the positive evaluation, this shows \(R(2)<\ell\), and continuity gives \(R(q)<\ell\) for every \(q\ge2\). Implicit differentiation at simple real roots yields
\[
\frac{dR}{dq}=\frac{R(d-aR)}{2BR-(dq+e)}>0.
\]
Thus the spectral radius rises strictly throughout each real-root regime after its onset, while in the nonreal-root regime it falls strictly. Consequently the unique minimizing \(q\) is \(2\) for \(s\le1\) and \(q_*(s)\) for \(s>1\), \(s\ne2\).

**5. Minimum values and resonance.** For \(s\le1\), substitution of \(q=2\) gives \(B=(s+3)^2\), \(N=2(5-s)\), and \(\sqrt{N^2-4B}=8\sqrt{1-s}\), yielding the first case in the displayed infimum. At \(q_*\),
\[
B=\frac{(s^2+s+2)^2}{(s-2)^2},
\]
so its double-root modulus is \(|s-2|/(s^2+s+2)\). For \(s=2\), \(B=4q+17\) and \(\rho(2,r)=1/\sqrt{4(r+r^{-1})+17}\). This is positive for finite \(r\) and tends to zero as \(r\to0\) or \(r\to\infty\), with the asserted square-root constants. These arguments exhaust all \(s>0\) and \(r>0\).

## Verification
Run `python verify.py` after installing the packages in `requirements.txt`. The checker reconstructs both transfer factors, symbolically verifies the trace, determinant, discriminant, Schur identities, and optimal boundary, then checks 135 directly computed spectral radii against the closed formula. It also tests finite grids of budgets and ratios and verifies exact coalescence/Jordan-block identities at the example below. These tests do not replace the all-parameter proof above.

At \(s=4\), the optimal ratios are \(r=7\pm4\sqrt3\). The sharp optimal spectral radius is \(1/11\), compared with \(1/7\) at equal steps. The optimal monodromy has a nontrivial Jordan block with double multiplier \(-1/11\), so the rate advantage does not assert a better finite-horizon operator norm. At \(s=2\), equal steps give \(\rho=1/5\), but extreme ratios make \(\rho\) arbitrarily small.

## Relationship to prior work
Li and Liao, arXiv:2201.00527 (first posted 2022-01-03), establish mesh-robust stability bounds for general variable-step BDF2 using discrete orthogonal convolution kernels. Wang, Mao, and Wang, arXiv:2003.03534 (first posted 2020-03-07), establish step-ratio-dependent PDE stability and error estimates. Söderlind, Fekete, and Faragó (2018) analyze zero-stability under smooth grid deformations. Their methods and stability notions differ from minimizing the exact Floquet spectral radius at fixed two-step physical time. The present result refines the scalar test-equation picture by giving the sharp rate-optimal alternating ratio, the transition at \(s=1\), and the unattained resonance at \(s=2\). It does not claim that existing general stability results are false or that their standard BDF2 recurrence is new.

## Limitations
Only the scalar negative-real-axis test equation, a fixed two-periodic grid, exact arithmetic, and the spectral radius objective are covered. A very imbalanced pair may be numerically undesirable because of transient amplification and large local truncation errors, even when its asymptotic Floquet radius is small. The optimization does not establish finite-time error optimality, convergence on arbitrary nonperiodic grids, ratio-uniform transient bounds, or optimality for a spectrum of distinct decay rates. A repeated optimal root generally corresponds to a defective monodromy, leading to polynomial prefactors in powers despite the stated geometric asymptotic rate.

## References
1. Z. Li and H.-L. Liao, *Stability of variable-step BDF2 and BDF3 methods*, arXiv:2201.00527 (2022), https://arxiv.org/abs/2201.00527, subsequently SIAM J. Numer. Anal. 60 (2022), 2253–2272.
2. W. Wang, M. Mao and Z. Wang, *Stability and error estimates for the variable step-size BDF2 method for linear and semilinear parabolic equations*, arXiv:2003.03534 (2020), https://arxiv.org/abs/2003.03534.
3. G. Söderlind, I. Fekete and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numerical Mathematics 58 (2018), 1125–1143, https://doi.org/10.1007/s10543-018-0716-y.
