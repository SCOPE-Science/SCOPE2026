# Unique worst-case rough-set ambiguity on every tree, with an edge-cover polynomial certificate

## Finding

**Theorem (a coefficientwise fiber bound and exact maximum ambiguity).** Let \(T=(V,E)\) be any finite undirected simple tree with \(n=|V|\ge 2\). Give \(V\) the reflexive, symmetric neighborhood relation \(vRw\) exactly when \(v=w\) or \(vw\in E\). For \(X\subseteq V\), define
\[
L(X)=\{v\in V:N_T[v]\subseteq X\},\qquad
U(X)=\{v\in V:N_T[v]\cap X\ne\varnothing\},
\qquad\rho(X)=(L(X),U(X)).
\]
Write \(\delta(X)\) for the set of edges with exactly one endpoint in \(X\). The edge-cover polynomial of the tree is
\[
E_T(z)=\sum_{\substack{F\subseteq E\\\forall v\in V:\ \deg_F(v)\ge1}}z^{|F|}.
\]
For any **realized** rough approximation \(Q\), define its cut-refined inverse-fiber polynomial by
\[
A_Q(z)=\sum_{\substack{X\subseteq V\\\rho(X)=Q}}z^{|\delta(X)|}.
\]
Then the completely uncertain approximation \(Q_*=(\varnothing,V)\) is realized and
\[
\boxed{A_{Q_*}(z)=2E_T(z).}
\]
Moreover, for every other realized \(Q=(L,U)\), write \(S=U\setminus L\) and
\[
h_Q=|E\setminus E(T[S])|\ge1.
\]
There is a degree-shifting injection from the inverse fiber of \(Q\) into edge covers of \(T\), giving the **coefficientwise** inequality
\[
\boxed{z^{h_Q}A_Q(z)\preceq E_T(z).}
\]
Consequently \(Q_*\) is the **unique** maximizer of the inverse-fiber size, with a factor-of-two gap to every other fiber:
\[
\boxed{\max_{Q\in\rho(2^V)}|\rho^{-1}(Q)|=2E_T(1),\qquad
Q\ne Q_*\Longrightarrow |\rho^{-1}(Q)|\le E_T(1).}
\]
For uniformly chosen \(X\subseteq V\), the output's order-\(\infty\) Rényi entropy is exactly
\[
\boxed{H_{\infty}(\rho(X))=n-1-\log_2 E_T(1).}
\]
Finally, \(E_T(1)\) is computable using a two-state bottom-up tree recurrence with \(O(n)\) arithmetic operations (large integers are allowed).

## Assumptions and scope

All trees are finite, simple, connected, and have at least two vertices, so every vertex has a neighbor. The relation is precisely *reflexive adjacency*; neither transitive closure nor a relation on graph edges is being used. Both approximation operators are computed using this same relation, without replacing either one by a complementary, inverse, or covering-based operator. A rough approximation \(Q=(L,U)\) is *realized* when at least one \(X\) satisfies \(\rho(X)=Q\). Polynomial comparison \(P(z)\preceq Q(z)\) means that each coefficient of \(P\) is at most the corresponding coefficient of \(Q\). The output information measure assumes a uniformly random vertex subset \(X\).

## Proof

**1. Mixed vertices are exactly cut endpoints.** Represent \(X\) by a binary coloring of \(V\). Since each closed neighborhood contains its center, a vertex \(v\) belongs to \(U(X)\setminus L(X)\) if and only if the colors appearing on \(N_T[v]\) are not constant. This is equivalent to \(v\) having some neighbor colored opposite to itself, i.e. to being incident to an edge in \(\delta(X)\). Hence
\[
U(X)\setminus L(X)=\{v:\deg_{\delta(X)}(v)>0\}.
\tag{1}
\]
If \(v\notin U(X)\setminus L(X)\), then \(N_T[v]\) is monochromatic. In particular, the approximation \(Q\) determines the color of \(v\): it is one when \(v\in L\) and zero when \(v\notin U\). Since \(L\subseteq U\), these two alternatives are exhaustive for \(v\notin S\).

**2. Every tree edge subset is the cut of exactly two colorings.** Choose a root vertex and prescribe its binary color. For an arbitrary \(F\subseteq E\), propagate the color along each edge, flipping precisely across edges of \(F\). The unique-path property of a tree makes the propagation globally consistent. The two root-color choices produce distinct complementary colorings and all colorings with cut \(F\). Consequently, the map \(X\mapsto\delta(X)\) is exactly two-to-one onto \(2^E\).

Combining this property with (1), the condition \(\rho(X)=(\varnothing,V)\) means exactly that every vertex is incident to at least one cut edge, i.e. \(\delta(X)\) is an edge cover. This proves \(A_{Q_*}(z)=2E_T(z)\). Since the full edge set covers every vertex, this central approximation is realized.

**3. Inject all other fibers into edge covers, preserving cut size up to a fixed shift.** Let \(Q=(L,U)\ne Q_*\) be realized and write \(S=U\setminus L\). Then \(S\subsetneq V\) (as \(S=V\) forces \(L=\varnothing\) and \(U=V\)). Fix any \(X\) with \(\rho(X)=Q\) and put \(F=\delta(X)\). By (1), the endpoint set of \(F\) is exactly \(S\), so \(F\subseteq E(T[S])\) and every vertex of \(S\) is covered by \(F\).

Define the fixed complement of the induced edge set by
\[
D_S=E\setminus E(T[S]),\qquad h_Q=|D_S|.
\]
Because \(T\) is connected, \(n\ge2\), and \(S\subsetneq V\), we have \(h_Q\ge1\). Every vertex outside \(S\) is incident to an edge in \(D_S\). Therefore
\[
\Psi_Q(X)=\delta(X)\cup D_S
\]
is an edge cover of \(T\), of size exactly \(|\delta(X)|+h_Q\). Moreover, \(\Psi_Q\) is injective **on the fiber**: equality of outputs implies equality of cuts, hence the two colorings are equal or complementary by Step 2. But \(V\setminus S\) is nonempty, and the fixed approximation \(Q\) prescribes the color of each vertex there, so two complementary colorings cannot both belong to the fiber. Thus \(\Psi_Q\) is a degree-shifting injection, proving the polynomial inequality.

Evaluating at \(z=1\) gives \(|\rho^{-1}(Q)|\le E_T(1)\). The central fiber has size \(2E_T(1)>E_T(1)\), proving **strict uniqueness**. Since \(X\) is uniform on \(2^V\), the largest output probability is \(2E_T(1)/2^n\); taking its negative base-two logarithm gives the entropy formula.

**4. Exact linear-arithmetic dynamic program.** Root \(T\) at any vertex \(r\). For each rooted subtree at \(v\), let \(a_v\) be the number of selected subsets of edges below \(v\) that cover every vertex in that subtree when the parent edge is **absent**, and \(b_v\) the number when the parent edge is **present** (the parent edge itself is not included in the count, but already covers \(v\)). For a leaf, \(a_v=0\), \(b_v=1\). For each internal vertex, independently choose whether each child edge is selected:
\[
\boxed{b_v=\prod_{u\text{ child of }v}(a_u+b_u),\qquad
 a_v=b_v-\prod_{u\text{ child of }v}a_u.}
\]
The subtracted term consists exactly of choices in which no child edge is selected, leaving \(v\) uncovered when the parent edge is absent. The root has no parent edge, so \(E_T(1)=a_r\). Each edge participates in a constant number of operations. This proves the computational assertion without treating numerical experiments as a proof.

## Verification

The accompanying standalone Python 3 program `verify.py` uses the standard library and integer arithmetic. It directly enumerates all \(18{,}248\) labeled trees on \(2\) through \(7\) vertices via Prüfer codes, all their vertex subsets and actual lower/upper neighborhoods, and all edge-cover subsets. It independently checks the equality \(A_{Q_*}(z)=2E_T(z)\), the coefficientwise injection bound for every realized noncentral fiber, the unique largest-fiber assertion, and the rooted dynamic-program count. It additionally checks \(600\) seeded larger trees on \(8\) through \(11\) vertices. The successful marker is `VERIFY_OK` and includes `individual_rough_fibers=1462212`. These checks are finite corroboration; the four-part proof above establishes all tree orders.

## Relationship to prior work

Järvinen and Radeleczki (2023) study algebraic rough-set systems determined by reflexive relations, including tolerance relations, and supply the relevant operator setting. Their conclusions concern order structure and lattice properties, not the cut-size-refined inverse-fiber comparison proved here. Their earlier treatment of rough sets determined by tolerances supplies broader background.

Csikvári (2013) studied the edge-cover polynomial and path/star extremality for trees; edge covers and their preexisting enumerative properties are **not** claimed as new here. Wang and coauthors (2013) connect graph edge covers with reducts of *covering-based* rough sets, a different construction from the simultaneous lower/upper closed-neighborhood observation studied here. The assertion that paths have a Fibonacci edge-cover count is an immediate specialization of known edge-cover enumeration, not a separate novelty claim. The claimed addition is the all-tree *coefficientwise injection for every realized rough observation*, the strict global fiber comparison, and the corresponding exact observation min-entropy.

## Limitations

No analogous equality with **all** edge covers is asserted for graphs with cycles: a general edge subset need not be a valid cut, so Step 2 uses essential tree acyclicity. The polynomial inequality counts fibers by crossing-edge number, not by input cardinality. The complexity statement counts arithmetic operations, not bit complexity, since the integers may grow exponentially. The result does not enumerate all distinct rough observations or claim any new path/star extremality of the edge-cover polynomial. Literature overlap under alternate terminology such as ambiguity classes, weak two-colorings, or covering systems remains possible; priority has not been independently certified.

## References

1. J. Järvinen and S. Radeleczki, *Pseudo-Kleene algebras determined by rough sets*, first public arXiv posting 12 April 2023, [arXiv:2304.05641](https://arxiv.org/abs/2304.05641).
2. J. Järvinen and S. Radeleczki, *Rough sets determined by tolerances*, 2013, [arXiv:1303.6332](https://arxiv.org/abs/1303.6332).
3. P. Csikvári, *On a Poset of Trees II*, Journal of Graph Theory 74 (2013), 81–103, [doi:10.1002/jgt.21693](https://doi.org/10.1002/jgt.21693).
4. *Equivalent Characterizations of Some Graph Problems by Covering-Based Rough Sets*, Journal of Applied Mathematics (2013), [doi:10.1155/2013/519173](https://doi.org/10.1155/2013/519173).
