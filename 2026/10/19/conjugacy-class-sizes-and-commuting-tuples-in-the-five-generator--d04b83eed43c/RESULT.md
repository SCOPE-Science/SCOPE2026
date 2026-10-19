# Conjugacy-class sizes and commuting tuples in the five-generator free left-regular-band algebra

## Finding
Let \(F_5\) be the free left-regular band on five generators: its elements are injective words in five letters (including the empty word), and multiplication appends the letters of the right factor not already present in the left factor, in their original order. Let \(k\) be any field, \(A=kF_5\), \(J=\operatorname{rad}(A)\), and \(G=1+J\). Define \(H_5\) as the smooth unipotent group of triples \((a,b,z)\in k^5\times k\times k^5\) under
\[
 (a,b,z)(a',b',z')=(a+a',b+b',z+z'+ab'),
\]
where \(ab'\) is scalar multiplication of the column \(a\) by \(b'\).

There is an isomorphism of affine group schemes over \(k\), valid in every characteristic,
\[
 \boxed{G\cong H_5^{20}\times\mathbb G_a^{74}.}
\]
In particular, \(\dim J=294\), \(\dim Z(G)=174\), and \(G\) has nilpotency class exactly two.

For every prime power \(q\) and every integer \(s\ge1\), the number of **ordered pairwise-commuting** \(s\)-tuples in \(G(\mathbb F_q)\) is
\[
 \boxed{C_s(q)=q^{174s}\bigl(q^{5s}+q^5(q^s-1)\bigr)^{20}.}
\]
If \(K_q(T)=\sum_{r\ge0} k_r(q)T^r\) is the conjugacy-class-size enumerator, in which \(k_r(q)\) is the number of conjugacy classes containing exactly \(q^r\) elements, then
\[
 \boxed{K_q(T)=q^{74}\bigl(q^5+q^4(q^5-1)T+q^5(q-1)T^5\bigr)^{20}.}
\]
Consequently the possible conjugacy-class sizes are precisely \(q^r\), with
\[
 r\in\{0,1,\ldots,88,90,91,92,95,96,100\};
\]
all six exponents \(89,93,94,97,98,99\) between zero and 100 are absent. The total number of conjugacy classes is \(q^{74}(q^9+q^4(q^2-1))^{20}\).

## Assumptions and scope
The conclusions apply to the **principal unipotent subgroup** \(1+J\) of the algebra unit group, not to the full group \(A^\times\). The coefficient field \(k\) is arbitrary for the group-scheme decomposition; \(\mathbb F_q\) denotes an arbitrary finite field for counting assertions. The arity \(s\) is an integer at least one. All conjugacy classes are classes inside \(G(\mathbb F_q)\). The group \(H_5\) is not the conventional \((2n+1)\)-dimensional extraspecial Heisenberg group; it is the rectangular \((5,1)\) two-step unipotent matrix group with a five-dimensional center.

## Proof
**Quiver input.** Saliola's theorem [1, Theorems 8.1 and 13.1] identifies \(kF_n\) with the path algebra of an acyclic quiver whose vertices are subsets \(X\subseteq[n]\) and which has exactly \(|X\setminus Y|-1\) arrows from \(X\) to a proper subset \(Y\subset X\) when \(|X\setminus Y|\ge2\), and no other arrows. This theorem holds over any field. The radical is spanned by all positive-length paths; composition concatenates composable arrows.

For \(n=5\), there are \(32\) vertices and \(194\) arrows. Every arrow lowers subset cardinality by at least two, so there are no paths of length three. Exactly \(100\) paths have length two, giving \(\dim J=194+100=294\) and \(J^3=0\). A length-two path must have intermediate subset \(U\) of cardinality \(2\) or \(3\). There are ten choices of each cardinality. For \(|U|=2\), precisely five arrows enter \(U\) (three from four-element sets and two from the five-element set), and one arrow leaves \(U\) (to the empty set). For \(|U|=3\), one arrow enters \(U\) (from the five-element set), and precisely five arrows leave \(U\) (two to the empty set and one to each singleton contained in \(U\)). These are the complete lists of arrows that can participate in a length-two path.

Each of the \(20\) intermediate subsets therefore supports an eleven-dimensional nilpotent subalgebra with five arrows on one side, one on the other, and five concatenations. Its only nonzero products pair an entering arrow with a leaving arrow; the five resulting length-two paths are linearly independent. A length-one arrow belongs to **at most one** of these blocks: its source is of size at least four when it is entering one of the intermediates, and its source is of size at most three when it is leaving one. Distinct intermediates share neither such arrows nor their concatenations, and products between blocks vanish. The remaining \(194-20\cdot6=74\) arrows participate in no length-two path and annihilate all of \(J\) on both sides. Thus, as nonunital nilpotent algebras,
\[
 J\cong B^{\oplus 10}\oplus(B^{\mathrm{op}})^{\oplus 10}\oplus k_{\mathrm{zero}}^{74},
\]
where \(B=k^5\oplus k\oplus k^5\) has multiplication \((a,b,z)(a',b',z')=(0,0,ab')\), and \(k_{\mathrm{zero}}^{74}\) means the vector space with identically zero multiplication. (Which orientation is labeled \(B\) is immaterial.) Passage to \(1+J\) converts algebra direct sums to group direct products. Polynomial group inversion identifies \(1+B^{\mathrm{op}}\) with \(1+B\), proving the group-scheme isomorphism. Since the bilinear commutator \((a,b),(a',b')\mapsto ab'-a'b\) is nonzero, the class is two; its common kernel on \(k^5\oplus k\) is zero, giving \(\dim Z(G)=20\cdot5+74=174\).

**Commuting tuples.** In one factor \(H_5\), the central \(z\)-coordinates are arbitrary. Write each noncentral coordinate as \((a_i,b_i)\in k^5\times k\), for \(1\le i\le s\). Pairwise commutation is equivalent to \(a_i b_j=a_j b_i\) for every pair of indices. If the vector \((b_1,\dots,b_s)\) vanishes, the \(a_i\) are arbitrary, yielding \(q^{5s}\) assignments. Otherwise, there is a *unique* vector \(v\in\mathbb F_q^5\) with \(a_i=v b_i\) for all \(i\), yielding \((q^s-1)q^5\) assignments. Multiplying by \(q^{5s}\) for central coordinates, taking the twentieth power, and allowing \(q^{74s}\) for the square-zero summand proves the displayed \(C_s(q)\).

**Conjugacy classes.** For \(g=(a,b,z)\in H_5(\mathbb F_q)\), its commutator map has image \(\{ab'-a'b:a'\in\mathbb F_q^5,b'\in\mathbb F_q\}\). Its dimension is \(0\) if \(a=b=0\), \(1\) if \(b=0,a\ne0\), and \(5\) if \(b\ne0\). The conjugacy class of \(g\) has the cardinality of that image because the group is two-step with central commutator. Including arbitrary \(z\), the respective numbers of group **elements** are \(q^5\), \(q^5(q^5-1)\), and \(q^{10}(q-1)\). Dividing each by its conjugacy-class size gives respectively \(q^5\), \(q^4(q^5-1)\), and \(q^5(q-1)\) conjugacy classes. Taking direct products of twenty factors and the central \(q^{74}\)-element group proves \(K_q(T)\). Class-size exponents are precisely \(a+5b\) for integers \(a,b\ge0\) with \(a+b\le20\), which simplifies to the stated explicit exponent set. Setting \(T=1\) yields the total class count.

## Verification
The accompanying standalone `verify.py` constructs Saliola's directed multiquiver using integer bitmasks and checks its arrows, all composable edge pairs, unique assignment to twenty blocks, and the 74 zero-product arrows. For rectangular-group commuting equations it exhaustively enumerates dimensions-six noncentral coordinates for \((q,s)=(2,1),(2,2),(2,3),(3,1),(3,2)\). It checks the three conjugacy ranks for \(q=2,3,5\), the class-number and weighted-size identities, and the exact set of attainable global class exponents. Running `python3 verify.py` prints `VERIFY_OK` upon success. These are finite checks; the field-uniform, all-arity assertions are established by the preceding proof.

## Relationship to prior work
Saliola [1] proves the quiver and path-algebra realization of \(kF_n\); these important structural results are **not new here**. Hennecart and Perry [2, Theorems 3.18 and 3.12 and Proposition 4.1] give radical-preserving source/sink splitting and count *commuting pairs* in general short quiver radicals. Consequently the special **two-tuple total** above is already accessible by specialization of their stronger theorem and is **not claimed as an independent novelty**. Their general radical-preserving methods also provide an alternative route toward factor decomposition, although the explicit twenty-block allocation requires applying the subset-quiver multiplicities.

The present focused classification supplies the exact five-letter block allocation and, most distinctly, the **entire conjugacy-class-size distribution**, its six excluded exponents, and a simultaneous formula for **all** commuting arities. These finer distributions do not follow numerically from a prior count of commuting pairs alone. Brauner, Commins and Reiner [3] study invariant subalgebras and symmetric-group representations of the same monoid algebra rather than its unipotent radical conjugacy strata. A stronger, unlocated classification of class sizes or all-arity commuting tuples might still imply the result; no exhaustive novelty guarantee is asserted.

## Limitations
The theorem concerns \(n=5\) and the principal unipotent group; it does not enumerate conjugacy classes in the full algebra unit group. The displayed class polynomial is an exact arithmetic invariant but does not classify individual conjugacy representatives or character degrees. The free left-regular-band family first has paths of length three at \(n=6\); the present two-step reduction does not extend verbatim to that case. The conclusions are supported by an algebraic proof and finite tests, not independent external audit. Originality is conditional on the compared accessible literature; another consequence of the 2022 radical-preserving operations or unlocated work may already describe these fine distributions.

## References
[1] Franco V. Saliola, *The Quiver of the Semigroup Algebra of a Left Regular Band*, arXiv:math/0608698v1 (first posted 2006-08-28), Theorems 8.1 and 13.1. https://arxiv.org/abs/math/0608698

[2] Lucien Hennecart and Nikolai Perry, *A Quiver Analogue of Higman's Conjecture*, arXiv:2208.07738v1 (2022), Sections 3–4, particularly Theorems 3.12, 3.18 and Proposition 4.1. https://arxiv.org/abs/2208.07738

[3] Sarah Brauner, Patricia Commins and Victor Reiner, *Invariant Theory for the Free Left-Regular Band and a \(q\)-Analogue*, arXiv:2206.11406 (2022), Sections 1–2. https://arxiv.org/abs/2206.11406
