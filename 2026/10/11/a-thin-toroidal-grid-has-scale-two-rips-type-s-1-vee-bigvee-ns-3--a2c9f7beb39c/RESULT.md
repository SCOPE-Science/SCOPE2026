# A thin toroidal grid has scale-two Rips type \(S^1\vee\bigvee^nS^3\)

## Finding
For every integer \(n\ge7\), let \(G_n=C_4\square C_n\) be the Cartesian product of two cycle graphs, with its graph shortest-path metric. For the **inclusive** Vietoris–Rips complex at threshold \(2\),
\[
X_n=\operatorname{VR}(V(G_n),d_{G_n};2)\simeq S^1\vee\bigvee^n S^3.
\]
More precisely, \(X_n\) admits \(16n\) explicit elementary simplicial collapses to a cyclic union of \(n\) triangulated three-spheres. Its face-count vector, indexed by nonempty face cardinality from one through five, is \((4n,22n,40n,27n,4n)\). In particular, its only nonzero positive-degree integral homology groups are \(H_1(X_n;\mathbb Z)\cong\mathbb Z\) and \(H_3(X_n;\mathbb Z)\cong\mathbb Z^n\).

## Assumptions and scope
Vertices are \((j,r)\), with \(j\in\mathbb Z/n\mathbb Z\) and \(r\in\mathbb Z/4\mathbb Z\). For columns and rows, let \(d_n\) and \(d_4\) denote their usual shortest cyclic distances. The product distance is
\[
d((i,r),(j,s))=d_n(i,j)+d_4(r,s).
\]
A nonempty vertex set is a face of \(X_n\) precisely when every pair has distance at most \(2\). A simplicial elementary collapse deletes a face and its unique codimension-one coface when the smaller face is contained in no other maximal simplex. The lower bound \(n\ge7\) ensures columns at cyclic distance two have a unique intervening column and prevents wrap-around coincidences in the face classification below.

## Proof
**1. Classify all faces outside consecutive-column slabs.** For each \(j\), let \(S_j\subseteq X_n\) be the induced subcomplex on the eight vertices of columns \(j\) and \(j+1\), and set \(U_n=\bigcup_{j\in\mathbb Z/n\mathbb Z}S_j\). Any face outside \(U_n\) has a pair of vertices from nonconsecutive columns. Their column distance must be exactly two, and their row distance must be zero. Consequently, the pair is of the form
\[
B_{j,r}=\{(j-1,r),(j+1,r)\}.
\]
Compatibility with both endpoints forces any further vertex to belong to column \(j\) and to have row \(r-1\), \(r\), or \(r+1\). Conversely every subset of these three middle-column vertices is compatible with \(B_{j,r}\) and internally compatible. In particular, each outside face is uniquely
\[
B_{j,r}\cup T,\qquad T\subseteq\{(j,r-1),(j,r),(j,r+1)\}.
\]
Uniqueness follows because no two different distance-two column pairs can occur in one face for \(n\ge7\): a face containing one such pair can use no further vertex in either endpoint column, and all its other vertices belong to the same intervening column. The eight faces corresponding to each \(B_{j,r}\) are disjoint from those corresponding to other endpoint pairs.

**2. An explicit elementary collapse.** Fix \(j,r\). Put \(v=(j,r)\), \(a=(j,r-1)\), and \(b=(j,r+1)\). Process the four subsets \(T\subseteq\{a,b\}\) in decreasing cardinality. At each step remove the elementary pair
\[
\bigl(B_{j,r}\cup T,\quad B_{j,r}\cup T\cup\{v\}\bigr).
\]
When the step with \(T\) is reached, all strict cofaces of the lower simplex other than the displayed upper simplex have been removed at earlier steps with larger subsets. Therefore the lower simplex is free. The pair is indeed a codimension-one incidence. Different endpoint pairs do not interact by the classification in step 1; the order of processing \(j,r\) is irrelevant. There are \(4n\) choices of \(B_{j,r}\) and four pairs per choice, hence \(16n\) elementary collapses delete precisely the \(32n\) non-slab faces. Thus \(X_n\searrow U_n\).

**3. Each slab is a triangulated three-sphere.** Within the eight vertices of \(S_j\), the only forbidden pairs are
\[
\{(j,r),(j+1,r+2)\},\qquad r\in\mathbb Z/4\mathbb Z.
\]
The four forbidden pairs form a perfect matching. The corresponding clique complex is the join of four two-point sets, or equivalently the boundary of the four-dimensional cross-polytope. Thus \(S_j\cong (S^0)^{*4}\cong S^3\). The four vertices of each single column form a full tetrahedron in each adjacent slab. For \(n\ge7\), the only nonempty pairwise overlaps are \(S_j\cap S_{j+1}\), the full tetrahedron on column \(j+1\); no three slabs share any vertex.

**4. Compute the homotopy type of the cyclic gluing.** Glue \(S_0,S_1,\ldots,S_{n-2}\) sequentially. Each new sphere meets the preceding union in one full tetrahedron, a nonempty contractible subcomplex. Because the inclusions are cofibrations, collapsing these contractible attaching subcomplexes shows that the resulting chain has the homotopy type of a wedge of \(n-1\) three-spheres. The last sphere \(S_{n-1}\) meets the chain in exactly two disjoint full tetrahedra, one in its column \(n-1\), the other in its column \(0\). Attaching the sphere along these two contractible, disjoint subcomplexes adds its \(S^3\) summand and an independent \(S^1\) corresponding to the cycle of slab intersections. One way to see the last assertion is to replace each contractible attaching tetrahedron by a point in the homotopy pushout; attaching a connected three-sphere at two distinct points of a connected space adds the sphere and a loop. Therefore \(U_n\simeq S^1\vee\bigvee^n S^3\), and step 2 gives the stated result for \(X_n\).

**5. Face counts.** Each of the \(n\) slabs has face counts \((8,24,32,16)\), and neighboring slabs overlap in a tetrahedron with face counts \((4,6,4,1)\); no triple-overlap correction is needed. Therefore \(U_n\) has vector \((4n,18n,28n,15n)\). The \(4n\) endpoint pairs contribute, respectively, \(4n,12n,12n,4n\) faces in cardinalities two through five. Adding them yields \((4n,22n,40n,27n,4n)\) as claimed.

## Verification
Run `python3 artifacts/verify.py` with Python 3 standard library. The script generates all cliques directly from the graph distance, independently constructs each slab, verifies all predicted face counts, tests every proposed elementary collapse against its entire current coface list, and checks the complete overlap pattern for each integer \(7\le n\le24\). It also calculates exact simplicial boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) for \(7\le n\le10\). Successful output ends with `VERIFY_OK 18 complete simplicial collapses; 12 exact homology checks`. These finite computations are cross-checks, not a substitute for the uniform proof in steps 1–5.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng, and Sterling [1] study square torus grids \(C_m\square C_m\). Their Theorem 5.8 gives a torus homotopy type in a different, small-scale symmetric regime, while Section 6 identifies the same elementary cross-polytope fact used here for **individual slabs**. Neither their square-grid formulas nor that local fact contains the present cyclic rectangular gluing or the all-\(n\) collapse. Gupta, Sarkar, and Shukla [2] study infinite integer lattices, a different metric space without the thin periodic factor and its essential loop. These references motivate and contextualize the result; no global rectangular statement is attributed to them.

## Limitations
No assertion is made for \(n\le6\), for any other scale, or for rectangular torus grids of other fixed widths. The topological conclusion relies essentially on the absence of additional wrap-around faces when \(n\ge7\). Existence of an equivalent result outside the sources examined is not excluded. This mathematical proof and its finite executable corroboration are not an independent external audit.

## References
[1] H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134, first posted 2025-02-10; especially Sections 5 and 6. https://arxiv.org/html/2502.07134v2

[2] R. K. Gupta, S. Sarkar, S. Shukla, *On the Vietoris-Rips Complexes of Integer Lattices*, arXiv:2511.04238, first posted 2025-11-06; especially the scale-two lattice results. https://arxiv.org/html/2511.04238v1
