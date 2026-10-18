# Exact Fourier interpolation and determinant on mixed-alphabet coordinate crosses

## Finding
Let \(d\ge2\), and let \(G_1,\ldots,G_d\) be arbitrary finite abelian groups with \(n_i=|G_i|\ge2\). In their direct product \(G=\prod_iG_i\), consider the **radius-one Hamming ball**
\[
X=\{0\}\cup\bigcup_{i=1}^{d}\{(0,\ldots,0,x_i,0,\ldots,0):x_i\in G_i\setminus\{0\}\}.
\]
Define \(X^*\subset\widehat G\) analogously using the nontrivial characters in each coordinate. They have the same size \(K=1+\sum_i(n_i-1)\). Let \(M=(\chi(x))_{\chi\in X^*,\,x\in X}\) be the corresponding **unnormalized Fourier submatrix**. Write
\[
v_i=\sqrt{n_i-1},\quad v=(v_1,\ldots,v_d)^\mathsf T,\quad D=\operatorname{diag}(n_1,\ldots,n_d),\quad
S=\begin{pmatrix}1&v^\mathsf T\\v&vv^\mathsf T-D\end{pmatrix}.
\]
Then \(M\) is invertible for **every** such product, with the complete singular-value multiset
\[
\boxed{\ \{\,|\lambda|:\lambda\in\operatorname{spec}(S)\,\}\ \sqcup\
\bigsqcup_{i=1}^{d}\{\sqrt{n_i}\}^{[n_i-2]}\ }.
\tag{1}
\]
Here the eigenvalues of the explicit real symmetric \((d+1)\)-by-\((d+1)\) matrix \(S\) are counted with multiplicity, and a block with \(n_i=2\) contributes no extra singular values. In particular, the complete, group-structure-independent Fourier-minor determinant law is
\[
\boxed{\ |\det M|=\prod_{i=1}^{d}n_i^{\,n_i/2}.\ }
\tag{2}
\]
The exceptional \((d+1)\)-dimensional block has the closed inverse
\[
\boxed{\ S^{-1}=\begin{pmatrix}1-v^\mathsf TD^{-1}v&v^\mathsf TD^{-1}\\D^{-1}v&-D^{-1}\end{pmatrix}.\ }
\tag{3}
\]
On all complementary subspaces, inversion consists of an adjoint punctured-character transform divided by \(n_i\). Thus (1)–(3) furnish **explicit stable interpolation from Fourier data on the same coordinate cross**, including the sharp lower and upper \(\ell^2\) reconstruction constants: the smallest and largest numbers in (1), divided by \(\sqrt{\prod_i n_i}\) for the unitary Fourier normalization.

As a closed-form equal-alphabet specialization, when every \(n_i=n\), put \(L=(d-1)(n-1)\) and
\[\lambda_\pm=\frac{L\pm\sqrt{L^2+4n}}{2}.\]
Then the complete multiset (1) is
\[\{\lambda_+,\,|\lambda_-|,\,n^{[d-1]},\,(\sqrt n)^{[d(n-2)]}\}.\]
For \(d\ge3\), its sharp spectral condition number is
\[\kappa(M)=\lambda_+^2/n,\]
whereas for \(d=2\) it equals \(n\). (The distinct algebraic eigenvalues are combined where they coincide; zero multiplicities are omitted.)

## Assumptions and scope
Each \(G_i\) is finite and abelian, written additively, with identity \(0\). There is no restriction on exponents, prime-power cardinalities, cyclicity, or equality of the cardinalities. The character groups \(\widehat G_i\) contain the trivial character \(1\), and \(X^*\) contains the all-trivial tuple exactly once. All Hilbert spaces on finite sets use unweighted counting norm. The unitary full-product Fourier transform has entries \(\chi(x)/\sqrt{|G|}\), so the restriction to \(X^*\) of Fourier transforms of signals supported in \(X\) is exactly \(M/\sqrt{|G|}\). Either convention of complex conjugation produces the same singular values, determinant magnitude, and reconstruction constants. No phase formula for \(\det M\) is claimed.

## Proof
**1. Orthogonal subspaces.** Index both \(X\) and \(X^*\) by a central point, followed by \(d\) punctured coordinate axes of respective lengths \(n_i-1\). The central matrix entry and all central–axis entries of \(M\) are \(1\). Its off-diagonal axis blocks consist entirely of \(1\)'s. Its diagonal axis block \(B_i\) is the nontrivial-character/nonzero-point submatrix of the character table of \(G_i\). Character orthogonality gives the exact identities
\[
B_i\mathbf1=-\mathbf1,\qquad B_i^*\mathbf1=-\mathbf1,\qquad
B_i^*B_i=n_iI-J,
\tag{4}
\]
where \(J=\mathbf1\mathbf1^\mathsf T\) on the \((n_i-1)\)-dimensional punctured coordinate block. The first identity uses \(\sum_{x\in G_i}\chi(x)=0\) for \(\chi\ne1\); the second and third follow by applying the same orthogonality on the dual group.

Let \(E_i\) consist of coefficient vectors on the punctured \(i\)-th axis whose entries sum to zero. Then \(\dim E_i=n_i-2\) (possibly zero). Identity (4) shows that \(B_i\) maps \(E_i\) into the corresponding dual mean-zero subspace, and its singular values there all equal \(\sqrt{n_i}\). Every off-axis all-ones block and all central couplings annihilate \(E_i\). Thus \(M\) reduces, as a map between the two Hilbert spaces, to \(d\) independent \(B_i|_{E_i}\) blocks and one constant-on-each-axis block.

**2. Exceptional block.** Take the orthonormal domain basis consisting of the center point mass and the normalized punctured-axis indicators \(\mathbf1/\sqrt{n_i-1}\); use the analogous codomain basis. The matrix of the remaining block is exactly \(S\), because the \(i\)-diagonal axis inner product is \(-1\) and the \(i\ne j\) axis inner product is \(\sqrt{(n_i-1)(n_j-1)}\). The displayed real symmetric \(S\) has singular values equal to the absolute values of its real eigenvalues. Combined with the \(E_i\) blocks, this proves (1) with the stated multiplicities, including every boundary case \(n_i=2\).

**3. Nonvanishing, determinant, and reconstruction.** The leading entry of \(S\) is \(1\), and its Schur complement is
\[
(vv^\mathsf T-D)-vv^\mathsf T=-D.
\]
Consequently \(\det S=(-1)^d\prod_i n_i\ne0\). Block inversion yields (3), directly confirmed by multiplication. On \(E_i\), (4) gives \((B_i|_{E_i})^{-1}=n_i^{-1}B_i^*\) as a map from the dual centered block to the original centered block. Therefore the entire \(M\) is invertible and can be inverted by orthogonal projections and these explicit formulas. The determinant absolute value of a square matrix equals the product of all its singular values. The \(E_i\) contribution is \(n_i^{(n_i-2)/2}\), while \(|\det S|=\prod_i n_i\). Multiplying proves (2).

**4. Sharp constants and uniform specialization.** By the singular-value theorem, the numbers in (1) give the best possible two-sided \(\ell^2\) bounds, and their extremizing spaces are precisely the corresponding orthogonal singular subspaces. If \(n_i=n\) for every \(i\), the axis-contrast subspace \(\{(a_1,\ldots,a_d):\sum a_i=0\}\) of \(S\) has eigenvalue \(-n\) with multiplicity \(d-1\). The remaining two-dimensional block has trace \((d-1)(n-1)\) and determinant \(-n\), yielding \(\lambda_\pm\). For \(d\ge3\), its positive eigenvalue is larger than \(n\) and its negative eigenvalue lies in \((-1,0)\), because its characteristic polynomial evaluated at \(n\) is \(n(2-d)(n-1)<0\), and \(\lambda_+|\lambda_-|=n\). These are the maximal and minimal singular values, so \(\kappa=\lambda_+^2/n\). At \(d=2\) one has \(\lambda_+=n\) and \(\lambda_-=-1\), giving condition number \(n\). This finishes the complete claim.

## Verification
The standalone checker `artifacts/verify.py` constructs character matrices directly on mixed cyclic and noncyclic products, without reusing formula (4) or the block decomposition. It compares numerical SVD singular values against (1), checks determinant magnitudes using a stable log-determinant, and directly multiplies the proposed inverse (3) by \(S\). Tested configurations have two to four coordinates, distinct coordinate cardinalities, repeated cardinalities, and noncyclic finite abelian factors. The maximum observed singular-value discrepancy was below \(4\times10^{-15}\), and all tests passed. Run using `OPENBLAS_NUM_THREADS=1 python artifacts/verify.py` with NumPy installed. These finite calculations corroborate the exact proof rather than replacing it.

## Relationship to prior work
Slepian (1978) initiated the discrete time–frequency concentration eigenvalue program, chiefly for one-dimensional interval supports. Ghobber–Jaming (first publicly available in 2009) prove general finite-dimensional uncertainty and recovery criteria, including sufficient small-support product conditions, but not the mixed-alphabet full axis-cross singular spectrum or determinant (2). Gilbert–Rzeszotnik (2010) study full finite-abelian Fourier operator norms and subgroup structure, rather than this simultaneous time/frequency truncation.

Several closely related published exact concentration results were also compared. The degree-one Fourier band on a **uniform-alphabet Hamming shell** of nonzero weight is different from the **ball** containing the origin here; its known spectral formula does not directly assert (1)–(3) for arbitrary unequal abelian alphabets. A published Boolean Hamming-ball theorem includes the special all-order-two case, and a previously published quadratic-cone first-band theorem includes the two-axis equal-prime-power case. Neither statement supplies the mixed-cardinality determinant factorization and full recovery formula for all finite abelian coordinate products. A previously published fourth-moment theorem for two-axis crosses concerns a different operator norm and equality classification; it does not imply (1)–(3). Broad generalized Hamming-association-scheme reductions could still give an alternate route to this computation; the precise mixed-alphabet result was not located in the inspected sources.

## Limitations
This gives all singular values through a concrete \((d+1)\)-by-\((d+1)\) real symmetric matrix, not a general radical expression for its eigenvalues when the orders differ. Individual singular-vector bases on the centered axis blocks depend on the chosen character tables; their **singular values**, rather than their phases, are universal. It does not classify arbitrary higher-radius Hamming balls, arbitrary distinct spatial/frequency sets, or nonabelian factors. No uniqueness or independent peer validation is asserted, and mathematically equivalent forms may exist in the broad finite Fourier/minor literature.

## References
1. D. Slepian, *Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case*, Bell System Technical Journal **57** (1978), 1371–1430, DOI: https://doi.org/10.1002/j.1538-7305.1978.tb02104.x (public record dated 1978-05-01).
2. S. Ghobber and P. Jaming, *On uncertainty principles in the finite dimensional setting*, arXiv:0903.2923 (first posted 2009-03-17), https://arxiv.org/abs/0903.2923.
3. J. E. Gilbert and Z. Rzeszotnik, *The norm of the Fourier transform on finite abelian groups*, Annales de l'Institut Fourier **60** (2010), 1317–1346, DOI: https://doi.org/10.5802/aif.2556.
4. Published exact first-band concentration on nonbinary Hamming shells, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-q-ary-hamming-shell-fourier-concentration-and-the-arithmet--89a15e26e594.
5. Published Boolean Hamming-ball Fourier concentration spectrum, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-walsh-band-concentration-spectra-on-boolean-hamming--a2f5ddac5a0f.
6. Published split quadratic-cone first-band concentration theorem, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-first-band-fourier-concentration-on-split-quadratic-cones--dbf8fa8aec40.
7. Published fourth-moment extension theorem on finite abelian two-axis crosses, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
