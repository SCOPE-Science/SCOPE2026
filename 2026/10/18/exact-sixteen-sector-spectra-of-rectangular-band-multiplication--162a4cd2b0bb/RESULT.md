# Exact sixteen-sector spectra of rectangular-band multiplication-table graphs

## Finding

For arbitrary integers \(a,b\ge1\), let \(S_{a,b}=I_a\times J_b\) be the rectangular band with \((i,j)(k,l)=(i,l)\). Its generalized Latin square graph \(\Gamma(S_{a,b})\), with vertices \((x,y,xy)\) and edges when **exactly one** of the three entries agrees, has a complete, integral adjacency spectrum given below. This exact census refines the previously established regularity statement for rectangular bands.

Define \(m_r(r)=1\) and \(m_r(0)=r-1\). For \(u,w\in\{0,a\}\) and \(v,t\in\{0,b\}\), set
\[
\lambda(u,v,w,t)=1+uv+vw+wt-2v-2w.
\]
The characteristic polynomial, including all multiplicities and coincidences, is
\[
\boxed{\chi_{a,b}(z)=\prod_{u,w\in\{0,a\}}\prod_{v,t\in\{0,b\}}
\bigl(z-\lambda(u,v,w,t)\bigr)^{m_a(u)m_b(v)m_a(w)m_b(t)}.}
\]
Zero exponents are omitted; in particular the formula is valid when \(a=1\) or \(b=1\). The graph has \((ab)^2\) vertices and is regular of degree \(d=3ab-2a-2b+1\).

For \(a,b\ge2\), the graph is connected. If \(a=1\) or \(b=1\), it is the disjoint union of \(ab\) copies of \(K_{ab}\). The full spectrum determines the unordered semigroup-factor sizes \(\{a,b\}\): writing \(n=\sqrt{|V|}=ab\), one has \(a+b=(3n+1-d)/2\). Hence two rectangular bands give isomorphic such graphs exactly when their ordered factor sizes agree up to exchange; exchanging factors corresponds to taking opposite semigroups.

At \(a=b=2\), the graph has spectrum \(5\) with multiplicity \(1\), \(1\) with multiplicity \(10\), and \(-3\) with multiplicity \(5\), and is the \(16\)-vertex, degree-\(5\) Clebsch graph (equivalently the antipodal folded \(5\)-cube), with strongly regular parameters \((16,5,0,2)\).

As exact consequences, its adjacency energy is the sum of \(|\lambda|\) with the displayed multiplicities. For \(a,b\ge2\), its spanning-tree number is
\[
\tau(\Gamma(S_{a,b}))=\frac1{(ab)^2}
\prod_{(u,v,w,t)\ne(a,b,a,b)}
\bigl(d-\lambda(u,v,w,t)\bigr)^{m_a(u)m_b(v)m_a(w)m_b(t)},
\]
where the product runs over the sixteen sectors with the all-constant sector removed.

## Assumptions and scope

All sets \(I_a,J_b\) are finite and nonempty; \(a,b\) are positive integers with no primality or field assumptions. The graph is simple, undirected, and excludes pairs of vertices sharing two or three of \(x,y,xy\). The characteristic polynomial is over \(\mathbb Z\), with eigenvalues interpreted over \(\mathbb C\). Factor exchange is an anti-isomorphism in general, not an assertion that every rectangular band is isomorphic to its opposite.

## Proof

Represent a vertex by \((i,j,k,l)\in I_a\times J_b\times I_a\times J_b\), encoding \(x=(i,j)\), \(y=(k,l)\), and \(xy=(i,l)\). Let \(J_r\) denote the all-ones \(r\times r\) matrix and \(I_r\) the identity.

The matrices indicating equality of the first, second and product coordinates are respectively
\[
X=I_a\otimes I_b\otimes J_a\otimes J_b,\quad
Y=J_a\otimes J_b\otimes I_a\otimes I_b,\quad
Z=I_a\otimes J_b\otimes J_a\otimes I_b.
\]
Equality in the first and product coordinates has indicator \(XZ=I_a\otimes I_b\otimes J_a\otimes I_b\); equality in the second and product coordinates has indicator \(YZ=I_a\otimes J_b\otimes I_a\otimes I_b\). Equality in the first and second coordinates already forces equality of all four indices, so \(XY=XYZ=I\).

For three Boolean indicators, the indicator of exactly one being true equals their sum minus twice their pairwise products plus three times their triple product. Substituting \(XY=XYZ=I\) yields the **exact adjacency matrix**
\[
A=X+Y+Z-2XZ-2YZ+I.
\]
This identity also makes the diagonal zero: \(3-2-2+1=0\). Tensor-coordinate constants and sum-zero spaces simultaneously diagonalize all five commuting Kronecker factors. The all-ones matrix \(J_r\) acts as \(r\) on constants and as \(0\) on the sum-zero space, of dimension \(r-1\). On sector \((u,v,w,t)\), the operators \(Y,Z,X,XZ,YZ\) act as \(uv,vw,wt,w,v\), respectively. Thus \(A\) acts by \(1+uv+vw+wt-2w-2v\), with the sector multiplicity in the finding. Since these tensor eigenspaces exhaust a basis, this proves the entire characteristic polynomial for every \(a,b\ge1\) and proves integrality.

The all-constant sector has eigenvalue \(d=3ab-2a-2b+1\), establishing regularity. Suppose \(a,b\ge2\). Holding the first \((i,j)\) fixed, first-coordinate-only edges join \((k,l)\) to \((k',l')\) whenever \(l\ne l'\); the induced graph is complete \(b\)-partite and is connected. Holding the second \((k,l)\) fixed, second-coordinate-only edges join \((i,j)\) to \((i',j')\) whenever \(i\ne i'\); that induced graph is complete \(a\)-partite and connected. These two moves connect any pair of four-coordinate vertices. If \(a=1\), an edge exists exactly when \(j=j'\), \(l\ne l'\), giving \(b=ab\) copies of \(K_b\); the \(b=1\) case follows symmetrically.

The vertex number and degree recover the elementary symmetric functions of \(a,b\), so the unordered pair is the root multiset of \(z^2-(a+b)z+ab\). Conversely, switching the left and right semigroup factors while reversing multiplication maps vertices \((i,j,k,l)\) to \((l,k,j,i)\) and exchanges first/second coordinate agreement while preserving product agreement, proving graph isomorphism.

For \(a=b=2\), label the index sets by \(\mathbb F_2\). Directly from exactly-one agreement, the adjacency graph is Cayley on \(\mathbb F_2^4\) with five steps
\[
(0,0,0,1),\ (0,0,1,1),\ (1,0,0,0),\ (1,1,0,0),\ (0,1,1,0).
\]
Their sum is zero and any four form a basis, so this is precisely the folded \(5\)-cube obtained from the \(5\)-cube by quotienting antipodes. Two distinct vertices are adjacent iff they differ by one generating step; distinct generators sum to ten distinct nonzero two-step displacements, giving zero common neighbors for adjacent vertices and two for nonadjacent vertices. This proves the Clebsch identification. Finally, the energy identity is the definition of graph energy, and the spanning-tree product follows from the matrix-tree theorem using the unique degree eigenvalue for connected graphs.

## Verification

The included standalone \(\texttt{verify.py}\) runs using only Python's standard library. It builds adjacency directly from equality of the three multiplication-table entries, not from the predicted tensor matrix. For all \(16\) pairs \(1\le a,b\le4\), it constructs a full explicit integral tensor eigenbasis and checks the eigenvector equations entry by entry. It also checks degree, both trace moment identities, connected components, factor reconstruction, and the Clebsch common-neighbor parameters. The completed run returned \(\texttt{VERIFY_OK 16 rectangular bands}\). These finite checks corroborate, but do not replace, the uniform proof.

## Relationship to prior work

Sorouhesh, Golriz, and Panbehkar introduce the exactly-one-coordinate graph and prove rectangular-band regularity in arXiv:2511.23190v1, Proposition 5.3. Their revised arXiv:2511.23190v2, Proposition 5.3 and Lemma 5.4, discuss degree uniformity and a qualitative block decomposition; Section 6 computes an exact spectrum for **null semigroups**, a different multiplication law. Neither version provides the sixteen-sector eigenvalue/multiplicity formula for rectangular bands, the connectedness dichotomy, or the folded-cube identification. The exact spectrum here is not claimed for arbitrary bands or arbitrary semigroups. The degree and recoverability from degree alone are elementary consequences of the earlier degree-counting framework and are included as context, not claimed as the primary novel contribution.

## Limitations

The theorem concerns rectangular bands only; no classification of graphs from all bands or arbitrary finite semigroups is asserted. Graph isomorphism detects the band only up to exchange of left and right factor sizes (opposite semigroup). The proof is self-contained; the verification exhausts only the stated finite test range. Literature indexing can be incomplete, and an equivalent spectral formula in unindexed material remains possible. No independent mathematical audit has been performed.

## References

1. M. R. Sorouhesh, M. Golriz, and B. Panbehkar, *Generalized Latin Square Graphs of Semigroups: A Counting Framework for Regularity*, arXiv:2511.23190v1, first posted 2025-11-28, https://arxiv.org/html/2511.23190v1 (Definition 3.1 and Proposition 5.3).
2. M. R. Sorouhesh, M. Golriz, and B. Panbehkar, *Generalized Latin Square Graphs of Semigroups: A Counting Framework for Regularity and Spectra*, arXiv:2511.23190v2, 2025-12-30, https://arxiv.org/html/2511.23190v2 (Proposition 5.3, Lemma 5.4, Section 6, Appendices A–B).
3. Classical matrix-tree theorem and basic spectral decomposition of the all-ones matrix (standard linear algebra); no novelty is claimed for these ingredients.
