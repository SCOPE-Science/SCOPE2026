# Exact Laplacian spectrum and spanning-tree count of two-token complete-bipartite graphs

## Finding

Let \(m,n\ge 3\) be integers, set \(t=m+n\), and let \(F_2(K_{m,n})\) denote the graph of unordered pairs of distinct vertices of \(K_{m,n}\), with two pairs adjacent when moving one token along one original edge transforms the first into the second without collision. Its Laplacian characteristic polynomial, with \(z\) denoting the indeterminate, is

\[
\begin{aligned}
\det(zI-L)={}&z(z-t)(z-2t+2)\\
&\cdot(z-2n)^{m(m-3)/2}(z-2m)^{n(n-3)/2}\\
&\cdot(z-t+2)^{(m-1)(n-1)}\\
&\cdot(z-n)^{m-1}(z-m-2n+2)^{m-1}\\
&\cdot(z-m)^{n-1}(z-2m-n+2)^{n-1}.
\end{aligned}
\]

All multiplicities are nonnegative integers in the stated domain; coincident factors are to be multiplied. In particular the entire spectrum is integral, with at most ten distinct eigenvalues. The number \(\tau_{m,n}\) of spanning trees is

\[
\begin{aligned}
\tau_{m,n}={}&4(2n)^{m(m-3)/2}(2m)^{n(n-3)/2}(t-2)^{(m-1)(n-1)}\\
&\quad\cdot\bigl[n(m+2n-2)\bigr]^{m-1}
\bigl[m(2m+n-2)\bigr]^{n-1}.
\end{aligned}
\]

The new classification is the full explicit factorization and associated spanning-tree product, **not** the already-known general assertion that token graphs of cographs have integral Laplacian spectra, nor the already-known algebraic connectivity of token graphs of complete bipartite graphs.

## Assumptions and scope

All graphs are finite, simple and unweighted. \(K_{m,n}\) has fixed left and right vertex parts \(A\), \(B\) of sizes \(m,n\). A two-token configuration is a two-element subset of \(A\cup B\). No move may place both tokens on one vertex. The Laplacian is the combinatorial matrix \(L=D-\mathrm{Adj}\), not the normalized Laplacian. The matrix-tree count is for labeled vertices of the resulting token graph; the theorem does not classify the critical-group invariant factors. The lower bounds \(m,n\ge3\) ensure the incidence maps used in the proof are surjective.

## Proof

Partition the \(\binom t2\) token configurations into \(AA=\binom A2\), \(AB=A\times B\), and \(BB=\binom B2\). Their degrees are, respectively, \(2n\), \(t-2\), and \(2m\). There are \(mn(t-2)\) exchange edges.

For a set of size \(r\ge3\), let \(T_r:\mathbb R^{\binom r2}\to\mathbb R^r\) be the unsigned complete-graph edge-incidence map \(T_r e_{\{i,j\}}=e_i+e_j\). Direct multiplication gives
\[
T_rT_r^{\mathsf T}=(r-2)I_r+J_r.
\]
Hence \(T_r\) has rank \(r\), \(\dim\ker T_r=\binom r2-r=r(r-3)/2\), and the restriction of \(T_rT_r^{\mathsf T}\) to the zero-sum coordinate subspace is the scalar \(r-2\).

Under the real orthogonal decomposition of \(\mathbb R^A\) and \(\mathbb R^B\) into constants and zero-sum vectors, and of the two-pair spaces into incidence-image and incidence-kernel pieces, the token Laplacian separates into six kinds of invariant subspaces:

1. \(\ker T_m\) in \(AA\) has eigenvalue \(2n\), multiplicity \(m(m-3)/2\); \(\ker T_n\) in \(BB\) has eigenvalue \(2m\), multiplicity \(n(n-3)/2\).
2. The tensor product of the two zero-sum spaces inside \(AB\) has eigenvalue \(t-2\), multiplicity \((m-1)(n-1)\).
3. For each of the \(m-1\) standard directions of \(A\), the coupling between \(AA\) and \(AB\) is represented in an orthonormal basis by
\[
\begin{pmatrix}
2n&-\sqrt{n(m-2)}\\
-\sqrt{n(m-2)}&t-2
\end{pmatrix}.
\]
Its characteristic polynomial factors as \((z-n)(z-m-2n+2)\).
4. For each of the \(n-1\) standard directions of \(B\), the corresponding block is
\[
\begin{pmatrix}
2m&-\sqrt{m(n-2)}\\
-\sqrt{m(n-2)}&t-2
\end{pmatrix},
\]
with characteristic polynomial \((z-m)(z-2m-n+2)\).
5. Finally the three-dimensional space of vectors constant on each of \(AA,AB,BB\) has quotient matrix
\[
Q=\begin{pmatrix}
2n&-2n&0\\
-(m-1)&t-2&-(n-1)\\
0&-2m&2m
\end{pmatrix}
\]
and characteristic polynomial \(z(z-t)(z-2t+2)\).

For clarity, these five displayed items list the two kernel spaces separately within the first item: together they account for all dimensions. In each coupling, off-diagonal adjacency is precisely the complete-graph unsigned incidence map tensored with a part-constant vector, so no additional invariant space is omitted. Summing all listed dimensions gives \(\binom t2\). Multiplying the block characteristic polynomials proves the asserted factorization.

All nonzero displayed eigenvalues are strictly positive for \(m,n\ge3\), so the zero eigenvalue is simple. By the matrix-tree theorem, \(\tau_{m,n}\) is their product divided by the number \(\binom t2\) of token configurations. The two nonzero constant-block eigenvalues contribute
\[
\frac{t(2t-2)}{\binom t2}=4.
\]
The paired standard-direction eigenvalue products are \(n(m+2n-2)\) and \(m(2m+n-2)\). Multiplying the remaining scalar factors gives the asserted spanning-tree formula.

## Verification

The included `verify_primary.py` constructs each token Laplacian directly from possible single-token moves, then compares its **exact** integer characteristic polynomial and an exact reduced-Laplacian determinant with the two formulas for \((m,n)\in\{(3,3),(3,4),(3,5),(4,4),(4,5)\}\). It reproduces spanning-tree counts \(199148544\) for \((3,3)\), \(40310784000000\) for \((3,4)\), \(83985958291540377600\) for \((3,5)\), \(676302730297344000000\) for \((4,4)\), and \(146876009148194068050739200000\) for \((4,5)\).

Independently, `verify_alt.cpp` constructs the same token Laplacian by iterating over each base edge and each third, stationary token, then checks predicted eigenvalue nullities and the matrix-tree cofactor modulo \(1000000007\). It checks eight parameter pairs including \((6,7)\). Both scripts are standalone and enumerate only finite cases: the theorem for all \(m,n\ge3\) is established by the preceding block decomposition, not by extrapolating computations.

Reproduce using Python 3 with SymPy (`python3 verify_primary.py`) and a C++17 compiler (`g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt && ./verify_alt`).

## Relationship to prior work

Fabila-Monroy and coauthors introduced the standard token-graph framework in their original publicly available 2009 paper, which treats connectivity, diameter, cliques, colourings, Hamiltonian paths, and products [1], not this spectral and spanning-tree product. Dalfó and coauthors proved general Laplacian spectrum inclusion and complement relations and specifically determined the algebraic connectivity for \(F_k(K_{m,n})\) [2]; that connectivity value is not claimed as new. Reyes, Dalfó, and Fiol strengthened the common commuting-algebra framework for token graph Laplacians [3]. Verma proved that all token graphs of cographs are Laplacian integral [4], which already implies integrality here because \(K_{m,n}\) is a cograph. This paper's contribution is the explicit full multiplicity-resolved spectrum and closed Kirchhoff product. Such a product is not displayed in the inspected full texts, although the general spectral methods provide related starting points.

## Limitations

This is a result for exactly two indistinguishable tokens and \(m,n\ge3\); no statement is made for a higher token number, weighted edges, or the complete Smith normal form of the Laplacian. Exact finite checks cover only the listed cases. Search coverage is not a guarantee of publication priority, and an equivalent product identity could exist in unindexed literature or follow through a different specialization of the known commuting-algebra machinery.

## References

1. R. Fabila-Monroy, D. Flores-Peñaloza, C. Huemer, F. Hurtado, J. Urrutia, D. R. Wood, *Token Graphs*, arXiv:0910.4774v1, first public 2009-10-25, https://arxiv.org/abs/0910.4774.
2. C. Dalfó et al., *On the Laplacian spectra of token graphs*, arXiv:2012.00808v1 (2020), https://arxiv.org/abs/2012.00808.
3. M. A. Reyes, C. Dalfó, M. A. Fiol, *On two algebras of token graphs*, arXiv:2403.18800 (2024), https://arxiv.org/abs/2403.18800.
4. P. Verma, *Laplacian spectral radius and integrality of token graphs*, Electronic Journal of Linear Algebra 42 (2026), 27–38, https://journals.uwyo.edu/index.php/ela/article/download/10053/7371/28463.
