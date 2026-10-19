# Commuting probabilities of truncated-quiver unit groups are Fortuin--Kasteleyn evaluations

## Finding
For a finite quiver \(Q=(V,E)\), including loops and multiple arrows, set \(A_Q=\mathbb F_qQ/J^2\) and \(G_Q=A_Q^\times\). Write \(H\) for the underlying undirected multigraph, retaining edge multiplicities. Define the Fortuin--Kasteleyn polynomial by
\[
 Z_H(t,v)=\sum_{F\subseteq E}t^{k(V,F)}v^{|F|},
\]
where \(k(V,F)\) is the number of connected components of the spanning subgraph with edge set \(F\), including isolated vertices. For every prime power \(q\), letting \(n=|V|\) and \(m=|E|\),
\[
\begin{aligned}
\#\{(g,h)\in G_Q^2:gh=hg\}&=q^m Z_H((q-1)^2,q-1),\\
k(G_Q)&=\frac{Z_H((q-1)^2,q-1)}{(q-1)^n},\\
\operatorname{cp}(G_Q)&=\frac{Z_H((q-1)^2,q-1)}{q^m(q-1)^{2n}}.
\end{aligned}
\]
Here \(k(G_Q)\) is the number of conjugacy classes. Thus these quantities are independent of the directions of all arrows, not merely a global orientation reversal. This applies also in residue characteristic two.

For every prime \(p\ge5\), the unit groups of the directed 3-cycle and of the transitive orientation of a triangle are **not isomorphic**, even though the displayed three invariants agree. At \(p=5\) each group has order \(8000\), conjugacy-class number \(140\), and commuting probability \(7/400\).

## Assumptions and scope
Here \(Q\) is a finite quiver, and \(J\) denotes its arrow ideal. The quotient by \(J^2\) has a basis consisting of vertex idempotents and individual arrows: distinct parallel arrows remain distinct, and the length-two products of any two arrows vanish. Every unit has a unique form
\[
 g=\sum_{v\in V}d_v e_v+\sum_{a\in E}x_a a,\qquad d_v\in\mathbb F_q^\times,\quad x_a\in\mathbb F_q.
\]
Thus \(|G_Q|=(q-1)^n q^m\). A loop is permitted and contributes a central radical coordinate; the definitions and formulas remain valid. The graph polynomial counts every arrow separately, including parallel arrows. A quiver with no arrows is included and has an abelian unit group. For the nonisomorphism assertion only, the coefficient field is the prime field \(\mathbb F_p\), with \(p\ge5\).

## Proof
**Commutativity equation.** Put \(g=(d,x)\) and \(h=(e,y)\). On an arrow \(a:u\to v\), multiplication in \(A_Q\) gives
\[
 (gh-hg)_a=(d_u-d_v)y_a-(e_u-e_v)x_a.
\]
The diagonal components automatically commute. For fixed diagonal assignments \(d,e\), the displayed equation is one linear equation in the two independent variables \(x_a,y_a\), for every arrow separately. It admits \(q^2\) solutions precisely when \(d_u=d_v\) and \(e_u=e_v\), and otherwise admits \(q\) solutions. This conclusion also applies to loops, which always satisfy the first case.

**Graph-polynomial expansion.** Attach to each vertex the color \(c_v=(d_v,e_v)\) in the \((q-1)^2\)-element set \((\mathbb F_q^\times)^2\). The total number of solutions for a fixed coloring is
\[
 q^m\prod_{a:u\to v}\left(1+(q-1)\mathbf 1_{c_u=c_v}\right).
\]
Expanding the product over the arrow subsets \(F\subseteq E\), a chosen edge enforces equality of colors at its endpoints, so exactly \(((q-1)^2)^{k(V,F)}\) colorings satisfy all chosen equalities. Summing gives the commuting-pair formula. Standard orbit-stabilizer for conjugation gives \(\#\{(g,h):gh=hg\}=|G_Q|\,k(G_Q)\); division by \(|G_Q|\) and \(|G_Q|^2\) proves the other two formulas.

**Nonisomorphic orientations.** Take three vertices and either the directed cycle \(1\to2\to3\to1\) or the transitive triangle \(1\to2\), \(2\to3\), \(1\to3\). Over \(\mathbb F_p\), where \(p\ge5\), the normal additive radical subgroup \(P=1+J\cong(C_p)^3\) is the unique Sylow \(p\)-subgroup of \(G_Q\); the quotient is the torus \(T\cong(C_{p-1})^3\). Conjugation of \(T\) on \(P\) splits into three one-dimensional characters, one for each arrow \(a:u\to v\):
\[
 \chi_a(d_1,d_2,d_3)=d_u d_v^{-1}.
\]
Since \(P\) is characteristic, an isomorphism between the groups would intertwine these character multisets, up to an automorphism of \(T\) and permutation of the three arrows. Accordingly, it would preserve the subgroup of exponent triples giving the trivial product of the three characters, up to a permutation of coordinates.

For the directed cycle the relation subgroup is \(\{(t,t,t):t\in\mathbb Z/(p-1)\}\). For the transitive triangle it is \(\{(t,t,-t):t\in\mathbb Z/(p-1)\}\). When \(p-1\ge4\), these are not equal under any coordinate permutation: the first has all coordinates equal, while the second contains \((1,1,-1)\). Therefore the groups are not isomorphic. Yet both have the same underlying undirected triangle, proving the equal-invariant assertion. For \(p=5\), evaluating the three-cycle polynomial yields \(k(G_Q)=140\); since \(|G_Q|=5^3\cdot4^3=8000\), \(\operatorname{cp}(G_Q)=140/8000=7/400\).

**Two closed classes.** For a forest of \(m\) edges, each chosen edge decreases the component count by one; hence \(Z_H(t,v)=t^{n-m}(t+v)^m\). Substituting the given parameters gives \(\operatorname{cp}(G_Q)=(q-1)^{-m}\). For a connected simple unicyclic graph with unique cycle length \(\ell\), the bridge edges factor out of the subgraph expansion, while the cycle contribution is \((t+v)^\ell+(t-1)v^\ell\); substitution yields
\[
 \operatorname{cp}(G_Q)=(q-1)^{-m}\left(1+(q-2)q^{1-\ell}\right).
\]
No assertion about graphs with several cycles is needed beyond the general polynomial formula.

## Verification
The included standalone \(\texttt{checker.py}\) uses integer arithmetic and exhaustive lists of units to count pairs by the actual arrow-by-arrow multiplication law, independently of the subgraph formula. It compares this brute-force count with a separately implemented spanning-subgraph calculation in ten finite-field cases, including reversed arrows, loops, and parallel edges. It then checks the unicyclic closed formula exactly for three small prime fields and three cycle lengths. Execute \(\texttt{python3 checker.py}\) with Python 3; success ends with \(\texttt{VERIFY_OK}\). These finite checks are evidence of implementation fidelity, not a substitute for the general proof. The nonisomorphism argument is algebraic rather than a brute-force isomorphism search.

## Relationship to prior work
Browning [1] studies the global set and limits of finite-group commuting probabilities; no quiver unit-group or graph-partition enumeration appears in the inspected material. Rossmann [2] counts conjugacy classes in *class-two graphical groups*, which are constructed differently from the solvable unit groups \(A_Q^\times\) considered here; the full introduction and group construction were compared, and neither the general formula nor the orientation-pair example follows from the stated results without additional work. Hennecart and Perry [3] study commuting pairs in radicals of quiver endomorphism algebras (and quiver operations preserving those radical counts); this is not commuting pairs among arbitrary *units*, where the nonzero diagonal torus matters. The Fortuin--Kasteleyn subgraph expansion is classical; identifying the finite-group class number with its specified specialization is the proposed contribution, not invention of that identity.

A previously considered rank enumerator for all elements of a radical-square-zero path algebra uses the same elementary edge commutator but allows **all** diagonal labels, not only invertible ones. Restricting to units and interpreting the result as group conjugacy, including the nonisomorphic-orientation examples, is a separate claim. Although this makes the new proof short, it increases the need to check for equivalent unit-group results in the literature.

## Limitations
The theorem is about radical-square-zero quiver algebras; ordinary path algebras with surviving length-two paths generally violate the independent-edge equation. The graph polynomial gives only group commuting pairs and the total conjugacy-class number, not complete conjugacy-class size distributions, irreducible-character degrees, or a classification of all isomorphic unit groups. The nonisomorphism witness is proved for **prime** coefficient fields of characteristic at least five and is not claimed for all prime powers. A broader semidirect-product conjugacy-count formula in existing literature may imply the result; no exhaustive novelty certification is claimed. Independent audit has not been performed.

## References
[1] T. Browning, *Limit Points of Commuting Probabilities of Finite Groups*, arXiv:2201.09402v1 (first public 2022-01-24), https://arxiv.org/abs/2201.09402.

[2] T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1 (first public 2021-07-12), https://arxiv.org/abs/2107.05564; Bull. London Math. Soc. **54** (2022), 1923–1943, https://doi.org/10.1112/blms.12665.

[3] L. Hennecart and N. Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1 (first public 2022-08-16), https://arxiv.org/html/2208.07738v1.

[4] A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, Surveys in Combinatorics (2005). The subgraph expansion is used as a standard combinatorial identity.
