# A complete census of maximum binary aperiodic orientable words of order \(6\)

## Finding
A finite binary word \(w\) of length \(L\ge6\) is *aperiodic orientable of order \(6\)* if its \(L-5\) consecutive length-\(6\) factors are nonpalindromic, and no two are equal or reverses of one another. Positions and the binary symbols are distinguished (the object is not a necklace).

The greatest possible \(L\) is the **previously known** value \(26\). The complete classification at that length is:

1. Exactly **\(22\)** distinct binary words of length \(26\) satisfy the condition.
2. They form **six** classes under reversal and global bit complementation. Five classes have four words each; one has two.
3. Every length-\(26\) solution starts in \(00000\) and ends in \(11111\), or starts in \(11111\) and ends in \(00000\). Thus, up to global complementation, **all** maximizers are *ideal* in the sense of Mitchell and Wild (2022). There are exactly \(11\) words of each endpoint orientation.

Canonical representatives (the lexicographically smallest word in each orbit), followed by orbit cardinality:

| Canonical representative | Orbit size |
| --- | ---: |
| `00000100110111000101011111` | 4 |
| `00000100111010100011011111` | 2 |
| `00000100111011000101011111` | 4 |
| `00000110100011101010011111` | 4 |
| `00000110100111010100011111` | 4 |
| `00000110101001110100011111` | 4 |

`maximizers.txt` supplies all \(22\) strings, one per line.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\). Consecutive length-\(6\) factors are taken *linearly*, with no wraparound. Reverse means reverse the order of symbols; complement interchanges \(0\) and \(1\). There is no identification by shift, and rotations need not preserve the constraint. The classification concerns all linear words meeting the stated condition, not only words constructed by a specified recursion.

## Proof
A length-\(6\) binary factor corresponds to an edge of the order-\(5\) binary de Bruijn graph: from its first five bits to its last five bits. There are \(64\) candidate edges. Exactly \(8\) (the length-\(6\) palindromes) are forbidden individually. The remaining \(56\) edges form \(28\) two-element reversal orbits. A word is admissible if and only if its edge walk uses no orbit more than once. Indeed, a palindrome conflicts with itself under reversal, and two other factors conflict precisely when they occupy the same reversal orbit.

Index the \(28\) permitted orbits by \(0,\ldots,27\). Let \(v\) be a five-bit suffix (integer \(0\le v<32\)) and \(S\) a set of previously used orbits. Let \(F(v,S)\) be the maximum number of *additional* admissible edges from that state. If the new bit is \(b\in\{0,1\}\), the candidate six-bit edge has integer value \(e=2v+b\), its new five-bit suffix is \(e\bmod32\), and its reversal-orbit index is \(j(e)\), undefined for palindromes. Then the exact recurrence is

\[
F(v,S)=\max\left(\{0\}\cup\left\{1+F(e\bmod32,S\cup\{j(e)\}):b\in\{0,1\},\ j(e)\text{ defined},\ j(e)\notin S\right\}\right).
\]

This recurrence terminates because each nonzero transition increases \(|S|\); the induction base at a state with no usable outgoing edge is \(0\). Every admissible word is represented uniquely by its first five bits and its sequence of appended bits, and conversely every legal recurrence path constructs such a word. The recurrence therefore examines the *entire* finite domain, without a probabilistic or finite-prefix extrapolation.

Evaluating \(F(v,\varnothing)\) on the \(16\) vertices with leading bit \(0\), listed in lexicographic five-bit order, gives:

`21,20,19,19,19,19,18,18,18,17,18,18,19,20,17,1`.

The other \(16\) values agree by bit-complement symmetry. Hence the maximum edge count is \(21\), so \(L=21+5=26\). The exact-optimal transitions are those achieving the displayed recurrence maximum at each step. Traversing only these transitions for every starting five-bit word yields exactly \(22\) maximal strings. Applying the four transformations consisting of reversal and/or complementation partitions this list into the six disjoint orbits in the table, of sizes \(4,2,4,4,4,4\). Directly examining their first and last five bits gives the claimed all-maximizers endpoint property and the \(11+11\) split.

All numerical recurrence evaluations and resulting words are reproduced, rather than trusted as an unshown table, by the complete standard-library program `verify.py`. It contains two mathematically equivalent but differently implemented exact enumerations: a reversal-orbit mask dynamic program and a literal-string search with string-based reversal tests. Their computed *sets* of length-\(26\) maximizers are asserted equal.

## Verification
Run `python3 verify.py` in a directory containing the accompanying file; it requires no packages beyond Python 3. The checker constructs all \(28\) reverse classes, evaluates both algorithms, establishes the global \(21\)-edge maximum and the \(22\)-word solution set, checks six symmetry orbits and their cardinalities, and checks the endpoint classification. It also independently enumerates \(56\), \(108\), and \(22\) valid words at lengths \(6\), \(25\), and \(26\), respectively. The two independent algorithms agree on all length-\(26\) words; these computations constitute an exhaustive finite certificate through the explicit recurrence, not empirical evidence for an infinite-length statement.

## Relationship to prior work
Burns and Mitchell (1992), Section 5.2.2 and Figure 7, already stated the optimal *length* \(26\), based on exhaustive search. Mitchell and Wild (2022), Section 5 and Table 3, repeated the established optimum and, in Definition 5.2, introduced **ideal** aperiodic orientable sequences; their Example 5.6 constructs one of order \(6\). Neither source, in the portions inspected, states the complete \(22\)-word enumeration, the six orbit sizes, or that every maximum word is ideal up to complement. The exact **classification**, not the optimal length or existence of ideal examples, is the contribution here. Gabric and Sawada (2024) primarily treat longer constructions and compare known optimum lengths; their reported constructions do not entail this complete finite census. A published equivalent under different terminology cannot be absolutely excluded.

## Limitations
This is a completely finite statement for binary order \(6\), with an exhaustive computational proof whose correctness depends on inspection and reproducibility of the included finite-state algorithm. It does not assert a similar count, endpoint condition, or maximum at other orders or alphabets. It gives no decoding-complexity improvement. An independent audit has not been performed.

## References
- J. Burns and C. J. Mitchell, *Coding Schemes for Two-Dimensional Position Sensing*, HP Laboratories Technical Report HPL-92-19 (January 1992), esp. Sections 3.2 and 5.2.2, Figure 7. https://www.chrismitchell.net/HPL-92-19.pdf
- C. J. Mitchell and P. R. Wild, *Constructing orientable sequences*, arXiv:2108.03069, first public 6 August 2021; IEEE Transactions on Information Theory 68 (2022), 4782–4789. https://arxiv.org/html/2108.03069v2
- D. Gabrić and J. Sawada, *Construction of orientable sequences in O(1)-amortized time per bit*, arXiv:2401.14341 (2024). https://arxiv.org/abs/2401.14341
- D. Gabrić and J. Sawada, *Efficient Construction of Long Orientable Sequences*, CPM 2024, Article 15. https://doi.org/10.4230/LIPIcs.CPM.2024.15
