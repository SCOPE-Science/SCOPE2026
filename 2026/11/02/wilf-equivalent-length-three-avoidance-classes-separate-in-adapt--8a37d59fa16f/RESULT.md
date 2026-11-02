# Wilf-equivalent length-three avoidance classes separate in adaptive comparison dimension

## Finding
Let \(\operatorname{Av}_n(\tau)\) be all permutations of \([n]\) avoiding the classical length-three pattern \(\tau\). Interpret each permutation as a total order on the labeled symbols: the Boolean query \(q_{a,b}\), for \(1\le a<b\le n\), asks whether \(a\) occurs before \(b\) in its one-line notation. Let \(\mathcal C_n(\tau)\) be the resulting comparison concept class.

**Exact finite adaptive classification.** For every forbidden pattern \(\tau\in S_3\), the Littlestone dimensions at \(n=1,2,3,4,5,6,7,8\) are respectively

\[
\begin{array}{c|rrrrrrrr}
 n&1&2&3&4&5&6&7&8\\ \hline
 \tau\in\{123,321\}&0&1&2&3&4&6&7&9\\
 \tau\in\{132,213,231,312\}&0&1&2&3&5&6&8&9
\end{array}.
\]

In particular, **five symbols give the first adaptive-dimension distinction** among single length-three pattern-avoidance classes: \(\operatorname{Ldim}(\mathcal C_5(123))=4\), whereas \(\operatorname{Ldim}(\mathcal C_5(132))=5\). This distinction recurs at seven symbols and disappears again at six and eight within the proved range. All six classes have the same cardinality \(C_n=\frac1{n+1}\binom{2n}{n}\), so cardinality and Wilf equivalence do not determine the dimension.

**Unrestricted static statement.** For every \(n\ge1\) and \(\tau\in S_3\),
\[
\operatorname{VCdim}(\mathcal C_n(\tau))=n-1.
\]
Thus at five symbols the nonmonotone patterns have adaptive-minus-static gap one, while the two monotone patterns have gap zero; at seven symbols the corresponding gaps are two and one.

## Assumptions and scope
Classical pattern avoidance means no three positions \(i<j<k\) whose selected values have relative order \(\tau\). Querying a pair of **labels** is not querying adjacency of positions, and is not the alternative permutation-family VC notion that shatters sets of positions into all factorial patterns. There are \(\binom n2\) Boolean label-comparison queries. Littlestone dimension is the maximum depth of a complete binary query tree in which each root-to-leaf sequence of answers is realized by at least one single concept. The table is asserted only through \(n=8\); the static identity is valid for every \(n\).

## Proof
**1. Symmetry reduction.** Reversing one-line position order flips every pairwise-comparison answer. Complementing all permutation values, \(j\mapsto n+1-j\), permutes/reverses the pair-query labels. Both operations preserve VC and Littlestone dimensions. Under these operations the six forbidden patterns split into two orbits: \(\{123,321\}\) and \(\{132,213,231,312\}\). It therefore suffices to calculate adaptive dimensions for \(123\) and \(132\).

**2. VC upper bound for every \(n\).** A support of comparison queries corresponds to a simple graph on the \(n\) labels. If that graph contains a cycle, assigning comparison outcomes that orient that cycle consistently around itself cannot be realized by any total order. A shattered support must therefore be a forest, of size at most \(n-1\).

**3. VC lower bound for both orbit representatives, for every \(n\).** Query the \(n-1\) pairs \(\{1,j\}\), \(2\le j\le n\), and prescribe independently which symbols occur before \(1\). Write the prescribed before-set as \(B\), its complement in \(\{2,\dots,n\}\) as \(A\). For forbidden pattern \(123\), the permutation \(B\) in decreasing order, followed by \(1\), followed by \(A\) in decreasing order avoids \(123\), because its three blocks are decreasing and \(1\) cannot be the middle value of an increasing triple. For forbidden pattern \(132\), use \(B\) in decreasing order, \(1\), and \(A\) in increasing order. Here no \(132\) pattern can lie entirely in a monotone block; its first member cannot be followed by a later descent in the increasing right block, and \(1\) cannot be the first member of a \(132\) pattern because the right block is increasing. In either case every choice of \(B\) is realized. Symmetry gives all six patterns and the equality \(\operatorname{VCdim}=n-1\).

**4. Exact finite Littlestone computation.** For each of the two representatives and each \(3\le n\le8\), the supplied programs enumerate **all** \(n!\) permutations, reject precisely those having a forbidden length-three subsequence, and produce the \(\binom n2\) full-column Boolean incidence vectors for the remaining permutations. Their class sizes match the Catalan numbers \(5,14,42,132,429,1430\).

For an actual nonempty subset \(B\) of these concepts let \(F(B,d)\) mean that \(B\) shatters a complete depth-\(d\) tree, with \(F(B,0)=\mathrm{true}\). For \(d\ge1\), the exact recurrence is
\[
F(B,d)\quad\Longleftrightarrow\quad
\bigvee_{q}\Bigl(F(B_{q=0},d-1)\ \land\ F(B_{q=1},d-1)\Bigr).
\]
Any branch containing fewer than \(2^{d-1}\) concepts fails its depth-\(d-1\) requirement, and any \(B\) with fewer than \(2^d\) concepts fails immediately. These are sound pruning conditions, not heuristic approximations. The verifier uses memoization of actual subsets of the explicitly enumerated class; every possible first query is tried if necessary. Induction on \(d\) proves its answer is exactly correct, including the negative answers proving the upper bounds.

For each calculated dimension \(d\), the package also contains a complete depth-\(d\) binary tree with a concrete avoiding permutation attached to **every leaf**. In a separate verifier the original permutations and query columns are regenerated; the verifier checks all root-to-leaf constraints, all \(2^d\) distinct leaf witnesses, and nonexistence of a tree of depth \(d+1\). Across the twelve nontrivial representative cases this verifies 1,596 internal nodes, 1,608 distinct-at-each-tree leaf witnesses, and 32,941 visited upper-search states. In particular, the negative depth-ten test for the \(132\)-avoiding eight-symbol class examines 31,849 distinct recursion states. The upper-bound program is exhaustive over its finite domain and the positive trees are independent certificates. This proves all entries through eight; no numerical extrapolation is used.

For \(n=1\) there is one concept, hence dimension zero; for \(n=2\) every length-three pattern is vacuously avoided, and the unique pair query shatters depth one.

## Verification
Using Python 3 with no external packages, place `compute_dimensions.py`, `verify_certificates.py`, and `SHATTERING_TREES.json` in one directory and execute `python3 verify_certificates.py`. Its final line is `PATTERN_CLASS_WITNESS_CHECKS_PASS 12 1596 1608 32941`; its full output is supplied as `verification_output.txt`. Running `python3 compute_dimensions.py` deterministically regenerates the witness-tree JSON and its source-search checks. `generation_output.txt` records the generator's output. Leaf numbers refer to the zero-indexed lexicographic list of the avoiding permutations, as regenerated by the verifier. The verification code checks the complete trees and independently recomputes the upper-depth decision, rather than trusting their asserted dimensions.

## Relationship to prior work
Classical Catalan enumeration and Wilf equivalence for avoidance of a single length-three pattern are established background, explicitly stated for all six patterns in Janson's 2017 paper. Cerbai, Claesson, Ferrari, and Steingrímsson (2020) study *stack-sortable* permutations for a \(132\)-restricted machine and related pattern classes; this is a different object and contains no pairwise-comparison online-shattering dimension theorem. Chase, Freitag, and Reyzin (2023) develop general applications of Littlestone dimension to query learning and compression; their generic results do not instantiate this exact pattern-dependent comparison class. An accessible published finite census of fixed points, excedances, and descents on \(123\)-avoiders through ten symbols concerns statistics on the same set, not adaptive label comparisons, and does not supply the tree dimensions. A preceding exact dimension result for **all** unrestricted total orders and its VC forest condition are stronger in object inclusion but give only bounds for these avoidance subclasses, not the sharp values or the Wilf-equivalent contrast.

## Limitations
The adaptive classification is exhaustive only for \(n\le8\), not an asymptotic claim. A general formula beyond that range is neither proved nor asserted. The static formula is an unrestricted proof and does not depend on finite tests. Historical-priority assessment is based on accessible comparisons, not an exhaustive proof of novelty; older work on learning sorting/stack-sortable rankings or special permutation classes might contain an equivalent special case. The quoted source literature supplies background and motivation; it is not represented as an external independent certification of these new exact values.

## References
1. Svante Janson, *Patterns in random permutations avoiding the pattern 321*, arXiv:1709.08427, first posted 2017-09-25, especially Section 1 and Catalan formula (1.3).
2. Giulio Cerbai, Anders Claesson, Luca Ferrari, Einar Steingrímsson, *Sorting with pattern-avoiding stacks: the 132-machine*, arXiv:2006.05692, first posted 2020-06-10, especially Sections 1, 3, and 4.
3. Hunter Chase, James Freitag, Lev Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812, first posted 2023-10-07, especially Sections 1 and 2.
4. Aïssatou Diallo, Markus Zopf, Johannes Fürnkranz, *Permutation Learning via Lehmer Codes*, DOI:10.3233/FAIA200206, first published online 2020-09-18 (abstract and publisher metadata consulted).
