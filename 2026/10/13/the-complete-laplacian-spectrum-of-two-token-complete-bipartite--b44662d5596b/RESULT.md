# The complete Laplacian spectrum of two-token complete bipartite graphs

## Finding

For all integers \(m,n\ge2\), the entire combinatorial Laplacian spectrum of the two-token graph \(F_2(K_{m,n})\), including algebraic multiplicities, is given by the following table. The graph has \(\binom{m+n}{2}\) vertices. An entry appears only when its listed condition holds; if distinct rows give the same numerical eigenvalue, their multiplicities are added.

| Laplacian eigenvalue | Multiplicity | Condition |
| --- | --- | --- |
| \(0\) | \(1\) | all \(m,n\ge2\) |
| \(m+n\) | \(1\) | all |
| \(2(m+n-1)\) | \(1\) | all |
| \(m+n-2\) | \((m-1)(n-1)\) | all |
| \(n\) | \(m-1\) | all |
| \(m+2n-2\) | \(m-1\) | \(m\ge3\) |
| \(m\) | \(n-1\) | all |
| \(2m+n-2\) | \(n-1\) | \(n\ge3\) |
| \(2n\) | \(m(m-3)/2\) | \(m\ge4\) |
| \(2m\) | \(n(n-3)/2\) | \(n\ge4\) |

One exact consequence is the spanning-tree count. Put \(\varepsilon_a=1\) if \(a\ge3\), otherwise \(\varepsilon_a=0\), and \(d_a=\max\{0,a(a-3)/2\}\). Then

\[
\begin{aligned}
\tau(F_2(K_{m,n}))={}&4(m+n-2)^{(m-1)(n-1)}n^{m-1}m^{n-1}\\
&\cdot(m+2n-2)^{(m-1)\varepsilon_m}
(2m+n-2)^{(n-1)\varepsilon_n}\\
&\cdot (2n)^{d_m}(2m)^{d_n}.
\end{aligned}
\]

The integrality of this spectrum is already implied by the known theorem that token graphs of cographs are Laplacian integral; integrality itself is **not** an originality claim here. The new assertion is the explicit, parameter-uniform eigenvalue *multiset with multiplicities*, and its exact spanning-tree enumeration.

## Assumptions and scope

All graphs are finite, undirected and simple. The base graph \(K_{m,n}\) has disjoint independent shores \(A\) and \(B\) of sizes \(m\) and \(n\). Vertices of \(F_2(K_{m,n})\) are two-element subsets of \(A\cup B\); two such subsets are adjacent if their symmetric difference is one edge of the base graph. The Laplacian is the unnormalized combinatorial matrix \(L=D-\mathsf A\). Multiplicities are algebraic (equivalently geometric, since this matrix is symmetric). No regularity or balance assumption is made. The size-two exceptions in the table are essential.

## Proof

Partition token configurations as \(X_A=\binom A2\), \(Y=A\times B\), and \(X_B=\binom B2\). Their token degrees are respectively \(2n\), \(m+n-2\), and \(2m\). Let \(M_a\) denote the unsigned incidence matrix of two-subsets of an \(a\)-set versus its individual elements. The Laplacian therefore has the symmetric block form

\[
L=\begin{pmatrix}
2nI&-T_A^{\mathsf T}&0\\
-T_A&(m+n-2)I&-T_B\\
0&-T_B^{\mathsf T}&2mI
\end{pmatrix},
\]

where \(T_A\) repeats the \(a\)-indexed incidence vector \(M_mf\) in each of the \(n\) columns of \(Y\), while \(T_B\) repeats \(M_ng\) in each of the \(m\) rows. This description follows directly by counting token moves from each of the three classes; it fixes the normalization without relying on a spectral-radius bound.

The key incidence identity, checked by counting shared two-subsets, is

\[
M_aM_a^{\mathsf T}=(a-2)I_a+J_a.
\]

For \(a\ge3\), \(M_a\) has rank \(a\); on the zero-sum subspace \(U_a=\mathbf1_a^\perp\) its nonzero squared singular value is \(a-2\), whereas on constants it is \(2(a-1)\). For \(a=2\), \(M_a\) has rank one and its zero-sum singular sector is absent. For \(a\ge3\), the orthogonal decomposition of \(\mathbb R^{\binom a2}\) is the direct sum of its constant line, \(M_a^{\mathsf T}U_a\), and \(\ker M_a\); the kernel has dimension \(a(a-3)/2\). For \(a=2\), only the constant line remains.

Decompose the mixed block as the four orthogonal tensor-product spaces

\[
\mathbb R^{A\times B}=
(\langle\mathbf1_m\rangle\otimes\langle\mathbf1_n\rangle)
\oplus(U_m\otimes\langle\mathbf1_n\rangle)
\oplus(\langle\mathbf1_m\rangle\otimes U_n)
\oplus(U_m\otimes U_n).
\]

The constant lines from all three token types make an invariant three-dimensional space. In the (not necessarily orthonormal) basis of indicator vectors of \(X_A,Y,X_B\), its quotient is

\[
Q=\begin{pmatrix}
2n&-2n&0\\
-(m-1)&m+n-2&-(n-1)\\
0&-2m&2m
\end{pmatrix}.
\]

A direct characteristic-polynomial calculation gives \(\det(tI-Q)=t(t-m-n)(t-2(m+n-1))\), yielding the three simple eigenvalues in the first rows of the table.

The mixed sector \(U_m\otimes U_n\) is annihilated by both off-diagonal incidence couplings, so it has eigenvalue \(m+n-2\) and dimension \((m-1)(n-1)\).

For \(m\ge3\), each of the \(m-1\) standard \(U_m\)-directions couples one vector in \(M_m^{\mathsf T}U_m\subseteq X_A\) to one vector in \(U_m\otimes\langle\mathbf1_n\rangle\subseteq Y\). In orthonormal coordinates the repeated symmetric block is

\[
\begin{pmatrix}
2n&-\sqrt{n(m-2)}\\
-\sqrt{n(m-2)}&m+n-2
\end{pmatrix}.
\]

Its eigenvalues are \(n\) and \(m+2n-2\), each repeated \(m-1\) times. If \(m=2\), the first subspace vanishes because \(M_2^{\mathsf T}U_2=0\); only the single mixed-block eigenvalue \(n\) remains. Interchanging \(m,n\) proves the corresponding rows \(m\), \(2m+n-2\), including the \(n=2\) exception.

Finally, \(\ker M_m\subseteq X_A\) and \(\ker M_n\subseteq X_B\) are invariant eigenspaces of values \(2n\) and \(2m\), respectively, with the displayed dimensions. These components are pairwise orthogonal and their dimensions sum to \(\binom{m+n}{2}\). Thus no eigenvalues or multiplicities are missing, proving the asserted full spectrum for every permitted pair.

The zero eigenvalue occurs only once, so the token graph is connected. By the Matrix–Tree theorem, \(\tau\) is the product of all nonzero Laplacian eigenvalues divided by \(\binom{m+n}{2}\). Multiplying the table rows gives the stated formula; the prefactor simplifies because

\[
\frac{(m+n)\,2(m+n-1)}{\binom{m+n}{2}}=4.
\]

## Verification

The accompanying `verify.py` constructs each token-graph Laplacian directly from edges of the base graph, not from the incidence-block proof. It uses exact symbolic characteristic polynomials to check **all 36 ordered pairs** with \(2\le m,n\le7\). It separately evaluates exact integer Laplacian cofactors and checks the Matrix–Tree product for \((m,n)=(2,2),(2,3),(3,3),(3,4),(4,4)\). The independently recomputed cofactor values are respectively \(32\), \(10800\), \(199148544\), \(40310784000000\), and \(676302730297344000000\). All exact tests pass. Run `python -m pip install -r requirements.txt` and `python verify.py` in one directory containing the two accompanying files. Finite testing supports, but does not replace, the uniform proof above.

## Relationship to prior work

Song, Dalfó, Fiol and Zhang [1] studied algebraic connectivity and Laplacian spectral radius of token graphs. Their full first-version manuscript gives an equitable three-cell quotient for \(F_2(K_{m,n})\) (Corollary 4.14), yielding \(2(m+n-1)\) as a spectral-radius lower bound, not the complete eigenvalue multiset. The largest eigenvalue alone was previously determined by other work and is not new here. Dalfó and collaborators [2] proved general token-spectrum containment and the algebraic connectivity of complete bipartite token graphs (Theorem 7.2(iv)); their comparison with the complement does not specify the remaining eigenvalues and all their multiplicities. Verma [3], Theorem 3.6, already proves integrality for token graphs of all cographs, encompassing the integrality consequence here; it does not determine the displayed complete multiset or the spanning-tree product. Reyes, Dalfó and Fiol [4] address spectral-radius bounds and quotient spectra for distance-regular base graphs, again not the complete multiset for arbitrary rectangular \(K_{m,n}\).

The 2024 paper of Barik and Verma [5] reports general spectral bounds in its accessible abstract. Its full text was not obtained for a definitive comparison; possible unindexed equivalent results are acknowledged below. The exact full-spectrum statement is stronger than the earlier largest-eigenvalue fact on the same family and is not obtained by merely taking a scalar specialization of any inspected theorem.

## Limitations

This theorem concerns **two** indistinguishable tokens, simple complete bipartite base graphs, and the **unnormalized** Laplacian. It makes no claim for arbitrary token number, weighted edges, or general bipartite graphs. Entries with coincident eigenvalues require multiplicity addition. The finite verifier covers only the stated sample domain; the proof supplies the infinite conclusion. The full text of [5] remained inaccessible, and equivalent unindexed or unpublished statements cannot be excluded. No independent external audit has been performed.

## References

[1] X. Song, C. Dalfó, M. À. Fiol and S. Zhang, *The Algebraic Connectivity and Laplacian Spectral Radius of Token Graphs*, arXiv:2610.00500v1 (first posted 30 September 2026), https://arxiv.org/html/2610.00500v1, esp. Sections 3–4 and Corollary 4.14.

[2] C. Dalfó et al., *On the Laplacian spectra of token graphs*, arXiv:2012.00808v1 (2020), https://arxiv.org/pdf/2012.00808, esp. Sections 3, 5–7 and Theorem 7.2(iv).

[3] P. Verma, *Laplacian spectral radius and integrality of token graphs*, Electronic Journal of Linear Algebra 42 (2026), 27–38, https://doi.org/10.13001/ela.2026.10053, esp. Theorem 3.6.

[4] M. A. Reyes, C. Dalfó and M. À. Fiol, *On the spectra and spectral radii of token graphs*, Boletín de la Sociedad Matemática Mexicana 30 (2024), https://doi.org/10.1007/s40590-023-00583-3, esp. Sections 3 and 5.

[5] S. Barik and P. Verma, *Spectral properties of token graphs*, Linear Algebra and its Applications 687 (2024), 181–206, https://doi.org/10.1016/j.laa.2024.02.004 (abstract consulted; full text unavailable).
