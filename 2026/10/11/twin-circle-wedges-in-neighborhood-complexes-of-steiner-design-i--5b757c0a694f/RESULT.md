# Twin circle wedges in neighborhood complexes of Steiner-design incidence graphs
## Finding
For every nontrivial Steiner \(2\)-design \(D=S(2,k,v)\) with \(2\le k<v\), let \(b\) be the number of blocks, let \(r\) be the number of blocks through each point, and let \(G_D\) be the point-block incidence graph. Then the Lovász neighborhood complex \(\mathcal N(G_D)\) has exactly two connected components. Each component simplicially collapses to a connected graph of cycle rank \(\mu=vr-v-b+1=b(k-1)-v+1=v(r-1)-b+1\), so each component has simple-homotopy type \(\bigvee^{\mu}S^1\). Hence \(\mathcal N(G_D)\simeq(\bigvee^{\mu}S^1)\sqcup(\bigvee^{\mu}S^1)\). For a projective plane of order \(q\), this specializes to \(\mu=q^3\).

The two components are the point-side and block-side parts of the neighborhood complex. The statement is stronger than a Betti-number calculation: each component is reduced by elementary simplicial collapses to a graph, so the displayed wedge is its simple-homotopy type.

## Assumptions and scope
A Steiner \(2\)-design \(D=S(2,k,v)\) consists of a set \(P\) of \(v\) points and a collection \(\mathcal B\) of \(k\)-element blocks such that every pair of distinct points lies in exactly one block. We assume \(2\le k<v\). Standard double counting gives a constant replication number
\[
r=\frac{v-1}{k-1}
\]
and a block count \(b\) satisfying \(bk=vr\).

The incidence graph \(G_D\) is bipartite on \(P\sqcup\mathcal B\), with a point adjacent to a block exactly when it lies in that block. For a graph \(G\), \(\mathcal N(G)\) denotes the Lovász neighborhood complex: a finite set of vertices is a simplex when its members have a common graph neighbor.

No existence assertion is made for parameter triples for which no Steiner design exists. The theorem concerns the ordinary neighborhood complex, not closed-neighborhood, Vietoris–Rips, independence, matching, or cut complexes.

## Proof
Because \(G_D\) is bipartite, a simplex of \(\mathcal N(G_D)\) cannot mix point and block vertices. Thus \(\mathcal N(G_D)\) is the disjoint union of a point-side complex \(X_P\) and a block-side complex \(X_B\).

On the point side, a set of points has a common neighbor precisely when all of them lie in one block. Therefore the maximal simplices of \(X_P\) are the \((k-1)\)-simplices \(\Delta(B)\), one for each \(B\in\mathcal B\). Two distinct blocks share at most one point: if they shared two, that point-pair would lie in two blocks. Hence no positive-dimensional face belongs to two different maximal simplices.

We use the following relative-collapse lemma. If \(V\) is a finite vertex set and \(T\) is any spanning tree on \(V\), then the simplex \(\Delta(V)\) simplicially collapses to \(T\) while retaining every vertex. Induct on \(|V|\). Choose a leaf \(x\) of \(T\) with neighbor \(y\), and put \(W=V\setminus\{x\}\). Since \(\Delta(W)\) collapses to the vertex \(y\), coning that collapsing sequence from \(x\) collapses \(x*\Delta(W)\) relative to its base onto \(\Delta(W)\cup xy\). Then apply the induction hypothesis inside \(\Delta(W)\), leaving the edge \(xy\) untouched. This yields \(T\).

Apply the lemma independently to every block simplex of \(X_P\). Independence is legitimate because different block simplices share no positive-dimensional face. Choose an arbitrary spanning tree inside each block. The result is a graph with \(v\) vertices and exactly \(b(k-1)\) edges; edges contributed by different blocks are distinct because every point-pair lies in a unique block. This graph is connected: any two points lie in their unique common block, and that block's chosen tree connects them. Its cycle rank is therefore
\[
\mu_P=b(k-1)-v+1.
\]

On the block side, the maximal simplex associated with a point \(p\) consists of the \(r\) blocks containing \(p\). Two such point-star simplices, for distinct points \(p,p'\), intersect in exactly the unique block containing \(p,p'\). Again all positive-dimensional faces belong to only one maximal simplex, so each point-star simplex collapses independently to a spanning tree. The resulting graph has \(b\) vertices and \(v(r-1)\) edges. It is connected: for blocks \(B,C\), choose \(p\in B\) and \(q\in C\); the unique block through \(p,q\) connects \(B\) to \(C\) through the two point-star trees. Hence
\[
\mu_B=v(r-1)-b+1.
\]

Since \(bk=vr\),
\[
\mu_P=bk-b-v+1=vr-v-b+1=\mu_B.
\]
Calling the common value \(\mu\), both components collapse to connected graphs of rank \(\mu\), and every connected graph of cycle rank \(\mu\) is homotopy equivalent to \(\bigvee^\mu S^1\). The explicit collapses show equality of simple-homotopy types, not only ordinary homotopy types.

For a projective plane of order \(q\), one has \(v=b=q^2+q+1\) and \(k=r=q+1\). Thus
\[
\mu=(q+1)(q^2+q+1)-2(q^2+q+1)+1=q^3.
\]

## Verification
The standalone script `verify.py` reconstructs four concrete Steiner designs: \(S(2,2,5)\), the affine plane \(AG(2,3)\), and the projective planes \(PG(2,2)\) and \(PG(2,3)\). It verifies the Steiner axiom, replication and block counts, builds both neighborhood-complex components, and performs explicit elementary collapses to chosen facet trees. In all four cases it independently checks that both collapsed graphs have cycle rank \(\mu=vr-v-b+1\). The projective-plane tests give \(\mu=8\) and \(27\), matching \(q^3\).

The finite computations corroborate the all-parameter proof; they are not used to extrapolate from examples.

## Relationship to prior work
Kozlov gives the standard neighborhood-complex definition and proves that \(\mathcal N(G)\) and \(\operatorname{Hom}(K_2,G)\) have the same simple-homotopy type for every graph. That general theorem supplies the simple-homotopy framework but does not compute the neighborhood complex of Steiner-design or projective-plane incidence graphs. In particular, the inspected paper contains no projective-plane specialization.

Shukla proves that for connected graphs of maximum degree at most \(3\), every connected component of the neighborhood complex is contractible or a wedge of circles, and separately treats \(4\)-regular circulant graphs. This includes a coarse statement applicable to the Fano incidence graph, but it neither gives the design-wide formula above nor covers general Steiner incidence graphs, whose degrees need not be bounded by \(3\).

A closely related indexed result for finite projective planes computes a scale-two Vietoris–Rips complex as a wedge of \(q^3\) two-spheres. That is a different simplicial complex: a Vietoris–Rips simplex is defined by pairwise metric distance, whereas a neighborhood simplex is defined by a common graph neighbor. The matching multiplicity \(q^3\) does not provide an implication between the two statements.

## Limitations
The originality check cannot rule out every unindexed design-theory or hypergraph-topology source. In particular, an older general lemma about clique unions of a linear hypergraph could subsume the relative-collapse step under different terminology. The checked sources and searches did not locate such a statement specialized to neighborhood complexes of Steiner-design incidence graphs. The theorem is nonequivariant: no claim is made that the collapses respect automorphism groups of the design.

## References
D. N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1, first submitted 2005-03-28; *Topology and its Applications* 153 (2006), 2445–2454. DOI: 10.1016/j.topol.2005.09.005.

S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1; *Electronic Journal of Combinatorics* 26(2) (2019), #P2.4. DOI: 10.37236/7549.
