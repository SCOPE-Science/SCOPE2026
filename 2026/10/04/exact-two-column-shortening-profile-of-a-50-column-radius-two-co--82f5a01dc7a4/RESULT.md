# Exact two-column shortening profile of a 50-column radius-two covering seed
## Finding
Let \(S\subset\mathbb F_2^{10}\) be the column set of the published \(10\times 50\) parity-check matrix, using its decimal column labels:

\[
S=\{1,2,4,15,16,32,65,86,128,173,183,202,212,247,256,297,320,329,341,366,373,381,391,403,438,460,479,491,502,559,576,608,653,734,742,754,771,777,789,821,846,855,869,881,893,897,927,981,1003,1004\}.
\]

For every two-element set \(D\subset S\), define \(u(D)\) to be the number of syndromes in \(\mathbb F_2^{10}\) not represented by the empty sum, by one column, or by two distinct columns of \(S\setminus D\). Over all \(\binom{50}{2}=1225\) choices of \(D\), the exact histogram of \(u(D)\) is

\[
\begin{array}{c|rrrrrrrrrrrrrrrrrrr}
u&27&31&40&45&47&49&53&54&56&59&61&62&65&73&74&76&78&79&92\\
\hline
\#D&9&6&12&29&94&3&6&48&69&46&71&6&6&608&87&35&11&78&1
\end{array}.
\]

In particular,

\[
u_2(S):=\min_{D\subset S,\ |D|=2}u(D)=27.
\]

The minimum is attained exactly by

\[
\{329,381\},\{329,927\},\{381,479\},\{381,777\},\{381,927\},\{479,491\},\{479,777\},\{479,927\},\{491,927\}.
\]

## Assumptions and scope
The decimal labels are interpreted exactly as in the cited matrix: each integer is the corresponding ten-bit binary column. Sums are XORs in \(\mathbb F_2^{10}\). A syndrome is covered after deleting \(D\) if it is \(0\), a remaining column, or the XOR of two distinct remaining columns.

The result concerns only the fixed 50-column seed. It neither proves nor assumes that \(50\) is globally minimal, and it gives no lower bound on \(\ell_2(10,2)\) at lengths \(48\) or \(49\).

## Proof
There are finitely many cases, and the certificate checks all of them. First, the 50 labels are verified to be distinct nonzero ten-bit columns. The original set covers all \(2^{10}=1024\) syndromes with sums of at most two columns, agreeing with the published covering-radius-two property.

For each of the \(1225\) unordered pairs \(D\), Algorithm A removes those two columns, forms the exact set

\[
C_D=\{0\}\cup(S\setminus D)\cup\{a\oplus b:a,b\in S\setminus D,\ a<b\},
\]

and records \(u(D)=1024-|C_D|\). This directly produces the stated histogram and the nine minimizers.

Algorithm B independently constructs, for every syndrome \(s\), the complete family \(R_s\) of supports of size at most two representing \(s\) in the original matrix. After deleting \(D\), the syndrome \(s\) is uncovered exactly when every support in \(R_s\) meets \(D\). Thus Algorithm B computes

\[
u(D)=\#\{s: \forall R\in R_s,\ R\cap D\ne\varnothing\}
\]

without rebuilding the shortened sumset. The two algorithms agree for every one of the \(1225\) deletions, so the minimum, the complete histogram, and the minimizer list are exhaustively established.

## Verification
Run `python3 artifacts/verify.py` from the package root. It reconstructs the matrix from the embedded decimal list, verifies full original syndrome coverage, reproduces the published single-deletion benchmark \(\min_{|D|=1}u(D)=9\) attained exactly at \(381,479,927\), and then checks every two-column deletion by both algorithms. It compares the resulting histogram and minimizer list with `artifacts/double_deletion_profile.json` and prints `VERIFY_OK` only if every equality holds.

No random search, timeout, or partial enumeration is used in the proof.

## Relationship to prior work
Wu introduced the 50-column matrix and proved that it gives a binary \([50,40]_2\) covering code of radius \(2\). The author-hosted explanatory text states that deleting any single column destroys coverage and that the least damaging single deletion leaves \(9\) syndromes uncovered. Davydov--Marcugini--Pambianco--Wu reproduce the matrix, prove it is locally optimal, and use it as the seed of an improved infinite family. Their full text defines local optimality only as failure of every one-column removal; it does not quantify two-column removals.

A later public manuscript on exact partition numbers records the single-deletion minimum and several representation statistics, but its stated-results ledger contains no two-column shortening profile. Database and web searches under the aliases “two-column deletion,” “shortening defect,” “minimal 1-saturating set,” and the numerical minimizers located no statement implying the histogram above.

## Limitations
This is an exact finite stability invariant of one distinguished seed, not a new global bound for \(\ell_2(10,2)\). The computation says that every 48-column subset obtained by deleting two columns from this particular matrix misses at least \(27\) syndromes; another unrelated 48- or 49-column set could behave differently. Novelty searches can miss obscure or unindexed sources, so absolute priority is not claimed.

## References
1. S. Wu, *Covering 1024 syndromes with 50 columns*, arXiv:2608.27494v1, 2026.
2. A. A. Davydov, S. Marcugini, F. Pambianco, S. Wu, *Further results on binary codes of covering radius 2 and saturating sets in projective spaces*, arXiv:2609.16078v1, 2026.
3. *Exact (2,0)-partition numbers for two binary covering codes of covering radius two*, public manuscript snapshot dated 2026-09-07.
