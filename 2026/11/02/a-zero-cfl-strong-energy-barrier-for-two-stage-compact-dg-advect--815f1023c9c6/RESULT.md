# A zero-CFL strong-energy barrier for two-stage compact DG advection

## Finding
For the uncorrected two-stage, second-order compact Runge–Kutta discontinuous Galerkin (cRKDG) method on a periodic one-dimensional positive-speed linear advection equation, **there exists no positive Courant number for which the whole solution polynomial is an \(L^2\) nonexpansion for every initial polynomial**. This statement applies to every two-stage order-two explicit Runge–Kutta tableau under the compact-stage construction specified below. A two-cell Fourier mode already has an energy-decrement matrix with strictly negative determinant for every positive Courant number. The mode's exact maximal squared-energy amplification and its sharp small-step asymptotics are also determined.

More precisely, with \(\nu=a\Delta t/\Delta x>0\) and \(W=\operatorname{diag}(1,1/3)\), the restriction of the update to an alternating piecewise-affine subspace is
\[
M_\nu=\begin{pmatrix}1-2\nu&-2\nu+2\nu^2\\6\nu&1-6\nu^2\end{pmatrix},\qquad
\det(W-M_\nu^{\mathsf T}WM_\nu)=-4\nu^4.
\]
Let \(T(\nu)=4\nu-16\nu^2+24\nu^3-48\nu^4\). The maximum squared-energy ratio on that subspace is exactly
\[
\mathcal A(\nu)=1+\frac{\sqrt{T(\nu)^2+48\nu^4}-T(\nu)}{2}
=1+3\nu^3+O(\nu^4)\quad(\nu\downarrow0).
\]
In particular, this distinguishes eigenvalue-based Fourier stability from the stronger *one-step physical-energy monotonicity* required by a fully discrete quadratic-entropy inequality.

## Assumptions and scope
Consider \(u_t+a u_x=0\) with constant speed \(a>0\) on a periodic domain partitioned into any even number \(N\ge2\) of cells of common width \(\Delta x>0\). On cell \(j\), use the reference coordinate \(\xi=2(x-x_j)/\Delta x\) and polynomial \(u_j(\xi)=A_j+B_j\xi\), without slope correction, filtering, or end-of-step entropy limiting. All mass, volume and interface terms are integrated exactly. Use the physical upwind numerical flux \(\widehat f=a u^-\).

Define the compact internal-stage operator \(G\) as the cellwise \(L^2\) projection of \(-a\partial_x u\), and the final-stage operator \(F\) as the usual upwind DG residual. For an explicit two-stage Runge–Kutta tableau with entries \(c_2=a_{21}\) and \(b_1,b_2\), assume the order-two conditions \(b_1+b_2=1\) and \(b_2c_2=1/2\). The uncorrected full step is
\[
U^{(2)}=U^n+c_2\Delta t\,G(U^n),\quad
U^{n+1}=U^n+\Delta t\,[b_1F(U^n)+b_2F(U^{(2)})].
\]
The physical global quadratic energy is \(\lVert u\rVert_{L^2}^2=\Delta x\sum_j(A_j^2+B_j^2/3)\). Here \(\nu=a\Delta t/\Delta x\) has no upper restriction. The special two-cell pattern below is an admissible periodic DG function; its jumps are allowed.

## Proof
**1. Exactly reconstruct the DG operators.** Testing the upwind weak form against \(1\) and \(\xi\), and dividing by the diagonal reference mass matrix, gives
\[
\begin{aligned}
F(A_j)&=-\frac a{\Delta x}(A_j+B_j-A_{j-1}-B_{j-1}),\\
F(B_j)&=\frac{3a}{\Delta x}(A_j-B_j-A_{j-1}-B_{j-1}).
\end{aligned}
\]
Because \(-a\partial_x(A_j+B_j\xi)=-2aB_j/\Delta x\) is constant inside each cell, the compact operator gives
\[
G(A_j)=-2aB_j/\Delta x,\qquad G(B_j)=0.
\]
Both formulas use the physical upwind trace on interfaces and no numerical flux inside the compact operator.

**2. The two-stage tableau disappears.** Linearity of the equation and the order conditions imply
\[
U^{n+1}=U^n+\Delta t\,F(U^n)+\frac{\Delta t^2}{2}F(G(U^n)).
\]
Thus all explicit two-stage order-two tableaux share this update on the specified linear problem; the explicit-midpoint tableau is merely a convenient representative.

**3. Restrict to the alternating invariant subspace.** Let \(A_j=(-1)^jA\) and \(B_j=(-1)^jB\), which is compatible with periodicity whenever \(N\) is even. The first operator is represented in dimensionless form by \(\left(\begin{smallmatrix}-2&-2\\6&0\end{smallmatrix}\right)\) and the second by \(\left(\begin{smallmatrix}0&-2\\0&0\end{smallmatrix}\right)\). Substituting into step 2 produces
\[
\binom{A^+}{B^+}=M_\nu\binom AB,\qquad
M_\nu=\begin{pmatrix}1-2\nu&-2\nu+2\nu^2\\6\nu&1-6\nu^2\end{pmatrix}.
\]
The per-cell squared \(L^2\) norm is exactly \(\Delta x(A^2+B^2/3)\), so global norm ratios on this invariant mode are the generalized Rayleigh quotients of \(M_\nu^{\mathsf T}WM_\nu\) relative to \(W=\operatorname{diag}(1,1/3)\).

**4. An exact sign obstruction at every positive step.** Direct multiplication yields the energy decrement
\[
Q_\nu:=W-M_\nu^{\mathsf T}WM_\nu
=\begin{pmatrix}
4\nu(1-4\nu)&2\nu^2(8\nu-3)\\
2\nu^2(8\nu-3)&8\nu^3(1-2\nu)
\end{pmatrix}.
\]
A complete polynomial expansion gives the exact identity \(\det Q_\nu=-4\nu^4\). Consequently, for every \(\nu>0\), the *real symmetric* matrix \(Q_\nu\) has one strictly negative and one strictly positive eigenvalue. Choose a real vector \((A,B)\ne(0,0)\) in a negative direction. Then
\[
\lVert u^{n+1}\rVert_{L^2}^2-\lVert u^n\rVert_{L^2}^2
=-N\Delta x\,(A,B)Q_\nu(A,B)^{\mathsf T}>0.
\]
For a rational witness at \(\nu=1/10\), take \((A,B)=(3/20,1)\). The **per-cell squared energy** rises by exactly \(7\Delta x/5000\), since \((A,B)Q_{1/10}(A,B)^{\mathsf T}=-7/5000\).

**5. Exact maximal amplification and asymptotics.** The generalized eigenvalues of \(Q_\nu\) relative to \(W\) have trace
\[
T(\nu)=\operatorname{tr}(W^{-1}Q_\nu)=4\nu-16\nu^2+24\nu^3-48\nu^4
\]
and product \(\det(W^{-1}Q_\nu)=-12\nu^4\). Their smaller member is \([T(\nu)-\sqrt{T(\nu)^2+48\nu^4}]/2<0\). Since the squared-energy ratio is \(1\) minus this generalized Rayleigh quotient, its exact maximum is \(\mathcal A(\nu)\) in the Finding. As \(\nu\downarrow0\), \(T(\nu)=4\nu+O(\nu^2)>0\); rationalization gives
\[
\mathcal A(\nu)-1
=\frac{24\nu^4}{\sqrt{T(\nu)^2+48\nu^4}+T(\nu)}
=3\nu^3+O(\nu^4).
\]
This is the sharp extremal excess *within the alternating mode*, not a purported closed-form maximization over all Fourier modes on arbitrary grids. The determinant argument proves the universal no-nonexpansion result.

## Verification
A standalone exact-symbolic and finite-mesh verifier is included as `verify.py`. It independently constructs the two-cell weak-form spatial matrices, recovers the alternating update, checks the polynomial determinant and generalized trace, checks the rational witness, and tests the exact root formula and asymptotics numerically over positive step sizes. Execute `python verify.py` with Python and SymPy installed. Symbolic identities establish the algebraic certificate; numerical sampling is a supplemental diagnostic, not the universal proof.

## Relationship to prior work
Chen, Sun, and Xing (2023 preprint; 2024 journal article) define the compact-stage RKDG construction and report second-order **von Neumann eigenvalue** stability up to Courant number approximately \(1/3\). That spectral statement does not imply contraction of the physical \(L^2\) norm at each step. The present exact determinant and \(\nu^3\) small-step amplification characterize that missing stronger property.

Sun's October 2026 study proves **weak cell-average entropy inequalities** for compact RKDG under suitable conditions and adds terminal cell-average-preserving corrections for strong entropy stability. The present analysis concerns the **uncorrected full DG polynomial** and shows that the need for an energy correction cannot generally be removed merely by choosing a smaller positive step. It does not contradict weak cell-average entropy stability, and it does not claim failure of the corrected method.

Liu, Jiang, and Zhang (October 2026) establish a different arbitrarily-small-step *weak cell-average entropy obstruction* for **standard noncompact three-stage RKDG**, along with flux/correction designs for compact single-step schemes. Neither their counterexample nor their stabilized method implies the precise **uncorrected two-stage compact** \(L^2\) decrement determinant, its all-positive-step sign, or its sharp alternating-mode amplification.

Sun and Shu (2017) prove a one-step \(L^2\) contraction theorem for a Lax–Wendroff DG scheme using upwind numerical fluxes for both its state and auxiliary derivative, and a weaker long-time bound for another flux arrangement. The auxiliary flux arrangements differ from the cell-local stage operator used here, so their strong contraction theorem is not a contradiction and does not cover the present uncorrected compact construction. A relevant later filtered-RKDG Fourier-analysis paper could only be assessed from accessible bibliographic material, not its full text.

## Limitations
The result is restricted to the exactly integrated degree-one real cRKDG method, constant-coefficient scalar advection, periodic even uniform meshes, physical upwind flux, and the **uncorrected** polynomial. It is a one-step norm obstruction, not a divergence or spectral-radius instability theorem. The exact amplification coefficient \(3\) is sharp only on the exhibited invariant alternating Fourier subspace, although that subspace suffices for the all-Courant global obstruction. It does not establish behavior under terminal entropy correction, filters, nonlinear fluxes, odd mesh sizes, finite precision, or an alternate Lax–Wendroff derivative-flux choice. Historical priority cannot be proven by a bounded literature search; an inaccessible specialized paper remains a residual comparison risk. Independent mathematical audit has not been performed.

## References
1. Z. Sun, *Fully discrete multi-entropy-stable compact Runge–Kutta discontinuous Galerkin methods for hyperbolic conservation laws*, arXiv:2610.18837v1 (first public 2026-10-13), https://arxiv.org/abs/2610.18837.
2. Q. Chen, Z. Sun, and Y. Xing, *The Runge–Kutta discontinuous Galerkin method with compact stencils for hyperbolic conservation laws*, arXiv:2307.06471v1 (2023), https://arxiv.org/abs/2307.06471.
3. Y. Liu, Y. Jiang, and M. Zhang, *High-Order Fully Discrete Entropy-Stable DG Methods with Compact Explicit Single-Step Time Discretizations*, arXiv:2610.30535v1 (2026-10-21), https://arxiv.org/abs/2610.30535.
4. Z. Sun and C.-W. Shu, *Stability analysis and error estimates of Lax–Wendroff discontinuous Galerkin methods for linear conservation laws*, ESAIM: M2AN (2017), DOI:10.1051/m2an/2016049, https://doi.org/10.1051/m2an/2016049.
5. B. Atawiah and Z. Sun, *Filtered RKDG Methods: Fourier Analysis for the Second-Order Case*, Journal of Scientific Computing (2026), DOI:10.1007/s10915-026-03437-y. Full text not inspected.
