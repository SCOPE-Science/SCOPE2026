# Richardson-parameter invariance and a unique conditioning optimum for two-grid acceleration

## Finding
Consider the depth-one, one-presmoothing, no-postsmoothing two-grid accelerator with the two residual columns introduced in Adler, He, Hu, and Lefebvre (2026), using a scalar Richardson preconditioner. On every admissible linear system, its **exact-arithmetic iterate** is independent of the positive Richardson weight: one cycle is exactly a restarted two-step GMRES cycle. Nevertheless, the corresponding two-column coarse normal matrix is weight-dependent and has a **unique** best-conditioned positive weight. The exact optimum, conditioning penalty, equality criterion, and both extreme-weight asymptotics are given below.

More precisely, let \(A\in\mathbb R^{n\times n}\) be nonsingular, \(n\ge2\), let \(r=b-Ax\ne0\), and suppose \(r\) and \(Ar\) are linearly independent. Write
\[
 a=Ar,\quad d=A^2r,\quad u=a^\top a,\quad v=a^\top d,\quad w=d^\top d,\quad \Delta=uw-v^2>0.
\]
For any \(\omega>0\), define the presmoothed point \(x_{\mathrm{pre}}=x+\omega r\), the presmoothed residual \(r_{\mathrm{pre}}=r-\omega Ar\), and the two-column prolongation
\[
 P_\omega=\bigl[-\omega r,\;-\omega(r-\omega Ar)\bigr].
\]
Set \(G_\omega=P_\omega^\top A^\top A P_\omega\), and compute
\[
 x_+=x_{\mathrm{pre}}+P_\omega G_\omega^{-1}P_\omega^\top A^\top r_{\mathrm{pre}}.
\]
Then \(x_+\) uniquely minimizes \(\|b-Az\|_2\) over \(z\in x+\operatorname{span}\{r,Ar\}\); hence it is the length-two GMRES cycle started at \(x\), independently of \(\omega\). Every subsequent nondegenerate cycle repeats this property with a fresh residual.

The coarse matrix satisfies
\[
 G_\omega=\omega^2\begin{bmatrix}
 u&u-\omega v\\ u-\omega v&u-2\omega v+\omega^2w
 \end{bmatrix},\quad
 \det G_\omega=\omega^6\Delta.
\]
Its spectral condition number \(\kappa_2(G_\omega)\) has the unique global minimum over all positive weights at
\[
 \boxed{\omega_\star=\sqrt{\frac{2u}{w}}=\frac{\sqrt2\,\|Ar\|_2}{\|A^2r\|_2}}.
\]
Defining \(T_\omega=\operatorname{tr}(G_\omega)/\sqrt{\det G_\omega}\) gives the exact penalty identity
\[
 T_\omega-T_{\omega_\star}=\frac{w(\omega-\omega_\star)^2}{\omega\sqrt\Delta},
 \qquad T_{\omega_\star}=\frac{2(\sqrt{2uw}-v)}{\sqrt\Delta}.
\]
The minimum possible condition number is one if and only if \(v=\sqrt{uw/2}\). In either extreme,
\[
 \kappa_2(G_\omega)\sim\frac{4u^2}{\Delta\,\omega^2}\quad(\omega\downarrow0),\qquad
 \kappa_2(G_\omega)\sim\frac{w^2\omega^2}{\Delta}\quad(\omega\to\infty).
\]
Thus the exact outer update cannot be accelerated by changing this scalar smoothing weight, while its normal-equation conditioning deteriorates without bound at both weight extremes. The unique best-conditioned weight need not lie in the stand-alone Richardson stability interval: for \(A=\operatorname{diag}(1,2,4)\) and \(r=(1,1/100,1/100)^\top\), one obtains \(\omega_\star=\sqrt{835/428}>1/2\), whereas the ordinary unaccelerated Richardson step is stable only for \(0<\omega<1/2\). The residual-minimizing coarse cycle remains the same in exact arithmetic.

## Assumptions and scope
All vectors and matrices are real; the Euclidean vector norm and spectral matrix condition number are used. The linear system is square and nonsingular, the arithmetic and coarse least-squares solve are exact, \(\omega>0\), and \(r,Ar\) are independent. No symmetry or definiteness assumption on \(A\) is required. The prolongation is specifically the paper's depth-one two-residual construction, not a generic depth-one Anderson or nonlinear-GMRES history space. The projection is the residual-minimizing \(A^\top A\) projection, with exactly one scalar Richardson presmoothing step and no postsmoothing. If an eventual restarted residual is zero, the solver terminates; if it becomes an eigenvector residual, the displayed two-column inverse is singular and is outside the theorem's domain.

## Proof
The two prolongation columns span \(r\) and \(r-\omega Ar\). Their difference equals \(\omega Ar\) up to a nonzero scalar; hence for \(\omega>0\), \(\operatorname{Range}(P_\omega)=\operatorname{span}\{r,Ar\}\). Because \(x_{\mathrm{pre}}-x=\omega r\) is already in this space, both affine search spaces coincide:
\[
 x_{\mathrm{pre}}+\operatorname{Range}(P_\omega)
 =x+\operatorname{span}\{r,Ar\}.
\]
The correction equation \(G_\omega c=P_\omega^\top A^\top r_{\mathrm{pre}}\) is the normal equation for minimizing \(\|r_{\mathrm{pre}}-AP_\omega c\|_2^2\). Nonsingularity of \(A\) and independence of the columns make \(G_\omega\) positive definite, so the minimizer is unique. The affine space is exactly the GMRES length-two Krylov affine space. This proves weight-invariant identity of the resulting iterate, including for nonsymmetric matrices. Repeating from the new residual gives restarted GMRES with restart length two on every nondegenerate cycle.

For the conditioning assertion, apply \(A\) to the columns; their signs cancel from the Gram matrix, leaving the two vectors \(\omega a\) and \(\omega a-\omega^2d\). Their inner products give the displayed entries. Direct expansion yields the determinant \(\omega^6(uw-v^2)\) and trace \(\omega^2(2u-2\omega v+\omega^2w)\). Since \(\Delta>0\), both eigenvalues are positive. Writing \(\lambda_+\ge\lambda_->0\) for these eigenvalues,
\[
 T_\omega=\frac{\lambda_++\lambda_-}{\sqrt{\lambda_+\lambda_-}}
 =\sqrt{\kappa_2(G_\omega)}+\frac1{\sqrt{\kappa_2(G_\omega)}}
 =\frac{2u/\omega-2v+\omega w}{\sqrt\Delta}.
\]
The function \(s+1/s\) is strictly increasing on \(s\ge1\); hence minimizing \(\kappa_2(G_\omega)\) is equivalent to minimizing \(T_\omega\). Completing the square with \(\omega_\star^2=2u/w\) gives
\[
 T_\omega-T_{\omega_\star}
 =\frac{2u/\omega+\omega w-2\sqrt{2uw}}{\sqrt\Delta}
 =\frac{w(\omega-\omega_\star)^2}{\omega\sqrt\Delta}.
\]
This is zero at exactly one positive weight. The eigenvalue formula equivalently reads
\[
 \kappa_2(G_\omega)=
 \frac{T_\omega+\sqrt{T_\omega^2-4}}
 {T_\omega-\sqrt{T_\omega^2-4}},\quad T_\omega\ge2.
\]
At its minimum, \(\kappa_2=1\) exactly when \(T_{\omega_\star}=2\). Squaring \(\sqrt{2uw}-v=\sqrt{uw-v^2}\) and using \(v\in(-\sqrt{uw},\sqrt{uw})\) shows this occurs if and only if \(v=\sqrt{uw/2}\). Finally, for \(T\to\infty\), the eigenvalue ratio satisfies \(\kappa_2/T^2\to1\). Substituting \(T_\omega\sim2u/(\omega\sqrt\Delta)\) as \(\omega\downarrow0\) and \(T_\omega\sim\omega w/\sqrt\Delta\) as \(\omega\to\infty\) establishes the claimed sharp asymptotics.

## Verification
The accompanying self-contained `check.py` (Python standard library only) performs 1,242 rational-identity and numerical conditioning assertions over 23 explicitly constructed nonsingular three-dimensional systems and eight rational positive weights per system. These check exact equality of two-grid and length-two GMRES corrections, the Gram entries, determinant and trace; they also examine the unique optimum and small-weight asymptotics. The proof above, not the finite tests, establishes the universal assertions. For example, at \(A=\operatorname{diag}(1,2,4)\), \(r=(1,1,1)^\top\), one obtains \(u=21\), \(v=73\), \(w=273\), \(\Delta=404\), and \(\omega_\star=\sqrt{2/13}\).

## Relationship to prior work
Adler, He, Hu, and Lefebvre (2026), equation (27) and Algorithm 6, introduce the two-residual prolongation and residual-minimizing two-grid correction. The equality of this specific scalar-Richardson specialization with cyclewise restarted GMRES(2), and its exact unique normal-matrix conditioning optimum, are the assertions assessed here, **not** the original two-grid construction, generic Krylov minimal-residual principle, or normal-equation algebra. The paper discusses connections between nonlinear GMRES and GMRES, but does not present these two conclusions for its new depth-one two-residual prolongation. He (2026) analyzes nonlinear GMRES on preconditioned Richardson iteration, a different iterative construction. Pollock and Rebholz (2022) control conditioning of Anderson least-squares spaces through length and angle filtering, rather than this optimal scalar weight for the specified two-grid normal matrix. The connections to classic restarted GMRES and to generic two-column conditioning are therefore explicit; additional specialized prior derivations cannot be categorically excluded.

## Limitations
The theorem is an exact-arithmetic statement and an exact condition-number computation. It does **not** prove the actual floating-point rounding error, backward stability, or wall-clock advantage of any implementation. In particular, direct normal equations may incur a squared least-squares matrix condition number; using an orthogonal Krylov basis or QR can change numerical behavior without changing the exact search space. The invariance fails to follow for generic matrix preconditioners, non-Richardson smoothing, more history columns, different coarse inner products, or nonlinear problems. No blanket convergence claim is made for restarted GMRES(2) on arbitrary nonsymmetric systems. The excluded rank-deficient case needs a breakdown-aware implementation. Literature overlap remains a scientific risk despite the inspected relevant works.

## References
1. James Adler, Yunhui He, Xiaozhe Hu, Satchel Lefebvre, *A Unified Two-Grid Framework for Anderson Acceleration and Nonlinear GMRES*, arXiv:2609.13091 (public 2026-09-11), https://arxiv.org/abs/2609.13091. In particular Section 4.1, equation (27), Algorithm 6, and Section 5.
2. Yunhui He, *Properties of Nonlinear GMRES Applied to the Preconditioned Richardson Iteration*, arXiv:2603.25983 (2026), https://arxiv.org/abs/2603.25983.
3. Sara Pollock and Leo Rebholz, *Filtering for Anderson acceleration*, arXiv:2211.12953 (2022), https://arxiv.org/abs/2211.12953.
4. Hans De Sterck, Yunhui He, Oliver Krzysik, *Anderson Acceleration as a Krylov Method with Application to Asymptotic Convergence Analysis*, arXiv:2109.14181 (2021), https://arxiv.org/abs/2109.14181.
