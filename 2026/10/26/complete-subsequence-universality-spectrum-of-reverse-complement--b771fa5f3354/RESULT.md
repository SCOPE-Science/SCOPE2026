# Complete subsequence-universality spectrum of reverse-complement palindromes

## Finding
Let \(q=2p\ge 2\), let \(\Sigma\) be a fixed labelled alphabet of \(q\) symbols, and fix a fixed-point-free involution \(a\mapsto\bar a\). For a finite word \(v\), write \(v^R\) for its reversal and \(\bar v\) for symbolwise complementation. Every reverse-complement palindrome of even length has the unique form \(W=v\overline{v^R}\). Define \(\iota(W)\) to be the largest integer \(k\ge0\) for which every word in \(\Sigma^k\) is a scattered subsequence of \(W\).

For \(m,k\ge0\), let \(N_q(m,k)\) count the **indexed**, length-\(2m\) reverse-complement palindromes of index exactly \(k\). Put
\[
A_q(x)=\frac{q!x^q}{\prod_{j=1}^{q-1}(1-jx)},\qquad
B_q(x)=\sum_{s=0}^{q-1}\binom qs\frac{s!x^s}{\prod_{j=1}^s(1-jx)},
\]
\[
H_p(x)=\sum_{s=p}^{2p-1}\binom p{s-p}2^{2p-s}\frac{s!x^s}{\prod_{j=1}^s(1-jx)}.
\]
The empty product and the term for \(s=0\) equal one. Then the **complete length-and-index generating function** is
\[
\boxed{\sum_{m,k\ge0}N_q(m,k)x^m u^k=\frac{B_q(x)+(u-1)H_p(x)}{1-u^2 A_q(x)}.}
\]
Here \(x\) marks **half-length**, so the physical length is \(2m\). For the binary complement, the formula simplifies to
\[
\boxed{\sum_{m,k\ge0}N_2(m,k)x^mu^k=\frac{1+(2u-1)x}{1-x-2u^2x^2}.}
\]
For every integer \(h\ge1\), the smallest possible physical length of such an \(h\)-universal word is exactly \(qh\), and **the exact number attaining this minimum** is
\[
\boxed{(q!)^{\lfloor h/2\rfloor}\begin{cases}
1,&h\text{ even},\\
2^p p!,&h\text{ odd}.
\end{cases}}
\]

## Assumptions and scope
The complement involution has no fixed symbols, so \(q\) is necessarily even and all nonempty reverse-complement palindromes have even length. Universality is relative to the entire fixed alphabet \(\Sigma\), including symbols not present in a particular half-word. The empty word contributes \(N_q(0,0)=1\). Counts distinguish different positions/strings and do not identify words under rotation, reversal, complementation, or relabelling. The formula holds for every \(q=2p\ge2\), every \(m\ge0\), and every \(k\ge0\).

## Proof
**1. Greedy arches.** Scan \(v\) from left to right. As soon as all \(q\) symbols have appeared, close a *complete arch* and reset the set of seen symbols. There is a unique factorization \(v=A_1\cdots A_t R\), with each \(A_i\) ending at the first occurrence of its last missing symbol, and with \(S=\operatorname{alph}(R)\subsetneq\Sigma\). The standard arch characterization gives \(\iota(v)=t\): the completed arches each contain every symbol, while fewer than \(t+1\) disjoint complete-alphabet blocks can be cut out because each greedy closing point is the earliest possible endpoint.

**2. Exact central correction.** The suffix \(\overline{v^R}=\overline{R^R}\overline{A_t^R}\cdots\overline{A_1^R}\) has exactly \(t\) complete arches when scanned from right to left, followed by the incomplete central block \(\overline{R^R}\). Thus \(W\) contains \(2t\) successive complete-alphabet blocks. It has at least \(2t+1\) if and only if \(R\overline{R^R}\) is alphabet-complete, equivalently \(S\cup\bar S=\Sigma\). Conversely, suppose \(W\) contains \(2t+1\) disjoint alphabet-complete consecutive blocks. The first \(t\) can be replaced by the leftmost greedy \(t\) arches without making them end later, and the last \(t\) by the rightmost greedy \(t\) arches without making them begin earlier. Consequently one alphabet-complete block lies in the central \(R\overline{R^R}\), and \(S\cup\bar S=\Sigma\). More than \(2t+1\) complete blocks would require two disjoint complete blocks inside this centre after the same boundary replacement. That is impossible: neither \(R\) nor \(\overline{R^R}\) is complete, so **every** complete block inside their concatenation must cross the one central junction, and two disjoint blocks cannot both cross it. Hence
\[
\boxed{\iota(v\overline{v^R})=2t+\mathbf 1_{\{S\cup\bar S=\Sigma\}}.}
\]
The argument concerns *disjoint consecutive alphabet-complete blocks*, which is equivalent to subsequence universality by the greedy-arch theorem; it does not assume that every target subsequence uses the same positions.

**3. Enumerating arches.** For a fixed length \(n\), the number of greedy arches with precisely \(n\) symbols is \(q!\,{n-1\brace q-1}\): before the last symbol exactly \(q-1\) distinct symbols are seen, and the last symbol is the unique missing one. The Stirling-number generating identity yields \(A_q(x)\). A remainder using exactly \(s<q\) symbols has \(\binom qs s!\,{n\brace s}\) possible length-\(n\) words; summing gives \(B_q(x)\). A symbol set \(S\) with \(S\cup\bar S=\Sigma\) contains both elements of exactly \(s-p\) complement pairs, and one element of each remaining pair. Thus there are \(\binom p{s-p}2^{2p-s}\) possible such sets of size \(s\). Multiplication by \(s!\,{n\brace s}\) and summation yields \(H_p(x)\). The unique factorization of every half-word is a sequence of complete arches followed by a remainder. Each arch contributes index two in the reverse-complement palindrome; a hitting remainder contributes an additional one. The geometric-series identity therefore gives
\[
\sum_{m,k\ge0}N_q(m,k)x^m u^k=\sum_{t\ge0}(u^2 A_q(x))^t\big(B_q(x)-H_p(x)+uH_p(x)\big),
\]
which equals the claimed rational function. For \(q=2\), inserting \(A_2(x)=2x^2/(1-x)\), \(B_2(x)=(1+x)/(1-x)\), and \(H_1(x)=2x/(1-x)\) gives the stated special case.

**4. Sharp minimum and multiplicity.** Every word that contains all \(q^h\) length-\(h\) words as subsequences has at least \(h\) copies of every alphabet letter (test constant target words); hence it has length at least \(qh\). This also follows from the arch bound. With \(h=2t\), take a half-word of length \(qt\) that is a concatenation of \(t\) alphabet permutations. Its reverse-complement palindrome has index exactly \(h\); conversely, each half of a shortest index-\(h\) palindrome must consist of exactly \(t\) arches of length \(q\), so there are \((q!)^t\) such half-words. With \(h=2t+1\), the half-length is \(qt+p\). Every shortest half-word must consist of exactly \(t\) length-\(q\) permutation arches followed by a \(p\)-letter remainder that hits all \(p\) involution pairs exactly once. There are \(2^p p!\) ordered choices for that remainder and \((q!)^t\) for the arches. Both constructions have the indicated index by Step 2. This proves sharpness and exact multiplicities.

## Verification
The accompanying standalone Python program `verify_rc_universal.py` makes three logically separate finite comparisons: (i) brute definition-level universality tests of explicitly listed target subsequences versus the central-correction identity for short half-words; (ii) dynamic-programming counts obtained from a q-symbol seen-mask automaton versus coefficients independently built from Stirling-number arch and remainder enumerators; and (iii) minimal-length counts and the absence of any shorter witnesses. It checks all \(35{,}856\) half-words in its specified exhaustive finite ranges, and generating-function coefficients through half-length \(60\) for \(q=2\), \(30\) for \(q=4\), \(22\) for \(q=6\), and \(17\) for \(q=8\). The program needs only the Python standard library and runs with `python verify_rc_universal.py`. Finite checks support, but do not replace, the all-length proof above.

## Relationship to prior work
Barker, Fleischmann, Harwardt, Manea and Nowotka [1] introduced these universality and arch-factorization results, and their Proposition 15 gives the exact index for ordinary even/odd palindromes. Their Lemma 17 and Proposition 18 concern concatenations \(w\pi(w)\) under alphabet permutations. In contrast, the present fixed-point-free reverse-complement symmetry requires \(v\bar{v^R}\), and its new **full bivariate enumeration and exact shortest-word multiplicities** are not stated in [1]. In particular, [1] implies that ordinary *even-length* palindromes have **even** universality index, whereas reverse-complement palindromes of shortest allowable length realize **every** positive index. Adamson [2] provides algorithms counting and enumerating unrestricted \(k\)-subsequence universal words; those unrestricted totals cannot be specialized just by substituting the length or alphabet size to count fixed points of the reverse-complement involution. Fleischmann, Germann and Nowotka [3] study remainders and repeated-word circular universality, rather than the present fixed-point count. Adamson and collaborators [4] count universal words accepted by a specified finite automaton, but their regular-language counting result does not cover the present symmetry language: its intersection with the regular set of words consisting of a fixed letter followed by its complement is the nonregular language of equally long complementary constant runs. The underlying arch theorem and Stirling generating identities are preexisting ingredients; they are not claimed as new.

## Limitations
This is an exact mathematical enumeration of labelled words fixed by a chosen **fixed-point-free** complement, not a formula for arbitrary alphabet involutions with fixed symbols, odd-length fixed points, approximate universality, cyclic classes, or embedding multiplicities. The elementary central-correction lemma should be viewed in light of the broader published arch-factorization method; the claimed contribution is the constrained **complete index distribution and sharp minimum-length spectrum**. No claim of independent peer verification is made. It remains possible that an equivalent symmetry-constrained enumeration exists under different terminology or as an unstated corollary of an unlocated treatment.

## References
[1] L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, arXiv:2003.04629 (first public 2020-03-10), especially Section 4, Proposition 15, Lemma 17 and Proposition 18. https://arxiv.org/abs/2003.04629

[2] D. Adamson, *Ranking and Unranking k-Subsequence Universal Words*, arXiv:2304.04583 (first public 2023-04-10), especially Sections 3–5. https://arxiv.org/abs/2304.04583

[3] P. Fleischmann, S. B. Germann, and D. Nowotka, *Scattered Factor Universality -- The Power of the Remainder*, arXiv:2104.09063 (first public 2021-04-19). https://arxiv.org/abs/2104.09063

[4] D. Adamson, P. Fleischmann, A. Huch, T. Koß, F. Manea, and D. Nowotka, *k-Universality of Regular Languages*, arXiv:2311.10658 (first public 2023-11-17), especially the introduction and counting-algorithm statement. https://arxiv.org/abs/2311.10658
