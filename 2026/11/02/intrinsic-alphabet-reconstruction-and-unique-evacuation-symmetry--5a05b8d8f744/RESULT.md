# Intrinsic alphabet reconstruction and unique evacuation symmetry of stylic monoids

## Finding

Let \(A\) and \(B\) be arbitrary finite totally ordered sets (empty sets allowed). Denote their stylic monoids of column-insertion transformations by \(\operatorname{Styl}(A)\) and \(\operatorname{Styl}(B)\). Every monoid isomorphism \(\operatorname{Styl}(A)\to\operatorname{Styl}(B)\) exists if and only if \(|A|=|B|\), and, when it exists, it is **unique**, induced by the unique order-preserving bijection \(A\to B\). Likewise there is exactly one monoid anti-isomorphism when the ranks agree: it sends generators by the unique order-reversing bijection and reverses the order of multiplication. For \(|A|\ge2\), the group of all automorphisms and anti-automorphisms of \(\operatorname{Styl}(A)\) is cyclic of order two, with the nontrivial element given by the canonical evacuation (Schützenberger) involution. For \(|A|\le1\), this group is trivial.

More strongly, the unordered abstract multiplication table itself reconstructs both the generator set and its original linear order. The generators are precisely the maximal elements below the identity in Green's \(\mathcal J\)-order; for distinct generators \(a,b\),
\[
 a>b\quad\Longleftrightarrow\quad (ab)^2=ab.
\]
Thus the rigidity claim is not a statement merely about automorphisms already assumed to preserve a chosen presentation.

## Assumptions and scope

The stylic monoid is the quotient of the free monoid on \(A\) by the Knuth relations and the idempotence relations \(a^2=a\) for \(a\in A\), equivalently the faithful action on columns by Schensted left insertion (Abram--Reutenauer, Theorem 8.1). A column is a subset of \(A\) written in decreasing order. On inserting \(a\) into a column, the least existing letter \(\ge a\), if present, is replaced by \(a\); otherwise \(a\) is adjoined. In a word action the rightmost letter acts first. The empty word is the identity.

Use the standard Green preorder \(x\le_{\mathcal J}y\) if \(x\in MyM\) for \(M=\operatorname{Styl}(A)\); it is a partial order because stylic monoids are \(\mathcal J\)-trivial (Abram--Reutenauer, Theorem 11.1). The support \(\operatorname{supp}(x)\) is the set of letters in any representing word; it is well-defined (ibid., Lemma 5.3) and satisfies \(\operatorname{supp}(xy)=\operatorname{supp}(x)\cup\operatorname{supp}(y)\). All conclusions are valid for every finite rank, without assuming a field or restricting to permutations that preserve the named generators.

## Proof

**1. Recover the alphabet without naming a presentation.** Every nonidentity element \(x\in M\) has nonempty support, and any letter \(a\in\operatorname{supp}(x)\) occurs in a representative \(x=uav\), so \(x\le_{\mathcal J}a\). If \(x\ne a\), this comparison is strict: otherwise \(a=pxq\) for some \(p,q\), forcing \(\operatorname{supp}(x)\subseteq\{a\}\); since a word supported solely on \(a\) reduces by idempotence to \(a\), this would imply \(x=a\). Conversely, suppose \(a\le_{\mathcal J}y\). Writing \(a=pyq\), support preservation gives \(\operatorname{supp}(y)\subseteq\{a\}\), so \(y\) is either \(1\) or \(a\). Therefore each generator \(a\) is maximal strictly below \(1\), and every other proper element lies strictly below some such generator. These coatoms are exactly the original letters, hence intrinsic under any monoid isomorphism or anti-isomorphism (the latter also preserves two-sided principal ideals).

**2. Recover the linear order using an idempotence test.** Let \(a<b\). The two-letter specializations of the Knuth relations, together with the idempotence of letters, give
\[
 aba=ba=bab.
\]
It follows that \((ab)^2=abab=ba\) and \((ba)^2=baba=ba\). The elements \(ab\) and \(ba\) are distinct: on the empty column, \(ab\) yields the one-letter column \(\{a\}\), whereas \(ba\) yields \(\{a,b\}\). Thus \(ab\) is not idempotent and \(ba\) is. Interchanging the labels establishes, for *every* distinct pair, \((ab)^2=ab\) exactly when \(a>b\). This reconstructs the orientation of every pair in the total order using only multiplication.

**3. Classify isomorphisms.** Any isomorphism permutes the intrinsically recognized letters, and by step 2 its restriction to letters is strictly increasing. There is a unique order-preserving bijection between finite chains of equal cardinality and none between chains of different cardinalities. Such a bijection respects the Knuth/idempotence presentation and hence extends to an isomorphism. Conversely, since letters generate \(M\), any isomorphism is determined by this unique bijection. The same reasoning works for empty and singleton alphabets.

**4. Classify anti-isomorphisms.** An anti-isomorphism preserves idempotency but reverses products; applying the test from step 2 shows that its restriction to letters reverses the total order. The source's canonical involutive anti-automorphism (Abram--Reutenauer, Section 9.1 and Theorem 9.1) reverses both the order of letters and the order of words. Combining this map with an increasing relabeling constructs the anti-isomorphism between any two equally sized alphabets. Its uniqueness follows because letters generate. On a chain with at least two letters, the anti-involution is distinct from the identity because it exchanges extreme generators. At rank zero or one, the monoid is commutative and the two maps coincide. This completes the proof.

## Verification

The proof covers unrestricted finite ranks and is independent of the finite checks. The accompanying standalone `verify_stylic.py` constructs stylic monoids as transformations of all columns, not from a word-rewriting implementation; it enumerates all elements for ranks one through five, recovering the Bell numbers \(2,5,15,52,203\), checks the intrinsic Green-order coatoms at ranks at most four, verifies idempotent-product comparisons for all ordered pairs of distinct generators, and checks the evacuation map anti-multiplicatively against **every** ordered pair of monoid elements up through rank five. Its terminal output is `VERIFY_OK`. These finite checks are corroboration, not a substitute for proof or a claim of independent mathematical review.

Reproduction: run `python3 verify_stylic.py` with a standard Python 3 installation; the program uses no third-party packages.

## Relationship to prior work

Abram and Reutenauer established the stylic presentation, the canonical evacuation anti-involution, well-defined support, and the \(\mathcal J\)-triviality/graded structure. All are used explicitly and none is presented as new. The contribution here is the **intrinsic reconstruction and exhaustive uniqueness classification** of abstract isomorphisms and anti-isomorphisms, not the prior construction of evacuation. Aird and Ribeiro later studied the canonical involution through a faithful tropical representation and identities; their inspected statements likewise do not assert uniqueness among all abstract anti-automorphisms.

Kudryavtseva and Mazorchuk proved analogous rigidity for Kiselman's semigroups (as reported precisely in Andrenšek, Introduction, Proposition 20 of the earlier work). That is a distinct family with a different presentation: a proof for its automorphisms does not formally classify those of the stylic quotient, although the shared two-letter relations explain why a related reconstruction works here. This is the closest methodological precedent and limits any claim of conceptual novelty.

## Limitations

This is a classification of **invertible** (anti-)homomorphisms only; it does not enumerate noninvertible endomorphisms, their kernels, or minimal presentations. The proof uses the existing stylic presentation and \(\mathcal J\)-triviality, not independent proofs of those published prerequisites. The rigidity follows by a short intrinsic argument from them; it is not claimed to introduce a new presentation or an independent evacuation construction. Publication priority is provisional because an earlier equivalent abstract-semigroup rigidity corollary could have escaped retrieval. No independent mathematical audit has been performed.

## References

1. A. Abram and C. Reutenauer, *The stylic monoid*, arXiv:2106.06556, first posted June 11, 2021, https://arxiv.org/html/2106.06556v2 . Relevant: Lemma 5.3; Theorem 8.1; Section 9.1 and Theorem 9.1; Theorem 11.1.
2. T. Aird and J. Ribeiro, *Tropical representations and identities of the stylic monoid*, Semigroup Forum 106 (2023), first published December 6, 2022, https://doi.org/10.1007/s00233-022-10328-9 . Relevant: Sections 2.4, 3, 5.
3. L. Andrenšek, *A complete classification of endomorphisms of Kiselman's semigroup*, Semigroup Forum 112 (2026), published September 17, 2025, https://doi.org/10.1007/s00233-025-10577-4 . Relevant: Introduction and statement of Kudryavtseva--Mazorchuk's Proposition 20; this is comparative literature on a distinct monoid.
4. G. Kudryavtseva and V. Mazorchuk, *On Kiselman's semigroup*, arXiv:math/0511374, https://arxiv.org/abs/math/0511374 .
