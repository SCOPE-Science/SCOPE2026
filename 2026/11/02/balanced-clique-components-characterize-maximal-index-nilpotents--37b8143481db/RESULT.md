# Balanced clique components characterize maximal-index nilpotents in partial graph automorphism monoids

## Finding

Let \(G=K_{s_1}\sqcup\cdots\sqcup K_{s_r}\), where \(r\ge 1\), the integers \(s_i\ge1\), and \(n=\sum_{i=1}^{r}s_i\ge2\). Let \(\operatorname{PAut}(G)\) be the inverse monoid of isomorphisms between induced subgraphs of \(G\), including the empty map \(0\). A nilpotent element has *index* \(k\) when \(\alpha^k=0\) but \(\alpha^{k-1}\ne0\). Define \(M(G)\) as the number of nilpotents of index exactly \(n\).

**Theorem.** A nilpotent of index \(n\) exists if and only if \(\max_i s_i-\min_i s_i\le1\). Put \(n=hr+t\), where \(h\ge1\) and \(0\le t<r\). Then its exact multiplicity is
\[
M(G)=
\begin{cases}
0,&\max_i s_i-\min_i s_i>1,\\
\displaystyle r!\prod_{i=1}^{r}s_i!,&t=0,\\
\displaystyle t!(r-t)!\prod_{i=1}^{r}s_i!,&1\le t<r.
\end{cases}
\]
All such elements are precisely the partial shifts along ordered Hamiltonian paths \(v_0,v_1,\ldots,v_{n-1}\) in which the clique identifiers repeat with period \(r\), each occurring once among the first \(r\) positions. In the unequal-size case, the first \(t\) residue positions are occupied by the cliques of size \(h+1\).

More generally, for any simple graph \(H\) on \(n\) vertices, index-\(n\) nilpotents in \(\operatorname{PAut}(H)\) are in bijection with vertex orderings making the adjacency matrix symmetric Toeplitz. The formula above evaluates this natural count for cluster graphs, and, since complementation preserves partial automorphisms, also for the complementary complete multipartite graphs.

## Assumptions and scope

Graphs are finite, loopless, undirected and simple; all clique components are nonempty and distinguished by their vertex sets, even when component orders coincide. A partial graph automorphism preserves both adjacency and nonadjacency on its domain, rather than merely being a graph homomorphism. Products are composition of partial maps. For a nilpotent partial bijection on an \(n\)-point set, index \(n\) is the largest possible, because its functional digraph consists of disjoint directed paths and no directed cycles. The theorem counts distinct partial transformations on the *fixed labeled vertex set*, not isomorphism classes or conjugacy orbits.

## Proof

**1. Nilpotent paths.** A nilpotent partial bijection cannot contain a directed cycle, and injectivity ensures that each of its connected functional-digraph components is a directed path (including isolated vertices). Its index is the largest number of vertices on one path. Thus index \(n\) is possible exactly when all \(n\) vertices form one directed path, giving a unique ordering \(v_0,\ldots,v_{n-1}\) and the rank-\(n-1\) partial bijection
\[
\alpha(v_j)=v_{j+1}\quad(0\le j<n-1),\qquad
\operatorname{dom}(\alpha)=\{v_0,\ldots,v_{n-2}\}.
\]
Different orderings give different partial bijections: the unique source vertex outside the image is \(v_0\) and successive iterates recover the whole ordering. In particular \(\alpha^{n-1}\ne0\), while \(\alpha^n=0\).

**2. Exact graph condition.** The path shift is a partial graph automorphism if and only if, for all \(0\le i<j\le n-2\),
\[
\{v_i,v_j\}\in E(H)\quad\Longleftrightarrow\quad
\{v_{i+1},v_{j+1}\}\in E(H).
\]
Equivalently every off-diagonal of the adjacency matrix in this vertex order is constant; symmetry and the zero main diagonal give a symmetric Toeplitz adjacency matrix. This proves the general graph statement without assuming that any partial automorphism extends to a full graph automorphism.

**3. Rigidity of the clique word.** For the cluster graph, let \(c_j\) be the identifier of the component containing \(v_j\). Adjacency of two distinct vertices means equality of identifiers, so the condition in step 2 reads
\[
 c_i=c_j\quad\Longleftrightarrow\quad c_{i+1}=c_{j+1}
 \qquad(0\le i<j\le n-2).
\]
If no identifier repeats, there are \(n\) singleton components and the word already has the stated period \(r=n\). Otherwise, let \(d\) be the smallest positive distance between equal identifiers. Some equality at distance \(d\), together with shift invariance of the diagonal of that distance, forces
\[
 c_j=c_{j+d}\qquad(0\le j<n-d).
\]
The first \(d\) identifiers must be distinct; otherwise an equality at distance smaller than \(d\) contradicts minimality. Hence all identifiers are exactly those \(d\) residues, no two different residues share a component, and \(r=d\). Conversely, any period-\(r\) word with distinct first \(r\) identifiers satisfies step 2: equality occurs exactly when the index difference is divisible by \(r\).

**4. Existence and counting.** In a period-\(r\) word of length \(n=hr+t\), positions of residues \(0,1,\ldots,t-1\) occur \(h+1\) times and the other residues occur \(h\) times. The component sizes therefore have to be \(h\) or \(h+1\). Conversely, if the component sizes satisfy this condition, assign the \(t\) larger components to the first \(t\) residues and the \(r-t\) smaller components to the remaining residues, then repeat periodically. This yields a valid partial automorphism. If \(t=0\), there are \(r!\) bijections from the \(r\) distinct components to the residue positions; if \(t>0\), there are \(t!(r-t)!\) such assignments. Independently ordering the \(s_i\) distinct vertices of each component in its designated residue positions contributes \(s_i!\). Multiplication gives the formula, with no overcount by step 1.

## Verification

The accompanying `verify.py` enumerates all orderings for every integer partition of \(n\) with \(2\le n\le7\), independently checks induced adjacency and nonadjacency for the source and image of the resulting partial shift, and compares the resulting number with the theorem. It additionally checks four eight-vertex instances with different component-balance patterns. All **47** exhaustive test configurations pass and produce `VERIFY_OK`. Examples include \(M(K_3\sqcup K_2)=12\), \(M(K_3\sqcup K_3)=72\), \(M(K_2\sqcup K_2\sqcup K_1)=8\), and \(M(K_4\sqcup K_2)=0\). These are finite consistency checks, not substitutes for the unrestricted proof.

To replay: run `python3 verify.py` using Python's standard library (no data files or third-party packages).

## Relationship to prior work

Elliott, Levine and Mitchell (arXiv:2303.12387, first posted 22 March 2023) enumerate isomorphism types of monogenic (inverse) submonoids of full and symmetric inverse transformation monoids; their general ambient counting does not give the number of individual maximal-index nilpotents in graph-restricted inverse monoids. Jajcay, Jajcayova, Szakács and Szendrei (arXiv:1809.04422) establish the inverse-monoid framework of partial graph automorphisms and its Green-type structure, rather than this index extremizer multiplicity. Dimitrova, Fernandes, Koppitz and Quinteiro (DOI 10.1007/s00233-021-10193-y) study the path-graph partial automorphism and injective partial endomorphism monoids.

The Toeplitz reduction is closely related to known graph theory: Mojallal, Jung, Cheon, Kim and Kang (arXiv:2112.14371), Proposition 2.3, show that Toeplitz graphs with all allowed distances divisible by one base gap split into residue-class components. This encompasses the component-size geometry after imposing the clique condition; that earlier graph decomposition is **not** asserted to be new. The new subject here is the correspondence with longest nilpotent chains in \(\operatorname{PAut}(G)\), the sharp if-and-only-if for cluster components, and the exact **labeled-element** multiplicities. Other relevant equivalent formulations include partial automorphisms of equivalence relations and their complementary complete multipartite graphs.

## Limitations

This is a complete classification of only the nilpotents of *maximal possible index*; it does not enumerate nilpotents of smaller indices or all elements of the inverse monoid. The Toeplitz statement concerns the existence of a *vertex ordering*, not an intrinsic condition for arbitrary graph families. Existing Toeplitz-graph component theory explains part of the structural mechanism, and potential differently phrased results in partition-preserving inverse-semigroup literature remain an originality risk. Publication priority is not asserted without a broader independent literature audit.

## References

1. L. Elliott, A. Levine and J. D. Mitchell, *Counting monogenic monoids and inverse monoids*, arXiv:2303.12387 (initial submission 2023-03-22).
2. R. Jajcay, T. Jajcayova, N. Szakács and M. B. Szendrei, *Inverse monoids of partial graph automorphisms*, arXiv:1809.04422 (2018).
3. S. A. Mojallal, J.-H. Jung, G.-S. Cheon, S.-R. Kim and B. Kang, *Structural properties of Toeplitz graphs*, arXiv:2112.14371 (2021), especially Proposition 2.3.
4. I. Dimitrova, V. H. Fernandes, J. Koppitz and T. M. Quinteiro, *Partial automorphisms and injective partial endomorphisms of a finite undirected path*, *Semigroup Forum* (2021), DOI 10.1007/s00233-021-10193-y.
