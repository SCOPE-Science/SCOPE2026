# Exact Hessian recovery inside a Q-order-one BFGS trajectory
## Finding
For the specific nonterminating exact-line-search BFGS trajectory constructed by Liu, Li, and Wen, the BFGS Hessian approximations recover the true Hessian in the full operator norm:
\[
\|B_k-\nabla^2F(0)\|_{\mathrm{op}}=\|B_k-I_n\|_{\mathrm{op}}\longrightarrow 0.
\]
This occurs on the same trajectory for which the adjacent iterate errors are Q-superlinear but have minimum Q-order one: no fixed exponent \(p>1\) controls all sufficiently late adjacent errors. Thus the Q-order-one phenomenon persists even when the entire quasi-Newton matrix, not only its action along the current search direction, converges to the exact Hessian.

More precisely, write \(V\) for the two-dimensional active subspace in the construction and \(C_k=B_k|_V\). For \(k\ge1\),
\[
\det C_{k+1}
=
\frac{s_k^\top y_k}{\|s_k\|_2^2}
\frac{\|y_{k-1}\|_2^2}{s_{k-1}^\top y_{k-1}},
\]
and both factors tend to one.

## Assumptions and scope
The statement concerns the explicit \(C^\infty\), globally strongly convex objective and exact-line-search BFGS orbit from arXiv:2609.00596. The construction has unique minimizer \(0\), satisfies \(\nabla^2F(0)=I_n\), uses \(B_0=I_n\), and evolves in a fixed two-dimensional subspace \(V\), with \(B_k=C_k\oplus I_{V^\perp}\). The source constructs sequences \(g_k\), \(\Delta_k\), and \(x_k=g_k+\Delta_k\), where \(\nabla F(x_k)=g_k\), \(r_k=\|g_k\|_2\), \(\|\Delta_k\|_2=|\delta_k|\), \(|\delta_k|/r_k\to0\), and \(r_{k+1}/r_k\to0\).

The finding is an asymptotic matrix-convergence statement for this particular counterexample. It does not assert a matrix-convergence theorem for arbitrary BFGS trajectories.

## Proof
Set \(s_k=x_{k+1}-x_k\) and \(y_k=g_{k+1}-g_k\). Because \(x_k=g_k+\Delta_k\),
\[
y_k-s_k=\Delta_k-\Delta_{k+1}.
\]
The source proves \(\|x_k\|_2=r_k(1+o(1))\) and \(\|x_{k+1}\|_2/\|x_k\|_2\to0\). Hence
\[
\frac{\|s_k\|_2}{r_k}\to1.
\]
Moreover,
\[
\frac{\|y_k-s_k\|_2}{r_k}
\le
\frac{|\delta_k|}{r_k}
+
\frac{|\delta_{k+1}|}{r_{k+1}}
\frac{r_{k+1}}{r_k}
\longrightarrow0.
\]
Therefore
\[
\frac{\|y_k-s_k\|_2}{\|s_k\|_2}\to0,
\qquad
\frac{s_k^\top y_k}{\|s_k\|_2^2}\to1,
\qquad
\frac{\|y_k\|_2^2}{s_k^\top y_k}\to1.
\]

Now restrict to \(V\). The source's two-dimensional realization gives the secant relation \(C_k s_{k-1}=y_{k-1}\) and the exact orthogonality \(y_{k-1}^\top s_k=0\). Let
\[
u=\frac{s_{k-1}}{\|s_{k-1}\|_2},
\]
and choose an orthonormal basis \((u,v)\) of \(V\). Write
\[
\frac{y_{k-1}}{\|s_{k-1}\|_2}=(a,c)
\]
in this basis. Symmetry and the secant relation imply
\[
C_k=
\begin{pmatrix}
a&c\\
c&d
\end{pmatrix}.
\]
Since \(s_k\) is orthogonal to \(y_{k-1}\), its unit direction is, up to sign,
\[
w=\frac{(-c,a)}{\sqrt{a^2+c^2}}.
\]
A direct multiplication gives
\[
w^\top C_k w
=
\frac{a\det C_k}{a^2+c^2}
=
\det C_k\,
\frac{s_{k-1}^\top y_{k-1}}{\|y_{k-1}\|_2^2}.
\]
Consequently,
\[
s_k^\top C_k s_k
=
\|s_k\|_2^2\det C_k
\frac{s_{k-1}^\top y_{k-1}}{\|y_{k-1}\|_2^2}.
\]

For a Hessian-form BFGS update, the determinant identity is
\[
\det C_{k+1}
=
\det C_k\frac{s_k^\top y_k}{s_k^\top C_k s_k}.
\]
Substituting the previous expression cancels \(\det C_k\) and yields the exact formula
\[
\det C_{k+1}
=
\frac{s_k^\top y_k}{\|s_k\|_2^2}
\frac{\|y_{k-1}\|_2^2}{s_{k-1}^\top y_{k-1}}.
\]
The two limits established above show \(\det C_{k+1}\to1\).

Finally, use the orthonormal basis whose first vector is \(s_k/\|s_k\|_2\). The new secant relation \(C_{k+1}s_k=y_k\) says that the first column of \(C_{k+1}\) is \(y_k/\|s_k\|_2\), which converges to \((1,0)^\top\). Thus, writing
\[
C_{k+1}=
\begin{pmatrix}
a_k&c_k\\
c_k&d_k
\end{pmatrix},
\]
we have \(a_k\to1\) and \(c_k\to0\). Since \(\det C_{k+1}\to1\),
\[
d_k=\frac{\det C_{k+1}+c_k^2}{a_k}\to1.
\]
Therefore \(\|C_{k+1}-I_V\|_{\mathrm{op}}\to0\). The source has \(B_k=C_k\oplus I_{V^\perp}\), so
\[
\|B_k-I_n\|_{\mathrm{op}}\to0.
\]
The final localization/scaling step of the source preserves the BFGS matrices and has \(\nabla^2F(0)=I_n\), completing the claim.

## Verification
The proof uses only exact identities from the constructed trajectory and the standard BFGS determinant identity. The critical index shift was checked explicitly: the source gives \(y_k^\top s_{k+1}=0\), hence \(y_{k-1}^\top s_k=0\) in the determinant argument. Positivity of all denominators follows from positive definiteness of \(C_k\) and strong convexity, which give \(s_k^\top C_k s_k>0\) and \(s_k^\top y_k>0\).

No finite numerical experiment is used to establish the asymptotic statement.

## Relationship to prior work
Liu, Li, and Wen prove that their exact-line-search BFGS trajectory is nonterminating, Q-superlinear, and has minimum adjacent-iterate Q-order one. Their theorem also gives \(\nabla^2F(0)=I_n\), while the construction proves positive definiteness and the block form \(B_k=C_k\oplus I_{V^\perp}\). The inspected source does not state that \(B_k\) converges to \(I_n\).

Classical Dennis-Moré theory characterizes superlinear quasi-Newton convergence through a directional approximation condition; that condition does not by itself require full operator-norm convergence of the approximate Hessians. The result here is stronger for this particular trajectory because it proves convergence of the whole matrix.

Jin, Jiang, and Mokhtari derive non-asymptotic linear and superlinear convergence rates for exact-line-search BFGS and record the same determinant identity used above. Their rate analysis does not cover the present implication that the Liu-Li-Wen Q-order-one counterexample simultaneously has full Hessian-matrix recovery.

## Limitations
The conclusion is specific to the two-dimensional active-subspace construction of arXiv:2609.00596. No rate is claimed for \(\|B_k-I_n\|_{\mathrm{op}}\), and no analogous statement is proved here for arbitrary smooth strongly convex objectives, inexact line search, limited-memory BFGS, or dimensions in which the active subspace grows. Targeted searches did not identify a published statement of this exact matrix-recovery property, but absence from the searched sources is not a proof of historical novelty.

## References
1. B. Liu, C. Li, and Z. Wen, “The Minimum Q-Order of BFGS with Exact Line Search Is One,” arXiv:2609.00596v1, 2026.
2. J. E. Dennis, Jr. and J. J. Moré, “A characterization of superlinear convergence and its application to quasi-Newton methods,” Mathematics of Computation 28 (1974), 549–560.
3. Q. Jin, R. Jiang, and A. Mokhtari, “Non-asymptotic global convergence rates of BFGS with exact line search,” Mathematical Programming 219 (2026), 667–704, DOI 10.1007/s10107-025-02256-7.
