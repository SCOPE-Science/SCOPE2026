# Two sharp constant-weight single-deletion code sizes at lengths 14 and 15

## Finding

Let \(M_3(n)\) be the maximum size of a binary code of blocklength \(n\), constant Hamming weight \(3\), and pairwise disjoint single-deletion output sets. Then
\[
\boxed{M_3(14)=32,\qquad M_3(15)=37.}
\]
Both values attain the general upper bound \(M_3(n)\le (n^2-3)/6\) of Hagiwara and Nation at these parameters. They settle two unresolved rows of that work's table; its previously recorded lower bounds were \(31\) and \(35\), respectively.

## Assumptions and scope

The alphabet is \(\{0,1\}\). A word has exactly three symbols equal to one. For a word \(x=(x_1,\ldots,x_n)\), let \(D(x)\) be the *set of distinct* length-\(n-1\) words obtained by deleting exactly one coordinate, including either a zero or a one. A code \(C\) corrects one deletion precisely when \(D(x)\cap D(x')=\varnothing\) for all distinct \(x,x'\in C\). Nothing is assumed about linearity, word ordering, or any decoding architecture. Codeword lists in `witnesses.json` specify three one-based positions of the ones.

## Proof

**Upper bounds.** For either \(n=14\) or \(n=15\), put \(m=n-1\). Define a nonnegative integer weight \(u_m(y)\) for each binary output word \(y\) of length \(m\). For an output of Hamming weight two, with support \(\{a,b\}\) where \(1\le a<b\le m\), set
\[
u_m(y)=1+\mathbf 1_{b=a+1}+\mathbf 1_{m=14,\ (a,b)=(13,14)}.
\]
For an output of Hamming weight three with support \(\{s,s+1,s+2\}\) where \(s\in\{1,3,5,7,9,11\}\), set \(u_m(y)=1\). Assign zero to every other output. The last exceptional term contributes only when \(n=15\). Direct counting gives
\[
\sum_{y\in\{0,1\}^{13}}u_{13}(y)={13\choose 2}+12+6=96,
\]
\[
\sum_{y\in\{0,1\}^{14}}u_{14}(y)={14\choose 2}+13+1+6=111.
\]
For **every** input word \(x\) with three ones, we claim
\[
\sum_{y\in D(x)}u_m(y)\ge3.
\]
To verify this, let the one-positions be \(i<j<k\). If neither successive pair is adjacent, deleting each of the three ones produces three *different* weight-two outputs, each of weight at least one. If precisely one successive pair is adjacent, the output from deleting the isolated one has adjacent ones and weight at least two, while deleting a one from the adjacent pair produces another weight-two output of weight at least one. Finally, if the three ones are consecutive at positions \(i,i+1,i+2\), deleting a one gives the output with adjacent ones at positions \(i,i+1\), of weight at least two. Unless \(n=15\) and \(i=13\), deleting a zero immediately before or after the three-one block produces a three-one output starting at one of \(i-1\) or \(i\) that is odd and belongs to \(\{1,3,5,7,9,11\}\), adding weight one. In the remaining case \(n=15\), \(i=13\), the adjacent-pair output \(\{13,14\}\) already has weight three. This proves the claim for every candidate word, including both boundaries.

For a one-deletion-correcting code, the output sets \(D(x)\) are disjoint. Summing the last inequality over codewords thus yields \(3|C|\le\sum_yu_m(y)\), or \(|C|\le32\) for \(n=14\) and \(|C|\le37\) for \(n=15\). This argument proves the upper bounds without requiring an optimization solver or relying on a published numerical table.

**Attainment.** The data file `witnesses.json` gives a 32-word binary weight-three code of length 14 and a 37-word code of length 15, using one-based triples of support indices. The standalone `verify.py` checks from the actual transmitted bits that every word has the required length and weight and that no deletion output occurs in two different codewords. Therefore both upper bounds are attained.

## Verification

Run `python3 verify.py` in the directory containing `verify.py` and `witnesses.json` (Python standard library only). It generates every deletion of each witness by literal removal from the binary word; a separate position-update implementation independently produces every possible deletion support. Both implementations are compared for **all** \({14\choose3}=364\) and \({15\choose3}=455\) candidate input words. The program also reconstructs all values of \(u_m\), checks \(\sum u_{13}=96\) and \(\sum u_{14}=111\), verifies the lower coverage inequality for every possible weight-three input, and checks the two codes for pairwise disjoint output sets. Successful execution prints `VERIFY_OK max3(14)=32 max3(15)=37`. This is finite *exhaustive* checking over exactly the domains stated, not evidence for any additional blocklength.

## Relationship to prior work

Cullina, Kulkarni, and Kiyavash (2012) considered deletion-correcting codes restricted to constant-weight layers and the associated graph-coloring constructions. Hagiwara and Nation's dated 2023 draft, particularly Theorem 11 and Table 3, proves \(M_3(n)\le(n^2-3)/6\), gives the two lower bounds \(31\) and \(35\), and explicitly leaves the optimum unknown at lengths 14 and 15. The present contribution consists of explicit larger witnesses, and a short independently checkable weighted-output certificate showing they are sharp. The pre-existing upper-bound theorem and the general constant-weight framework are not claimed as new.

## Limitations

The statement concerns only binary codes of constant weight exactly three, exact correction of one deletion, and the two specified blocklengths. It does not classify or count all optimal codebooks, prove a new general upper bound, or settle longer blocklengths. The originality comparison relies on the inspected cited papers, available mathematical records, and targeted search; it cannot rule out every unindexed later code construction.

## References

1. D. Cullina, A. A. Kulkarni, and N. Kiyavash, *A Coloring Approach to Constructing Deletion Correcting Codes from Constant Weight Subgraphs*, IEEE International Symposium on Information Theory (2012), pages 513–517, DOI `10.1109/ISIT.2012.6284242` (conference proceedings, July 2012). Publicly dated preprint: *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv `1211.4056v1` (submitted 2012-11-16 UTC).
2. M. Hagiwara and J. B. Nation, *Bounds on the Size of k-of-n Single Deletion Error Correcting Codes*, draft dated October 12, 2023, Theorem 11, Table 3, pages 9–11. Source: https://www.math.hawaii.edu/~jb/k_of_n_writeup_II.pdf.
3. J. B. Nation, *Bounds on the Size of Single Deletion Error Correcting Codes*, seminar slides, April 14, 2023, page 20, https://math.hawaii.edu/~jb/nycs_on_deletion_codes.pdf.
