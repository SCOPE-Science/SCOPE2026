# Rotation-resolved shortest absent subsequences of sparse binary necklaces and Fibonacci words

## Finding
Let a circular binary word have \(k\ge2\) occurrences of \(1\). Assume that the number of zeros between each pair of consecutive cyclic ones is either \(1\) or \(2\), and that at least one gap has length \(2\). Let \(z\ge1\) denote the number of length-\(2\) gaps. Write its cyclic gap sequence as
\[
2\,1^{r_1}\,2\,1^{r_2}\cdots2\,1^{r_z},\qquad r_i\ge0,\quad \sum_i r_i=k-z.
\]
For every cut of the circular word, form the linear word beginning at that cut. Let \(M\) count shortest absent **scattered** binary subsequences of this linear word. Count cuts by their positions even if the circular word is periodic. Then the shortest absent subsequences always have length \(k+1\), and their *complete multiplicity histogram* is
\[
\#\{\text{cuts}:M=1\}=z,\qquad
\#\{\text{cuts}:M=2\}=2z,
\]
\[
\#\{\text{cuts}:M=s+2\}=2\#\{i:r_i\ge s\}\quad(s\ge1).
\]
Every other value of \(M\) occurs at zero cuts. Thus the profile is determined by the lengths of runs of short gaps, regardless of their cyclic order. The total number of cut positions is \(2k+z\).

In particular, define \(W_m=\varphi^m(0)\) with \(\varphi(0)=01\), \(\varphi(1)=0\), and \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\). For every integer \(m\ge3\), \(W_m\) is primitive and its \(F_{m+2}\) distinct rotations have exactly \(F_m\) as their longest scattered-subsequence universality index. The number of *shortest absent subsequences* among its length-\(F_m+1\) binary targets has rotation histogram
\[
\#(M=1)=F_{m-1},\qquad
\#(M=2)=2F_{m-1},\qquad
\#(M=3)=2F_{m-2}.
\]
No other \(M\) occurs. For instance, when \(m=8\), the 55 rotations have multiplicities \(1,2,3\) at respectively \(13,26,16\) rotations.

## Assumptions and scope
A *scattered subsequence* is obtained by removing any positions while preserving order; it is not required to be contiguous. A binary word is \(t\)-universal when it contains every binary length-\(t\) word as a scattered subsequence. A shortest absent subsequence is one whose length is minimal among absent binary words. The cyclic word is fixed but a *cut* means an indexed position, and cuts are counted separately even for a periodic word. The Fibonacci specialization uses distinct literal rotations, justified below by primitivity; reversal and letter complementation are not identified. All quantifiers range over arbitrary \(k\ge2\), all specified gap sequences, all their cuts, and all \(m\ge3\) in the specialization.

## Proof
**1. Universality and missing targets for a cut just after a one.** A cut immediately following a \(1\) has the form
\[
w=0^{a_1}1\,0^{a_2}1\cdots0^{a_k}1,\qquad a_j\in\{1,2\}.
\]
Each of the \(k\) consecutive blocks \(0^{a_j}1\) contains either alphabet letter, so selecting one letter from each block embeds every length-\(k\) binary target. The target \(1^{k+1}\) is absent because the word has only \(k\) ones. Hence the shortest absent length is \(k+1\).

For a binary target \(u\) of length \(k+1\), the pigeonhole principle implies that any embedding must select at least two target positions from one of these \(k\) blocks. If \(u\) has a consecutive pair \(01\), such an embedding always exists: place this pair within block number \(j\), where \(j\) is its position in \(u\), and place one remaining symbol in every other block. Consequently absent targets cannot contain \(01\), so they must be of the form \(1^a0^{k+1-a}\), \(0\le a\le k+1\).

The only possible adjacent pair of zeros within one block occurs in a block \(001\). The target \(1^a0^{k+1-a}\) embeds exactly when \(a\le k-1\) and some \(001\)-block has index \(j\ge a+1\): first assign each of the \(a\) ones to an earlier block, then assign two consecutive zeros to block \(j\), and place one zero in every other unused block. Necessity follows from the pigeonhole argument and from the fact that two zeros must occur after the first \(a\) ones. Let \(h\) be the largest index with \(a_h=2\). It exists by hypothesis. Thus precisely the targets
\[
1^a0^{k+1-a}\quad\text{for }h\le a\le k+1
\]
are absent, and the count is \(k-h+2\). If the last \(r\) gaps in this linear gap list are all short and the preceding gap is long, then \(h=k-r\), so \(M=r+2\).

**2. Cuts internal to a double-zero gap.** Exactly one cut position lies strictly between the two zeros of each double-zero gap. A word beginning at such a cut contains the alternating word \((01)^k0\) as a scattered subsequence: use the final zero of the split gap at the beginning, one zero preceding each one, then its other zero at the end. The alternating word \((01)^k0\) has every binary length-\(k+1\) word as a scattered subsequence except \(1^{k+1}\). To prove this, greedily embed the target. The earliest last matched index is \(2(k+1)-\mathbf 1_{\{u_1=0\}}-c(u)\), where \(c(u)\) is the number of changes of letter between consecutive positions of the target; the displayed index is at most \(2k+1\) unless the target is all ones. Since the circular source has only \(k\) ones, exactly that one target is absent. Hence \(M=1\) at each of the \(z\) interior cuts.

**3. All other cuts and their histogram.** Every other cut lies immediately before or immediately after one of the \(k\) ones. Among the \(k\) cuts immediately after one, the terminal streak of short gaps has length \(0\) at exactly \(z\) cuts. Each run of \(r_i\) short gaps following a long gap contributes one cut with each terminal streak length \(1,2,\ldots,r_i\); therefore the number with streak at least index \(s\), *exactly* length \(s\), is \(\#\{i:r_i\ge s\}\). By step 1 these yield \(M=2\) and \(M=s+2\), respectively. Reversal of a word reverses its scattered subsequences bijectively and preserves the number and shortest length of absent subsequences. On a circle, reversal exchanges cuts just before ones with cuts just after ones, and reverses the order of gaps without altering the multiset of short-gap run lengths. Thus cuts before ones give exactly the same histogram. Together with step 2, this proves the general statement. The sum of counts is \(z+2z+2\sum_i r_i=2k+z\), so no cuts are unaccounted for.

**4. Fibonacci specialization.** The substitution satisfies \(W_m=W_{m-1}W_{m-2}\) for \(m\ge2\), and consequently its letter counts are \(\#1(W_m)=F_m\) and \(\#0(W_m)=F_{m+1}\). For \(m\ge3\), the circular word \(W_m\) has no adjacent \(11\) and no triple \(000\). This follows by induction: the image of any cyclic word under \(\varphi\) has no \(11\) because every image begins with zero and every one appears only at the end of image \(01\); if the source has no adjacent \(11\), its image cannot have \(000\), because any two consecutive source ones would be needed to place three consecutive output zeros. The seed \(W_2=010\) has neither forbidden circular pattern, so the assertion follows.

Every one in the image corresponds to a source zero. Two consecutive output ones have either one or two zeros between them because the source zeros are separated by either zero or one source ones. Two consecutive gaps of length one would require three consecutive source zeros, which is forbidden. Thus the cyclic zero gaps of \(W_m\) are in \(\{1,2\}\), with no consecutive short gaps. Let \(t\) be the number of short gaps. Counting both gaps and zeros yields \(t+z=F_m\) and \(t+2z=F_{m+1}\); therefore \(t=F_{m-2}\) and \(z=F_{m-1}\), with \(z\ge1\). Every maximal short-gap run has length one; the general histogram reduces to the three claimed Fibonacci counts.

Finally \(W_m\) is primitive: a proper power must have its symbol-count gcd greater than one, while \(\gcd(F_m,F_{m+1})=1\). Thus its \(F_{m+2}\) indexed cuts give distinct rotations. Their histogram totals \(F_{m-1}+2F_{m-1}+2F_{m-2}=F_{m+2}\). This completes the proof.

## Verification
The accompanying standalone program `verification/verify_circular_sas.py` enumerates every binary cyclic gap sequence of lengths \(2\) through \(8\) with at least one long gap, checks all indexed cuts, directly enumerates the absent length-\(k+1\) binary subsequences, and compares to the proposed histogram. This covers 501 gap sequences and 8,890 cut positions; an independent next-occurrence dynamic program checks shortest-absent counts for the smaller cases. The verifier separately generates Fibonacci words by substitution and concatenation, checks all their rotations through level \(11\), and compares the predicted histogram with dynamic-programming counts. Successful execution prints:

`VERIFY_OK binary_gap_necklaces=501 rooted_cuts=8890 fibonacci_m3_to11=9`

These finite checks do not prove the general theorem; its proof is the preceding classification.

## Relationship to prior work
Brinda, Pelantová, and Turek (2013) study letter balance of the related \(m\)-bonacci morphic words, including the binary Fibonacci specialization; their subject is factor balance rather than absent scattered subsequences. Kosche, Koß, Manea, and Siemer (2021) develop general shortest-absent-subsequence descriptions via arch factorizations. Fleischmann, Haschke, Huch, Mayrock, and Nowotka (2022) develop general nearly-universal scattered-subsequence characterizations, including a recursive counting method for individual linear words. The present statement extracts an exact *complete cyclic rotation histogram* with an order-independent gap-run formula and an explicit Fibonacci orbit law; neither inspected primary treatment presents these evaluations. The general characterization/algorithm can be applied to each rotation in principle, so originality of the closed cyclic classification, not of the underlying scattered-subsequence test, is the point.

## Limitations
The general formula requires binary circular words with zero gaps of length one or two and at least one two-zero gap; no formula is claimed when all gaps have length one or when other gap lengths occur. Indexed cuts and distinct cyclic rotations agree only for primitive words; the general result counts indexed cuts even for periodic inputs. The Fibonacci identity holds for \(m\ge3\). Independent scientific validation and a complete bibliographic uniqueness guarantee have not been established; earlier equivalent formulas under different terminology could exist.

## References
- K. Brinda, E. Pelantová, O. Turek, *Balances of m-bonacci words*, arXiv:1301.3334 (first publicly submitted 2013-01-15). https://arxiv.org/abs/1301.3334
- P. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (2021). https://arxiv.org/abs/2108.13968
- P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words – Investigating Simon Congruence*, arXiv:2202.07981 (2022). https://arxiv.org/abs/2202.07981
- *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025). https://arxiv.org/abs/2504.21471
