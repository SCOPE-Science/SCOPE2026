# Exact single-deletion optima for the \((2,\infty)\)-RLL source through length eleven
## Finding
For the Kulkarni--Kiyavash constrained source \(S_n(2,\infty)\), the exact maximum sizes of single-deletion-correcting codes for \(2\le n\le11\) are \(1,1,1,1,1,1,2,2,3,4\). At \(n=11\), where the source has \(19\) words and the published Theorem V.2 bound is \(823/105\) (hence the integer upper bound \(7\)), the exact maximum is \(4\) and there are exactly three labeled maximum codes. All three contain \(00000000000\), their other three words each have Hamming weight \(2\), their one-deletion shadow-size profile is \(1,5,5,5\), and each covers exactly \(16\) distinct length-ten received words. Coordinate reversal fixes one maximum and interchanges the other two.

The three maximum length-eleven codes are
\[
\begin{aligned}
C_1&=\{00000000000,00000100100,00010001000,00100100000\},\\
C_2&=\{00000000000,00001000100,00010010000,00100001000\},\\
C_3&=\{00000000000,00001001000,00010000100,00100010000\}.
\end{aligned}
\]
Reversal fixes \(C_1\) and swaps \(C_2\) with \(C_3\).

## Assumptions and scope
For \(n\ge2\), let \(S_n(2,\infty)\) be the binary length-\(n\) source used by Kulkarni and Kiyavash: the first and last runs are zero-runs of length at least \(2\), every zero-run has length at least \(2\), and every one-run has length exactly \(1\). For a word \(x\), let \(D_1(x)\) be the set of distinct length-\(n-1\) words obtained by deleting one coordinate. A code \(C\subseteq S_n(2,\infty)\) corrects one deletion when \(D_1(x)\cap D_1(y)=\varnothing\) for all distinct \(x,y\in C\).

The claim is finite and only concerns \(2\le n\le11\), with an equality-case classification at \(n=11\). “Labeled” means that distinct subsets of the fixed coordinate set are counted separately; no quotient by reversal is taken in the count of three.

## Proof
The source is generated directly from the run constraints. Its cardinalities for \(n=2,\ldots,11\) are
\[
1,1,1,2,3,4,6,9,13,19.
\]
For each source word, form its exact distinct one-deletion shadow. Two source words are compatible precisely when these shadows are disjoint.

An exhaustive subset search gives maximum code sizes
\[
1,1,1,1,1,1,2,2,3,4
\]
for \(n=2,\ldots,11\), with numbers of labeled maximizers
\[
1,1,1,2,3,4,1,6,3,3.
\]
For each \(n\), after all maximizing subsets are found, every subset of one larger cardinality is also enumerated and none is compatible. Since any still larger code would contain such a forbidden subset, this is an exhaustive upper bound, not a heuristic search.

At \(n=11\), the three compatible four-subsets are exactly \(C_1,C_2,C_3\) above. Direct inspection of the reconstructed shadows gives profile \((1,5,5,5)\) for each code and a disjoint union of \(16\) received words. Their intersection is exactly \(\{00000000000\}\), and every other codeword in the three maxima has Hamming weight \(2\).

As an independent compatibility calculation, the verifier computes the longest common subsequence length by dynamic programming. For two length-\(n\) words, their one-deletion shadows intersect exactly when they have a common subsequence of length \(n-1\); thus compatibility is equivalent to longest common subsequence length at most \(n-2\). This independent pairwise criterion agrees with direct shadow disjointness on every source pair for every \(2\le n\le11\).

Finally, substituting \(n=11\) and \(d=2\) into Kulkarni--Kiyavash Theorem V.2 gives \(823/105\). Since code cardinality is integral, that published bound gives at most \(7\), while the exhaustive calculation gives the strict exact value \(4\).

## Verification
`artifacts/verify.py` uses only the Python standard library. It regenerates every source word for \(2\le n\le11\), constructs all deletion shadows, independently computes longest common subsequences, enumerates all candidate subsets through the first impossible size, verifies the complete optimum and maximizer-count sequences, checks the three explicit length-eleven maxima, re-evaluates the published bound as \(823/105\), and checks the reversal action. The recorded replay is in `artifacts/verification_output.txt`.

The calculation is finite: the largest source contains only \(19\) words, and the decisive no-five-code check at \(n=11\) examines all \(\binom{19}{5}=11628\) five-subsets. No timeout, sampling, randomization, or extrapolation is used.

## Relationship to prior work
Kulkarni and Kiyavash define the exact constrained-source deletion-code problem and the convention for \(S_n(d,\infty)\), then derive Theorem V.2, a non-asymptotic upper bound for the optimal one-deletion code. Their run-length-limited section explicitly says that simplifying the resulting bounds exactly is beyond the scope of that paper; it does not give the exact optimum or equality cases at \((d,n)=(2,11)\).

Earlier and contemporaneous run-length-limited synchronization-code papers by Bours, Cheng--Ferreira--Broere, and Palunčić--Abdel-Ghaffar--Ferreira--Clarke develop algebraic or moment-based constructions and asymptotic performance. The directly inspected Palunčić et al. text develops an asymptotically optimal construction and decoding framework, not an exact finite maximum at this source and length. These constructions therefore do not imply the finite equality census above.

Targeted database searches using the exact source notation, the parameters \((2,\infty)\) and \(n=11\), “run-length limited single deletion,” and equivalent constrained-source wording did not locate a published exact value or equality classification. The result is accordingly a finite refinement of the published constrained-source bound, not a replacement for the general theory.

## Limitations
The result is restricted to the endpoint convention for \(S_n(2,\infty)\) used in the cited 2012 source, where the first and last zero-runs also have length at least \(2\). Other RLL conventions can produce different finite source sets. No formula for arbitrary \(n\) or arbitrary \(d\) is claimed. The originality search cannot exclude an obscure or unindexed historical enumeration.

## References
1. A. A. Kulkarni and N. Kiyavash, “Non-asymptotic Upper Bounds for Deletion Correcting Codes,” arXiv:1211.3128v1, 13 November 2012; especially Section V-A and Theorem V.2.
2. P. A. H. Bours, “Construction of fixed-length insertion/deletion correcting runlength-limited codes,” IEEE Transactions on Information Theory 40(6), 1841–1856 (1994), DOI 10.1109/18.340459.
3. L. Cheng, H. C. Ferreira, and I. Broere, “Moment Balancing Templates for (d,k)-Constrained Codes and Run-Length Limited Sequences,” IEEE Transactions on Information Theory 58(4), 2244–2252 (2012), DOI 10.1109/TIT.2011.2178089.
4. F. Palunčić, K. A. S. Abdel-Ghaffar, H. C. Ferreira, and W. A. Clarke, “A Multiple Insertion/Deletion Correcting Code for Run-Length Limited Sequences,” IEEE Transactions on Information Theory 58(3), 1809–1824 (2012), DOI 10.1109/TIT.2011.2172725.
