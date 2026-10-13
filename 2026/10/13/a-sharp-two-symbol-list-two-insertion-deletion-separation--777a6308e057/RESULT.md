# A sharp two-symbol list-two insertion–deletion separation

## Finding

For a finite alphabet \(Q\) with \(|Q|=q\ge2\), let \(D_q\) be the largest possible cardinality of a code \(C\subseteq Q^2\) such that every word of length one occurs as a deletion result of at most two members of \(C\). Let \(I_q\) be the analogous maximum when every word of length three is a one-insertion result of at most two members of \(C\). The following **single short-block separation theorem** holds:

\[
D_q=\left\lfloor\frac{3q}{2}\right\rfloor,\qquad
I_2=3,\qquad I_3=6,\qquad
I_q\ge 2\left\lfloor\frac{q^2}{4}\right\rfloor\quad(q\ge2).
\]

Thus \(I_2=D_2=3\), \(I_3=6>D_3=4\), and \(I_q>D_q\) for all \(q\ge3\). Moreover, \(I_q/D_q\) grows without bound as \(q\to\infty\); the certified lower bound on the ratio is asymptotic to \(q/3\). The theorem determines the first alphabet-size separation in the shortest blocklength for which a deletion retains a nonempty received word. It does **not** determine \(I_q\) exactly beyond \(q=3\).

## Assumptions and scope

Codewords are distinct ordered pairs of letters, without a linearity assumption. Repeated-letter words such as \(aa\) are allowed. A deletion receiver observes one of the two constituent letters. An insertion receiver observes an ordered triple \(xyz\); a pair \(ab\) is compatible exactly when it is one of the (distinct) subsequences \(xy\), \(xz\), or \(yz\). Each received word must be compatible with at most two *distinct codewords*. Alphabet size \(q\) is an integer \(\ge2\). Exactly one edit, not at most one edit, is required. There are no assumptions about an underlying probability distribution or adversarial randomization.

## Proof

**Deletion optimum.** Let \(\ell\) of the chosen pairs be diagonal \(aa\), and let \(r\) be off-diagonal. Sum the number of compatible codewords over all \(q\) length-one received symbols. A diagonal word is counted once and an off-diagonal word twice, so \(\ell+2r\le 2q\). Also \(\ell\le q\). Consequently \(|C|=\ell+r\le q+\ell/2\le3q/2\), yielding the integer upper bound. For equality, include every diagonal \(aa\), and one arbitrarily oriented pair \(ab\) for each edge of a matching of size \(\lfloor q/2\rfloor\) on the alphabet. Every letter then participates in its diagonal word and in at most one extra pair. The resulting cardinality is \(q+\lfloor q/2\rfloor=\lfloor3q/2\rfloor\).

**Insertion lower bound.** Partition \(Q=A\sqcup B\) into parts of sizes \(\lfloor q/2\rfloor\) and \(\lceil q/2\rceil\). Let \(C=(A\times B)\cup(B\times A)\), of size \(2|A||B|=2\lfloor q^2/4\rfloor\). In any ordered triple, at least two of its three letters are in the same part, by the two-part pigeonhole principle. The pair of positions occupied by those letters produces no codeword, so among its three possible two-letter subsequences at most two belong to \(C\). Therefore this entire family is insertion-list-two.

**Exact binary boundary.** The deletion result gives \(D_2=3\). Among the four binary ordered pairs, the three distinct length-two subsequences of received triple \(010\) are \(01\), \(00\), and \(10\), so the full four-word code is not insertion-list-two. The three-word code \(\{00,01,11\}\) is insertion-list-two, as can be checked by listing its eight possible received triples (or the attached checker). Thus \(I_2=3\).

**Exact ternary boundary.** Let \(\ell\) denote the chosen diagonal pairs and \(e\) the off-diagonal ordered pairs over an alphabet of three letters. Consider all six ordered triples whose letters are pairwise distinct. Each off-diagonal ordered pair appears as a subsequence in exactly three of those six triples. Because the list size is at most two at each triple, double counting gives \(3e\le 12\), hence \(e\le4\). If \(e=4\), the three unordered distinct-letter pairs force at least one antiparallel pair of codewords \(ab,ba\). The presence of either diagonal \(aa\) or \(bb\) would give three compatible codewords for the received triple \(aba\) or \(bab\), respectively. Hence at most one diagonal word remains and \(|C|\le5\). If \(e\le3\), then trivially \(|C|=e+\ell\le3+3=6\). Thus \(I_3\le6\). For equality, use the three diagonal words together with an oriented three-cycle: \(C=\{00,11,22,01,12,20\}\). A triple of three distinct symbols has at most two subsequences among the oriented cycle edges, since a three-cycle has no transitive directed triangle. A triple with exactly two distinct symbols has at most one off-diagonal oriented cycle edge and at most one distinct diagonal pair in its subsequence set, so again at most two. A constant triple has only one compatible codeword. Thus \(I_3\ge6\).

Together these statements give the first separation \(I_3>D_3\), and for \(q\ge4\), \(2\lfloor q^2/4\rfloor>\lfloor3q/2\rfloor\). Finally \(I_q/D_q\ge 2\lfloor q^2/4\rfloor/\lfloor3q/2\rfloor\), which is asymptotic to \(q/3\).

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. Its exhaustive subset search enumerates all \(2^4\) binary and \(2^9\) ternary length-two codebooks and obtains the deletion/insertion maxima \((3,3)\) and \((4,6)\). It also checks the explicit ternary witness and both parameterized construction families for all integer alphabet sizes \(2\le q\le24\). The successful run prints `VERIFY_OK`. The unrestricted statements follow from the foregoing mathematical proof, not the finite checks.

## Relationship to prior work

Haeupler–Shahrasbi–Sudan (2018) and Guruswami–Haeupler–Shahrasbi (2019) already established that insertion and deletion list decoding are qualitatively asymmetric; this fact is **not claimed as new**. Con–Doron–Ribeiro (2026) determine an asymptotic insertion list-decoding capacity, while Kiah–Wei–Zeng (2026) examine fixed-list asymptotic bounds and insertion/deletion reductions. The theorem here instead pins down the first two-letter, list-two alphabet-size frontier exactly for \(q=2,3\), computes the deletion optimum for all alphabets, and supplies a quadratic explicit insertion family for each alphabet size. None of the portions actually inspected in the above sources establishes that combined finite-length statement. See the limitations on incomplete access.

## Limitations

The exact insertion optimum for alphabets of size \(q\ge4\) is **not determined**. The length-two conclusion is not a claim about the earliest possible blocklength overall: length one has an empty deletion output. The full 2026 Kiah–Wei–Zeng preprint could not be read from authorized accessible sources during this comparison, so an uninspected finite appendix or an unindexed earlier classification remains a genuine originality risk. No claim of independent verification is made; the described mathematical and computational checks are self-review only.

## References

1. H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion--Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395, initially public 2026-09-18. https://arxiv.org/abs/2609.21395
2. B. Haeupler, A. Shahrasbi and M. Sudan, *Synchronization Strings: List Decoding for Insertions and Deletions*, ICALP 2018. https://drops.dagstuhl.de/storage/00lipics/lipics-vol107-icalp2018/LIPIcs.ICALP.2018.76/LIPIcs.ICALP.2018.76.pdf
3. V. Guruswami, B. Haeupler and A. Shahrasbi, *Optimally Resilient Codes for List-Decoding from Insertions and Deletions*, ECCC TR19-153 (2019). https://eccc.weizmann.ac.il/report/2019/153/revision/1/download
4. R. Con, D. Doron and J. Ribeiro, *The Insertion List-Decoding Capacity and an Improved Bound on the Deletion List-Decoding Capacity*, arXiv:2607.03989 (2026). https://arxiv.org/abs/2607.03989
