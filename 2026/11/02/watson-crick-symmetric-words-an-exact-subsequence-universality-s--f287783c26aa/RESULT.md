# Watson–Crick symmetric words: an exact subsequence-universality spectrum

## Finding

Let \(\Sigma\) be a labeled alphabet of size \(q=2d\), where \(d\ge1\), and let \(\pi\) be any fixed-point-free involution on \(\Sigma\). Extend the reverse-complement operation \(\theta\) to words by \(\theta(a_1\cdots a_n)=\pi(a_n)\cdots\pi(a_1)\). A word satisfying \(W=\theta(W)\) is called a Watson–Crick (WC) palindrome. Every such word has even length and is uniquely \(W=H\theta(H)\).

The scattered-subsequence universality index \(\iota(W)\) is the largest nonnegative integer \(k\) such that *every* word in \(\Sigma^k\) occurs as a not-necessarily-contiguous subsequence of \(W\). Let \(C_q(2h,k)\) count length-\(2h\) WC palindromes of index exactly \(k\). These counts are independent of the pairing \(\pi\), and have the following **exact rational bivariate generating function** for all \(q=2d\ge2\):

\[
\boxed{\displaystyle
\sum_{h,k\ge0} C_q(2h,k)z^{2h}u^k
=\frac{R_q(z^2)+(u-1)U_q(z^2)}{1-u^2 A_q(z^2)}.}
\]

Here, for \(j\ge1\), set \(B_j(t)=j!\,t^j/\prod_{i=1}^j(1-it)\), and \(B_0(t)=1\). The three explicit rational functions are

\[
\begin{aligned}
A_q(t)&=q\,t\,B_{q-1}(t),\\
R_q(t)&=\sum_{j=0}^{q-1}\binom qj B_j(t),\\
U_q(t)&=\sum_{j=d}^{q-1}\binom d{j-d}2^{q-j} B_j(t).
\end{aligned}
\]

In particular, for the binary swapping involution the distribution is

\[
\boxed{\displaystyle\sum_{h,k\ge0}C_2(2h,k)z^{2h}u^k
=\frac{1-z^2+2uz^2}{1-z^2-2u^2z^4}.}
\]

For every integer \(k\ge1\), the minimum length of a \(k\)-universal WC palindrome is exactly \(qk\). **All** minimum-length solutions and their counts are as follows. If \(k=2m\), the word is \(H\theta(H)\) with \(H=P_1\cdots P_m\), each \(P_i\) a permutation of \(\Sigma\). There are \((q!)^m\) such words. If \(k=2m+1\), the word is \(H\theta(H)\) with \(H=P_1\cdots P_mS\), where the \(P_i\) are permutations and \(S\) is a permutation of a set containing exactly one symbol from each \(\pi\)-pair. There are

\[
\boxed{\displaystyle (q!)^m\,2^d d!}
\]

such minimum-length words. Unlike ordinary palindromic hosts, the reverse-complement constraint does not increase the shortest universal host length above the unrestricted minimum.

## Assumptions and scope

The alphabet is fixed, finite, labeled, and even-sized; \(\pi\) is a fixed-point-free letter involution, not necessarily the particular pairing of consecutive integer labels. Only indexed linear words are counted, not necklaces or orbits under relabeling. Subsequence embeddings allow gaps of any nonnegative size. The empty word is included with index zero; all nonempty WC palindromes have even lengths. Counts in the generating function are **exact-index counts**, not counts with index at least \(k\).

For any word \(H\), its greedy arch factorization is \(H=A_1\cdots A_r S\), where each \(A_i\) is the shortest full-alphabet prefix of the remaining suffix, and \(S\) omits at least one letter. Every arch contains all \(q\) letters. The number of arches is \(r=\iota(H)\). For a finite set \(T\subseteq\Sigma\), write \(\pi(T)=\{\pi(a):a\in T\}\).

## Proof

**1. Symmetric arch lemma.** Write \(H=A_1\cdots A_r S\) as above and \(W=H\theta(H)\). Then

\[
\boxed{\displaystyle
\iota(W)=2r+\mathbf1_{\{\operatorname{alph}(S)\cup\pi(\operatorname{alph}(S))=\Sigma\}}.}
\]

Indeed, each \(A_i\) and its reverse-complement \(\theta(A_i)\) is full-alphabet, so \(W\) contains \(2r\) disjoint full-alphabet intervals; if the middle word \(S\theta(S)\) is full-alphabet, it supplies an additional interval. Conversely, a decomposition of \(W\) into more than \(2r\) disjoint full-alphabet intervals has at most \(r\) intervals wholly in the left half (because \(\iota(H)=r\)) and at most \(r\) wholly in the right half (because reversal and letter permutation preserve the index). Thus exactly one of any \(2r+1\) intervals must cross the midpoint, with \(r\) intervals on each side. The leftmost greedy \(r\) arches finish no later than any other disjoint selection of \(r\) full-alphabet intervals in \(H\); analogously the rightmost co-arches start no earlier on the right. Hence the midpoint-crossing interval lies inside \(S\theta(S)\), which must contain every letter. No \(2r+2\) intervals can exist, since at most one disjoint interval crosses the midpoint. The equivalence follows. The argument includes \(r=0\).

**2. The generating function.** A length-\(\ell\) word on a *fixed* set of exactly \(j\) letters that uses every one of them is counted by \(j!\,\bigl\{\!\!\begin{smallmatrix}\ell\\j\end{smallmatrix}\!\!\bigr\}\), whose ordinary generating function is \(B_j(t)\); this follows by counting surjections, or from the standard Stirling-number recurrence. An incomplete suffix has precisely \(j<q\) distinct letters in \(\binom qj\) choices, yielding \(R_q(t)\). Every minimal arch ends in a letter not occurring earlier in that arch, while its preceding part uses each of the other \(q-1\) letters at least once. Therefore its generating function is \(A_q(t)=qtB_{q-1}(t)\).

By unique greedy factorization, the generating function for halves \(H\) with exactly \(r\) arches is \(A_q(t)^rR_q(t)\). Among incomplete remainders \(S\), the extra central arch in Step 1 exists iff the used alphabet meets every one of the \(d\) involution pairs. If \(S\) uses exactly \(j\) letters, choose \(j-d\) involution pairs to use twice and choose one letter from each of the remaining \(q-j\) pairs. This gives \(\binom d{j-d}2^{q-j}\) possible used sets; note that \(d\le j\le q-1\). Their aggregate remainder generating function is exactly \(U_q(t)\).

Consequently, for every \(r\ge0\), half-words yielding index \(2r\) have generating function \(A_q(t)^r(R_q(t)-U_q(t))\), while those yielding index \(2r+1\) have \(A_q(t)^rU_q(t)\). Marking the full-word length by \(z\), the half length by \(t=z^2\), and the index by \(u\), geometric summation over \(r\) yields the boxed bivariate formula. For \(q=2\), one has \(A_2(t)=2t^2/(1-t)\), \(R_2(t)=(1+t)/(1-t)\), and \(U_2(t)=2t/(1-t)\), giving the displayed binary specialization. Setting \(u=1\) gives \(1/(1-qz^2)\), as required by the bijection between length-\(2h\) WC palindromes and unrestricted halves of length \(h\).

**3. Shortest universal WC palindromes.** Every length-\(k\) constant-letter pattern must occur, so any \(k\)-universal word has at least \(k\) occurrences of each of the \(q\) letters and hence length at least \(qk\). Equality means precisely \(k\) complete greedy arches of length \(q\), hence a concatenation of \(k\) permutation blocks, and conversely such a concatenation is \(k\)-universal. (More explicitly: each greedy arch requires at least \(q\) letters and equality of their total lengths forces every arch to be a permutation.)

At length \(qk\) an involution-symmetric word is uniquely \(H\theta(H)\). For \(k=2m\), it is a concatenation of \(2m\) permutation blocks. The midpoint is a block boundary; the first \(m\) permutations can be arbitrary and the other \(m\) are forced by reverse complementation. Thus exactly \((q!)^m\) minimum solutions exist.

For \(k=2m+1\), the midpoint bisects the central permutation block of length \(q=2d\). Such a permutation is invariant under reverse complementation iff its first \(d\) letters contain exactly one representative of each of the \(d\) disjoint complement pairs, in any order, with the last \(d\) forced. There are \(2^d d!\) choices for this central permutation; the first \(m\) outer permutation blocks are arbitrary, yielding \((q!)^m2^dd!\) solutions. They attain the lower bound, proving the asserted minimum and complete classification.

## Verification

The supplied standalone program `verify_wc_universality.py` constructs \(W=H\theta(H)\) from all halves in several alphabets. It checks the index by greedy arches and independently by literal embedding of every candidate pattern in selected exhaustive ranges. Independently formed surjection counts give the predicted bivariate coefficient tables, and independently constructed permutation-block families give the exact shortest-host sets. The successful run prints `WC_UNIVERSAL_VERIFY_OK symmetric_hosts=32199 literal_checks=2647 bivariate_profiles=24 shortest_classifications=10`.

The verified half lengths are \(0\le h\le9\) for \(q=2\), \(0\le h\le7\) for \(q=4\), and \(0\le h\le5\) for \(q=6\). All these finite tests are supplementary to the all-parameter proofs, not substitutes for them. The test canonicalizes \(\pi\) by swapping consecutive letter pairs, which suffices up to uniform alphabet relabeling.

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea and Nowotka (2020), Proposition 15, already determines the universality index of *ordinary* palindromes in terms of the arch factorization of their halves. Their Proposition 18 treats concatenation with an alphabet-permuted copy, not the reverse-complement antimorphic involution \(H\theta(H)\) studied here. Those existing results and the general arch-factorization theorem are ingredients, not new claims. The present classification replaces the ordinary-palindrome missing-letter condition by coverage of all disjoint involution pairs and enumerates the complete bivariate index spectrum and every shortest host over any fixed-point-free involution.

Mahalingam, Pandoh and Maity (2020) study Watson–Crick palindromes and their conjugates, but their definitions and the inspected results concern conjugacy, not scattered-subsequence universality. Schnoebelen and Veron (2023) develop general arch-jumping algorithms for indices, without giving this reverse-complement-symmetric enumeration. The exact total number of unrestricted universal words, and the existence of generic word algorithms, do not directly imply the symmetry-restricted coefficient formulas or optimum multiplicities without the involution-orbit analysis.

## Limitations

The theorem concerns linear WC palindromes under a fixed-point-free pairing; it does not cover involutions with fixed letters, circular universality, errors or gap-bounded subsequence embeddings, or biological binding kinetics. The generator is an exact formal series identity, not an estimate. Computational tests are finite. The related full-text comparison may still have overlooked an equivalent theorem in indexed or unindexed literature; novelty is not certified independently.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, 2020, arXiv:2003.04629v1, especially Proposition 15 and Proposition 18. https://arxiv.org/abs/2003.04629
2. K. Mahalingam, P. Pandoh, and A. Maity, *Theta Palindromes in Theta Conjugates*, 2020, arXiv:2008.00255v1. https://arxiv.org/abs/2008.00255
3. P. Schnoebelen and J. Veron, *On Arch Factorization and Subword Universality for Words and Compressed Words*, 2023, arXiv:2304.11932v1. https://arxiv.org/abs/2304.11932
