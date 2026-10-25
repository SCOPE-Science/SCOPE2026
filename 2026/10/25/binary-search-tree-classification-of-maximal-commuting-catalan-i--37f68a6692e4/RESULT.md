# Binary-search-tree classification of maximal commuting Catalan idempotent families

## Finding
For every integer \(n\ge2\), let \(C_n\) be the monoid of nondecreasing, order-decreasing maps on \([n]=\{1,\ldots,n\}\), composed as transformations. Let \(E_n\) be its idempotents. An inclusion-maximal pairwise-commuting subset of \(E_n\) is called a maximal commuting idempotent family; equivalently it is a maximal semilattice of idempotents in \(C_n\).

**Theorem.** These families are in canonical bijection with binary search trees on the ordered keys \(2,3,\ldots,n\). For a tree \(T\), let \(\mathcal I(T)\) be its sets of ancestor-closed nodes (including the empty set). Writing \(e_A(i)=\max((\{1\}\cup A)\cap[1,i])\), the corresponding maximal family is exactly
\[
\mathcal F_T=\{e_A:A\in\mathcal I(T)\}.
\]
In particular, the number of maximal families is exactly
\[
\boxed{\frac1n\binom{2n-2}{n-1}}.
\]
Their sizes are recursively determined by \(s(\varnothing)=1\) and \(s(T)=1+s(T_L)s(T_R)\). The minimum size is \(n\), attained by exactly \(2^{n-2}\) maximal families, corresponding to binary search trees that are paths. For \(n\ge4\), other maximal families are larger, so the flag clique complex on commuting idempotents is nonpure.

The *entire size profile* is computable recursively: let \(H_0(z)=z\), and for \(m\ge1\) set
\[
H_m(z)=\sum_{a+b=m-1}\ \sum_{u,v\ge1}
[z^u]H_a(z)\,[z^v]H_b(z)\ z^{1+uv}.
\]
Then \([z^j]H_{n-1}(z)\) counts maximal commuting idempotent families of size \(j\).

## Assumptions and scope
Transformations act on the left by composition, and only *idempotents* of the full order-preserving, order-decreasing transformation monoid are vertices. No characteristic or field is involved. A binary search tree has each key in its left subtree smaller than its root and each key in its right subtree larger; its ancestor-closed subsets need not be interval subsets. Empty subtrees each contribute one ideal.

## Proof
**1. Normal form.** An idempotent monotone order-decreasing map \(e\) fixes exactly a set \(\{1\}\cup A\) with \(A\subseteq\{2,\ldots,n\}\). For any \(i\), its value \(e(i)\) is a fixed point not exceeding \(i\). If \(j\) is any fixed point with \(j\le i\), monotonicity gives \(j=e(j)\le e(i)\). Hence \(e=e_A\). Conversely each such floor projection is an idempotent in \(C_n\).

**2. Local commutation facts.** If nonempty sets \(A,B\subseteq\{2,\ldots,n\}\) are disjoint, their projections do not commute. For example, if \(\max A>\max B\), evaluating at \(i=\max A\) yields
\[
e_B(e_A(i))=\max B,\qquad e_A(e_B(i))=e_A(\max B)<\max B.
\]
The reverse inequality between maxima is symmetric. If \(e_A,e_B\) commute, their product is an idempotent with fixed set exactly \((\{1\}\cup A)\cap(\{1\}\cup B)\): a common fixed point is fixed by the product, and a point fixed by their commuting product is fixed by each (both maps are order-decreasing). Thus \(e_Ae_B=e_{A\cap B}\), which commutes with every map commuting with both factors. Finally, if \(r\in A\), then \(e_{\{r\}}\) commutes with \(e_A\): for \(i<r\), both composites equal \(1\); for \(i\ge r\), both composites equal \(r\).

**3. Existence and uniqueness of the root.** Let \(\mathcal F\) be maximal. The constant projection \(e_\varnothing\) and the identity belong to \(\mathcal F\); maximality and the product fact make its index sets closed under intersection. Choose an inclusion-minimal *nonempty* index set \(W\) from \(\mathcal F\). For every other nonempty index set \(A\) in the family, the disjointness obstruction gives \(W\cap A\ne\varnothing\), and product closure gives \(W\cap A\in\mathcal F\). Minimality implies \(W\subseteq A\). For any \(r\in W\), the singleton projection \(e_{\{r\}}\) commutes with every member; maximality forces it into the family. Minimality then forces \(W=\{r\}\). Hence every nonempty index set contains this unique \(r\), and no other singleton can occur.

**4. Separation at the root.** For any two index sets containing \(r\), commutation on arguments \(i<r\) depends only on the indices to the left of \(r\), and on \(i\ge r\) only on indices to the right. Indeed, above \(r\) each floor projection has values at least \(r\), and on the lower interval both have values below \(r\). After relabeling the two intervals, these restrictions are themselves floor projections. Consequently the maps commute if and only if their two left restrictions commute and their two right restrictions commute. Every combination of a left index set seen in the family and a right index set seen in the family can therefore be adjoined without violating commutation, so maximality forces the *full Cartesian product* of the two side families. Moreover each side family is maximal: any extra side projection commuting with it, combined with \(r\) and the empty opposite side, would extend \(\mathcal F\). The same reasoning proves that two maximal side families yield a maximal global family.

**5. Induction and enumeration.** Recurse on the left and right intervals, yielding unique search trees \(T_L,T_R\) with root \(r\). The full product rule identifies the nonempty index sets with \(\{r\}\cup L\cup R\), where \(L,R\) range over ancestor-closed sets in the two subtrees. Adding the empty index set gives exactly \(\mathcal I(T)\), and the root is recoverable as the unique singleton index set, proving bijectivity. With \(m=n-1\) keys, the number \(c_m\) obeys \(c_0=1\) and \(c_m=\sum_{a+b=m-1}c_ac_b\), so \(c_m=\binom{2m}{m}/(m+1)\). An ideal is either empty or consists of the root and independently chosen left/right ideals; hence \(s(T)=1+s(T_L)s(T_R)\), yielding the profile recurrence. By induction \(s(T_L)\ge a+1\) and \(s(T_R)\ge b+1\), so \(s(T)\ge 1+(a+1)(b+1)=m+ab+1\ge m+1=n\). Equality requires one subtree empty and the other a minimizing tree, producing precisely the \(2^{m-1}=2^{n-2}\) one-branch-at-each-node trees. At \(m=3\) a root with one key on each side has \(5>4\) ideals; adding more keys preserves the existence of both types, proving nonpurity for all \(n\ge4\).

## Verification
The standalone Python verifier `verify.py` constructs all floor projections and tests commutation using literal transformation composition, independently enumerating every maximal clique. It compares these with the recursively generated search-tree families for \(2\le n\le7\), and checks distinctness, Catalan totals and sharp minimum-size counts through \(n=9\). Invocation: `python3 verify.py`. Its deterministic success marker is `VERIFY_OK_CATALAN_MAXIMAL_IDEMPOTENT_CLIQUES`. Finite checks supplement, but do not replace, the preceding proof.

## Relationship to prior work
Ganyushkin and Mazorchuk (arXiv:1006.0316) establish type-A Catalan/Kiselman quotient structure and count idempotents. Catarino, Higgins and Levi (2015) prove that inverse subsemigroups of the entire order-preserving transformation monoid on a chain are semilattices of idempotents (Theorem 2.7), without in that theorem enumerating maximal such families. Solomon's 1995 Catalan-monoid report supplies early context and presentations; only its abstract and descriptive page were accessible for this comparison. The classification here is of *all maximal commuting idempotent families and their size spectrum* rather than the count of individual idempotents, commuting pairs, all elements, or arbitrary maximal proper subsemigroups.

## Limitations
The theorem does not classify pairwise commuting families containing non-idempotents, partial Catalan monoids, or all order-preserving maps. Older terminology may conceal related classifications, particularly in semilattice and Catalan transformation monoid literature. The accessible published-source comparison is not an exhaustive historical priority determination. No independent mathematical audit has been performed.

## References
1. O. Ganyushkin and V. Mazorchuk, *On Kiselman quotients of 0-Hecke monoids*, arXiv:1006.0316v1 (2010-06-02), https://arxiv.org/abs/1006.0316 ; full accessible manuscript https://arxiv.org/html/1006.0316v3 .
2. P. Catarino, P. M. Higgins and I. Levi, *On inverse subsemigroups of the semigroup of orientation-preserving or orientation-reversing transformations*, Algebra and Discrete Mathematics 19 (2015), 162–171, https://repository.essex.ac.uk/13220/1/document.pdf .
3. A. Solomon, *Catalan monoids, monoids of local endomorphisms, and their presentations*, University of Sydney Research Report 95-6 (February 1995; revised 7 August 1995), https://ns.maths.usyd.edu.au/u/ResearchReports/Algebra/Sol/cat-mon-end.html .
