# A bipartite product-digraph threshold for full power semirings

## Finding
Let \(S\) be a finite semigroup with zero \(0\), satisfying \(S^3=\{0\}\) and \(S^2\ne\{0\}\). Form the directed graph \(D_S\) on \(S\setminus\{0\}\) by putting an arc \(u\to v\) exactly when \(uv\ne0\). Assume that its vertices admit a two-colouring under which every arc joins opposite colours. The graph may have isolated vertices and may contain both orientations of an undirected edge.

For the full power semiring \(\mathcal P(S)\), including the empty set, with union as addition and setwise multiplication, in the constant-free binary signature, the following dichotomy holds:

\[
\mathcal P(S)\text{ is finitely based}\quad\Longleftrightarrow\quad
\nexists u,v,w\in S\setminus\{0\}:uv\ne0\text{ and }vw\ne0.
\]

In the finitely based case, a finite identity basis relative to the usual additively idempotent semiring identities uses at most four variables, and the induced-substructure obstruction bound of the nonzero-product relational structure is exactly three. In the other case no bounded-variable identity family generates its equational theory.

The bipartiteness assumption is essential already for semigroups with five elements. On \(\{0,z,a,b,c\}\), define all unlisted products to be zero. With \(ab=bc=z\), the full power semiring is nonfinitely based; adding only \(ac=z\) makes it finitely based with a four-variable relative basis. Both semigroups have nilpotency index three, every square zero, and no pair of mutually nonzero reverse products.

## Assumptions and scope
A semigroup has nilpotency index three here if every product of three elements is zero and at least one product of two elements is nonzero. Associativity is assumed. An arc's endpoints need not be distinct in the general graph construction, but the stated two-colouring hypothesis prohibits loops. A directed two-walk may repeat its first vertex, so a directed two-cycle counts. The full power semiring includes the empty subset. "Finitely based" refers to its ordinary equational theory in the two-operation, constant-free signature; a relative basis presupposes the standard finite additively idempotent semiring axioms.

Write \(b(D)\) for the least bound such that every finite directed graph not admitting a homomorphism to \(D\) contains an induced subgraph on at most \(b(D)\) vertices that also does not admit a homomorphism. Unary relations that include all vertices do not affect these homomorphism statements.

## Proof
**Reduction to directed graphs.** Theorem 1.1 of Wang–Yin–Wang gives, for a finite index-three nilpotent semigroup, finite basability of \(\mathcal P(S)\) precisely when the relational structure of its nonzero products has finite homomorphism duality. That structure has the universal unary relation and the binary arc relation of \(D_S\). Hence finite duality of the structure is equivalent to finite duality of the directed graph. The same paper's Theorem 4.1 gives a relative basis using at most \(\max\{4,b(D_S)\}\) variables whenever \(b(D_S)\) is finite.

**No directed two-walk.** Choose any arc \(p\to q\) of \(D_S\), which exists because \(S^2\ne\{0\}\). If a finite directed graph \(H\) has no directed two-walk, no vertex of \(H\) has both an incoming and an outgoing arc. Map vertices with outgoing arcs to \(p\), vertices with incoming arcs to \(q\), and isolated vertices to \(p\). This is a homomorphism \(H\to D_S\). Conversely, a homomorphism \(H\to D_S\) cannot exist when \(H\) contains a directed two-walk, because \(D_S\) has none. Consequently a single directed path of two arcs is a complete obstruction. Its three-vertex instance has every proper induced subgraph mapping to \(D_S\), so \(b(D_S)=3\). The variable bound is thus four.

**A directed two-walk in a bipartite target.** If \(D_S\) has arcs \(p\to q\to r\), the directed two-arc path \(P\) maps to \(D_S\). For every odd \(N=2m+1\ge3\), construct a directed graph \(H_N\) on \(0,1,\ldots,2m\). On the consecutive edges of the path \(0-1-\cdots-2m\), direct each edge from its even endpoint to its odd endpoint. Add the closing arc \(2m\to0\). The underlying undirected graph is an odd cycle. Its orientation has exactly one directed two-walk, \(2m\to0\to1\), and no longer directed walk.

No \(H_N\) maps to \(D_S\): a graph homomorphism into a two-colourable graph would induce a two-colouring of the underlying odd cycle. After deleting any vertex of \(H_N\), the remaining oriented graph is a single path. If the special two-walk is destroyed, each vertex is a source, a sink, or isolated, and maps to the endpoints of \(P\) as in the preceding paragraph. Otherwise, map the special walk to \(0\to1\to2\) in \(P\); along its two remaining tails the arc orientations alternate. Label consecutive tail vertices alternately \(0,1\) on the entering tail and \(1,2\) on the exiting tail, preserving every arc. Thus every vertex-deleted induced subgraph maps to \(P\), and hence to \(D_S\). Every smaller induced subgraph also maps. Taking \(N\) arbitrarily large rules out any finite induced-obstruction bound and therefore finite duality. Theorem 1.1 yields nonfinite basability and excludes any bounded-variable identity basis. The same obstruction gives the explicit valid absorption identities

\[
\prod_{i=0}^{2m}x_i\preceq\sum_{(i,j)\in E(H_{2m+1})}x_ix_j\qquad(m\ge1),
\]

where \(u\preceq v\) means \(u+v\approx v\). Indeed a nonempty left-hand product is zero, while, if every displayed right-hand product avoided zero, selecting one nonzero member of each assigned subset would give a forbidden graph homomorphism \(H_{2m+1}\to D_S\). The theorem on unbounded-variable obstructions, not just validity of this family, establishes nonfinite basability.

**A one-product boundary pair.** Let \(S_- =\{0,z,a,b,c\}\) with nonzero products exactly \(ab=bc=z\). Let \(S_+\) have the same elements and additionally \(ac=z\). Every product of length two lies in \(\{0,z\}\), both of whose elements annihilate everything on either side; thus both multiplications are associative and all triple products vanish. Both have nonzero double products, zero squares, and no reverse-positive pair. Their arc relations are, respectively, the directed two-arc path and the transitive three-vertex tournament, together with the isolated vertex \(z\).

For \(S_-\), the bipartite directed two-walk case above applies. For \(S_+\), a finite directed graph \(H\) maps to the transitive three-vertex tournament if and only if it contains no directed walk of length three: a homomorphism necessarily strictly increases the target level at each arc, and, conversely, in the absence of such a walk the maximum length of a directed walk ending at each vertex gives a level \(0,1,\) or \(2\), strictly increasing across every arc. Therefore a directed three-arc path is a single complete obstruction, its four-vertex instance is critical, and \(b(D_{S_+})=4\). The published nilpotent classification and variable bound give a four-variable relative basis for \(\mathcal P(S_+)\).

Finally, \(S_-\) is minimal among nilpotent index-three examples whose nonzero-product graph has neither loops nor opposite arc pairs but contains a two-walk. Such a walk must have three distinct vertices; the nonzero product of its first arc lies in the two-sided annihilator \(S^2\) and so is distinct from the three vertices, each of which participates in an arc. Together with zero these require at least five elements.

## Verification
The standalone `verify.py` checker independently verifies associativity of both five-element multiplication tables. For every nonempty, loopless, underlying-bipartite directed target on two or three labelled vertices, it confirms on all directed inputs of up to three vertices (loops allowed in inputs) the homomorphism equivalence in the no-two-walk branch. It checks the odd-cycle obstruction and all single-vertex deletions for cycle lengths three, five, seven, and nine. It separately checks the transitive-tournament homomorphism criterion on all directed inputs of up to three vertices, plus the four-vertex critical obstruction. Its observed output is `VERIFY_OK bipartite finite targets: [14, 25] odd obstructions tested through size 9`, with the two entries counting target digraphs without and with a directed two-walk. This enumeration supports, but does not establish, the all-size statements proved above.

## Relationship to prior work
Wang, Yin and Wang (2026), arXiv:2610.01329, Theorem 1.1 establishes the full-power-semiring/finite-duality correspondence for arbitrary finite nilpotent semigroups; Theorem 4.1 supplies the variable bound. Example 4.4 treats one directed arc, and Example 4.5 treats a two-way arc. Neither states the bipartite-support if-and-only-if criterion, the general three-vertex obstruction bound, or the one-product boundary pair. The present finding relies on their general theorem and contributes the explicit graph-homomorphism classification and boundary constructions, not a replacement proof of that theorem.

Larose, Loten and Tardif (2007), arXiv:0707.2562, develop finite duality and the corresponding constraint-satisfaction characterization. Their introduction discusses the transitive tournament and directed paths; this earlier work provides the graph-theoretic context for the boundary. The directed-odd-cycle witness and the semiring classification for the stated bipartite product graphs are made explicit here. They are not claims of a new general finite-duality theory.

## Limitations
The finite-basis classification is restricted to finite nilpotent semigroups of index exactly three whose nonzero-product digraph is bipartite. It does not claim a classification for arbitrary directed product relations, higher nilpotency index, or nonnilpotent semigroups. Four is a proven upper bound on the number of variables in a relative basis, not a claim that four are always necessary. Finite tests are not a substitute for the universal proof. The foundational nilpotent equivalence and variable-bound theorems are used as published results. An implicit prior presentation of the precise bipartite graph criterion remains a bibliographic risk.

## References
1. Lili Wang, Qingrui Yin, and Aifa Wang, *Finite bases for full power semirings of finite nilpotent semigroups*, arXiv:2610.01329, first posted 2026-10-01, especially Theorems 1.1 and 4.1, Examples 4.4–4.5 and Section 7. https://arxiv.org/abs/2610.01329
2. Benoit Larose, Cynthia Loten, and Claude Tardif, *A Characterisation of First-Order Constraint Satisfaction Problems*, Logical Methods in Computer Science 3(4:6) (2007), arXiv:0707.2562, especially introduction and Section 2. https://arxiv.org/abs/0707.2562
