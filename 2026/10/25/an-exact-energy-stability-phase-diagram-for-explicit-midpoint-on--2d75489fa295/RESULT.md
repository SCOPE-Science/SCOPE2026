# An exact energy-stability phase diagram for explicit midpoint on partially damped planar oscillators

## Finding
Consider the linear system \(\dot u=L_{a,b}u\), where
\[
L_{a,b}=\begin{pmatrix}-a&-b\\b&0\end{pmatrix},\qquad a>0,\quad b>0.
\]
The explicit midpoint rule, or any two-stage second-order explicit Runge--Kutta method on this linear system, has one-step matrix
\[R_h=I+hL_{a,b}+\tfrac12h^2L_{a,b}^2.\]
Set \(t=b^2/a^2>0\), \(x=ah\), and
\[g_t(x)=t^2x^3-2tx^2+4x-8.\]
Let \(\xi(t)\) be its unique positive root. For every \(a,b>0\) and \(h\ge0\), the Euclidean energy inequality \(\|R_hu\|_2\le\|u\|_2\) for **every** \(u\in\mathbb R^2\) holds **if and only if**
\[
0\le ah\le E(t),\qquad
E(t)=\begin{cases}\xi(t),&0<t\le1,\\2/t,&t\ge1.\end{cases}
\]
In particular, the largest possible dimensionless energy-safe stepsize over all nonzero coupling-to-damping ratios is
\[
\boxed{\max_{t>0}E(t)=\frac83,\quad\text{uniquely at }t=\frac38.}
\]
There is an exact endpoint degeneracy at \(t=1\), \(ah=2\): \(R_h=-I\), so every nonzero trajectory alternates signs without decaying. At all other critical endpoints the largest singular value is one but the entire matrix is not an isometry.

The spectral absolute-stability stepsize can be substantially more permissive. Let \(S(t)\) be the supremum of \(ah>0\) for which \(\rho(R_h)\le1\). Then
\[
S(t)=\begin{cases}
\dfrac4{1+\sqrt{1-4t}},&0<t\le\tfrac14,\\
\text{the unique positive root of }t^2x^3-2tx^2+2x-4=0,&t>\tfrac14.
\end{cases}
\]
For every \(t\ne1\), \(S(t)>E(t)\); equality holds only at \(t=1\). As the oscillation frequency increases relative to damping,
\[
\frac{S(t)}{E(t)}\sim 2^{-1/3}t^{1/3}\longrightarrow\infty
\qquad(t\to\infty).
\]
Thus eigenvalue-based RK absolute stability can permit arbitrarily larger steps than the requirement that each numerical step preserve the physical Euclidean energy. This comparison concerns single-step operator nonexpansiveness, not asymptotic convergence of repeated steps.

## Assumptions and scope
All matrices and initial data are real. Both \(a\) and \(b\) are strictly positive; the decoupled boundary \(b=0\) is excluded. No weighted norms, nonlinear vector fields, variable steps, or perturbations are included. \(\|\cdot\|_2\) is the usual Euclidean vector norm and its induced matrix norm; \(\rho\) is spectral radius. The continuous system is nonexpansive because \(L_{a,b}+L_{a,b}^{\mathsf T}=\operatorname{diag}(-2a,0)\), and in fact strictly contractive in the operator norm for every positive physical time: an equality trajectory would have first coordinate identically zero and hence, since \(b>0\), must vanish identically.

## Proof
**1. Dimensionless reduction.** Divide \(L_{a,b}\) by \(a\) and write \(b/a=\sqrt t\). The normalized matrix is \(L=\begin{pmatrix}-1&-\sqrt t\\\sqrt t&0\end{pmatrix}\). With \(R=I+xL+x^2L^2/2\), define the symmetric energy-defect matrix \(Q=I-R^{\mathsf T}R\). Since \(R^{\mathsf T}R\) is positive semidefinite, \(\|R\|_2\le1\) is exactly \(Q\succeq0\). Multiplication gives
\[
Q_{22}=\frac{t x^3}{4}\bigl(4-(1+t)x\bigr),\quad
Q_{12}=-\frac{\sqrt t\,x^2}{4}(x-2)^2,
\]
\[
\det Q=-\frac{t x^4}{16}(2-tx)g_t(x).
\]
These are polynomial identities; they are independently reproduced with rational polynomial arithmetic by the attached verification script. For \(x>0\) and \(Q_{22}>0\), the \(2\times2\) principal-minor criterion says \(Q\succeq0\) exactly when \(\det Q\ge0\). Endpoint equality is addressed by continuity, except for the simultaneous-zero point below.

**2. Root placement and the complete feasible interval.** The derivative has the strictly positive form
\[
g_t'(x)=3\bigl(tx-\tfrac23\bigr)^2+\tfrac83>0.
\]
Since \(g_t(0)=-8\) and \(g_t(x)\to+\infty\), a unique positive root \(\xi(t)\) exists. Two exact evaluations locate it:
\[
g_t(2/t)=\frac{8(1-t)}{t},\qquad
g_t\bigl(4/(1+t)\bigr)=-\frac{8(t-1)^3}{(1+t)^3}.
\]
When \(0<t<1\), both values are positive. Thus \(\xi(t)<\min\{2/t,4/(1+t)\}\), and the determinant is positive precisely up to \(x=\xi(t)\) inside the necessary diagonal range \(0<x\le4/(1+t)\). Beyond that root, the determinant immediately becomes negative, so no larger positive step is feasible. When \(t>1\), both evaluations are negative: \(2/t<\xi(t)\) and \(2/t<4/(1+t)\). Hence the determinant is nonnegative up to \(x=2/t\) and immediately negative beyond, establishing \(E(t)=2/t\). At \(t=1\), the root and both competing cutoffs equal \(2\); direct substitution gives \(R=-I\) at \(x=2\), while strict positivity of the minors holds for \(0<x<2\). For \(x>4/(1+t)\), \(Q_{22}<0\), excluding later nonexpansive windows in every parameter regime. At \(x=0\), \(R=I\) is nonexpansive.

**3. Optimize the physical energy step.** Implicit differentiation at the simple zero \(g_t(\xi(t))=0\) yields
\[
\xi'(t)=\frac{2\xi(t)^2\bigl(1-t\xi(t)\bigr)}{g_t'(\xi(t))}.
\]
As \(g_t(1/t)=(3-8t)/t\) and \(g_t\) is increasing, \(1-t\xi(t)>0\) if and only if \(t<3/8\); the sign reverses for \(t>3/8\). At \(t=3/8\), \(\xi(t)=1/t=8/3\). Therefore \(E\) is strictly increasing up to \(3/8\), strictly decreasing from \(3/8\) to \(1\), and equals the strictly decreasing \(2/t\) for \(t>1\). The global maximum is unique. At \(t=1\), the left and right slopes are respectively \(-1\) and \(-2\), explaining the branch change.

**4. Contrast with the spectral stability region.** Eigenvalues of the normalized \(L\) solve \(\lambda^2+\lambda+t=0\). For \(0<t\le1/4\), both are real negative; for each scalar \(\lambda<0\), the polynomial \(1+x\lambda+(x\lambda)^2/2\) has modulus at most one exactly when \(-2\le x\lambda\le0\). The more negative eigenvalue yields the stated real-spectrum formula for \(S(t)\).

For \(t>1/4\), the pair is \(\lambda=-1/2\pm i\sqrt{t-1/4}\). Substituting \(\lambda^2=-\lambda-t\) in the stability polynomial gives exactly
\[
\bigl|1+x\lambda+(x\lambda)^2/2\bigr|^2-1
=\frac{x}{4}\bigl(t^2x^3-2tx^2+2x-4\bigr).
\]
The cubic on the right is strictly increasing, because its derivative is \(3(tx-2/3)^2+2/3>0\); hence it has one positive root and the spectral stability interval is precisely the one claimed. For \(0<t\le1/4\), write \(u=\sqrt{1-4t}\in[0,1)\). Substituting \(S=4/(1+u)\) gives \(g_t(S)=4(1-u)^2/(1+u)>0\), so \(S>\xi(t)=E(t)\). For \(1/4<t<1\), \(g_t(2)=8t(t-1)<0\), hence \(E(t)>2\); the spectral cubic evaluated at \(E(t)\) equals \(4-2E(t)<0\), whence \(S>E\). For \(t>1\), evaluating the spectral cubic at \(E(t)=2/t\) gives \(4(1/t-1)<0\), again \(S>E\). At \(t=1\) both endpoints are \(2\). Finally, setting \(x=c t^{-2/3}\) in the spectral cubic and comparing leading terms gives \(c^3=4\), so \(S(t)\sim4^{1/3}t^{-2/3}\); combining with \(E(t)=2/t\) proves the claimed unbounded ratio.

## Verification
Run `python3 verify.py` with Python's standard library; it checks the matrix-defect identities and critical rational parameter cases using exact rational polynomial arithmetic and prints `VERIFY_OK`. The algebraic proof above, not finite numerical experiments, establishes the statements for all real positive parameters. Independent exact symbolic expansion was also used while preparing the identities. Every threshold equality and the excluded decoupled parameter boundary are explicit.

## Relationship to prior work
Achleitner, Arnold, and Jüngel (2023), arXiv:2308.05689v1, develop necessary and sufficient structural criteria for strong stability of explicit Runge--Kutta methods and hypocoercivity; their theorems are largely about sufficiently small steps and classes of matrices. They do not state this parameter-resolved largest **finite** energy-safe step, the optimizing skew-to-damping ratio, or the asymptotic gap from the spectral scalar stability interval. Their 2023 follow-up arXiv:2310.19758 likewise studies structural/local strong stability. Sun, Wei, and Wu (2022), arXiv:2201.06501, study energy laws for linear seminegative systems in more general settings; their conditions do not supply the present sharp oscillator family optimization. Sun and Shu (2019), arXiv:1912.11596, develop strong-stability remedies based on superviscosity, not the unmodified explicit midpoint's exact matrix interval. A previously recorded fixed-coefficient oscillator calculation establishes \(x\le2\) for the particular ratio \(t=1\) and several RK orders; that **special case is not new**. The results claimed here are the complete variable-coupling phase diagram, the unique optimum \((t,x)=(3/8,8/3)\), and the quantitative unbounded spectral-vs-energy disparity. An earlier exact-splitting study on the same continuous oscillator concerns a different integrator, so its unconditional stepwise passivity neither proves nor contradicts these results.

## Limitations
The result gives exact one-step Euclidean nonexpansiveness in this one-parameter family of \(2\times2\) linear systems. It does not imply spectral instability whenever energy nonexpansiveness fails: indeed the spectral stability interval is often longer. It does not claim every trajectory grows when \(\|R_h\|_2>1\), nor does it extend to general high-dimensional, nonlinear, variable-step, or weighted-norm schemes. Although the literature checks identified no implication-equivalent theorem, undiscovered equivalent coverage remains possible; independent literature validation has not been performed.

## References
1. F. Achleitner, A. Arnold, A. Jüngel, *Necessary and sufficient conditions for strong stability of explicit Runge--Kutta methods*, arXiv:2308.05689v1, 2023. https://arxiv.org/html/2308.05689v1
2. F. Achleitner, A. Arnold, A. Jüngel, *Hypocoercivity for Linear ODEs and Strong Stability for Runge--Kutta Methods*, arXiv:2310.19758v1, 2023. https://arxiv.org/abs/2310.19758
3. Z. Sun, Y. Wei, K. Wu, *On Energy Laws and Stability of Runge--Kutta Methods for Linear Seminegative Problems*, arXiv:2201.06501, 2022. https://arxiv.org/abs/2201.06501
4. Z. Sun, C.-W. Shu, *Enforcing strong stability of explicit Runge--Kutta methods with superviscosity*, arXiv:1912.11596, 2019. https://arxiv.org/abs/1912.11596
5. J. M. Sanz-Serna, K. C. Zygalakis, *Contractivity of Runge--Kutta methods for convex gradient systems*, arXiv:1909.09971, 2019. https://arxiv.org/abs/1909.09971
