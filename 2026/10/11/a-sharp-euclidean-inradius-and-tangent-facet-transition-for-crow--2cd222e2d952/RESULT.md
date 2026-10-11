# A sharp Euclidean inradius and tangent-facet transition for crown-graph symmetric edge polytopes

## Finding
For every integer \(n\ge4\), let \(C_n\) be the *crown graph*: its two vertex classes are \(\{A_1,\ldots,A_n\}\) and \(\{B_1,\ldots,B_n\}\), and its edges are precisely \(A_iB_j\) with \(i\ne j\). In the Euclidean zero-sum hyperplane \(H=\{x\in\mathbb R^{2n}:\sum_v x_v=0\}\), let
\[
P_n=\operatorname{conv}\{\pm(e_{A_i}-e_{B_j}):i\ne j\}.
\]
The radius of the largest Euclidean ball contained in \(P_n\), centered at the origin (and also allowing an arbitrary center), is exactly
\[
\boxed{r(P_n)=\left[\max\left\{\frac{n+8}{2},\ n-\frac{n\bmod2}{2n}\right\}\right]^{-1/2}.}
\]
Define \(F_n\) to be the number of facets of \(P_n\) tangent to the largest origin-centered ball. Then
\[
\boxed{F_n=\begin{cases}
2n,&4\le n\le7,\\
156,&n=8,\\
4\binom n{(n-1)/2},&n\ge9\text{ odd},\\
2\binom n{n/2},&n\ge10\text{ even}.
\end{cases}}
\]
At \(n=8\), the two geometrically distinct types of tangent facet coexist. Below this threshold every tangent facet is of the first type, and above it every tangent facet is of the second type.

## Assumptions and scope
All lengths are measured using the ambient standard inner product restricted to \(H\), not the nonisometric coordinate-deletion realization sometimes used for symmetric edge polytopes. The graph has \(2n\) vertices and is connected for \(n\ge4\). The word *facet* means a face of codimension one in \(H\). For any real coordinate assignment \(u\in\mathbb R^{2n}\), let \(\bar u=(2n)^{-1}\sum_vu_v\) and \(u^\circ=u-\bar u\mathbf1\). Differences between coordinates are invariant under this centering.

The polar polytope in \(H\) is
\[
L_n=P_n^\circ=\{u\in H:|u_{A_i}-u_{B_j}|\le1\text{ for }i\ne j\}.
\]
Write \(R_n=\max_{u\in L_n}\|u\|_2\). The claimed inradius is \(1/R_n\).

## Proof
**1. Integer potentials at the vertices.** A vertex of \(L_n\) must have a spanning connected graph of *tight edges* \(\{A_iB_j:i\ne j,|u_{A_i}-u_{B_j}|=1\}\). Indeed, if these edges are disconnected, shifting one tight component by a sufficiently small amount, followed by projection to \(H\), produces a nontrivial line segment through \(u\). Conversely, tight connectedness gives \(2n-1\) independent incidence equations and fixes a unique point of \(H\). Thus each vertex, upon adding a scalar constant, is an integer-valued potential with minimum label zero: integrate the signed unit increments along a tight spanning tree. Since the diameter of \(C_n\) equals three (for these parameters), every such potential takes values among \(0,1,2,3\).

**2. Potentials of range three.** If the minimum and maximum are \(0\) and \(3\), their vertices must be nonadjacent and distance three, hence must be a deleted matched pair \(A_i,B_i\). After possibly negating the potential and adding a constant, take \(u_{A_i}=0,u_{B_i}=3\). Constraints force \(u_{A_j}=2\) and \(u_{B_j}=1\) for each \(j\ne i\). For the \(A_j\)-labels this follows from the edge \(A_jB_i\) and an edge \(A_jB_k\) where \(k\notin\{i,j\}\); similarly for \(B_j\). The \(2n\) assignments obtained by choosing \(i\) and the sign satisfy all inequalities; their tight graphs are connected. Their uncentered labels are one zero, \(n-1\) ones, \(n-1\) twos, and one three, so
\[
\|u^\circ\|_2^2=(5n+4)-\frac{(3n)^2}{2n}=\frac{n+8}{2}=:S_n.
\]

**3. Potentials of range at most two with no diagonal gap two.** Such an assignment is feasible also for the complete bipartite graph \(K_{n,n}\), since all omitted matched differences also have absolute value at most one. The vertices of the complete-bipartite polar have two forms, up to sign and translation: the constants \(0\) and \(1\) on opposite sides; or, on one side, a nonempty group at \(0\) and its complement at \(2\), with the other side entirely at \(1\). To see exhaustion, a polar vertex again has connected tight edges. For range two the extremes must lie on the same side, forcing the other side to be entirely \(1\); a label \(1\) on the varying side would have no tight incident edge. For range one, any variation on either side disconnects the tight-edge graph, so the two sides are separately constant. A range-two configuration with \(k\) zero coordinates on the varying side has
\[
\|u^\circ\|_2^2=n-\frac{(n-2k)^2}{2n}.
\]
The maximum for \(1\le k\le n-1\) is
\[
U_n=n-\frac{n\bmod2}{2n}.
\]
This dominates the squared norm \(n/2\) of the range-one vertices. Its equality assignments have cardinality \(2\binom{n}{n/2}\) if \(n\) is even, or \(4\binom{n}{(n-1)/2}\) if \(n\) is odd. In particular, every point of this complete-bipartite polar has squared norm at most \(U_n\), since a strictly convex quadratic function is maximized on a vertex.

**4. Remaining potentials of range two.** Suppose some omitted diagonal has gap two. After negation if needed, set \(u_{A_i}=0,u_{B_i}=2\). For \(j\ne i\), necessarily \(u_{A_j}\in\{1,2\}\) and \(u_{B_j}\in\{0,1\}\). Let \(J=\{j\ne i:u_{A_j}=2\}\) and \(K=\{j\ne i:u_{B_j}=0\}\). If \(j\in J,k\in K,j\ne k\), the edge \(A_jB_k\) would have forbidden gap two. Thus either \(J\) or \(K\) is empty, or \(J=K=\{j\}\) for a single index. When one is empty, letting \(t\) be the size of the other gives exactly
\[
\|u^\circ\|_2^2=2+t-\frac{t^2}{2n}\le 2+\frac n2<S_n.
\]
For \(J=K=\{j\}\) the squared norm is \(4<S_n\). Therefore no such potential attains the claimed maximum.

**5. Maximization and tangencies.** The squared norm is strictly convex; its maximum on \(L_n\) is attained only at vertices. Steps 2--4 give \(R_n^2=\max\{S_n,U_n\}\), with all maximizing potentials and their multiplicities explicitly classified. The inequality \(S_n>U_n\) holds exactly for \(4\le n\le7\); equality holds exactly at \(n=8\); and \(U_n>S_n\) for all \(n\ge9\). As \(P_n\) is origin symmetric, averaging any inscribed ball with its reflection produces an equally large origin-centered ball. Polarity shows that the origin-centered radius is \(1/R_n\). Each maximal-norm polar point is a vertex, hence its supporting hyperplane is a facet of \(P_n\), and its distance to the origin is \(1/R_n\). Conversely, all facets tangent to that ball arise this way. Counting the assignments above proves the formula for \(F_n\). \(\square\)

## Verification
The self-contained standard-library script `verify_crown.py` enumerates every feasible integer potential in the range \(0\) through \(3\), modulo common translation and simultaneous permutation of indices; all multiplicities are exact integers. For every \(3\le n\le14\), it verifies both the maximal squared polar radius and exact tangent-facet count. For \(n=3,4\), a second direct-coordinate enumeration independent of permutation compression confirms the same values. Running `python3 verify_crown.py` prints `ALL EXACT FINITE CHECKS PASS`. The symbolic proof above, not the finite tests, establishes the conclusions for every \(n\ge4\).

## Relationship to prior work
Chen, Davis, and Korchevskaia describe the face/facet-subgraph correspondence for general symmetric edge polytopes (arXiv:2107.12315, Theorem 3). D'Alì, Juhnke-Kubitzke, and Koch relate the polars of generalized symmetric edge polytopes to cut-labeling and Ehrhart theory (arXiv:2307.04933, Section 5); in particular, their background facet-potential description explains the integrality and tight-spanning-tree criterion used here. Neither inspected treatment supplies the Euclidean radial optimization, the crown-graph inradius, or the transition in which facets are tangent to its inball. The ambient Euclidean metric is not preserved under general lattice/unimodular equivalence, so purely combinatorial facet descriptions cannot by themselves imply these metric values.

## Limitations
The smallest crown graph \(C_3\) is the six-cycle; its symmetric edge-polytope inradius is a special case of the previously established cycle result and is not asserted as a new finding here. The result concerns the specified Euclidean root embedding and \(n\ge4\); it does not claim that different embeddings or other graph families have the same radius. All mathematical independence and originality judgments are provisional pending independent literature assessment. An equivalent formulation in the literature of graph spread, Lipschitz polytopes, or Euclidean root-polytope metrics may exist. Finite verification covers only the specified finite values.

## References
1. T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315, initially submitted 2021-07-26, https://arxiv.org/html/2107.12315v2.
2. A. D'Alì, M. Juhnke-Kubitzke, M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933, 2023, https://arxiv.org/html/2307.04933v1.
