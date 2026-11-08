# Catalan classification and maximal-clique size spectrum of type-A 0-Hecke idempotents

## Finding

For each integer \(m\ge1\), let \(H_m=H_0(S_{m+1})\) be the type-A 0-Hecke monoid, and let \(\Gamma_m\) be the graph whose vertices are **monoid idempotents** and whose edges join distinct commuting idempotents. For \(I\subseteq[m]\), let \(e_I\) be the longest parabolic element on the generators indexed by \(I\), including \(e_\varnothing=1\). All monoid idempotents are of this form.

The inclusion-maximal cliques of \(\Gamma_m\) are in canonical bijection with binary search trees \(T\) on the ordered keys \([m]\). The corresponding clique is
\[
\mathcal C(T)=\{e_I:I\in J(T)\},
\]
where \(J(T)\) is the order-ideal lattice of the partial order in which every descendant lies below its ancestors. Multiplication on each clique is union of supports, so \(\mathcal C(T)\) is a semilattice isomorphic to \(J(T)\). In particular, there are exactly \(C_m=\binom{2m}{m}/(m+1)\) inclusion-maximal cliques.

Let \(f_m(s)\) count those cliques with exactly \(s\) vertices, with \(f_0(1)=1\) and all other \(f_0(s)=0\). The complete size spectrum satisfies
\[
\boxed{f_m(s)=\sum_{i=0}^{m-1}\ \sum_{\substack{a,b\ge1\\ ab=s-1}} f_i(a)f_{m-1-i}(b).}
\]
Its minimum size is \(m+1\), attained by exactly \(2^{m-1}\) cliques, and its maximum \(M_m\) satisfies
\[
M_0=1,\qquad M_m=1+\max_{0\le i<m}M_iM_{m-1-i}.
\]
For example \(f_4(5)=8\), \(f_4(6)=2\), and \(f_4(7)=4\), with no other nonzero values.

## Assumptions and terminology

The 0-Hecke generators satisfy \(\pi_i^2=\pi_i\), \(\pi_i\pi_j=\pi_j\pi_i\) for \(|i-j|>1\), and the usual adjacent braid relations. The product is the Demazure product: appending a simple transposition changes the permutation if Coxeter length increases and otherwise leaves it unchanged. An idempotent is an element satisfying \(e*e=e\), not a linear idempotent in the monoid algebra. A clique is *inclusion-maximal*, not necessarily of largest size; no claim is made about commutative submonoids containing nonidempotents. The empty key set corresponds to one empty search tree whose order-ideal lattice has one element.

## Proof

**Idempotent supports and their commutation.** Standard Demazure-monoid theory classifies the idempotents as the parabolic longest elements \(e_I\), uniquely determined by their supports. We first prove, for all \(I,J\subseteq[m]\),
\[
 e_I*e_J=e_J*e_I\quad\Longleftrightarrow\quad
 \text{each connected component of }I\cup J\text{ in the path on }[m]
 \text{ lies entirely in }I\text{ or entirely in }J.
\]
In that case both products equal \(e_{I\cup J}\). If \(e_I\) and \(e_J\) commute, their product is idempotent and has support \(I\cup J\), so it equals \(e_{I\cup J}\). Restricting to a connected component \(K\) of this union, the corresponding ordinary parabolic-longest group element \(w_K\) would have to lie in \(W_AW_B\), with \(A=I\cap K\), \(B=J\cap K\). Indeed Demazure multiplication of an element in \(W_A\) on the right by generators in \(B\) stays in \(W_AW_B\) as an ordinary permutation set.

If both \(A,B\) are proper subsets of the connected interval \(K\), this is impossible. The subset \(W_AW_B\subseteq W_K\) is downward closed for Bruhat order: a reduced subword of a product of words for elements of \(W_A\) and \(W_B\) can again be factored into a word in \(W_A\) followed by a word in \(W_B\). Since \(w_K\) is the unique Bruhat maximum of \(W_K\), its membership would imply \(W_AW_B=W_K\). But \(W_B\) is proper and therefore preserves some nontrivial initial segment of positions of cardinality \(p\) in the natural symmetric-group representation. Equality would force \(W_A\) to act transitively on all \(p\)-subsets; a proper parabolic \(W_A\) cannot do so, because it preserves a nontrivial consecutive block and the size of intersection with that block varies. This contradiction proves the necessary condition. For sufficiency, a connected component contained in \(I\) has its longest element absorbing all factors from \(J\) on both sides, and conversely; factors from disconnected components commute. Thus the product is \(e_{I\cup J}\).

**Unique root and factorization.** A maximal commuting family \(\mathcal F\) necessarily contains \(e_\varnothing\) and \(e_{[m]}\), and is closed under pairwise products, hence under support unions. The union \(U\) of all *proper* supports in \(\mathcal F\) is itself proper: if a union of proper commuting supports first became \([m]\), at the last step it would contradict the connected-component criterion above. Choose \(r\notin U\). The support \(K=[m]\setminus\{r\}\) commutes with every proper support of \(\mathcal F\), so maximality implies \(e_K\in\mathcal F\). Consequently \(K\) is the unique maximal proper support, and \(r\) is uniquely determined.

Removing \(r\) splits \([m]\) into left and right intervals. The component criterion applies independently in these two intervals. Projecting proper supports from \(\mathcal F\) onto each interval gives a maximal commuting family there; otherwise an additional commuting support could be inserted into \(\mathcal F\). The proper supports contain every pair of projected supports, since the union of a left and a right support commutes with every member. Thus proper supports are exactly the Cartesian product of the two projected families, while \([m]\) is their sole additional support. Induction produces unique left/right binary search trees, with \(r\) as their parent root. Conversely, the descendant-first ideals of any such tree form a maximal commuting family by the same criterion. Their idempotent products agree with union of ideals, establishing the claimed semilattice isomorphism.

**Size spectrum, minimum and maximum.** If the left and right subtrees have \(a,b\) order ideals, respectively, then the whole tree has exactly \(1+ab\) ideals: every ideal omitting its root is a pair of subtree ideals, while only the full ideal contains the root. This gives the displayed \(f_m\) and \(M_m\) recurrences, as well as the ordinary Catalan recurrence after summing over \(s\).

For the minimum, induction gives \(a\ge i+1\) when the left subtree has \(i\) keys and \(b\ge m-i\) when the right subtree has \(m-1-i\) keys. Therefore
\[
1+ab\ge1+(i+1)(m-i)=m+1+i(m-1-i)\ge m+1.
\]
For \(m\ge2\), equality holds only for an endpoint root \(i=0\) or \(i=m-1\), together with a minimum-size nonempty subtree. (When \(m=1\), there is one tree.) Hence exactly two endpoint choices arise at each rank \(m\ge2\), giving \(2^{m-1}\) minimizing trees. This argument replaces the incorrect inequality \(1+ab\ge(a+1)+(b+1)-1\) for arbitrary positive \(a,b\), which is false when \(a=1\), and proves the minimum with the actual subtree-size constraints.

## Reproduction and limitations

The existing `verify.py` independently implements Demazure multiplication on symmetric-group permutations, checks all parabolic-idempotent commutation pairs and maximal clique families through rank seven, checks all group elements for idempotence through rank five, and checks the size recurrence through rank ten. These are finite consistency checks; the proof above covers every \(m\ge1\). The result concerns type-A 0-Hecke **monoid** idempotents and inclusion-maximal commuting families only; it does not classify nonidempotent commutative subsemigroups, the monoid algebra's linear idempotents, or unlabeled binary-tree shapes.

## Relationship to established results

The idempotent classification and the Demazure multiplication rules are standard and explicitly credited to Elias–Ko and the general theory of Hecke monoids. The Catalan size of Kiselman quotient monoids from Ganyushkin–Mazorchuk concerns a distinct quotient construction; it is not evidence of the present maximal commuting-family classification. Other commutative constructions in the Hecke algebra, including work of He and Denton, concern different objects. The claimed contribution is the bijection between these maximal commuting idempotent families and ordered binary search trees, including their complete cardinality spectrum. Related results about general Coxeter parabolics or combinatorial building sets may contain equivalent implicit formulations; historical priority is not asserted as certified.

## References

- B. Elias and H. Ko, *A singular Coxeter presentation*, arXiv:2105.08563, especially the Demazure product and parabolic idempotents.
- A. Berenstein, J. Greenstein and J.-R. Li, *Hecke monoids, their homomorphisms and parabolicity*, arXiv:2605.09761, §2 (parabolic elements and idempotents).
- O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, arXiv:1006.0316.
- X. He, *A subalgebra of 0-Hecke algebra*, arXiv:0904.1786.
- T. Denton, *Excursions into Algebra and Combinatorics at q=0*, arXiv:1108.4379.
