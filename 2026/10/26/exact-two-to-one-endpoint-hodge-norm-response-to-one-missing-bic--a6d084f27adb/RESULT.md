# Exact two-to-one endpoint Hodge-norm response to one missing biclique edge

## Finding
Let \(m,n\ge2\) be integers. Let \(G=K_{m,n}-e_0\) be the graph obtained by deleting one edge from the unweighted complete bipartite graph, with its real oriented edge space. Write \(Q_G\) for the Euclidean-orthogonal projection onto the cut subspace, and \(P_G=I-Q_G\) for the Euclidean-orthogonal projection onto the cycle-flow subspace. All edge-space norms below are the induced \(\ell_1\) or \(\ell_\infty\) norms. Put \(t=(m-1)(n-1)\). Then
\[
\|Q_G\|_{1\to1}=\|Q_G\|_{\infty\to\infty}=3-\frac2m-\frac2n+\frac2{mn}-\frac2{mnt},
\]
\[
\|P_G\|_{1\to1}=\|P_G\|_{\infty\to\infty}=\frac{4t}{mn}-\frac4{mnt}.
\]
Both norms decrease strictly relative to the intact biclique, by exactly \(2/(mnt)\) and \(4/(mnt)\), respectively. Their deletion deficits therefore have the exact ratio \(1:2\).

Every retained edge with neither endpoint incident to the missing edge attains both maxima in the absolute column-sum formulas. If \(m,n\ge3\), precisely those edges attain the maxima. At \(m=2\) or \(n=2\), additional ties can occur. The formulas include the tree case \(m=n=2\), when \(Q_G=I\) and \(P_G=0\).

## Assumptions and scope
All edges have unit conductance. The ambient edge space is real, with each edge oriented from the part of size \(m\) to the part of size \(n\); reversing any orientation merely conjugates the projection by a diagonal sign matrix and preserves its endpoint norms. The word *orthogonal* refers to the Euclidean inner product on the edge coordinates, even when measuring operator norms in \(\ell_1\) or \(\ell_\infty\). No claim of minimum norm over all possible, nonorthogonal projections is made.

## Proof
Write the two vertex parts as \(A=\{a_0,\ldots,a_{m-1}\}\) and \(B=\{b_0,\ldots,b_{n-1}\}\), with missing edge \(e_0=(a_0,b_0)\). Let \(D_0\) be the vertex-edge incidence matrix of the intact biclique, \(L_0=D_0D_0^{\mathsf T}\) its Laplacian, and \(b_0\) the incidence column of \(e_0\). Let \(D\) and \(L\) denote the incidence matrix and Laplacian after deletion. On the space of zero-sum vertex vectors, \(L=L_0-b_0b_0^{\mathsf T}\) and \(L_0\) is invertible. The cut projector is \(Q_G=D^{\mathsf T}L^+D\), with \(L^+\) the zero-mean pseudoinverse.

For intact \(K_{m,n}\), direct decomposition into constant and zero-sum vectors on each part gives the following entries of \(Q_0=D_0^{\mathsf T}L_0^+D_0\). If \(e=(a,b)\), \(f=(a',b')\), then \(mn(Q_0)_{f,e}\) equals \(m+n-1\) when \(f=e\); \(m-1\) when \(a=a'\), \(b\ne b'\); \(n-1\) when \(a\ne a'\), \(b=b'\); and \(-1\) when \(a\ne a'\), \(b\ne b'\). Consequently
\[
R_0=b_0^{\mathsf T}L_0^+b_0=\frac{m+n-1}{mn},\qquad 1-R_0=\frac{t}{mn}>0.
\]
The Sherman--Morrison inverse identity on zero-sum vectors yields
\[
L^+=L_0^++\frac{(L_0^+b_0)(L_0^+b_0)^{\mathsf T}}{1-R_0}.
\]
Thus for retained edges \(e,f\),
\[
mn(Q_G)_{f,e}=s(f,e)+\frac{z_fz_e}{t},
\]
where \(s(f,e)=mn(Q_0)_{f,e}\) is classified above, and \(z_e=m-1\) for edges \((a_0,b_j)\) with \(j>0\) (type A), \(z_e=n-1\) for \((a_i,b_0)\) with \(i>0\) (type B), and \(z_e=-1\) for \((a_i,b_j)\) with \(i,j>0\) (type C).

All absolute values in the column sums can be resolved without approximation. For a type-A column, the type-A entries are positive; the type-B entries vanish; its type-C entries equal \(n(n-2)/(n-1)\) if the \(B\)-endpoint is shared and \(-n/(n-1)\) otherwise, after multiplication by \(mn\). Type B is obtained by interchanging \(m,n\). For a type-C column, the type-A entries are respectively \(n(n-2)/(n-1)\) and \(-n/(n-1)\) according to whether the \(B\)-endpoint is shared; the type-B entries are respectively \(m(m-2)/(m-1)\) and \(-m/(m-1)\) according to whether the \(A\)-endpoint is shared. Among type-C entries, the diagonal and entries sharing an endpoint are positive, whereas entries sharing neither endpoint equal \(-1+1/t\le0\), after multiplication by \(mn\). These statements cover the zero boundary cases \(m=2\) or \(n=2\).

Let \(S_A,S_B,S_C\) be the absolute column sums of \(Q_G\) for the three respective edge types. Summing the stated sign classes and their multiplicities gives
\[
S_A=\frac{3mn-5m-2n+4}{m(n-1)},\qquad
S_B=\frac{3mn-2m-5n+4}{n(m-1)},
\]
\[
S_C=3-\frac2m-\frac2n+\frac2{mn}-\frac2{mnt}.
\]
The strictness of the maximizer comparison is explicit:
\[
S_C-S_A=\frac{2(m-2)}{n(m-1)(n-1)},\qquad
S_C-S_B=\frac{2(n-2)}{m(m-1)(n-1)}.
\]
Hence \(\|Q_G\|_{1\to1}=S_C\), with strict inequalities for both other edge types when \(m,n\ge3\).

For every orthogonal projector, the absolute column sum of its complement is \(1+S_e-2Q_{e,e}\), since \(0\le Q_{e,e}\le1\). Using the diagonal values from the rank-one formula above, the absolute column sums \(T_A,T_B,T_C\) of \(P_G=I-Q_G\) are
\[
T_A=\frac{4(m-1)(n-2)}{m(n-1)},\qquad
T_B=\frac{4(m-2)(n-1)}{n(m-1)},
\]
\[
T_C=\frac{4t}{mn}-\frac4{mnt}.
\]
Their gaps are \(T_C-T_A=2(S_C-S_A)\) and \(T_C-T_B=2(S_C-S_B)\), so type C maximizes both complement norms. Both projectors are symmetric matrices, hence the induced \(\ell_\infty\) norms equal the induced \(\ell_1\) norms.

For comparison, the intact biclique's sole edge orbit has projector column sums \(\|Q_0\|=3-2/m-2/n+2/(mn)\) and \(\|I-Q_0\|=4t/(mn)\). Subtracting the deleted-graph formulas proves the strictly positive and exactly two-to-one deficits. This completes the proof for every \(m,n\ge2\).

## Verification
A separate exact-rational implementation builds each punctured biclique directly, inverts its grounded Laplacian, reconstructs every column of the orthogonal cut and cycle projectors, and compares the resulting induced norms and edge-orbit inequalities with these formulas. The included `verify_punctured_biclique.py` tests the full grid \(2\le m,n\le7\): 36 parameter pairs and 693 projector columns. All tests pass. This finite computation corroborates, but is not a substitute for, the symbolic proof for all \(m,n\ge2\).

## Relationship to prior work
The identification of graph transportation spaces with edge \(\ell_1\)-spaces modulo cycles and the projection framework are established in Dilworth--Kutzarova--Ostrovskii (2018, 2023). The latter investigates minimal and invariant cycle-space projections primarily on tori and Hamming graphs. The present statement concerns the canonical *orthogonal* projections, not generally minimal projections, and identifies the exact effect of one missing biclique edge. The intact-biclique formulas can be obtained by standard eigenspace calculations; the punctured-graph maximizer theorem and exact deficits require the rank-one update and complete sign analysis supplied here.

## Limitations
No assertion is made that the canonical projections are norm-minimizing among all linear projections. General deleted matchings, weighted deletions, and arbitrary graph perturbations are not addressed. No universal monotonicity under arbitrary edge deletion is implied. The finite tests cover only \(2\le m,n\le7\). Possible equivalent calculations in specialized electrical-network or projection literature remain a bibliographic risk; no independent mathematical validation is claimed.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first public version 10 July 2018), https://arxiv.org/abs/1807.03814.
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 21 May 2023), https://arxiv.org/abs/2305.12582.
