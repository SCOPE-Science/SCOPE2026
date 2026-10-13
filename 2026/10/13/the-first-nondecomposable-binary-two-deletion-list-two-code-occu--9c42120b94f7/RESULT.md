# The first nondecomposable binary two-deletion list-two code occurs at length seven

## Finding
Let \(M_2(n,L)\) denote the maximum cardinality of a set \(C\subseteq\{0,1\}^n\) such that every binary word of length \(n-2\) is an ordered subsequence of at most \(L\) distinct words of \(C\). For every integer \(2\le n\le7\), the exact capacities for list sizes one and two are
\[
\begin{array}{c|rrrrrr}n&2&3&4&5&6&7\\\hline
M_2(n,1)&1&2&2&2&4&5\\
M_2(n,2)&2&3&4&4&7&11
\end{array}.
\]
Consequently the **smallest** length with \(M_2(n,2)>2M_2(n,1)\) is \(n=7\). In particular, a binary eleven-word code correcting two deletions with lists of at most two cannot be a union of two codes each uniquely correcting two deletions.

## Assumptions and scope
All words are binary and of fixed length. Exactly two symbols are deleted, and distinct deletion positions producing the same received word count as a single possible codeword, not multiple outputs. A list size \(L\) bounds the number of *distinct codewords* compatible with each received word. A union of two uniquely decodable codes has at most twice the largest uniquely decodable code cardinality; the theorem proves a strict excess at the earliest length. No statement is made about larger lengths, different alphabets, or any number of deletions other than two.

## Proof
For \(n\ge3\), index all binary length-\(n\) words by integers \(j\in[0,2^n-1]\), and all binary length-\(n-2\) words by \(i\in[0,2^{n-2}-1]\), both using most-significant-bit-first encodings. Define \(A_{ij}=1\) if the received word indexed by \(i\) occurs as an ordered subsequence of word \(j\), otherwise \(A_{ij}=0\). Therefore each code is a zero-one vector \(c\) with \(Ac\le L\mathbf1\), and its cardinality equals \(\sum_jc_j\).

For any nonnegative integer vectors \(w\) and \(s\), and integer \(d\ge1\), satisfying
\[
\sum_{i:A_{ij}=1}w_i+s_j\ge d\qquad(0\le j<2^n),
\]
we obtain by multiplying each column inequality by \(c_j\) and using \(Ac\le L\mathbf1\) and \(c_j\le1\) the exact upper bound
\[
|C|\le\left\lfloor\frac{L\sum_iw_i+\sum_js_j}{d}\right\rfloor.
\]
The complete integer certificates and lower-bound codebooks are embedded in `verify.py`. For \(n=7\), choose \(d=59\), the following \(32\) weights, in order of the five-bit received-word indices:

`[52,7,0,26,7,5,4,26,0,1,2,5,4,1,16,7,7,16,1,4,5,2,1,0,26,4,5,7,26,0,7,52]`.

All slack weights vanish except \(s_0=s_{127}=7\). The verifier checks **all 128** column inequalities; moreover \(\sum_iw_i=326\) and \(\sum_js_j=14\). Consequently
\[
M_2(7,1)\le\left\lfloor340/59\right\rfloor=5,
\qquad M_2(7,2)\le\left\lfloor666/59\right\rfloor=11.
\]
These inequalities have no solver dependency.

For \(n=6\), use \(d=5\), weights `[3,2,0,1,0,0,0,2,2,0,0,0,1,0,2,3]`, and slacks \(s_0=s_{63}=2\), all other slacks zero. The same argument yields \(M_2(6,1)\le4\) and \(M_2(6,2)\le7\). For \(n=4,5\), give weight one to the all-zero and all-one received words and zero to all others, with no slack: every input word contains a constant length-\(n-2\) subsequence by pigeonhole, so \(M_2(n,L)\le2L\). For \(n=3\), assign weight one to the received symbol zero, and slack one to the all-one input; the resulting bound is \(M_2(3,L)\le L+1\). For \(n=2\), all words have the same empty length-zero descendant, so \(M_2(2,L)=\min(L,4)\).

For the matching lower bounds, the verifier lists explicit codewords at every indicated \((n,L)\) and enumerates every distinct two-deletion descendant of each. As the codebooks satisfy the exact per-received-word list constraints, their sizes match the upper bounds. In particular, the eleven-word length-seven list-two code is

`0000000, 0000100, 0001111, 0011110, 0101010, 1000011, 1010101, 1110000, 1110111, 1111000, 1111111`.

Thus the displayed capacities are exact. For \(n=2,3,4,5,6\), the list-two capacities are at most twice their list-one counterparts; at \(n=7\), \(11>2\cdot5\), which proves the claimed first occurrence and the nondecomposability consequence.

## Verification
Run `python3 verify.py` with a standard Python installation. It independently forms the ordered-subsequence sets by enumerating all \(\binom n2\) choices of the retained positions, deduplicates them as sets, checks all codebook list multiplicities, and verifies every dual inequality with **integer arithmetic only**. Successful output ends in `VERIFY_OK`. The proof does not depend on an integer-optimization solver: the embedded codebooks and integer-weight certificates are complete finite witnesses.

## Relationship to prior work
Lin (2026) studies general asymptotic lower bounds for list-decodable deletion codes and defines the same hypergraph/received-word list condition, but does not give this exact seven-bit capacity or earliest-length separation. Guruswami and Håstad (2020) construct explicit size-two-list two-deletion codes in the large-blocklength setting; their construction does not imply the finite optimum. Kiah, Wei and Zeng (2026) develop general finite-length and asymptotic bounds, not this sharp parameter evaluation. OEIS A057591 lists the **already-known** unique two-deletion optimum \(M_2(7,1)=5\); that number is a comparison baseline rather than a new contribution. The present distinction is \(M_2(7,2)=11\) and its earliest nondecomposability consequence. A separate exact single-deletion analysis addresses a different deletion radius and cannot imply the two-deletion capacity.

## Limitations
This is an exact small-blocklength classification for only list sizes one and two and deletion count two, not a large-blocklength lower bound. Bibliographic searching cannot eliminate the possibility of an unindexed earlier finite table. The case \(n=7\) is independently checkable through a finite, explicit certificate; it makes no assertion of an independently performed scientific audit.

## References
- A. D. Lin, *Lower Bounds for all List-Decodable Deletion Codes*, arXiv:2609.26650v1 (first public 2026-09-22), especially Definition 2.1 and Theorem 1.1.
- V. Guruswami and J. Håstad, *Explicit two-deletion codes with redundancy matching the existential bound*, arXiv:2007.10592v1 (2020), particularly Theorem 1.2.
- H. M. Kiah, H. Wei and R. Zeng, *Constant-List Insertion–Deletion Codes: New Bounds and an Improvement of Levenshtein's Lower Bound*, arXiv:2609.21395v1 (2026), Theorem 23.
- OEIS Foundation, A057591, *Maximal size of binary code of length n that corrects 2 deletions*, including the \(n=7\) value.
