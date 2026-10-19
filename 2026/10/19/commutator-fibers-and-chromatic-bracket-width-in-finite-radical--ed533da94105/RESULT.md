# Commutator fibers and chromatic bracket width in finite radical-square-zero quiver algebras

## Finding
Let \(A=\mathbb F_q Q/J^2\) for an arbitrary finite quiver \(Q\) with at least one vertex and any finite field of order \(q\). The exact number of ordered algebra-element pairs with a prescribed associative commutator is a vertex-coloring partition function. In addition, the minimal number of commutators needed for each target and the maximum such number are **exactly determined by ordinary graph chromatic numbers**.

For a target \(w\) in the derived Lie subspace \(J_{\mathrm{off}}\), with support graph \(G_w\), the additive commutator length is
\[
\ell(w)=\left\lceil\log_{q^2}\chi(G_w)\right\rceil.
\]
The zero vector has length zero, as does every target when there are no nonloop arrows. For the full graph \(G\), the width is therefore \(\lceil\log_{q^2}\chi(G)\rceil\). The result also determines **all** exact commutator fibers, including those of unattainable targets.

## Assumptions and scope
Take a finite quiver \(Q\) with vertex set \(V\), loops, parallel arrows, and arrows in opposite directions all allowed. Put \(A=\mathbb F_qQ/J^2\), where \(J\) is the arrow ideal. Set \(J_{ij}=e_iJe_j\). For each unordered pair of distinct vertices \(e=\{i,j\}\), let \(\mu_e=\dim J_{ij}+\dim J_{ji}\), and let \(G=(V,E)\) have exactly those edges with \(\mu_e>0\). Let \(h=\sum_i\dim J_{ii}\), \(M=\sum_{e\in E}\mu_e\), and \(J_{\mathrm{off}}=\bigoplus_{i\ne j}J_{ij}\). By \([A,A]\) we mean the \(\mathbb F_q\)-linear span of the associative brackets \([x,y]=xy-yx\); this is not the derived subgroup of units.

For \(w\in J_{\mathrm{off}}\), let \(G_w=(V,E_w)\) where an edge \(\{i,j\}\) lies in \(E_w\) exactly when the joint coordinate of \(w\) in \(J_{ij}\oplus J_{ji}\) is nonzero. Proper coloring on \(G_w\) means unequal colors at endpoints of every supported edge. Every graph considered has the full vertex set \(V\), so the chromatic number is one for the empty-edge graph.

**Fiber theorem.** If \(w\in J_{\mathrm{off}}\), then
\[
N(w)=\#\{(x,y)\in A^2:[x,y]=w\}
=q^{2h+M}\sum_{\substack{c:V\to\mathbb F_q^2\\c\text{ proper on }G_w}}
q^{\sum_{e=\{i,j\}\in E:\,c(i)=c(j)}\mu_e}.
\]
If \(w\notin J_{\mathrm{off}}\), then \(N(w)=0\). The number of distinct single commutators is
\[
\sum_{F\subseteq E:\ \chi(V,F)\le q^2}\ \prod_{e\in F}(q^{\mu_e}-1).
\]
The empty product contributes one. For every \(r\ge0\), a target \(w\in J_{\mathrm{off}}\) is a sum of at most \(r\) brackets if and only if \(\chi(G_w)\le q^{2r}\). Thus
\[
\ell(w)=\lceil\log_{q^2}\chi(G_w)\rceil,\qquad
\operatorname{bw}(A^-)=\lceil\log_{q^2}\chi(G)\rceil.
\]
These are statements about the **additive Lie bracket**, not group commutators in \(A^\times\).

## Proof
First, every element decomposes uniquely as \(x=\sum_i a_ie_i+\sum_{i,j}u_{ij}\), with \(u_{ij}\in J_{ij}\). Multiplication respects the vertex-corner actions and \(J^2=0\). For \(y=\sum_i b_ie_i+\sum_{i,j}v_{ij}\), direct multiplication gives
\[
[x,y]_{ij}=(a_i-a_j)v_{ij}-(b_i-b_j)u_{ij}.
\]
For \(i=j\) this is zero, so every commutator lies in \(J_{\mathrm{off}}\). Conversely, each \(u\in J_{ij}\) with \(i\ne j\) equals \([e_i,u]\), proving \([A,A]=J_{\mathrm{off}}\) as a linear space.

Assign to vertex \(i\) the diagonal pair \(c(i)=(a_i,b_i)\in\mathbb F_q^2\), independently across vertices. On a nonloop corner of dimension \(m\), the map \((u_{ij},v_{ij})\mapsto[x,y]_{ij}\) is zero when \(c(i)=c(j)\), giving exactly \(q^{2m}\) preimages of the zero vector and none of a nonzero vector. When \(c(i)\ne c(j)\), at least one scalar coefficient in the displayed equation is nonzero; therefore the map is surjective, and each vector has exactly \(q^m\) preimages. Opposite orientations and parallel arrows obey these rules independently, while every loop contributes \(q^2\) unconstrained choices. Consequently a vertex labeling is compatible with \(w\) exactly when it is proper on \(G_w\), and multiplying the independent corner counts proves the fiber theorem.

A target \(w\in J_{\mathrm{off}}\) is one commutator precisely when some labeling by \(q^2\) vertex colors separates every edge of \(G_w\), equivalently when \(\chi(G_w)\le q^2\). The number of choices of a target with **exactly** support \(F\) is \(\prod_{e\in F}(q^{\mu_e}-1)\). Distinct supports are disjoint; summing those with chromatic number at most \(q^2\) proves the image-size formula.

For a sum of \(r\) commutators, each summand has its own diagonal pair coloring. Combine the \(r\) choices at each vertex into a single \(q^{2r}\)-valued color. If an edge supports a nonzero coordinate of \(w\), at least one summand must separate that edge, so the combined colors are distinct there. This establishes necessity of \(\chi(G_w)\le q^{2r}\). Conversely, given a proper coloring by \(q^{2r}\) colors, identify each color with \(r\) ordered pairs from \(\mathbb F_q^2\). For each edge of \(G_w\), choose a summand where its endpoint pairs differ, assign the entire vector component of \(w\) on that edge to that summand, and make the remaining contributions zero. By the surjective corner map above, select radical coordinates realizing every assigned component. This produces exactly \(w\) as a sum of \(r\) brackets. Finally, a target supported on every edge exists because each positive-dimensional corner admits a nonzero vector, so the maximum length equals the length dictated by \(G\).

## Verification
Run `python3 check_commutators.py` with Python 3 and its standard library. The script constructs multiplication in the quiver quotient directly from vertex and arrow basis rules, exhaustively enumerates ordered pairs over fields of orders two and three in seven small configurations, and compares every fiber size to a second implementation of the vertex-coloring sum. It also exhaustively determines the chromatic thresholds for the complete graphs on four and five vertices and for the five-cycle. The final expected line is `ALL_COMMUTATOR_FIBER_AND_WIDTH_CHECKS_PASSED`.

As a sharp example, over \(\mathbb F_2\), an algebra whose graph is the complete graph on five vertices has a nonzero-on-every-edge target which **cannot** be a single commutator, since five colors are needed but only four diagonal pairs are available. Every such target is a sum of two commutators, because sixteen combined colors are available. The complete graph on seventeen vertices yields width three. In the complete four-vertex graph with one oriented arrow per edge, the all-nonzero target has exactly \(2^6\cdot4!=1536\) ordered preimages, by the displayed formula. These large-graph consequences are proved by coloring, not by exhaustive element enumeration.

## Relationship to prior work
Kunyavskii, Makedonskyi and Regeta (arXiv:2404.06045, 2024) develop bracket width for current Lie algebras over algebraically closed characteristic-zero fields, including an upper bound of two in their different tensor-product setting. Their Theorem 1 and proof do not imply a finite-field, quiver-specific chromatic formula or commutator fibers. Dubouloz, Kunyavskii and Regeta (arXiv:2102.08674, 2021) establish a broader motivation for studying bracket width but focus on simple Lie algebras of vector fields. Mazorchuk and Zhang (arXiv:1703.08377, 2017) analyze bimodules for certain radical-square-zero quiver algebras, not additive commutator images.

Existing finite Kronecker-algebra commutator-fiber records concern two vertices; their outcomes are special cases, not a uniform statement for arbitrary finite quivers. An earlier finite-quiver **unit-group** commutator-width theorem uses multiplicative commutators and a different palette \((q-1)^{2r}\) when \(q>2\); it does not imply the current all-element additive theorem, especially over \(\mathbb F_2\), where the unit group can be abelian while \(A^-\) has nonzero brackets. The present finding's central extra invariant is the exact fiber of **every prescribed** additive commutator target, not merely the graph-coloring threshold.

## Limitations
This result applies to finite split radical-square-zero quiver algebras and requires the standard associative commutator; general path algebras with nonzero products of two arrows are not covered. Chromatic numbers can be computationally hard for large graphs; the formulas are mathematically exact, not promised polynomial-time algorithms. The source comparisons establish no absolute priority or exhaustive survey of inaccessible older literature. The finite checks do not replace the proof. Independent mathematical audit has not been performed.

## References
- B. Kunyavskii, I. Makedonskyi and A. Regeta, *Bracket width of current Lie algebras*, arXiv:2404.06045, first public version 2024-04-09.
- A. Dubouloz, B. Kunyavskii and A. Regeta, *Bracket width of simple Lie algebras*, arXiv:2102.08674, first public version 2021-02-17.
- V. Mazorchuk and X. Zhang, *Bimodules over uniformly oriented \(A_n\) quivers with radical square zero*, arXiv:1703.08377, first public version 2017-03-24.
