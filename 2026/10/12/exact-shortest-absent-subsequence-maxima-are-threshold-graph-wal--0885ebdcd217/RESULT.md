# Exact shortest-absent-subsequence maxima are threshold-graph walk numbers
## Finding
Fix an alphabet
\[
\Sigma=\{0,1,\ldots,\sigma-1\},\qquad \sigma\ge 2,
\]
and let
\[
M_{\sigma,k}=\max\{|\operatorname{SAS}(w)|:\operatorname{alph}(w)=\Sigma,\ \iota(w)=k\},
\qquad k\ge1,
\]
where \(\operatorname{SAS}(w)\) is the set of shortest absent subsequences and \(\iota(w)\) is the subsequence-universality index.

Let \(T(r,m)\) denote the entry in displayed row \(r\) and zero-based column \(m\) of OEIS A050447. Then
\[
M_{\sigma,k}=T(\sigma-1,k+1).
\]

Equivalently, let \(G_{\sigma-1}\) be the threshold graph on
\[
\{0,1,\ldots,\sigma-1\}
\]
with an edge, including loops, whenever
\[
i+j\ge \sigma-1.
\]
Then \(M_{\sigma,k}\) is the number of walks of length \(k+1\) in \(G_{\sigma-1}\) starting at the vertex \(\sigma-1\).

For the first five alphabet sizes, the values for \(k=1,\ldots,6\) are
\[
\begin{array}{c|rrrrrr}
\sigma&1&2&3&4&5&6\\ \hline
2&3&5&8&13&21&34\\
3&6&14&31&70&157&353\\
4&10&30&85&246&707&2037\\
5&15&55&190&671&2353&8272\\
6&21&91&371&1547&6405&26585
\end{array}
\]
where the header \(1,\ldots,6\) lists the universality index \(k\).

## Assumptions and scope
A word \(u\) is a subsequence of \(w\) if its letters occur in \(w\) in the same order, not necessarily contiguously. A shortest absent subsequence is an absent subsequence of minimum possible length. Every shortest absent subsequence of a word of universality index \(k\) has length \(k+1\).

Prior work proves that the maximum number of shortest absent subsequences among words of fixed universality index \(k\) is attained by the alternating-arch word
\[
A_k=P\,P^R\,P\,P^R\cdots,
\]
with exactly \(k\) permutation blocks, where
\[
P=0\,1\,\cdots\,(\sigma-1).
\]
Thus the new counting problem is to determine \(|\operatorname{SAS}(A_k)|\) exactly.

## Proof
Consider a candidate word
\[
x=x_0x_1\cdots x_k\in\Sigma^{k+1}.
\]
Greedily embed \(x\) into \(A_k\), always taking the earliest available occurrence of the next letter.

In an ascending block \(P\), after matching \(x_i\), the next letter \(x_{i+1}\) can remain in that same block exactly when
\[
x_{i+1}>x_i.
\]
If instead \(x_{i+1}\le x_i\), including equality, its next available occurrence lies in the following block. In a descending block \(P^R\), the corresponding same-block condition is
\[
x_{i+1}<x_i.
\]

Every step of the greedy embedding either stays in its current block or advances by exactly one block. Starting in the first block, \(x\) is absent precisely when all \(k\) transitions advance to the next block, because that would require \(k+1\) blocks although only \(k\) exist. Therefore
\[
x\in\operatorname{SAS}(A_k)
\]
if and only if
\[
x_0\ge x_1\le x_2\ge x_3\le\cdots.
\]
If any one of these weak inequalities fails, one transition stays within its block and the remaining transitions advance by at most one block each, so the complete word embeds within the \(k\) available blocks.

It remains to count these weak zigzags. Define
\[
y_i=
\begin{cases}
x_i,&i\text{ even},\\
\sigma-1-x_i,&i\text{ odd}.
\end{cases}
\]
Each weak zigzag inequality becomes
\[
y_i+y_{i+1}\ge \sigma-1.
\]
Hence weak zigzags \(x_0\cdots x_k\) are in bijection with walks
\[
(\sigma-1),y_0,y_1,\ldots,y_k
\]
of length \(k+1\) in \(G_{\sigma-1}\): the fixed initial vertex \(\sigma-1\) is adjacent to every possible \(y_0\).

OEIS A050447 records exactly these threshold-graph walk counts. Its reverse-accumulate algorithm starts from a vector of \(\sigma\) ones, repeatedly reverses it and takes prefix sums; after \(m\) iterations the last entry is the displayed row \(\sigma-1\), column \(m\). Taking \(m=k+1\) gives
\[
|\operatorname{SAS}(A_k)|=T(\sigma-1,k+1).
\]
Combining this exact count with the published extremality theorem for \(A_k\) proves the stated formula for \(M_{\sigma,k}\).

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses three checks. First, for every \(2\le\sigma\le5\) and \(1\le k\le5\), it explicitly enumerates all \(\sigma^{k+1}\) candidate shortest absent subsequences of \(A_k\), tests them by a direct subsequence scan, and confirms that absence is equivalent to the weak-zigzag inequalities.

Second, it independently computes the counts by threshold-graph dynamic programming and by the reverse-accumulate recurrence, checking agreement for \(2\le\sigma\le9\) and lengths through \(12\).

Third, as a finite stress test of the extremality premise, it enumerates every full-alphabet binary and ternary word through length \(7\), computes its universality index and shortest-absent-subsequence count, and verifies the claimed bound whenever the index is \(1\) or \(2\). This finite test supplements, but does not replace, the published general extremality theorem.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced the alternating words \(A_k\) and proved that they maximize the number of shortest absent subsequences at fixed universality index. Their Proposition 3.10 gives only an exponential lower estimate for \(|\operatorname{SAS}(A_k)|\), explicitly notes that the estimate is not tight, and writes the alternating prefix/suffix recurrences for endpoint counts used in that estimate. Proposition 3.14 proves the extremality of \(A_k\).

Adamson, Fleischmann, Huch, Manea, Sarnighausen-Cahn, and Wiedenhöft later generalize the same alternating-arch construction to absent subsequences of arbitrary lengths and explicitly credit the earlier shortest-length extremality result.

The new point here is the exact evaluation of the shortest-length extremum for every alphabet size and universality index: its weak-zigzag set is identified with threshold-graph walks and therefore with the classical array A050447. The binary row reduces to the Fibonacci values already familiar from the two-letter case, while the higher rows give the exact general-alphabet values.

Targeted searches for the exact A050447 identification, the threshold-graph interpretation in this shortest-absent-subsequence setting, and the characteristic initial rows did not locate a published covering statement.

## Limitations
The formula concerns shortest absent subsequences, namely length \(k+1\). It does not give a closed form for the maximal number of absent subsequences at arbitrary longer lengths.

The extremal word need not be unique in every parameter regime; the claim is only about the maximum count.

The A050447 identification is an exact counting equivalence, not a new claim about the older distributive-lattice and threshold-graph interpretations already associated with that array.

An unindexed note or unpublished computation could have made the same sequence identification.

## References
1. M. Kosche, T. Koß, F. Manea, and S. Siemer, “Absent Subsequences in Words,” arXiv:2108.13968v1, first public version 2021-08-31; Fundamenta Informaticae 189(3–4), 199–240.
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, and M. Wiedenhöft, “Tight Bounds for the Number of Absent Subsequences,” arXiv:2407.18599v1, first public version 2024-07-26; MSC 68R15.
3. OEIS Foundation Inc., OEIS A050447, array with reverse-accumulate and threshold-graph-walk interpretations.
