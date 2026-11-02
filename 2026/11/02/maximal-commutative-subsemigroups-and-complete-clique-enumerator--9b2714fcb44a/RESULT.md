# Maximal commutative subsemigroups and complete clique enumerators of finite Brandt semigroups

## Finding

Let \(G\) be any finite group of order \(m\), let \(n\geq2\), and let \(B_n(G)\) be the Brandt semigroup on \([n]\times G\times[n]\), with an additional zero. Its commuting graph \(\Delta_n(G)\) has all nonzero elements as vertices and joins distinct commuting elements. The central zero is deliberately excluded.

Let \(\operatorname{MaxAb}(G)\) be the set of inclusion-maximal abelian subgroups of \(G\), and define
\[
A_G(y)=\sum_{H\in\operatorname{MaxAb}(G)}y^{|H|},\qquad
P_G(z)=\sum_{X\subseteq G\, :\, ab=ba\;\forall a,b\in X}z^{|X|}.
\]
The empty subset is included in \(P_G\). Write \(h=|\operatorname{MaxAb}(G)|\) and \(a=\max_{H\in\operatorname{MaxAb}(G)}|H|\).

**Structure and maximal-clique enumerator.** Every inclusion-maximal clique is uniquely of one of these forms:

1. For each \(i\in[n]\), choose a maximal abelian subgroup \(H_i\leq G\) and take all \((i,g,i)\) with \(g\in H_i\).
2. Partition \([n]=S\sqcup T\sqcup U\) with \(S,T\ne\varnothing\). For each \(u\in U\), choose a maximal abelian subgroup \(H_u\leq G\); take all \((u,g,u)\) with \(g\in H_u\), together with **all** \((s,g,t)\) for \(s\in S\), \(t\in T\), and \(g\in G\).

Each clique, with zero adjoined, is a maximal commutative subsemigroup. If \(M_{n,G}(y)\) counts inclusion-maximal cliques according to their number of nonzero vertices, then
\[
M_{n,G}(y)= A_G(y)^n+
\sum_{\substack{s,t\geq1\\s+t\leq n}}
\binom{n}{s,t,n-s-t}y^{mst}A_G(y)^{n-s-t}.
\]
In particular, the **exact number** of maximal commutative subsemigroups is
\[
\boxed{M_{n,G}(1)=(h+2)^n-2(h+1)^n+2h^n},
\]
and the clique number is
\[
\boxed{\omega(\Delta_n(G))=\max\left\{na,\;m\left\lfloor\frac{n^2}{4}\right\rfloor\right\}}.
\]

**All-clique enumerator.** For integers \(s,t\geq1\), put
\[
F^{(m)}_{s,t}(z)=
\sum_{i=0}^{s}\sum_{j=0}^{t}
(-1)^{s+t-i-j}\binom{s}{i}\binom{t}{j}(1+z)^{mij}.
\]
The complete polynomial \(C_{n,G}(z)=\sum_{r\geq0}c_r z^r\), where \(c_r\) is the number of \(r\)-element subsets of pairwise-commuting **nonzero** elements, is
\[
\boxed{C_{n,G}(z)=P_G(z)^n+
\sum_{\substack{s,t\geq1\\s+t\leq n}}
\binom{n}{s,t,n-s-t}P_G(z)^{n-s-t}F^{(m)}_{s,t}(z)}.
\]
The full-element commuting graph, with the zero included, has clique polynomial \((1+z)C_{n,G}(z)\).

For abelian \(G\), one has \(h=1\) and therefore precisely \(3^n-2^{n+1}+2\) maximal commutative subsemigroups, independently of the isomorphism type and even the order of \(G\). Moreover, if two nonisomorphic finite abelian groups have the same order, their Brandt semigroups have isomorphic commuting graphs but are nonisomorphic as semigroups: for example \(B_2(C_4)\) and \(B_2(C_2\times C_2)\).

## Assumptions and scope

The group \(G\) is arbitrary but finite, not necessarily abelian. The index-set size satisfies \(n\geq2\). Multiplication is
\[
(i,g,j)(k,h,l)=\begin{cases}(i,gh,l),&j=k,\\0,&j\ne k,\end{cases}
\]
and zero annihilates everything. In this range the center of \(B_n(G)\) is exactly \(\{0\}\). The graph \(\Delta_n(G)\) is the standard semigroup commuting graph on noncentral elements, with no loops. A clique is a set of distinct elements, unlike an ordered commuting tuple; the polynomials above count subsets, not repeated selections. All powers and polynomial identities are over the integers. The terms “maximal” and “maximum” are distinct: maximal means inclusion-maximal; the clique number concerns maximum cardinality.

## Proof

**Step 1: Exact commutation rules.** For distinct nonzero diagonal elements \((i,g,i)\) and \((j,h,j)\), if \(i\ne j\) both products are zero; if \(i=j\), they commute precisely when \(gh=hg\). A diagonal element at index \(u\) commutes with the offdiagonal element \((i,g,j)\), \(i\ne j\), precisely when \(u\notin\{i,j\}\). Two offdiagonal elements \((i,g,j)\) and \((k,h,l)\) commute exactly when \(j\ne k\) and \(l\ne i\). Indeed, in this case both products are zero. Otherwise at least one is nonzero; if both are nonzero, then \(k=j\), \(l=i\) and the two products lie in distinct diagonal positions \(i\) and \(j\), so cannot be equal. Consequently, group labels never affect commutation between offdiagonal elements.

**Step 2: All maximal cliques.** Associate to each chosen offdiagonal element \((i,g,j)\) the directed arc \(i\to j\). Step 1 prohibits any index from being both the source of one selected arc and the target of another. Thus, if an offdiagonal element is selected, its set \(S\) of sources and set \(T\) of targets are disjoint, nonempty, and uniquely determined by the chosen elements. No diagonal elements can occur at indices of \(S\cup T\). At any index of the complementary set \(U\), the selected diagonal elements form a commuting subset of \(G\). Such a clique can always be enlarged by adding any missing element of an offdiagonal label fiber \(\{(s,g,t):g\in G\}\) for \((s,t)\in S\times T\), and by extending each diagonal commuting subset at an unused index. Hence maximality forces *all* offdiagonal fibers in \(S\times T\) and a maximal commuting subset of \(G\) at each \(u\in U\). Conversely, the resulting clique is maximal: every excluded diagonal element fails to commute with the maximal subgroup at its index or touches a selected offdiagonal arc; every excluded offdiagonal element has an endpoint in \(U\), contradicting its occupied diagonal subgroup, or has the opposite orientation or a source/target collision. With no selected offdiagonal elements, maximality forces a maximal commuting subset at every diagonal index.

A maximal pairwise-commuting subset \(H\subseteq G\) is a maximal abelian subgroup: the subgroup generated by its elements is abelian and still commutes with \(H\), so maximality forces equality. The same elementary closure argument works in any semigroup: a product of two elements commuting with every member of a pairwise-commuting set also commutes with every member. Thus each maximal clique becomes, upon adjoining zero, a maximal commutative subsemigroup. This proves both structural cases and their uniqueness.

**Step 3: Count and size the maximal cliques.** For the all-diagonal case the maximal-clique size polynomial is \(A_G(y)^n\). For a fixed ordered partition \((S,T,U)\) with sizes \((s,t,u)\), the complete offdiagonal block contributes \(mst\) elements and the independent diagonal choices contribute \(A_G(y)^u\). There are \(\binom{n}{s,t,u}\) such partitions. Summing gives \(M_{n,G}(y)\). Setting \(y=1\) and using the binomial theorem, the mixed cases count
\[
\sum_{u=0}^{n-2}\binom n u h^u(2^{n-u}-2)
=(h+2)^n-2(h+1)^n+h^n.
\]
Adding the \(h^n\) all-diagonal cases yields the displayed count. The largest possible clique with \(s+t=x\) has size at most \((n-x)a+m\lfloor x^2/4\rfloor\). The first differences of \(\lfloor x^2/4\rfloor\) are \(\lfloor(x+1)/2\rfloor\), a nondecreasing sequence, so this upper bound is discretely convex in \(x\) and maximized at \(x=0\) or \(x=n\). Both endpoint values occur (all diagonal; balanced complete source-sink block). This proves the clique-number formula.

**Step 4: Count every clique.** The cliques with no offdiagonal elements contribute \(P_G(z)^n\). For a clique containing offdiagonal elements, define \(S,T\) as its *occupied* source and target sets, rather than arbitrary supersets; this makes the classification unique. At each of the \(st\) possible directed pairs in \(S\times T\), the \(m\) distinct group-labeled elements may independently be selected or omitted, contributing \((1+z)^m\). All vertices of \(S\) must have positive outdegree and all vertices of \(T\) positive indegree. Inclusion–exclusion over isolated source and target vertices gives exactly \(F^{(m)}_{s,t}(z)\). Each unused index in \(U\) independently contributes a commuting subset of \(G\), counted by \(P_G(z)\). Multiplying and summing over unique ordered partitions yields the claimed complete polynomial, including the empty clique from the diagonal-only term. Since zero commutes with everything, adjoining zero multiplies this polynomial by \(1+z\).

**Step 5: Nonreconstruction.** If \(G\) is abelian, whether two nonzero Brandt elements commute depends only on their index positions, except that two elements in the same diagonal fiber always commute. For two same-order abelian groups, any bijection of the group-label sets induces a commuting-graph isomorphism. But a semigroup isomorphism must send each nonzero maximal subgroup at an idempotent to a corresponding maximal subgroup, hence induce a group isomorphism. Taking cyclic and elementary abelian groups of order four proves the example.

## Verification

The accompanying `verify.py` computes multiplication directly in each finite Brandt semigroup, builds its undirected commuting graph, enumerates *all* cliques (including the empty clique), identifies inclusion-maximal cliques by checking possible extensions, and independently computes the two predicted polynomials using integer polynomial arithmetic and inclusion–exclusion. It checks ten finite configurations: trivial groups at three index sizes, cyclic groups of orders two through four, the Klein four group, and the nonabelian symmetric group of degree three. It also directly compares every ordered element pair under the label-bijection between the cyclic and Klein groups of order four at index size two. Running `python verify.py` prints `VERIFY_OK` if all comparisons succeed. These are finite checks, not a substitute for the all-group proof above.

For example, the aperiodic semigroup at \(n=4\) has exactly \(51\) maximal commutative subsemigroups: \(44\) have three nonzero elements and \(7\) have four. For \(B_2(S_3)\), the maximal-clique size polynomial is \(9y^4+6y^5+3y^6\), giving \(18\) maximal commutative subsemigroups of different sizes. These values are checked independently by multiplication.

## Relationship to prior work

Kumar, Dalal and Pandey (2020) explicitly determine the commuting-graph clique number of the aperiodic Brandt semigroup and identify balanced source-sink blocks attaining its maximum; their Lemma 3.10 supplies the disjoint-source/target observation for *maximum-size* cliques. Those observations are foundational and not claimed as new. The present result concerns **every inclusion-maximal clique** for arbitrary finite structure groups, the complete size distribution of maximal commutative subsemigroups, and every clique coefficient. These are not consequences of merely knowing the clique number. Margolis, Rhodes and Silva (2017) identify the general subsemigroup lattice of the aperiodic Brandt semigroup with transitive relations and study a different subsemigroup complex; those foundational identifications are acknowledged, but do not state the two enumerators above. Related work on Rees matrix commuting graphs studies different products and graph invariants. The relationship is supported by direct comparison with the cited available primary mathematical texts; it does not establish publication priority.

## Limitations

The classification concerns finite Brandt semigroups and does not automatically extend to arbitrary Rees sandwich matrices or to infinite structure groups. The explicit formulas depend on the commuting-subset and maximal-abelian-subgroup enumerators of \(G\), which may themselves be difficult to determine for large groups. The full-clique polynomial counts pairwise-commuting subsets, not all commutative subsemigroups; only its maximal-clique classification automatically identifies maximal commutative subsemigroups. Computational checks cover finitely many small cases. A broader previously published classification of commutative subsemigroups of completely zero-simple inverse semigroups could imply some statements; novelty and publication priority have not been independently certified.

## References

1. J. Kumar, S. Dalal and P. Pandey, *On the commuting graphs of Brandt semigroups*, arXiv:2010.05000 (first public version 10 October 2020), especially Lemma 3.10 and Theorem 3.14. https://arxiv.org/abs/2010.05000
2. S. Margolis, J. Rhodes and P. V. Silva, *On the subsemigroup complex of an aperiodic Brandt semigroup*, arXiv:1705.04956 (14 May 2017), especially Section 5. https://arxiv.org/abs/1705.04956
3. *Commuting graphs of Rees matrix semigroups*, *Semigroup Forum*, DOI:10.1007/s00233-025-10597-0 (2025), particularly the definitions and Theorem 3.7. https://doi.org/10.1007/s00233-025-10597-0
