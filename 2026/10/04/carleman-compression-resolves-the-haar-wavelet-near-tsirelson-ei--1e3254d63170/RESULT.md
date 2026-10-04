# Carleman compression resolves the Haar-wavelet near-Tsirelson eigenvalue conjecture
## Finding
Let \(A(N,K)\) be the real symmetric matrix introduced by Dudal and Vandermeersch from Haar-wavelet integrals, with scale indices \(0\le n,m\le N\) and translation indices \(1\le k,\ell\le K\). Then
\[
\lim_{N,K\to\infty}\lambda_{\max}(A(N,K))=\pi
\]
in the directed sense: for every \(\delta>0\) there are finite \(N_0,K_0\) such that
\[
\lambda_{\max}(A(N,K))>\pi-\delta
\]
whenever \(N\ge N_0\) and \(K\ge K_0\).

This proves Conjecture B of Dudal and Vandermeersch. Their paper proves that this eigenvalue statement supplies the finite Haar-wavelet systems needed for Bell--CHSH violations arbitrarily close to the Tsirelson limit in the free massless \(1+1\)-dimensional fermion construction.

## Assumptions and scope
Let \(\psi\) be the standard Haar mother wavelet and
\[
\psi_{n,j}(x)=2^{n/2}\psi(2^n x-j).
\]
The source defines
\[
A_{(n,k),(m,\ell)}
=
-\iint_{\mathbb R_-^2}
\frac{\psi_{n,-k}(x)\psi_{m,-\ell}(y)}{x+y}\,dx\,dy ,
\]
for \(k,\ell\ge1\). Only the finite matrices specified above are considered.

Define the Carleman operator \(C\) on \(L^2(\mathbb R_+)\) by
\[
(Cf)(x)=\int_0^\infty \frac{f(y)}{x+y}\,dy.
\]
The classical Mellin diagonalization of \(C\) is used as published input. It identifies \(C\) with multiplication by
\[
\frac{\pi}{\cosh(\pi\xi)},
\]
so \(C\) is positive and \(\|C\|=\pi\).

No claim is made here about the source's separate fixed-\(K\) conjecture that a matrix-valued Fourier symbol attains its maximum at \(t=0\). The argument bypasses that question and proves the two-parameter Conjecture B directly.

## Proof
The source proves the reflection identity
\[
\psi_{n,k}(-x)=-\psi_{n,-k-1}(x)
\]
almost everywhere. Put \(x=-u\), \(y=-v\) in the definition of \(A\). Since \(x+y=-(u+v)\), the two reflection signs cancel and give
\[
A_{(n,k),(m,\ell)}
=
\int_0^\infty\!\!\int_0^\infty
\frac{\psi_{n,k-1}(u)\psi_{m,\ell-1}(v)}{u+v}\,du\,dv.
\]
Thus \(A(N,K)\) is exactly the matrix of the compression of \(C\) to
\[
V_{N,K}
=
\operatorname{span}\{\psi_{n,j}:0\le n\le N,\ 0\le j<K\}.
\]
The Haar vectors are orthonormal, hence
\[
\lambda_{\max}(A(N,K))
=
\sup_{\substack{f\in V_{N,K}\\ \|f\|_2=1}}
\langle f,Cf\rangle
\le \|C\|=\pi.
\]

It remains to prove a matching lower bound. Let
\[
\mathcal H=\overline{\bigcup_{N,K}V_{N,K}}.
\]
For every fixed dyadic Haar wavelet on \((0,1)\), its scale and translation indices occur in some \(V_{N,K}\). Consequently \(\mathcal H\) contains the entire mean-zero subspace
\[
L^2_0(0,1)
=
\left\{f\in L^2(0,1):\int_0^1 f(x)\,dx=0\right\}.
\]

Fix \(\varepsilon>0\). Because \(C\) is positive with norm \(\pi\), and compactly supported functions are dense in \(L^2(\mathbb R_+)\), there is \(g\in C_c(\mathbb R_+)\) with
\[
\|g\|_2=1,
\qquad
\langle g,Cg\rangle>\pi-\varepsilon.
\]
For \(a>0\), define the unitary dilation
\[
(D_ag)(x)=a^{-1/2}g(x/a).
\]
A direct change of variables shows
\[
CD_a=D_aC.
\]
Therefore \(D_ag\) has the same norm and the same Carleman Rayleigh quotient as \(g\).

Choose \(a\) small enough that \(\operatorname{supp}(D_ag)\subset(0,1/2)\). Writing
\[
I=\int_0^\infty g(x)\,dx,
\]
one has
\[
\int_0^\infty (D_ag)(x)\,dx=a^{1/2}I.
\]
Let
\[
h(x)=2\,\mathbf 1_{[1/2,1]}(x),
\qquad
\int_0^1h(x)\,dx=1,
\]
and set
\[
f_a=D_ag-a^{1/2}Ih.
\]
Then \(f_a\) is supported in \((0,1)\), has integral zero, and hence belongs to \(L^2_0(0,1)\subset\mathcal H\). Moreover
\[
\|f_a-D_ag\|_2
=
a^{1/2}|I|\,\|h\|_2
\longrightarrow0.
\]
Since \(C\) is bounded, after normalizing \(f_a\) its Rayleigh quotient converges to that of \(D_ag\), and therefore exceeds \(\pi-2\varepsilon\) for sufficiently small \(a\).

Finally, finite Haar sums from \(\bigcup_{N,K}V_{N,K}\) are dense in \(\mathcal H\). Approximating this normalized \(f_a\) by one such finite sum and using boundedness of \(C\) produces finite \(N,K\) with
\[
\lambda_{\max}(A(N,K))>\pi-3\varepsilon.
\]
Because \(\varepsilon\) is arbitrary and the upper bound is \(\pi\), the directed limit is \(\pi\). The spaces \(V_{N,K}\) are nested in each parameter, so once a pair works, every coordinatewise larger pair works as well.

## Verification
The proof uses no finite experiment as a substitute for an infinite argument. The critical external operator-theoretic input was checked against the published Carleman diagonalization: under the Mellin transform the quadratic form of \(C\) has multiplier
\[
\frac{\pi}{\cosh(\pi\xi)},
\]
whose essential supremum is \(\pi\).

The remaining steps are explicit: the source's reflection formula converts its matrix entries to Carleman matrix elements; \(D_a\) is unitary and commutes with \(C\); the mean correction has exact size \(a^{1/2}|I|\|h\|_2\); and the standard Haar basis on \((0,1)\) spans its mean-zero \(L^2\) subspace.

## Relationship to prior work
Dudal and Vandermeersch state Conjecture B as the assertion that for every \(\delta>0\), sufficiently large finite \(N,K\) satisfy
\[
\lambda_{\max}(A(N,K))>\pi-\delta.
\]
Their April 2026 publication says a complete proof remains open, establishes the fixed-\(K=1\) limit \(3.1105202\ldots\), and gives numerical evidence for larger \(K\). In their conclusion they explicitly suggest that Hilbert-space operator methods might prove the conjecture, but do not identify the finite matrices as compressions whose joint Haar subspace retains the full Carleman norm.

The Carleman operator itself is classical. Yafaev's work records its Mellin diagonalization and spectrum, in particular the upper spectral edge \(\pi\). That whole-space theorem alone does not imply Conjecture B, because the matrices use a restricted family of nonnegative-scale Haar wavelets. The new step is the dilation-plus-mean-correction argument showing that the restricted joint Haar closure still has Carleman compression norm \(\pi\), followed by finite Haar approximation.

Targeted searches for the arXiv identifier, Conjecture B, the Carleman-operator formulation, the compression-norm formulation, and the \(A(N,K)\) eigenvalue limit found no published result that supplies this bridge.

## Limitations
The result concerns the source's two-parameter finite Haar matrices and proves their directed maximal-eigenvalue limit. It does not establish the separate identity
\[
\max_t\lambda_{\max}(F_K(t))=\lambda_{\max}(F_K(0))
\]
for each fixed \(K\), nor does it provide an explicit rate telling how large \(N\) and \(K\) must be for a prescribed \(\delta\). The near-extremizer argument is existential.

A residual literature risk remains that an equivalent compression-norm argument may appear in very recent or remotely indexed operator-theory work not linked to the source terminology. No such result was found in the targeted source, published-finding corpus, and web searches performed for this finding.

## References
1. D. Dudal and K. Vandermeersch, *Further evidence for near-Tsirelson Bell--CHSH violations in quantum field theory via Haar wavelets*, arXiv:2410.13362v1, first public 2024-10-17; Eur. Phys. J. C 86, 349 (2026), DOI 10.1140/epjc/s10052-026-15559-6.
2. D. R. Yafaev, *Spectral and scattering theory for perturbations of the Carleman operator*, arXiv:1210.5709.
3. D. R. Yafaev, *Diagonalizations of two classes of unbounded Hankel operators*, Bull. Math. Sci. 4 (2014), 175--198, DOI 10.1007/s13373-013-0044-0.
