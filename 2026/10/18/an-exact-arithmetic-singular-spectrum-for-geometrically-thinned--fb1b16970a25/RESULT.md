# An exact arithmetic singular spectrum for geometrically thinned Rhaly matrices

## Finding
For every integer \(b\ge2\), consider the Rhaly (terraced) operator \(R_b\) on \(\ell^2(\mathbb N)\), with matrix rows
\[
(R_bx)_n=\begin{cases}
(kb^k)^{-1/2}\sum_{j=1}^{b^k-1}x_j,&n=b^k-1\text{ for an integer }k\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]
All its **nonzero singular values**, counted with multiplicities and in decreasing order, are exactly
\[
\boxed{s_j(R_b)=j^{-1/2}\quad(j=1,2,\ldots).}
\]
They are simple and **independent of the geometric thinning base** \(b\). In particular, \(\|R_b\|=1\); \(R_b\) is compact; its optimal approximation error by operators of rank below \(j\) is \(j^{-1/2}\); and \(R_b\in\mathcal S_p\) exactly when \(p>2\) (for \(0<p<\infty\)). Its critical weak-Schatten-two quasi-norm is \(\sup_{j\ge1}\sqrt j\,s_j=1\), and \(\sum_{j=1}^N s_j^2=\sum_{j=1}^N j^{-1}\).

More generally, for every \(0<q<1\), if \(S\) is the forward unilateral shift and \(De_k=k^{-1/2}e_k\), the compact triangular operator
\[
T_q=\sqrt{1-q^2}\,D(I-qS)^{-1},\qquad
(T_q)_{kl}=\sqrt{\frac{1-q^2}{k}}q^{k-l}\mathbf1_{l\le k},
\]
has exactly the same nonzero singular values \(j^{-1/2}\). The Rhaly operators arise from \(q=b^{-1/2}\) via isometric block compression and output reindexing.

## Assumptions and scope
All Hilbert spaces are complex; indices begin at \(1\). An operator's singular values are the nonincreasing eigenvalues of its modulus, with multiplicity, and only the nonzero singular sequence is specified; \(R_b\) has an infinite-dimensional kernel. The integer constraint \(b\ge2\) applies to the concrete Rhaly rows; the triangular isospectral family is valid for every real \(0<q<1\). The spectral claim is exact for the infinite operators and is not inferred from truncations.

## Proof
**1. Geometric block compression.** Put \(N_0=0\), \(N_k=b^k-1\) and \(B_l=\{N_{l-1}+1,\ldots,N_l\}\). The cardinality is \(d_l=(b-1)b^{l-1}\). Define isometries \(U:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\) and \(V:\ell^2(\mathbb N)\to\ell^2(\mathbb N)\) on basis vectors by
\[
Ue_l=d_l^{-1/2}\sum_{j\in B_l}e_j,\qquad Ve_k=e_{N_k}.
\]
The sum through the selected row \(N_k\) is constant on each block, hence \(R_b=VT_qU^*\), where \(q=b^{-1/2}\). Indeed the \((k,l)\) matrix coefficient, for \(l\le k\), is
\[
\frac{\sqrt{d_l}}{\sqrt{kb^k}}=
\sqrt{\frac{1-b^{-1}}{k}}\,b^{-(k-l)/2},
\]
and it is zero for \(l>k\). Thus the nonzero singular values of \(R_b\) and \(T_q\) coincide, since \(R_b^*R_b=UT_q^*T_qU^*\) and \(U\) is isometric.

**2. An unbounded Jacobi inverse.** Since \(I-qS\) has a bounded inverse and \(D\) is compact, positive, injective and has dense range, \(T_q\) is compact, injective and has dense range. Its inverse \(B=T_q^{-1}\), with natural dense domain \(\{x:(\sqrt{k}x_k)_k\in\ell^2\}\), is
\[
B=(1-q^2)^{-1/2}(I-qS)D^{-1}.
\]
Write \(c=q^2\). On finitely supported vectors the positive operator \(J=B^*B\) has the Jacobi matrix
\[
J_{k,k}=\frac{(1+c)k}{1-c},\qquad
J_{k,k+1}=J_{k+1,k}=-\frac{\sqrt{c\,k(k+1)}}{1-c}\quad(k\ge1),
\]
all other coefficients being zero. The minimal symmetric Jacobi operator is essentially selfadjoint by Carleman's criterion: the reciprocal off-diagonal sum diverges, since \(\sum_{k\ge1}(k(k+1))^{-1/2}=\infty\). Consequently its closure is precisely the selfadjoint \(B^*B\), not merely a formal matrix representation.

**3. Exact diagonalization using Meixner polynomials.** On the nonnegative integers let
\[
\mu_c(m)=(1-c)^2(m+1)c^m,\qquad m=0,1,\ldots,
\]
a probability distribution. Define the standard Meixner polynomials
\[
M_n(m;2,c)={}_2F_1(-n,-m;2;1-c^{-1}),\qquad
p_n(m)=\sqrt{(n+1)c^n}\,M_n(m;2,c).
\]
For \(0<c<1\), classical Meixner orthogonality gives \(\sum_{m\ge0}\mu_c(m)p_n(m)p_l(m)=\delta_{nl}\). These polynomials are complete: if \(h\in L^2(\mu_c)\) annihilates every polynomial, the exponential generating function \(\sum_m h(m)\mu_c(m)z^m\) is analytic in a disk strictly larger than the unit disk by Cauchy–Schwarz and exponential decay, and all derivatives at \(z=1\) vanish; therefore all coefficients vanish. The three-term Meixner recurrence in this normalization reads
\[
mp_n(m)=-\frac{\sqrt{c(n+1)(n+2)}}{1-c}p_{n+1}(m)
+\frac{n+(n+2)c}{1-c}p_n(m)
-\frac{\sqrt{cn(n+1)}}{1-c}p_{n-1}(m)
\]
with \(p_{-1}=0\). Under the unitary map \(e_{n+1}\mapsto p_n\), the Jacobi matrix in step 2 is therefore unitarily equivalent to multiplication by \(m+1\) on \(L^2(\mu_c)\): the off-diagonals match, and the diagonal differs from the multiplication-by-\(m\) recurrence by exactly \(1\), because
\[
\frac{(n+1)(1+c)-n-(n+2)c}{1-c}=1.
\]
Hence \(\sigma(J)=\{1,2,3,\ldots\}\), each spectral point a simple eigenvalue, with no additional spectrum.

**4. Singular values and thresholds.** Since \(J=B^*B=(T_qT_q^*)^{-1}\), spectral inversion gives the nonzero eigenvalues of \(T_qT_q^*\) as \(1,1/2,1/3,\ldots\). Therefore \(s_j(T_q)=j^{-1/2}\) exactly, and the block equivalence gives the asserted \(R_b\) spectrum. Compactness and every Schatten/approximation assertion now follow directly from the exact sequence. In particular, divergence of \(\sum j^{-1}\) proves failure of Hilbert–Schmidt membership; the sharp weak-Schatten endpoint follows from equality of all terms.

## Verification
The standalone `CHECK.py` uses rational arithmetic to check the block-entry identity and the Meixner recurrence for four geometric bases, and a symmetric-tridiagonal eigensolver to check leading Jacobi eigenvalues for three bases at dimension \(1600\). It reports 720 exact block/recurrence checks and leading eigenvalues numerically equal to \(1,\ldots,8\), up to floating-point errors below \(10^{-12}\). Run with `python CHECK.py` after installing packages listed in `requirements.txt`. This is numerical corroboration only; completeness and the infinite spectral identity are consequences of the proof above.

## Relationship to prior work
Bellavita, Dellepiane and Stylogiannis (2026) study Rhaly and factorable matrices on weighted Hardy spaces and develop boundedness, compactness and Schatten-class criteria. In its inspected theorem statements and substantial text, that work does not identify an exactly base-independent nonzero singular sequence for geometrically sparse Rhaly rows. Their 2025 paper addresses general \(\mathcal S_p\) membership for Rhaly operators and not the full explicit spectrum exhibited here. Meixner orthogonality and the Jacobi recurrence are classical and are used as established lemmas; the result is the operator-to-Meixner equivalence and its exactly arithmetic, base-independent singular ladder. Generalized Cesàro matrices and geometric Rhaly matrices in related spectral literature concern different coefficient regimes; none of the inspected matching claims implies this sparse-row example.

## Limitations
The exact law is proved for the particular geometric-support and square-root-amplitude family, not general terraced or factorable matrices. The claim is not that Meixner spectral theory itself is new. Some classical special-function or Jacobi-matrix representations could furnish equivalent operator-level spectral consequences not found in the searched literature; independent publication-priority verification remains appropriate. The sparse Rhaly operator has an infinite-dimensional zero singular subspace; the theorem does not assert injectivity or describe every singular vector of the full-space operator. Numerical truncation is not used to justify the infinite spectral conclusion.

## References
1. Carlo Bellavita, Eugenio Dellepiane and Georgios Stylogiannis, *Rhaly operators on weighted Hardy spaces and factorable matrices*, arXiv:2606.15875v1 (publicly posted 2026-06-14), https://arxiv.org/abs/2606.15875.
2. Carlo Bellavita, Eugenio Dellepiane and Georgios Stylogiannis, *Schatten class for Rhaly matrices and spaces of analytics functions*, arXiv:2503.21930 (2025), https://arxiv.org/abs/2503.21930.
3. NIST Digital Library of Mathematical Functions, §§18.19 and 18.22, Meixner orthogonality and recurrence, https://dlmf.nist.gov/18.22 and https://dlmf.nist.gov/18.19.
4. Dongbin Xiu and George Em Karniadakis, *The Wiener–Askey Polynomial Chaos for Stochastic Differential Equations*, SIAM Journal on Scientific Computing 24 (2002), 619–644, appendix A.2.3, doi:10.1137/S1064827501387826.
