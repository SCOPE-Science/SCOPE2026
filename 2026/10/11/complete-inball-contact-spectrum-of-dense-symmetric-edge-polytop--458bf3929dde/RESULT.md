# Complete inball contact spectrum of dense symmetric edge polytopes under degree-two deletions

## Finding

Let \(n\ge5\), and let \(H\) be any simple graph on \([n]\) with maximum degree **exactly two**. Write \(G=\overline H\) for its complement, and give the zero-sum subspace \(U=\{x\in\mathbb R^n:\sum_i x_i=0\}\) its inherited Euclidean metric. The **symmetric edge polytope** is
\[
P_G=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G)\}\subset U.
\]
Define \(Q_n=\lfloor n^2/4\rfloor\), let \(d_2(H)\) be the number of degree-two vertices of \(H\), and let \(c_4(H)\) be the number of connected components of \(H\) isomorphic to a four-cycle. Put
\[
B_n=\begin{cases}\binom{n}{n/2},&n\text{ even},\\[2pt]2\binom{n}{(n-1)/2},&n\text{ odd}.\end{cases}
\]
Then the exact intrinsic Euclidean inradius of \(P_G\) is
\[
\boxed{r(P_G)=
\begin{cases}
\sqrt{\dfrac{n}{\max\{Q_n,\,3n-1\}}},&c_4(H)=0,\\[6pt]
\sqrt{\dfrac{n}{\max\{Q_n,\,4n\}}},&c_4(H)>0.
\end{cases}}
\]
The ball of this radius **centered at the origin** is maximal. Moreover, the complete number \(T(P_G)\) of facets tangent to that particular maximum inball is
\[
\boxed{T(P_G)=
\begin{cases}
2d_2(H),&c_4(H)=0,\quad 5\le n\le11,\\
B_n,&c_4(H)=0,\quad n\ge12,\\
2c_4(H),&c_4(H)>0,\quad 5\le n\le15,\\
B_{16}+2c_4(H),&c_4(H)>0,\quad n=16,\\
B_n,&c_4(H)>0,\quad n\ge17.
\end{cases}}
\]
Thus deleting any maximum-degree-two graph without a four-cycle from \(K_n\) preserves the Euclidean inradius of \(P_{K_n}\) for **all \(n\ge12\)**. With four-cycles allowed, the sharp universal threshold is **\(n=16\)**. Both cutoffs are best possible. They classify both the radius transition and the tangent-facet transition over the entire degree-two deletion class.

For instance, when \(H=C_n\), the origin-centered inball has precisely \(2n\) tangent facets for \(5\le n\le11\), but \(B_n\) tangent facets for \(n\ge12\). When \(H\) consists of one four-cycle and \(n-4\) isolated vertices, its inradius is exactly \(1/2\) for \(5\le n\le16\). Its tangent-facet count is just \(2\) for \(5\le n\le15\), rises to \(\binom{16}{8}+2=12872\) at \(n=16\), and equals \(B_n\) for every \(n\ge17\).

## Assumptions and scope

All graphs are finite, loopless, simple and undirected; \(n\ge5\) and \(\Delta(H)=2\) are essential. The inradius is the supremal radius of a Euclidean ball contained in the polytope **in its affine span**, not the ambient \(n\)-dimensional radius. For a centrally symmetric body, a maximum-radius ball can be placed at its symmetry center; the theorem does not assert that the center is unique. The facet count refers specifically to this origin-centered inball. A four-cycle in a graph with maximum degree two must be a whole connected component. The statement does not claim a comparable formula for deleted graphs of maximum degree greater than two.

## Proof

**1. Polar and optimal center.** The complement \(G\) is connected and has diameter at most two. Indeed, a pair nonadjacent in \(G\) is an edge of \(H\). Each endpoint has at most one other neighbor in \(H\), so among the \(n-2\ge3\) remaining vertices at least one is adjacent to both endpoints in \(G\). Because \(P_G\) is centrally symmetric, if a ball of radius \(r\) centered at \(c\) is contained in \(P_G\), its reflected ball centered at \(-c\) is also contained; convexity implies the ball of radius \(r\) centered at zero is contained. Its polar, taken intrinsically in \(U\), is
\[
L_G=P_G^\circ=\{y\in U:|y_i-y_j|\le1\text{ for every }\{i,j\}\in E(G)\}.
\]
Since \(P_G\) is full dimensional in \(U\), polarity gives
\[
r(P_G)^{-2}=\max_{y\in L_G}\sum_{i=1}^n y_i^2.
\]

**2. An integral maximizer with three levels.** Choose the gauge \(f_1=0\). In the \(n-1\) remaining coordinates, the inequalities \(\pm(f_i-f_j)\le1\) have an oriented incidence matrix with one column deleted; this is totally unimodular. Since the right-hand sides are integers and \(G\) is connected, every vertex of the resulting bounded polytope is integral. The strictly convex squared centered norm \(\sum_i(f_i-\bar f)^2\) achieves its maximum at vertices only, hence every maximizing potential is integer-valued up to a common constant. Because \(G\) has diameter two, every feasible integer-valued potential has range at most two; after subtracting its minimum, its image lies in \(\{0,1,2\}\).

**3. Binary potentials.** If only two consecutive values occur, translate them to \(0,1\). The potential is feasible for any choice of \(k\) ones. Its squared centered norm is
\[
\sum_i(f_i-\bar f)^2=\frac{k(n-k)}n,
\]
whose maximum is \(Q_n/n\), attained exactly when \(k\) is one of the two integers nearest \(n/2\). For \(n\ge5\), \(G\) has edges, so the constant potential cannot maximize.

**4. Three-level potentials.** Suppose both values \(0\) and \(2\) occur. Let \(A\) and \(B\) be their respective nonempty level sets, of sizes \(a\) and \(b\). Every pair in \(A\times B\) must be a nonedge of \(G\), hence an edge of \(H\). As \(\Delta(H)=2\), necessarily \(1\le a,b\le2\). Writing the middle level as zero after subtracting one, the centered squared norm is
\[
\sum_i(f_i-\bar f)^2=a+b-\frac{(b-a)^2}{n}.
\]
This is \(2\) for \((a,b)=(1,1)\), \(3-1/n\) for \((a,b)=(1,2)\) or \((2,1)\), and \(4\) for \((a,b)=(2,2)\). Since \(H\) has a degree-two vertex, every \((1,2)\) pattern is achievable by putting \(0\) at that vertex, \(2\) at its two neighbors in \(H\), and \(1\) elsewhere; its reverse is also feasible. The \((2,2)\) pattern is feasible exactly when \(H\) contains a \(K_{2,2}\), equivalently, a whole four-cycle component. Comparing these values with the binary maximum proves the radius formula.

**5. Sharp thresholds and all contacts.** The elementary comparisons
\[
Q_n<3n-1\ \text{for }5\le n\le11,\qquad Q_n>3n-1\ \text{for }n\ge12,
\]
and
\[
Q_n<4n\ \text{for }5\le n\le15,\quad Q_{16}=4\cdot16,\quad Q_n>4n\ \text{for }n\ge17
\]
are strict except at the displayed four-cycle tie. For any full-dimensional polytope, vertices of the polar correspond bijectively to facets of the original polytope. The squared norm is strictly convex, so every maximizer is a vertex of \(L_G\); these and only these polar vertices correspond to facets at distance \(r(P_G)\) from the origin. In the two-level regime, they are exactly the \(B_n\) balanced binary labelings modulo constants. In the \((1,2)\) regime, each degree-two vertex of \(H\) determines exactly two opposite labelings, giving \(2d_2(H)\) facets. In the \((2,2)\) regime, each four-cycle component contributes exactly two opposite labelings, giving \(2c_4(H)\). At \(n=16\), the balanced and four-cycle families coexist and are disjoint. This proves the entire contact spectrum and both optimal cutoffs.

## Verification

A standalone Python 3 standard-library program, `verify.py`, constructs every unlabeled graph with maximum degree two from its path/cycle component multiset, for orders \(5\) through \(11\). It independently enumerates **all** integer-valued \(\{0,1,2\}\) vertex labelings with minimum zero, retains exactly those satisfying the complementary graph's edge inequalities, and checks both the exact maximum centered norm and the number of maximizing labelings. The run checks \(404\) component-multiset profiles, of which \(73\) contain four-cycle components. It also verifies the two arithmetic cutoff comparisons for every \(5\le n\le59\). Execute `python3 verify.py` from the folder containing this result and the verifier. This finite computation is a consistency check, not the proof for arbitrary \(n\); the preceding argument provides that proof.

## Relationship to prior work

Symmetric edge polytopes and their facets have an established graph-labeling description, notably the facet theorem of Higashitani, Jochemko and Michałek; the construction is also connected to Kantorovich–Rubinstein and Lipschitz polytopes by D'Alì, Delucchi and Michałek. In particular, the polar optimization above is exactly \(n\) times the classical **graph spread** invariant: \(r(P_G)^{-2}=n\operatorname{spread}(G)\). The integer-optimizer principle is not claimed as new; it already appears in the graph-spread literature. The present contribution is the exact closed radius formula, the sole four-cycle obstruction within arbitrary degree-two deletion graphs, the sharp dimension cutoffs, and the complete count of Euclidean inball-tangent facets. These are not statements about Ehrhart polynomials, gamma-vectors, total facet counts or typical random graphs. Prior results for symmetric edge polytopes of cycles concern the original cycles, not generally their dense complements; the five-vertex self-complementary cycle is an overlapping boundary instance, not a determination of the full family.

## Limitations

The result requires \(n\ge5\), \(\Delta(H)=2\), the canonical unweighted root realization, and the inherited Euclidean metric. It does not classify all possible centers of maximal inballs, and it does not assert metric invariance under arbitrary unimodular changes of coordinates. The computation enumerates orders at most \(11\); all-order validity rests on the analytical proof. Literature comparisons cannot exclude every unindexed or unpublished equivalent identity.

## References

1. A. D'Alì, M. Juhnke-Kubitzke, D. Köhne and L. Venturello, *On the gamma-vector of symmetric edge polytopes*, arXiv:2201.09835v1 (first publicly posted 2022-01-24), primary MSC2020 52B20; especially definition and introductory comparison of graph-polytopal invariants.
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (2018), Theorem 3.1 (integral facet labelings) and Corollary 3.3.
3. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (2019), Sections 2.3 and 3.1 (Lipschitz polar and facet structure).
4. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156v1 (2009), Section 1.1 (graph spread and previously known integer maximizers).
5. B. Braun, K. Bruegge and M. Kahle, *Facets of random symmetric edge polytopes, degree sequences, and clustering*, arXiv:2204.07239v1 (2022), Section 2 (shared facet-supporting hyperplanes and the dense-graph comparison).
