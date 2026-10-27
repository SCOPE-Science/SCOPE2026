# Interval orders classify the maximum-length classes of two-subsequence congruence

## Finding
Let \(\Sigma\) be a labeled alphabet of size \(q\ge 1\). Under Simon's two-subsequence congruence, two words are equivalent precisely when they contain the same distinct scattered subsequences of lengths at most two. Define \(\ell(C)\) to be the minimum length of a word representing a congruence class \(C\).

**Theorem.** Every class has \(\ell(C)\le 2q\). The classes attaining equality are in canonical bijection with the labeled interval orders on \(\Sigma\) (equivalently, the \((2+2)\)-free partial orders). The bijection sends a word \(w\) to the relation
\[
a<_{P_w}b\quad\Longleftrightarrow\quad \operatorname{last}_w(a)<\operatorname{first}_w(b).
\]
Consequently the number of maximum-minimum-length classes is precisely the established labeled-interval-order number \(I_q\), beginning
\[
I_1=1,\quad I_2=3,\quad I_3=19,\quad I_4=207,\quad I_5=3451.
\]
In particular this layer contains exactly \(19\) of the \(152\) ternary classes and \(207\) of the \(2326\) four-letter classes. Using the independently established asymptotic for labeled interval orders [3], this layer also has the exact transferred growth law
\[
I_q=\frac{12\sqrt{3}}{\pi^{5/2}}(q!)^2\sqrt{q}\left(\frac{6}{\pi^2}\right)^q\left(1+O(q^{-1})\right)\quad(q\to\infty).
\]
Modulo renaming letters, its classes correspond exactly to unlabeled interval orders. Furthermore, within this layer, inclusion of the observed subsequence sets reverses containment of the associated strict order relations.

## Assumptions and scope
All words are finite; the empty word is allowed. Letters are labeled and \(q\) is any positive integer. Scattered subsequences use strictly increasing positions and record **presence**, not multiplicity. An interval order is a partial order representable by intervals with \(a<b\) exactly when the interval for \(a\) ends strictly before that for \(b\) starts. The \((2+2)\)-free characterization is proved constructively below rather than assumed. \(I_q\) is the pre-existing enumeration of labeled interval orders, not a newly proposed integer sequence.

## Proof
**1. Universal two-occurrence reduction and sharp depth.** From any word \(w\), retain only the first and last occurrence of each letter (retaining just one when there is only one). This preserves every singleton and every repeated-letter subsequence \(aa\). For distinct letters \(a,b\), \(ab\) occurs in \(w\) exactly when \(\operatorname{first}_w(a)<\operatorname{last}_w(b)\); the retained endpoint word preserves that inequality. Therefore the reduced word has the identical length-at-most-two subsequence set and length at most \(2q\). If any \(aa\) is absent, the reduced representative has at most \(2q-1\) positions. Conversely, if each \(aa\) is present then every representative must contain each letter at least twice, so \(\ell(C)=2q\). Thus the deepest layer is exactly the set of classes having every repeated-letter observation \(aa\).

**2. Distinct-letter observations determine intervals.** For a word in that layer, define \(J_a=[\operatorname{first}_w(a),\operatorname{last}_w(a)]\). Then \(ab\) is absent for \(a\ne b\) exactly when \(\operatorname{last}_w(b)<\operatorname{first}_w(a)\), or \(b<_{P_w}a\). Thus the entire observation set is determined by the interval order \(P_w\), and conversely \(P_w\) can be recovered from the observation set. Because \(P_w\) is represented by intervals, it is an interval order. Distinct signatures cannot collapse to the same order, nor vice versa.

**3. Every interval order is realized by a twice-occurring word.** Take a finite \((2+2)\)-free poset \(P\) on \(\Sigma\). Its strict predecessor sets \(D(x)=\{y:y<x\}\) are linearly ordered by inclusion. Indeed, incomparable predecessor sets would provide \(u<x\) and \(v<y\) with neither crossed relation and with \(u,v\) and \(x,y\) incomparable, producing an induced \((2+2)\). List the distinct sets as \(D_1\subsetneq\cdots\subsetneq D_m\), and define \(i(x)\) by \(D(x)=D_{i(x)}\). Define \(j(x)\) as the smallest index with \(x\in D_{j(x)}\), or \(m+1\) if none. Because \(x\notin D(x)\) and the sets are nested, \(j(x)>i(x)\). Put the left endpoint at \(2i(x)\) and the right endpoint at \(2j(x)-1\). For distinct \(x,y\),
\[
2j(x)-1<2i(y)\ \Longleftrightarrow\ j(x)\le i(y)\ \Longleftrightarrow\ x\in D(y)\ \Longleftrightarrow\ x<y.
\]
Separate tied left endpoints and tied right endpoints by sufficiently small distinct perturbations; this changes no cross-type comparison or interval positivity. Sort the resulting \(2q\) pairwise distinct endpoints, writing the letter \(x\) at both endpoints of its interval. This gives a length-\(2q\) word with the requested order and all \(xx\) present. The construction also proves directly the converse interval-order characterization used in the theorem.

**4. Counting and containment.** Steps 2 and 3 give inverse maps between deepest-layer congruence classes and labeled interval orders, proving the exact \(I_q\) count. For distinct letters \(a,b\), \(ab\) is present precisely when \(b\not<_{P_w}a\). All singleton and diagonal-pair observations are fixed in this layer. Thus one observation set contains another precisely when its associated strict order relation is contained in the other's strict relation, with the inclusion direction reversed. Alphabet permutation commutes with the construction, yielding the unlabeled orbit statement.

## Verification
The accompanying standard-library program `verify_interval_simon.py` performs two independent complete finite calculations for each \(1\le q\le5\). A breadth-first traversal of the exact two-subsequence update automaton finds all attainable signatures and their shortest realizing lengths. Separately, a generator enumerates every length-\(2q\) word containing two copies of each letter, computes the subsequences by direct nested loops, and computes its interval relation using first and last positions. Both directions of the relation-to-signature bijection are checked, and the deepest-layer sets are compared with the automaton. The program checks total class counts \(3,16,152,2326,52132\), deepest-layer counts \(1,3,19,207,3451\), and \(113400\) doubled-endpoint words at \(q=5\). The all-alphabet theorem follows from the proof, not from finite enumeration.

## Relationship to prior work
Karandikar, Kufleitner and Schnoebelen (arXiv:1310.1278) studied the index of Simon's congruence and tabulated total two-congruence class counts on small alphabets. Fleischmann, Höfer, Huch and Nowotka (arXiv:2306.14192, first made public 2023-06-25) characterized binary classes using arch factorizations and investigated ternary classes, motivating a complementary all-alphabet structural question. Brightwell and Keller (arXiv:1111.6766) enumerated labeled interval orders asymptotically; OEIS A079144 records the established values \(I_q\). The contribution here is **not** the previously known numbers or the known notion of interval order, but the explicit all-alphabet bijection identifying the maximal shortest-representative layer and its observation-containment structure. The relevant definitions, theorem statements, index classifications and counting assertions in these primary works were inspected; no exact interval-order identification of this Simon-congruence layer was found in the inspected material. Unindexed or older equivalent descriptions remain a risk.

## Limitations
The theorem counts only classes whose shortest representative has length exactly \(2q\), not all two-congruence classes or higher levels of Simon's congruence. Counts and asymptotics of labeled interval orders are established external results, not independently reproved here. The novelty assessment is based on examined sources and targeted literature/database searches, not a proof of global priority. Independent scholarly validation has not been performed.

## References
1. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *Alpha-beta Factorization and the Binary Case of Simon's Congruence*, arXiv:2306.14192 (first version 2023-06-25), https://arxiv.org/abs/2306.14192.
2. P. Karandikar, M. Kufleitner, Ph. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, arXiv:1310.1278 (2013), https://arxiv.org/abs/1310.1278.
3. G. Brightwell, M. T. Keller, *Asymptotic Enumeration of Labelled Interval Orders*, arXiv:1111.6766 (2011), https://arxiv.org/abs/1111.6766.
4. OEIS A079144, *Number of labeled interval orders on n elements*, https://oeis.org/A079144.
