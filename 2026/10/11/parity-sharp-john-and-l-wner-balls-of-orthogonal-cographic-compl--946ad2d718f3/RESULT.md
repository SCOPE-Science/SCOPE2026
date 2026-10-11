# Parity-sharp John and Löwner balls of orthogonal cographic complete-graph polytopes

## Finding

Let \(n\ge5\) be an integer. The intrinsic John ellipsoid and Löwner ellipsoid of the orthogonal cographic polytope defined below are uniquely determined Euclidean balls centered at the origin. Their squared radii are
\[
r_n^2=\begin{cases}
\dfrac{2}{n(n-1)},& n\text{ odd},\\[4pt]
\dfrac{2}{n(n-2)},& n\text{ even},
\end{cases}
\qquad R_n^2=\dfrac{n-2}{n}.
\]
A facet meets the John ball if and only if its polar flow corresponds, in odd order, to a regular tournament on all vertices, or, in even order, to an Eulerian orientation of the complete graph with exactly a perfect matching deleted. Consequently every facet is tangent when \(n\) is odd, whereas non-tangent facets occur when \(n\) is even. Every projected signed-edge vertex lies on the Löwner sphere. For \(d=(n-1)(n-2)/2\), the exact containment factor is
\[
\frac{R_n}{r_n}=\begin{cases}\sqrt d,&n\text{ odd},\\[3pt]\dfrac{n-2}{\sqrt2},&n\text{ even}.
\end{cases}
\]
Thus this natural family attains the sharp symmetric John containment factor in all odd orders, but not in even orders.

## Assumptions and scope

Fix the complete graph \(K_n\) on \(\{1,\dots,n\}\), orient every edge from its smaller to its larger endpoint, and identify its \(N=\binom n2\) edge coordinates with the standard orthonormal basis \(\{u_{ij}:i<j\}\) of \(\mathbb R^N\). Let \(B:\mathbb R^N\to\mathbb R^n\) be the signed vertex-edge incidence map, \(Bu_{ij}=e_j-e_i\). The real circulation space is \(Z_n=\ker B\), with the *induced edge-coordinate Euclidean inner product*, and \(\Pi_n\) denotes orthogonal projection onto \(Z_n\). Define
\[
P_n=\operatorname{conv}\{\pm\Pi_n u_{ij}:1\le i<j\le n\}\subset Z_n.
\]
The signed projected columns realize the dual (cographic) matroid of \(K_n\) up to an invertible linear change of coordinates, so this is a specified orthogonal metric realization of its generalized symmetric edge polytope. The metric is essential: no assertion is made that arbitrary integer totally unimodular realizations give the same Euclidean radii. John means maximum-volume inscribed ellipsoid; Löwner means minimum-volume enclosing ellipsoid, both taken in \(Z_n\), not in the ambient edge space.

A **polar flow** is \(f\in Z_n\) with \(|f_{ij}|\le1\) for every edge. When all its nonzero entries are \(\pm1\), direct each supported edge according to its sign relative to the fixed orientation. Its conservation condition \(Bf=0\) says that this supported directed graph is Eulerian. A **contact facet** means a facet at Euclidean distance exactly \(r_n\) from the origin.

## Proof

**Projection and outer sphere.** The incidence matrix satisfies \(BB^{\mathsf T}=nI-J\), and its row vectors sum to zero. Hence
\[
\Pi_n=I-\frac1n B^{\mathsf T}B,\qquad
\|\Pi_n u_{ij}\|^2=1-\frac2n=\frac{n-2}{n}.
\]
The projections span \(Z_n\), whose dimension is \(d=N-n+1=(n-1)(n-2)/2\). Every signed projected column is an exposed vertex: its scalar product with itself is \((n-2)/n\), whereas the absolute scalar product with any different edge projection is at most \(1/n\). Thus all these vertices lie at the asserted outer radius.

**All polar vertices.** Intrinsic polarity gives
\[
Q_n=P_n^\circ=\{f\in Z_n:|f_{ij}|\le1\text{ for all }i<j\}.
\]
For a point \(f\in Q_n\), let \(F\) be the undirected graph of unsaturated coordinates \(|f_{ij}|<1\). If \(F\) has a cycle, a sufficiently small signed circulation around it can be added or subtracted while remaining in \(Q_n\); thus \(f\) is not extreme. Conversely, if \(F\) is a forest, any two feasible points having midpoint \(f\) must agree with \(f\) on all saturated coordinates. Their difference is then a circulation supported on a forest and must vanish, so \(f\) is extreme. Therefore \(f\) is a polar vertex **exactly when its unsaturated graph is a forest**.

Every such vertex is integral. Indeed, for an unsaturated edge \(ij\in F\), remove that edge from its tree, take the vertex set \(S\) of either resulting component, and sum the conservation equations over \(S\). Among edges crossing this cut, the only unsaturated one is \(ij\); hence its flow equals an integer sum of saturated \(\pm1\) flows. Because its absolute value is less than one, it is zero. Thus polar vertices have entries in \(\{-1,0,1\}\), and their zero-edge set is a forest. Conversely every balanced trinary vector with forest zero set is an extreme point by the preceding argument.

**Parity and closest facets.** At each graph vertex, the number of nonzero incident coordinates must be even, since the \(\pm1\) contributions balance. Accordingly, for the zero-edge forest \(F\),
\[
\deg_F(v)\equiv n-1\pmod2\quad\text{for every vertex }v.
\]
If \(n\) is odd, all zero degrees must be even. A nonempty finite forest has a leaf of degree one, so \(F\) is empty. Thus every polar vertex has squared norm \(N=n(n-1)/2\), corresponding exactly to an Eulerian orientation (regular tournament) of \(K_n\); existence follows from the standard cyclic orientation of an odd-order complete graph.

If \(n\) is even, every vertex of \(F\) has positive odd degree, so \(2|E(F)|\ge n\). Consequently any polar vertex satisfies
\[
\|f\|^2=N-|E(F)|\le N-\frac n2=\frac{n(n-2)}2.
\]
Equality holds exactly if every vertex of \(F\) has degree one, meaning that \(F\) is a perfect matching. Every perfect matching achieves equality: its complement is connected and of even degree \(n-2\), and therefore admits an Eulerian orientation producing an extreme flow. Nonmaximum vertices exist: take the star of \(n-1\) zero edges at one vertex and a regular tournament on the remaining odd number \(n-1\) of vertices. This is a balanced trinary extreme flow with squared norm \((n-1)(n-2)/2<n(n-2)/2\). The polar maximum squared norm is therefore
\[
\max_{f\in Q_n}\|f\|^2=\begin{cases}\dfrac{n(n-1)}2,&n\text{ odd},\\[3pt]\dfrac{n(n-2)}2,&n\text{ even}.\end{cases}
\]
The maximum over \(Q_n\) occurs at a vertex by convexity. Since \(P_n=(Q_n)^\circ\), the largest Euclidean ball centered at zero contained in \(P_n\) has radius the reciprocal of \(\max_{f\in Q_n}\|f\|\). A facet \(\langle x,f\rangle=1\), associated with a polar vertex \(f\), is at distance \(1/\|f\|\); this proves the radius formula and the complete contact-facet classification.

**Why John and Löwner ellipsoids are balls.** Relabeling vertices acts orthogonally on the edge space by the induced signed permutations of oriented edges. It preserves \(Z_n\) and \(P_n\). The action of the symmetric group \(S_n\) on \(Z_n\) is irreducible over \(\mathbb R\). Here is an elementary proof. Signed triangle circulations \(t_{ijk}=u_{ij}+u_{jk}-u_{ik}\) (with consistently ordered indices) span \(Z_n\). Given a nonzero invariant subspace \(U\subset Z_n\), select \(a\in U\) and a triangle with \(\langle a,t_{ijk}\rangle\ne0\). Alternating \(a\) over the six permutations of \(i,j,k\) gives a nonzero vector in the sign-isotypic component of the edge space under this \(S_3\). That component is exactly the line spanned by \(t_{ijk}\): among edge coordinates, only the three edges internal to the triple carry a sign summand; the other edge-coordinate representations are sums of trivial and standard permutation summands. Thus \(t_{ijk}\in U\), and all its relabeled triangles belong to \(U\), whence \(U=Z_n\).

The unique maximal-volume inscribed ellipsoid and the unique minimal-volume circumscribed ellipsoid are preserved by this orthogonal group. Their centers are fixed vectors, necessarily zero by irreducibility and \(d>1\). Their symmetric quadratic forms commute with the action; each eigenspace is invariant, so irreducibility forces each form to be a scalar multiple of the identity. Both ellipsoids are therefore centered Euclidean balls. Their radii must be the exact origin-centered inradius and vertex circumradius calculated above. In particular every signed projected generator is a Löwner-sphere contact.

Taking the ratio of the two formulas gives \(R_n/r_n=\sqrt d\) in odd order and \(R_n/r_n=(n-2)/\sqrt2<\sqrt d\) in even order. This concludes the proof.

## Verification

The supplied standalone, integer/rational-arithmetic checker `verify.py` enumerates balanced trinary circulations in orders \(n=4,5,6\), filters zero-edge forests, checks exact orthogonal projection identities, and verifies the extremal squared polar norms. It gives \(14\) polar vertices in order \(4\), with squared norms \(3\) (eight) and \(4\) (six); \(24\) in order \(5\), all squared norm \(10\); and \(3594\) in order \(6\), of squared norms \(10\) (\(1584\)), \(11\) (\(1440\)), and \(12\) (\(570\)). All numbers were obtained by exhaustive enumeration within these explicitly finite domains. An independently parameterized halfspace-intersection reconstruction in orders \(4\) and \(5\) returned respectively \(14\) and \(24\) polar vertices. The proof above, not finite enumeration, establishes every order \(n\ge5\).

## Relationship to prior work

D’Alì, Juhnke-Kubitzke and Koch introduce symmetric edge polytopes of regular matroids and characterize facets via spanning \(2\)-cuts. Their Proposition 5.12 recovers the nowhere-zero-flow behavior relevant to odd complete graphs, but does not impose the orthogonal cycle-space metric or determine either Euclidean ellipsoid, the parity-sharp radii, or the even-order perfect-matching tangent facets. Bandekar and coauthors connect the *volumes* of these cographic facets to arborescence counts and study extremal Eulerian orientations; volume is not the facet-to-origin distance, and their results do not yield the present metric extremum. Publicly indexed work on acyclic signatures of complete graphs minus a matching concerns acyclic, rather than Eulerian, orientations and does not imply this classification. The present result uses a specific orthogonal realization, so unimodular equivalence statements alone do not transfer these Euclidean formulas.

## Limitations

The statement does not cover arbitrary graphs, arbitrary real embeddings of a cographic matroid, or arbitrary Euclidean metrics on a totally unimodular coordinate representation. The classification gives contact *facets*, not their face volumes or combinatorial face lattices in general. The finite checks cover only the indicated orders and are not a substitute for the all-order proof. Literature screening cannot exclude unidentified prior equivalent formulas; no independent audit or external certification is claimed.

## References

1. Alessio D’Alì, Martina Juhnke-Kubitzke, Melissa Koch, “On a generalization of symmetric edge polytopes to regular matroids,” arXiv:2307.04933v1 (first public version 2023-07-10), especially §5 and Theorem 5.8, Proposition 5.12. https://arxiv.org/html/2307.04933v1
2. Sandip Bandekar et al., “Extremal number of arborescences,” arXiv:2409.17893v1 (first public version 2024-09-26), especially §1.2. https://arxiv.org/html/2409.17893v1
