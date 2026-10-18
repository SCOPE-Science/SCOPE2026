# A uniform mixed-dimensional Rips sphere wedge for type-\(D_n\) roots

## Finding
For each integer \(n\ge5\), put
\[
R_n=\{\epsilon e_i+\delta e_j:1\le i<j\le n,\ \epsilon,\delta\in\{-1,1\}\}\subset\mathbb R^n.
\]
Use ordinary Euclidean distance and the inclusive Vietoris--Rips convention (a finite set is a face when all pairwise distances are at most \(r\)). For every \(\sqrt2\le r<2\),
\[
\boxed{\operatorname{VR}_{\le r}(R_n)\simeq
\left(\bigvee^{\,8\binom n3-2n(n-1)+2n-1}S^2\right)
\vee\left(\bigvee^{\,2n}S^{n-2}\right).}
\]
In particular, the only nonzero reduced **integral** homology groups are free of ranks
\[
\operatorname{rank}\widetilde H_2=8\binom n3-2n(n-1)+2n-1,
\qquad \operatorname{rank}\widetilde H_{n-2}=2n.
\]
The dimensions are different because \(n\ge5\). The first examples are \(\bigvee^{49}S^2\vee\bigvee^{10}S^3\) for \(n=5\) and \(\bigvee^{111}S^2\vee\bigvee^{12}S^4\) for \(n=6\).

## Assumptions and scope
No ambient points other than the \(2n(n-1)\) explicitly listed roots are used. All simplicial complexes are finite, and wedge notation denotes ordinary based homotopy equivalence of geometric realizations. We do not assert the full Rips filtration or equivariance of the displayed wedge splitting. Each root has squared norm \(2\), so for distinct roots the smallest positive squared distance is \(2\); the next is \(4\). Therefore the complex is constant on \([\sqrt2,2)\), and its edges there are precisely pairs of roots of inner product \(1\).

Call \(P_n=\{(i,\epsilon):i\in[n],\epsilon\in\{-1,1\}\}\) the signed-coordinate set. A root \(\epsilon e_i+\delta e_j\) corresponds to an unordered pair \(\{(i,\epsilon),(j,\delta)\}\) of distinct coordinate indices. Let \(\mathcal O_n\) be the simplicial boundary of the \(n\)-crosspolytope, namely the join of \(n\) two-point sets \(\{(i,+1),(i,-1)\}\). Its one-skeleton is the complete \(n\)-partite graph with two vertices in every part.

## Proof
**1. Classify the cliques.** Two *distinct* roots have inner product \(1\) exactly when their signed-coordinate pairs share precisely one signed coordinate. If their underlying two-element coordinate supports coincide, their inner product cannot be \(1\). Accordingly, the coordinate supports of roots in a clique are distinct two-subsets that intersect pairwise. An elementary classification of pairwise-intersecting distinct two-subsets gives two possibilities: all share one common index, or they are exactly the three edges on a three-element coordinate set. In the common-index case, adjacency forces the common sign to be the same for all roots. In the three-edge case, pairwise adjacency uniquely forces a consistent sign on each of the three indices. Thus every simplex is either in a signed-coordinate star or is one of the exceptional triangles indexed by three signed coordinates from three distinct indices. There are exactly \(8\binom n3\) exceptional triangles; none has a higher-dimensional coface outside the stars.

**2. Describe the stars and intersections.** For every \(p=(i,\epsilon)\in P_n\), let \(A_p\) be the subcomplex induced by roots containing \(p\). For each \(j\ne i\) one may select at most one of the two roots \(\epsilon e_i+e_j\) and \(\epsilon e_i-e_j\), and selections for different \(j\) are compatible. Hence
\[
A_p\cong\mathop{*}_{j\ne i}S^0\cong S^{n-2}.
\]
For signed coordinates \(p,q\) from different indices, \(A_p\cap A_q\) is the single root corresponding to \(\{p,q\}\); for opposite signs on the same index their intersection is empty. Every triple intersection is empty. Consequently the pairwise intersection graph of the \(2n\) stars is exactly the one-skeleton of \(\mathcal O_n\).

**3. Replace point identifications by cylinders.** Write \(Y=\bigcup_{p\in P_n}A_p\). Because star intersections are individual vertices and there are no triple intersections, the ordinary gluing of the stars is a homotopy pushout of the diagram of their point intersections. It can equivalently be modeled by disjoint star copies, joined by one interval for every edge \(\{p,q\}\) of the crosspolytope graph. For each star, choose a tree in its one-skeleton joining its finitely many intersection vertices. Quotienting by this tree is a homotopy equivalence (collapse of a contractible subcomplex in a CW complex); it makes all the star's intersection vertices one point while preserving the homotopy type \(S^{n-2}\). The resulting model of \(Y\) is a graph of \(2n\) spheres over the crosspolytope graph.

**4. Attach the exceptional triangles.** An exceptional triangle indexed by signed coordinates \(p,q,s\) has vertices the three pair-roots \(pq,ps,qs\). Its three boundary edges lie respectively in \(A_p,A_s,A_q\). In the interval model from step 3, its attaching loop consists of the three corresponding graph intervals interspersed with paths inside these three stars. The internal star paths become based loops after tree contraction; they are null-homotopic because \(n-2\ge3\). By the homotopy extension property, all the finitely many triangle attaching maps may be replaced simultaneously, up to homotopy equivalence of their adjunction spaces, by the three-edge graph loops \(p\to q\to s\to p\). As \(p,q,s\) ranges over signed triples with different indices, these are exactly the two-faces of \(\mathcal O_n\). Thus
\[
\operatorname{VR}_{\le\sqrt2}(R_n)\simeq
\mathcal O_n^{(2)}\vee\bigvee^{2n}S^{n-2}.
\]
The wedge splitting is nonequivariant; it does not depend on selecting compatible trees under symmetry.

**5. Identify the two-dimensional factor.** The full crosspolytope boundary is \(\mathcal O_n\cong S^{n-1}\), and \(n\ge5\). Its two-skeleton is simply connected, since attaching cells of dimension at least three cannot change the fundamental group. A simply connected two-dimensional CW complex is homotopy equivalent to a wedge of two-spheres: choose integral degree-one representatives of a basis of its free \(H_2\), use Hurewicz to construct a map from a wedge of two-spheres, and apply the simply connected Whitehead theorem. The face numbers of \(\mathcal O_n^{(2)}\) are
\[
f_0=2n,\qquad f_1=2n(n-1),\qquad f_2=8\binom n3.
\]
As its first reduced homology vanishes, its second Betti number is \(f_2-f_1+f_0-1\), which equals the number displayed in the finding. The decomposition proves the homotopy and integral homology statements for every \(n\ge5\). \(\square\)

## Verification
Run the supplied standalone file `verify_dn_root.py` with Python 3; it uses only the standard library. It independently constructs all roots and simplices at the inclusive threshold, checks the forbidden nonstar faces and exact exceptional-triangle count, and computes all boundary-matrix ranks over \(\mathbb F_2\) by bitset Gaussian elimination for \(n=4,5,6,7\). The reproduced face vectors are \((24,96,96)\), \((40,240,400,160)\), \((60,480,1120,960,384)\), and \((84,840,2520,3360,2688,896)\). The resulting positive-degree Betti numbers are respectively \(\beta_2=23\); \((\beta_2,\beta_3)=(49,10)\); \((\beta_2,\beta_4)=(111,12)\); and \((\beta_2,\beta_5)=(209,14)\). The exact combinatorial and homotopy argument above, not these finite characteristic-two calculations, proves the general integral statement.

## Relationship to prior work
The connection between type-\(D_n\) symmetry and topology of its associated half-cube is studied by Green [1], but its half-cube CW subcomplexes have a different vertex set and adjacency structure from the Euclidean *root-set* Rips complex here. Goyal--Shukla--Singh [2, Theorem 3.9] determine clique complexes of actual line graphs of complete multipartite graphs. Although the root graph here has the same vertices as the line graph of the complete graph on the signed coordinate pairs, it deletes every line-graph adjacency between roots with common signed coordinate and opposite signs on the other coordinate. In fact the four roots \(u=e_1+e_2\), \(v=e_1+e_3\), \(w=e_1-e_3\), and \(z=e_2+e_4\) induce a claw centered at \(u\): the center has inner product one with each leaf, and distinct leaves have inner product zero. Hence this root graph cannot be the line graph of a simple graph. That deletion changes the homotopy type substantially: for \(n\ge5\), our complex has nonzero integral homology above degree two, unlike the studied multipartite line-graph complexes. Neither theorem implies the present mixed-dimensional splitting. The rank-four \(24\)-cell case gives \(23\) two-spheres and is outside the claimed new domain.

## Limitations
The proof addresses only the inclusive Euclidean thresholds \(\sqrt2\le r<2\), and the ordinary (not equivariant) homotopy type. It does not compute later filtration maps, integral symmetry modules, or analogous types for exceptional root systems. An equivalent result may exist under different signed-line-graph terminology; absence from the searched sources is not a proof of global novelty. The machine computation is mod two and checks only \(n=4,5,6,7\); integrality and all larger \(n\) follow from the topological proof, not finite experimentation.

## References
[1] R. M. Green, *Homology representations arising from the half cube* (first submitted 2008-06-09), arXiv:0806.1503, https://arxiv.org/abs/0806.1503.

[2] S. Goyal, S. Shukla, and A. Singh, *Topology of Clique Complexes of Line Graphs* (first submitted 2020-09-25), arXiv:2009.12130, https://arxiv.org/abs/2009.12130; in particular Sections 2 and 3.1 and Theorem 3.9.
