# Sharp positivity and mass consistency for three-node function-space SBP differentiation

## Finding

On the fixed nodes \((-1,0,1)\), the three-dimensional exponential space \(\mathcal F_\lambda=\operatorname{span}\{1,\cosh(\lambda x),\sinh(\lambda x)\}\), with \(\lambda>0\), has a **unique** exact diagonal-norm summation-by-parts (SBP) differentiator. Its norm is positive but never integrates constants exactly, and its spectral condition number is precisely \(2(1+\cosh\lambda)\).

For the equally sized trigonometric space \(\mathcal T_\omega=\operatorname{span}\{1,\cos(\omega x),\sin(\omega x)\}\), with \(\omega>0\), an exact **positive diagonal-norm** SBP differentiator exists precisely when
\[
\omega\bmod 2\pi\in(0,2\pi/3)\ \cup\ (\pi,4\pi/3).
\]
In each permitted band it is unique; all omitted frequencies are genuinely infeasible for this fixed three-node discretization. The second positive band is a reentrant window separated from the first by a forbidden range. Within the first period \(0<\omega<2\pi\), its norm integrates constants exactly at one and only one frequency, \(\omega_*\in(\pi,4\pi/3)\), characterized by
\[
\sin\omega_*(2+\cos\omega_*)=\omega_*(1+2\cos\omega_*),
\qquad\omega_*\approx4.02870132202536.
\]
The first positive band always assigns total quadrature mass strictly greater than the interval length \(2\).

## Assumptions and scope

All quantities are real and all identities hold in exact arithmetic. The nodal ordering is \((-1,0,1)\), and the boundary matrix is \(B=\operatorname{diag}(-1,0,1)\). A diagonal-norm SBP pair consists of a real matrix \(D\in\mathbb R^{3\times3}\) and a **positive diagonal** matrix \(H\) satisfying \(D f(\mathbf x)=f'(\mathbf x)\) for every function in the designated three-dimensional space, and \(HD+D^{\mathsf T}H=B\). Here \(f(\mathbf x)\) is the nodal-value column. Constant-exactness of the norm is the **additional** property \(\mathbf1^{\mathsf T}H\mathbf1=\int_{-1}^1 1\,dx=2\); it is not included in the basic SBP definition.

The exponential parameter is \(\lambda>0\), and the trigonometric parameter is \(\omega>0\) without upper bound. Frequencies with \(\sin\omega=0\) are treated as non-unisolvent rather than assigned spurious limiting operators. The normalization classification in the trigonometric case is specifically restricted to the first period \(0<\omega<2\pi\).

## Proof

**Common forced differentiation matrix.** Introduce \((k,c,s)=(\lambda,\cosh\lambda,\sinh\lambda)\) for the exponential space or \((k,c,s)=(\omega,\cos\omega,\sin\omega)\) for the trigonometric space. For \(s\ne0\) and \(c\ne1\), the nodal basis matrix and the unique exact differentiation matrix are
\[
V=\begin{pmatrix}1&c&-s\\1&1&0\\1&c&s\end{pmatrix},\quad
\det V=-2s(c-1),\qquad
D=\frac{k}{2s}\begin{pmatrix}
-(2c+1)&2(c+1)&-1\\-1&0&1\\1&-2(c+1)&2c+1
\end{pmatrix}.
\]
Indeed, multiplication gives \(DV=V'\), using \(c^2-s^2=1\) in the exponential case and \(c^2+s^2=1\) in the trigonometric case. Invertibility of \(V\) makes \(D=V'V^{-1}\) mandatory, not a free design parameter.

**Forced diagonal norm and the singular obstruction.** The first and last diagonal equations in \(HD+D^{\mathsf T}H=B\) force \(H_{11}=H_{33}=s/[k(1+2c)]\). The off-diagonal equations involving the middle node then force \(H_{22}=2(1+c)H_{11}\). Conversely direct multiplication confirms the entire SBP identity for
\[
H=\frac{s}{k(1+2c)}\operatorname{diag}\bigl(1,2(1+c),1\bigr).
\]
If \(1+2c=0\), the corner entries of \(D\) are zero, contradicting \(2H_{11}D_{11}=-1\); thus no finite diagonal norm exists. For \(\lambda>0\) neither obstruction occurs and every diagonal entry of \(H\) is strictly positive. In the trigonometric case, when \(\sin\omega=0\), the nodal vector of \(\sin(\omega x)\) vanishes identically but its nodal derivative does not; hence **no** exact \(D\) exists. At all remaining frequencies, \(1+\cos\omega>0\) and positive definiteness of \(H\) is equivalent to \(\sin\omega/(1+2\cos\omega)>0\). The sign chart in each full period is exactly the two open bands stated above. This proves sharp existence, nonexistence and uniqueness without searching over an ansatz.

**Exponential conditioning and missing constant mass.** Because \(2(1+\cosh\lambda)>1\), the spectral condition number of the diagonal norm is exactly \(2(1+\cosh\lambda)\). Its mass is
\[
M_{\exp}(\lambda)=\mathbf1^{\mathsf T}H\mathbf1
=\frac{2\sinh\lambda\,(2+\cosh\lambda)}{\lambda(1+2\cosh\lambda)}.
\]
Set \(F(t)=\sinh t\,(2+\cosh t)-t(1+2\cosh t)\). Then \(F(0)=0\) and \(F'(t)=2\sinh t\,(\sinh t-t)>0\) for every \(t>0\). Thus \(M_{\exp}(\lambda)>2\) for every \(\lambda>0\); since \(H\) is unique, **no** constant-exact positive diagonal norm exists at these three fixed nodes for nonzero exponential tension. Moreover \(M_{\exp}(\lambda)\sim e^\lambda/(2\lambda)\) and \(\kappa_2(H)\sim e^\lambda\) as \(\lambda\to\infty\). The polynomial limit \(\lambda\downarrow0\) has mass \(2\), but the limiting basis must be suitably rescaled and \(\lambda=0\) is excluded from the claim.

**Trigonometric normalization in the first period.** For each admissible \(\omega\), the total mass is
\[
M_{\mathrm{trig}}(\omega)
=\frac{2\sin\omega\,(2+\cos\omega)}{\omega(1+2\cos\omega)}.
\]
For \(0<\omega<2\pi/3\), the difference from \(2\) has the positive sign of \(G(\omega)=\sin\omega(2+\cos\omega)-\omega(1+2\cos\omega)\). Indeed \(G(0)=0\) and \(G'(\omega)=2\sin\omega(\omega-\sin\omega)>0\). Therefore there is no normalized SBP pair in the first positive band. In the second positive band write \(\omega=\pi+t\), \(0<t<\pi/3\). Then
\[
\frac{M_{\mathrm{trig}}(\pi+t)}2
=\frac{\sin t\,(2-\cos t)}{(\pi+t)(2\cos t-1)}.
\]
Its logarithmic derivative is \(\cot t+\sin t/(2-\cos t)+2\sin t/(2\cos t-1)-1/(\pi+t)\), which is strictly positive because \(\cot t\ge1/\sqrt3>1/\pi\) and the other trigonometric summands are positive. The mass increases continuously from \(0\) to \(+\infty\); it equals \(2\) exactly once, at the displayed root \(\omega_*\). Every other frequency in the first period either has no positive-norm SBP operator or fails constant normalization.

## Verification

The included companion algebraic checker `verify_fsbp.py` verifies the complete matrix identity symbolically, verifies exact differentiation modulo both hyperbolic and trigonometric identities, and tests positive-frequency bands and masses across finite grids; it prints `VERIFICATION_OK 2862 checks`. The analytical sign and monotonicity arguments above, rather than finite sampling, prove the quantified statements. The root decimal is informational; its defining equation and uniqueness are exact.

## Relationship to prior work

Glaubitz, Nordström and Öffner (2022/2023), *Summation-by-Parts Operators for General Function Spaces*, introduce the positive-norm FSBP framework and its exact-quadrature existence criterion. Their Section 6.1 uses a trigonometric basis with **four** nodes on a fixed-frequency interval; Section 6.2 uses a different exponential basis \(\operatorname{span}\{1,x,e^x\}\) with **five** nodes. Their general criterion supplies the underlying definition, but their displayed constructions do not classify the **three fixed nodes, variable frequency/tension**, or the resulting sharp bands, conditioning and mass failures.

Glaubitz, Nordström and Öffner (2024), *An Optimization-Based Construction Procedure for Function Space Based Summation-by-Parts Operators on Arbitrary Grids*, explicitly add constant-integral normalization as a design requirement (Section 2.3). Their Section 4 illustrates optimization on other function spaces and larger node sets; they do not derive this three-node impossibility and reentrant-frequency classification. Glaubitz and coauthors (2023), *The Second Derivative*, study a different derivative order and illustrate first-derivative trigonometric construction with four nodes. Hale, Harley, Nchupang and Nordström (2026), *Optimal Nodes*, optimize **free node locations** using generalized Gauss–Lobatto theory and analyze different examples. Their movable-node existence theorems do not imply fixed-grid feasibility, nor give the exact trigonometric threshold bands or forced constant masses.

## Limitations

This is a first-derivative, three-node, diagonal-norm, real-exact-arithmetic statement on a **fixed** symmetric grid. A nondiagonal norm, additional nodes, an adjustable midpoint, weakly enforced consistency, or a different function space can avoid the fixed-grid obstructions. No accuracy, full PDE convergence, time-step stability, or application-optimality theorem is asserted. The normalization uniqueness statement is restricted to the first frequency period, not all higher alias bands. The general FSBP framework and matrix-algebra reductions are established prior art; publication priority for the explicit classifications remains subject to specialized literature not identified here.

## References

1. J. Glaubitz, J. Nordström and P. Öffner, *Summation-by-Parts Operators for General Function Spaces*, arXiv:2203.05479, first public 2022-03-10. https://arxiv.org/abs/2203.05479
2. J. Glaubitz, J. Nordström and P. Öffner, *An Optimization-Based Construction Procedure for Function Space Based Summation-by-Parts Operators on Arbitrary Grids*, arXiv:2405.08770, first public 2024-05-14. https://arxiv.org/abs/2405.08770
3. J. Glaubitz, S.-C. Klein, J. Nordström and P. Öffner, *Summation-by-Parts Operators for General Function Spaces: The Second Derivative*, arXiv:2306.16314. https://arxiv.org/abs/2306.16314
4. N. Hale, C. Harley, P. Nchupang and J. Nordström, *Summation-by-Parts Operators for General Function Spaces: Optimal Nodes*, arXiv:2604.23306. https://arxiv.org/abs/2604.23306
