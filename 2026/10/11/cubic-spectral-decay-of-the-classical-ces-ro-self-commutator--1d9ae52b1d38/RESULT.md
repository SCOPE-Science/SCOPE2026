# Cubic spectral decay of the classical Cesàro self-commutator

## Finding
For the classical Cesàro averaging operator \(C\) on \(\ell^2(\mathbb N_0)\), its self-commutator \(K=C^*C-CC^*\) is positive, injective, and trace class, with exact trace \(1\). Write its eigenvalues in nonincreasing order as \(\lambda_1(K)\ge\lambda_2(K)\ge\cdots>0\). The sharp polynomial order is cubic: for every integer \(n\ge1\),
\[
\lambda_n(K)\ge\frac{1}{48n^3},
\]
whereas for every integer \(n\ge2\),
\[
\lambda_{7n+1}(K)\le\frac{4}{n^3}.
\]
Consequently \(\lambda_n(K)\asymp n^{-3}\), and \(K\) belongs to the Schatten class \(\mathcal S_p\) exactly for real \(p>1/3\); at the endpoint it lies in the weak Schatten class \(\mathcal S_{1/3,\infty}\), but not \(\mathcal S_{1/3}\). The estimate is quantitative rather than an exact leading asymptotic coefficient.

## Assumptions and scope
Let \(H=\ell^2(\mathbb N_0)\) over the complex field, with its standard orthonormal basis \((e_j)_{j\ge0}\). Define \((Cx)_j=(j+1)^{-1}\sum_{k=0}^j x_k\) for each \(j\ge0\). The classical Hardy inequality ensures \(C\in\mathcal B(H)\). Define \(K=C^*C-CC^*\). We index decreasing positive eigenvalues starting at \(1\). For \(0<p<1\), \(\mathcal S_p\) means the usual Schatten quasi-ideal. The weak class \(\mathcal S_{1/3,\infty}\) means \(\sup_{n\ge1}n^3\lambda_n(K)<\infty\).

## Proof
**1. Exact positive Gram representation.** The matrix of \(C\) is \(C_{ji}=(j+1)^{-1}\mathbf1_{\{i\le j\}}\). Consequently
\[
(C^*C)_{ij}=\sum_{k=\max(i,j)}^\infty\frac1{(k+1)^2},\qquad
(CC^*)_{ij}=\frac1{\max(i,j)+1}.
\]
Define \(d_j=\sum_{k=j}^\infty(k+1)^{-2}-(j+1)^{-1}\), so \(K_{ij}=d_{\max(i,j)}\). The differences are
\[
a_j=d_j-d_{j+1}=\frac1{(j+1)^2(j+2)}>0.
\]
Writing \(v_j=e_0+\cdots+e_j\), summing \(d_m=\sum_{j\ge m}a_j\) yields the trace-norm convergent positive expansion
\[
K=\sum_{j=0}^\infty a_jv_jv_j^*,\quad
\langle Kx,x\rangle=\sum_{j=0}^\infty a_j\left|\sum_{k=0}^j x_k\right|^2.
\]
Trace-norm convergence follows from \(\sum_{j\ge0}a_j\|v_j\|^2=\sum_{j\ge0}[(j+1)(j+2)]^{-1}=1\). Thus \(K\ge0\), \(\operatorname{Tr}K=1\), and \(K\) is compact. If the displayed quadratic form vanishes, all partial sums vanish and hence \(x=0\). Therefore \(K\) is injective and has infinitely many positive eigenvalues.

**2. Lower min--max bound.** For an integer \(n\ge1\) take \(E_n=\operatorname{span}\{e_n,\ldots,e_{2n-1}\}\), of dimension \(n\). For \(x\in E_n\), let \(s_j=\sum_{k=n}^j x_k\) for \(n\le j\le2n-1\), with \(s_{n-1}=0\). Since \(x_j=s_j-s_{j-1}\), the triangle inequality for the unilateral shift on this finite block gives \(\sum_{j=n}^{2n-1}|s_j|^2\ge\|x\|^2/4\). Also
\[
a_{2n-1}=\frac1{(2n)^2(2n+1)}\ge\frac1{12n^3}.
\]
Retaining just these nonnegative summands in the Gram form yields \(\langle Kx,x\rangle\ge\|x\|^2/(48n^3)\). The Courant--Fischer principle on \(E_n\) gives the first inequality.

**3. Upper min--max bound.** Fix integer \(n\ge2\). Let \(J=\lceil2\log_2 n\rceil\) and \(M=2^Jn\). Then \(M\ge n^3\) and \(J\le2n\). Form a closed subspace \(F_n\) by requiring: the first \(n\) coordinates of \(x\) vanish; and, for every \(0\le j<J\), partition the consecutive band \(I_j=\{2^jn,\ldots,2^{j+1}n-1\}\) into consecutive blocks of length at most \(L_j=\lceil2^{3j/2}\rceil\), requiring the sum of \(x_k\) on each block to be zero. Since each band contains \(2^jn\) indices and needs at most \(2^jn/L_j+1\le n2^{-j/2}+1\) blocks, the number of independent or redundant linear conditions is at most
\[
n+\sum_{j=0}^{J-1}(n2^{-j/2}+1)
\le(3+\sqrt2)n+J\le(5+\sqrt2)n<7n.
\]
Thus \(\operatorname{codim}F_n\le7n\).

For \(x\in F_n\), the prefix sum of \(x\) is zero at the start of each block. On any block \(B\subset I_j\), Cauchy--Schwarz gives
\[
\sum_{m\in B}a_m\left|\sum_{k\in B,\ k\le m}x_k\right|^2
\le \frac{L_j^2}{(2^jn)^3}\sum_{k\in B}|x_k|^2
\le\frac4{n^3}\sum_{k\in B}|x_k|^2,
\]
because \(L_j\le2^{3j/2}+1\le2\cdot2^{3j/2}\). In the tail \(m\ge M\), the prefix sum of all earlier coordinates still vanishes. Another Cauchy--Schwarz bound gives
\[
\sum_{m\ge M}a_m\left|\sum_{k=M}^m x_k\right|^2
\le\|x_{\{M,M+1,\ldots\}}\|^2\sum_{m\ge M}\frac1{(m+1)^2}
\le\frac{\|x_{\{M,M+1,\ldots\}}\|^2}{M}
\le\frac{\|x_{\{M,M+1,\ldots\}}\|^2}{n^3}.
\]
Adding the disjoint band and tail contributions proves \(\langle Kx,x\rangle\le4n^{-3}\|x\|^2\) for every \(x\in F_n\). The upper Courant--Fischer principle gives \(\lambda_{7n+1}(K)\le4n^{-3}\).

**4. Sharp Schatten threshold.** The preceding min--max bounds imply two-sided estimates \(c n^{-3}\le\lambda_n(K)\le Cn^{-3}\) for all \(n\ge1\), with absolute constants \(c,C>0\) (adjust \(C\) for finitely many initial eigenvalues). Therefore \(\sum\lambda_n(K)^p<\infty\) exactly when \(3p>1\). Moreover \(\sup_n n^3\lambda_n(K)<\infty\), while \(\sum\lambda_n(K)^{1/3}\) diverges.

## Verification
Run the included \(\texttt{verify_cesaro_commutator.py}\) using Python 3 with its standard library. The program verifies finite rational Gram identities, rational trace identities, block counting, and finite-dimensional matrix inequalities. These computational tests check coefficients and construction arithmetic only; the infinite-dimensional min--max proof above is the basis for the result.

## Relationship to prior work
The classical Cesàro operator is standard; its Hardy-space Toeplitz-algebra membership is the subject of Yuanqi Sang, *The Cesàro Operator is in the Toeplitz Algebra*, arXiv:2608.25740 (first public 2026-08-26). Earlier Berger--Shaw theory gives trace-class self-commutators for rationally cyclic hyponormal operators; Feldman's treatment provides trace and compactness results but not this operator-specific cubic eigenvalue law. Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193, supplies hyponormality and weighted quadratic bounds rather than the exact \(\mathcal S_p\) cutoff for the ordinary operator. The cubic lower and upper min--max estimates are proved explicitly here and do not follow from trace class alone.

## Limitations
The result gives polynomial comparability and the sharp Schatten-class cutoff, not an exact asymptotic prefactor for \(n^3\lambda_n(K)\). It applies to the ordinary Cesàro matrix, not to all generalized Cesàro matrices. Full text of the motivating 2026 Toeplitz-algebra manuscript was unavailable in the attempted lawful sources, leaving a bibliographic overlap risk; no claim of independent external verification is made.

## References
1. Yuanqi Sang, *The Cesàro Operator is in the Toeplitz Algebra*, arXiv:2608.25740v1 (2026-08-26), https://arxiv.org/abs/2608.25740.
2. Nathan S. Feldman, *The Self-Commutator of a Subnormal Operator*, doctoral thesis, University of Tennessee (1997), https://feldman.academic.wlu.edu/papers/the-self-commutator-of-a-subnormal-operator/.
3. Yicen Ma, *Hyponormality of Generalized Cesàro Matrices of Every Positive Integer Order*, arXiv:2610.00193v1 (2026), https://arxiv.org/abs/2610.00193.
4. Relevant published comparisons retrieved via semantic mathematical research search: *Trace-class Mellin semigroup defects and zeta traces for Cesaro powers* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-zeta-trace-cesaro-mellin-defects--b8e60639c683; and *A quasinilpotent Schatten self-commutator counterexample* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-quasinilpotent-schatten-selfcommutator-counterexample--8ac62c6f153b.
