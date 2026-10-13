# Critical groups of partial matching deletions from balanced complete bipartite graphs

## Finding
Let \(n\ge3\) and \(1\le t\le n-1\) be integers. Let \(G_{n,t}\) be obtained from the balanced complete bipartite graph \(K_{n,n}\) by deleting an arbitrary matching of size \(t\). Set
\[
q=n-t,\qquad A=n(n-2),\qquad C=n(n-2)+t.
\]
The critical group \(K(G_{n,t})\) has the following **invariant-factor decomposition** (all unlisted factors are \(1\)):
\[
K(G_{n,1})\cong (\mathbb Z/n\mathbb Z)^{2n-5}\oplus
  \mathbb Z/[n(n-1)^2]\mathbb Z,
\]
whereas for \(2\le t\le n-1\),
\[
K(G_{n,t})\cong
(\mathbb Z/n\mathbb Z)^{2q-2}
\oplus(\mathbb Z/A\mathbb Z)^{t-2}
\oplus\mathbb Z/(AC)\mathbb Z.
\]
Consequently the spanning-tree count for every \(1\le t\le n-1\) is
\[
\tau(G_{n,t})=n^{2q-2}A^{t-1}C.
\]
The exponent \(2q-2\) is nonnegative. These decompositions are invariant-factor ordered because \(n\mid A\mid AC\) and \(n\mid n(n-1)^2\). As examples, deleting two independent edges from \(K_{4,4}\) gives \((\mathbb Z/4\mathbb Z)^2\oplus\mathbb Z/80\mathbb Z\); deleting three gives \(\mathbb Z/8\mathbb Z\oplus\mathbb Z/88\mathbb Z\).

## Assumptions and scope
Graphs are finite, undirected, unweighted and simple. Label the bipartition \(x_1,\ldots,x_n\) and \(y_1,\ldots,y_n\), delete edges \(x_i y_i\) for \(1\le i\le t\), and take the unmatched vertex \(y_n\) as the sink. It is essential that \(t\le n-1\), so this sink exists; \(n\ge3\) ensures connectivity. The critical group is \(\mathbb Z^{2n-1}/\operatorname{im}\widetilde L\), where \(\widetilde L\) is the reduced integer graph Laplacian. We determine the complete isomorphism type, not merely its order.

## Proof
Write \(X=\sum_{i=1}^n x_i\) and \(Y=\sum_{j=1}^{n-1}y_j\), now interpreting the vertex symbols as generators of the cokernel (the sink \(y_n=0\)). In the reduced-Laplacian presentation, the sink row relation \(X=0\) is already implied by the other vertex-row relations: all full Laplacian rows sum to zero. Adding this redundant relation permits a symmetric use of all vertex relations without modifying the presented group.

For each deleted pair \(i\le t\), the right-vertex row is \((n-1)y_i+x_i-X=0\), whence \(x_i=-(n-1)y_i\). Its left-vertex row \((n-1)x_i+y_i-Y=0\) becomes
\[
A y_i+Y=0,\qquad A=(n-1)^2-1=n(n-2).
\]
For the \(q=n-t\) unmatched left vertices, the rows state \(nx_j=Y\). For the \(q-1\) unmatched nonsink right vertices, the rows state \(ny_j=0\).

Choose \(x=x_n\), put \(u_j=x_j-x\) for \(t<j<n\), and put \(z_j=y_j\) for \(t<j<n\). Set \(U=\sum_{t<j<n}u_j\), \(V=\sum_{t<j<n}z_j\), and \(T=\sum_{i\le t}y_i\), interpreting empty sums as zero. The left rows and definition of \(Y\) give
\[
Y=nx=T+V,\qquad nu_j=nz_j=0.
\]
The sink relation \(X=0\), using the eliminated matched left generators, becomes \(qx+U-(n-1)T=0\); eliminating \(T\) yields
\[
Cx=U+(n-1)V,\qquad C=n(n-2)+t.
\]
Eliminate \(y_t\) by \(T=nx-V\). The remaining deleted-pair rows read \(Ay_i+nx=0\) for \(1\le i<t\). The eliminated last matched row is redundant: substituting the earlier rows into its left-hand side \(Ay_t+nx\) gives \(nCx-AV=n(U+V)=0\), as \(nu_j=nz_j=0\). Thus the full presentation is equivalent, by integer generator elimination and relation addition, to
\[
\begin{gathered}
  Ay_i+nx=0\quad(1\le i<t),\qquad Cx=U+(n-1)V,\\
  nu_j=0\quad(t<j<n),\qquad nz_j=0\quad(t<j<n).
\end{gathered}
\]

If \(q\ge2\), eliminate \(u_{t+1}\) through the relation for \(Cx\). Its former torsion relation becomes \(nCx=0\); the remaining \(2q-3\) independent \(u,z\) generators each have order \(n\). If \(t=1\), there are no \(y_i\) left, so the core is cyclic of order \(nC=n(n-1)^2\), and there are \(2q-3=2n-5\) copies of \(\mathbb Z/n\mathbb Z\).

If \(q\ge2\) and \(t\ge2\), take \(w=x+(n-2)y_1\), and \(v_i=y_i-y_1\) for \(2\le i<t\). These are a unimodular change of generators. The relations become \(nw=0\), \(Av_i=0\), and \(ACy_1=0\), because \(nCx=nCw-ACy_1\) and \(nw=0\). The core therefore splits as \(\mathbb Z/n\mathbb Z\oplus(\mathbb Z/A\mathbb Z)^{t-2}\oplus\mathbb Z/(AC)\mathbb Z\), alongside the \(2q-3\) independent order-\(n\) generators.

Finally \(q=1\) forces \(t=n-1\ge2\). There are no \(u,z\); the relations are \(Cx=0\) and \(Ay_i+nx=0\). Taking differences \(v_i=y_i-y_1\) splits off \(t-2\) order-\(A\) generators. The final two-generator presentation has relation matrix
\[
\begin{pmatrix}C&0\\n&A\end{pmatrix}.
\]
Its entries have greatest common divisor \(1\), since \(C\equiv-1\pmod n\), and its determinant is \(AC\). Its Smith form is therefore \(\operatorname{diag}(1,AC)\), yielding the claimed endpoint decomposition.

This exhausts all allowed \((n,t)\). Multiplying the cyclic orders gives the displayed spanning-tree formula by the matrix-tree theorem. This derivation uses no finite enumeration as an infinite-case argument.

## Verification
The accompanying `verify.py` constructs the reduced Laplacian directly from the edge set, calculates its exact integer Smith form by unimodular Euclidean row/column transformations, and compares all nontrivial factors with the formula for \(3\le n\le10\), \(1\le t<n\). It reports `VERIFY_OK full_smith_cases=44 orders=3..10 intermediate_matching_deletions`. The direct arbitrary-parameter proof above, rather than these finite checks, establishes the theorem. A separate SymPy Smith-form implementation also checked all \(65\) pairs through \(n=12\) before publication of this manuscript; it is not required to replay the standalone verification.

To reproduce the packaged check, run `python3 verify.py` with Python 3.9 or later. No third-party packages or external datasets are required.

## Relationship to prior work
Corrales–Valencia explicitly calculate the critical group for the balanced complete bipartite graph with a **perfect** matching removed (the \(t=n\) endpoint), in their Corollary 3.8 and applications; they do not state this strictly partial \(1\le t<n\) decomposition. Machacek's thesis, Theorem 14, likewise treats the complete perfect-matching deletion and its line graph, not intermediate deletion sizes. Jacobson–Niedermaier–Reiner determine critical groups of complete multipartite graphs, including the \(t=0\) endpoint. Dong–Jiang–Guo study a family of multipartite chains built from complete consecutive bipartite joins; their hypotheses do not include deleted-matching bicliques. Hence endpoint formulas and general Smith-form methods are acknowledged as preexisting; the present finding is the explicit intermediate invariant-factor classification. A search cannot rule out an older equivalent formula under different nomenclature.

## Limitations
The statement excludes \(t=0\) and \(t=n\), whose group structures have earlier treatments. It assumes equal bipartition sizes and deleted edges that are pairwise disjoint; arbitrary edge-deletion patterns and unequal sizes are not classified here. Coverage against poorly indexed or inaccessible independent formulas is not guaranteed. The check is finite and does not constitute independent mathematical review.

## References
1. H. Corrales and C. E. Valencia, *On the critical group of matrices*, arXiv:1008.5176v1 (first posted 2010-08-30), particularly §3 and Corollary 3.8. https://arxiv.org/pdf/1008.5176
2. J. Machacek, *The critical group of a line graph: The bipartite case* (manuscript dated 2011-12-14), §4.1 and Theorem 14. https://www-users.cse.umn.edu/~reiner/HonorsTheses/Machacek_thesis.pdf
3. B. Jacobson, A. Niedermaier and V. Reiner, *Critical groups for complete multipartite graphs and Cartesian products of complete graphs*, J. Graph Theory 44 (2003), 231–250. DOI: 10.1002/jgt.10139.
4. X. Dong, G. Jiang and W. Guo, *On the critical group of the k-partite graph*, arXiv:2409.02654v1 (2024), Definition 2.3. https://arxiv.org/html/2409.02654
