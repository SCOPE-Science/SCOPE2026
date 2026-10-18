# The dodecahedral two-independence complex is \(S^6\) with sign rotation

## Finding
For the dodecahedral graph \(D=GP(10,2)\), the two-independence complex has integral homotopy type
\[
\operatorname{Ind}_2(D)\simeq S^6.
\]
The canonical tenfold rotation \(\rho\) of the generalized Petersen presentation acts as \(-1\) on \(\widetilde H_6(\operatorname{Ind}_2(D);\mathbb Z)\cong\mathbb Z\). Thus, for every integer \(0\le t<10\),
\[
\operatorname{tr}\left(\rho^t\mid \widetilde H_6(\operatorname{Ind}_2(D);\mathbb Q)\right)=(-1)^t.
\]
This is an ordinary integral homotopy equivalence and a homology-representation statement; it does **not** assert an equivariant homotopy equivalence with any specified action on a sphere.

## Assumptions and scope
Use the labeled generalized Petersen presentation with vertices \(u_i=i\), \(v_i=10+i\) for \(i\in\mathbb Z/10\) and undirected edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+2}\), with indices modulo ten. This is the 20-vertex, 30-edge, 3-regular dodecahedral graph. An allowed face \(F\subseteq V(D)\) induces connected components of cardinality at most two. Equivalently, every vertex of \(D[F]\) has induced degree at most one. Equivalently again, \(F\) contains no three-vertex set consisting of a vertex together with two of its neighbors. There are exactly 60 such forbidden triples in this graph.

All calculations use the indicated twenty-vertex labeling and ascending vertex order for orientations. A simplex of cardinality \(j+1\) has dimension \(j\). The complex has dimension eleven and has facets in dimensions seven, eight, nine, and eleven.

## Proof
**1. Complete face list.** Enumerate all subsets of twenty vertices and apply the induced-degree-at-most-one criterion. The numbers of nonempty faces in dimensions zero through eleven are, respectively,
\[
(20,190,1080,3985,9772,15870,16640,10770,4000,750,60,5).
\]
Their sum is \(63142\), and their alternating sum (ordinary Euler characteristic) is \(2\). The maximum size of a face is twelve. The independent forbidden-triple implementation confirms the list and gives facet counts \(25,60,420,5\) in dimensions \(7,8,9,11\), respectively.

**2. Acyclic matching.** Start with the nonempty face poset. In ascending order \(v=0,1,\ldots,19\), pair every currently unmatched face \(F\) not containing \(v\) with \(F\cup\{v\}\) whenever both are currently unmatched faces. This produces \(31565\) disjoint cover pairs. By the staged element-matching theorem, their union is acyclic. Independently, direct all unmatched Hasse covers from larger to smaller face and each matched cover from smaller to larger. A complete topological sort visits all \(63142\) faces across \(410500\) Hasse covers, establishing acyclicity without reliance on the theorem's implementation details. The critical faces are precisely one vertex, one 5-simplex, six 6-simplices, and four 7-simplices. Their bitmask identifiers, in ascending order by dimension and then value, are
\[
\begin{aligned}
\dim 0:&\ (1),\\
\dim 5:&\ (132266),\\
\dim 6:&\ (68436,78418,150674,197452,197930,246282),\\
\dim 7:&\ (102036,151188,246540,406098).
\end{aligned}
\]

**3. Exact integer Morse boundaries.** The signed coefficient of \(F\) in the simplicial boundary of \(F\cup\{v\}\) is \((-1)^j\), where \(j\) is the zero-based position of the removed vertex in ascending order. For a lower face paired upward, recursively substitute the boundary of its paired upper face, divided by its unit incidence \(\pm1\). Critical lower faces give coordinate vectors and faces paired downward give zero. The acyclic matching makes this integer gradient-path recursion terminate. In the critical-face bases displayed above, the only possibly nonzero Morse boundary maps are
\[
\partial_6=\begin{pmatrix}0&0&-1&0&1&0\end{pmatrix},
\qquad
\partial_7=\begin{pmatrix}
1&1&0&0\\
0&0&0&-1\\
0&1&0&0\\
0&-1&1&0\\
0&1&0&0\\
0&0&-1&0
\end{pmatrix}.
\]
Direct multiplication gives \(\partial_6\partial_7=0\). The first map is primitive and has rank one. Its kernel has integral basis
\[
(e_0,e_1,e_3,e_5,e_2+e_4),
\]
where \(e_j\) are the six critical 6-cell basis vectors indexed from zero. Expressed in this kernel basis, the columns of \(\partial_7\) give the five-by-four matrix formed by taking the original rows in order \(0,1,3,5,4\). Its first four rows form an integral four-by-four minor of determinant \(-1\). Hence the image is a primitive rank-four direct summand of the rank-five kernel.

**4. From the Morse CW model to a sphere.** The matching gives a CW model with one 0-cell, one 5-cell, six 6-cells, and four 7-cells, and no other cells. The attaching maps of the 6-cells are completely classified by their degrees in \(\pi_5(S^5)\cong\mathbb Z\). Primitivity of \(\partial_6\) permits one 5/6-cell cancellation. Its resulting 6-skeleton is a wedge of five 6-spheres. The four 7-cell attaching maps are classified by their degree vectors in
\[
\pi_6\left(\bigvee^5S^6\right)\cong\mathbb Z^5.
\]
The primitive full-rank minor above allows integral changes of basis and four further 6/7-cell cancellations. Exactly one 6-cell remains, establishing \(\operatorname{Ind}_2(D)\simeq S^6\), with neither hidden torsion nor an unproved inference from Betti numbers alone.

**5. Cyclic rotation.** The automorphism \(\rho:u_i\mapsto u_{i+1},\ v_i\mapsto v_{i+1}\) has order ten. Each orbit on graph vertices consists of all ten outer vertices or all ten inner vertices. Neither orbit is an allowed face, as its induced subgraph contains vertices of degree two. Thus no nonempty simplex is setwise preserved by \(\rho\). Its unreduced simplicial Lefschetz number is zero. Since only \(H_0\cong\mathbb Z\) and \(\widetilde H_6\cong\mathbb Z\) survive, the Lefschetz formula reads \(0=1+\operatorname{tr}(\rho\mid H_6)\). The integral rank-one action is therefore \(-1\), and its powers have the claimed sign character. Explicit signed fixed-simplex enumeration of all ten powers independently reproduces the character.

## Verification
The package includes `dodecahedron_ind2_verify.cpp` (standard C++17), `dodecahedron_ind2_crosscheck.py` (standard Python 3), and their actual output when run. To reproduce:

```sh
g++ -O2 -std=c++17 dodecahedron_ind2_verify.cpp -o verify
./verify
python3 dodecahedron_ind2_crosscheck.py
```

The C++ verifier reconstructs every nonempty face, all matched pairs, the entire oriented Hasse diagram, the complete topological sort, the signed Morse matrices, the unit determinant, and all ten signed Lefschetz numbers. The Python program uses a separate forbidden-three-vertex-hypergraph definition rather than induced-degree enumeration to confirm the face vector and facet profile. Both completed successfully. Computational exhaustiveness applies only to this fixed graph, not to an infinite family.

## Relationship to prior work
Deshpande and Singh's *Higher Independence Complexes of Graphs and Their Homotopy Types* (arXiv:2001.05448, first version January 15, 2020) introduced systematic Morse-theoretic homotopy classifications for complete multipartite graphs, fully whiskered graphs, paths, cycles, and perfect rooted trees. Its staged element-matching result is useful here, but those graph-class theorems do not calculate this 3-regular girth-five graph. Abdelmalek, Deshpande, Goyal, Roy, and Singh (arXiv:2106.10863, first version June 21, 2021) study chordal graphs, trees, and caterpillars, which likewise do not contain the dodecahedral graph in their hypotheses.

A public calculation of the **ordinary** dodecahedral independence complex addresses a different object: it forbids each edge, whereas the current two-independence complex forbids every connected triple. Results about Petersen, Heawood, and Pappus two-independence complexes likewise concern nonisomorphic graphs. Known dodecahedral matching, neighborhood, graph-metric, and Čech complexes are not the present induced-component-bounded complex. No equal or logically dominating statement was identified in the sources inspected, but this bibliographic search is not a proof of uniqueness.

## Limitations
The theorem is restricted to \(GP(10,2)\). It makes no claim for all generalized Petersen graphs, all cubic graphs, or all polyhedral graphs. The cyclic statement determines the integral homology action of the displayed rotation, **not** a complete equivariant homotopy type or full automorphism-group character. The computational certificate relies on faithfully implementing finite simplicial Morse theory; the proof documents all normalization choices and integral attaching-degree arguments. Independent mathematical audit has not been performed. Unindexed or inaccessible equivalent prior work remains an originality risk.

## References
1. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v1, 2020-01-15. https://arxiv.org/abs/2001.05448
2. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy, and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v1, 2021-06-21. https://arxiv.org/abs/2106.10863
3. Wolfram MathWorld, *Dodecahedral Graph*: identification with generalized Petersen graph GP(10,2). https://mathworld.wolfram.com/DodecahedralGraph.html
