# Complete repetition-factorization ambiguity profile of the regular paperfolding word
## Finding
Let \(\mathbf{p}\) be the regular paperfolding word, obtained from the fixed point of
\[
0\mapsto01,\qquad 1\mapsto21,\qquad 2\mapsto03,\qquad 3\mapsto23
\]
by the coding \(0,1\mapsto0\) and \(2,3\mapsto1\).

Among all distinct factors of \(\mathbf{p}\), exactly \(232\) admit a repetition factorization. Of these, exactly \(112\) have a unique repetition factorization and exactly \(120\) have more than one. The complete distribution by number of factorizations is
\[
\begin{array}{c|rrrrrr}
\text{number of factorizations}&1&2&3&4&5&6\\ \hline
\text{number of factors}&112&94&12&2&10&2.
\end{array}
\]
No factor has more than \(6\) repetition factorizations.

The shortest nonuniquely factorable factors have length \(9\), and there are exactly four:
\[
\mathtt{000110110},\quad
\mathtt{011011000},\quad
\mathtt{100100111},\quad
\mathtt{111001001}.
\]
For example,
\[
\mathtt{111001001}
=(\mathtt{11})(\mathtt{1001001})
=(\mathtt{111})(\mathtt{001001}).
\]
The longest factors with a unique repetition factorization have length \(30\), and there are exactly two. The maximum multiplicity \(6\) occurs for exactly two factors, both of length \(25\). The complete factor-by-factor list and every factorization are given in `catalog.json`.

## Assumptions and scope
A nonempty word is a repetition if it has a period at most half its length. A repetition factorization is a decomposition into nonempty repetitions.

The classification uses the published theorem that every factor of every paperfolding word having a repetition factorization has length at most \(45\). Thus it is enough to determine the exact regular-paperfolding factor language through length \(45\) and inspect all such factors.

The statement is for the regular paperfolding word with the coding displayed above. It does not classify ambiguity for all paperfolding instruction sequences.

## Proof
Let \(\mu\) denote the displayed \(2\)-uniform morphism on four letters, and let
\[
U_k=\mu^k(0).
\]
Direct exact factor-set computation gives identical factor sets in \(U_9\) and \(U_{10}\) for every length at most \(45\).

This stabilization is a finite certificate of the complete factor language at those lengths. Indeed, a length-\(L\) factor of \(\mu(z)\) is determined by its starting offset modulo \(2\) and by a source factor of length at most
\[
\left\lceil\frac{L+1}{2}\right\rceil.
\]
For \(L\le45\), this source length is at most \(23\). Since all source factor sets through length \(45\), in particular through length \(23\), agree at two consecutive stages, applying \(\mu\) produces no new factor of length at most \(45\) at the next stage. Induction gives no new such factors at any later stage. Applying the coding therefore gives the exact binary factor language of \(\mathbf p\) through the published global cutoff.

For each binary factor \(w\) in this finite language, the verifier tests every prefix length \(j\). A prefix \(w[0..j-1]\) is an admissible first block exactly when it has a period \(d\) satisfying
\[
1\le d\le j/2.
\]
Dynamic programming over the cut position then enumerates every repetition factorization of \(w\), with no pruning by width or by a guessed bound. Summing the resulting exact factorization counts gives the displayed distribution.

Because the published cutoff \(45\) applies to every factor carrying any repetition factorization, the finite computation is exhaustive for the infinite regular paperfolding word rather than a sampled prefix census.

## Verification
Run `python3 verify.py` beside `catalog.json` and `certificate.json`.

The first engine reconstructs the four-letter fixed point, proves bounded factor-language stabilization by exact equality of the length-\(1\) through length-\(45\) factor sets at substitution levels \(9\) and \(10\), applies the binary coding, and enumerates all repetition factorizations by dynamic programming.

A second engine generates \(65536\) paperfolding bits independently from the odd-part characterization: the bit at one-based position \(n\) is \(0\) when the odd part of \(n\) is congruent to \(1\pmod4\), and \(1\) otherwise. It independently recovers exactly the same factor sets through length \(45\).

Finally the verifier recomputes the full catalogue and checks byte-level scientific content against the embedded `catalog.json` summary and records.

## Relationship to prior work
Rampersad, Shallit, and Xu develop a general first-order method for repetition factorizations in automatic sequences. For the Thue--Morse word they prove that every factor having a repetition factorization has exactly one. In the following paperfolding section they determine the maximum shortest width for the regular paperfolding word and for arbitrary paperfolding words, but do not state an ambiguity census or a uniqueness classification.

The same paper proves the decisive global cutoff: every factor of every paperfolding word that admits a repetition factorization has length at most \(45\). That theorem makes a complete factor-by-factor ambiguity classification possible without any asymptotic extrapolation.

The earlier work of Inoue, Matsuoka, Nakashima, Inenaga, Bannai, and Takeda develops algorithms for computing shortest and longest repetition factorizations of finite strings and studies Fibonacci strings. It does not contain a regular-paperfolding ambiguity profile.

Targeted searches for regular-paperfolding repetition-factorization uniqueness, nonuniqueness, the length-\(45\) cutoff together with ambiguity, and the shortest ambiguous factor did not locate a covering published statement.

## Limitations
The result is a complete finite classification for one named infinite word because a published theorem supplies the global length cutoff. It does not give a symbolic characterization of which unfolding-instruction sequences have unique or nonunique factorizations.

The counts depend on distinct factors, not occurrences. The catalogue records factorizations by their cut-length compositions; for a fixed word those compositions determine the factor blocks uniquely.

An unindexed computation or unpublished note could contain the same census.

## References
1. N. Rampersad, J. Shallit, and X. Xu, “Repetition Factorization of Automatic Sequences,” arXiv:2311.14961v1, first public version 2023-11-25; International Journal of Foundations of Computer Science 36(3), 479–499, DOI 10.1142/S0129054124430019.
2. H. Inoue, Y. Matsuoka, Y. Nakashima, S. Inenaga, H. Bannai, and M. Takeda, “Factorizing Strings into Repetitions,” Theory of Computing Systems 66 (2022), 484–501, DOI 10.1007/s00224-022-10070-3.
