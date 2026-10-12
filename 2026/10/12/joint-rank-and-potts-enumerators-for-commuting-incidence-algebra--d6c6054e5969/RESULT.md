# Joint-rank and Potts enumerators for commuting incidence-algebra idempotents

## Finding

Let \(P\) be any nonempty finite poset with \(n\) elements, let \(K\) be any field, and let \(k\geq2\). Write \(I_K(P)\) for its incidence algebra. The variety of ordered, pairwise-commuting \(k\)-tuples \((e_1,\ldots,e_k)\) satisfying \(e_j^2=e_j\) is a disjoint union of exactly \(2^{kn}\) affine varieties. Its pieces are indexed by colorings \(c:P\to\{0,1\}^k\), and the piece with diagonal tuple \(c\) is explicitly isomorphic to an affine space of dimension
\[
d_P(c)=\#\{(x,y):x<y\text{ in }P,\ c(x)\neq c(y)\}.
\]
Every such tuple is simultaneously conjugate by an element of \(1+J\), where \(J\) is the strictly upper-incidence radical, to its diagonal tuple. This diagonalization itself is known from the structural-matrix-algebra literature; the specified affine normal form and the joint enumerator below are the conclusions investigated here. The conjugating element has a unique representative \(1+a\) with \(a(x,y)=0\) whenever \(c(x)=c(y)\).

For \(K=\mathbb F_q\), the joint ordinary matrix-rank enumerator is
\[
F_{P,k,q}(T_1,\ldots,T_k)=
\sum_{c:P\to\{0,1\}^k}q^{d_P(c)}
\prod_{h=1}^k T_h^{\#\{x:c_h(x)=1\}}.
\]
This holds for every prime power \(q\), including even characteristic. Let \(G_P\) be the undirected comparability graph (one edge for each strict comparable pair), with \(m\) edges, and define the Fortuin--Kasteleyn polynomial
\[
Z_G(Q,v)=\sum_{A\subseteq E(G)}Q^{\kappa(A)}v^{|A|},
\]
where \(\kappa(A)\) counts the connected components, including isolated vertices, of the spanning graph \((V(G),A)\). Then the total number of tuples is
\[
F_{P,k,q}(1,\ldots,1)=q^m Z_{G_P}(2^k,q^{-1}-1).
\]
In particular this total depends only on the comparability graph, and varying \(k\) and \(q\) determines its full two-variable Fortuin--Kasteleyn (equivalently Tutte) polynomial by interpolation. For fixed \(k\), the degree in \(q\) is the maximum \(2^k\)-cut size of \(G_P\), with leading coefficient the number of maximizing labeled \(2^k\)-colorings. Writing \(h(P)\) for the maximum size of a chain, this degree equals the total number \(m\) of strict comparabilities **if and only if** \(2^k\ge h(P)\); in that case its leading coefficient is the proper-coloring polynomial \(\chi_{G_P}(2^k)\).

## Assumptions and scope

Fix a linear extension of \(P\). Identify \(I_K(P)\) with the subalgebra of \(n\)-by-\(n\) upper-triangular matrices supported on \((x,y)\) with \(x\leq y\). Its radical \(J\) is supported on strict intervals. Matrix rank is the rank on the natural \(n\)-dimensional representation, not the rank of left multiplication on the incidence algebra. The tuple is ordered and idempotence means multiplicative idempotence of each element, not composition-idempotence of an algebra map. The affine decomposition is valid over arbitrary fields. No restriction on the characteristic or height of the poset is needed.

## Proof

**Joint spectral projections.** For a commuting idempotent tuple \(e=(e_h)\), let \(c_h(x)=e_h(x,x)\in\{0,1\}\). For each \(\sigma\in\{0,1\}^k\), define
\[
p_\sigma=\prod_{h:\sigma_h=1}e_h\prod_{h:\sigma_h=0}(1-e_h),
\qquad
D_\sigma=\operatorname{diag}(\mathbf1_{\{x:c(x)=\sigma\}}).
\]
These are mutually orthogonal idempotents summing to \(1\); the diagonal of \(p_\sigma\) equals \(D_\sigma\). Set \(u=\sum_\sigma p_\sigma D_\sigma\). Then \(u\equiv1\pmod J\), so \(u\in1+J\) is invertible. Moreover \(uD_\sigma=p_\sigma u\), whence \(e_h=uD_hu^{-1}\), with \(D_h=\sum_\sigma\sigma_hD_\sigma\). This works without division and in any characteristic.

**A canonical affine coordinate chart.** Split the radical as a vector space \(J=J_{\mathrm{same}}\oplus J_{\mathrm{diff}}\), according as \(c(x)=c(y)\) or not on each strict interval. The first summand is a nilpotent subalgebra, and \(J_{\mathrm{diff}}J_{\mathrm{same}}\subseteq J_{\mathrm{diff}}\). Thus every \(u\in1+J\) decomposes uniquely as
\[
u=(1+a)b,\qquad a\in J_{\mathrm{diff}},\quad b\in1+J_{\mathrm{same}}.
\]
Indeed, write \(u=1+s+t\), with \(s\) of same-color support and \(t\) of different-color support. Choose \(b=1+s\); then \(a=t(1+s)^{-1}\in J_{\mathrm{diff}}\). In the opposite direction, the same-color part of \((1+a)b-1\) equals \(b-1\), proving uniqueness. Exactly \(1+J_{\mathrm{same}}\) centralizes all \(D_h\). Consequently the fiber at \(c\) consists bijectively of
\[
((1+a)D_h(1+a)^{-1})_{h=1}^k,
\quad a\in J_{\mathrm{diff}}.
\]
The forward map is polynomial because \(J\) is nilpotent. Its inverse is polynomial: recover \(p_\sigma\), then \(u=\sum p_\sigma D_\sigma\), then \(b=1+\operatorname{pr}_{\mathrm{same}}(u-1)\), and finally \(a=ub^{-1}-1\). Every inverse is a finite nilpotent geometric series. Therefore this is an affine-space isomorphism, not merely a point count. Its dimension is \(d_P(c)=\dim J_{\mathrm{diff}}\). Distinct color patterns have distinct diagonals, hence disjoint fibers; the diagonal map takes values in a finite discrete set, so these are precisely the connected and irreducible components after extension to an algebraic closure.

**Counting and ranks.** There are \(q^{d_P(c)}\) choices of \(a\) in the fiber over \(c\). Since an idempotent upper triangular matrix has rank equal to the number of diagonal entries equal to \(1\), weighting by each \(\operatorname{rank}(e_h)\) yields the stated formula.

**Graph-polynomial identification.** Every strict interval gives precisely one edge of \(G_P\), contributing weight \(q\) if its endpoint colors differ and \(1\) otherwise. Thus the total is
\[
\sum_c\prod_{xy\in E(G_P)}(q+(1-q)\mathbf1_{\{c(x)=c(y)\}}).
\]
Expand the product over subsets \(A\) of equality-constrained edges. Exactly \((2^k)^{\kappa(A)}\) colorings satisfy those equalities, giving \(\sum_A q^{m-|A|}(1-q)^{|A|}(2^k)^{\kappa(A)}\), the displayed Fortuin--Kasteleyn evaluation. Because this is a polynomial in \(Q\) and \(v\), its evaluations at infinitely many \(Q=2^k\) and infinitely many \(v=q^{-1}-1\) uniquely determine it. Finally, the degree and leading coefficient of the original positive sum in \(q\) are the maximal cross-color edge count and its number of achievers. No cancellation occurs in that positive expansion. The maximal cut contains all \(m\) edges precisely when the comparability graph admits a proper \(2^k\)-coloring. Every chain in \(P\) is a comparability clique, hence requires at least \(h(P)\) colors. Conversely, assigning to each element the length of a longest chain ending there gives a proper coloring by \(h(P)\) colors: for \(x<y\), the longest-chain length strictly increases. The claimed sharp threshold and chromatic leading coefficient follow.

## Verification

The self-contained `checker.py` enumerates every incidence-algebra matrix over small finite fields, tests idempotence and pairwise commutation by direct multiplication, then independently generates all tuples using the canonical different-color coordinate charts and compares complete joint-rank multiplicities against the formula. Cases include chains, a fork, a diamond, and an antichain; field sizes include \(2\), \(3\), and \(4\), and one case checks \(k=3\). Running `python3 checker.py` prints `VERIFY_OK` upon success.

For the three-element chain over \(\mathbb F_2\) and \(k=2\), direct enumeration finds \(26\) individual idempotents and \(340\) ordered commuting idempotent pairs. For the four-element diamond over \(\mathbb F_2\), there are \(114\) individual idempotents and \(4132\) ordered commuting pairs. These are finite checks, not substitutes for the general proof.

## Relationship to prior work

Gogić and Tomašević, *Jordan Embeddings and Linear Rank Preservers of Structural Matrix Algebras* (arXiv:2409.16906v1, 2024), prove intrinsic simultaneous diagonalization of arbitrary commuting families of diagonalizable complex matrices in a structural matrix algebra (Theorem 3.4). Their subsequent *Multiplicative and Jordan Multiplicative Maps on Structural Matrix Algebras* (arXiv:2503.14116v1, 2025, Remark 3.8) explicitly extends the **commuting-idempotent simultaneous diagonalization** statement to structural matrix algebras over arbitrary fields. Every incidence algebra of a finite poset is a structural matrix algebra; therefore the bare simultaneous-diagonalization assertion in the present proof is a **known premise**, not a novelty claim. The inspected full texts do not derive canonical affine coordinates for each joint diagonal color pattern, the characteristic-uniform exact joint-rank polynomial, or its Fortuin--Kasteleyn identification. That combinatorial and enumerative package is the claim at issue.

Can, Casimiro and Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets* (arXiv:2208.01073v1, first posted 2022-08-01), establish the decomposition of the **single-idempotent** variety into \(2^n\) conjugacy-orbit components (Theorem 3.2). Their examples and complete bipartite cases include affine component charts. The \(k=1\) specialization of our statement is therefore not claimed as new. Their Theorem 4.9 studies multiplication of components in a special antichain monoid, not arbitrary commuting tuples with joint rank weights.

Can, *Incidence Monoids: Automorphisms and Complexity* (arXiv:2105.09826v1, 2021), studies algebraic-monoid automorphisms, torus-action complexity and star-poset orbits. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field* (arXiv:1409.2698, 2014), studies general commuting tuples under full-matrix similarity, rather than the incidence-algebra constrained point-counting problem. The Fortuin--Kasteleyn edge-subset expansion itself is standard; the new connection, if not previously observed, is its equality with the total count of algebraically constrained commuting-idempotent tuples.

## Limitations

The theorem concerns tuples of **idempotents** that commute; it does not count arbitrary commuting tuples or classify commuting nilpotents. Its rank is the ordinary matrix rank in the natural incidence representation. The simultaneous-diagonalization step is already established by Gogić and Tomašević, and the single-idempotent orbit decomposition by Can, Casimiro and Malheiro. The precise originality claim is limited to the explicit joint-color affine coordinates, finite-field multivariate rank distribution and incidence-algebra/Potts identification; their possible derivability from general orbit methods remains a bibliographic risk. This account does not claim an independent novelty certification. The Tutte specialization determines the comparability-graph polynomial but does not reconstruct the directed poset. The full-rank-leading-degree threshold is a consequence of comparability-graph coloring, not an assertion of a new graph coloring theorem.

## References

1. M. B. Can, A. Casimiro and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073v1 (2022), Theorem 3.2 and Sections 3, 5 and 7.
2. M. B. Can, *Incidence Monoids: Automorphisms and Complexity*, arXiv:2105.09826v1 (2021), Theorems 1.1--1.4.
3. U. B. Sharma, *Simultaneous Similarity Classes of Commuting Matrices over a Finite Field*, arXiv:1409.2698 (2014), Section 1 and subsequent type calculations.
4. I. Gogić and M. Tomašević, *Jordan Embeddings and Linear Rank Preservers of Structural Matrix Algebras*, arXiv:2409.16906 (2024), Theorem 3.4 and its proof.
5. I. Gogić and M. Tomašević, *Multiplicative and Jordan Multiplicative Maps on Structural Matrix Algebras*, arXiv:2503.14116 (2025), Theorem 2.2 and Remark 3.8.
