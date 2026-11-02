# Exact palindromic-factor spectrum of finite binary Cantor words

## Finding

For each integer \(k\ge1\), define the finite binary Cantor word recursively by \(C_0=1\) and \(C_{k+1}=C_k0^{3^k}C_k\). The length of \(C_k\) is \(3^k\). Let \(P_k(n)\) be the number of **distinct nonempty contiguous palindromic factors** of length \(n\) in \(C_k\). Write \(L=3^{k-1}\). For every positive integer \(n\),

\[
P_k(n)=\begin{cases}
2,&n=1,\\
1,&2\le n\le L\text{ and }n\text{ even},\\
3,&3\le n\le L\text{ and }n\text{ odd},\\
1,&L<n\le3L\text{ and }n\text{ odd},\\
0,&\text{otherwise}.
\end{cases}
\]

In particular \(C_k\) has exactly \(3^k\) distinct nonempty palindromic factors; equivalently, it is rich in the usual sense. The **newly resolved object is the complete finite length-by-length factor spectrum and canonical representatives**, not the already known richness assertion.

To specify every factor explicitly, write \(\operatorname{mid}_n(W)\) for the centered contiguous factor of odd length \(n\) of an odd-length palindrome \(W\). At length one the factors are 0 and 1. At any even length \(2\le n\le L\) the sole factor is \(0^n\). For odd \(3\le n\le L\), let \(j\) be the unique integer with \(3^{j-1}<n\le3^j\). Exactly three palindromes occur:

\[
0^n,\qquad \operatorname{mid}_n(C_j),\qquad
\operatorname{mid}_n(0^{3^{j-1}}C_{j-1}0^{3^{j-1}}).
\]

For odd \(L<n\le3L\), the sole palindrome is \(\operatorname{mid}_n(C_k)\). All remaining lengths have no palindromic factors.

## Assumptions and scope

Factor means a **contiguous** substring, not a scattered subsequence, and distinct factors are counted once irrespective of occurrence frequency. Positions are zero-based in the proof. The alphabet is exactly \(\{0,1\}\); the recursion starts from \(C_0=1\), and the theorem assumes \(k\ge1\). The centered factor is defined only when the ambient palindrome and desired length are both odd. The all-zero power \(0^n\) denotes \(n\) zero symbols.

## Proof

**1. Basic structure.** Every \(C_j\) is a palindrome, by induction from \(C_{j+1}=C_j0^{3^j}C_j\). Its length is \(3^j\); it begins and ends with 1. Every occurrence of 1 in \(C_k\) has an even zero-based index: the 1-indices are precisely the integers between 0 and \(3^k-1\) whose base-three digits lie in \(\{0,2\}\). In particular, reflection in the axis of an even-length factor interchanges index parity. Hence any even-length palindromic factor must consist entirely of zeros. The largest zero run in \(C_k\) is exactly \(L=3^{k-1}\), by induction on its two copies and its middle gap. Therefore the even-length counts and factors are exactly as asserted.

**2. Two nonzero odd palindromes at every short odd length.** For \(j\ge1\), set \(B_j=0^{3^{j-1}}C_{j-1}0^{3^{j-1}}\). This is a palindrome of length \(3^j\). It occurs as a contiguous factor of \(C_{j+1}\): the rightmost copy of \(C_{j-1}\) inside the left \(C_j\) is preceded by \(3^{j-1}\) zeros and followed by the middle block of \(3^j\) zeros. Thus, for every \(j\le k-1\), both \(C_j\) and \(B_j\) occur in \(C_k\).

For every odd \(n\) with \(3\le n\le L\), there is a unique \(j\in\{1,\dots,k-1\}\) satisfying \(3^{j-1}<n\le3^j\). The three palindromes \(0^n\), \(\operatorname{mid}_n(C_j)\), and \(\operatorname{mid}_n(B_j)\) therefore all occur. The two nonzero candidates each contain a 1: around the center of \(C_j\), the zero run has length \(3^{j-1}<n\); around the center of \(B_j\), a 1 occurs at least as close. They are distinct from each other. If \(j=1\), their centers are respectively 0 and 1; if \(j\ge2\), the lengths of their central zero runs are respectively \(3^{j-1}\) and \(3^{j-2}\), so the centered factors of length \(n>3^{j-1}\) differ. At length one, both 0 and 1 occur. Finally, for each odd \(L<n\le3L\), the centered factor \(\operatorname{mid}_n(C_k)\) supplies at least one palindrome.

**3. Saturation of the universal palindromic bound.** Any finite word of length \(N\) contains at most \(N\) distinct nonempty palindromic factors: when appending a letter, at most one new palindrome can appear, because any shorter palindromic suffix of a new longest palindromic suffix also appears as its prefix at an earlier position. Apply this bound with \(N=3L\). Step 2 produces at least two palindromes at length one, at least three at each of the \((L-1)/2\) odd lengths from 3 through \(L\), at least one at each of the \((L-1)/2\) positive even lengths at most \(L\), and at least one at each of the \(L\) odd lengths from \(L+2\) through \(3L\). Their sum is

\[
2+3\frac{L-1}{2}+\frac{L-1}{2}+L=3L.
\]

These are palindromes of distinct lengths or distinct explicit representatives at a fixed length. Thus the universal upper bound is attained **exactly**; there can be no additional palindromic factors of any length. This proves both the spectrum and the exhaustive representative list. \(\square\)

## Verification

The accompanying self-contained `checker.py` generates the words directly, enumerates palindromes by expanding around each possible odd and even center, independently forms the proposed representatives, and checks **set equality at every length** for \(k=1,\dots,8\) (final word length \(6561\)). It also checks the total count at each level. This exhaustive finite testing is diagnostic only; the proof above covers all \(k\ge1\) and all lengths.

To replay, run `python3 checker.py` in the package directory. No third-party Python modules or data files are used.

## Relationship to prior work

Glen, Justin, Widmer and Zamboni (2008, Proposition 2.10) explicitly identify the **infinite Cantor word as rich**; this already implies that its finite prefixes, including \(C_k\), are rich. That total-count property is therefore prior knowledge, not an originality claim. Their work supplies the general rich-word context and the classical palindrome count bound but does not state a lengthwise classification or the three canonical families for finite \(C_k\).

Anisiu, Anisiu and Kása (2010) study palindrome-complexity functions of arbitrary finite words, without this Cantor-specific formula. Lü, Chen, Guo and Wen (2016, Remark 5) give ordinary infinite Cantor **factor complexity**, namely \(p(n)=2n-1\) for \(n\ge2\); this does not, on its own, specify the finite palindromic-factor spectrum. Bulgakova, Frid and Scanvic (2022) determine **prefix palindromic length** for the Sierpiński/Cantor word, an invariant counting the minimum number of palindromes needed for a decomposition rather than distinct palindromic factors. OEIS A292686 tabulates the finite Cantor words themselves, not their palindrome length profiles.

## Limitations

The result applies to complete ternary substitution iterates \(C_k\), not arbitrary-length prefixes, different substitutions, or occurrence-weighted palindrome frequencies. The rich-word property is not new. A complete historical-priority guarantee is impossible; an earlier equivalent formula under Sierpiński-word terminology remains a specific possibility. The 2016 publisher text was only partly accessible through indexed text, although its relevant factor-complexity section was inspected; the independent proof does not depend on that section.

## References

1. A. Glen, J. Justin, S. Widmer, L. Q. Zamboni, *Palindromic Richness* (first posted 2008-01-10), arXiv:0801.1656; especially Proposition 2.10.
2. M.-C. Anisiu, V. Anisiu, Z. Kása, *Properties of palindromes in finite words* (2010), arXiv:1002.2723.
3. X.-T. Lü, J. Chen, Y.-J. Guo, Z. Wen, *On the permutation complexity of the Cantor-like sequences*, Theoretical Computer Science 616 (2016), 100–110, DOI:10.1016/j.tcs.2015.12.022; especially Remark 5.
4. D. V. Bulgakova, A. E. Frid, J. Scanvic, *Prefix palindromic length of the Sierpinski word* (2022), arXiv:2201.09556.
5. OEIS A292686, *Sierpinski-type iteration: 1 to 101 and 0 to 000*.
