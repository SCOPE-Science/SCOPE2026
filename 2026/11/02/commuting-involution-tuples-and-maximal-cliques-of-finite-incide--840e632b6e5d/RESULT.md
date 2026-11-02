# Commuting involution tuples and maximal cliques of finite incidence algebras

## Finding
Let \(P\) be any nonempty finite poset with \(n\) vertices and \(m\) strictly comparable unordered pairs. Write \(G_P\) for its comparability graph (all pairs \(x<y\), not merely cover relations). For an odd prime power \(q\), let \(A=I(P,\mathbb F_q)\) be its incidence algebra. Write \(C_k(P,q)\) for the number of ordered \(k\)-tuples \((a_1,\ldots,a_k)\in A^k\) such that \(a_i^2=1\) for every \(i\) and \(a_ia_j=a_ja_i\) for every pair, including repeated entries. Set \(Q=2^k\), and, for a graph edge set \(F\), let \(\kappa(F)\) be the number of connected components of \((V(G_P),F)\), including isolated vertices.

**The joint-involution and maximal-clique theorem.** For every integer \(k\ge0\),
\[
 C_k(P,q)=\sum_{c:V(G_P)\to[Q]}q^{\#\{xy\in E(G_P):c(x)\ne c(y)\}}=\sum_{F\subseteq E(G_P)}q^{m-|F|}(1-q)^{|F|}Q^{\kappa(F)}.
\]
In particular, the complete all-arity sequence is the \(Q\)-state random-cluster/Potts polynomial of the comparability graph at \(Q=2^k\) and interaction \(q^{-1}-1\), multiplied by \(q^m\).

Form the graph whose vertices are all elements \(a\in A\) with \(a^2=1\), and whose distinct vertices are adjacent exactly when they commute. Every inclusion-maximal clique has exactly \(2^n\) vertices, and there are **exactly \(q^m\)** such cliques. Each is an elementary abelian \(2\)-subgroup of \(A^\times\), and they are conjugate under the unipotent group \(1+J(A)\). Equivalently, every maximal elementary abelian \(2\)-subgroup of \(A^\times\) is such a conjugate.

The full all-arity sequence determines the number \(f_r\) of unordered commuting sets of \(r\) *distinct* involutions for every \(0\le r\le2^n\):
\[
 f_r=\frac1{r!}\sum_{j=0}^r s(r,j)C_j(P,q),
\]
where \(s(r,j)\) are signed Stirling numbers of the first kind; \(f_r=0\) for \(r>2^n\). For all odd prime powers \(q\) jointly and all \(k\ge0\), these numbers recover the full random-cluster polynomial of \(G_P\), hence its Tutte polynomial. For fixed \(k\),
\[
 \lim_{q\to\infty\atop q\text{ odd prime power}}q^{-m}C_k(P,q)=\chi_{G_P}(2^k),
\]
where \(\chi_{G_P}\) is the chromatic polynomial.

For a three-element fork poset (one minimal point below two incomparable points) or its opposite, \(G_P\) is a path on three vertices and
\[
 C_k(P,q)=2^k\bigl(1+(2^k-1)q\bigr)^2.
\]
These nonisomorphic posets have identical commuting-involution tuple sequences for every odd \(q\) and every \(k\).

## Assumptions and scope
The field has characteristic different from \(2\). The poset is finite and nonempty, with an arbitrary number of connected components; incidence-algebra basis vectors correspond to every interval \(x\le y\). Here \(J(A)\) is the ideal of matrices with vanishing diagonal entries, of \(\mathbb F_q\)-dimension \(m\). The argument concerns *elements* squaring to the identity, not involutive anti-automorphisms of the algebra. Every tuple entry is invertible. The \(k=0\) tuple is counted once. The coloring labels are ordered sign-character vectors and are not identified up to permutation.

## Proof
**Simultaneous character projections.** Let \(a_1,\ldots,a_k\) be pairwise commuting square-one elements. Because \(2\) is invertible, for each \(\epsilon=(\epsilon_1,\ldots,\epsilon_k)\in\{\pm1\}^k\), put
\[
 e_\epsilon=2^{-k}\prod_{i=1}^k(1+\epsilon_i a_i).
\]
The \(e_\epsilon\) are pairwise orthogonal idempotents summing to \(1\), and \(a_i=\sum_\epsilon\epsilon_i e_\epsilon\). At each diagonal position \(x\in P\), exactly one \(e_\epsilon(x,x)\) equals \(1\); all others vanish. Thus the tuple determines a unique labeling \(c:P\to\{\pm1\}^k\), i.e. a \(Q\)-coloring.

**Unipotent simultaneous diagonalization.** For fixed coloring, let \(d_\epsilon\) be the diagonal idempotent with a \(1\) precisely at positions of color \(\epsilon\). Define \(u=\sum_\epsilon e_\epsilon d_\epsilon\). Its diagonal entries are all \(1\), so \(u\in1+J(A)\) is invertible. Orthogonality gives \(e_\epsilon u=ud_\epsilon\), hence \(e_\epsilon=ud_\epsilon u^{-1}\) and \(a_i=u(\sum_\epsilon\epsilon_i d_\epsilon)u^{-1}\). Conversely, any such conjugate tuple has the required commutation and square-one properties. Different colorings yield disjoint sets of tuples because conjugation by \(1+J(A)\) preserves diagonal entries.

**Orbit size.** The group \(U=1+J(A)\) has size \(q^m\). An element \(u\in U\) centralizes the diagonal tuple precisely when its coefficient \(u(x,y)\) vanishes at every strict comparable pair \(x<y\) with \(c(x)\ne c(y)\). Indeed, its commutator with the \(i\)-th diagonal generator has \((x,y)\)-entry \(u(x,y)(\epsilon_i(y)-\epsilon_i(x))\); at least one difference is a nonzero field element exactly when the colors differ. If \(d(c)\) denotes the number of differently colored comparable pairs, the stabilizer size is \(q^{m-d(c)}\), hence the orbit contains \(q^{d(c)}\) tuples. Summing over all colorings proves the first formula.

**Random-cluster expansion.** The edge weight is \(q\) when endpoint colors differ and \(1\) when they agree. Rewrite it as \(q+(1-q)\mathbf1_{c(x)=c(y)}\), multiply over the \(m\) edges and expand. A selected edge subset \(F\) forces a constant color on each of its \(\kappa(F)\) components and admits exactly \(Q^{\kappa(F)}\) colorings. This proves the second formula, including \(k=0\).

**Maximal cliques.** Any set of pairwise commuting involutions generates a finite elementary abelian \(2\)-subgroup, whose generators can be simultaneously diagonalized by the preceding construction. Therefore every clique lies in a conjugate of the full diagonal sign subgroup \(D\cong(C_2)^n\). All these conjugates have \(2^n\) elements and are therefore maximal; there can be no larger clique. The conjugation action of \(U\) on \(D\) is free: if \(uDu^{-1}=D\), then every diagonal of \(udu^{-1}\) equals that of \(d\), forcing \(udu^{-1}=d\) for all \(d\in D\). Since the diagonal signs separate any distinct \(x,y\), this forces every strict offdiagonal coefficient of \(u\) to vanish. Thus \(u=1\). Consequently the number of distinct conjugates is exactly \(|U|=q^m\).

**Clique-size, Tutte and chromatic consequences.** Let \(f_r\) count commuting sets of \(r\) different involutions. An ordered commuting \(k\)-tuple has an underlying commuting set of \(r\) elements, with \(r!S(k,r)\) surjections from the \(k\) labeled positions onto them. Hence \(C_k=\sum_{r\le k}r!S(k,r)f_r\); Stirling inversion yields the displayed formula. To recover the random-cluster polynomial, fix an odd \(q\). As \(k\) varies, the distinct unbounded integers \(Q=2^k\) determine its polynomial in \(Q\) at \(v=q^{-1}-1\). Varying \(q\) over infinitely many odd prime powers gives infinitely many \(v\) values, determining each coefficient as a polynomial in \(v\). The standard change of variables yields the Tutte polynomial. Finally, divide the color sum by \(q^m\): each coloring having at least one monochromatic edge contributes a negative power of \(q\), whereas each proper coloring contributes \(1\), proving the chromatic limit.

## Verification
A standalone standard-library program `verify.py` constructs incidence-algebra matrices and multiplies them explicitly. It exhaustively checks all square-one elements and commuting pairs/triples for chains, two fork orientations, disjoint chains over \(\mathbb F_3\), and a three-chain over \(\mathbb F_5\); it also independently verifies the random-cluster identity in 36 finite parameter tests. Execute `python verify.py` to reproduce the tests. The formal proof above covers all finite posets and odd prime-power fields; these finite enumerations are corroboration, not an infinite proof.

## Relationship to prior work
Gargate and Gargate (2019, arXiv:1907.06805v1) enumerate **individual** involutions in incidence algebras, including general finite-poset cases. Their \(k=1\) enumeration and diagonal-sign philosophy are prior results, not claimed independently here. Their subsequent work (2020, arXiv:2009.04243v1) counts individual matrices satisfying higher polynomial equations in triangular and incidence algebras. The new assessed result is the joint all-arity commutation enumeration over every odd field, its exact maximal-clique conjugacy classification, and the comparison with random-cluster/chromatic/Tutte invariants. In particular, individual involution counts do not imply a general count of commuting pairs or triples in a fixed algebra. The use of unipotent conjugacy of split semisimple diagonal idempotents is standard; the theorem does not claim discovery of that principle. Existing finite-field classification methods may contain implications not yet identified, so priority is provisional.

## Limitations
Characteristic \(2\) is excluded. The full bivariate Tutte polynomial is recovered from the family of spectra varying \(q\), **not** from a single fixed \(q\). The theorem neither recovers a poset from its comparability graph nor classifies arbitrary noninvolutive commuting tuples. The independent literature review is not an exhaustive guarantee of publication priority. No independent mathematical audit has been performed.

## References
- Y. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805v1, first public version 2019-07-16; https://arxiv.org/abs/1907.06805 .
- Y. Gargate and M. Gargate, *(k+1)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243v1, first public version 2020-08-30; https://arxiv.org/abs/2009.04243 .
- Standard Fortuin–Kasteleyn random-cluster expansion and Tutte-polynomial identities are used as established graph-theoretic background.
