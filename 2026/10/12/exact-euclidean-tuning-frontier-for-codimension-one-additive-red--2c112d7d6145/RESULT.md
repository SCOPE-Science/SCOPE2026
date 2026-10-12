# Exact Euclidean tuning frontier for codimension-one additive reduced-basis preconditioning

## Finding
Let \(m\ge 1\), let \(A\in\mathbb R^{(m+1)\times(m+1)}\) be symmetric positive definite, and let \(P\in\mathbb R^{(m+1)\times m}\) have orthonormal columns. Choose a unit vector \(q\) perpendicular to the columns of \(P\), and write
\[
H=P^{\mathsf T}AP,\qquad b=P^{\mathsf T}Aq,\qquad d=q^{\mathsf T}Aq.
\]
Define the Type-II additive reduced-basis inverse action and the unit-relaxation Richardson error operator by
\[
B_\alpha=PH^{-1}P^{\mathsf T}+\alpha qq^{\mathsf T},\qquad E_\alpha=I-B_\alpha A,\qquad \alpha>0.
\]
Put \(c=\|H^{-1}b\|_2\), \(p=\|b\|_2\), and \(\tau=b^{\mathsf T}H^{-1}b\). The **exact optimal worst-case one-step Euclidean error factor** is
\[
\boxed{\ \inf_{\alpha>0}\|E_\alpha\|_2
=\max\left\{c,\frac{p\sqrt{1+c^2}}{\sqrt{d^2+p^2}}\right\}.\ }
\]
Its **unique** minimizing regularizer is
\[
\boxed{
\alpha_{\mathrm{opt}}=
\begin{cases}
1/d,&dc\ge p,\\[2pt]
d(1+c^2)/(d^2+p^2),&dc<p.
\end{cases}}
\]
The first branch includes \(b=0\). In particular, a positive choice of \(\alpha\) making **every Euclidean error strictly smaller after one step** exists if and only if
\[
\boxed{\ c<1\quad\text{and}\quad d>pc.\ }
\]
In contrast, the stationary iteration is **spectrally convergent** exactly for
\[
\boxed{\ 0<\alpha<\frac{2}{d+\tau}.\ }
\]
Thus spectral convergence need not imply Euclidean contraction for any choice of the complement regularizer.

For an explicit example, take \(m=2\), \(P=(e_1,e_2)\), and
\[
A_*=
\begin{pmatrix}
1&0&1/2\\
0&4&2\\
1/2&2&27/20
\end{pmatrix}\succ0.
\]
Here \(\tau=5/4\), \(d-\tau=1/10>0\), \(c^2=1/2\), and \(p^2=17/4\). Every \(\alpha>0\) satisfies the sharp lower bound
\[
\boxed{\ \|I-B_\alpha A_*\|_2\ge\sqrt{2550/2429}>1,\ }
\]
with equality only at \(\alpha=810/2429\). Yet **all** \(0<\alpha<10/13\) yield an asymptotically convergent stationary iteration. This strict noncontraction persists under sufficiently small perturbations within the symmetric positive-definite matrices.

More specifically, dimension three is minimal for the obstruction \(c<1\) but \(d\le pc\): when \(m=1\), \(pc=\tau\), so positive definiteness enforces \(d>pc\). This minimal-dimension statement does **not** exclude two-dimensional noncontraction caused by \(c\ge1\).

## Assumptions and scope
All spaces are finite-dimensional and real; the block decomposition uses the Euclidean inner product and an orthonormal basis. The matrix \(A\) is symmetric positive definite, hence \(H\succ0\), \(d>\tau\ge0\), and \(d>0\). The reduced space and \(B_\alpha\) are fixed during the iteration. The update is \(x^{+}=x+B_\alpha(f-Ax)\), with unit outer relaxation, and the error is measured in the original **Euclidean** norm, not an energy or preconditioner-weighted norm. No floating-point effects, adaptive reduced-space changes, or FGMRES residual-minimization steps are included. All formulas quantify over every such \(m,A,P,q\) and every positive regularizer as indicated.

## Proof
**Block reduction.** Orthogonal conjugation by \([P,q]\) preserves spectral norms and eigenvalues. In these coordinates
\[
A=\begin{pmatrix}H&b\\b^{\mathsf T}&d\end{pmatrix},\quad
B_\alpha=\begin{pmatrix}H^{-1}&0\\0&\alpha\end{pmatrix},\quad
E_\alpha=\begin{pmatrix}0&-H^{-1}b\\-\alpha b^{\mathsf T}&1-\alpha d\end{pmatrix}.
\]
If \(b=0\), then \(\|E_\alpha\|_2=|1-\alpha d|\) and its unique minimum is zero at \(\alpha=1/d\), giving every assertion for this case. Assume henceforth \(b\ne0\), so \(p,c>0\). The operator annihilates first-block inputs perpendicular to \(b\). Choosing unit input direction \(b/p\) and unit first-block output direction \(H^{-1}b/c\) therefore shows that its **nonzero singular values** are those of
\[
T_\alpha=\begin{pmatrix}0&-c\\-\alpha p&1-\alpha d\end{pmatrix}.
\]
(The displayed input and output bases need not coincide; this is an independent orthogonal reduction of singular values.) In particular \(\|E_\alpha\|_2=\|T_\alpha\|_2\ge c\), since the Euclidean norm of its first row is \(c\).

**Exact minimax.** For a trial squared bound \(z>c^2\), the condition \(\|T_\alpha\|_2^2\le z\) is equivalent to \(zI-T_\alpha^{\mathsf T}T_\alpha\succeq0\). Its determinant is
\[
\begin{aligned}
F_z(\alpha)
&=(z-\alpha^2p^2)(z-c^2)-z(1-\alpha d)^2\\
&=z(z-c^2-1)+2zd\alpha-
\bigl[(z-c^2)p^2+zd^2\bigr]\alpha^2.
\end{aligned}
\]
Put \(W_z=(z-c^2)p^2+zd^2>0\). This is a strictly concave quadratic in \(\alpha\), uniquely maximized at \(\alpha_z=zd/W_z\), with
\[
\boxed{\ W_zF_z(\alpha_z)
=z(z-c^2)\bigl[(d^2+p^2)z-p^2(1+c^2)\bigr].\ }
\]
Thus if \(z>c^2\) is attainable then necessarily
\(z\ge z_*:=p^2(1+c^2)/(d^2+p^2)\). In conjunction with the row bound, every choice of regularizer obeys
\[
\|E_\alpha\|_2^2\ge\max\{c^2,z_*\}.
\]
If \(dc\ge p\), choose \(\alpha=1/d\). Then \(T_\alpha\) has off-diagonal entries \(-c\) and \(-p/d\), so \(\|T_\alpha\|_2=\max\{c,p/d\}=c\). This realizes the lower bound; equality at its row lower bound also requires \(1-\alpha d=0\), proving uniqueness.

If \(dc<p\), then \(z_*>c^2\). Set \(\alpha=d(1+c^2)/(d^2+p^2)\). This equals \(\alpha_{z_*}\), so \(F_{z_*}(\alpha)=0\), while the leading principal minor of \(z_*I-T_\alpha^{\mathsf T}T_\alpha\) is
\[
z_*-\alpha^2p^2
=\frac{p^2(1+c^2)(p^2-c^2d^2)}{(d^2+p^2)^2}>0.
\]
Hence that matrix is positive semidefinite and \(\|T_\alpha\|_2^2=z_*\). Strict concavity of \(F_{z_*}\) forces \(\alpha\) to be its unique maximizer whenever the bound is attained. The two branches agree at \(dc=p\). This proves the exact norm and unique minimizer claims.

**Strict contraction and spectral convergence.** The minimum factor is less than one precisely when \(c<1\) and \(p^2(1+c^2)<d^2+p^2\), equivalently \(c<1\) and \(d>pc\). This is a necessary-and-sufficient condition; the corresponding minimizing positive regularizer supplies sufficiency.

Since \(B_\alpha\succ0\), the product \(B_\alpha A\) is similar to the SPD matrix \(B_\alpha^{1/2}AB_\alpha^{1/2}\). Consequently \(\rho(E_\alpha)<1\) if and only if all eigenvalues of that SPD matrix are less than two. In block coordinates,
\[
B_\alpha^{1/2}AB_\alpha^{1/2}
=\begin{pmatrix}I&\sqrt\alpha\,H^{-1/2}b\\
\sqrt\alpha\,b^{\mathsf T}H^{-1/2}&\alpha d\end{pmatrix}.
\]
The Schur complement of the top block of \(2I-B_\alpha^{1/2}AB_\alpha^{1/2}\) is \(2-\alpha(d+\tau)\). Therefore this difference is positive definite exactly when \(\alpha<2/(d+\tau)\). Positivity of \(\alpha\) completes the claimed sharp spectral-convergence interval.

**Counterexample and dimensional boundary.** The Schur complement of \(H=\operatorname{diag}(1,4)\) in the displayed \(A_*\) is \(1/10\), verifying \(A_*\succ0\). Exact rational calculation yields \(z_*=2550/2429>1\), \(\alpha_{\mathrm{opt}}=810/2429\), and \(2/(d+\tau)=10/13\). Moreover \(c<1\) and \(d<pc\) hold strictly, so continuity of \(c,p,d\) on the SPD cone makes this failure robust under small perturbations. If \(m=1\), then \(H=(h)\), \(p=|b|\), \(c=|b|/h\), and \(pc=b^2/h=\tau<d\), excluding this particular obstruction.

## Verification
The standalone `verify.py` uses exact rational arithmetic to check the Schur complement, minimizing parameter, worst-case squared norm, and spectral-convergence interval for \(A_*\). It then independently forms \(I-B_\alpha A\) using NumPy and checks the derived optimal factor and direct comparisons against four alternate scalings for 3,500 generated positive-definite blocks of sizes \(2\) through \(8\). The script reports `VERIFY_OK exact_witness=1 random_SPD_blocks=3500`. Such finite checks corroborate identities but are not proofs of the quantified claims; the proof is the algebra above. Reproduce with `python verify.py` after installing `requirements.txt`.

## Relationship to prior work
Fan, Hu, and Zhang [1, eqs. (3.3)–(3.6), Theorem 3.4] introduce the Type-II additive reduced-basis inverse action and prove nonsingularity. Their section 3.3 discusses keeping the scalar regularization small, whereas their Richardson estimate in section 3.4 uses **Type I** and is conditioned on a projection-error hypothesis; neither determines the optimal scalar in the fixed Type-II codimension-one **Euclidean operator norm**, nor the sharp noncontraction obstruction. Southworth and Olivier [2, sections 1–2] analyze the spectrum and convergence of broader block-diagonal and Schur-complement preconditioners, not the exact minimizing one-step Euclidean factor over this scalar family. Demmel [3] studies near-optimal **condition-number** block scaling, a different objective. Published related results [4] concern fixed-diagonal Jacobi with global Richardson damping, [5] compare two-coordinate Gauss–Seidel orders, and [6] study additive forward/backward triangular inverses. Their preconditioner families and quantified objectives do not imply the present formulas. These comparisons establish no absolute priority claim; an algebraically equivalent result in older block-iterative literature remains possible.

## Limitations
The theorem is an exact-arithmetic statement for real SPD systems with a **one-dimensional** orthogonal complement and a **fixed** reduced subspace, with left-preconditioned unit-relaxation Richardson. It does not establish behavior for general codimension, changing POD subspaces, finite precision, GMRES or FGMRES residual minimization, or convergence in the Euclidean norm at every later step. The strict one-step inequality and spectral convergence are distinct properties; eventually decreasing errors in a weighted norm are compatible with the counterexample. The result is not a claim about condition-number-optimal preconditioning.

## References
[1] X. Fan, Q. Hu, S. Zhang, *Additive reduced basis preconditioners for large-scale parametrized PDEs*, arXiv:2609.11097v1 (2026-09-10), https://arxiv.org/abs/2609.11097.

[2] B. S. Southworth and S. A. Olivier, *A note on \(2\times2\) block-diagonal preconditioning*, arXiv:2001.00711v1 (2020), https://arxiv.org/html/2001.00711v1.

[3] J. Demmel, *Nearly optimal block-Jacobi preconditioning*, SIAM J. Matrix Anal. Appl. 44 (2023), 408–413, https://doi.org/10.1137/22M1504901.

[4] *Sharp Euclidean damping frontier for weighted Jacobi on \(2\times2\) SPD systems*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-weighted-jacobi-euclidean-damping-frontier--457b47fc383f.

[5] *Sharp minimax Euclidean transient bound for two-coordinate Gauss–Seidel ordering*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-two-coordinate-gauss-seidel-euclidean-transient-threshold--21774554697b.

[6] *Additive bidirectional Gauss–Seidel inverse: exact SPD threshold and quadratic weak-coupling clustering*, published mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-additive-bidirectional-gauss-seidel-inverse--e4dd7b4e2fba.
