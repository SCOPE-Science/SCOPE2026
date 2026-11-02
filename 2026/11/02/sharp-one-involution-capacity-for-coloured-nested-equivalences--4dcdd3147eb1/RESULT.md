# Sharp one-involution capacity for coloured nested equivalences

## Finding
Let \(q\geq1\) and \(K\geq1\) be integers. Consider finite nonempty structures with exactly \(q\) named, pairwise disjoint and exhaustive unary colours and nested equivalence relations \(E_1\subseteq\cdots\subseteq E_K\). Isomorphisms preserve the colours and all equivalences.

Define \(R_h(z)\) and \(T_h(z)\) as the ordinary size-generating polynomials for isomorphism types of rooted height-\(h\) coloured hierarchies whose colour-preserving automorphism groups have orders \(1\) and \(2\), respectively; their size is their number of coloured leaves. Set
\[
R_0(z)=qz,\qquad T_0(z)=0,\qquad
F_h(z)=\prod_{s\geq1}(1+z^s)^{[z^s]R_h(z)}.
\]
These are finite products. For every \(h\geq0\), the following exact polynomial recurrences hold:
\[
\boxed{R_{h+1}(z)=F_h(z)-1,}\qquad
\boxed{T_{h+1}(z)=F_h(z)T_h(z)+F_h(z)\sum_{s\geq1}\frac{[z^s]R_h(z)\,z^{2s}}{1+z^s}.}
\]
Every displayed quotient is a polynomial after cancellation. For the original \(K\)-equivalence structures the polynomials are \(R_{K+1}\) and \(T_{K+1}\); the number of labelled structures of size \(n\) with automorphism group of order \(1\) is \(n![z^n]R_{K+1}\), and with order \(2\) is \(\frac{n!}{2}[z^n]T_{K+1}\).

Put \(a_0=q\), \(a_{h+1}=2^{a_h}-1\), and
\[
C_h=q\,2^{\sum_{j=0}^{h-2}(a_j-1)}\quad(h\geq1),\qquad
B_h=1+\sum_{i=1}^{h}C_i\quad(h\geq1),
\]
with the empty sum interpreted as zero. Then a rigid structure exists on exactly every carrier size \(1\leq n\leq C_{K+1}\); an order-two automorphism-group structure exists on exactly every size \(2\leq n\leq B_{K+1}\). Neither is possible beyond its corresponding bound. There is exactly one unlabelled rigid structure at size \(C_{K+1}\), and exactly \(q\) order-two structures at size \(B_{K+1}\). In particular, any structure of size greater than \(B_{K+1}\) has at least four automorphisms.

The numbers of unlabelled low-symmetry types, \(a_h=R_h(1)\) and \(b_h=T_h(1)\), obey
\[
 b_0=0,\qquad b_{h+1}=2^{a_h}b_h+a_h2^{a_h-1}.
\]
For \(q=2\), \(K=1\), there are seven rigid and 44 order-two unlabelled structures, with exact size polynomials
\[
R_2=2z+2z^2+2z^3+z^4,\qquad
T_2=4z^2+8z^3+11z^4+12z^5+7z^6+2z^7.
\]
Thus the rigid capacity is four and the one-involution capacity is seven in this example.

## Assumptions and scope
A colour is a named unary predicate; each element belongs to exactly one of the \(q\) predicates, including when \(q=1\). All \(E_i\) are genuine reflexive, symmetric and transitive relations; inclusion means \(E_i\)-classes refine \(E_{i+1}\)-classes. No restrictions are imposed on block cardinalities or on equality among adjacent equivalence relations. There are no additional relation symbols or constants. All carriers are finite and nonempty. Automorphisms must preserve every named predicate and equivalence relation. An order-two automorphism group is necessarily isomorphic to \(C_2\), and its unique nonidentity element is an involution.

A height-zero type is one coloured leaf. A height-one type is a nonempty multiset of leaves, interpreted as an \(E_1\)-class. Inductively a height-\(h+1\) type is a nonempty multiset of height-\(h\) types. A full structure is a nonempty multiset of height-\(K\) types, hence has height \(K+1\) after adjoining an invisible top root. This encoding is bijective on isomorphism classes and preserves automorphism groups.

## Proof
**1. Rooted-multiset automorphisms.** Fix any rooted hierarchy with children grouped by isomorphism type \(U\), each occurring with multiplicity \(m_U\). The automorphism group is a product over \(U\) of \(\operatorname{Aut}(U)^{m_U}\rtimes S_{m_U}\). Its order is \(\prod_U |\operatorname{Aut}(U)|^{m_U}m_U!\). Therefore the whole hierarchy is rigid if and only if its children are rigid and pairwise nonisomorphic. Its group has order exactly two if and only if precisely one of the following disjoint cases holds: (i) it has one child of group order two, together with pairwise nonisomorphic rigid children (the order-two type appears once); (ii) all children are rigid and there is exactly one repeated isomorphism type, which appears exactly twice, while every other child type appears at most once. Any other nontrivial multiplicity or child automorphism yields a group of order at least four. This also inductively excludes groups of order three.

**2. The polynomial census.** Each rigid child type contributes either zero or one copy, yielding \(F_h(z)\). Removing the empty multiset gives \(R_{h+1}=F_h-1\). In case (i), choose exactly one order-two child and an arbitrary set of pairwise nonisomorphic rigid children: contribution \(F_hT_h\). In case (ii), choose a rigid type of size \(s\) to duplicate and choose any subset of the remaining rigid types: contribution \(([z^s]R_h)z^{2s}F_h/(1+z^s)\). Summing gives the recurrence. Standard orbit-stabilizer counting gives exactly \(n!/|\operatorname{Aut}|\) labellings of each isomorphism type.

**3. The sharp bounds.** Write \(S_h=R_h'(1)\), the sum of leaf counts of all rigid height-\(h\) types, counted once per isomorphism type. Because \(R_{h+1}=F_h-1\), its degree is \(C_{h+1}=S_h\), and its top coefficient is one: include each rigid child type exactly once. Differentiating the product gives \(S_{h+1}=2^{a_h-1}S_h\). As \(S_0=q\), it follows that \(C_1=q\) and \(C_h=q2^{\sum_{j=0}^{h-2}(a_j-1)}\) for all \(h\geq1\). Evaluating the recurrences at \(z=1\) gives the displayed formulas for \(a_h,b_h\).

At height one, the largest order-two object contains two copies of one colour and one copy of every other colour, hence \(B_1=q+1\), with exactly \(q\) top-size isomorphism types. For \(h\geq1\), the greatest degree in case (i) is \(C_{h+1}+B_h\), whereas in case (ii) it is \(C_{h+1}+C_h\). Since \(B_h>C_h\), only (i) attains the maximum. Thus \(B_{h+1}=C_{h+1}+B_h\), giving \(B_h=1+\sum_{i=1}^{h}C_i\). The highest coefficient remains \(q\), because the maximum uses every rigid child type and precisely one maximum-size order-two child.

**4. Every intermediate size occurs.** At height one, every size from one to \(q=C_1\) is rigid: choose that many distinct colour types. Suppose rigid height-\(h\) types occur for all weights \(1,\dots,C_h\). Order every rigid type by nondecreasing size. Every weight \(w\geq2\) comes after a selection of types having sizes \(1,\dots,w-1\), whose total weight is at least \(w-1\); the usual contiguous-subset-sums induction therefore makes all weights \(0,\dots,S_h=C_{h+1}\) available. Nonempty selections give all rigid sizes \(1,\dots,C_{h+1}\).

At height one, an order-two type on each of \(2,\dots,q+1\) leaves is obtained by doubling one colour and taking the desired number of other colours once. Suppose order-two height-\(h\) types exist for all sizes \(2,\dots,B_h\). Taking one such type together with an arbitrary set of distinct rigid height-\(h\) types, whose total size ranges over all \(0,\dots,C_{h+1}\), realizes every size \(2,\dots,B_h+C_{h+1}=B_{h+1}\). This proves both asserted full spectra, all sharp upper bounds, and the maximal isomorphism counts.

## Verification
The accompanying standalone `checker.py` uses two independent constructions: the coefficient recurrence above, and exhaustive labelled colorings with nested set partitions. For the latter it evaluates every colour-preserving permutation to obtain the exact automorphism-group order, canonicalizes the nested partition type, and compares both the unlabelled type count and orbit-stabilizer-labelled count with polynomial coefficients. Completed ranges were \((q,K,n_{\max})=(1,1,5),(1,2,5),(2,1,5),(2,2,4),(3,1,4)\). The executable reported `ALL_CHECKS_OK`. Such finite checks do not certify the statement for all \(q,K,n\); the preceding proof supplies the general argument.

## Relationship to prior work
Fiuk, *The Guarded Fragment with Nested Equivalences* (2026), studies the same chain-of-equivalences semantic object in guarded finite model theory and uses a rooted hierarchy representation. It establishes finite-model and complexity results, rather than the present exact low-automorphism census and sharp size spectra. Imrich and Tucker, *Asymmetrizing trees of maximum valence* (2020), establish results on asymmetric colourings of trees, explaining why distinct child types govern rigidity; their rooted-tree motion results do not state the present nested-equivalence order-two polynomial or capacity. Classical rooted-tree automorphism-product formulas underpin Step 1 and are not claimed as new.

## Limitations
The theorem concerns only structures with \(q\) exhaustive named colours and a chain of nested equivalences, with no other symbols. The coefficients count unlabelled isomorphism types, not all finite models of a guarded formula. The result does not establish an analogous exact bound for groups of order three or higher; it only excludes order three for this class. The proof is elementary once the rooted-multiset decomposition is recognized. Historical priority for the particular coupled census and capacity remains open to independent assessment; older bounded-height coloured-tree counting literature may subsume components, and one relevant textbook treatment could not be fully inspected.

## References
1. Oskar Fiuk, *The Guarded Fragment with Nested Equivalences*, arXiv:2605.15072 (first submitted 14 May 2026); LICS 2026, DOI: 10.4230/LIPIcs.LICS.2026.44.
2. Wilfried Imrich and Thomas W. Tucker, *Asymmetrizing trees of maximum valence \(2^{\aleph_0}\)*, *Monatshefte für Mathematik* **192** (2020), 615–624, DOI: 10.1007/s00605-020-01420-9.
3. Jaroslav Nešetřil and Patrice Ossona de Mendez, *Sparsity: Graphs, Structures, and Algorithms*, Springer (2012), Lemma 6.10 on bounded-height coloured rooted forests (comparison based on an accessible lemma excerpt; full textbook not inspected).
