# Exact first-band Fourier concentration on split quadratic cones over odd finite fields

## Finding
Let \(q\) be an odd prime power, \(m\ge1\), and \(G=\mathbb F_q^{2m}\). Consider the split quadratic cone
\[
X=\{(x,y)\in G:\ \textstyle\sum_{j=1}^m x_jy_j=0\}
\]
and the Fourier first-Hamming-band space \(H_1\), spanned by the constant character and all nontrivial characters depending on precisely one coordinate. Put
\[
r=q-1,\quad a=1/q,\quad c=q^{-m},\quad b=rc/q,\quad v=rc,\quad L=2mr.
\]
On \(H_1\), the positive operator \(K=P_{H_1}M_{\mathbf1_X}P_{H_1}\) (ambient normalized counting measure) has the following *complete spectrum, including multiplicities*:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
\lambda_+&1\\
\lambda_-&1\\
a+v&m\\
a-v&m-1\\
a&2m(q-2)
\end{array}
\]
where \(\lambda_\pm\) are the two roots of the characteristic polynomial of
\[
T=\begin{pmatrix}a+b&b\sqrt L\\b\sqrt L&a-v+bL\end{pmatrix},
\]
namely
\[
\lambda_\pm=a+\frac{b(1+L)-v\pm\sqrt{(v+b(1-L))^2+4b^2L}}2.
\]
Zero-multiplicity rows are omitted. When \(m=1\), the spectrum simplifies to \(1\) twice, \(q^{-1}\) with multiplicity \(2(q-2)\), and \(q^{-2}\) once. When \(m\ge2\), all five displayed values are distinct and obey
\[
0<a-v<\lambda_-<a<a+v<\lambda_+<1.
\]
In particular, the restriction of \(H_1\) to the cone is always injective. Its sharp squared concentration constant is \(\lambda_+\), and for \(m\ge2\) the nonzero equality cases are precisely the complex multiples of
\[
f_+(x,y)=\alpha+\beta\sum_{j=1}^m\sum_{u\in\mathbb F_q^\times}
(\psi(u x_j)+\psi(u y_j)),\qquad
\frac{\alpha}{\beta}=\frac{bL}{\lambda_+-a-b},\quad\beta\ne0.
\]
For \(m=1\), the squared concentration constant equals \(1\), with a two-dimensional equality space \(\operatorname{span}\{\mathbf1_{x=0},\mathbf1_{y=0}\}\). Thus the cone has nonzero perfectly concentrated first-band signals exactly at \(m=1\). The sharp smallest Rayleigh quotient is \(q^{-2}\) at \(m=1\), and \(a-v\) at \(m\ge2\), so all singular values of restriction are the square roots of the spectrum above.

## Assumptions and scope
Fix any nontrivial complex-valued additive character \(\psi\) of \(\mathbb F_q\). For frequencies \(\xi\in G\), put \(\chi_\xi(z)=\psi(\xi\cdot z)\). Inner products use \(\langle f,g\rangle=q^{-2m}\sum_{z\in G}f(z)\overline{g(z)}\). These characters form an orthonormal basis. Let \(E=\{0\}\cup\{ue_j:u\in\mathbb F_q^\times,\ 1\le j\le2m\}\) and \(H_1=\operatorname{span}\{\chi_\xi:\xi\in E\}\), of dimension \(1+2m(q-1)\). The energy being optimized is **ambiently normalized**:
\[
\mathcal C(f)=\frac{q^{-2m}\sum_{z\in X}|f(z)|^2}{q^{-2m}\sum_{z\in G}|f(z)|^2},\quad 0\ne f\in H_1,
\]
not the conditional average on \(X\). All assertions hold for every odd prime power, including nonprime fields; the coordinate system and split quadratic form are fixed as stated. No claim is made for nonsplit quadratic forms, arbitrary spectra, or \(L^p\) norms other than \(p=2\).

## Proof
**Character sum.** The additive orthogonality identity is \(\mathbf1_{\{w=0\}}=q^{-1}\sum_{t\in\mathbb F_q}\psi(tw)\). For any \((\xi,\eta)\in\mathbb F_q^m\times\mathbb F_q^m\), evaluate
\[
F(\xi,\eta)=q^{-2m}\sum_{x,y\in\mathbb F_q^m}\mathbf1_X(x,y)\psi(\xi\cdot x+\eta\cdot y).
\]
The zero multiplier gives \(q^{-1}\mathbf1_{\xi=\eta=0}\). At multiplier \(t\ne0\), summation over \(y\) forces \(x=-\eta/t\), yielding exactly \(q^m\psi(-\xi\cdot\eta/t)\). Consequently
\[
F(\xi,\eta)=q^{-1}\mathbf1_{(\xi,\eta)=0}+q^{-m-1}
\sum_{t\ne0}\psi(-\xi\cdot\eta/t)
=\begin{cases}a+b,&(\xi,\eta)=0,\\b,&(\xi,\eta)\ne0,\ \xi\cdot\eta=0,\\-q^{-m-1},&\xi\cdot\eta\ne0.\end{cases}
\]
The last equality uses \(\sum_{t\ne0}\psi(u/t)=q-1\) for \(u=0\), and \(-1\) otherwise.

**Exact matrix and invariant decomposition.** The Gram entry between characters with frequencies \(s,t\in E\) is \(F(t-s)\), so
\[
K=aI+bJ-cA,
\]
where \(J\) is all ones and \(A\) is the adjacency matrix of \(m\) disjoint complete bipartite graphs \(K_{r,r}\), with an isolated zero-frequency vertex. The two parts of each bipartite component correspond to the \(r\) frequencies on \(x_j\) and the \(r\) frequencies on \(y_j\). Indeed, the split dual quadratic form is nonzero on a difference of first-band frequencies precisely for a pair of distinct coordinate characters on matching \(x_j,y_j\).

Decompose \(\mathbb C^E\) orthogonally as follows. Contrasts summing to zero within one of the \(2m\) coordinate blocks give \(2m(r-1)\) eigenvectors with eigenvalue \(a\). Antisymmetric constant vectors on the two parts of each paired block yield \(m\) eigenvectors with eigenvalue \(a+cr=a+v\). Symmetric paired-block constants whose \(m\) amplitudes sum to zero yield \(m-1\) eigenvectors with eigenvalue \(a-cr=a-v\). The remaining subspace is spanned by the zero-frequency basis vector and \(L^{-1/2}\) times the sum of all nonzero-frequency basis vectors; direct multiplication gives the displayed \(2\)-by-\(2\) matrix \(T\). These dimensions sum to \(1+2mr\), proving that no eigenvalues are omitted.

**Ordering and boundaries.** At \(m=1\), direct substitution gives \(\operatorname{spec}(T)=\{1,q^{-2}\}\) and \(a+v=1\), establishing the three-level formula. For \(m\ge2\), \(a-v>0\), and \(T-(a-v)I\) is positive definite: its upper-left entry is \(b+v>0\), and its determinant is \(vbL>0\). Also \(\det(T-aI)=-bv<0\), so \(\lambda_-<a<\lambda_+\). Since the second diagonal entry of \(T\) is \(a-v+bL>a+v\) (equivalent to \(m(q-1)>q\)), \(\lambda_+>a+v\). Finally, \(1-a-b>0\) and
\[
\det(I-T)=\left(\frac{q-1}{q}\right)^2
\left(1-\frac{(2m-1)(q-1)}{q^m}-q^{1-2m}\right)>0.
\]
Indeed \(q^{m-1}\ge2m-1\), so the last parentheses exceed \(1-(q-1)/q-q^{1-2m}>0\). Hence \(I-T\) is positive definite and \(\lambda_+<1\). This proves the strict five-eigenvalue ordering and injectivity.

**Sharp equality cases.** The Courant--Fischer principle identifies the maximal concentration with \(\lambda_+\). For \(m\ge2\), it is a simple eigenvalue and exceeds all other eigenvalues. Its eigenvector has constant nonzero-frequency coefficient \(\beta\), and the eigen-equation at zero frequency yields \((\lambda_+-a-b)\alpha=bL\beta\), exactly the stated profile. For \(m=1\), the eigenvalue \(1\) has multiplicity two, and \(\mathbf1_{x=0}\) and \(\mathbf1_{y=0}\) lie in \(H_1\), are supported on \(X=\{xy=0\}\), and are linearly independent; therefore their span is the full equality space. The minimum-eigenvalue eigenspace for \(m\ge2\) consists of pair-symmetric block constants with amplitudes summing to zero.

## Verification
The accompanying standalone `CHECK.py` uses the standard Python library and reconstructs the Gram matrix both by the exact formula \(aI+bJ-cA\) and direct character summation. It checks all invariant blocks with rational arithmetic, including trace, characteristic polynomial, exact eigenvector relations, dimensions, and the strict ordering at tested parameters. Eight prime-field cases are verified: \((q,m)=(3,1),(3,2),(3,3),(5,1),(5,2),(7,1),(7,2),(11,1)\). The run reported `VERIFY_OK prime_field_cases=8 Fourier_matrix_entries=1880 complete_block_decompositions=8 max_error=2.997e-16`. The exact character-sum and block-decomposition proof, not these samples, establish the universal assertion for odd prime powers.

## Relationship to prior work
Iosevich--Koh (arXiv:0804.4505v1) establish quadratic-surface Fourier restriction and extension estimates on *nonzero* level sets, using exponential sums and Fourier decay. In particular their Lemma 9 provides bounds for a different surface normalization; it does not state an exact first-Hamming-band Gram spectrum on the *zero* split cone. Vinh (arXiv:0904.0441v1, Section 10) uses spectra of finite Euclidean graphs associated with quadratic forms; these are adjacency spectra on a full affine vertex space, not the compression of multiplication by a quadratic cone indicator to first-level coordinate characters. Classical association schemes related to nondegenerate quadrics may reproduce ingredients of the Fourier coefficient calculation, but no exact five-level compression/equality-space theorem was identified in the inspected sources. The present result concerns a constrained Fourier energy localization operator rather than full-space graph eigenvalues or \(L^2\)-to-\(L^4\) extension.

## Limitations
The result is for the split form and first Hamming Fourier band only, with ambient counting normalization. The verified tests cover prime fields, whereas the proof covers all odd prime powers. Historical priority relative to older association-scheme character tables and quadric-code results is not fully resolved; exact novelty is not independently certified. No conclusion is asserted for sampling noise models, nonlinear phase retrieval, or generic quadratic forms.

## References
1. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505v1, first posted 2008-04-28, https://arxiv.org/html/0804.4505v1.
2. Le Anh Vinh, *The sovability of norm, bilinear and quadratic equations over finite fields via spectra of graphs*, arXiv:0904.0441v1, first posted 2009-04-02, https://arxiv.org/html/0904.0441v1.
3. I. M. Chakravarti, *Association Schemes, Orthogonal Arrays and Codes from Non-Degenerate Quadrics and Hermitian Varieties in Finite Projective Geometries*, Journal of the Indian Society of Agricultural Statistics 40 (1990), 89--96, DOI:10.1177/0008068319900507 (abstract inspected; full text unavailable).
