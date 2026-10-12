# Binary three-state unambiguous automata have mortality threshold \(6\) in one class
## Finding
Let \(\mathcal A=(Q,\{a,b\},\delta)\) be a three-state nondeterministic finite automaton, with transitions represented by \(3\times3\) zero-one matrices \(A\) and \(B\). Call \(\mathcal A\) unambiguous when, for every word \(w\) and states \(p,q\), there is at most one path from \(p\) to \(q\) labeled \(w\). Equivalently, every ordinary integer product of \(A\) and \(B\) is again a zero-one matrix.

A word is killing, mortal, or uncompletable when it labels no path at all, equivalently when its transition-matrix product is zero. Among all binary three-state unambiguous automata that admit such a word, the maximum possible length of a shortest killing word is
\[
6.
\]

Among all \(512^2=262{,}144\) ordered labeled pairs of transition matrices, exactly \(12{,}502\) are unambiguous and exactly \(7{,}699\) of those are mortal. Their shortest killing-word lengths have the exact distribution
\[
\begin{array}{c|rrrrrr}
\ell&1&2&3&4&5&6\\
\hline
N_\ell&271&3552&3192&540&132&12.
\end{array}
\]

The twelve labeled extremizers form a single isomorphism class under simultaneous permutation of the three states and exchange of the two input letters. A canonical representative is
\[
A=\begin{pmatrix}0&1&0\\1&0&0\\0&0&0\end{pmatrix},\qquad
B=\begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix}.
\]
Thus every extremizer is in fact partial deterministic. For the displayed representative, \(a\) swaps states \(0,1\) and is undefined at state \(2\), while \(b\) is the directed three-cycle \(0\to1\to2\to0\). A shortest killing word is \(\mathtt{abaaba}\).

## Assumptions and scope
Unambiguity is the strong all-pairs notion: for each word and ordered pair of states, there is at most one labeled path. Under ordinary integer matrix multiplication, the \((p,q)\)-entry of a word product counts such paths, so the matrix formulation is exact.

The two input letters are named during labeled enumeration and may induce equal transition relations. The final class quotient allows state relabeling and exchange of the letters. Automata without a killing word are excluded from the threshold maximum.

## Proof
There are \(2^9=512\) possible zero-one transition relations for one letter, hence \(512^2\) ordered binary automata.

Precompute the ordinary integer product of every pair of zero-one \(3\times3\) matrices. A product is marked invalid as soon as an entry exceeds \(1\). For a generator pair \((A,B)\), perform breadth-first search from the identity matrix through right multiplication by \(A\) and \(B\). Every reachable node is a word product. The automaton is unambiguous exactly when no explored multiplication is invalid. If it is unambiguous, the first visit to the zero matrix is exactly the length of a shortest killing word.

The exhaustive search yields \(12{,}502\) unambiguous pairs. Of these, \(7{,}699\) reach zero, with the complete histogram stated above. No unambiguous pair has mortality threshold greater than \(6\).

For every threshold-\(6\) pair, examine all six simultaneous state permutations and both letter orders, and select the lexicographically least encoded matrix pair. All twelve extremizers have the same canonical pair, whose row-major binary codes are \((10,98)\), giving the displayed matrices.

For this representative, exhaustive testing of every binary word of lengths below \(6\) finds no zero product, while
\[
A B A A B A=0.
\]
Hence \(\mathtt{abaaba}\) proves that the upper bound \(6\) is sharp.

## Verification
Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The verifier regenerates all \(262{,}144\) generator pairs. It checks unambiguity and mortality by ordinary integer matrix multiplication. Whenever an integer product remains zero-one, a separately implemented Boolean-relation composition must give the identical relation, providing an independent transition-product check.

The replay checks the full mortality histogram, the twelve extremizers, their unique canonical class, the partial-deterministic and strong-connectivity properties of the representative, every shorter binary word, and the killing product for \(\mathtt{abaaba}\).

## Relationship to prior work
Kiefer and Mascle formulate killing words for nonnegative integer matrices and unambiguous finite automata, prove a polynomial upper bound for the length of a shortest killing word in an \(n\)-state unambiguous automaton, and discuss quadratic lower bounds. Their results are asymptotic in the number of states and do not give the exact binary three-state value.

Boccuto and Carpi study the same automata under the term uncompletable word, emphasizing that sharp estimates for the shortest uncompletable word remain a central problem. Their results provide structural and general upper bounds, not a complete three-state binary census.

Ryzhikov later studies the mortality threshold as a function of state count and alphabet size for general nondeterministic automata. That broader model has a different extremal function; the paper surveys the polynomial unambiguous-automaton bound but does not determine the exact binary three-state unambiguous threshold or classify equality cases.

Searches using killing-word, mortal-word, uncompletable-word, diamond-free, Boolean-matrix, and three-state binary formulations found no published statement of the value \(6\), the twelve labeled extremizers, or the one-class classification.

## Limitations
The classification is specific to three states and two letters. It does not determine the exact mortality threshold for larger unambiguous automata or for larger fixed alphabets.

The exhaustive proof is finite and exact, but an unindexed computation or unpublished small-state census could contain the same data. The public literature inspected establishes the general problem and bounds rather than this equality layer.

## References
1. S. Kiefer and A. Mascle, “On Nonnegative Integer Matrices and Short Killing Words,” arXiv:1808.00940v1, first public version 2018-08-02.
2. G. Boccuto and A. Carpi, “On the length of uncompletable words in unambiguous automata,” RAIRO - Theoretical Informatics and Applications 53 (2019), article 2, DOI 10.1051/ita/2019002.
3. A. Ryzhikov, “On shortest products for nonnegative matrix mortality,” arXiv:2405.19622v1, first public version 2024-05-30.
