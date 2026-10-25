# Strict three-leader coherence hierarchy on crown graphs

## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the unweighted crown graph with \(n\ge4\), where \(M_n\) removes the pairs \(a_i b_i\), indexed by \(1\le i\le n\). For any exactly three distinct noise-free leaders \(S\), let \(F=V\setminus S\) and \(J(S)=\operatorname{tr}(L_{FF}^{-1})\), where \(L\) is the combinatorial Laplacian. Every leader triple lies in precisely one of three symmetry classes: \(A\) (all three on one bipartition side); \(M\) (two on one side, one on the other, and at least one deleted-matching pair wholly selected); or \(U\) (two on one side and one on the other, with no deleted-matching pair wholly selected). The costs are constant on each class and are
\[
J_A=\frac{8n^3-31n^2+38n-24}{3n(n-2)(n-1)},\quad
J_M=\frac{8n^3-31n^2+38n-18}{3n(n-2)(n-1)},
\]
\[
J_U=\frac{8n^4-35n^3+56n^2-43n+12}{n(n-1)(3n^2-8n+3)}.
\]
They obey the **strict ordering** \(J_A<J_M<J_U\) for every integer \(n\ge4\). Thus exactly \(2\binom{n}{3}\) unordered triples minimize three-leader grounded coherence: three vertices selected entirely from either bipartition side.

## Assumptions and scope
All \(2n\) vertices are distinct and all existing edges have unit conductance. The bipartition sides are \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\); \(a_i\) and \(b_j\) are adjacent exactly when \(i\ne j\). Three leaders are pinned (noise free), and all remaining nodes are followers. The objective is the **unscaled** inverse-trace cost, so physical steady-state variance under a standard common node-noise model is a constant multiple of this cost. No probabilistic or finite-sample approximations are used. The smallest allowed order here is \(n=4\). The special \(n=3\) crown is the six-cycle, whose optimal evenly spaced leaders are already treated by the earlier cycle theorem in [1].

## Proof
The group of simultaneous permutations of the indices, together with interchange of \(A\) and \(B\), preserves both the graph and the objective. For three vertices, either they are all on one side, or two are on one side and the third is on the other. In the latter case, the third vertex has its missing-matching partner selected among the two or not. Hence there are exactly the three classes stated above, with no unclassified placements.

Write \(d=n-1\). If the follower set contains \(p\) vertices of one side and \(q\) of the other, with \(p\le q\), then the grounded Laplacian is
\[
L_{FF}=\begin{pmatrix}dI_p&-C\\-C^{\mathsf T}&dI_q\end{pmatrix},
\]
where \(C\) is the remaining follower-to-follower bipartite adjacency matrix. If \(\sigma_1,\ldots,\sigma_p\) are its singular values, an orthogonal singular-value decomposition produces paired eigenvalues \(d+\sigma_j,d-\sigma_j\) and \(q-p\) unpaired eigenvalues \(d\). Because the connected graph is grounded at three leaders, the matrix is positive definite; in particular \(\sigma_j<d\). Therefore
\[
\operatorname{tr}(L_{FF}^{-1})=\frac{q-p}{d}+2d\sum_{j=1}^p\frac1{d^2-\sigma_j^2}.\tag{1}
\]

**Class \(A\).** Here \(p=n-3\), \(q=n\), and \(C=\mathbf 1_{p\times n}-P\), where each row of the zero-one matrix \(P\) has one distinct marked column. Thus \(CC^{\mathsf T}=I_p+(n-2)\mathbf1_p\mathbf1_p^{\mathsf T}\), with squared singular values \(1\) of multiplicity \(n-4\) and \(1+(n-2)(n-3)=n^2-5n+7\) once. Equation (1) gives
\[
J_A=\frac3d+2d\left[\frac{n-4}{d^2-1}+\frac1{d^2-(n^2-5n+7)}\right].\tag{2}
\]

**Class \(M\).** Take leaders \(a_1,a_2,b_1\). Here \(p=n-2\), \(q=n-1\), and each follower row has its own distinct missing column present. Consequently \(CC^{\mathsf T}=I_p+(n-3)\mathbf1_p\mathbf1_p^{\mathsf T}\), with squared singular values \(1\) of multiplicity \(n-3\) and \(n^2-5n+7\) once. Then
\[
J_M=\frac1d+2d\left[\frac{n-3}{d^2-1}+\frac1{d^2-(n^2-5n+7)}\right].\tag{3}
\]

**Class \(U\).** Take leaders \(a_1,a_2,b_3\). Put \(m=n-3\), so \(m\ge1\). One follower row has no deleted-matching column among followers, and the remaining \(m\) follower rows have one distinct such column. In this row ordering,
\[
CC^{\mathsf T}=\begin{pmatrix}m+2&(m+1)\mathbf1_m^{\mathsf T}\\(m+1)\mathbf1_m&I_m+m\mathbf1_m\mathbf1_m^{\mathsf T}\end{pmatrix}.
\]
The orthogonal complement of \(\mathbf1_m\) carries eigenvalue \(1\) with multiplicity \(m-1=n-4\). The remaining two eigenvalues are those of the symmetric block
\[
\begin{pmatrix}m+2&(m+1)\sqrt m\\(m+1)\sqrt m&m^2+1\end{pmatrix},
\]
whose trace is \(T=m^2+m+3=n^2-5n+9\) and determinant is exactly \(2\). Combining the two reciprocal denominators in (1) gives
\[
J_U=\frac1d+2d\left[\frac{n-4}{d^2-1}+\frac{2d^2-T}{d^4-Td^2+2}\right].\tag{4}
\]

Substituting \(d=n-1\), using \(d^2-1=n(n-2)\), \(d^2-(n^2-5n+7)=3(n-2)\), and \(d^4-Td^2+2=(n-2)(3n^2-8n+3)\) reduces (2)–(4) to the rational formulas in the finding. Their differences factor exactly as
\[
J_M-J_A=\frac{2}{n(n-2)(n-1)}>0,\tag{5}
\]
\[
J_U-J_M=\frac{2(n-1)(2n^2-9)}{3n(n-2)(3n^2-8n+3)}>0.\tag{6}
\]
For every \(n\ge4\), all denominators are positive, as are \(n-1\) and \(2n^2-9\). Thus the inequalities are strict. Each side contains \(\binom{n}{3}\) possible three-vertex subsets, yielding precisely \(2\binom{n}{3}\) minimizers. This proves the claim.

## Verification
The accompanying `verify.py` symbolically checks the three block-trace identities and both factored differences using exact rational polynomial cancellation. It constructs the original \(2n\)-vertex Laplacian and, for each \(n\in\{3,4,5,6,7,8\}\), exhaustively compares the exact inverse trace of **every** three-vertex leader set with the predicted symmetry-class formula. The \(n=3\) check is an additional boundary verification only; the claimed new strict classification is for \(n\ge4\). The finite tests corroborate, but do not replace, the all-\(n\) spectral proof. Run `python verify.py` with SymPy installed as in `requirements.txt`; the captured deterministic summary is in `verification_output.txt`.

## Relationship to prior work
Fitch and Leonard [1] define joint centrality for noise-free leader sets and solve multiple-leader placement explicitly on paths and cycles. In particular their cycle theorem already covers the \(n=3\) graph \(\operatorname{Cr}_3\cong C_6\), which is not asserted as a new special case. The present result applies instead to the distinct infinite family \(n\ge4\), where crown graphs are regular bipartite networks of diameter three, rather than cycles; it classifies and strictly ranks every symmetry orbit of three-leader choices. Patterson, McGlohon and Dyagilev [2] optimize leader positions using one-dimensional decomposition methods for paths and rings, not crown graphs. These works establish the optimization framework but do not provide equations (2)–(6) or the general crown classification. Similar graph terminology such as "finite crown" can mean a poset rather than this graph; equivalence of objects was checked by defining adjacency.

## Limitations
Only exactly three noise-free pinned leaders, unit edge weights, identical node-noise normalization and integer \(n\ge4\) are covered. The statement does not classify more leaders, edge-weight perturbations, imperfect leaders or arbitrary biregular bipartite networks. A same-model mathematical and originality review is not independent verification; specialized uncatalogued literature may contain an equivalent implication. The strict positive gaps can be numerically small for large \(n\), although they are analytically exact.

## References
[1] K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first publicly submitted 2014-07-07). https://arxiv.org/abs/1407.1569 ; https://arxiv.org/pdf/1407.1569 .

[2] S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first publicly submitted 2014-12-20). https://arxiv.org/abs/1412.6595 ; https://arxiv.org/pdf/1412.6595 .

[3] *Crown graph*, standard graph-family description and the identity \(\operatorname{Cr}_n=K_{n,n}-M_n\). https://en.wikipedia.org/wiki/Crown_graph .
