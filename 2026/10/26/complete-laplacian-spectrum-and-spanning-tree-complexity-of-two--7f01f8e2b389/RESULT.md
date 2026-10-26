# Complete Laplacian spectrum and spanning-tree complexity of two-token bicliques

## Finding
Let \(m,n\geq3\) be integers, put \(N=m+n\), and let \(H=F_2(K_{m,n})\) be the graph of unordered pairs of distinct vertices of the complete bipartite graph. Two pairs are adjacent when their symmetric difference is an edge of the biclique. Write \(\lambda^{[r]}\) for an eigenvalue \(\lambda\) with multiplicity \(r\), including zero multiplicities when they occur. The complete Laplacian spectrum, with repeated numerical values combined, is the multiset
\[
\begin{aligned}
\operatorname{Spec}_L(H)=\{&0^{[1]},\ N^{[1]},\ (2N-2)^{[1]},\\
 &n^{[m-1]},\ m^{[n-1]},\\
 &(m+2n-2)^{[m-1]},\ (n+2m-2)^{[n-1]},\\
 &(N-2)^{[(m-1)(n-1)]},\\
 &(2n)^{[m(m-3)/2]},\ (2m)^{[n(n-3)/2]}\}.
\end{aligned}
\]
In particular, the number \(\tau(H)\) of spanning trees is exactly
\[
\boxed{\tau(H)=4\,n^{m-1}m^{n-1}
(m+2n-2)^{m-1}(n+2m-2)^{n-1}
(N-2)^{(m-1)(n-1)}
(2n)^{m(m-3)/2}(2m)^{n(n-3)/2}.}
\]
The previously known spectral-gap and spectral-radius values are recovered as consequences; they are not claimed as original separate results.

## Assumptions and scope
Graphs are finite, simple, unweighted and undirected. The two parts of \(K_{m,n}\) have labelled sets \(A\) and \(B\) of respective sizes \(m\) and \(n\). Token vertices are *unordered* two-subsets, and an edge is allowed only if exactly one token crosses an original graph edge to an unoccupied vertex. The domain \(m,n\geq3\) ensures that the unsigned incidence maps used below have full column rank and all displayed multiplicities are nonnegative. The Laplacian is \(L=D-\mathcal A\), and spanning trees are counted on the labelled token graph.

## Proof
**Step 1: Three layers and block operator.** Partition the token vertices into the layers \(\binom A2\), \(A\times B\), and \(\binom B2\). Their degrees are \(2n\), \(N-2\), and \(2m\), respectively. Let \(B_m\) denote the unsigned vertex-edge incidence matrix of \(K_m\), of shape \(\binom m2\times m\): a row corresponding to \(\{i,j\}\) has ones in columns \(i\) and \(j\). Define \(B_n\) similarly and write \(\mathbf1_r\) for an all-ones vector of length \(r\). With coordinates of the middle layer ordered by \((i,j)\in A\times B\), the symmetric Laplacian block matrix is
\[
L=\begin{pmatrix}
2nI&-B_m\otimes\mathbf1_n^{\mathsf T}&0\\
-B_m^{\mathsf T}\otimes\mathbf1_n&(N-2)I&-\mathbf1_m\otimes B_n^{\mathsf T}\\
0&-\mathbf1_m^{\mathsf T}\otimes B_n&2mI
\end{pmatrix}.
\]
Here the outer row/column spaces are unordered-pair spaces; this displayed tensor notation means that the \(\binom m2\times mn\) block between the first and second layers has coefficient one exactly for pairs sharing an \(A\)-vertex, and similarly for the last layer. Thus it is also an entrywise definition independent of tensor-order conventions.

**Step 2: Orthogonal invariant subspaces.** One has
\[
B_m^{\mathsf T}B_m=(m-2)I_m+J_m,\qquad
B_n^{\mathsf T}B_n=(n-2)I_n+J_n,
\]
where \(J_r=\mathbf1_r\mathbf1_r^{\mathsf T}\). Consequently, \(B_m\) has rank \(m\). Decompose the first outer layer into
\[\operatorname{span}\{B_m\mathbf1_m\}\oplus B_m(\mathbf1_m^\perp)\oplus\ker B_m^{\mathsf T},\]
with dimensions \(1,m-1,m(m-3)/2\). The third layer has the analogous decomposition with \(m\) replaced by \(n\). Split the middle layer orthogonally as
\[
(\mathbf1_m\oplus\mathbf1_m^\perp)\otimes
(\mathbf1_n\oplus\mathbf1_n^\perp).
\]
The tensor-product coupling preserves one constant block, \(m-1\) identical two-dimensional blocks, \(n-1\) other identical two-dimensional blocks, and the unused orthogonal summands. This accounts for the full \(\binom N2\)-dimensional token-vertex space.

**Step 3: Eigenvalues of the blocks.** The first-layer kernel of \(B_m^{\mathsf T}\) is an eigenspace of eigenvalue \(2n\), with dimension \(m(m-3)/2\); the third-layer kernel contributes \(2m\), with dimension \(n(n-3)/2\). The middle-layer space \(\mathbf1_m^\perp\otimes\mathbf1_n^\perp\) contributes \(N-2\), with dimension \((m-1)(n-1)\).

For each unit vector in \(\mathbf1_m^\perp\), normalize its image under \(B_m\) and the corresponding middle-layer tensor with \(\mathbf1_n\). Their Laplacian block is
\[
\begin{pmatrix}
2n&-\sqrt{n(m-2)}\\
-\sqrt{n(m-2)}&N-2
\end{pmatrix}.
\]
Its trace is \(m+3n-2\) and determinant is \(n(m+2n-2)\), so its eigenvalues are \(n\) and \(m+2n-2\), each occurring \(m-1\) times. Likewise the other family has blocks
\[
\begin{pmatrix}
2m&-\sqrt{m(n-2)}\\
-\sqrt{m(n-2)}&N-2
\end{pmatrix},
\]
whose eigenvalues are \(m\) and \(n+2m-2\), each repeated \(n-1\) times.

Using unit constant vectors in the three layers gives the remaining block
\[
C=\begin{pmatrix}
2n&-\sqrt{2n(m-1)}&0\\
-\sqrt{2n(m-1)}&N-2&-\sqrt{2m(n-1)}\\
0&-\sqrt{2m(n-1)}&2m
\end{pmatrix}.
\]
Its determinant is zero because the global constant token-vertex vector lies in its kernel. Its trace is \(3N-2\), and the sum of its principal minors of order two is \(2N(N-1)\). Therefore its eigenvalues are \(0\), \(N\), and \(2(N-1)\). This proves the claimed complete multiset. When some parameter values make eigenvalues coincide, ordinary multiset addition handles those coincidences automatically. Exactly one eigenvalue is zero, so \(H\) is connected.

**Step 4: Spanning trees.** By the matrix-tree theorem, for a connected graph on \(\binom N2\) vertices, its spanning-tree count equals the product of all positive Laplacian eigenvalues divided by \(\binom N2\). The contribution from the two single eigenvalues \(N\) and \(2(N-1)\) cancels the denominator to give \(4\). Substitution of the other blocks gives the displayed exact product for every \(m,n\geq3\). No finite-sampling assumption enters the proof.

## Verification
The accompanying standalone `verify.py` constructs the Laplacian directly from token moves, independently computes its numerical eigenvalues, and compares them with the exact formula for all \(3\leq m\leq6\) and \(m\leq n\leq7\) (14 parameter pairs). It also constructs a principal Laplacian minor and computes its determinant modulo each of two primes, independently verifying the spanning-tree product for nine pairs with \(3\leq m\leq5\) and \(m\leq n\leq6\). It reports `VERIFY_OK spectra_pairs=14 exact_modular_matrix_tree_pairs=9` when these checks pass. These finite tests serve as reproducibility checks, not as a substitute for Steps 1–4.

## Relationship to prior work
Song, Dalfó, Fiol and Zhang (arXiv:2610.00500v1, first submitted 2026-09-30) study algebraic connectivity and Laplacian spectral radii; their Corollary 4.14 gives the quotient lower bound \(2(N-1)\) for the two-token biclique. The fact that the largest Laplacian eigenvalue of a *bipartite* graph is visible in an equitable quotient, recalled by Reyes, Dalfó, Fiol and Messegué (2023, Section 2.2), already upgrades this bound to an equality. Accordingly, that endpoint is not presented as independent novelty here. Earlier work of Dalfó et al. (2021, particularly Theorem 6.2) proves that token-graph Laplacians for a graph and its complement commute and can be paired with the Johnson-graph spectrum. For \(K_{m,n}\), the complement is \(K_m\sqcup K_n\), so that theorem offers an alternative route through spectral alignment, but does not itself list the requisite aligned eigenvalue multiplicities or the spanning-tree product. Reyes et al. (2023) establishes the exact biclique spectral gap. Reyes, Dalfó and Fiol (2024) derive spectral-radius and quotient-eigenvalue information for distance-regular hosts; those partial quotient eigenspaces likewise do not specify the complete multiplicity table here. Verma (2026, Theorem 3.6) proves that token graphs of cographs are Laplacian integral, covering the integrality consequence for bicliques. The present claim is instead the **complete eigenvalue list with all multiplicities and its exact Kirchhoff product**. The accessible primary texts inspected for these comparisons do not state those formulas. A relevant 2024 article of Barik and Verma focuses, in its accessible abstract, on structural properties and eigenvalue bounds; its inaccessible full text is a residual historical-priority risk, not evidence of noncoverage.

## Limitations
The proof treats only two tokens and part sizes at least three. It does not determine spectra for higher token numbers or arbitrary multipartite hosts. The eigenvalue formula recovers known extremal values and known integrality; only the full factorization and consequent spanning-tree product are proposed as new. No independent review or exhaustive historical-priority certification has been performed. The 2024 Barik–Verma article could not be read in full, so an equivalent result hidden in its main text or appendix remains possible.

## References
1. X. Song, C. Dalfó, M. À. Fiol and S. Zhang, *The Algebraic Connectivity and Laplacian Spectral Radius of Token Graphs*, arXiv:2610.00500v1 (2026-09-30), https://arxiv.org/html/2610.00500v1.
2. M. A. Reyes, C. Dalfó, M. À. Fiol and A. Messegué, *On the spectra of token graphs of cycles and other graphs*, Linear Algebra Appl. 679 (2023), 38–66, https://arxiv.org/abs/2309.07089.
3. C. Dalfó, F. Duque, R. Fabila-Monroy, M. À. Fiol, C. Huemer, A. L. Trujillo-Negrete and F. J. Zaragoza Martínez, *On the Laplacian spectra of token graphs*, Linear Algebra Appl. 625 (2021), 322–348, https://arxiv.org/abs/2012.00808.
4. P. Verma, *Laplacian spectral radius and integrality of token graphs*, Electron. J. Linear Algebra 42 (2026), 27–38, https://journals.uwyo.edu/index.php/ela/article/download/10053/7371/28463.
5. S. Barik and P. Verma, *Spectral properties of token graphs*, Linear Algebra Appl. 687 (2024), 181–206, https://doi.org/10.1016/j.laa.2024.02.004 (full text not accessed).
6. M. A. Reyes, C. Dalfó and M. À. Fiol, *On the spectra and spectral radii of token graphs*, Bol. Soc. Mat. Mex. 30 (2024), Article 11, https://link.springer.com/article/10.1007/s40590-023-00583-3.
