# Palindromic-return rigidity of rich double-occurrence words

## Finding

Fix an integer \(q\geq 1\). A **double-occurrence word** is a linear word \(w\) of length \(2q\) on exactly \(q\) symbols in which every symbol occurs twice. A *palindromic factor* means an ordinary contiguous palindrome, with symbols unchanged by reversal; two words differing only by a bijective alphabet relabeling are identified only when explicitly counting canonical classes. Call \(w\) **rich** when it has exactly \(2q+1\) distinct palindromic factors, including the empty word.

For pairwise distinct symbols \(a_1,\ldots,a_r\), write a **rainbow block** for the word \(a_1\cdots a_r a_r\cdots a_1\), where \(r\geq1\). A **crossing block** is \(abab\), where \(a\ne b\).

**Classification theorem.** The following are equivalent for every double-occurrence word \(w\):

1. \(w\) is rich.
2. For every symbol \(a\), the factor beginning at its first occurrence and ending at its second occurrence is an ordinary palindrome.
3. \(w\) has a **unique** concatenation into rainbow blocks and crossing blocks, with distinct blocks using disjoint alphabets.

Two symbols *interlace* when their four occurrences appear in the order \(abab\) or \(baba\). Let \(e(w)\) count unordered interlacing pairs. For canonical words (letters relabeled \(1,2,\ldots,q\) in order of first appearance), let \(c_{q,t}\) count rich words with \(e(w)=t\), and put \(c_{0,0}=1\). Then the **complete crossing-refined enumeration** is

\[
\sum_{q,t\geq0}c_{q,t}z^q u^t
=\frac{1-z}{1-2z-u z^2+u z^3}.
\]

In particular, the number \(c_q=\sum_t c_{q,t}\) of rich canonical words is determined by

\[
\sum_{q\geq0}c_q z^q=\frac{1-z}{1-2z-z^2+z^3},
\qquad c_0=1,\ c_1=1,\ c_2=3,
\]

\[
c_q=2c_{q-1}+c_{q-2}-c_{q-3}\quad(q\geq3).
\]

The first values for \(q=1,2,3,4,5,6,7,8\) are \(1,3,6,14,31,70,157,353\). There are exactly \(q!c_q\) rich words on a fixed labeled \(q\)-symbol alphabet. Exactly \(2^{q-1}\) canonical rich words have no interlacing pairs for every \(q\geq1\). Furthermore, the irreducible rich double-occurrence words, meaning those with no proper nonempty double-occurrence prefix, are precisely the single rainbow blocks and the crossing block; at fixed \(q\) there are \(1\), \(2\), and \(1\) canonical irreducibles for \(q=1\), \(q=2\), and \(q\geq3\), respectively.

## Assumptions and scope

Words are **linear**, not circular. The alphabet comprises exactly the \(q\) letters occurring twice, and equality of palindrome factors is literal symbolwise equality. The canonical normalization preserves positions and renames symbols by order of first appearance; it does not identify rotation or reversal. The count \(e(w)\) concerns unordered pairs of **distinct letters**, not crossing positions of one letter. The generating functions are formal power series in \(z\) and \(u\), and \(q=0\) supplies only the empty-word counting convention.

The classification is not a statement about arbitrary repeated-letter multiplicities, palindromic subsequences, or double-occurrence words considered symmetric up to renaming under reversal.

## Proof

**Step 1: Richness forces each two-occurrence span to be a palindrome.** A standard characterization of rich finite words says that every complete return to an ordinary palindromic factor is itself a palindrome (Glen–Justin–Widmer–Zamboni, Theorem 2.14). The span between the two occurrences of a letter \(a\) is a complete return to the one-letter palindrome \(a\), since no third \(a\) occurs. Hence (1) implies (2). This implication can also be deduced directly from the unique-palindromic-suffix characterization.

**Step 2: Analyze the first letter.** Assume (2). Write \(w=aUaV\), taking \(a\) to be the first symbol of \(w\) and the two displayed occurrences to be its only occurrences. The hypothesis says \(U\) is a palindrome. Each distinct symbol other than \(a\) occurs at most twice in \(U\). Any symbol appearing exactly once in a palindrome must occupy its central position; hence there can be *at most one* such symbol in \(U\). Every symbol appearing twice in \(U\) must occupy positions symmetric about the center.

If no symbol occurs exactly once in \(U\), its paired symbols occur in symmetric pairs. Consequently \(aUa\) is necessarily a rainbow block, and every symbol appearing in this block is exhausted there. Its suffix \(V\) is another double-occurrence word on disjoint letters.

Otherwise, let \(b\) be the unique symbol occurring once in \(U\). It is central, so \(U=XbX^{\mathrm R}\), where the letters of \(X\) are pairwise distinct, and all letters of \(X\) occur exactly twice inside \(U\). The second occurrence of \(b\) lies in \(V\). If \(X\) were nonempty, let \(x\) be its last letter. Immediately after the first occurrence of \(b\) comes \(x\). Because the span from the first \(b\) to the second \(b\) is also a palindrome, the letter immediately preceding the second \(b\) would have to be \(x\). But both copies of \(x\) occur within \(U\), before the second \(a\), whereas the second \(b\) lies after that \(a\). This is impossible. Thus \(X\) is empty, and \(w\) begins \(aba\).

The span from the first \(b\) to the second \(b\) now has the form \(baYb\) and is palindromic. Since the only occurrence of \(a\) inside that span is its first interior letter, \(a\) must be the unique central letter. Thus \(Y\) is empty, \(w\) begins \(abab\), and both \(a\) and \(b\) are exhausted. The remaining suffix is again a double-occurrence word on disjoint letters.

Applying the argument recursively to the suffix proves (2) implies the existence in (3). The first symbol and the position of its partner determine which of the two displayed first-block cases occurs, including the block length; therefore the decomposition is unique.

**Step 3: Every such concatenation is rich.** A rainbow on \(r\) symbols has exactly \(r\) distinct one-letter palindromes and exactly \(r\) further palindromes, namely its centered even palindromes of lengths \(2,4,\ldots,2r\). Thus it has \(2r\) nonempty palindromic factors. A crossing block \(abab\) has exactly the four nonempty palindromic factors \(a,b,aba,bab\). No palindrome of length at least two can cross the boundary between two blocks with disjoint alphabets: its first and last letters would then belong to disjoint sets and could not match. Nonempty palindromic-factor sets of different blocks are disjoint as well. Hence a concatenation of blocks on \(q\) symbols has exactly \(2q\) nonempty palindromic factors, and is rich. This proves (3) implies (1). Each listed block plainly also has palindromic two-occurrence spans, completing the equivalence.

**Step 4: Crossing statistic and exact enumeration.** In a rainbow, letter-pair intervals are nested and none interlace; in \(abab\), exactly one unordered pair interlaces; and pairs in distinct disjoint blocks never interlace. Therefore \(e(w)\) equals the number of crossing blocks. Under first-appearance normalization, the concatenation grammar corresponds bijectively to an ordered composition of \(q\): for each part size \(r\geq1\), use one rainbow block, and for \(r=2\) there is the additional crossing option. As each block consumes the next \(r\) unused canonical letters, it introduces no additional relabeling factor. The generating series for a single block is

\[
B(z,u)=\sum_{r\geq1}z^r+uz^2=\frac{z}{1-z}+uz^2.
\]

The unique ordered sequence of blocks has generating series \(1/(1-B(z,u))\), which simplifies to the displayed bivariate rational function. Specializing \(u=1\) gives the recurrence and total count. Specializing \(u=0\) gives \((1-z)/(1-2z)\), whose coefficient at \(z^q\) is \(2^{q-1}\) when \(q\geq1\). Each canonical pattern admits exactly \(q!\) bijective choices of labels in first-appearance order, establishing the labeled count.

Finally, an irreducible double-occurrence word cannot contain more than one of the constructed blocks, since the first block would be a proper double-occurrence prefix; conversely a rainbow or crossing block has no proper nonempty double-occurrence prefix. This proves the irreducible classification.

## Verification

A standalone Python checker (`check_rich_dow.py`) enumerates all \((2q-1)!!\) first-appearance-canonical double-occurrence words independently for \(q=1,\ldots,7\). On each word it compares three predicates: direct enumeration of all distinct contiguous palindromes, palindromicity of every letter-to-itself span, and the unique-block parser. It also computes \(e(w)\) directly from endpoints and compares the full distribution with the coefficient recurrence of the bivariate rational generating function.

The checker completed successfully over \(146599\) words in total. It found exactly \(1,3,6,14,31,70,157\) rich canonical words for \(q=1,\ldots,7\), with crossing distributions recorded in `VERIFICATION.md`. The infinite statements follow from the preceding proof; finite exhaustiveness is explicitly limited to these values of \(q\).

Run with `python3 check_rich_dow.py`; it uses only the Python standard library. The checker is included in the same package and not referenced from another record.

## Relationship to prior work

Glen, Justin, Widmer, and Zamboni's characterization of rich words via complete palindromic returns supplies the necessary condition in Step 1. Rukavicka's 2019 study of rich-word extensions discusses the general richness framework but not this double-occurrence grammar or crossing-refined enumeration. Cruz, Ferrari, Jonoska, Nabergall, and Saito's 2018 preprint develops double-occurrence insertion and return patterns, but its stated theorems classify equivalent insertions, not rich double-occurrence words. Burns and Muche enumerate *palindromic* double-occurrence words in the different sense of equality to their reverse **up to alphabet relabeling**; their counting problem is not the present ordinary-palindromic-factor property.

The *univariate numerical sequence* \(1,3,6,14,31,70,\ldots\) (after its initial shift) already appears in OEIS A006356 in other combinatorial interpretations. Thus numerical coincidence alone is **not** asserted to be novel. The claim here is the complete structural classification of rich double-occurrence words and the crossings-refined bivariate generating function. A prior derivation of these statements under unindexed terminology remains a residual originality risk.

## Limitations

The theorem does not classify words in which any symbol has multiplicity other than two, and does not count circular or reversal-identified classes. Richness here uses contiguous palindromic factors, not scattered palindromes or a weaker complete-return condition in arbitrary words. The scope also differs from palindromic double-occurrence *equivalence classes* under reversal and relabeling. The computational enumeration is finite; it is not an independent proof for arbitrary \(q\). No independent external audit is claimed.

## References

1. A. Glen, J. Justin, S. Widmer, L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656, Theorem 2.14 (first public preprint 2008). https://arxiv.org/abs/0801.1656
2. D. A. Cruz, M. M. Ferrari, N. Jonoska, L. Nabergall, M. Saito, *Insertions Yielding Equivalent Double Occurrence Words*, arXiv:1811.11739 (first publicly posted 2018-11-28). https://arxiv.org/abs/1811.11739
3. J. Rukavicka, *A Unique Extension of Rich Words*, arXiv:1910.00826 (first publicly posted 2019-10-02; primary MSC 68R15). https://arxiv.org/abs/1910.00826
4. J. Burns, T. Muche, *Counting Irreducible Double Occurrence Words*, arXiv:1105.2926, Sections 2–3 (2011). https://arxiv.org/abs/1105.2926
5. OEIS Foundation, A006356, known coefficients and recurrence in other combinatorial interpretations. https://oeis.org/A006356
