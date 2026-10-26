# Pell resonances in cubic spherical-harmonic sampling on hypersimplices

## Finding

Let \(n\ge5\) and \(2\le k\le\lfloor n/2\rfloor\) be integers. Embed the vertices of the \(k\)-th hypersimplex as the spherical set
\[
X_{n,k}=\left\{x_S=\frac{{\bf1}_S-(k/n){\bf1}}{\sqrt{k(n-k)/n}}:\ S\subseteq\{1,\ldots,n\},\ |S|=k\right\}\subset S^{n-2}.
\]
Let \(\mathcal H_3\) be the real degree-three homogeneous harmonic polynomials on the \((n-1)\)-dimensional zero-sum subspace, restricted to its unit sphere, with normalized surface \(L^2\) norm. Define \(E:\mathcal H_3\to\mathbb R^{\binom nk}\) by \((Ef)(S)=f(x_S)/\sqrt{\dim\mathcal H_3}\). Set \(G=EE^*\), \(N=\binom nk\), \(K=k(n-k)\), \(h=n-2k\), and \(D=K^2(n-1)(n-2)^2\).

The complete spectrum of \(G\) consists of the following four scalar levels, each on a Johnson harmonic sector \(U_j\) of multiplicity \(m_j=\binom nj-\binom n{j-1}\) (where \(\binom n{-1}=0\)):
\[
\begin{aligned}
\frac{\lambda_0}{N}&=\frac{(n+1)h^2}{K(n-1)(n-2)^2},\\
\frac{\lambda_1}{N}&=\frac{n\,[n(n+1)-6K]^2}{D(n-3)},\\
\frac{\lambda_2}{N}&=\frac{6n(k-1)(n-k-1)(n+1)h^2}{D(n-4)(n-3)},\\
\frac{\lambda_3}{N}&=\frac{6n^2(k-2)(k-1)(n+1)(n-k-1)(n-k-2)}{D(n-5)(n-4)(n-3)}.
\end{aligned}
\]
Only levels \(0\le j\le\min(k,3)\) are present; the formula for \(\lambda_3\) is used only when \(k\ge3\). Every higher Johnson sector has eigenvalue zero.

For \(k<n/2\), all permitted levels are strictly positive except that \(\lambda_1=0\) precisely when
\[
(n-1)^2-3(n-2k)^2=1.
\]
These exceptional pairs form an infinite Pell family: writing
\[
a_r+b_r\sqrt3=(2+\sqrt3)^r,\qquad n_r=a_r+1,\qquad k_r=(n_r-b_r)/2,\qquad r\ge2,
\]
the first pairs \((n_r,k_r)\) are \((8,2)\), \((27,6)\), \((98,21)\), and \((363,77)\). At each exceptional pair, precisely the \((n-1)\)-dimensional sector \(U_1\), consisting of functions \(S\mapsto\sum_{i\in S}a_i\) with \(\sum_{i=1}^n a_i=0\), is additionally missing from the sampling image. Thus the degree-three image rank at nonbalanced parameters is
\[
\operatorname{rank}E=\binom n{\min(k,3)}-(n-1)\,\mathbf1_{\{n(n+1)=6k(n-k)\}}.
\]
At the balanced parameter \(n=2k\), antipodal complement symmetry removes exactly \(U_0\oplus U_2\). The remaining \(U_1\oplus U_3\) has rank \(\binom n3-\binom n2+n-1\).

## Assumptions and scope

All parameters are integers with \(n\ge5\) and \(2\le k\le\lfloor n/2\rfloor\); a complementary pair of subsets is counted as two separate observations whenever their vertices are distinct. The normalized surface measure is the probability measure, and the harmonic evaluation is divided by \(\sqrt{\dim\mathcal H_3}\). The eigenvalue formulas refer to the output Gram matrix, not the unnormalized sampling matrix. For \(k=2\), the \(j=3\) sector is absent. The zero eigenvalues in sectors \(j\ge4\) arise from the fixed harmonic degree, not from an arithmetic resonance.

## Proof

The inner product of two sampled vertices depends only on \(t=|S\cap T|\):
\[
\langle x_S,x_T\rangle=\frac{nt-k^2}{k(n-k)}.
\]
The addition formula for degree-three spherical harmonics on the \((n-2)\)-sphere, normalized to value one at the diagonal, is
\[
Q_3(u)=\frac{(n+1)u^3-3u}{n-2}.
\]
Hence \(G_{S,T}=Q_3((nt-k^2)/K)\), a polynomial of degree three in \(t\).

For \(r\in\{0,1,2,3\}\), let \(W_r\) be the incidence matrix between \(k\)-subsets and \(r\)-subsets: \((W_r)_{S,R}=\mathbf1_{\{R\subseteq S\}}\). Then \((W_rW_r^*)_{S,T}=\binom{|S\cap T|}{r}\). Write \(P(t)=Q_3((nt-k^2)/K)=\sum_{r=0}^3 c_r\binom tr\), with \(c_r=\sum_{i=0}^r(-1)^{r-i}\binom riP(i)\). Consequently \(G=\sum_{r=0}^3c_rW_rW_r^*\).

The nested incidence-image filtration \(V_j=\operatorname{im}W_j\) (with \(V_{-1}=0\)) yields the orthogonal Johnson sectors \(U_j=V_j\ominus V_{j-1}\). The classical incidence diagonalization, obtainable by counting subsets containing a fixed \(j\)-subset and annihilating lower incidence levels, gives
\[
W_rW_r^*\big|_{U_j}=\begin{cases}
\binom{k-j}{r-j}\binom{n-r-j}{k-r}\,I,&j\le r,\\
0,&j>r.
\end{cases}
\]
Here \(\dim U_j=\binom nj-\binom n{j-1}\) for \(0\le j\le k\) because \(n\ge2k\). Inserting the finite-difference coefficients \(c_r\) and factoring the resulting rational expressions gives the four displayed levels; the exact symbolic equalities are checked by the standalone script. This also shows no sector \(j\ge4\) contributes.

Every factor in \(\lambda_3\), whenever that sector exists, is strictly positive in the stated range. The displayed formulas show that \(\lambda_0\) and \(\lambda_2\) vanish if and only if \(h=0\), and \(\lambda_1\) vanishes if and only if \(n(n+1)=6K\). Setting \(h=n-2k\), this last equation rearranges to \((n-1)^2-3h^2=1\). Since \(h>0\) off the balanced slice, its positive integer solutions are exactly \(n-1+h\sqrt3=(2+\sqrt3)^r\); the constraints \(n\ge5\) and \(k\ge2\) begin at \(r=2\). The eigenvector characterization of \(U_1\) identifies the missing sector explicitly, while the dimension sums yield the rank formulas.

## Verification

Run `python checker.py` with Python 3, NumPy, and SymPy in the same directory. `checker_output.txt` records its result. It checks the four exact symbolic Johnson eigenvalue identities independently through the finite-difference expansion; compares nine directly assembled Gram matrices (all entries evaluated using exact rational arithmetic before floating conversion) against the four-sector spectrum; and verifies four large Pell instances with exact integers. The direct-matrix eigenvalue errors are below \(4\times10^{-15}\). The infinite theorem depends on the algebraic proof and standard incidence diagonalization, not on bounded numerical tests.

## Relationship to prior work

The earlier inclusion-matrix framework of Ghorbani and collaborators (2007) organizes the subset-incidence operators used in the proof. Krebs and Shaheen (2008) prove the Eberlein-polynomial description of Johnson-graph adjacency spectra, providing the finite association-scheme diagonalization machinery. Bannai, Okuda, and Tagami (2013) develop the harmonic-index design formalism and Gegenbauer reproducing kernels; Zhu and collaborators (2015) investigate tight harmonic-index designs. The new classification here concerns the **entire cubic-harmonic evaluation image of every spherical hypersimplex**, and the exact infinite Pell set of rank collapses. The cited background does not state that arithmetic rank-defect classification in its inspected sections. A more general association-scheme formula can in principle be specialized to this kernel; no priority claim is made for that general machinery.

## Limitations

Only exact degree three is classified. The eigenvalues are those of the output Gram matrix in the specified normalization; they do not imply a dimension-uniform lower frame bound. General Johnson-scheme diagonalization is classical, so an older unpublished or differently phrased specialization to cubic harmonic evaluations may cover the Pell locus. Full historical uniqueness and an independent mathematical audit have not been established.

## References

1. E. Ghorbani, G. B. Khosrovshahi, Ch. Maysoori, M. Mohammad-Noori, “Inclusion Matrices and Chains,” arXiv:`0709.3144v1`, public September 20, 2007.
2. M. Krebs and A. Shaheen, “On the spectra of Johnson graphs,” *Electronic Journal of Linear Algebra* **17** (2008), 154–167. DOI: `10.13001/1081-3810.1256`.
3. E. Bannai, T. Okuda, M. Tagami, “Spherical designs of harmonic index \(t\),” arXiv:`1308.5101v1`, public August 23, 2013.
4. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, “More on spherical designs of harmonic index \(t\),” arXiv:`1507.05373`, first public July 20, 2015.
