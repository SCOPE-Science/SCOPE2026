# Rank-four reconstruction and sharp modularity for tree-neighborhood concept lattices

## Finding

**Theorem (closed-neighborhood concept lattices of finite trees).** Let \(T=(V,E)\) be a finite simple tree with \(n=|V|\ge3\). Form the two-sorted formal context \((V,V,I)\) with distinct object and attribute copies of \(V\), where \(uIv\) means \(u=v\) or \(uv\in E\). Let \(\mathcal L(T)\) be its concept lattice, ordered by inclusion of extents. Write \(I_T=\{v\in V:\deg_T(v)\ge2\}\) and \(i=|I_T|\).

If \(T\) is the star \(K_{1,n-1}\) with center \(c\), then its distinct extents are exactly
\[
\mathcal L(T)=\{\{c\},V\}\ \cup\ \{\{c,\ell\}:\ell\in V\setminus\{c\}\}.
\]
It is the height-two lattice with \(n-1\) atoms, has \(n+1\) elements, and has rank polynomial \(1+(n-1)t+t^2\).

If \(T\) is not a star, then its distinct extents are exactly the disjoint union
\[
\boxed{\quad
\{\varnothing,V\}
\ \dot\cup\ \{\{v\}:v\in I_T\}
\ \dot\cup\ \{\{u,v\}:uv\in E\}
\ \dot\cup\ \{N_T[v]:v\in I_T\}.\quad}
\]
Here \(N_T[v]=\{v\}\cup\{w:vw\in E\}\). The lattice is graded of length four: these five displayed classes occur in successive ranks \(0,1,2,3,4\). Consequently
\[
\boxed{|\mathcal L(T)|=n+2i+1,\qquad
R_{\mathcal L(T)}(t)=1+it+(n-1)t^2+it^3+t^4.}
\]

For **every** tree with \(n\ge3\), the abstract order of \(\mathcal L(T)\), without vertex labels or recorded incidence, reconstructs \(T\) up to graph isomorphism. In particular, for such trees \(T\) and \(T'\),
\[
\boxed{\mathcal L(T)\cong\mathcal L(T')\ \Longleftrightarrow\ T\cong T',\qquad
\operatorname{Aut}(\mathcal L(T))\cong\operatorname{Aut}(T).}
\]
The reconstruction is explicit: for a nonstar tree, rank-one elements are its nonleaf vertices; rank-two elements are its edges, with exactly one or two rank-one predecessors specifying the nonleaf endpoints, and a new leaf is supplied for each rank-two element with only one predecessor. The height-two case reconstructs the star from its number of atoms.

Finally, the **sharp modularity and distributivity boundaries** are
\[
\boxed{\mathcal L(T)\text{ is modular}\ \Longleftrightarrow\ \operatorname{diam}(T)\le3,}
\]
and
\[
\boxed{\mathcal L(T)\text{ is distributive}\ \Longleftrightarrow\ T\cong P_3\text{ or }T\cong P_4.}
\]
The last two formulas hold under the stated assumption \(n\ge3\); the excluded two-vertex context has only a single concept.

## Assumptions and scope

The relation is **reflexive, undirected closed-neighborhood incidence**, not ordinary graph edge incidence, not the open-neighborhood context, and not the rough-set lower/upper approximation map. Its two copies of \(V\) are separate sorts despite sharing labels. For \(A\subseteq V\), let \(A'=\{v\in V:\forall u\in A,\ uIv\}\); the formal concepts are \((A,A')\) with \(A=A''\). By the Galois correspondence, the distinct concept extents are the intersections \(\bigcap_{v\in S}N_T[v]\) over all \(S\subseteq V\), where the empty intersection is \(V\).

A star includes the three-vertex path \(P_3\) but excludes the two-vertex complete graph. The rank polynomial counts concepts by order-theoretic rank, not by extent cardinality. The automorphism group consists of order-preserving lattice automorphisms, not order-reversing symmetries.

## Proof

**1. Intersections of neighborhoods.** For distinct vertices \(u,v\) of a tree, the lack of triangles and unique paths give
\[
N_T[u]\cap N_T[v]=
\begin{cases}
\{u,v\},&d_T(u,v)=1,\\
\{w\},&d_T(u,v)=2\text{ with unique middle vertex }w,\\
\varnothing,&d_T(u,v)\ge3.
\end{cases}
\]
Intersections of three or more neighborhoods cannot introduce a new type beyond the displayed singleton, edge, or empty set. No singleton leaf can occur: the only closed neighborhoods containing a leaf \(\ell\) are those centered at \(\ell\) and its unique neighbor \(p\); their intersection still contains \(p\). A singleton internal vertex \(\{v\}\), conversely, occurs by intersecting the closed neighborhoods of two distinct neighbors of \(v\). Every edge endpoint pair \(\{u,v\}\) occurs as \(N_T[u]\cap N_T[v]\). A nonstar tree has diameter at least three, so two distant closed neighborhoods have empty intersection. These facts prove that every listed set occurs and that there are no others. For a star, all neighborhoods contain the center, while pairwise intersections of distinct leaf neighborhoods equal its singleton; this gives the stated height-two lattice.

**2. Distinct ranks and exact counting.** A nonstar tree has no universal vertex. Its internal neighborhoods \(N_T[v]\) are proper subsets of \(V\), all have size at least three, and are pairwise distinct: if two different internal vertices \(u,v\) had the same closed neighborhood, their adjacency would force a triangle or the two-vertex tree. None of these neighborhoods contains another internal neighborhood, because an internal neighbor has another neighbor at distance two from the first center. Every internal neighborhood properly contains at least two incident edge endpoint pairs, while each edge endpoint pair properly contains exactly one or two internal singletons. Hence the four nontrivial displayed classes are precisely ranks \(1,2,3\) between the empty and full extents. A tree has \(n-1\) edges. Counting the disjoint classes gives \(2+i+(n-1)+i=n+2i+1\) and the stated rank polynomial. The star case is immediate from its listed extents.

**3. Intrinsic reconstruction and automorphisms.** In the nonstar case, let the recovered internal vertices be the rank-one elements and the recovered edges be the rank-two elements of the **abstract** lattice. Each edge element has one or two rank-one elements below it. If two, join the corresponding vertices. If one, attach a fresh leaf to that vertex. Step 2 proves there are no additional edge elements and that this reproduces exactly the original tree. If the lattice has length two instead, the original tree is a star and its number of leaves equals the number of atoms. The construction is functorial under order isomorphisms. Conversely, a graph automorphism preserves all closed-neighborhood intersections and therefore induces a lattice automorphism. No extra lattice automorphism occurs: rank-zero through rank-two elements are fixed by the recovered graph action; each internal neighborhood is the join of its incident rank-two edge elements, while the top and bottom are intrinsic. The same statement is immediate for stars. Thus the two automorphism groups are naturally isomorphic, and lattice isomorphism is equivalent to tree isomorphism.

**4. Failure of modularity at diameter at least four.** A diameter path of length at least four has three consecutive nonleaf vertices \(u,v,w\). Put \(x=\{u\}\), \(y=\{w\}\), and \(z=\{u,v\}\) in the extent lattice. Since the sole closed neighborhood containing both \(u\) and \(w\) is \(N_T[v]\), one has \(x\vee y=N_T[v]\). Also \(x\le z\), \(y\wedge z=\varnothing\), and \((x\vee y)\wedge z=z\). The modular identity gives incompatible sides \(x\) and \(z\), so the lattice is not modular.

**5. Modularity at diameter at most three.** A star yields a height-two lattice, which is modular. Every nonstar tree of diameter three is a *double star*: two adjacent nonleaf vertices \(u,v\), with nonempty leaf families \(a_1,\ldots,a_k\) at \(u\) and \(b_1,\ldots,b_\ell\) at \(v\). Choose distinct rational numbers \(t_1,\ldots,t_k\) and \(s_1,\ldots,s_\ell\). Let \(W\) be four-dimensional over \(\mathbb Q\), with basis vectors \(e_u,e_v,e_a,e_b\). Embed the extents as the following subspaces:
\[
\begin{aligned}
\varnothing&\mapsto0,&V&\mapsto W,\\
\{u\}&\mapsto\langle e_u\rangle,&\{v\}&\mapsto\langle e_v\rangle,\\
\{u,v\}&\mapsto\langle e_u,e_v\rangle,\\
\{u,a_i\}&\mapsto\langle e_u,e_a+t_i e_v\rangle,\\
\{v,b_j\}&\mapsto\langle e_v,e_b+s_j e_u\rangle,\\
N_T[u]&\mapsto\langle e_u,e_v,e_a\rangle,&
N_T[v]&\mapsto\langle e_u,e_v,e_b\rangle.
\end{aligned}
\]
Distinct parameters make distinct lines through the same rank-one point; their pairwise joins are the appropriate three-dimensional subspace. A line from the \(u\)-leaf family and a line from the \(v\)-leaf family have zero intersection and span all of \(W\). The remaining intersections and spans follow directly from the basis. Thus this set of subspaces is closed under intersection and vector-space sum, and its inclusion order is the specified concept lattice. A sublattice of a modular subspace lattice is modular. This proves the opposite implication.

**6. Distributivity boundary.** For \(P_3\) the lattice is the four-element Boolean lattice; for \(P_4\) its nine extents form the product of two three-element chains (the two atoms lie at \((1,0)\) and \((0,1)\), the three rank-two elements at \((2,0),(1,1),(0,2)\)). Stars with at least three leaves have three incomparable atoms and therefore contain the nondistributive diamond \(M_3\). A diameter-three double star other than \(P_4\) has at least two leaves at one internal vertex, say \(u\); the interval from \(\{u\}\) to \(N_T[u]\) contains the internal-edge concept and at least two leaf-edge concepts as incomparable middle elements, again yielding \(M_3\). Finally, diameter at least four is already nonmodular by Step 4, hence nondistributive. This exhausts all trees with \(n\ge3\).

## Verification

The accompanying `VERIFY.py` uses only the Python standard library and independently enumerates all Prüfer-coded labeled trees of orders three through seven. For each, it computes the Galois-closed extents by repeated bitmask intersection without assuming the theorem's normal form; checks the predicted extent family, counts and ranks; and recovers the original edges from the first two abstract ranks. It additionally computes all meets and joins and evaluates the modular and distributive laws on every labeled tree through order six and on a deterministic subset of order-seven trees. The executed result was:

```text
SIZE 3 labeled_trees 3 normal_form_reconstruction=PASS
SIZE 4 labeled_trees 16 normal_form_reconstruction=PASS
SIZE 5 labeled_trees 125 normal_form_reconstruction=PASS
SIZE 6 labeled_trees 1296 normal_form_reconstruction=PASS
SIZE 7 labeled_trees 16807 normal_form_reconstruction=PASS
VERIFY_OK labeled_trees 18247 modularity_distributivity_cases 1895 normal_form=PASS ranks=PASS reconstruction=PASS modularity=PASS distributivity=PASS
```

These finite computations are corroboration, not proof of the arbitrary-order theorem; all infinite-family assertions follow from Steps 1–6.

## Relationship to prior work

Rawson, Myers, Green, Robinson and Joslyn give the general concept-lattice/intersection-complex correspondence for hypergraphs [1, Theorem 3.1]. The use of neighborhood intersections as a concept-lattice representation is therefore established; it is not a new part of the claim. The result above instead specializes that framework to **every finite tree**, identifies all ranks and their exact numbers, and derives a diameter-three modularity threshold plus a rank-two unlabeled reconstruction algorithm.

General reduced-context results in formal concept analysis [2] also explain why a context may retain incidence information through its concept lattice; the explicit reconstruction here should not be mistaken for a claim that all reconstruction principles are new. The tree-specific rank description and sharp lattice-identity boundary are the main assertions requiring comparison. Apollonio, Caramia and Franciosa [3] analyze Galois lattices of bipartite distance-hereditary graphs, with a different structural characterization; their results do not state this closed-neighborhood rank-four tree theorem. Koh and Poh's graph *closed-set lattice* literature [4,5] uses the closure rule \(a,b\in S\Rightarrow N(a)\cap N(b)\subseteq S\), not intersections of reflexive closed neighborhoods; it is a different object. Path examples are specializations of the present theorem and are not asserted to be separately novel.

## Limitations

The result is limited to undirected finite trees with at least three vertices, a **reflexive** relation, and the two-sorted formal-concept Galois construction. It does not imply the same normal form for general forests, cycles, graph powers, open-neighborhood contexts, or rough-set approximation lattices. The two-vertex context is exceptional and excluded. The automorphism statement concerns order-preserving symmetries only.

The literature comparison does not establish publication priority: equivalent tree-specific results under neighborhood-hypergraph, concept-context reduction, or Galois-lattice terminology may exist. In particular, [4] was available primarily through its published abstract and a reliable mathematical review of the definitions [5], not through a complete inspected original paper. This residual access limit does not alter the elementary mathematical proof, but constrains the originality assessment.

## References

[1] M. G. Rawson, A. Myers, R. Green, M. Robinson, C. Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681, first submitted 2023-07-21, Theorem 3.1 and Sections 2–4. https://arxiv.org/abs/2307.11681

[2] B. Ganter, R. Wille, *Formal Concept Analysis: Mathematical Foundations*, Springer, 1999.

[3] N. Apollonio, M. Caramia, P. G. Franciosa, *On the Galois Lattice of Bipartite Distance Hereditary Graphs*, arXiv:1406.0154, 2014, especially Theorem 1 and Sections 2–4. https://arxiv.org/abs/1406.0154

[4] K. M. Koh, K. S. Poh, *On an isomorphism problem on the closed-set lattice of a graph*, Order 1 (1985), 285–294. https://doi.org/10.1007/BF00383605

[5] K. M. Koh, K. S. Poh, *On the lower length of the closed-set lattice of a tree*, Discrete Mathematics (1996). https://doi.org/10.1016/0012-365X(94)00090-6

[6] T. Hanika, J. Hirth, *Knowledge cores in large formal contexts*, Annals of Mathematics and Artificial Intelligence 90 (2022), 537–567. https://doi.org/10.1007/s10472-022-09790-6
