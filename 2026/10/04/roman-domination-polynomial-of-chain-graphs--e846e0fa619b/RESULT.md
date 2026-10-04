# Roman domination polynomial of chain graphs
## Finding
Let \(G=(A,B,E)\) be a connected chain graph. Use its canonical nonempty twin classes
\[
A_1,\ldots,A_p,\qquad B_1,\ldots,B_p,
\]
ordered so that every \(a\in A_i\) has
\[
N(a)=B_1\cup\cdots\cup B_i,
\]
and hence every \(b\in B_j\) has \(N(b)=A_j\cup\cdots\cup A_p\). Put \(\alpha_i=|A_i|\), \(\beta_j=|B_j|\), and \(N=|V(G)|\).

A Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that each vertex labelled \(0\) has a neighbor labelled \(2\). Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\), and the Roman domination polynomial is
\[
R_G(x)=\sum_f x^{w(f)},
\]
where the sum runs over all Roman dominating functions.

For \(n\ge1\) and \(z,t\in\{0,1\}\), define
\[
F_n^{0,0}(x)=x^n,\quad
F_n^{1,0}(x)=(1+x)^n,\quad
F_n^{0,1}(x)=(x+x^2)^n,\quad
F_n^{1,1}(x)=(1+x+x^2)^n.
\]
The first superscript records whether label \(0\) is allowed in a class and the second whether label \(2\) is allowed.

Then
\[
R_G(x)=x^N+\sum_{s=1}^p U_s(x)+\sum_{r=1}^p V_r(x)+\sum_{r=1}^p\sum_{s=1}^p W_{r,s}(x),
\]
where
\[
U_s=(F_{\alpha_s}^{0,1}-F_{\alpha_s}^{0,0})
\prod_{i<s}F_{\alpha_i}^{0,1}
\prod_{i>s}F_{\alpha_i}^{0,0}
\prod_{j\le s}F_{\beta_j}^{1,0}
\prod_{j>s}F_{\beta_j}^{0,0},
\]
\[
V_r=(F_{\beta_r}^{0,1}-F_{\beta_r}^{0,0})
\prod_{j<r}F_{\beta_j}^{0,0}
\prod_{j>r}F_{\beta_j}^{0,1}
\prod_{i<r}F_{\alpha_i}^{0,0}
\prod_{i\ge r}F_{\alpha_i}^{1,0},
\]
and, writing \(\mathbf 1[P]\) for the indicator of a proposition \(P\),
\[
\begin{aligned}
W_{r,s}={}&
\bigl(F_{\alpha_s}^{\mathbf 1[s\ge r],1}-F_{\alpha_s}^{\mathbf 1[s\ge r],0}\bigr)
\bigl(F_{\beta_r}^{\mathbf 1[r\le s],1}-F_{\beta_r}^{\mathbf 1[r\le s],0}\bigr)\\
&\times\prod_{i\ne s}F_{\alpha_i}^{\mathbf 1[i\ge r],\mathbf 1[i\le s]}
\prod_{j\ne r}F_{\beta_j}^{\mathbf 1[j\le s],\mathbf 1[j\ge r]}.
\end{aligned}
\]
Thus every coefficient of the Roman domination polynomial is available from a finite \(O(p^2)\)-term product expression in the canonical twin-class sizes.

A direct corollary is
\[
\gamma_R(G)=\min\{4,|A|+1,|B|+1\}.
\]
The minimum-value corollary is not the originality-bearing part of the finding; the contribution is the complete all-weight classification and factorization.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. Every canonical class is nonempty. The statement covers every connected chain graph, including stars and complete bipartite graphs. The complete-bipartite specialization \(p=1\) is already present in the literature and is used as a boundary consistency check, not claimed as new.

The polynomial counts all Roman dominating functions, not only minimum-weight or inclusion-minimal ones. The variable \(x\) records total Roman weight.

## Proof
Partition Roman dominating functions according to whether label \(2\) occurs on neither bipartition side, only on \(A\), only on \(B\), or on both.

If no vertex is labelled \(2\), no vertex may be labelled \(0\); hence the unique function is the all-one function, contributing \(x^N\).

Suppose label \(2\) occurs only on \(A\), and let \(s\) be the largest index whose class \(A_s\) contains a label \(2\). No \(A\)-vertex can be labelled \(0\), because there is no label \(2\) on \(B\). In \(A_i\), label \(2\) is allowed exactly for \(i\le s\), and \(A_s\) must contain at least one \(2\). A vertex of \(B_j\) has a neighbor labelled \(2\) exactly when \(j\le s\), so label \(0\) is allowed exactly in those \(B_j\). These independent class choices give \(U_s\). The case with label \(2\) only on \(B\) is symmetric and gives \(V_r\), where \(r\) is the smallest \(B\)-index containing a \(2\).

Now suppose both sides contain label \(2\). Let \(r\) be the smallest index with a \(2\) in \(B_r\), and let \(s\) be the largest index with a \(2\) in \(A_s\). For \(a\in A_i\), a defending label \(2\) exists in \(N(a)=B_1\cup\cdots\cup B_i\) exactly when \(i\ge r\); therefore label \(0\) is allowed in \(A_i\) exactly for \(i\ge r\). Similarly, label \(0\) is allowed in \(B_j\) exactly for \(j\le s\). By the definitions of \(r\) and \(s\), label \(2\) is allowed in \(A_i\) exactly for \(i\le s\), and in \(B_j\) exactly for \(j\ge r\); moreover \(A_s\) and \(B_r\) must each contain at least one label \(2\). The factor \(F_n^{z,t}\) counts all independent assignments permitted by those two binary permissions, while subtracting the corresponding \(t=0\) factor in each boundary class enforces at least one label \(2\). This is exactly \(W_{r,s}\).

The four top-level cases are disjoint, and within each nonempty-label-\(2\) case the extremal indices are unique, so no Roman dominating function is omitted or counted twice.

For the minimum-weight corollary, a function with labels \(2\) on both sides has weight at least \(4\), attained by labelling one vertex of \(A_p\) and one vertex of \(B_1\) by \(2\) and all others by \(0\). If labels \(2\) occur only on \(A\), every \(A\)-vertex is nonzero, so the weight is at least \(|A|+1\), attained by labelling one vertex of \(A_p\) by \(2\), all other \(A\)-vertices by \(1\), and all \(B\)-vertices by \(0\). The symmetric bound \(|B|+1\) is attained similarly. The no-\(2\) function has weight \(N\), which cannot improve the displayed minimum.

## Verification
The accompanying standard-library script `verify_roman_chain.py` independently constructs every canonical positive twin-class profile of total order at most \(9\). For each profile it enumerates all \(3^N\) assignments, tests the Roman domination condition directly from the adjacency relation, forms the brute-force weight polynomial, and compares every coefficient with the formula above.

Replay result:

`VERIFY_OK profiles=255 labelings=3023307 coefficient_checks=4351 max_order=9`

This finite computation is a check of the formula and its boundary cases; the proof above is the justification for arbitrary order.

## Relationship to prior work
Cockayne, Dreyer, Hedetniemi, and Hedetniemi introduced the standard Roman domination framework in 2004. The 2021 paper *On the Roman Domination Polynomial of Graphs* defines the all-weight polynomial used here and gives an explicit theorem for complete bipartite graphs. Since complete bipartite graphs are exactly the one-pair canonical chain graphs, that specialization is prior coverage and is not claimed as original.

A 2020 paper titled *Algorithmic aspects of Roman domination in graphs* studies the minimum-weight Roman domination problem and reports efficient treatment of chain graphs. Full text was not available from the accessible sources checked in this run, so incidental stronger content cannot be excluded; this is retained as a bibliographic risk. The present claim is deliberately about the full all-weight enumerator, not the minimum value.

The 2023 *Roman Census* paper was inspected in full. It studies enumeration and counting of **minimal** Roman dominating functions on graph classes including split, cobipartite, interval, chordal, and forest classes, and exact counting for paths. That object does not imply the polynomial here, which counts every Roman dominating function by total weight, and chain graphs are not among its stated target classes.

A 2021 preprint on Roman domination in convex bipartite graphs, a broader bipartite class containing chain graphs, was also inspected through its accessible full text. Its objective and dynamic program compute an optimal Roman dominating function and the minimum Roman domination number; it does not enumerate all Roman dominating functions by weight.

## Limitations
The formula is specialized to connected chain graphs and uses their canonical nested-neighborhood decomposition. It does not claim an analogous factorization for arbitrary bipartite graphs. The finite verification reaches order \(9\) only and is corroborative rather than an infinite proof.

The literature comparison cannot rule out every poorly indexed or inaccessible source. In particular, the inaccessible full text of the 2020 chain-graph optimization paper leaves a residual risk of an incidental all-function formula, although its accessible title and abstract frame the problem as minimum-weight optimization rather than all-weight enumeration.

## References
1. E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, and S. T. Hedetniemi, *Roman domination in graphs*, Discrete Mathematics 278 (2004), 11–22. DOI: 10.1016/j.disc.2003.06.004.
2. D. Gangabylaiah, M. H. Indiramma, N. D. Soner, and A. Alwardi, *On the Roman Domination Polynomial of Graphs*, Bulletin of the International Mathematical Virtual Institute 11(2) (2021), 355–365. DOI: 10.7251/BIMVI2102355G.
3. C. Padamutham and V. S. R. Palagiri, *Algorithmic aspects of Roman domination in graphs*, Journal of Applied Mathematics and Computing 64 (2020), 89–102. DOI: 10.1007/s12190-020-01345-4.
4. F. N. Abu-Khzam, H. Fernau, and K. Mann, *Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes*, MFCS 2023, LIPIcs 272, Article 6. DOI: 10.4230/LIPIcs.MFCS.2023.6; full version arXiv:2208.05261.
5. S. Rout and G. K. Das, *Roman Domination in Convex Bipartite Graphs*, arXiv:2111.09040 (2021).
