# A sharp anti-CFL positivity horizon for four-node Fourier Strang splitting

## Finding

For the canonical four-point, real Fourier-pseudospectral spatial discretization of periodic Allen–Cahn reaction–diffusion and the exact heat–reaction–heat Strang map, preservation of the entire nonnegative unit cube for **every** reaction strength is equivalent to a *lower* bound on the heat half-step, not an upper CFL bound. Write \(t>0\) for the dimensionless diffusion half-step and \(\rho\geq0\) for the reaction duration. There exists a unique \(q_*\in(1/2,3/5)\) satisfying \(q_*+q_*^2+q_*^3=1\), and set \(\theta=-\log q_*=0.609377863436006\ldots\). The exact theorem is

\[
\forall\rho\geq0\;\forall u\in[0,1]^4:\quad S_{t,\rho}(u)\in[0,1]^4
\quad\Longleftrightarrow\quad t\geq\theta.
\]

By contrast, for the purely linear heat map, \(S_{t,0}=H_{2t}\) preserves nonnegativity for all data exactly when \(t\geq\theta/2\). Thus \(\theta/2\leq t<\theta\) is an exact interval in which heat alone preserves positivity but a sufficiently strong pointwise cubic reaction destroys it. For \(0<t<\theta/2\), every fixed reaction strength admits an arbitrarily small nonnegative input whose image has a negative component. On four nodes this yields an exact three-regime classification and a sharp nonlinear factor-of-two separation between the half-step and full-heat positivity thresholds.

## Assumptions and scope

Use grid points \(x_j=2\pi j/4\), \(j=0,1,2,3\), and the standard Fourier pseudospectral Laplacian with Fourier symbols \((0,-1,-4,-1)\). It is the real circulant matrix

\[
L=\operatorname{circ}(-3/2,\,1,\,-1/2,\,1).
\]

Let \(H_t=\exp(tL)\) for \(t>0\). Solve the scalar nonlinear subproblem \(\dot z=\beta(z-z^3)\) exactly for time \(\Delta>0\), with \(\rho=\beta\Delta\geq0\). Its componentwise flow is

\[
R_\rho(z)=\frac{z}{\sqrt{e^{-2\rho}+(1-e^{-2\rho})z^2}}.
\]

For diffusivity \(\nu>0\), the heat half-step parameter is \(t=\nu\Delta/2\). The precise Strang map is \(S_{t,\rho}=H_t\circ R_\rho\circ H_t\), where \(R_\rho\) acts on each coordinate separately. The requirement is simultaneous preservation of \([0,1]^4\) for *all* \(\rho\geq0\); it is not a statement about one fixed reaction strength or a continuous function between collocation nodes. The same sufficiency preserves the whole nonnegative cone because \(R_\rho(z)\geq0\) whenever \(z\geq0\), although the upper bound of one requires cube inputs.

## Proof

**1. Fourier heat weights.** Set \(q=e^{-t}\in(0,1)\). Inverting the four-point discrete Fourier transform gives the circulant kernel

\[
H_t=\operatorname{circ}(a,b,c,b),\quad
 a=\frac{1+2q+q^4}{4},\quad
 b=\frac{1-q^4}{4},\quad
 c=\frac{1-2q+q^4}{4}.
\]

The row sum is \(a+2b+c=1\); \(a,b>0\), and

\[
4c=(1-q)(1-q-q^2-q^3).
\]

The function \(q\mapsto q+q^2+q^3\) increases strictly from zero to three, and hence has a unique root \(q_*\in(1/2,3/5)\) at height one. Thus \(H_t\) is entrywise nonnegative **if and only if** \(t\geq\theta=-\log q_*\). At the boundary, \(q_*^4=2q_*-1\), giving \(a(\theta)=q_*>1/2\). Since \(a\) increases with \(q\), every \(0<t<\theta\) has \(a(t)>1/2\) and \(c(t)<0\).

**2. Sufficiency for every reaction strength.** If \(t\geq\theta\), \(H_t\) is a nonnegative, row-stochastic matrix, so it maps \([0,1]^4\) to itself. For \(0\leq z\leq1\), \(0\leq R_\rho(z)\leq1\) since the denominator squared minus \(z^2\) equals \(e^{-2\rho}(1-z^2)\geq0\). Hence the full composition maps the cube into itself for every \(\rho\geq0\).

**3. Necessity using saturation.** Suppose \(0<t<\theta\), and choose \(u=e_0=(1,0,0,0)^\mathsf{T}\). Its first half-step is \((a,b,c,b)^\mathsf{T}\), with \(a,b>0>c\). The output coordinate opposite the initial impulse is

\[
\bigl(S_{t,\rho}(e_0)\bigr)_2
=cR_\rho(a)+2bR_\rho(b)+aR_\rho(c).
\]

For each nonzero real \(z\), \(\lim_{\rho\to\infty}R_\rho(z)=\operatorname{sgn}(z)\). Therefore the last display tends to \(c+2b-a=1-2a<0\). By continuity there is a **finite** \(\rho\) with a negative output, disproving universal cube preservation. Continuity in \(u\) permits a strictly positive initial vector, e.g. a sufficiently small perturbation of \(e_0\) toward \((1/4,1/4,1/4,1/4)^\mathsf{T}\). The necessity and sufficiency prove the equivalence.

**4. Linear comparison and the lower regime.** For \(\rho=0\), \(R_0\) is the identity, so \(S_{t,0}=H_tH_t=H_{2t}\). Applying step 1 with \(2t\) proves that heat-only positivity holds exactly for \(t\geq\theta/2\). If \(0<t<\theta/2\), then the opposite kernel coefficient \(c(2t)<0\). For any fixed finite \(\rho\geq0\), differentiability of \(R_\rho\) at zero gives \(R_\rho(z)=e^\rho z+O(z^3)\), and therefore

\[
S_{t,\rho}(\delta e_0)
=e^\rho\delta H_{2t}e_0+O(\delta^3)
\quad(\delta\downarrow0).
\]

The opposite coordinate is negative for every sufficiently small \(\delta>0\). This establishes all three regimes. Finally, in the physical parameters the universal threshold is \(\nu\Delta\geq2\theta\), versus \(\nu\Delta\geq\theta\) for the linear map.

**5. Minimal grid size (context).** On standard equispaced periodic Fourier grids with two or three nodes, the spectral Laplacian has nonnegative off-diagonal entries (respectively \(1/2\) and \(1/3\)), so its heat exponential is nonnegative at every time. Four nodes are the first such periodic collocation grid for which the negative opposite Laplacian entry \(-1/2\) enables this phenomenon. This assertion concerns the standard one-dimensional pseudospectral symbols with the usual even-grid Nyquist mode.

## Verification

The accompanying standalone \(\texttt{verify.py}\) uses only Python's standard library. It checks the kernel factorization and stochastic row sum in 499 exact rational cases, finite-parameter negative witnesses in six subcritical cases, the linear versus nonlinear distinctions, semigroup composition, and 2,500 randomly chosen cube inputs at times above the exact threshold. It reports **3,533 passing checks**. Numerical checks corroborate, but do not replace, the proofs for every \(t,\rho,u\).

An illustrative witness is \(t=3\theta/4=0.457033397577\ldots\), \(\rho=100\), and \(u=e_0\). The opposite component of \(S_{t,100}(u)\) is approximately \(-0.21351581612\), while the opposite component of \(H_{2t}u\) is approximately \(+0.05601190446\). All coefficients and threshold values are reproduced by running \(\texttt{python verify.py}\).

## Relationship to prior work

Luo, Quan, Tan and Wu (2026, arXiv:2610.14867v1) study periodic Allen–Cahn Strang splitting, including continuum heat and numerical Fourier-pseudospectral experiments. Their stability/error and reported maximum-principle observations do not provide the finite four-node exact strong-reaction cutoff derived here. Dong Li (2021, arXiv:2107.09438) studies effective, approximately sharp maximum principles for spectral and Fourier-collocation schemes, including Strang splitting; that work establishes that sharp continuum maximum principles need not carry over to spectral discretizations. The present result does not claim this observation as new; its narrower contribution is the exact finite-grid, all-reaction-strength iff threshold and its factor-of-two gap from the purely linear threshold. Cai, Fang, Chen and Sun (2022, arXiv:2209.08437) prove an unconditionally discrete-maximum-principle-preserving splitting for a different, Toeplitz-based spatial fractional discretization, which does not cover the standard Fourier pseudospectral matrix used here.

## Limitations

Only four equispaced periodic nodes, the standard Fourier pseudospectral Laplacian, exact subflows, and nonnegative cubic reaction duration are covered. The cutoff is universal over reaction strengths; no full classification for each *fixed* finite strength is asserted. Between-grid-point trigonometric interpolation, higher spatial dimensions, nonuniform grids, alternate spatial stencils, noisy or approximate subflows, and arbitrary nonlinearities are not covered. The low-diffusion failure does not contradict unconditional time stability or continuum maximum principles, and says nothing about convergence accuracy as the grid is refined. The literature comparison is same-authority source inspection rather than independent priority certification; undiscovered equivalent specialized results remain possible.

## References

1. R. Luo, C. Quan, Z. Tan, Y. Wu, *Stability and Error Estimates with Optimal ε-Dependence for Strang Splitting of the Allen–Cahn Equation*, arXiv:2610.14867v1 (first public 2026-10-10). https://arxiv.org/html/2610.14867v1
2. D. Li, *Effective maximum principles for spectral methods*, arXiv:2107.09438v1 (2021). https://arxiv.org/abs/2107.09438
3. Y.-Y. Cai, Z.-W. Fang, H. Chen, H.-W. Sun, *A fast two-level Strang splitting method for multi-dimensional spatial fractional Allen-Cahn equations with discrete maximum principle*, arXiv:2209.08437v1 (2022). https://arxiv.org/abs/2209.08437
