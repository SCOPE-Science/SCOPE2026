# A center-zero injection for prefix-normal palindromes
## Finding
Let \(\operatorname{NPal}(n)\) be the set of binary prefix-normal palindromes of length \(n\), and write
\[
\operatorname{npal}(n)=|\operatorname{NPal}(n)|.
\]
For every integer \(m\ge1\), there is an explicit injection
\[
I_m:\operatorname{NPal}(2m)\longrightarrow\operatorname{NPal}(2m+1).
\]
If an even palindrome is written uniquely as
\[
w=x x^R,
\]
with \(|x|=m\), then
\[
I_m(w)=x0x^R.
\]
Moreover \(1^{2m+1}\) is not in the image, so
\[
\operatorname{npal}(2m+1)\ge \operatorname{npal}(2m)+1.
\]
In particular,
\[
\operatorname{npal}(2m+1)>\operatorname{npal}(2m)
\]
for every \(m\ge1\).

## Assumptions and scope
A binary word is prefix normal when, for every length \(k\), its prefix of length \(k\) contains at least as many \(1\)s as every factor of length \(k\). A prefix-normal palindrome is a word that is both prefix normal and equal to its reversal.

The result compares each even length with the immediately following odd length. It does not give an exact formula for \(\operatorname{npal}(n)\), nor does it prove a converse inequality comparing an even length with the preceding odd length.

## Proof
Fix \(m\ge1\) and let \(w=x x^R\in\operatorname{NPal}(2m)\). Put
\[
v=x0x^R.
\]
The word \(v\) is a palindrome. We prove that it is prefix normal.

First take \(1\le k\le m\). The length-\(k\) prefixes of \(v\) and \(w\) are identical. Consider any length-\(k\) factor \(u\) of \(v\). If \(u\) avoids the inserted central \(0\), then \(u\) is also a length-\(k\) factor of \(w\), so its number of \(1\)s is at most that of the common length-\(k\) prefix.

If \(u\) contains the inserted central \(0\), delete that zero. The remaining word \(u'\) is a contiguous factor of \(w\) of length \(k-1\), with
\[
|u|_1=|u'|_1.
\]
Because \(k-1<2m\), the occurrence of \(u'\) in \(w\) can be extended on at least one side to a length-\(k\) factor \(z\) of \(w\). Hence
\[
|u|_1=|u'|_1\le |z|_1\le |\operatorname{Pref}_k(w)|_1=|\operatorname{Pref}_k(v)|_1.
\]
Thus the prefix-normal inequality holds for every \(k\le m\).

Now take \(m+1\le k\le2m+1\). Every factor of \(v\) of length \(k\) contains the central zero, since each side of it has length only \(m\). Deleting that zero from a length-\(k\) factor \(u\) produces a length-\((k-1)\) factor \(u'\) of \(w\), with the same number of \(1\)s. The length-\(k\) prefix of \(v\) also contains the central zero, and deleting it gives exactly the length-\((k-1)\) prefix of \(w\). Prefix normality of \(w\) therefore gives
\[
|u|_1=|u'|_1\le |\operatorname{Pref}_{k-1}(w)|_1=|\operatorname{Pref}_k(v)|_1.
\]
So \(v\) is prefix normal for every factor length, hence \(v\in\operatorname{NPal}(2m+1)\).

The map \(I_m\) is injective because deleting the unique inserted central position recovers \(w\). Finally the all-one palindrome \(1^{2m+1}\) is prefix normal but is not in the image of \(I_m\), since every image has central symbol \(0\). This proves the strict inequality.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier independently enumerates every binary palindrome through length \(23\), tests prefix normality directly against all of its factors, and reproduces the published counts through that range. For each \(1\le m\le11\), it applies the center-zero map to every even-length prefix-normal palindrome, verifies that the image is prefix normal, checks injectivity, and confirms that the all-one odd palindrome is outside the image.

It also replays, factor by factor, the two reductions used in the symbolic proof: short factors crossing the inserted zero reduce to extendable factors of the even word, while every factor longer than one half necessarily crosses the inserted zero and reduces to a factor one position shorter. These finite checks are consistency tests; the quantified conclusion follows from the symbolic argument above.

## Relationship to prior work
Fleischmann, Kulczynski, Nowotka, and Poulsen isolate prefix-normal palindromes as a special subclass and define \(\operatorname{npal}(n)\). They state that determining \(\operatorname{npal}(n)\) is an unsolved subproblem, tabulate the values through length \(30\), and note that the data support previously observed different behavior at even and odd lengths. Their later recursive analysis proves, among other relations, that if \(w\) is a prefix-normal palindrome then \(1w1\) is again one; this changes the length by two rather than one.

Fleischmann's 2021 dissertation revisits the same recursive problem and again states that an exact formula for \(\operatorname{npal}(n)\) is unavailable. It studies constructions such as \(w0w\) when \(w\) itself is a prefix-normal palindrome, which is a different operation from inserting a zero between the two reversal halves of an arbitrary even palindrome.

OEIS A308465 records the computed prefix-normal-palindrome counts and references these works. Targeted searches for a one-step injection, a center-zero construction, and the inequality between \(\operatorname{npal}(2m+1)\) and \(\operatorname{npal}(2m)\) located the tables and recursive results but not the injection above.

## Limitations
The theorem gives a structural one-step lower bound, not the exact difference between consecutive even and odd counts. It leaves the enumeration of \(\operatorname{NPal}(n)\) open and does not classify the odd palindromes outside the injected family.

A later or unindexed computation may contain the same injection without using this terminology. The accessible indexed text of the 2021 dissertation was compared with the claim, but its direct PDF endpoint was not available during the literature check.

## References
1. P. Fleischmann, M. Kulczynski, D. Nowotka, and D. B. Poulsen, “On Collapsing Prefix Normal Words,” arXiv:1905.11847v1, first public version 2019-05-28; LATA 2020, pp. 412–424, DOI 10.1007/978-3-030-40608-0_29.
2. P. Fleischmann, “On Special \(k\)-Spectra, \(k\)-Locality, and Collapsing Prefix Normal Words,” Ph.D. dissertation, Kiel University, 2021.
3. OEIS A308465, “Number of prefix normal palindromes of length \(n\).”
