# The rough-set lattice of a complete multipartite tolerance: normal form, symmetries, and reconstruction

## Finding

**Theorem.** Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite simple graph on \(V=P_1\sqcup\cdots\sqcup P_r\), where \(r\ge2\), all \(n_i=|P_i|\ge1\), and \(N=|V|\). Form the reflexive symmetric relation \(R=\Delta_V\cup E(G)\). For every \(X\subseteq V\), put
\[
L(X)=\{v\in V:R(v)\subseteq X\},\qquad
U(X)=\{v\in V:R(v)\cap X\ne\varnothing\},
\]
and order \(\mathcal R(G)=\{(L(X),U(X)):X\subseteq V\}\) by inclusion in both coordinates.

Let \(\mathcal B_m\) be the Boolean lattice on an \(m\)-element set; let \(H\) be the horizontal sum of \(\mathcal B_{n_i}\) over exactly those parts with \(n_i\ge2\) (identifying all bottoms and all tops, with no other cross-factor comparisons). If there are no such parts, define \(H=\mathcal B_1\). Then
\[
\boxed{\mathcal R(G)\cong H\oplus H,\qquad
|\mathcal R(G)|=3+2\sum_{i=1}^{r}(2^{n_i}-2).}
\]
Here \(H\oplus H\) denotes the *vertical* or ordinal sum formed by identifying the top of the first copy with the bottom of the second copy.

Write \(a=|\{i:n_i=2\}|\), \(b_m=|\{i:n_i=m\}|\) for \(m\ge3\), and \(q=|\{i:n_i\ge2\}|\). The full order-preserving automorphism group is
\[
\boxed{\operatorname{Aut}(\mathcal R(G))\cong
\left(\mathfrak S_{2a}\times\prod_{m\ge3}(\mathfrak S_m\wr\mathfrak S_{b_m})\right)^2,}
\]
where factors with zero multiplicity are trivial. In particular, its order is
\[
\boxed{\left((2a)!\prod_{m\ge3}(m!)^{b_m}b_m!\right)^2.}
\]
The lattice is distributive exactly when \(q\le1\), and modular exactly when \(q\le1\) or every \(n_i\le2\). Two such rough-set lattices are isomorphic if and only if the multisets \(\{n_i:n_i\ge2\}\), with multiplicities, agree. Thus singleton parts are invisible to the abstract rough-set lattice, but supplying \(N\) recovers the complete multipartite graph up to isomorphism.

## Assumptions and scope

There are at least two nonempty graph parts. Adjacency excludes loops in the graph, but **the approximation relation includes all loops**. All the conclusions concern the same single tolerance \(R\) in both lower and upper approximations, not a mixed pair of approximation relations. The poset \(\mathcal R(G)\) uses coordinatewise inclusion, not an external completion. A horizontal sum of one Boolean factor means the factor itself; the no-factor convention was specified above.

## Proof

**1. Complete description of approximation pairs.** For \(v\in P_i\), the reflexive neighborhood is
\[
R(v)=(V\setminus P_i)\cup\{v\}.
\]
If \(X=\varnothing\), the pair is \((\varnothing,\varnothing)\). If \(X\) meets just one part \(P_i\), with \(\varnothing\ne X\subseteq P_i\), then \(L(X)=\varnothing\) and \(U(X)=(V\setminus P_i)\cup X\). If \(X\) meets at least two parts, then \(U(X)=V\). In this latter case, \(L(X)=V\) exactly when \(X=V\); \(L(X)=A\) for some nonempty proper \(A\subsetneq P_i\) exactly when \(X=(V\setminus P_i)\cup A\); otherwise \(L(X)=\varnothing\). In particular, \(X=P_i\) realizes the central pair \((\varnothing,V)\) for any \(i\).

Therefore the complete, nonredundant list of approximation pairs consists of three distinguished points
\[
(\varnothing,\varnothing),\quad (\varnothing,V),\quad (V,V),
\]
and, for every \(i\) and nonempty proper \(A\subsetneq P_i\), precisely the two pairs
\[
\left(\varnothing,(V\setminus P_i)\cup A\right)
\quad\text{and}\quad (A,V).
\]
No other pairs occur; every listed pair is realized by an explicit \(X\) above. Consequently the total is \(3+2\sum_i(2^{n_i}-2)\).

**2. Exact lattice order.** All the first-family proper pairs lie strictly between \((\varnothing,\varnothing)\) and \((\varnothing,V)\); for fixed \(i\), they have precisely the inclusion order of nonempty proper subsets of \(P_i\). Pairs from different parts are incomparable because their upper coordinates omit nonempty subsets of disjoint parts. Consequently this lower interval is the horizontal sum \(H\). Dually, the second-family proper pairs form another copy of \(H\) between \((\varnothing,V)\) and \((V,V)\). Every lower-half element is below every upper-half element. Thus the poset is \(H\oplus H\), which is a lattice, with the asserted cardinality. The order-reversing map \((A,B)\mapsto(V\setminus B,V\setminus A)\) exchanges the two halves.

**3. Modularity and distributivity.** If there is at most one nonsingleton part, then \(H\) is Boolean and its vertical double is distributive. With two or more nonsingleton parts, choose complementary nonempty proper subsets \(A\) and \(P_i\setminus A\) in one factor, and any nonempty proper subset \(C\) from a second factor. These three elements have pairwise meet \(0\) and join \(1\), so together with \(0,1\) they form the nondistributive five-element sublattice \(M_3\). Therefore the double cannot be distributive. If all nonsingleton parts have size two, \(H\) has height two and is the modular lattice with \(2q\) middle atoms. If there is just one nonsingleton part, \(H\) is Boolean, hence modular. Conversely, when one part has size at least three and a second has size at least two, take \(\varnothing\subsetneq A\subsetneq B\subsetneq P_i\) in the first Boolean factor and a nonzero non-top element \(C\) in the second. In \(H\), \(A\le B\), \(C\wedge B=0\) and \(A\vee C=1\), so
\[
A\vee(C\wedge B)=A\ne B=(A\vee C)\wedge B.
\]
Hence modularity fails. The vertical sum of two modular lattices is modular; conversely each interval of a modular lattice is modular. This proves both criteria.

**4. Automorphisms and inverse classification.** The central point \((\varnothing,V)\) is the unique element other than bottom or top comparable to every lattice element: for each proper nonzero element within a Boolean factor of size at least two, a singleton outside its represented subset is incomparable to it. Therefore every order automorphism fixes the center and restricts independently to automorphisms of the two copies of \(H\). Remove the bottom and top of \(H\), and join two remaining vertices in an auxiliary graph when their lattice elements are comparable. Each Boolean factor of size \(m\ge3\) contributes one connected component containing \(2^m-2\) elements; within that component, every automorphism is induced by a permutation of its \(m\) singleton atoms. Each factor with \(m=2\) contributes exactly two isolated vertices; all \(2a\) isolated vertices are mutually interchangeable. Components of different sizes cannot be permuted, and the \(b_m\) equal-size components are freely interchangeable. This proves
\[
\operatorname{Aut}(H)\cong\mathfrak S_{2a}\times\prod_{m\ge3}(\mathfrak S_m\wr\mathfrak S_{b_m}),
\]
and the two independently moving copies give the group square. The same comparability-component decomposition recovers every \(m\ge3\) and its multiplicity from the component sizes, and recovers \(a\) as half the number of isolated components. Hence it recovers exactly the nonsingleton part-size multiset. Conversely this multiset determines \(H\oplus H\). Since \(N\) is the sum of all part sizes, specifying \(N\) additionally recovers the number of singleton parts.

## Verification

The standalone `verify.py` uses only the Python standard library. It constructs the reflexive neighborhoods of every complete multipartite graph for 134 ordered part profiles with total size between two and eight, enumerates all input subsets, and compares the resulting rough approximation pairs to the asserted normal form. It then constructs the coordinatewise order independently, checks existence and uniqueness of all binary meets and joins, evaluates modular and distributive identities, and verifies complement-swap self-duality. Run `python verify.py`; its expected success line starts `VERIFY_OK multipartite_profiles= 134`. The general theorem follows from the proof, not finite testing. The group and inverse claims follow from the component argument rather than from computational group enumeration.

## Relationship to prior work

Järvinen and Radeleczki's work on tolerance rough sets establishes general conditions under which their coordinatewise ordered pairs form a lattice, including a sufficient condition on forbidden tolerance paths; this already explains lattice existence for a reflexive complete multipartite graph, which has no induced five-vertex path. Their later work studies pseudo-Kleene operations and Dedekind–MacNeille completions for general reflexive relations. The present result does not claim these frameworks or the general lattice-existence criterion as new. Its asserted contribution is the explicit multipartite **order normal form**, exact cardinality and order-preserving automorphism group, and complete reconstruction and modularity boundaries.

Chiaselotti and collaborators compute indistinguishability partitions and closure systems from open adjacency neighborhoods of complete multipartite graphs; these concern a different graph-to-closure construction. Järvinen and collaborators' mixed \((E,T)\) rough-set constructions use an equivalence for the lower approximation and a compatible tolerance for the upper approximation, unlike the single tolerance used here. No inspected source supplied an implication that determines the full order structure and group formula asserted here. An equivalent specialization elsewhere, possibly under another lattice-decomposition terminology, remains a publication-priority risk.

## Limitations

Only connected complete multipartite graphs with at least two parts, and reflexive neighborhoods, are covered; arbitrary tolerance graphs need not have rough-set lattices. An abstract rough-set lattice cannot recover singleton parts without the original universe size. The available literature checks are not a proof of publication priority. This result has undergone the recorded self-review but no independent external audit.

## References

1. J. Järvinen and S. Radeleczki, *Rough sets determined by tolerances*, arXiv:1303.6332 (first public version 2013-03-25).
2. J. Järvinen and S. Radeleczki, *Pseudo-Kleene algebras determined by rough sets*, arXiv:2304.05641 (first public version 2023-04-12); *International Journal of Approximate Reasoning* 161 (2023), 108991, DOI:10.1016/j.ijar.2023.108991.
3. G. Chiaselotti et al., *Simplicial complexes and closure systems induced by indistinguishability relations*, *Comptes Rendus Mathématique* 355 (2017), 991–1021, DOI:10.1016/j.crma.2017.09.010.
4. J. Järvinen and collaborators, *Defining rough sets using tolerances compatible with an equivalence*, *Information Sciences* 496 (2019), 264–283, DOI:10.1016/j.ins.2019.05.030.
