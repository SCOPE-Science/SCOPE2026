# A topological boundary for preferred extensions of countable finitary argumentation frameworks

## Finding
For a countable Dung framework \(\mathcal F=(A,R)\), with finite attacker sets at each argument, the collection \(\operatorname{Adm}(\mathcal F)\) is closed in the product Cantor space \(2^A\), and \(\operatorname{Pref}(\mathcal F)\), the set of inclusion-maximal admissible sets, is \(G_\delta\) there. This is a Borel topological bound for the family of extensions of a *fixed* framework, not a claim about the computability of deciding whether an input framework has an extension. In any countable locally finite *symmetric irreflexive* framework the preferred family is also closed. In contrast, there exists an explicit computable framework with at most three incoming and at most three outgoing attacks per vertex whose preferred family is not closed. Indeed its admissible sets form a convergent sequence with its limit and its preferred sets are exactly the sequence without its limit.

## Assumptions and scope
A framework is a pair \((A,R)\) with \(R\subseteq A\times A\), interpreted as attacks. A set \(S\subseteq A\) is conflict-free if it contains no attacking pair. It defends its member \(a\) if every attacker \(bRa\) is in turn attacked by a member \(c\in S\). An admissible set is conflict-free and defends every member. A preferred extension is an inclusion-maximal admissible set. Finitary means \(\{b:bRa\}\) is finite for every \(a\). Local finiteness means both attacker and outgoing-neighbor sets are finite. The set \(A\) is finite or countably infinite, and \(2^A=\{0,1\}^A\) has the coordinatewise product topology. All claims use ordinary classical set theory; no effective descriptive-set-theoretic completeness is asserted.

## Proof
**Closed admissibility.** For each attacking pair \((a,b)\), requiring that not both arguments belong to \(S\) is a clopen condition. For every argument \(a\), admissibility also requires the implication
\[
 a\in S\ \Longrightarrow\ \bigwedge_{bRa}\ \bigvee_{cRb}(c\in S).
\]
The conjunction is finite because \(\operatorname{Att}(a)\) is finite, and each disjunction is finite because \(\operatorname{Att}(b)\) is finite. Each such implication is clopen. The intersection over all pairs and all arguments is therefore closed. As \(2^A\) is compact, so is \(C=\operatorname{Adm}(\mathcal F)\).

**Preferred sets are \(G_\delta\).** For each \(a\in A\), define
\[
K_a=\{(S,T)\in C\times C:S\subseteq T,\ a\notin S,\ a\in T\}.
\]
The inclusion relation is closed (a coordinatewise intersection of clopen constraints). Thus \(K_a\) is compact, and its first-coordinate projection \(P_a\) is closed. A member of \(C\) is nonmaximal precisely when it belongs to some \(P_a\). Consequently
\[
\operatorname{Pref}(\mathcal F)=C\setminus\bigcup_{a\in A}P_a.
\]
This is \(G_\delta\) in \(C\), hence also in the ambient metrizable Cantor space: use the fact that closed subsets of a metric space are \(G_\delta\) and intersections of two \(G_\delta\) sets are \(G_\delta\). Equivalently, \(C\setminus P_a\) is relatively open in \(C\), and the closed set \(C\) itself is ambient \(G_\delta\).

**Closed preferred sets under undirected attacks.** Suppose \(R\) is symmetric, irreflexive and locally finite. A conflict-free set automatically defends every member: any attack on \(a\in S\) is counterattacked by \(a\). Hence admissible sets are exactly independent sets of the underlying locally finite simple graph. An independent set is maximal if and only if it dominates every vertex: for each \(a\), either \(a\in S\) or some neighbor of \(a\) lies in \(S\). Each of these local conditions is clopen because neighborhoods are finite. Intersecting them with the closed independent-set condition proves preferred sets are closed.

**Directed bounded-degree counterexample.** Introduce the core arguments \(a_{n,k}\) and the auxiliary self-attacking arguments \(u_{n,k}\) for all \(n,k\in\mathbb N\), and \(d_{n,k}\) for \(n\in\mathbb N\), \(k\ge1\). Include all and only the following attacks, in addition to their explicitly named converses:

1. \(u_{n,k}\to u_{n,k}\), \(u_{n,k}\to a_{n,k}\), and \(a_{n,k+1}\to u_{n,k}\), for all \(n,k\).
2. \(d_{n,k}\to d_{n,k}\), \(d_{n,k}\to a_{n,k}\), and \(a_{n,k-1}\to d_{n,k}\), for all \(n\) and \(k\ge1\).
3. For every unordered pair \(\{n,m\}\) of different row indices, include the two mutual attacks between \(a_{n,j_n(m)}\) and \(a_{m,j_m(n)}\), where \(j_n(m)=m\) for \(m<n\) and \(j_n(m)=m-1\) for \(m>n\). Thus \(j_n\) bijects \(\mathbb N\setminus\{n\}\) onto \(\mathbb N\).

No auxiliary argument belongs to a conflict-free set because of its self-loop. If an admissible set contains \(a_{n,k}\), defending it against \(u_{n,k}\) forces \(a_{n,k+1}\); for \(k\ge1\), defending against \(d_{n,k}\) forces \(a_{n,k-1}\). Indeed the other attacker of either auxiliary vertex is its own forbidden self-loop. Therefore inclusion of any core argument forces inclusion of the whole row \(E_n=\{a_{n,k}:k\in\mathbb N\}\). Every pair of different rows has a mutual attack by rule 3, so an admissible set contains at most one whole row.

Each \(E_n\) is admissible: it is conflict-free; it counterattacks each auxiliary attacker of its elements by the preceding and succeeding row elements, and its unique external attacker of each element is counterattacked by that very element, since every cross-row attack is mutual. The empty set is also admissible. Thus
\[
\operatorname{Adm}(\mathcal F)=\{\varnothing\}\cup\{E_n:n\in\mathbb N\},\qquad \operatorname{Pref}(\mathcal F)=\{E_n:n\in\mathbb N\}.
\]
Every argument has at most three incoming and at most three outgoing attacks: a core vertex has at most two incoming auxiliary attacks and one cross-row attack, and sends attacks to at most its predecessor/successor auxiliaries and one cross-row partner; a self-loop auxiliary has one self-loop and at most one other incident attack in each direction. All edge predicates and complete finite attacker lists are computable using the displayed formulas. Finally, the \(E_n\) are pairwise disjoint and hence converge coordinatewise to \(\varnothing\), which is not preferred. This proves nonclosure despite a uniform degree bound.

## Verification
The standalone `checker.py` enumerates finite cyclic analogues with two, three, and four core rows, using cyclic predecessor/successor enforcers. It independently enumerates all \(2^{rp}\) eligible core subsets for \((r,p)=(2,2),(3,3),(4,4)\), checks attacker-closure and degrees, and finds exactly the empty set and the \(r\) complete rows admissible, with precisely the rows maximal. These are finite analogues, not finite truncations of the infinite construction; they only corroborate the local argument. The infinite claims are established by the explicit forcing argument and compactness proof above.

## Relationship to prior work
Xu and Luo (2026, arXiv:2610.12008), Section 5, study the computability complexity of decision problems for preferred semantics in computably finitary frameworks, using finitely branching computation trees. Their results concern complexity across input frameworks, rather than the topological family of preferred extensions inside one fixed Cantor space. Andrews and San Mauro (2025, arXiv:2508.16986) establish foundational computational restrictions of finitary infinite frameworks and present paths through trees for admissibility-based semantics; this is compatible with our closed-admissibility observation, but they do not state this combined \(G_\delta\)/closed/nonclosed trichotomy or the degree-three counterexample. Elaroussi et al. (2022, arXiv:2202.05506) study maximality in finite frameworks, which cannot detect the nonclosed sequence phenomenon. The proof of the abstract compact-family maximality lemma uses elementary topology; originality is not asserted for that lemma independently of the preferred-semantics contrast and bounded-degree construction.

## Limitations
No optimality is asserted for the degree-three bound; a smaller-degree construction might exist. No \(G_\delta\)-completeness, uniform algorithm for deciding preferred status, or complexity classification for varying framework codes is claimed. The literature comparison cannot exclude an older theorem on maximal subsets of compact families or an argumentation example under different terminology. Full independent audit has not been performed.

## References
1. J. Xu and J. Luo, *Complexity of Grounded Semantics and Preferred Semantics in Finitary Argumentation Frameworks* (first made public 2026-10-08), arXiv:2610.12008, https://arxiv.org/abs/2610.12008.
2. U. Andrews and L. San Mauro, *Complexity in Finitary Argumentation (extended version)* (2025), arXiv:2508.16986, https://arxiv.org/abs/2508.16986.
3. M. Elaroussi et al., *On the preferred extensions of argumentation frameworks: bijections with naive sets* (2022), arXiv:2202.05506, https://arxiv.org/abs/2202.05506.
4. P. M. Dung, *On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games*, Artificial Intelligence 77 (1995), 321–357.
