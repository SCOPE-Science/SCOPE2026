# Exact ternary length-five two-deletion capacity via a universal weighted shadow

## Finding

Let \(\Sigma_q=\{0,\dots,q-1\}\), where \(q\ge2\). For \(w\in\Sigma_q^5\), let \(D_2(w)\) denote the **set of distinct** ordered subsequences of length three obtained by deleting two positions. A code \(\mathcal C\subseteq\Sigma_q^5\) corrects two deletions if \(D_2(u)\cap D_2(v)=\varnothing\) for distinct \(u,v\in\mathcal C\). Define \(A_q(5,2)\) as the largest such cardinality.

**Theorem.** For every integer \(q\ge2\),
\[
A_q(5,2)\le\left\lfloor\frac{q^3-q^2+5q}{5}\right\rfloor.
\]
For the ternary alphabet, this bound is sharp:
\[
A_3(5,2)=6,
\qquad
\mathcal C_*=\{00000,11111,22222,00112,10221,21100\}.
\]
The general bound is not asserted to be sharp for other alphabets.

## Assumptions and scope

An output records the surviving three letters in their original order, **without recording deletion positions**. Repeated embeddings of the same length-three output count once. Codewords are unrestricted five-letter words, not necessarily linear or systematic. The alphabet is labeled; no special algebraic structure is assumed. The theorem concerns exactly two deletions, equivalently correction of up to two deletions when the length of the received word identifies the deletion count.

For any triple \(v=v_1v_2v_3\), put
\[
h(v)=\begin{cases}
1,&v_1=v_2=v_3,\\
0,&v_1=v_3\ne v_2,\\
1/5,&v_1\ne v_3.
\end{cases}
\]
The three cases are disjoint and exhaustive. The critical fact is \(\sum_{v\in D_2(w)}h(v)\ge1\) for **every** five-letter word \(w\), regardless of the alphabet size.

## Proof

**Lemma (five-letter nonpalindromic shadow).** If no symbol occurs at least three times in \(w\in\Sigma_q^5\), then \(D_2(w)\) contains at least five distinct triples \(v_1v_2v_3\) with \(v_1\ne v_3\).

*Proof of lemma.* The multiset of symbol multiplicities in \(w\) is necessarily one of \((2,2,1)\), \((2,1,1,1)\), or \((1,1,1,1,1)\). Here the symbols in distinct multiplicity classes are different.

In case \((2,2,1)\), call the twice-occurring letters \(a,b\) and the singleton \(c\). Delete \(c\) from the source word. What remains is a four-letter word containing two \(a\)'s and two \(b\)'s; it has **at least two distinct nonpalindromic length-three subsequences**. This can be verified from the six possible orderings: \(aabb\) gives \(aab,abb\); \(abab\) gives \(aab,abb\); \(abba\) gives \(abb,bba\); \(baab\) gives \(baa,aab\); \(baba\) gives \(baa,bba\); and \(bbaa\) gives \(bba,baa\). Every listed pair consists of distinct nonpalindromic triples.

It remains to find three distinct nonpalindromic triples containing \(c\). If \(c\) is at either endpoint of the five-letter word, the four other positions have at least three distinct ordered length-two subsequences: \(aa\), \(bb\), and at least one of \(ab\) and \(ba\). Attach \(c\) at its endpoint to each; all three triples are distinct and nonpalindromic. If \(c\) is one position away from an endpoint, its longer three-position side contains both \(a\) and \(b\), so gives at least two distinct ordered length-two subsequences on that side. Attaching \(c\) gives two distinct nonpalindromic triples with \(c\) at an endpoint. Choose the letter on the shorter one-position side and a different letter on the longer side to make a third triple with \(c\) in its middle, whose ends differ. If \(c\) is in the middle position, the two positions on either side furnish one triple with \(c\) at the end and one with \(c\) at the start. Because the four remaining letters include two \(a\)'s and two \(b\)'s, one may choose different letters from the opposite sides, forming a third triple with \(c\) in the middle. All triples obtained here are distinct and nonpalindromic. Thus there are at least five in total, with two not containing \(c\).

In case \((2,1,1,1)\), call the repeated letter \(a\). Select the first \(a\) and the three distinct singleton letters, producing a length-four subsequence of four distinct letters. Its four length-three subsequences are pairwise distinct and nonpalindromic. If a singleton lies before the first \(a\) or after the second \(a\), the subsequence consisting of this singleton and both \(a\)'s is nonpalindromic and is new, because it repeats a letter. Otherwise all three singletons occur between the two \(a\)'s. Write \(b,c\) for their first two letters in order. The triple \(bca\) using the *second* \(a\) is nonpalindromic and is not among the four triples using the first \(a\): in the latter, the letter \(a\), if present, is first. This yields five distinct triples.

Finally, in case \((1,1,1,1,1)\), all ten choices of three positions give distinct, nonpalindromic triples. This proves the lemma. \(\square\)

If some letter occurs at least three times in \(w\), the constant triple of that letter belongs to \(D_2(w)\) and has weight one. Otherwise, the lemma supplies at least five **distinct** nonpalindromic descendants, each with weight \(1/5\). Hence in all cases
\[
\sum_{v\in D_2(w)}h(v)\ge1.
\]
For a correcting code, deletion-descendant sets are pairwise disjoint, so summing this inequality over all codewords yields
\[
|\mathcal C|\le \sum_{w\in\mathcal C}\sum_{v\in D_2(w)}h(v)
\le\sum_{v\in\Sigma_q^3}h(v).
\]
There are \(q\) constant triples and \(q^3-q^2\) nonpalindromic triples (the remaining \(q^2-q\) are nonconstant palindromes). Consequently the last sum equals \(q+(q^3-q^2)/5\). Integer rounding gives the general bound.

At \(q=3\), the bound is \(\lfloor 33/5\rfloor=6\). The following are the exact descendant sets of the proposed six codewords, with no repeated outputs within any set:

| Codeword | Distinct length-three descendants |
|---|---|
| `00000` | `000` |
| `11111` | `111` |
| `22222` | `222` |
| `00112` | `001`, `002`, `011`, `012`, `112` |
| `10221` | `021`, `022`, `101`, `102`, `121`, `122`, `221` |
| `21100` | `100`, `110`, `200`, `210`, `211` |

Inspection of these explicitly listed sets shows they are pairwise disjoint. Thus six codewords exist and six is optimal. \(\square\)

## Verification

The standalone `verify.py` enumerates all \(52\) restricted-growth representatives of equality patterns on five positions. Such representatives are exhaustive for **every alphabet**, because the deletion-shadow weights depend only on equality between letters. Each representative satisfies the integral inequality \(\sum_{v\in D_2(w)}5h(v)\ge5\). The program separately checks all words for alphabet sizes two through six and independently rebuilds the exact six-word witness shadows. Its direct output is in `verification_output.txt`. The universal theorem is supported by the preceding symbolic case proof; finite checks alone are not extrapolated into an infinite claim.

## Relationship to prior work

Kulkarni and Kiyavash (2013 preprint, arXiv:1211.3128) introduced general deletion-shadow hypergraph and fractional-transversal bounds. Their Theorem IV.1 uses the weight reciprocal to the smaller deletion-ball size, giving for the present parameters the numerical bound \(A_3(5,2)\le14\). The explicit five-letter-specific weight above gives a strictly stronger upper bound of six; the fractional-packing *method* is not claimed to be new. Li, Wang and Fu (January 10, 2026, arXiv:2601.06493) study individual nonbinary deletion-descendant cardinalities, not this exact cross-code packing problem. Chee, Ge and Ling (2010, arXiv:1008.1343) determine spectra of *perfect* codes in the \(n-t=2\) regime; the theorem here concerns \(n-t=3\) and an unrestricted optimum. Schaller, Toesca and Vu (2025, arXiv:2501.13534) construct codes for the different multiplicity-free regime \(q>n\).

A historical ternary edit-metric table of Houghten and collaborators (2005/2006) uses minimum edit distance with substitutions permitted; its entries must not be identified with the insertion/deletion-only metric used here. For example, a code correcting two deletions has minimum insertion/deletion distance at least six between distinct length-five words, while an optimal code for a metric charging one per substitution can have a different size. Neither matching Hamming-code parameters nor the table's \(E_3(5,d)\) values establish the present claim.

## Limitations

Only the ternary capacity is proved exact. The upper bound holds for every finite alphabet, but is not asserted optimal for other values of \(q\). The result does not classify all maximum ternary codebooks, provide bounds for other lengths, or prove publication priority. The claim does not establish publication priority or a complete spectrum beyond the displayed alphabet and block length.

## References

- H. Li, X. Wang and F.-W. Fu, *On the Number of Subsequences in the Nonbinary Deletion Channel*, first posted January 10, 2026, https://arxiv.org/abs/2601.06493.
- M. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, https://arxiv.org/abs/1211.3128.
- Y. M. Chee, G. Ge and S. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, arXiv:1008.1343, https://arxiv.org/abs/1008.1343.
- L. Schaller, M. Toesca and P. Vu, *A New Construction of Non-Binary Deletion Correcting Codes and their Decoding*, arXiv:2501.13534, https://arxiv.org/abs/2501.13534.
- S. K. Houghten, D. Ashlock and J. Lenarz, *A Table of Bounds on Optimal Fixed-Length Ternary Edit-Metric Codes* (2005), https://www.cosc.brocku.ca/~shoughten/ternaryedit.html.
