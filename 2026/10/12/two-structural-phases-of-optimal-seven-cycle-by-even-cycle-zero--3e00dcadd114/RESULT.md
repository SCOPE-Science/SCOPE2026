# Two structural phases of optimal seven-cycle by even-cycle zero-error codes

## Finding

Let \(k\ge 3\) be an integer. The confusability graph of a heterogeneous two-use channel is the strong product \(G_k=C_7\boxtimes C_{2k}\), with each cycle carrying its fixed residue labels. The maximum cardinality of a zero-error code is the known value \(\alpha(G_k)=3k\). **Every** maximum code belongs to exactly one of two disjoint structural families, described below, and the **exact number of labeled maximum codes** is

\[
T_{2k}=2\left(7^k+\operatorname{tr}\left((3I_7+A_7)^k\right)\right)
=2\left(7^k+\sum_{j=0}^{6}\left(3+2\cos\frac{2\pi j}{7}\right)^k\right),
\]

where \(A_7\) is the adjacency matrix of the seven-cycle. A maximum code is either:

1. **Dense–empty family:** alternating empty columns and maximum independent triples of \(C_7\), with each occupied column an arbitrary one of the seven triples; or
2. **Singleton–pair family:** alternating singleton and independent-pair columns, such that every adjacent singleton–pair union is an independent triple of \(C_7\). When successive singleton columns carry symbols \(s,t\in\mathbb Z/7\mathbb Z\), the number of permissible intermediate pairs is three for \(s=t\), one for \(s-t\equiv\pm1\pmod 7\), and zero otherwise.

The two family counts are respectively \(2\cdot 7^k\) and \(2\operatorname{tr}((3I_7+A_7)^k)\). In particular, the dense–empty family accounts for asymptotically all labeled maximum codes:

\[
\frac{2\cdot7^k}{T_{2k}}=1-O\left((5/7)^k\right)\qquad(k\to\infty).
\]

## Assumptions and scope

The vertices of \(C_r\) are residues \(0,\ldots,r-1\), with undirected edges between residues differing by \(\pm1\pmod r\). Distinct vertices \((a,i)\) and \((b,j)\) of \(G_k\) are confusable if each coordinate is equal or adjacent in its respective cycle. A code is a subset containing no confusable pair. Column \(i\) is the set \(S_i=\{a:(a,i)\in C\}\subseteq\mathbb Z/7\mathbb Z\), with \(i\) taken modulo \(2k\). All counts distinguish the given residue labels, not isomorphism classes. The proof applies to every integer \(k\ge3\), with no unreported computational assumption.

## Proof

**Step 1: sharp size bound and equality rigidity.** Each column \(S_i\) is independent in \(C_7\). Because consecutive columns have equal or adjacent second coordinates, their union is disjoint and independent in \(C_7\). Hence

\[
|S_i|+|S_{i+1}|\le\alpha(C_7)=3.
\]

Summing over all \(2k\) cyclic adjacent column pairs gives \(2|C|\le 6k\), so \(|C|\le 3k\). Conversely, put independent triples into one column parity and leave the other parity empty; these give a code of size \(3k\). At equality each summand must attain three, and subtraction of consecutive equations gives \(|S_{i+2}|=|S_i|\) for every \(i\). The column-size pattern must therefore alternate between \((0,3)\) or \((1,2)\), including their reversed orientations. No other equality patterns exist.

**Step 2: dense–empty count.** The seven-cycle has exactly seven independent sets of cardinality three: around the cycle, the successive gaps between chosen vertices consist of two gaps of size two and one gap of size three, and the position of the exceptional gap uniquely determines the set. The \(k\) occupied columns can therefore be chosen independently in \(7^k\) ways. There are two choices of which column parity is occupied, giving \(2\cdot7^k\) labeled codes.

**Step 3: singleton–pair local transition.** Fix a singleton column \(\{s\}\). To be compatible with it, an adjacent pair column must contain two nonadjacent symbols from the four vertices \(s+\{2,3,4,5\}\pmod7\). The only possibilities are

\[
\{s+2,s+4\},\qquad\{s+2,s+5\},\qquad\{s+3,s+5\}.
\]

The corresponding sets of singleton symbols compatible on the other side are, respectively,

\[
\{s,s-1\},\qquad \{s\},\qquad\{s,s+1\}.
\]

Thus the exact number \(M_{s,t}\) of intervening pair columns compatible with successive singleton columns \(s,t\) is

\[
M_{s,t}=\begin{cases}3,&t=s,\\1,&t=s\pm1\pmod7,\\0,&\text{otherwise},\end{cases}
\qquad M=3I_7+A_7.
\]

Fix which parity consists of singleton columns. A code is then uniquely described by a cyclic sequence of \(k\) singleton values and a compatible pair between each successive pair of singleton values. Summing the products of these exact local multiplicities over all cyclic singleton sequences gives \(\operatorname{tr}(M^k)\). Choosing the other parity doubles the answer. Together with Step 2 this establishes the stated complete classification and counting formula. Because \(M\) is circulant, its eigenvalues are \(3+2\cos(2\pi j/7)\) for \(j=0,\ldots,6\), proving the second expression.

**Step 4: asymptotic proportions.** \(M\) is nonnegative with every row sum five, and it is symmetric. Thus every eigenvalue has absolute value at most five; \(\operatorname{tr}(M^k)\) is nonnegative and at most \(7\cdot5^k\). Substitution in the exact count yields the asserted relative error. The leading count is \(T_{2k}\sim2\cdot7^k\).

## Verification

Two standalone Python 3 programs accompany this result. The command `python3 check_cycle.py` independently enumerates all 29 possible independent column subsets of \(C_7\), uses a cyclic transfer dynamic program over all compatible labeled column assignments, and reports the optimum and exact count for every \(6\le n\le14\); for even \(n\) it independently evaluates the trace formula. The command `python3 verify_transfer.py` reconstructs singleton–pair compatibility from combinations, checks every entry of the claimed matrix \(M\), and enumerates both structural families through length sixteen.

The independent all-column counts at even lengths \(6,8,10,12,14\) are \(1316,7532,45836,291144,1905876\), in exact agreement with the formula. Odd lengths are printed only as control values; no odd-length classification is claimed. The finite checks test implementations and boundary cases; Steps 1–4 prove the infinite theorem.

## Relationship to prior work

The optimum cardinality \(3k\) is **not** the novelty claim. Hales's 1973 study develops independence-number bounds for products of odd cycles, while the 2012 Korže–Vesel paper presents known two-odd-cycle formulas and new results on three-odd-cycle products. Mathew–Östergård (2015) studies packings in strong powers of individual odd cycles and motivates the zero-error code interpretation. The OEIS toroidal-king entry A279409 tabulates maximum **sizes**, not the number of maximizing placements. The new contribution here is the exact **all-even-length equality classification**, its two component counts, and the asymptotic structural dominance for the specific heterogeneous product \(C_7\boxtimes C_{2k}\).

## Limitations

The classification concerns labeled maximum independent sets only, not smaller independent sets or symmetry orbits. It does not cover odd \(n\), other first-factor widths, channel errors beyond graph confusability, or graph powers involving more than two factors. The 2005 Klobučar paper on strong products of paths and cycles is highly relevant but its full text could not be accessed in this comparison; no negative claim about its complete contents is made. Prior unpublished or unindexed enumerations could exist. The stated review is not independent validation.

## References

1. R. S. Hales, *Numerical Invariants and the Strong Product of Graphs*, Journal of Combinatorial Theory, Series B 15 (1973), 146–155. DOI: 10.1016/0095-8956(73)90014-2.
2. D. Korže and A. Vesel, *A Note on the Independence Number of Strong Products of Odd Cycles*, Ars Combinatoria 106 (2012), 473–481. https://combinatorialpress.com/article/ars/Volume%20106/volume-106-paper-41.pdf
3. K. A. Mathew and P. R. J. Östergård, *New Lower Bounds for the Shannon Capacity of Odd Cycles*, first arXiv version dated 2015-04-07. https://arxiv.org/abs/1504.01472
4. A. Klobučar, *Independent Sets and Independent Dominating Sets in the Strong Product of Paths and Cycles*, Mathematical Communications 10 (2005), 23–30. https://hrcak.srce.hr/657
5. OEIS A279409, *Maximum number of nonattacking kings on an \(n\times m\) toroidal board*. https://oeis.org/A279409
