# Primitive square-pair cycle basis for three-robust clique homology of rectangular grids

## Finding

**Theorem.** Fix arbitrary integers \(m,n\ge 2\). Let \(G=P_m\square P_n\) be the rectangular grid graph and let \(K=\operatorname{Cliq}_3(G)\) consist of vertex subsets inducing no independent triple. Let \(\mathcal F\) be the \(F=(m-1)(n-1)\) elementary square faces. Give the grid its standard planar orientation, and let \(z_Q\in C_1(G;\mathbb Z)\) be the counterclockwise simplicial boundary of each \(Q\in\mathcal F\). For every unordered pair of distinct faces define the exterior product \(Z_{Q,R}=z_Q\wedge z_R\in C_3(K;\mathbb Z)\).

Then every \(Z_{Q,R}\) is a simplicial cycle, and

\[
H_3(K;\mathbb Z)=\bigoplus_{\{Q,R\}\in\binom{\mathcal F}{2}}\mathbb Z[Z_{Q,R}].
\]

Consequently the full geometric symmetry group of the grid acts on integral third homology as the **unsigned permutation lattice on unordered pairs of elementary squares**. For a grid symmetry \(g\), if \(f_g\) is the number of fixed squares and \(t_g\) the number of two-cycles in its permutation of \(\mathcal F\), then

\[
\operatorname{tr}(g\mid H_3(K;\mathbb Q))=\binom{f_g}{2}+t_g.
\]

The theorem asserts a primitive **integral chain-level basis**; it does not claim the already established nonequivariant sphere-wedge classification or merely rederive a rational character.

## Assumptions and scope

The paths \(P_m,P_n\) have \(m,n\) vertices, so \(G\) has \(mn\) vertices. The coefficient chains are ordinary oriented simplicial chains. Formally, embed \(C_{k-1}\) in the degree-\(k\) part of the exterior algebra \(\Lambda_{\mathbb Z}\langle e_v:v\in V(G)\rangle\), identifying an increasing tuple of vertices with its wedge. The product of two oriented one-chains is their degree-two exterior product; repeated vertices contribute zero. A four-vertex set is a simplex of \(K\) exactly when it contains a matching of size two, by König's theorem for bipartite graphs. Every five-vertex set contains three vertices in one bipartition class, so \(K\) has dimension at most three. When \(F=1\), the asserted empty basis identifies the zero third homology.

A **square attachment** adjoins an elementary square to an earlier connected union of grid squares. An **edge attachment** has two new vertices, while a **corner attachment** has one new vertex and adjoins the other three vertices in a two-edge path. Take the standard row-by-row ordering, first along one row and then through each later row from its leftmost square; the first square in a new row is edge-attached and the remaining ones are corner-attached. In a corner attachment, the two old, nonadjacent opposite corners have exactly one common neighbor in the prior subgraph.

## Proof

**1. Chain construction.** The simplicial boundary extends to the exterior chain algebra as the unique degree-minus-one graded derivation with \(\partial e_v=1\). Each face boundary satisfies \(\partial z_Q=0\), so the graded Leibniz rule gives \(\partial(z_Q\wedge z_R)=0\). Each nonzero four-vertex summand of the product comes from disjoint edges, hence is a three-simplex of \(K\) by the bipartite matching criterion. Thus \(Z_{Q,R}\in\ker(\partial_3)\). Since \(K\) has no simplices of dimension four, \(H_3(K;\mathbb Z)=\ker(\partial_3)\subset C_3(K;\mathbb Z)\).

**2. An injectivity lemma valid over every field.** Let \(H\) be any simple graph and let distinct, nonadjacent vertices \(u,v\) have **at most one** common neighbor. For an arbitrary field \(k\), wedge multiplication by \(a=e_u-e_v\) defines an injection

\[
\ker(\partial:C_1(H;k)\to C_0(H;k))\longrightarrow\Lambda^3(k^{V(H)}),\qquad z\mapsto a\wedge z.
\]

Indeed, if \(a\wedge z=0\), exactness of the elementary exterior-algebra Koszul sequence for a nonzero degree-one vector gives \(z=a\wedge w\) for some one-vector \(w\). Comparing coefficients of \(e_u\wedge e_t\) and \(e_v\wedge e_t\), the coefficient of \(e_t\) in \(w\) must vanish unless \(t\) is adjacent to both \(u\) and \(v\). The coefficient of \(e_u\wedge e_v\) must also vanish because \(u,v\) are not an edge. With at most one common neighbor \(y\), therefore \(z=c(e_u-e_v)\wedge e_y\) for some \(c\in k\) (or \(z=0\) if no such \(y\) exists). But \(\partial z=-c(e_u-e_v)\); since \(z\) is a graph cycle, \(c=0\), proving injectivity even in characteristic two.

**3. Linear independence over every field, by square attachment.** The counterclockwise boundaries of the first \(s\) squares form a basis of the graph cycle space of their union over every field. To see this, every added square contributes one new independent fundamental cycle (it has at least one new edge), and the graph cycle rank increases by exactly one for either attachment type. We prove by induction on \(s\) that the \(\binom s2\) products of two distinct square boundaries are linearly independent in simplicial degree three over **every** field. For one square this is vacuous.

If square \(s+1\) is edge-attached with two new vertices \(x,y\), the component of \(z_{s+1}\wedge z_i\) supported on four-sets containing **both** \(x,y\) equals, up to a common overall sign, \((e_x\wedge e_y)\wedge z_i\). The old products have no new vertices and hence zero component there. Independence of the graph cycles \(z_i\) makes the new products independent modulo all old products.

If square \(s+1\) is corner-attached with new vertex \(x\), old opposite corners \(u,v\), and common neighbor \(y\), its boundary has the form \(z_{s+1}=\pm(e_x-e_y)\wedge(e_u-e_v)\), with the factors possibly swapped according to the orientation convention. Projecting \(z_{s+1}\wedge z_i\) onto four-sets containing \(x\), and removing its \(e_x\)-factor, yields \(\pm(e_u-e_v)\wedge z_i\). The old products have no \(x\). The injectivity lemma applies to the old union graph, because \(u,v\) are nonadjacent with their unique common neighbor \(y\); consequently the new products are independent modulo all old products. This closes the induction for all \(m,n\ge 2\) and every field, in particular for \(\mathbb Q\) and \(\mathbb F_p\) for every prime \(p\).

**4. Integral saturation and spanning.** Filakovský's grid theorem [1, Theorem 1.1] independently establishes \(K\simeq\bigvee^{\binom F2}S^3\). Thus \(H_3(K;\mathbb Z)\) is a free group of rank \(r=\binom F2\). Let \(L\) be the subgroup generated by the \(r\) product cycles. The field-independent independence just proved implies \(L\) has rank \(r\) and maps injectively into \(C_3(K;\mathbb F_p)\) for every prime \(p\). Since \(H_3=\ker\partial_3\) is a saturated subgroup of the free simplicial chain group \(C_3\), a nontrivial finite quotient \(H_3/L\) would have \(p\)-torsion for some prime \(p\), contradicting injectivity of \(L/pL\) into \(C_3/pC_3\). Hence \(H_3=L\) integrally.

**5. Natural symmetry action.** A planar grid isometry \(g\) sends every counterclockwise oriented square boundary to \(\epsilon(g)z_{gQ}\), where \(\epsilon(g)\in\{+1,-1\}\) is its global orientation sign. Because wedge multiplication of degree-two chains is commutative, \(gZ_{Q,R}=\epsilon(g)^2Z_{gQ,gR}=Z_{gQ,gR}\). This gives the integral permutation-lattice identification and the trace formula, since an unordered pair is fixed precisely when both constituent squares are individually fixed or form one two-cycle. No sign appears, including for coordinate swaps on square grids.

## Verification

The accompanying `verify.py` implements ordered simplicial chains using integer coefficients and checks cycle boundaries, simplex eligibility, signed exterior joins, and exact grid isometry actions. It tests all ten grids \(2\le m\le n\le5\), using modular rank checks in characteristics \(2,3,5\). It independently computes the full third-boundary kernel over \(\mathbb F_3\) for the five grids \((2,3),(2,5),(3,3),(3,4),(4,4)\). All assertions pass. These finite tests support the formulas but **do not substitute for** the field-uniform induction and the integral-saturation argument above. Reproduce with `python3 verify.py` (Python standard library only).

## Relationship to prior work

Filakovský [1] proves the nonequivariant homotopy equivalence and the requisite Betti-number formula for all rectangular grids; Sections 1 and 3 were read, including the actual edge/corner attachment sequence and its one-common-neighbor condition. That theorem gives an abstract free homology group, **not** a primitive cycle basis inside simplicial chains or a specified integral group action.

The existing indexed work titled *Two-square permutation character of three-robust clique complexes of even grids* describes a rational reflection-character permutation module in the even-by-even subfamily. *Equivariant Euler characters of 3-robust clique complexes of connected bipartite graphs* describes alternating rational characters. Neither accessible indexed summary determines an **integral chain-level basis**, which remains a strictly stronger assertion: rational-character agreement does not determine integral lattices. The full texts of those indexed records could not be inspected, so possible implicit integral generators remain an originality risk. Chandrakar and collaborators [2] study homotopy types of the Alexander-dual total cut complexes; this is not a construction of the integral face-pair generators claimed here.

## Limitations

The result is specific to the third robust-clique complex of rectangular Cartesian grid graphs. It does not classify robust levels four and above, nonrectangular square sequences, or all abstract automorphisms unrelated to the geometric grid symmetries. The independent prior theorem supplies the abstract top-homology rank; the new proof supplies explicit integral representatives, primitive spanning, and the actual isometry action. Equivalent unpublished or unindexed integral constructions cannot be ruled out, and no independent audit has been carried out.

## References

1. M. Filakovský, *The Topology of \(k\)-Robust Clique Complexes in Grid-like Graphs*, arXiv:2602.11365, first posted 2026-02-11, Theorem 1.1 and Section 3. https://arxiv.org/abs/2602.11365
2. P. Chandrakar et al., *Topology of Total Cut and Cut Complexes of Grid Graphs*, arXiv:2408.07646, initial preprint 2024. https://arxiv.org/abs/2408.07646
