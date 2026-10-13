# Prescribed bracket fibers of finite-field graphical Lie algebras on forests

## Finding
Let \(q\) be any prime power. For the canonical two-step nilpotent Lie algebra of **every** finite simple forest, we give a complete formula for the fiber of the Lie bracket at **each** prescribed central element, not merely at zero.

For a forest \(G=(V,E)\) with \(m=|E|\), fix an orientation of each edge. Write \(L_G=\mathbb F_q^V\oplus\mathbb F_q^E\), with the second summand central and \([e_u,e_v]=z_{uv}\) when \((u,v)\) is an oriented edge. For any \(z=\sum_{e\in E}b_e z_e\), put \(B=\{e\in E:b_e\ne0\}\), \(W(B)=\bigcup_{e\in B}e\), \(e(U)=|E(G[U])|\), and let \(c(U)\) be the number of connected components of the induced forest \(G[U]\) (with \(c(\varnothing)=0\)). Then

\[
\boxed{\#\{(x,y)\in L_G^2:[x,y]=z\}
=q^{2m+|B|}\sum_{W(B)\subseteq U\subseteq V}(q^2-1)^{c(U)}(q-1)^{e(U)-|B|}.}
\]

The count depends only on the **support** \(B\), not the nonzero values \(b_e\), and is strictly positive for every \(z\in\mathbb F_q^E\). Thus the Lie bracket map is surjective. The formula also applies to disconnected forests, empty edge sets, isolated vertices, fields of characteristic two, and extension fields.

## Assumptions and scope
All graphs here are finite, simple and acyclic. A forest may have isolated vertices. If \(V=\varnothing\), use \(L_G=0\) and the sole empty bracket fiber has size one. Choose edge orientations for coordinate signs; changing them only changes the signs of target coefficients. For every field and target, \(W(B)\) is the set of endpoints incident to at least one nonzero target coordinate. In any induced forest \(G[U]\), the component count satisfies \(e(U)=|U|-c(U)\).

The ordered pairs are taken from the **entire** Lie algebra, including its \(m\)-dimensional central summand. A graph with cycles is not covered: a prescribed set of edge determinants may impose nontrivial compatibility around a cycle.

## Proof
Write \(x=(a,\xi)\) and \(y=(b,\eta)\), with \(a,b\in\mathbb F_q^V\) and \(\xi,\eta\in\mathbb F_q^E\). The central entries are unrestricted; they contribute \(q^{2m}\). At each vertex \(v\), form the column \(w_v=(a_v,b_v)\in\mathbb F_q^2\). The coefficient of an oriented edge \(u\to v\) in the bracket is exactly
\[
\det(w_u,w_v)=a_u b_v-a_v b_u.
\]
This determinant description is valid also in characteristic two, since the bracket remains alternating.

For a candidate pair, let \(U=\{v\in V:w_v\ne0\}\). If an edge has a nonzero prescribed determinant, both its endpoints must lie in \(U\); hence \(W(B)\subseteq U\). Edges not entirely contained in \(U\) automatically have determinant zero. Conversely, for any \(U\supseteq W(B)\), we count nonzero columns at all vertices of \(U\) with determinants fixed on the edges of \(G[U]\).

Every connected component of \(G[U]\) is a tree. Choose a root and direct all its edges away from the root. The root column has exactly \(q^2-1\) nonzero possibilities. If a parent column \(w\ne0\) is fixed, the linear functional \(t\mapsto\det(w,t)\) on \(\mathbb F_q^2\) is surjective and each of its fibers has \(q\) members. For a zero prescribed determinant, the fiber is a one-dimensional subspace, and excluding \(t=0\) leaves \(q-1\) possibilities. For a nonzero determinant, all \(q\) points of its affine fiber are nonzero. The sign of a reversed parent edge does not affect these cardinalities. Since there are no cycles, these successive choices are independent and each edge constraint is imposed exactly once.

The number for this fixed \(U\) is therefore
\[
(q^2-1)^{c(U)}q^{|B|}(q-1)^{e(U)-|B|}.
\]
Summing over \(W(B)\subseteq U\subseteq V\), then multiplying by \(q^{2m}\), proves the claimed formula for every target. It depends only on \(B\). Taking \(U=V\) gives a strictly positive term for all \(q\ge2\), proving surjectivity. When \(E=\varnothing\), the sum is \(q^{2|V|}\) as it must be.

For a concrete support-sensitive example, take the path on vertices \(1,2,3,4\) with successive edges. Over \(\mathbb F_2\), direct evaluation of the subset formula gives \(36\) vertex-coordinate pairs for a target supported on an end edge but \(24\) for support on the middle edge. Here \(m=3\), so multiplying by the central factor \(2^{2m}=64\) gives \(2304\) and \(1536\) ordered Lie-algebra pairs. Thus the fiber is not determined merely by the number of nonzero target coordinates.

## Verification
The accompanying stand-alone file `verify_forest_fibers.py` implements finite-field determinant multiplication, evaluates every target directly by brute force over seven small forests and fields \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), and compares this with the support-subset formula. There are exactly 277 target checks. Independent normalization checks verify that the sum of all vertex-coordinate fibers equals \(q^{2|V|}\) for the same graphs and \(q\in\{2,3,4,5,7\}\). It also verifies the explicit path and star examples. Run `python3 verify_forest_fibers.py`; successful output begins with `VERIFY_OK`. These tests are finite; the proof above is what establishes all forests and all prime powers.

## Relationship to prior work
Dani and Mainkar (2004/2005) introduced the graph-associated two-step nilpotent Lie algebras used here. Rossmann (2022), Sections 2–4 and 6, develops their finite-field graphical groups and studies conjugacy classes and centralizers, i.e. distributions attached to the **zero bracket** and variable adjoint maps. Tittmann, Averbouch and Makowsky (2008) develop the induced-subgraph component polynomial, which gives a known graph-polynomial route to the **zero-target** case. Indeed at \(B=\varnothing\) our vertex-coordinate count is \(\sum_U(q^2-1)^{c(U)}(q-1)^{e(U)}\), a standard vertex-subset component evaluation, and no novelty is asserted for that specialization.

The new quantified assertion is the entire **prescribed nonzero-target** fiber law and its support dependence, uniform for forests including characteristic two. It does not follow from just the zero-target total or a conjugacy-class distribution: those determine centralizer sizes or a single target fiber, not the number of solutions for every nonzero element of the commutator subspace. Related formulas for associative radical-square-zero quiver algebras count commutators with different matrix coefficients; their exact Tutte specialization does not identify the determinant bracket map of this graphical Lie algebra.

## Limitations
The formula presupposes a forest. We do not claim it for cyclic graphs or arbitrary finite two-step nilpotent Lie algebras. The result counts all ordered pairs, not equivalence classes under automorphisms. It establishes surjectivity of the bracket map, not uniqueness of the underlying graph from the fiber data. Characteristic two is permitted, but no group-isomorphism assertion is needed. The finite checks are not a substitute for the general proof; the literature comparison may be incomplete, particularly for alternative descriptions of prescribed commutator word-map fibers.

## References
1. S. G. Dani and M. G. Mainkar, “Anosov automorphisms on compact nilmanifolds associated with graphs,” *Transactions of the American Mathematical Society* **357** (2005), 2235–2251; electronically published 27 April 2004. DOI: `10.1090/S0002-9947-04-03518-4`; author-hosted full text: https://people.se.cmich.edu/maink1m/trans.pdf.
2. T. Rossmann, “Enumerating conjugacy classes of graphical groups over finite fields,” *Bulletin of the London Mathematical Society* **54** (2022), 1923–1943. DOI: `10.1112/blms.12665`. Open full text: https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/blms.12665.
3. P. Tittmann, I. Averbouch and J. A. Makowsky, “The enumeration of vertex induced subgraphs with respect to the number of components,” 2008 preprint, arXiv:0812.4147v1 (22 December 2008), https://arxiv.org/abs/0812.4147.
