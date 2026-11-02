# A sharp dimension-independent squared-rank Gaussian threshold on binary three-column matrices

## Finding
For every integer \(m\ge3\), let \(G_m=M_{m,3}(\mathbb F_2)\) and \(d(X,Y)=\operatorname{rank}_{\mathbb F_2}(X-Y)\). For \(0\le u\le1\), the real symmetric matrix
\[
K_u(X,Y)=u^{d(X,Y)^2}\quad(X,Y\in G_m),\qquad 0^0=1,
\]
is positive semidefinite **if and only if** \(0\le u\le\rho\) or \(u=1\), where \(\rho\in(1/8,1/6)\) is the unique positive root of
\[
Q(u)=4u^5+4u^4+4u^3+6u^2+6u-1.
\]
Numerically, \(\rho\approx0.14371017391442545\). The matrix is strictly positive definite for \(0\le u<\rho\); at \(u=\rho\) its nullity is exactly \((2^m-1)(2^m-2)(2^m-4)\); and it is indefinite for \(\rho<u<1\). At \(u=1\), it is the all-ones matrix of rank one. Equivalently, \(\exp(-t d(X,Y)^2)\), with \(t\ge0\), is positive semidefinite if and only if \(t=0\) or \(t\ge-\log\rho\approx1.9399566887204878\), independently of \(m\).

## Assumptions and scope
Matrices have exactly three columns over the binary field; \(m\) is any integer at least three. Positive definiteness concerns the full \(2^{3m}\)-point translation-invariant matrix, not one code or a sampled submatrix. Only real bandwidths \(0\le u\le1\) (equivalently nonnegative Gaussian inverse bandwidths) are asserted. The rank metric, the exponent two, the endpoint convention, and all matrix-normalization choices are part of the claim.

## Proof
Write \(T=2^m\), and Fourier-diagonalize convolution on the additive group \(G_m\) using the real characters \(\chi_U(X)=(-1)^{\langle U,X\rangle}\), with \(\langle U,X\rangle=\sum_{i,j}U_{ij}X_{ij}\pmod2\). The eigenvalue depends only on the rank \(s\in\{0,1,2,3\}\) of \(U\). Put \(e_j(X)=\mathbf1_{\{\operatorname{rank}X=j\}}\).

For \(0\le t\le3\), let \(b_t(X)\) count \(t\)-dimensional subspaces \(W\le\mathbb F_2^3\) containing the row space of \(X\). Counting such spaces gives
\[
 b_0=e_0,\quad b_1=7e_0+e_1,\quad b_2=7e_0+3e_1+e_2,\quad b_3=e_0+e_1+e_2+e_3.
\]
For a fixed \(W\), summing \(\chi_U\) over the \(m\) rows in \(W\) yields \(T^{\dim W}\) if all rows of \(U\) lie in \(W^\perp\), and zero otherwise. Hence, with Gaussian binomial notation,
\[
 \widehat b_t(U)=T^t\binom{3-s}{t}_2\quad(t=0,1,2),
 \qquad \widehat b_3(U)=T^3\mathbf1_{\{s=0\}}.
\]
In particular, the coefficient lists for \(t=1,2\), indexed by \(s=0,1,2,3\), are \((7,3,1,0)\) and \((7,1,0,0)\). Inverting the four triangular identities proves the following *complete* Fourier spectrum of \(K_u=e_0+u e_1+u^4e_2+u^9e_3\):
\[
\begin{aligned}
\lambda_0&=1+7(T-1)u+7(T-1)(T-2)u^4+(T-1)(T-2)(T-4)u^9,\\
\lambda_1&=1+(3T-7)u+(T^2-9T+14)u^4+(-T^2+6T-8)u^9,\\
\lambda_2&=1+(T-7)u+(14-3T)u^4+(2T-8)u^9,\\
\lambda_3&=1-7u+14u^4-8u^9.
\end{aligned}
\]
Their exact multiplicities are, respectively,
\[
 1,\qquad7(T-1),\qquad7(T-1)(T-2),\qquad(T-1)(T-2)(T-4),
\]
which sum to \(T^3\) and are all positive for \(T\ge8\).

The first eigenvalue is strictly positive for \(0\le u\le1\). The second has the manifestly nonnegative factorization
\[
\lambda_1=(1-u)\left[1+(3T-6)(u+u^2+u^3)+(T^2-6T+8)(u^4+u^5+u^6+u^7+u^8)\right],
\]
so it is positive for \(0\le u<1\). Put
\[
H(u)=1-7u+14u^4-8u^9=-(u-1)(2u^3-1)Q(u),
\qquad G(u)=u-3u^4+2u^9,
\]
so \(\lambda_3=H\) and \(\lambda_2=H+TG\). Since \(Q'(u)>0\) for \(u\ge0\), with \(Q(1/8)<0<Q(1/6)\), the root \(\rho\) is unique; let \(a=2^{-1/3}\). The factored expression gives \(H>0\) on \([0,\rho)\), \(H(\rho)=0\), \(H<0\) on \((\rho,a)\), and \(H>0\) on \((a,1)\).

On \([0,\rho]\), \(G(u)=u(1-3u^3+2u^8)\ge u(1-3/6^3)\ge0\); thus \(\lambda_2>0\) there. On \((\rho,a)\), \(\lambda_3<0\), ruling out positive semidefiniteness. On \([a,1)\), set \(g(u)=1-3u^3+2u^8\). We have \(g(a)=(a^2-1)/2<0\), \(g(1)=0\), and \(g'(u)=u^2(16u^5-9)\) changes sign exactly once, from negative to positive, so \(G(u)<0\) for \(a\le u<1\). Since \(T\ge8\), \(\lambda_2\le H+8G=(u-1)R(u)\), where
\[
 R(u)=8(u^4+u^5+u^6+u^7+u^8)-2(u+u^2+u^3)-1.
\]
As \(a>3/4\), \(R(3/4)=26653/8192>0\), and \(R'(u)\ge32(3/4)^3-12>0\) for \(3/4\le u\le1\). Therefore \(\lambda_2<0\) throughout \([a,1)\). All eigenvalues are positive for \(0\le u<\rho\); exactly the rank-three branch vanishes at \(\rho\); at \(u=1\) only the trivial character survives. This proves every PSD, strictness, nullity, and indefiniteness assertion.

## Verification
Run `python3 checker.py` using the standard library. The checker constructs all \(2^{3m}\) binary matrices for \(m=3,4,5\), applies the exact integer Walsh-Hadamard transform to each of the four rank shells, matches all eigenvalues and multiplicities against the symbolic formulas, and checks several rational bandwidths on both sides of the critical range. It independently brackets the unique root using exact fractions. This finite replay is *supplementary*; the preceding symbolic derivation and inequalities establish every \(m\ge3\) and every real \(u\in[0,1]\).

## Relationship to prior work
Delsarte's full character table of the bilinear-forms association scheme (1978, especially Section 3 and Appendix Theorem A2) already contains the general Fourier machinery; no claim is made to invent rank-scheme diagonalization. Ravagnani's 2014 public preprint establishes elementary rank-metric MacWilliams identities and rank-enumerator transforms, which are consistent with the shell Fourier formulas above. Emonds and Führ's 2010 public preprint gives the general abelian positive-definiteness framework. The asserted contribution is the sharp **all-row-dimension** squared-rank Gaussian interval, explicit algebraic endpoint, precise nullity, and proof that the rank-two branch excludes any second PSD window even after the rank-three branch turns positive again. General character tables permit this calculation but do not state the resulting sign classification.

## Limitations
Only three-column matrices over \(\mathbb F_2\) and the squared rank-distance Gaussian family are classified; no assertion is made for larger column counts or other base fields. The proof is not an independent formal certification. General Delsarte eigenmatrices could provide an alternative derivation, and equivalent explicit cutoff formulas in older kernel or coding literature cannot be categorically excluded by bounded searches. No independent audit or external mathematical validation has occurred.

## References
- P. Delsarte, *Bilinear forms over a finite field, with applications to coding theory*, Journal of Combinatorial Theory A 25 (1978), 226–241, DOI: `10.1016/0097-3165(78)90015-8`. Sections 2–3 and Appendix A2 were inspected in the complete authorized paper.
- J. Emonds and H. Führ, *Strictly positive definite functions on compact abelian groups*, arXiv:1002.3017, first public submission 2010-02-16, https://arxiv.org/abs/1002.3017.
- A. Ravagnani, *Rank-metric codes and their duality theory*, arXiv:1410.1333, first public submission 2014-10-06, https://arxiv.org/abs/1410.1333.
