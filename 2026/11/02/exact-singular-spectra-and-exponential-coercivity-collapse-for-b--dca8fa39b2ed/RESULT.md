# Exact singular spectra and exponential coercivity collapse for boundary model-space quotients

## Finding

Fix a real parameter \(0<a<1\) and an integer \(N\geq1\). Write
\[
B_a(z)=\frac{z-a}{1-az},\qquad u_N=B_a^N,\qquad
K_{u_N}=H^2(\mathbb D)\ominus u_NH^2(\mathbb D).
\]
On this \(N\)-dimensional Hardy model space define the boundary difference-quotient operator
\[
Q_N f(z)=\frac{f(z)-f(1)}{z-1},
\]
with its removable value at \(z=1\). Let \(s_1(Q_N)>\cdots>s_N(Q_N)>0\) be its singular values in decreasing order. Set \(\eta=a/(1+a)\). For \(N\geq2\), let \(P_N\) be the real symmetric tridiagonal matrix with diagonal \(1+1/\eta,2,\ldots,2,1\) and both immediate off-diagonals equal to \(-1\); for \(N=1\), take \(P_1=[1/\eta]\). Its ordered positive eigenvalues are \(0<\rho_1<\cdots<\rho_N\). Then **every singular value is specified exactly** by
\[
\boxed{\displaystyle
s_k(Q_N)^2=\frac{(1+a)^2/\rho_k-a}{(1-a)^2}
}\qquad (1\leq k\leq N).
\]
In particular all singular values are simple. For each fixed positive integer \(k\),
\[
\boxed{\displaystyle
\lim_{N\to\infty}\frac{s_k(Q_N)}{N}
=\frac{2(1+a)}{\pi(1-a)(2k-1)}.
}
\]
At the *opposite* end of the same spectrum,
\[
\boxed{\displaystyle
\lim_{N\to\infty}\frac{s_N(Q_N)}{a^N}=1.
}
\]
Consequently the condition number satisfies
\[
\frac{s_1(Q_N)}{s_N(Q_N)}\sim
\frac{2(1+a)}{\pi(1-a)}N a^{-N},
\]
while all ordinary eigenvalues of \(Q_N\) equal \(a/(1-a)\), with algebraic multiplicity \(N\). The exact singular-value product is \((a/(1-a))^N\).

With \(\mathcal D_1\) denoting the local Dirichlet space equipped with squared norm \(\|f\|_{H^2}^2+\mathcal D_1(f)\), the inclusion \(K_{u_N}\hookrightarrow\mathcal D_1\) has singular values \(\sqrt{1+s_k(Q_N)^2}\) for \(1\leq k\leq N\). This is a direct quantitative application of the exact spectrum.

## Assumptions and scope

The Hardy norm is \(\|\sum_{j\geq0}c_jz^j\|_{H^2}^2=\sum_{j\geq0}|c_j|^2\). The parameter \(a\) is fixed independently of \(N\) and strictly between zero and one. The boundary point is \(1\), at which all functions of the finite Blaschke model space extend holomorphically. The singular-value notation counts singular values, not ordinary eigenvalues; the limit for \(s_k\) has fixed rank \(k\), and the opposite-edge limit refers only to \(s_N\).

The local Dirichlet integral is normalized by the local Douglas formula
\[
\mathcal D_1(f)=\left\|\frac{f(z)-f(1)}{z-1}\right\|_{H^2}^2,
\]
valid for these rational analytic functions. No assertion is made for \(a=0\), variable \(a=a_N\), or arbitrary finite Blaschke products.

## Proof

**1. A concrete orthonormal basis and the exact operator matrix.** The Takenaka–Malmquist functions
\[
e_j(z)=\frac{\sqrt{1-a^2}}{1-az}B_a(z)^j,
\qquad 0\leq j<N,
\]
are an orthonormal basis of \(K_{u_N}\). Their orthogonality follows because multiplication by the inner function \(B_a\) is isometric, and the decomposition \(K_{B_a^N}=\bigoplus_{j=0}^{N-1}B_a^j K_{B_a}\) is orthogonal. The compression of multiplication by \(B_a\) is the nilpotent shift \(J_N\), defined by \(J_Ne_j=e_{j+1}\) for \(j<N-1\) and \(J_Ne_{N-1}=0\). From
\[
z=\frac{a+B_a(z)}{1+aB_a(z)}
\]
we get for the compressed multiplication by \(z\)
\[
S_N=(aI+J_N)(I+aJ_N)^{-1}.
\]
The model space is backward-shift invariant. The boundary quotient is the restriction of \(S^*(I-S^*)^{-1}\), hence its matrix is \(X_N(I-X_N)^{-1}\), where \(X_N=S_N^*\). Finite nilpotence gives
\[
Q_N\simeq\frac{(aI+J_N^*)(I-J_N^*)^{-1}}{1-a}
=\frac{A_N^*}{1-a},
\]
where \(A_N\) has diagonal entries \(a\), entries \(1+a\) strictly below the diagonal, and zeros strictly above. Thus the claimed matrix can also be checked directly from the rational expressions for \(e_j\).

**2. An exact inverse tridiagonalization.** Put \(c=1+a\), \(\eta=a/c\), and index matrices by \(0\leq i,j<N\). Let
\[
U_{ij}=\min(i,j)+\eta.
\]
Expanding the rows of \(A_N\), one finds the exact identity
\[
A_NA_N^*+aI=c^2U.
\]
For \(i<j\), the product has \(i\) common strict-lower terms of size \(c^2\) plus \(ac\); for \(i=j\), the diagonal contribution after adding \(aI\) is \(ic^2+a^2+a=ic^2+ac\). Thus every entry with \(i\leq j\) equals \(c^2(i+\eta)\), as required. Since \(U\) is the covariance matrix of an initial variance \(\eta\) and independent unit increments, it is strictly positive and its inverse is exactly \(P_N\) specified above (verify by multiplying the tridiagonal with \(U\)). The matrix \(P_N\) is real symmetric tridiagonal with nonzero immediate off-diagonals, so all \(\rho_k\) are positive and simple. The positive eigenvalues of \(A_NA_N^*\) are \(c^2/\rho_k-a\); dividing by \((1-a)^2\) proves the exact singular formula and strict simplicity.

**3. Top fixed-rank asymptotics.** Identify \(\mathbb C^N\) isometrically with step functions on the partition of \([0,1]\) into \(N\) equal intervals. After this identification, \(A_N/N\) is the finite-rank integral operator with step kernel \(c\mathbf 1_{\{j<i\}}\) and a diagonal contribution of operator norm \(a/N\). These kernels converge in \(L^2([0,1]^2)\) to \(c\mathbf 1_{\{y<x\}}\), so the operators converge in Hilbert–Schmidt norm to \(cV\), where \((Vf)(x)=\int_0^x f(y)\,dy\). The eigenproblem for \(V^*V\) reduces to \(-g''=\lambda^{-1}g\) with a Dirichlet condition at one endpoint and a Neumann condition at the other, giving singular values \(2/[\pi(2k-1)]\). The fixed-rank singular values are continuous under operator-norm perturbations. Dividing by \(1-a\) gives the displayed limit. Also \(u_N'(1)=N(1+a)/(1-a)\), so this proves the parameter-independent sharp ratio
\[
\boxed{\displaystyle\lim_{N\to\infty}\frac{\|Q_N\|}{|u_N'(1)|}=\frac2\pi.}
\]

**4. The exponentially small last singular value.** Because \(A_N=(aI+J_N)(I-J_N)^{-1}\), its inverse has entries
\[
(A_N^{-1})_{ij}=\begin{cases}
a^{-1},&i=j,\\
(-1)^{i-j}(1+a)a^{-(i-j+1)},&i>j,\\
0,&i<j.
\end{cases}
\]
Reverse the row order of \(a^NA_N^{-1}\) and remove the alternating row/column signs using diagonal unitaries. For reversed row index \(r=N-1-i\) and column index \(t=j\), its strict-lower-triangle entries become \(c a^{r+t}\) whenever \(r+t\leq N-2\). All remaining entries lie on the anti-diagonal, where their absolute value is \(a^{N-1}\), or vanish. After zero extension to \(\ell^2(\mathbb N_0)\), this converges in Hilbert–Schmidt norm to the positive rank-one operator with matrix \(c(a^{r+t})_{r,t\geq0}\). The tail of the geometric square-sum vanishes, while the anti-diagonal contribution has Hilbert–Schmidt norm \(\sqrt N a^{N-1}\to0\). The limiting rank-one norm is \(c/(1-a^2)=1/(1-a)\). Therefore
\[
a^N\|A_N^{-1}\|\longrightarrow\frac1{1-a}.
\]
Since \(s_N(Q_N)=1/[(1-a)\|A_N^{-1}\|]\), it follows that \(s_N(Q_N)/a^N\to1\). Combining this with the top-rank law gives the condition-number asymptotic. Triangularity gives the eigenvalues and determinant assertion.

**5. Local Dirichlet interpretation.** By the local Douglas formula, \(\|f\|_{\mathcal D_1}^2=\|f\|_{H^2}^2+\|Q_Nf\|_{H^2}^2\) on the model space. The inclusion's squared singular values are consequently the eigenvalues of \(I+Q_N^*Q_N\), which are \(1+s_k(Q_N)^2\), proving the stated embedding spectrum.

## Verification

The standalone standard-library program `check.py` tests the claimed matrices using exact rational arithmetic. With \(a=1/5,1/2,3/4\), \(1\leq N\leq12\), and three rational interior evaluation points, it verifies the quotient's basis action, the inverse \(A_N^{-1}\), the covariance/inverse-tridiagonal identity, and \(A_NA_N^*+aI=c^2U\). Command: `python3 check.py`. The checker reports 2,796 exact rational assertions passed. These finite identities are cross-checks; the two infinite asymptotic statements are proved above by norm convergence and are not inferred from finite experiments.

## Relationship to prior work

Bellavita–Dellepiane–Mashreghi [1] study the same boundary quotient on general model spaces. Their Theorem 2.1 determines its ordinary spectrum from the inner-function spectrum; Theorems 2.6 and 2.8 give norm bounds. The ordinary eigenvalue \(a/(1-a)\) here is therefore an instance of their theorem, **not** a novelty claim. Their discussion of local Dirichlet spaces provides the natural motivation for the singular-value problem. Theorem 1.1 of Bellavita–Dellepiane [2] establishes whether a model space embeds into a local Dirichlet space, rather than exact approximation numbers for the power-Blaschke sequence. In related nonnormal matrix analysis, Greenbaum–Kyanfar–Salemi [3] study rank-one-like resolvents and qualitative small-singular behavior for finite Toeplitz matrices, but do not provide the stated tridiagonal spectrum, fixed-rank constants and exact exponentially small endpoint for these boundary model-space quotients.

The new content asserted here is the **complete singular-value formula** and the paired opposite-edge asymptotics with constants, together with the resulting exact local-Dirichlet inclusion spectrum. The transformation to a nilpotent Jordan matrix, standard Volterra singular values, and ordinary spectrum are used as ingredients rather than represented as independently new discoveries. Equivalent results under different finite Toeplitz normalizations remain a possible historical-priority risk.

## Limitations

The location \(a\) is real, positive, and fixed. The formula is not asserted uniformly as \(a\downarrow0\) or \(a\uparrow1\), and is not extended to arbitrary zero configurations, complex parameter paths, arbitrary boundary points, or singular inner functions. Only the two opposite spectral regimes (fixed top rank and the bottom singular value) are analyzed asymptotically; the finite tridiagonal formula nevertheless determines all intermediate ranks. Published-history completeness cannot be guaranteed, and no independent mathematical validation has been performed.

## References

[1] C. Bellavita, E. A. Dellepiane, and J. Mashreghi, *The spectral analysis of the difference quotient operator on model spaces*, arXiv:2410.18623v1, first posted 2024-10-24, https://arxiv.org/abs/2410.18623 .

[2] C. Bellavita and E. A. Dellepiane, *Embedding model and de Branges–Rovnyak spaces in Dirichlet spaces*, arXiv:2310.03604v1, first posted 2023-10-05, https://arxiv.org/abs/2310.03604 .

[3] A. Greenbaum, F. Kyanfar, and A. Salemi, *When is the Resolvent Like a Rank One Matrix?*, arXiv:2501.07686v1, first posted 2025-01-13, https://arxiv.org/abs/2501.07686 .
