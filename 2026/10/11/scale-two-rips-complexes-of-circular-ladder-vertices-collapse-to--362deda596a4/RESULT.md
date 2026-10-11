# Scale-two Rips complexes of circular ladder vertices collapse to a rim

## Finding
For every integer \(n\ge 7\), equip the vertex set of the circular ladder \(G_n=C_n\square K_2\) with the shortest-path metric and form the **inclusive** Vietoris--Rips complex \(X_n=\operatorname{VR}_{\le2}(V(G_n))\). There is a sequence of exactly \(9n\) elementary simplicial collapses from \(X_n\) onto the copy of \(C_n\) consisting of its lower-rim vertices and ordinary lower-rim edges. In particular,
\[
X_n\searrow C_n\simeq S^1,
\qquad\widetilde H_j(X_n;\mathbb Z)=
\begin{cases}\mathbb Z,&j=1,\\0,&j\ne1.\end{cases}
\]
The collapse retains the actual lower-rim subcomplex, not just a space with the same Betti numbers.

## Assumptions and scope
Write \(a_i=(i,0)\) and \(b_i=(i,1)\), with indices taken modulo \(n\). Edges of \(G_n\) join consecutive indices on each rim and join \(a_i\) to \(b_i\). Graph distances are
\[
d((i,e),(j,f))=\min\{|i-j|,n-|i-j|\}+\mathbf1_{e\ne f}.
\]
A nonempty subset spans a simplex of \(X_n\) exactly when all pairwise distances are at most \(2\). The assertion concerns only these \(2n\) sampled vertices, not all points of the continuous metric graph, and only \(n\ge7\). It uses graph distance, not Euclidean chord distance or the supremum product metric.

## Proof
**Maximal-face classification.** For \(n\ge7\), the maximal simplices of \(X_n\) are exactly the \(3n\) tetrahedra
\[
A_i=\{a_i,a_{i+1},a_{i+2},b_{i+1}\},\quad
B_i=\{b_i,b_{i+1},b_{i+2},a_{i+1}\},\quad
D_i=\{a_i,b_i,a_{i+1},b_{i+1}\}.
\]
Indeed, a clique's indices on one rim lie in a three-consecutive-index arc: for \(n\ge7\), these are the maximal cliques of the square of the cycle. An opposite-rim vertex can coexist with all three only at their middle index, and a clique with two vertices in each rim occupies two adjacent columns. Any smaller clique extends to one of the displayed tetrahedra. In particular, no five-point clique exists. The face numbers in dimensions \(0,1,2,3\) are respectively \(2n,7n,8n,3n\).

**Nine collapse phases.** The following table specifies a free face \(\sigma\) and its unique codimension-one coface \(\tau\) for each phase. In phase \(p\), simultaneously for every \(i\in\mathbb Z/n\mathbb Z\), translate all displayed indices by \(i\), and then delete the two faces \(\sigma_i\) and \(\tau_i\). Different translated pairs in the same phase are disjoint. They may equivalently be removed in increasing index order.

| Phase | Free face \(\sigma\) | Unique coface \(\tau\) |
| --- | --- | --- |
| 1 | \(a_0a_1a_2\) | \(a_0a_1b_1a_2\) |
| 2 | \(a_0b_0a_1\) | \(a_0b_0a_1b_1\) |
| 3 | \(a_0b_0b_{-1}\) | \(a_0b_0b_1b_{-1}\) |
| 4 | \(a_0a_2\) | \(a_0b_1a_2\) |
| 5 | \(a_0b_{-1}\) | \(a_0b_1b_{-1}\) |
| 6 | \(b_0b_2\) | \(b_0b_1b_2\) |
| 7 | \(b_0b_1\) | \(a_0b_0b_1\) |
| 8 | \(a_0b_0\) | \(a_0b_0a_{-1}\) |
| 9 | \(b_0\) | \(b_0a_{-1}\) |

Juxtaposition denotes a simplex containing the listed vertices. To check freeness **for arbitrary \(n\ge7\)**, use the three displayed tetrahedron families: at the start of a phase, list all codimension-one cofaces of its chosen \(\sigma_i\), and cancel those removed by earlier phases. Exactly its displayed \(\tau_i\) remains. This comparison uses only relative column indices \(-1,0,1,2\), so no additional cofaces arise upon changing \(n\ge7\). Every translated pair is present at the beginning of its phase; none is reused. The first three phases remove all \(3n\) tetrahedra and \(3n\) triangles; phases 4--8 remove the remaining \(5n\) triangles and \(5n\) non-rim edges; phase 9 removes the \(n\) upper-rim vertices and their final \(n\) incident edges. The remaining vertices are precisely \(a_i\) and the remaining edges precisely \(a_ia_{i+1}\), with no triangles.

Each removal is an elementary simplicial collapse and hence a strong deformation retraction of realizations. Their concatenation proves the assertion. The standard lower cycle has the homotopy type of the circle, giving the integral homology statement.

## Verification
The self-contained Python 3 script `verify.py`, supplied with this result, independently enumerates every scale-two clique from the shortest-path metric for \(7\le n\le20\), checks the claimed three tetrahedron families and the complete face vectors, and tests that each of the \(9n\) specified pairs is an actual elementary free-face pair in the current complex. The script checks the final remaining faces equal the lower cycle and prints `VERIFY_OK`. The code is finite corroboration; the all-\(n\) argument is the facet classification and nine uniform phases above.

## Relationship to prior work
Saleh, Titz Mite and Witzel classify graph-metric Vietoris--Rips complexes on the vertex sets of the five Platonic solids, including the cube. They explicitly mention extension to other polyhedral vertex sets as a possible direction; they do not give the present circular-ladder family or its nine-phase collapse.

Adamaszek and coauthors study circular ladders as *continuous metric graphs*, and describe their Rips types in ranges of scales strictly below \(2\). Their Example 2 does not imply the **inclusive scale-two finite-vertex** collapse established here. Sterling's later torus-grid study treats square grids with two cyclic factors, not the cylindrical vertex graph with one \(K_2\) factor.

## Limitations
No result is asserted for \(n\le6\), other scale parameters, continuous points along the ladder edges, or Euclidean distances. The proof is nonequivariant: its collapse phases retain the rotational index pattern but the elementary moves need not be simultaneous equivariant strong deformation retractions. No claim of exhaustive coverage of unpublished work is made.

## References
1. N. Saleh, T. Titz Mite, S. Witzel, *Vietoris--Rips complexes of Platonic solids*, arXiv:2302.14388v1 (first public 2023-02-28), primary MSC 55N31. https://arxiv.org/abs/2302.14388
2. M. Adamaszek et al., *On Homotopy Types of Vietoris--Rips Complexes of Metric Gluings*, arXiv:1712.06224v5 (initial public 2017-12-18), Section 5 and Example 2. https://arxiv.org/abs/1712.06224
3. J. Sterling, *Vietoris--Rips Complexes of Torus Grids*, Auburn University thesis (2025), Sections 2--4. https://auetd.auburn.edu/bitstream/handle/10415/9659/Vietoris_Rips_Complexes_of_Torus_Grids__Master_s_Thesis.pdf
