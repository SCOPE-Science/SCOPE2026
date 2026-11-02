# Distributivity of finite Heyting materializers: a minimal-support criterion and a sharp nine-element boundary

## Finding

Let \(H\) be a finite nontrivial Heyting algebra, let \(a\in H\), and define its *materializer*
\[
M_H(a)=\{b\in H:a\to b=\neg a\vee b\}.
\]
Give \(M_H(a)\) the order inherited from \(H\), with its own least upper bounds; these need not coincide with the joins in \(H\).

Represent \(H\cong J(P)\), the downset algebra of its finite poset of join-irreducibles, and represent \(a\) by a downset \(I\subseteq P\). Set \(U=\uparrow I\), \(Q=P\setminus U\), and for \(p\in U\) put \(S_p=I\cap\downarrow p\) (necessarily nonempty). For every \(q\in Q\), form the finite family
\[
\mathcal S_q=\{S_p:p\in U,\ q\le p\},
\]
possibly empty. The following conditions are equivalent:

1. The intrinsic lattice \(M_H(a)\) is distributive.
2. For all downsets \(K_1,K_2\) of \(I\), the map
   \[
   D(K)=Q\cap\downarrow\{p\in U:S_p\subseteq K\}
   \]
   satisfies \(D(K_1\cup K_2)=D(K_1)\cup D(K_2)\).
3. For every \(q\in Q\), each inclusion-minimal member of \(\mathcal S_q\) is a principal downset of \(I\), i.e. equals \(I\cap\downarrow i=\downarrow i\) for some \(i\in I\).

This is a finite-poset decision criterion; a direct implementation using set containment tests runs in polynomial time in \(|P|\). In particular, no such materializer is intrinsically nondistributive when \(|H|\le8\), and this bound is sharp: a nine-element Heyting algebra has a seven-element nondistributive materializer. Up to isomorphism, the unique nine-element algebra with this property is \(J(P)\) for the four-point poset consisting of three incomparable minimal points below a common maximum. In that poset, precisely the three choices of \(I\) comprising two of the minimal points give nondistributive materializers.

The intrinsic and ambient notions are strictly different: for the three-point poset with two incomparable points below a maximum, taking \(I\) to consist of both minima gives a four-element Boolean materializer whose join differs from the ambient join.

## Assumptions and scope

All posets and Heyting algebras are finite. A downset \(J\subseteq P\) contains every predecessor of each of its elements. The downset algebra \(J(P)\) has meet as intersection and join as union. Its implication satisfies
\[
p\in (I\Rightarrow J)\quad\Longleftrightarrow\quad I\cap\downarrow p\subseteq J.
\]
The principal downset \(\downarrow i\) is taken in \(P\); for \(i\in I\) it lies inside the downset \(I\). A minimum of a family of sets always means inclusion-minimal, not a set of smallest cardinality. If \(Q=\varnothing\) or \(\mathcal S_q=\varnothing\), the corresponding condition is vacuous. The result concerns distributivity of the *intrinsic lattice* of satisfying consequents, not a claimed Heyting-subalgebra structure or distributivity of implication itself.

## Proof

**1. Materializer normal form.** For \(J\in J(P)\), the implication rule above gives
\[
\neg I=\{p\in P:I\cap\downarrow p=\varnothing\}=Q.
\]
Because \(J\) is a downset, \(p\in J\) implies \(I\cap\downarrow p\subseteq J\). Hence \(I\Rightarrow J=Q\cup J\) exactly when
\[
\text{for every }p\in U,\quad
p\in J\ \Longleftrightarrow\ S_p\subseteq J.
\tag{1}
\]
Write \(K=J\cap I\), a downset of \(I\), and define
\[
F(K)=\{p\in U:S_p\subseteq K\},\qquad
D(K)=Q\cap\downarrow F(K).
\]
The family \(F(K)\) is a downset relative to \(U\); its intersection with \(I\) is exactly \(K\). Thus (1) says \(J\cap U=F(K)\). Its remaining part \(L=J\cap Q\) is a downset of \(Q\), and downwards closure of \(J\) requires precisely \(D(K)\subseteq L\). Conversely, for every pair of downsets
\[
K\in J(I),\quad L\in J(Q),\quad D(K)\subseteq L,
\tag{2}
\]
the union \(J=F(K)\cup L\) is a downset of \(P\) satisfying (1). This gives an order-isomorphism between \(M_H(a)\) and the pairs (2), ordered coordinatewise by inclusion. In particular this proves directly that \(M_H(a)\) is a finite lattice.

**2. Lattice operations.** Since \(F(K_1\cap K_2)=F(K_1)\cap F(K_2)\), coordinatewise intersection gives the meet. Monotonicity of \(D\) ensures that the pairwise join is
\[
(K_1,L_1)\mathbin{\vee_M}(K_2,L_2)
=\bigl(K_1\cup K_2,\ L_1\cup L_2\cup D(K_1\cup K_2)\bigr).
\tag{3}
\]
If \(D\) preserves unions, the final term in (3) is already contained in \(L_1\cup L_2\), since \(D(K_i)\subseteq L_i\). The pair representation is then closed under coordinatewise union and intersection within the distributive lattice \(J(I)\times J(Q)\); it is therefore distributive.

Conversely, suppose the union identity fails. There exist downsets \(K_1,K_2\subseteq I\) and \(q\in Q\) such that
\[
q\in D(K_1\cup K_2)\setminus\bigl(D(K_1)\cup D(K_2)\bigr).
\]
The elements \(A_i=(K_i,D(K_i))\) and \(E=(\varnothing,\downarrow_Q q)\) are admissible, because \(D(\varnothing)=\varnothing\). The second coordinate of \(E\wedge(A_1\vee_M A_2)\) contains \(q\), whereas the second coordinate of \((E\wedge A_1)\vee_M(E\wedge A_2)\) does not contain \(q\): both latter first coordinates are empty and no closure term is added. Thus distributivity fails. This proves equivalence of conditions 1 and 2.

**3. Minimal-support characterization.** For \(q\in Q\) and a downset \(K\subseteq I\),
\[
q\in D(K)\quad\Longleftrightarrow\quad
\exists S\in\mathcal S_q:\ S\subseteq K.
\tag{4}
\]
Every member \(S\in\mathcal S_q\) is a nonempty downset of \(I\). Suppose each inclusion-minimal member is principal. Whenever \(q\in D(K_1\cup K_2)\), choose a minimal \(S\in\mathcal S_q\) included in \(K_1\cup K_2\). Write \(S=\downarrow i\). Since \(i\) belongs to \(K_1\) or \(K_2\), the whole principal ideal \(S\) lies in the same downset. Equation (4) gives \(q\in D(K_1)\cup D(K_2)\). Monotonicity gives the reverse inclusion, so condition 2 follows.

Conversely, let \(S\) be an inclusion-minimal nonprincipal member of \(\mathcal S_q\). It has at least two incomparable maximal elements. Choose one, \(i\), and write \(K_1=S\setminus\{i\}\) and \(K_2=\downarrow i\). Both are proper downsets of \(S\), and \(K_1\cup K_2=S\). From minimality of \(S\) in \(\mathcal S_q\), no member of that family lies in either proper subset. Thus (4) gives
\[
q\in D(K_1\cup K_2),\qquad q\notin D(K_1)\cup D(K_2),
\]
contradicting condition 2. This proves equivalence of all three conditions.

**4. The sharp size boundary.** If nondistributivity occurs, step 3 supplies a point \(q\in Q\), a point \(p\in U\) with \(q\le p\), and two incomparable maximal points \(i,j\in S_p\subseteq I\), with \(i,j\le p\). The point \(q\) is incomparable with both \(i\) and \(j\). Indeed, \(i\le q\) would put \(q\) in \(\uparrow I\), while \(q\le i\) would put \(q\) in the downset \(I\). The induced subposet on \(\{i,j,q,p\}\) therefore has three incomparable minima and one maximum. It has exactly nine downsets. Restriction of downsets from \(P\) to this induced subposet is surjective: each downset of the subposet extends by taking its downclosure in \(P\). Hence \(|J(P)|\ge9\).

If \(P\) contains any additional point \(r\), this restriction is not injective. Indeed the two downsets \(\downarrow_P r\) and \(\downarrow_P(\downarrow_P r\cap\{i,j,q,p\})\) have the same intersection with the four-point subposet, but the former contains \(r\) and the latter does not. Thus equality \(|J(P)|=9\) forces \(P\) itself to be that four-point poset.

Conversely, let \(P=\{i,j,q,p\}\) with \(i,j,q<p\) and no other comparisons, and take \(I=\{i,j\}\). The materializer has exactly seven members,
\[
\varnothing,\ \{i\},\ \{j\},\ \{q\},\ \{i,q\},\ \{j,q\},\ P.
\]
Its intrinsic join of \(\{i\}\) and \(\{j\}\) is \(P\), but \(\{q\}\wedge\{i\}=\{q\}\wedge\{j\}=\varnothing\), so distributivity fails. Permuting the three minima gives exactly three such antecedents. For other antecedents the criterion of step 3 holds, establishing the equality classification.

Finally, for the three-point poset \(\{i,j,p\}\) with \(i,j<p\), take \(I=\{i,j\}\). Here \(Q=\varnothing\), so the criterion holds, and \(M_H(a)=\{\varnothing,\{i\},\{j\},P\}\) is Boolean in its inherited order, even though the ambient union of its two atoms is \(\{i,j\}\notin M_H(a)\).

**5. Decision procedure.** Compute transitive reachability of \(P\), then \(U,Q,S_p\). For each \(q\in Q\), list \(S_p\) with \(p\in U\) and \(q\le p\), discard those properly containing another listed set, and test whether each remaining set has a greatest element. The test is equivalent to the criterion. All lists have length at most \(|P|\), and all operations are finite set inclusions, giving an elementary polynomial-time test without enumerating the downsets of \(P\).

## Verification

Run `python3 materializer_distributivity_verify.py` using Python 3 (standard library only). The script enumerates each distinct naturally labeled finite poset in topological order on up to six points. For sizes up to five it independently constructs the Heyting-implication equality class and directly tests all intrinsic lattice distributivity triples. On all six-point posets it checks the equivalent union and minimal-support criteria, including every possible antecedent. It separately checks the four-point sharp counterexample. The reported totals are 5,231 posets and 101,658 antecedent downsets; the exhaustive intrinsic-lattice tests cover all sizes up to five only. This is finite corroboration, not the proof of the universal theorem.

## Relationship to prior work

Bumpus and Kocsis, *Degree of Satisfiability in Heyting Algebras* (arXiv:2110.11515, first posted 2021-10-21), Definition 3.13 and Remark 3.14, introduce materializers and note meet closure and other properties. The present result addresses the further, distinct question of intrinsic distributivity for one fixed antecedent and gives a necessary-and-sufficient poset criterion and a sharp smallest-algebra obstruction.

Cīrulis, *Lattice of closure endomorphisms of a Hilbert algebra* (arXiv:1701.03902, §4), shows a distributive structure for a lattice of **endomorphism maps**, not for the set of **consequents** satisfying one material-implication identity; his positive theorem does not imply intrinsic distributivity here. Adaricheva and Nation, *On implicational bases of closure systems with unique critical sets* (arXiv:1205.2881, §§2, 6–8), develop general implication-basis and closure-lattice tools, but do not specify the materializer fibers or the minimal external-support criterion. Standard finite Birkhoff representation and closure-system terminology are used as background, not claimed as new.

## Limitations

The theorem is finite; no statement is made for infinite Heyting algebras or closure systems without the materializer origin. The verification is not independent peer review. The precise historical originality of an equivalent result under other terminology is not established conclusively. The sharp nine-element assertion is a minimum *algebra size*, not a claim that the seven-element nondistributive lattice is unique among all lattices. The materializer need not be an ambient sublattice even when its intrinsic lattice is distributive.

## References

1. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, arXiv:2110.11515 (first public version 2021-10-21); relevant material §§1, 3.13–3.15. https://arxiv.org/abs/2110.11515
2. J. Cīrulis, *Lattice of closure endomorphisms of a Hilbert algebra*, arXiv:1701.03902 (2017), especially §4. https://arxiv.org/abs/1701.03902
3. K. Adaricheva and J. B. Nation, *On implicational bases of closure systems with unique critical sets*, arXiv:1205.2881 (2012), especially §§2, 6–8. https://arxiv.org/abs/1205.2881
