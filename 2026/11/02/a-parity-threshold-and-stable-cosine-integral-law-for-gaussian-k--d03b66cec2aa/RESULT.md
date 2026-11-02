# A parity threshold and stable cosine-integral law for Gaussian kernels on sunlet graph metrics

## Finding
For every integer \(n\ge3\), let \(S_n=C_n\odot K_1\) be the sunlet graph, with one leaf at each cycle vertex and the unweighted shortest-path distance \(d_n\). Define \(\wp_n\) as the supremum of exponents \(p\ge0\) for which the matrix \(D_p=[d_n(x,y)^p]_{x,y\in V(S_n)}\) is conditionally negative semidefinite. Then
\[
\wp_n=1\quad(n\text{ even}),\qquad 1<\wp_n<2\quad(n\text{ odd}),
\]
and the odd-order transition has the sharp asymptotic
\[
\boxed{\lim_{\substack{n\to\infty\\n\text{ odd}}} n^2(\wp_n-1)
=\frac{2\pi^2}{\operatorname{Cin}(2\pi)}=8.0976273568\ldots},\qquad
\operatorname{Cin}(x)=\int_0^x\frac{1-\cos u}{u}\,du.
\]
Equivalently, the Gaussian-type kernel \(K_{t,p}(x,y)=\exp(-t d_n(x,y)^p)\) is positive semidefinite for **every** \(t>0\) exactly for \(0\le p\le\wp_n\). The leading odd-order coefficient coincides with that of *undecorated* odd cycles; the contribution here is its persistence after adding pendant vertices, as well as the complete two-orbit finite-order test. The value of the finite-order threshold need not coincide with that of the bare cycle.

## Assumptions and scope
Vertices are \(r_j\) (cycle vertices) and \(l_j\) (leaves), indexed by \(j\in\mathbb Z/n\mathbb Z\). Set \(a_j=\min\{j,n-j\}\) for \(1\le j<n\). Distinct-site distances are \(d_n(r_i,r_j)=a_{i-j}\), \(d_n(r_i,l_j)=a_{i-j}+1\), \(d_n(l_i,l_j)=a_{i-j}+2\), and \(d_n(r_i,l_i)=1\). All diagonal distances are zero. Conditional negative semidefiniteness means \(\sum_{x,y}z_xd_n(x,y)^pz_y\le0\) for every real \(z\) with \(\sum_x z_x=0\). Complexified Hermitian testing is equivalent because the distance matrix is real symmetric. At \(p=0\), distinct-point distances have power one and diagonal entries zero.

For \(1\le k<n\) define the real scalars
\[
\begin{aligned}
 A_{n,k}(p)&=\sum_{j=1}^{n-1}a_j^p\cos(2\pi kj/n),\\
 E_{n,k}(p)&=1+\sum_{j=1}^{n-1}[(a_j+1)^p-a_j^p]\cos(2\pi kj/n),\\
 L_{n,k}(p)&=-2+\sum_{j=1}^{n-1}[a_j^p-2(a_j+1)^p+(a_j+2)^p]\cos(2\pi kj/n).
\end{aligned}
\]
Use the same definition for \(L_{n,0}\). The exact finite-order criterion is \(L_{n,0}(p)\le0\) together with negative semidefiniteness of each \(H_{n,k}(p)=\bigl(\begin{smallmatrix}A_{n,k}(p)&E_{n,k}(p)\\E_{n,k}(p)&L_{n,k}(p)\end{smallmatrix}\bigr)\) for \(1\le k\le\lfloor n/2\rfloor\). This criterion applies at every real \(p\ge0\) and specifies the threshold without any unproved root-uniqueness assumption.

## Proof
**1. Fourier reduction.** Write a zero-total-mass test vector as \(z(r_i)=u_i-v_i\), \(z(l_i)=v_i\). Its constraint is exactly \(\sum_i u_i=0\). Expanding the distance quadratic form gives circulant coefficient arrays: root/root coefficient \(a_j^p\) off the diagonal; root/leaf-minus-root coefficient \((a_j+1)^p-a_j^p\) away from zero and \(1\) at zero; leaf-minus-root coefficient \(a_j^p-2(a_j+1)^p+(a_j+2)^p\) away from zero and \(-2\) at zero. Discrete Fourier diagonalization yields the matrices \(H_{n,k}\). At frequency zero the \(u\)-coordinate is disallowed and only \(L_{n,0}\) remains. Conjugate modes have the same eigenvalues; testing \(1\le k\le\lfloor n/2\rfloor\) suffices.

**2. The exponent-one parity boundary.** At \(p=1\), every Fourier cross term vanishes and every \(L_{n,k}(1)=-2\), including zero. Direct summation of the cycle distance sequence gives, for \(1\le k<n\),
\[
A_{n,k}(1)=\begin{cases}
0,&n\text{ even and }k\text{ even},\\
-1/\sin^2(\pi k/n),&n\text{ even and }k\text{ odd},\\
-1/[4\cos^2(\pi k/(2n))],&n\text{ odd and }k\text{ even},\\
-1/[4\sin^2(\pi k/(2n))],&n\text{ odd and }k\text{ odd}.
\end{cases}
\]
Thus \(D_1\) is conditionally negative semidefinite for every \(n\), strictly so for odd \(n\), and not strictly so for even \(n\). If a metric has \(p\)-negative type at \(p>1\), it has strict 1-negative type (Li--Weston's strict-exponent theorem). Hence \(\wp_n=1\) for even \(n\). For odd \(n\), strictness and finiteness give an interval of exponents above one by continuity. At \(p=2\), \(L_{n,0}(2)=-2+2(n-1)=2(n-2)>0\), hence \(\wp_n<2\) for odd \(n\). The negative-type exponent set is downward closed and closed for finite metrics; its upper endpoint is included.

**3. Scaling of odd-cycle Fourier modes.** Now let \(n\) be odd, \(p_n=1+c/n^2\) with fixed \(c>0\), and set \(f(u)=\min(u,1-u)\log\min(u,1-u)\), continuously extended by zero at the endpoints. Taylor's theorem, uniformly in \(k\ne0\), yields
\[
A_{n,k}(p_n)=A_{n,k}(1)+\frac{c\log n}{n^2}A_{n,k}(1)+cJ_{n,k}
+O_c(\log^2n/n^2),\quad
J_{n,k}=\frac1n\sum_{j=1}^{n-1}f(j/n)\cos(2\pi kj/n).
\]
For each fixed positive \(k\), Riemann sums give \(J_{n,k}\to J_k=2\int_0^{1/2}u\log u\cos(2\pi ku)\,du\). The bounded variation of \(f\), combined with the geometric-sum bound for partial sums of discrete roots of unity, gives \(|J_{n,k}|\le C/k\) uniformly for \(1\le k\le n/2\). The exact exponent-one formula implies \(A_{n,k}(1)\le-1/4\) for all odd \(n\) and \(1\le k\le n/2\), while \(A_{n,k}(1)\to-1/4\) for each fixed even \(k\), and \(A_{n,k}(1)\to-\infty\) for each fixed odd \(k\).

For \(k=2r\), integration by parts gives the positive coefficient
\[
J_{2r}=\frac{\operatorname{Cin}(2\pi r)}{8\pi^2r^2}.
\]
This is strictly largest at \(r=1\): indeed \(\operatorname{Cin}(2\pi r)\le\operatorname{Cin}(2\pi)+2\log r\), and \(\operatorname{Cin}(2\pi)>1\) together with \(2\log r<r^2-1\) for \(r\ge2\) proves the claim. The limiting first even frequency is therefore \(A_{n,2}(p_n)\to-1/4+cJ_2\), changing sign at \(c_*=1/(4J_2)=2\pi^2/\operatorname{Cin}(2\pi)\).

For any fixed \(c<c_*\), choose a finite mode cutoff \(K\) so large that \(cC/K<1/8\). Fixed modes \(k\le K\) have strictly negative limits or diverge negatively by the preceding formulas; higher modes satisfy \(A_{n,k}(p_n)\le-1/4+cC/K+o(1)<0\), because the logarithmic multiple of \(A_{n,k}(1)\) is nonpositive. Thus all root-mode diagonal entries are uniformly negative for large odd \(n\). Finally the elementary mean-value bound on first differences and the integral bound on second differences give, uniformly in \(k\),
\[
|E_{n,k}(p_n)|=O_c(\log n/n),\qquad L_{n,k}(p_n)=-2+O_c(\log n/n^2).
\]
The same estimate applies to \(L_{n,0}\). Hence all nonzero-mode blocks are negative definite and the zero mode is negative, proving \(p_n\le\wp_n\) for large odd \(n\). For every \(c>c_*\), \(A_{n,2}(p_n)>0\) for sufficiently large odd \(n\), violating negative type. Squeezing \(c\) on both sides proves the asserted limit. In particular, the pendant-root cross blocks do not alter the leading odd-cycle constant even though finite-order thresholds change.

**4. Kernel equivalence.** Schoenberg's theorem says that \(\exp(-tD_p)\) is positive semidefinite for every \(t>0\) if and only if \(D_p\) is conditionally negative semidefinite. Applied to the metric powers above, this transfers the threshold exactly to the claimed Gaussian-type family.

## Verification
The accompanying standard-library script `check_sunlet.py` recomputes the Fourier symbols from independent full \(2n\)-vertex distance matrices, tests the closed exponent-one spectra, brackets finite-order thresholds, and compares the scaled odd-order thresholds against the cosine-integral constant. It passed 4,377 explicit assertion groups in one run. These finite computations test the identities and numerical convergence but do not prove the asymptotic or uniqueness of historical coverage; those depend on the argument above and the literature comparison.

## Relationship to prior work
Li and Weston provide the strict-exponent implication used for the parity boundary. Sánchez provides the general finite-metric matrix approach to supremal negative type, with a complete bipartite example; the present two-orbit sunlet symbol is a separate explicit classification. Murugan studies generalized roundness of vertex-transitive graphs, including cycles; sunlets are not vertex-transitive. The cosine-integral coefficient also occurs for undecorated odd cycles. Consequently the numerical constant itself is **not** asserted to be new: the new assertion is its survival after adding a leaf to *every* cycle vertex, established via an explicit coupled Fourier block and a uniform all-frequency argument.

## Limitations
The theorem treats the unweighted sunlet family only; unequal leaf lengths and nonuniform attachments are not covered. The finite-order thresholds for odd \(n\) are defined by the exact Fourier inequalities, not asserted to have a universal radical formula. No independent mathematical validation has been performed. Older general negative-type or graph-metric literature might contain an equivalent decorated-cycle theorem not identified in the bounded comparison.

## References
- H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first posted 2009-01-06), https://arxiv.org/abs/0901.0695.
- S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first posted 2011-08-02), https://arxiv.org/abs/1108.0451.
- M. K. Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657 (first posted 2011-12-23), https://arxiv.org/abs/1112.5657.
- I. J. Schoenberg, *Metric spaces and positive definite functions*, Transactions of the American Mathematical Society 44 (1938), 522–536.
