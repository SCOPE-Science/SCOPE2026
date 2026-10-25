# The binary four-state adversarial synchronization hierarchy collapses at level three

## Finding

For complete deterministic automata with four labeled states and the two distinguished input letters `a` and `b`, consider the adversarial \(k\)-synchronization game of Lipin and Volkov: Alice plays one letter per turn, Bob replies with any word of length strictly less than \(k\), including the empty word, and Alice wins upon obtaining a reset word. Write \(\mathcal A_k\) for the automata on which Alice can force a win, and \(\mathcal A_\omega\) for the arbitrary-finite-reply game.

**Theorem (complete binary four-state census).** For the \(4^8=65{,}536\) ordered transition tables, the exact numbers in the successive classes are

\[
\begin{array}{c|rrrrrrr}
 k&1&2&3&4&5&6&\omega\\\hline
 |\mathcal A_k|&51{,}520&25{,}360&22{,}384&22{,}384&22{,}384&22{,}384&22{,}384\\
\end{array}
\]

In particular, within the **binary four-state** class, \(\mathcal A_3=\mathcal A_\omega\) and this cutoff is sharp because \(\mathcal A_2\ne\mathcal A_3\). Partitioned into nonsynchronizing automata, \(\mathcal A_1\setminus\mathcal A_2\), \(\mathcal A_2\setminus\mathcal A_3\), and \(\mathcal A_\omega\), the labeled counts are respectively

\[14{,}016,\quad26{,}160,\quad2{,}976,\quad22{,}384.\]

Modulo simultaneous relabeling of the four states and interchange of the two input letters, there are exactly \(1{,}474\) equivalence classes; the four categories have respectively \(359,551,62,502\) classes. A sharpness witness in \(\mathcal A_2\setminus\mathcal A_3\) is the automaton whose transitions, indexed by states \(0,1,2,3\), are

\[a=(2,3,2,0),\qquad b=(1,0,0,0).\]

The witness has every two-state position winning in the \(2\)-game, whereas in the \(3\)-game only the pair \(\{1,2\}\) is winning when Bob may play first.

## Assumptions and scope

Both letters are distinguished; two symbols are counted separately even if their transition transformations coincide. States are exactly \(Q=\{0,1,2,3\}\), with complete deterministic transitions. All \(256\) functions \(Q\to Q\) are allowed as each letter's action, without accessibility, connectivity, minimality, or synchronizing restrictions. The group of state permutations and the independent two-letter swap acts on the full set of \(65{,}536\) tables. The orbit count identifies automata under that group only; it does not identify arbitrary transition semigroups.

The game has perfect information and lasts indefinitely unless a singleton image is reached. Alice chooses one input symbol on each turn; Bob chooses any word of length \(0,1,\ldots,k-1\) on each response, or an arbitrarily long finite word for \(k=\omega\). An automaton belongs to \(\mathcal A_k\) if Alice can force eventual synchronization regardless of Bob's choices. The order of the first move does not affect this whole-automaton winning property.

## Proof

**Pair reduction.** An image of an unordered pair \(p=\{i,j\}\) under a word is either a pair or a singleton. By the two-token localization lemma for synchronization games (Lipin--Volkov, Lemma 2.3), Alice wins from all four active states if and only if she wins from each two-token position. This equivalence also follows directly: Bob may preserve a pair that Alice cannot merge, while Alice may successively merge tokens pair by pair whenever all pairs are winning.

Let \(X\) be the six unordered distinct-state pairs and add an absorbing singleton symbol \(\bot\). For a letter \(c\), let \(t_c:X\cup\{\bot\}\to X\cup\{\bot\}\) apply the letter to both members of a pair, returning \(\bot\) when they coalesce. For \(p\) and integer \(k\ge1\), define the exact reply reachability set

\[R_k(p)=\{t_w(p):w\in\{a,b\}^{<k}\}.\]

For unrestricted replies, \(R_\omega(p)\) is the complete directed-graph reachability closure, including the empty path. Define \(W_0=\{\bot\}\), and for \(r\ge0\),

\[
W_{r+1}=W_r\cup\left\{p\in X:\ \forall q\in R_k(p)\ \exists c\in\{a,b\}:t_c(q)\in W_r\right\}.
\]

Inductively, the extra pairs in \(W_{r+1}\) are those from which Alice can force a merger in at most \(r+1\) of her moves when Bob chooses the next response word before she chooses a letter. The absorbing state always lies in \(W_r\). Because only six nonsingleton positions exist and the winning operator is monotone, the increasing sequence stabilizes after at most six strict additions. Its fixed point is the precise winning region: any position outside it permits Bob, after every move, to select a reply preserving the complement indefinitely. By the pair reduction and the irrelevance of who starts, the whole automaton is in \(\mathcal A_k\) precisely when all six pairs lie in the fixed point.

**Exhaustive evaluation.** Encode a map \(f:Q\to Q\) by its four base-four digits \((f(0),f(1),f(2),f(3))\). Iterate both independent maps from code \(0\) through \(255\), obtaining exactly \(256^2=65{,}536\) labeled ordered two-letter tables. For each table, build the six pair transitions and evaluate the finite fixed-point recurrence. The attached `verify_bobfirst.py` implements the displayed quantified operator; `verify_alicefirst.cpp` independently applies the opposite turn-order recurrence (Alice chooses a letter, Bob chooses a bounded response). Both produce the identical class counts stated above.

There is no unexamined infinite-word approximation in the \(\omega\)-column. Any nonsingleton pair reachable from a given pair has a shortest path using at most five transitions: a shorter path exists whenever a nonsingleton vertex repeats, and there are only six nonsingleton vertices. Thus \(R_6(p)\) includes every nonsingleton pair in \(R_\omega(p)\); any additional singleton endpoint is already winning. The independent implementation also computes the full unbounded reachability closure for every pair of every transition table and compares its nonsingleton part with \(R_6\). Therefore \(\mathcal A_6=\mathcal A_\omega\) holds by exact graph reachability, while the enumerated coincidence at levels \(3,4,5,6\) proves \(\mathcal A_3=\mathcal A_\omega\).

**Orbit evaluation.** For every state permutation \(\pi\), act on each letter transformation by conjugation \(\pi\circ f\circ\pi^{-1}\). Also interchange the two letter transformations. Take the lexicographically least encoded ordered pair of maps among these \(24\cdot2\) transforms. The code `verify_orbits.py` computes this canonical representative for all tables; equality of representatives holds exactly when the tables are in the same orbit. Its \(1{,}474\) classes and four-category orbit counts reproduce the labeled totals by adding the actual orbit sizes. The sharpness witness above was extracted from the \(62\) classes strictly between levels two and three.

These finite, fully enumerated calculations, together with the game-theoretic equivalence and finite fixed-point proof, establish the stated assertions for **every** binary four-state deterministic automaton.

## Verification

In the package directory, run `sh run_checks.sh` with a C++17 compiler and Python 3. The script builds the independent C++ enumerator and executes both Python checks. The included `check_output.txt` records:

- \(n=4\): the sequence \(51{,}520,25{,}360,22{,}384,22{,}384,22{,}384,22{,}384\) at levels one through six;
- independent Bob-first evaluation: the same sequence and unrestricted-closure count \(22{,}384\);
- disjoint labeled category counts \(14{,}016,26{,}160,2{,}976,22{,}384\);
- the independent quotient: \(1{,}474\) orbits, with category sizes \(359,551,62,502\);
- a smaller \(n=3\) cross-check: \(549,381,381\) at the first three levels.

Every claimed cardinality comes from exhaustive finite loops, not simulation or asymptotic inference. The programs use only the standard libraries of their respective languages.

## Relationship to prior work

Lipin and Volkov, *Adversarial Synchronization* (arXiv:2601.18362v1, first posted 26 January 2026), introduce these bounded-reply games, prove the pair-localization criterion, and establish that for **arbitrary alphabets** the optimal universal stabilization cutoff on four-state automata is \(\binom{4}{2}=6\). That theorem proves equality at six but neither implies the stronger binary-alphabet cutoff of three nor enumerates the four-level distribution. Their three- and four-letter constructions illustrate why alphabet restrictions change the question. This finding uses their game definitions and localization lemma, not a new game-solving algorithm.

Fernau, Haase, and Hoffmann, *The Synchronization Game on Subclasses of Automata* (LIPIcs FUN 2022, DOI:10.4230/LIPIcs.FUN.2022.14), study the earlier alternating single-letter game, plus complexity and structural subclasses. Their classification is not an enumeration of the bounded-response \(k\)-hierarchy across all four-state binary transition pairs. The marginal \(\mathcal A_1\) count concerns ordinary synchronizability and is not asserted as an independent novelty claim; the new content is the full adversarial stratification, sharp binary cutoff, and the symmetry-class census.

## Limitations

The result is finite and restricted to exactly four states and two distinguished input symbols. It does not assert any formula for larger state sets or larger alphabets, nor that the quotient classes are distinct transition monoids. The occurrence of a cutoff of three in this finite case alone is not evidence for an unrestricted alphabet-sensitive formula. Publicly unindexed equivalent enumerations or an inaccessible conference variant of the main source may affect historical priority; no independent human assessment is claimed.

## References

1. A. E. Lipin and M. V. Volkov, *Adversarial Synchronization*, arXiv:2601.18362v1 (26 January 2026), https://arxiv.org/abs/2601.18362, Sections 2, 4 and 5.
2. H. Fernau, C. Haase, and S. Hoffmann, *The Synchronization Game on Subclasses of Automata*, 11th International Conference on Fun with Algorithms (FUN 2022), DOI:10.4230/LIPIcs.FUN.2022.14, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FUN.2022.14.
3. A. E. Lipin and M. V. Volkov, *Adversarial Synchronization and Reset Length*, CiE 2026, pages 358--373, DOI:10.1007/978-3-032-31348-5_24 (conference version; complete accessible text not inspected).
