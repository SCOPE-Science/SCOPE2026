# Minimum total-domination pencils in finite subspace-intersection graphs

## Finding

Let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_q\), with \(n\ge3\), and let \(G(V)\) be the graph whose vertices are the proper nonzero subspaces of \(V\), with two distinct vertices adjacent exactly when their intersection is nonzero. Then \(\gamma_t(G(V))=q+1\). Moreover, the minimum total dominating sets are exactly the pencils of all \(q+1\) hyperplanes containing one fixed codimension-two subspace; hence their number is the Gaussian coefficient \(\begin{bmatrix}n\\2\end{bmatrix}_q=\frac{(q^n-1)(q^{n-1}-1)}{(q^2-1)(q-1)}\). The paired-domination number is \(\gamma_{\mathrm{pr}}(G(V))=q+1\) when \(q\) is odd and \(q+2\) when \(q\) is even. For odd \(q\), the minimum paired dominating sets are exactly the same hyperplane pencils.

The ordinary domination number \(q+1\) was known. The strengthened statement identifies every minimum total dominating set, counts them exactly, and determines paired domination.

## Assumptions and scope

Let \(V\) be an \(n\)-dimensional vector space over the finite field \(\mathbb F_q\), with \(n\ge3\). The graph \(G(V)\) has as vertices all proper nonzero subspaces of \(V\). Distinct vertices \(U,W\) are adjacent exactly when
\[
U\cap W\ne0.
\]

A total dominating set \(D\) requires every vertex, including each member of \(D\), to have a neighbor in \(D\). A paired dominating set is a dominating set whose induced graph has a perfect matching.

## Proof

First observe that every total dominating set is an ordinary dominating set. Jafari Rad and Jafari proved
\[
\gamma(G(V))=q+1.
\]
Hence
\[
\gamma_t(G(V))\ge q+1.
\tag{1}
\]

Choose a codimension-two subspace \(K\le V\). The hyperplanes containing \(K\) are in bijection with the one-dimensional subspaces of \(V/K\), so there are exactly
\[
q+1
\]
of them. Call this pencil \(\mathcal H(K)\).

Every nonzero vector \(v\in V\) belongs to one member of \(\mathcal H(K)\), because its image in the two-dimensional quotient \(V/K\) lies on a projective point. Thus the union of the pencil is \(V\). Also every two members of the pencil contain \(K\), which is nonzero because \(n\ge3\). Therefore \(\mathcal H(K)\) is a clique and totally dominates \(G(V)\). Together with (1),
\[
\gamma_t(G(V))=q+1.
\]

It remains to classify equality.

Let
\[
D=\{U_1,\ldots,U_{q+1}\}
\]
be a minimum total dominating set. Every one-dimensional subspace must meet one \(U_i\) nontrivially, hence must be contained in one \(U_i\). Therefore
\[
V=U_1\cup\cdots\cup U_{q+1}.
\tag{2}
\]

We use the following equality case for a \(q+1\)-subspace cover, proved here directly.

Extend each \(U_i\) to a hyperplane \(H_i\). No \(q\) proper subspaces can cover \(V\), because
\[
\left|\bigcup_{i=1}^{q}W_i\right|
\le
1+q(q^{n-1}-1)
=
q^n-q+1
<
q^n.
\]
Thus the \(H_i\) are \(q+1\) distinct hyperplanes.

Fix \(H_1\). The set \(V\setminus H_1\) has
\[
q^{n-1}(q-1)
\]
elements. For every \(i\ge2\),
\[
|H_i\setminus H_1|
=
q^{n-2}(q-1).
\]
There are exactly \(q\) such sets and they cover \(V\setminus H_1\), so equality of cardinalities forces them to be pairwise disjoint. Hence, for distinct \(i,j\ge2\),
\[
H_i\cap H_j\subseteq H_1.
\]
Both \(H_i\cap H_j\) and \(H_i\cap H_1\) have dimension \(n-2\), so
\[
H_i\cap H_j=H_i\cap H_1=H_j\cap H_1.
\]
Therefore all \(H_i\) contain one common codimension-two subspace \(K\).

Because the outside pieces \(H_i\setminus H_1\) are disjoint, (2) forces
\[
U_i\supseteq H_i\setminus H_1
\qquad(i\ge2).
\]
The set \(H_i\setminus H_1\) spans \(H_i\), so \(U_i=H_i\). The points of \(H_1\setminus K\) occur in no \(H_i\) with \(i\ge2\), so (2) likewise forces \(U_1=H_1\). Thus \(D=\mathcal H(K)\).

Conversely every pencil \(\mathcal H(K)\) is minimum total dominating by the first part. Distinct codimension-two subspaces give distinct pencils, since the intersection of all hyperplanes in the pencil is \(K\). Hence the number of minimum total dominating sets is
\[
\begin{bmatrix}n\\2\end{bmatrix}_q
=
\frac{(q^n-1)(q^{n-1}-1)}{(q^2-1)(q-1)}.
\]

For paired domination, every paired dominating set is total dominating, so its size is at least \(q+1\) and must be even.

If \(q\) is odd, then \(q+1\) is even, and every minimum total pencil is a clique of even order. Hence it has a perfect matching and
\[
\gamma_{\mathrm{pr}}(G(V))=q+1.
\]
The equality classification above shows that the minimum paired sets are exactly the same pencils.

If \(q\) is even, \(q+1\) is odd, so
\[
\gamma_{\mathrm{pr}}(G(V))\ge q+2.
\]
Take a pencil \(\mathcal H(K)\) and a one-dimensional subspace \(L\le K\). Add \(L\) to the pencil. Match \(L\) with one hyperplane and pair the remaining \(q\) hyperplanes inside the clique. This gives a paired dominating set of size \(q+2\), proving
\[
\gamma_{\mathrm{pr}}(G(V))=q+2.
\]

## Verification

The accompanying `verify.py` constructs every proper nonzero subspace directly for the cases
\[
(\mathbb F_2)^3,\qquad
(\mathbb F_3)^3,\qquad
(\mathbb F_2)^4.
\]
It exhaustively enumerates all minimum total dominating sets and checks that every one consists of hyperplanes with a common codimension-two intersection. The resulting counts are \(7\), \(13\), and \(35\), matching the Gaussian coefficient.

For \((\mathbb F_2)^3\) and \((\mathbb F_3)^3\), it also exhaustively determines paired domination.

Exact replay output:

```text
F_2^3: |V(G)|=14, gamma_t=3, min_total_sets=7
F_3^3: |V(G)|=26, gamma_t=4, min_total_sets=13
F_2^4: |V(G)|=65, gamma_t=3, min_total_sets=35
F_2^3: gamma_pr=4, min_paired_sets=77
F_3^3: gamma_pr=4, min_paired_sets=13
VERIFY_OK
```

These finite checks are corroborative only. The theorem for arbitrary prime powers follows from the symbolic cover argument above.

## Relationship to prior work

Jafari Rad and Jafari introduced this exact graph in the finite-vector-space setting and proved the ordinary domination formula
\[
\gamma(G(V))=q+1.
\]
Their public preprint dates from 4 May 2011. The full text inspected states ordinary domination, clique, chromatic, and independence results, but not total or paired domination.

A later full treatment of the same graph by Jafari Rad, Jafari, and Krzywkowski lists primary AMS classification \(15A03\). It studies degrees and characterizes connected, bipartite, complete, Eulerian, and planar cases. Full-text searches found no occurrence of “total domination,” “paired,” or even “domination.”

Targeted searches under the phrases “intersection graph of subspaces,” “subspace intersection graph,” “total domination,” “paired domination,” “hyperplane pencil,” and equivalent finite-vector-space covering language did not locate the minimum-set classification or paired formula.

## Limitations

The theorem requires \(n\ge3\). For \(n=2\), the vertices are the one-dimensional subspaces and the graph is edgeless, so total and paired domination do not exist.

The classification concerns minimum total dominating sets. For even \(q\), the theorem determines the paired-domination number but does not classify all paired dominating sets of size \(q+2\).

A residual originality risk is that the equality case for covering a finite vector space by \(q+1\) proper subspaces may occur in finite-geometry literature under different terminology, even though the direct searches performed here did not surface a source implying the graph-theoretic classification.

## References

1. N. Jafari Rad and S. H. Jafari, “Results on the intersection graphs of subspaces of a vector space,” arXiv:1105.0803, first posted 4 May 2011.
2. N. Jafari Rad, S. H. Jafari, and M. Krzywkowski, “On the intersection graphs of subspaces of a vector space,” public full text at `https://krzywkowski.pl/sub16.pdf`; AMS Subject Classification \(15A03,05C75,05C62,05C69\).
3. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
