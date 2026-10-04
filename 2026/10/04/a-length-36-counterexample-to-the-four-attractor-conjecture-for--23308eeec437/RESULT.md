# A length-\(36\) counterexample to the four-attractor conjecture for binary generalized pseudostandard words
## Finding
The conjecture that every pseudopalindromic prefix of a binary generalized pseudostandard sequence has a minimum string attractor of size at most four is false.  Take directive prefixes
\[
\Delta=00101,\qquad \Theta=EEEER.
\]
Under successive shortest pseudopalindromic closures, the fifth prefix is

`010110010101100101101001101010011010`

and has length \(36\).  Its minimum string-attractor size is exactly \(5\).  One minimum attractor, with positions indexed from zero, is
\[
\Gamma=\{3,7,15,21,25\}.
\]

## Assumptions and scope
For a finite binary word, a string attractor is a set of positions such that every nonempty factor has an occurrence crossing at least one selected position.  Let \(R\) be reversal and let \(E\) be reversal followed by binary complementation.  The \(R\)-closure or \(E\)-closure of a word is the shortest palindrome or antipalindrome, respectively, having that word as a prefix.

A binary generalized pseudostandard sequence is generated from \(w_0=\varepsilon\) by
\[
w_{n+1}=(w_n\delta_{n+1})^{\vartheta_{n+1}},
\]
where \(\delta_i\in\{0,1\}\), \(\vartheta_i\in\{E,R\}\), and the superscript denotes the corresponding shortest pseudopalindromic closure.  The finite directives above can be continued arbitrarily to infinite directives, so the displayed word is a pseudopalindromic prefix of a binary generalized pseudostandard sequence.

## Proof
Applying the closure definition gives the five successive prefixes
\[
\begin{aligned}
w_1&=01,\\
w_2&=0101,\\
w_3&=0101100101,\\
w_4&=010110010101100101,\\
w_5&=010110010101100101101001101010011010.
\end{aligned}
\]
The last word is a palindrome, as required by the final \(R\)-closure.

For the lower bound, for any factor \(f\) let \(U(f)\) be the union of all coordinate positions occupied by all occurrences of \(f\).  Every string attractor must meet \(U(f)\).  Seven factors give the following exact sets:
\[
\begin{array}{c|c}
f & U(f)\\ \hline
101101 & \{15,\ldots,20\}\\
01011001010 & \{0,\ldots,10\}\\
1100 & \{3,\ldots,6\}\cup\{11,\ldots,14\}\\
10101100 & \{7,\ldots,14\}\\
00110101 & \{21,\ldots,28\}\\
0011 & \{21,\ldots,24\}\cup\{29,\ldots,32\}\\
01010011010 & \{25,\ldots,35\}.
\end{array}
\]
The three sets in the coordinate range \(\{0,\ldots,14\}\) have empty common intersection, so at least two attractor positions are needed there.  The first listed factor forces one position in the disjoint range \(\{15,\ldots,20\}\).  The three sets in \(\{21,\ldots,35\}\) likewise have empty common intersection, so at least two positions are needed there.  Thus every attractor has size at least \(2+1+2=5\).

For the upper bound, exhaustive factor enumeration gives exactly \(500\) distinct nonempty factors.  For every one of them, the standalone verifier checks every occurrence and confirms that at least one occurrence crosses \(\Gamma=\{3,7,15,21,25\}\).  Hence \(\Gamma\) is an attractor, proving that the minimum size is exactly \(5\).

## Verification
Run `python3 verify.py`.  The program independently constructs each shortest \(R\)- or \(E\)-closure and checks closure minimality, reconstructs all five prefixes, enumerates all \(500\) distinct factors and all their occurrences, verifies the five-position attractor, and rechecks the seven-factor lower-bound certificate.  As redundant finite verification, it also tests all \(\binom{36}{4}=58905\) four-position sets and confirms that none is an attractor.

The exhaustive computation is finite and exact; it is not used to infer a statement about untested directive prefixes.  The theorem is the single explicit counterexample above.

## Relationship to prior work
Dvořáková and Hendrychová define binary generalized pseudostandard sequences via alternating palindromic and antipalindromic closures and explicitly conjecture that every pseudopalindromic prefix has a minimum string attractor of size at most four.  Their first public arXiv version appeared on 2023-08-01.  Their paper proves size two for the studied complementary-symmetric Rote subclass and size three for the all-antipalindromic pseudostandard subclass, but does not cover arbitrary mixed directives.

An earlier thesis by Hendrychová contains a general brute-force attractor generator and identifies attractors of generalized pseudostandard sequences as an open problem; the inspected thesis text does not state this length-\(36\) word or a size-five pseudopalindromic-prefix attractor.  Targeted searches using the exact word, the directive pair, the conjecture wording, and equivalent minimum-attractor formulations found no published source implying this counterexample.

## Limitations
This result disproves the universal upper bound four but does not determine the optimal universal bound, characterize all mixed directives producing size five, or establish whether minimum attractor sizes for generalized pseudostandard prefixes are bounded.  The originality search cannot exclude an unindexed note, thesis passage, or unpublished computation using different terminology.

## References
1. L. Dvořáková and V. Hendrychová, “String attractors of Rote sequences,” arXiv:2308.00850, first public version 2023-08-01; Discrete Mathematics & Theoretical Computer Science 26:3 (2024), DOI 10.46298/dmtcs.12385.
2. V. Hendrychová, “String attractors,” bachelor thesis, Czech Technical University in Prague, repository handle 10467/111201.
