# Canonical two-step normal form and census of finite modal splitting templates

## Finding

Let \(\mathfrak A=(\mathcal P([n]),\Box)\) be a finite, nontrivial normal modal algebra with \(n\ge1\) **Boolean atoms** (so its Boolean reduct has \(2^n\) elements). Suppose \(\Box^3 0=1\). Then \(\mathfrak A\) is subdirectly irreducible precisely when its unique dual finite Kripke relation is a directed acyclic graph with a single source and no directed path of three edges.

For \(n\ge2\), every such frame has one and only one decomposition \([n]=\{r\}\sqcup B\sqcup C\) with \(B\ne\varnothing\), characterized as follows: \(r\) is the source; every \(r\to b\) for \(b\in B\) is present; each \(c\in C\) has an arbitrary **nonempty** parent set \(P(c)\subseteq B\) and independently an optional edge \(r\to c\); there are no other edges. Here \(B\) comprises exactly those nonroot vertices that are not the endpoint of a two-edge path, and \(C\) consists of the endpoints of such paths.

The number of these normal modal operations on a **fixed labeled** Boolean atom set is \(L_1=1\), and for every integer \(n\ge2\),
\[
L_n=n\sum_{k=1}^{n-1}\binom{n-1}{k}\left(2(2^k-1)\right)^{n-1-k}.
\]

The isomorphism types admit a complete multiset classification. For fixed \(k=|B|\ge1\) and \(m=|C|=n-1-k\), put
\[
T_k=(\mathcal P([k])\setminus\{\varnothing\})\times\{0,1\}.
\]
Isomorphism types of this layer-size pair are exactly the orbits of size-\(m\) multisets of \(T_k\) under the natural \(S_k\) action on the subset coordinate. If \(\operatorname{Cyc}(\sigma,T_k)\) denotes the cycles of this action, their total number is \(U_1=1\) and
\[
U_n=\sum_{k=1}^{n-1}\frac1{k!}\sum_{\sigma\in S_k}
[t^{n-1-k}]\prod_{Q\in\operatorname{Cyc}(\sigma,T_k)}
\frac1{1-t^{|Q|}}\quad(n\ge2).
\]
The first labeled counts \((L_1,\ldots,L_8)\) are \((1,2,15,124,1525,26106,618695,20279288)\); the first isomorphism counts \((U_1,\ldots,U_8)\) are \((1,1,3,8,24,77,283,1182)\).

## Assumptions and scope

A normal modal algebra here is a Boolean algebra with a unary operation \(\Box\) preserving finite meets and \(1\). Its dual additive operator is \(\Diamond a=\neg\Box\neg a\). Every such algebra with \(n\) atoms can be represented uniquely as the complex algebra of a binary relation \(R\subseteq[n]^2\), with
\[
\Box_R A=\{x\in[n]:R[x]\subseteq A\},\qquad
\Diamond_R A=\{x\in[n]:\exists y\in A\ (xRy)\}.
\]
The empty path has length zero. A source is a vertex with indegree zero. Paths of length three mean directed walks of three edges; the absence of such walks also excludes loops and all directed cycles. Isomorphism allows relabeling Boolean atoms, equivalently relabeling vertices. The empty Boolean algebra is excluded. The case \(n=1\) is included separately.

## Proof

**1. Height restriction.** By direct modal duality, for every integer \(j\ge1\), the set \(\Diamond_R^j[n]\) is the set of vertices at the beginning of an \(R\)-walk of length \(j\). Since \(\neg\Box_R^j0=\Diamond_R^j1\), the identity \(\Box_R^3 0=1\) holds exactly when \(R\) has no length-three walk. A finite relation with this property is acyclic, since repeating a directed cycle supplies length-three walks.

**2. Subdirect irreducibility.** For a finite Boolean powerset algebra, congruence zero-classes are Boolean ideals \(I_U=\mathcal P(U)\), where \(U\subseteq[n]\). Such an ideal is a modal congruence ideal precisely when \(\Diamond_R U\subseteq U\), i.e., \(U\) is predecessor-closed: \(y\in U\) and \(xRy\) imply \(x\in U\). A nontrivial finite algebra is subdirectly irreducible exactly when the family of nonzero congruence ideals has a least member. In an acyclic frame, every nonempty predecessor-closed set contains a source (follow incoming edges backward). If there are two sources, their singletons supply incomparable minimal nonzero ideals. If there is exactly one source \(r\), its singleton is predecessor-closed and every nonempty predecessor-closed set contains it. Thus subdirect irreducibility is equivalent to a unique source. In a finite acyclic graph with one source, every vertex is reachable from that source.

**3. Canonical structure.** For \(n\ge2\), let \(B\) comprise vertices of positive distance one but no path of length two from \(r\). Every other nonroot vertex belongs to \(C\) and is reached by a two-edge path. If \(b\in B\), any predecessor of \(b\) other than \(r\) would create a two-edge path from \(r\) to \(b\); therefore \(r\) is its only parent. For \(c\in C\), any edge from \(c\) onward would extend a two-edge path to length three; therefore all such vertices are terminal. Its nonroot parents must belong to \(B\), and there is at least one. The source-to-terminal edge is unconstrained. There are no edges within \(B\), within \(C\), or from \(C\). Conversely, every relation specified by these data has a unique source and no length-three walk. Both the partition and the data are intrinsic, proving uniqueness.

**4. Labeled enumeration.** Select \(r\) in \(n\) ways and a \(k\)-element set \(B\) among its \(n-1\) other vertices. The \(n-1-k\) labeled vertices of \(C\) each have \(2^k-1\) nonempty parent subsets and two independent root-shortcut choices. Multiplication and summation yield \(L_n\). The one-atom case has only the empty relation.

**5. Isomorphism enumeration.** Once \(r\) and \(B,C\) are intrinsic, permutations of \(B\) induce the full symmetric-group action on nonempty parent subsets. Permuting \(C\) amounts to forgetting their labels and retaining their multiset of parent-set/shortcut-bit types. Therefore isomorphism classes with parameters \((k,m)\) are exactly the stated multiset orbits. A multiset fixed by \(\sigma\in S_k\) assigns equal multiplicities along each cycle \(Q\) of the induced action on \(T_k\); its fixed-multiset generating function is \(\prod_Q(1-t^{|Q|})^{-1}\). Taking coefficient \([t^m]\) and averaging over \(S_k\) by Burnside's lemma proves the displayed formula, including all values of \(k\) from \(1\) to \(n-1\).

## Verification

The standalone standard-library program `verify.py` checks the algebraic definition independently of the constructive normal form. For each \(1\le n\le4\), it examines **every** one of the \(2^{n^2}\) binary relations, including loops and cycles; tests the no-three-walk condition; explicitly enumerates all predecessor-closed Boolean congruence ideals to decide subdirect irreducibility; and compares the resulting relation set with an independent constructor using \((r,B,C)\). Counts are \(1,2,15,124\). For each qualifying relation it also computes an isomorphism canonical form by vertex permutations and compares the resulting \(1,1,3,8\) counts with the independent Burnside formula. Additional exact evaluations of the two formulas cover \(5\le n\le8\). Running `python3 verify.py` prints `VERIFY_OK` on success.

These finite calculations are falsification tests only; the universal statements for arbitrary finite \(n\) follow from the proofs above.

## Relationship to prior work

Takahashi's *Decidability of Being a Union-splitting* (first arXiv version 2025-10-16, Theorem 2.7 and Section 3) uses the full class of finite subdirectly irreducible modal algebras of finite height as Jankov splitting templates and gives decision procedures; it does not state the present canonical parent-set/shortcut data or their labeled and isomorphism counting laws. Venema's *Duals of subdirectly irreducible modal algebras* explains the finite-complex-algebra rootedness criterion and proves a broader dual characterization; its result supplies the algebraic starting point, not the height-two multiset orbit enumeration. General directed-acyclic-graph enumeration such as McKay's asymptotic work concerns wider graph families and does not directly yield the height-restricted isomorphism formula. The new classification explicitly organizes the first non-star height of these modal splitting templates.

## Limitations

The theorem enumerates **template algebras**, not necessarily pairwise distinct Jankov splitting logics. It does not classify all finite heights or the unbounded-height case, and the normal form fails in general if the restriction \(\Box^3 0=1\) is dropped. The formula for isomorphism types is a finite Burnside sum, not an asymptotic expansion. Exhaustive checks stop at four atoms, and exact formula evaluations through eight atoms are not a substitute for the general proof. Search coverage cannot rule out every independently developed equivalent graph-enumeration formula.

## References

1. Tenyo Takahashi, *Decidability of Being a Union-splitting*, arXiv:2510.14520v1 (first posted 2025-10-16); *Journal of Symbolic Logic* (published online 2026-02-10), doi:10.1017/jsl.2026.10187. https://arxiv.org/abs/2510.14520 ; https://doi.org/10.1017/jsl.2026.10187.
2. Yde Venema, *Duals of subdirectly irreducible modal algebras* (2002), ILLC PP-2002-10. https://eprints.illc.uva.nl/id/eprint/74/2/PP-2002-10.text.pdf.
3. Brendan D. McKay, *On the shape of a random acyclic digraph*, *Mathematical Proceedings of the Cambridge Philosophical Society*, doi:10.1017/S0305004100068195.
