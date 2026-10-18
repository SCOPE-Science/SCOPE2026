# Counting-logic identification of height-two permutation posets through ten points

## Finding
For each \(1\le n\le 10\), the stable counting-colour-refinement multiset of vertex colours in the directed strict-order relation determines, up to isomorphism, every \(n\)-element poset of height at most two and Dushnik--Miller order dimension at most two. Equivalently, within this poset class, \(\mathsf C^2\)-equivalence implies isomorphism for all sizes through ten. The exact number of types for sizes one through ten is
\[
(1,2,4,9,21,55,151,447,1389,4502).
\]
At size ten the proof examines \(16{,}796\) permutation representations yielding exactly \(4{,}502\) different types. No assertion is made for sizes eleven or larger.

## Assumptions and scope
A finite strict poset is encoded by the irreflexive transitive binary relation \(<\), not merely its Hasse covers. Its height is the largest cardinality of a chain, and its dimension the smallest number of linear extensions whose intersection is \(<\). A counting-refinement round starts from the uniform vertex colour and refines each vertex by its old colour and the separate multisets of predecessor and successor colours; palettes are shared globally across all structures being compared. Graph fingerprints are multisets of resulting vertex colours. The theorem concerns the relative isomorphism problem inside the specified natural subclass, not arbitrary graphs and not unbounded order sizes.

## Proof
**Finite search space.** Let \(P\) have dimension at most two. Choose a realizer of two linear orders and relabel elements \(0,\ldots,n-1\) in their first order. Write the second order as a permutation \(p\), so
\[
i<_P j\quad\Longleftrightarrow\quad i<j\text{ and }p_i<p_j.
\]
The strict order contains a three-element chain if and only if the permutation contains an increasing subsequence of length three. Hence precisely the permutations avoiding the pattern \(123\) cover every poset in scope (possibly several times through different realizers).

**Exact generator.** Starting with the empty tuple, insert the new largest value into a shorter avoiding permutation. An insertion is allowed precisely at or before the first position after an adjacent ascent in the shorter permutation (with all insertion positions allowed if it is decreasing). Indeed an increasing pair before the new maximum would create a new increasing triple, while one cannot otherwise create a new triple involving the maximum. Conversely deleting the maximum from a \(123\)-avoider uniquely reverses one such insertion. The algorithm in `verify_posets.py` implements this recurrence and checks each generated family against the Catalan number \(\binom{2n}{n}/(n+1)\). It generates exactly 16,796 objects at \(n=10\).

**Exact common palette.** For each size \(n\), initialize all vertices of every generated strict poset with the same integer colour. Simultaneously apply exactly \(n\) rounds of the tuple-valued directed counting update; a fresh integer is assigned to each *different exact tuple* in the joint collection, without hashing or floating-point comparisons. A graph signature is the sorted list of its final colours. The program groups all generated permutation posets by these signatures.

**Isomorphism certification.** For every signature group, `verify_posets.py` compares its first strict-order matrix with every remaining strict-order matrix by complete bijection backtracking. Only bijections preserving their current vertex colours are considered; both orientations of every ordered-pair relation are checked exactly as each new pair is assigned. Successful termination constructs an isomorphism, so there is no possibility of a false isomorphism assertion from a coincident signature. Every group passes. As automorphisms and isomorphisms preserve each refinement round, isomorphic posets necessarily have equal signatures. Conversely the exhaustive check shows each equal-signature pair is isomorphic. Since stable refinement is at least as discriminating as the displayed \(n\)-round refinement, equality of stable signatures likewise implies isomorphism. Each reported number of groups therefore equals the exact number of poset isomorphism types.

**Logical interpretation.** Directed counting refinement on a finite relational structure is the standard two-variable counting-logic equivalence test (using predecessor and successor counts), giving the relative \(\mathsf C^2\) conclusion. The finite proof does not require quantifier-rank minimality.

## Verification
Run `python3 verify_posets.py` and `python3 verify_generator.py` using standard Python. The former enumerates every \(123\)-avoiding permutation up to size ten, obtains exact strict-order matrices, executes common-palette refinement, and compares every within-signature pair to a representative by complete isomorphism search. Its last line is `PASS: every equal round-n directed-counting fingerprint is isomorphic through n=10; n=10 has 4502 global types`. The latter independently brute-forces every permutation through size eight, checks avoidance directly, and builds strict-order matrices and palettes independently; it ends `PASS: independent brute permutations agree through n=8`. Their actual standard outputs are enclosed as separate files. Computation is an exhaustive finite proof here, not extrapolation.

## Relationship to prior work
Cooper and Kirkpatrick (arXiv:1409.4368) discuss permutation posets and pattern-counting problems, providing the natural two-order representation but not the present exhaustive directed-refinement cutoff. Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255) develop graph colour refinement and counting logic for undirected graphs; a general methodology does not establish identification on the present restricted directed-order family. Klavík and Zeman (arXiv:1506.05064) study automorphism groups of comparability graphs, a different invariant on undirected comparability graphs. Search for equivalent directed-poset cutoff results did not find a stronger implication; specialist earlier enumeration remains a risk.

## Limitations
The bound ten is the largest *verified* size, not a proven sharp first-failure size. A collision might first occur at eleven or later, or never; this theorem does not decide it. The exact reported type counts follow from the executable finite certificate, so they depend on correct execution of the complete generator, palette update and bijection backtracking. The result concerns the full strict relation and a shared palette, not independent graph-by-graph palette names. No independent scientific validation or publication priority determination is claimed.

## References
1. Joshua Cooper and Andrew Kirkpatrick, *The Complexity of Counting Poset and Permutation Patterns*, arXiv:1409.4368v1, first public 2014-09-15, https://arxiv.org/abs/1409.4368.
2. Vikraman Arvind, Johannes Köbler, Gaurav Rattan, Oleg Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255v1, 2015-02-04, https://arxiv.org/abs/1502.01255.
3. Pavel Klavík and Peter Zeman, *Automorphism Groups of Comparability Graphs*, arXiv:1506.05064v1, 2015-06-16, https://arxiv.org/abs/1506.05064.
