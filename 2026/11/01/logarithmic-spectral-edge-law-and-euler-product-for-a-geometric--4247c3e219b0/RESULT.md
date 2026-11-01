# Logarithmic spectral edge law and Euler product for a geometric random-walk polynomial hypergroup

## Finding

Fix a real number \(q\geq5\). Define the random-walk polynomial sequence by \(P_0(x)=1\), \(P_1(x)=x\), and, for every integer \(n\geq1\),
\[
xP_n(x)=a_nP_{n+1}(x)+c_nP_{n-1}(x),\qquad a_n=1-c_n,
\]
where \(c_{2k-1}=1-q^{-(2k-1)}\) and \(c_{2k}=q^{-2k}\) for \(k\geq1\). Write \(\mu_q\) for its probability orthogonality measure. Its support is \(\{-1,1\}\cup\{\pm x_j(q):j\geq1\}\), where the positive interior points are simple and satisfy \(0<x_1(q)<x_2(q)<\cdots<1\) and \(x_j(q)\to1\).

The **squared-distance edge counting law** is
\[
N_q(\epsilon):=\#\{j\geq1:1-x_j(q)^2\geq\epsilon\}
=\frac{\log(1/\epsilon)}{2\log q}+O_q(1)
\quad(\epsilon\downarrow0).
\]
The exact additive and multiplicative spectral identities are
\[
\boxed{\displaystyle\sum_{j=1}^{\infty}(1-x_j(q)^2)=\frac{q^2+q-1}{q(q^2-1)}}
\]
and
\[
\boxed{\displaystyle\prod_{j=1}^{\infty}x_j(q)^2
=\prod_{n=1}^{\infty}(1-q^{-n})>0.}
\]
The product includes **one** representative of each positive spectral pair. These identities are statements about spectral locations, not about the point masses of \(\mu_q\).

## Assumptions and scope

The real parameter satisfies \(q\geq5\); all indices \(n,k,j\) are integers in the displayed ranges. The normalization is \(P_n(1)=1\) and \(\mu_q(\mathbb R)=1\). This recurrence belongs to the positive-linearization family of Kahler--Obermaier: setting \(s_n=q^{-n}\), their hypotheses hold because \(q^2-4q-2>0\) for \(q\geq5\), and the initial strict condition also holds. Only the original, not the switched-coefficient, recurrence is analyzed here.

The topological support includes the limit points \(\pm1\), but these are not spectral atoms. The asymptotic count is for \(\epsilon\to0^+\) with fixed \(q\); it is not asserted uniform in \(q\).

## Proof

**1. Jacobi representation and its parity block.** Set \(a_0=1\), \(h(0)=1\), and \(h(n)=\prod_{m=1}^n a_{m-1}/c_m\) for \(n\geq1\). Then \(p_n=\sqrt{h(n)}P_n\) are orthonormal. Multiplication by \(x\) in \(L^2(\mu_q)\) is unitarily represented by the zero-diagonal Jacobi operator \(J\) on \(\ell^2(\mathbb N_0)\), whose edge weight between \(n-1\) and \(n\) is \(\alpha_n=\sqrt{a_{n-1}c_n}\).

Because the corresponding tridiagonal random-walk transition operator is reversible with weights \(h(n)\) and stochastic, Jensen's inequality gives \(\|J\|\leq1\). Rearranging the basis into even and odd coordinates gives
\[
J=\begin{pmatrix}0&A^*\\A&0\end{pmatrix},
\]
where \(A\) is upper bidiagonal, with diagonal \(\beta_k\) and superdiagonal \(\gamma_k\):
\[
\beta_0^2=1-q^{-1},\quad
\beta_k^2=(1-q^{-2k})(1-q^{-(2k+1)})\ (k\geq1),
\qquad \gamma_k=q^{-(2k+3/2)}\ (k\geq0).
\]
Here \(\inf_k\beta_k=\sqrt{1-q^{-1}}>q^{-3/2}=\sup_k\gamma_k\). Thus diagonal-plus-shift factorization and a Neumann series show that \(A\) is invertible; in particular \(0\) is absent from the spectrum of \(J\).

**2. Exact trace and determinant.** Let \(D=I-A^*A\). It is nonnegative by \(\|J\|\leq1\). Its only nonzero matrix entries are
\[
D_{00}=q^{-1},\qquad
D_{kk}=(1+q^{-1})q^{-2k}-(q+q^{-1})q^{-4k}\quad(k\geq1),
\]
and \(D_{k,k+1}=D_{k+1,k}=-\beta_k\gamma_k\) for \(k\geq0\). These entries are absolutely summable, so \(D\) is trace class. Its trace is the elementary geometric series
\[
\operatorname{tr}D=q^{-1}+\frac{1+q^{-1}}{q^2-1}-\frac{q+q^{-1}}{q^4-1}
=\frac{q^2+q-1}{q(q^2-1)}.
\]
Also \(A-I\) is trace class because \(\sum_k|\beta_k-1|+\sum_k\gamma_k<\infty\). For each upper-left finite compression, its determinant is the product of diagonal entries. Convergence in trace norm therefore yields the Fredholm determinant
\[
\det A=\prod_{k=0}^{\infty}\beta_k,\qquad
\det(A^*A)=\prod_{k=0}^{\infty}\beta_k^2
=(1-q^{-1})\prod_{k=1}^{\infty}(1-q^{-2k})(1-q^{-(2k+1)})
=\prod_{n=1}^{\infty}(1-q^{-n}).
\]
The determinant is strictly positive because \(\sum_nq^{-n}<\infty\).

**3. Identifying all spectral points.** The nonzero off-diagonals of \(D\) make its eigenspaces at most one dimensional (each eigenvector is determined recursively by its first coordinate). Similarly, all eigenvectors of \(J\) must have nonzero first coordinate, so the cyclic spectral measure of the first coordinate contains every eigenvalue. Since \(D\) is compact, the only possible accumulation points of \(\sigma(J)\) are \(\pm1\). To exclude atoms there, note that a formal eigenvector of \(J\) at \(\pm1\) is \((\pm1)^n\sqrt{h(n)}\). But
\[
h(2k)=\frac{q^{k+1}}{q-1}\prod_{j=1}^{k-1}\frac{1-q^{-2j}}{1-q^{-(2j+1)}}\quad(k\geq1),
\]
which grows like a positive multiple of \(q^k\). The formal eigenvectors are not square summable. Hence \(\pm1\) are not eigenvalues. Therefore \(D\) has no zero eigenvalue and its strictly positive eigenvalues \(\delta_1>\delta_2>\cdots\downarrow0\) correspond bijectively to the positive spectral points of \(J\) by \(\delta_j=1-x_j(q)^2\), counted in decreasing order. Invertibility of \(A\) makes \(0<x_j(q)\). The trace and Fredholm determinant in Step 2 now prove the two exact spectral identities.

**4. Quantitative edge law.** Put \(W=\operatorname{diag}(q^{-2k})_{k\geq0}\). The factorization
\[
D=W^{1/2}CW^{1/2}
\]
defines a bounded self-adjoint tridiagonal \(C\), with
\[
C_{00}=q^{-1},\quad
C_{kk}=1+q^{-1}-(q+q^{-1})q^{-2k}\ (k\geq1),\quad
C_{k,k+1}=-q^{-1/2}\beta_k.
\]
Since \(D\geq0\) and finite-support sequences lie in the range of \(W^{1/2}\), \(C\geq0\). Its diagonal converges to \(1+q^{-1}\), and its off-diagonal converges to \(-q^{-1/2}\). Thus \(C\) is a compact perturbation of the constant-coefficient half-line Jacobi operator, whose essential spectrum is
\[
[(1-q^{-1/2})^2,(1+q^{-1/2})^2].
\]
This interval is bounded away from zero.

Define \(u_k=q^{-k}\sqrt{h(2k)}\). The displayed Haar-weight formula shows \(u\in\ell^2\). Substituting the identity \(P_n(1)=1\) into the original recurrence gives \(Cu=0\) coordinatewise. Since all off-diagonal entries of \(C\) are nonzero, any vector in \(\ker C\) is determined by its first coordinate: \(\ker C=\operatorname{span}\{u\}\). Consequently zero is an isolated simple eigenvalue and there are constants \(0<c_q<M_q<\infty\) such that
\[
c_q(I-\Pi_u)\leq C\leq M_qI,
\]
where \(\Pi_u\) projects orthogonally onto \(u\). Multiplying by \(W^{1/2}\) gives
\[
c_q(W-W^{1/2}\Pi_u W^{1/2})\leq D\leq M_qW.
\]
The operator subtracted from \(W\) has rank one. By the min--max principle and rank-one eigenvalue interlacing, its \(j\)-th decreasing eigenvalue is at least the \((j+1)\)-st eigenvalue \(q^{-2j}\) of \(W\). Since the \(j\)-th eigenvalue of \(W\) is \(q^{-2(j-1)}\),
\[
c_qq^{-2j}\leq\delta_j\leq M_qq^{-2(j-1)}\quad(j\geq1).
\]
These matching geometric bounds imply \(\#\{j:\delta_j\geq\epsilon\}=\log(1/\epsilon)/(2\log q)+O_q(1)\) as \(\epsilon\downarrow0\). This completes the proof.

## Verification

A self-contained Python checker verifies exact coefficient and Haar-recursion identities for representative rational \(q\), the finite-dimensional traces, and finite products against the stated infinite geometric expressions with rigorous analytic tail estimates. It also checks finite tridiagonal eigenvalue ratios as supplementary numerical diagnostics. Finite computations are not used to establish the infinite-dimensional spectral theorem. The analytical arguments above provide convergence, the rank-one comparison, and the full spectral identification.

## Relationship to prior work

Kahler and Obermaier [1], Section 2, construct the geometric example \(s_n=5^{-n}\) with positive polynomial-product linearization; Section 4 establishes the qualitative description of its discrete spectral support converging to \(\pm1\). They do not state the logarithmic counting coefficient or either of the two all-spectrum sum/product identities. Their recurrence is precisely the starting point here, not an independent discovery. Młotkowski and Szwarc [2] prove general discrete-support results under alternating Jacobi-coefficient hypotheses, but their qualitative accumulation statement does not supply these quantitative expressions. Kahler and Szwarc [3] analyze hypergroup Haar measures and dual spaces for other polynomial families, not the geometric spectral identities proved here.

## Limitations

The result concerns this one-parameter geometric recurrence with \(q\geq5\). It does not compute individual spectral atoms or their masses, an exact formula for the points \(x_j(q)\), a relative asymptotic \(1-x_j(q)^2\sim C_q q^{-2j}\), a uniform \(q\)-dependent error bound, or the spectrum of the switched-coefficient recurrence. No claim of independence from all possible unindexed special-function formulae is made. Independent validation has not been performed.

## References

[1] S. Kahler and J. Obermaier, *A new class of orthogonal polynomials*, arXiv:2603.17983v1, first posted 2026-03-18, §§2 and 4, https://arxiv.org/html/2603.17983v1.

[2] W. Młotkowski and R. Szwarc, *Nonnegative Linearization for Polynomials Orthogonal with Respect to Discrete Measures*, 2001, Section 5, qualitative discrete spectra.

[3] S. Kahler and R. Szwarc, *Dual spaces vs. Haar measures of polynomial hypergroups*, arXiv:2212.11229, especially its dual-space and Haar-measure classification.

[4] W. Rudin, *Functional Analysis*, standard facts concerning compact self-adjoint operators and the min--max principle (methodological reference, not claimed as an originality source).
