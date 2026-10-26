# Exact four-outlier Fourier sampling spectra under a symmetric two-node collision

## Finding
Let \(N=2n+1\ge5\) be odd, let \(h=2\pi/N\), and choose \(0<\delta<h/2\). Take the nodes \(x_0=\delta\), \(x_1=h-\delta\), and \(x_j=jh\) for \(2\le j<N\). The square trigonometric evaluation matrix is
\[
F_{jk}=N^{-1/2}e^{ikx_j},\qquad 0\le j<N,\quad -n\le k\le n.
\]
Write \(D_n(t)=\sum_{k=-n}^ne^{ikt}=\sin(Nt/2)/\sin(t/2)\), with its continuous values at multiples of \(2\pi\), and put
\[
a=\frac{D_n(\delta)}N,\qquad b=\frac{D_n(h-\delta)}N,\qquad c=\frac{D_n(h-2\delta)}N.
\]
The **complete multiset of eigenvalues** of \(FF^*\) consists of \(N-4\) copies of \(1\) together with, for each \(s\in\{+1,-1\}\), the two numbers
\[
\boxed{\lambda_{s,\pm}=\frac{2+sc\ \pm\sqrt{(2+sc)^2-4(a+sb)^2}}2.}
\]
All are strictly positive. Thus a two-node symmetric perturbation of an exact Fourier grid changes at most four Gram eigenvalues, and the displayed expressions give **all** singular values of \(F\) by taking positive square roots.

Put \(\eta=1-2\delta/h\), the separation of the two mobile nodes divided by the original mesh spacing. Then as \(\eta\downarrow0\) with fixed odd \(N\),
\[
\boxed{\sigma_{\min}(F)=K_N\eta+O_N(\eta^3),\qquad
K_N=\frac{\pi\cos(\pi/(2N))}{N^2\sin^2(\pi/(2N))}.}
\]
Also
\[
\boxed{\operatorname{cond}_2(F)=\frac{C_N}{\eta}+O_N(\eta),\qquad
C_N=\frac{1}{K_N}\sqrt{\frac{3+\sqrt{9-16d_N^2}}2},\quad
 d_N=\frac1{N\sin(\pi/(2N))}.}
\]
The constants converge to the explicit, strictly positive universal limits
\[
\lim_{N\to\infty}K_N=\frac4\pi,
\qquad \lim_{N\to\infty}C_N=
\boxed{\frac\pi4\sqrt{\frac{3+\sqrt{9-64/\pi^2}}2}=1.1893033136798503\ldots.}
\]
These are limits of exact, dimension-dependent sharp leading coefficients, not merely two-sided estimates. At the excluded collision point \(\eta=0\), the matrix becomes singular: its limiting Gram spectrum is \(N-4\) unit eigenvalues, the pair \(\tfrac12(3\pm\sqrt{9-16d_N^2})\), and \(\{0,1\}\).

## Assumptions and scope
Everything is for odd \(N\ge5\), real \(0<\delta<\pi/N\), the **complete** consecutive Fourier frequency set \(\{-n,\ldots,n\}\), and the unitary normalization \(N^{-1/2}\). Here \(\operatorname{cond}_2(F)\) means the ratio of the largest to smallest singular value. No weights, undersampling, generic node perturbations, or even Fourier orders are asserted. The collision point itself is excluded from invertibility statements. The limiting \(N\to\infty\) constant is taken after the fixed-\(N\) small-separation asymptotic.

## Proof
Start with the unitary discrete Fourier evaluation matrix \(U\) at the original nodes \(jh\). Right multiplication of the perturbed matrix \(F\) by \(U^*\) preserves all singular values. By discrete Fourier orthogonality, \(T=FU^*\) has lower \(N-2\) rows equal to the corresponding rows of the identity and upper two rows given by trigonometric cardinal interpolation coefficients. Partition its columns and rows according to the first two and remaining \(N-2\) grid sites:
\[
T=\begin{pmatrix}A&B\\0&I_{N-2}\end{pmatrix},\qquad
A=\begin{pmatrix}a&b\\b&a\end{pmatrix}.
\]
The upper rows of \(T\) are normalized Fourier evaluation vectors. Their squared norms are \(1\) and their inner product is \(c\). It follows exactly that
\[
BB^*=\begin{pmatrix}1-a^2-b^2&c-2ab\\c-2ab&1-a^2-b^2\end{pmatrix}.
\]
The symmetric/antisymmetric two-vector basis simultaneously diagonalizes \(A\) and \(BB^*\). In the parity sector \(s=\pm1\), the eigenvalues of \(A\) and \(BB^*\) are respectively
\[
\alpha_s=a+sb,\qquad \gamma_s=1+sc-(a+sb)^2\ge0.
\]
As \(B\) has only two rows, the orthogonal complement of its row space contributes \(N-4\) unit singular values (counted with multiplicity). In each parity sector the remaining squared singular values equal those of the triangular matrix
\[
\begin{pmatrix}\alpha_s&\sqrt{\gamma_s}\\0&1\end{pmatrix};
\]
its squared singular-value characteristic polynomial is
\[
\lambda^2-(2+sc)\lambda+(a+sb)^2.
\]
This proves the complete spectrum and the reality of its radicals without numerical assumptions. Since \(0<\delta<h/2\),
\[
\frac{b}{a}=\frac{\sin(\delta/2)}{\sin((h-\delta)/2)}\in(0,1).
\]
Therefore \(a>b>0\), both parity-sector determinants are positive, and all singular values are nonzero.

For the collision asymptotics, \(\delta=(h/2)(1-\eta)\) and \(D_n(h/2)=1/\sin(\pi/(2N))\). Differentiating \(D_n(t)\) gives
\[
D_n'(h/2)=-\frac{\cos(\pi/(2N))}{2\sin^2(\pi/(2N))}.
\]
Taylor expansion about the midpoint consequently yields
\[
a-b=K_N\eta+O_N(\eta^3),\quad c=1+O_N(\eta^2),\quad a+b=2d_N+O_N(\eta^2).
\]
The odd-sector polynomial has trace \(2-c=1+O_N(\eta^2)\) and determinant \((a-b)^2\). Its small eigenvalue is therefore \(K_N^2\eta^2+O_N(\eta^4)\), and the other tends to \(1\). The even-sector eigenvalues tend to \((3\pm\sqrt{9-16d_N^2})/2\). Because \(N\ge5\) implies \(0<d_N<1/\sqrt2\), these two limits are strictly positive and the larger exceeds \(1\). Thus the odd small eigenvalue is uniquely minimal near collision and the larger even eigenvalue is uniquely maximal. Taking square roots proves both sharp asymptotics.

Finally \(N\sin(\pi/(2N))\to\pi/2\) and \(\cos(\pi/(2N))\to1\), proving the universal limits. No finite computation is used to infer an assertion over all \(N\).

## Verification
A standalone NumPy checker (`checker.py`) constructs the actual complex Fourier matrices, diagonalizes \(FF^*\), and compares the resulting eigenvalues with all claimed closed forms for eight odd matrix sizes and five separation parameters each. It separately checks the leading small-gap constants at four matrix sizes. The recorded output is in `CHECKER_OUTPUT.txt`; the analytical block reduction and Taylor expansions constitute the proof.

## Relationship to prior work
Kunis and Potts (2007) study localization-kernel bounds for nonequispaced trigonometric interpolation; their sections 2 and 4 give kernel factorizations, general separation-based eigenvalue bounds, and the circulant equispaced case, but not this two-moved-node four-root spectrum. Austin and Trefethen (2016) address interpolation and quadrature under arbitrary bounded grid perturbations; their stated estimates do not supply this exact local singular spectrum. Kunis and Nagel (2018/2020) establish linear inverse-separation conditioning for nearly colliding Vandermonde nodes in an oversampled regime; their general estimates do not specify this critical-square-grid sharp leading coefficient. The more recent Chen–Lin–Zhang (2026) work concerns smallest-singular-value bounds for both perturbed grids and clusters; only its abstract was accessible for the present comparison. The classical Dirichlet-kernel identity and Fourier unitarity are inputs rather than claimed novelties.

## Limitations
This is an exact theorem for one symmetric adjacent two-node perturbation, not a general theorem for arbitrary off-grid sets. It does not improve the known generic inverse-separation exponent; the distinctive information is the complete four-outlier spectrum and its exact critical-square-grid coefficients. Publication priority remains qualified by the uninspected full text of the 2026 nonuniform Fourier-matrix paper and the possibility of an equivalent specialized older result. Independent validation has not been performed.

## References
1. S. Kunis and D. Potts, *Stability Results for Scattered Data Interpolation by Trigonometric Polynomials*, arXiv:math/0702019, first submitted 2007-02-01, especially sections 2 and 4.
2. A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018, first submitted 2016-12-13.
3. S. Kunis and D. Nagel, *On the condition number of Vandermonde matrices with pairs of nearly-colliding nodes*, arXiv:1812.08645 (2018); open-access article, *Numerical Algorithms* 87 (2021), 473–496, DOI:10.1007/s11075-020-00974-x.
4. L. Chen, R. Lin, and H. Zhang, *The Smallest Singular Value of Nonuniform Fourier Matrices*, arXiv:2608.21960, first submitted 2026-08-22 (abstract consulted; full text not inspected).
