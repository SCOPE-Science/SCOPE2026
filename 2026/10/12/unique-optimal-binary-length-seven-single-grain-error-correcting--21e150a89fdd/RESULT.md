# Unique optimal binary length-seven single-grain-error-correcting code
## Finding
Consider the binary single-grain channel of length \(7\), in which a received word may equal the transmitted word or may result from overwriting one coordinate by the immediately preceding coordinate. Then the classical optimal cardinality \(M(7,1)=26\) has **exactly one labeled optimal code**.

For an ordered six-bit string, define the following explicitly enumerated \(13\)-word set:
\[
\begin{aligned}
T=\{&000000,110000,011000,100100,101010,001110,111110,\\
&010101,101101,000011,110011,011011,100111\}.
\end{aligned}
\]
Write \(\bar x\) for the coordinatewise binary complement of the entire seven-bit word \(x\). Then the unique maximum code is
\[
C_* = \{0u:u\in T\}\ \cup\ \{\overline{0u}:u\in T\}.
\]
It has exactly \(26\) words, is fixed by global bit complementation, and every other grain-error-correcting code of cardinality \(26\) is literally equal to \(C_*\), without any coordinate or symbol relabeling.

## Assumptions and scope
Index the physical coordinates from \(0\) to \(6\), in the displayed left-to-right order. For \(x\in\{0,1\}^7\), its one-grain error ball is
\[
B(x)=\{x\}\cup\{x^{(i)}:1\le i\le6\},
\]
where \(x^{(i)}\) agrees with \(x\) except at position \(i\), which becomes the original preceding bit \(x_{i-1}\). Repeated outputs are identified. Two distinct codewords are compatible exactly when their \(B\)-sets are disjoint. This is the single-error case of the overlapping/non-overlapping grain model; these variants agree for a single grain. The channel never changes coordinate \(0\).

The claim is for arbitrary binary subsets, with no linearity assumption. Labeled uniqueness refers to the fixed physical coordinate order, not uniqueness merely up to equivalence.

## Proof
Because no allowed overwrite changes coordinate \(0\), every code \(C\) splits into independent branches \(C_0\) and \(C_1\) with first bit \(0\) or \(1\). There can be no confusable pair across the branches. Global binary complementation preserves the channel and bijects the branches, so the two branch maxima have equal cardinality and equal numbers of optimal subsets.

Fix the branch with first bit \(0\). It consists of \(2^6=64\) words. For each branch word, generate its complete error ball directly from the overwrite definition. Form the graph whose two distinct vertices are adjacent exactly when their error balls are disjoint. An admissible branch code is precisely a clique in this graph.

A complete pivoted Bron--Kerbosch recursion, with only the safe prune \(|R|+|P|<13\), produces **exactly one maximal clique of size at least \(13\)**. This clique has size \(13\) and is exactly \(\{0u:u\in T\}\). The verifier independently reconstructs the branch graph from the bit-flip-at-a-transition characterization of an error. It also runs a separate increasing-vertex, fixed-size clique enumerator whose pruning bound comes from an explicit proper greedy coloring of every candidate-induced subgraph. This independent search finds precisely one \(13\)-clique and no \(14\)-clique. Its coloring bound is valid because a clique can contain at most one vertex from each independent color class.

Thus each branch contains at most \(13\) compatible words, and equality requires its unique \(13\)-subset. The unique optimum in the first-bit-\(1\) branch is the bitwise complement of the unique first-bit-\(0\) optimum. Consequently \(|C|\le13+13=26\), equality is attained by \(C_*\), and there is exactly one labeled equality case.

The verifier also rechecks the actual \(26\)-word set directly against every pair of channel balls, so neither the clique search nor the complement argument is used as a substitute for checking the exhibited code.

## Verification
Run `python3 verify.py` in the directory containing this file. The verifier uses only the Python standard library, reconstructs all \(128\) channel words and their error balls, checks two independent ball formulations, and recomputes all claims. The first-bit-zero graph has exactly \(432\) forbidden edges and \(1584\) compatibility edges; both independent clique searches find its unique size-\(13\) maximum.

The terminal line must be:

`VERIFY_OK maximum=26 labeled_maxima=1 branch_maximum=13 branch_maxima=1 complementary_halves=true`

The recursions are finite complete searches with mathematically valid pruning; their success is not extrapolated beyond the stated length and error radius.

## Relationship to prior work
Sharov and Roth established \(M(7,1)=26\) in their finite parameter table. Their Section IV proves uniqueness for **infinite-grain** correction and for particular higher-error-radius families, but the displayed length-seven **single-grain** cardinality appears as an optimum size, not as a labeled equality-classification theorem. In particular, the uniqueness result at odd length \(n\) for radius \((n-3)/2\) specializes to radius \(2\) when \(n=7\), not to the present radius \(1\).

Gabrys, Yaakobi, and Dolecek state the same transition-dependent single-grain model and tabulate the known size \(26\) at length \(7\), citing Sharov and Roth. Their coding constructions and upper-bound discussion do not state the unique labeled size-\(26\) optimizer. Thus the known numerical optimum is explicitly excluded from the novelty claim; the contribution is the complete uniqueness/equality classification and its forced complementary-half structure.

## Limitations
This is only for binary words of length \(7\) and **at most one** grain overwrite of the form stated above. It does not classify multiple grain errors, nonbinary models, other blocklengths, or variants in which the direction of overwrite may vary. A negative bibliographic search does not prove absolute novelty; obscure finite censuses or supplementary computational tables remain possible residual coverage risks.

## References
1. A. Sharov and R. M. Roth, “Bounds and Constructions for Granular Media Coding,” *IEEE Transactions on Information Theory* **60** (2014), 2010–2027, DOI: 10.1109/TIT.2014.2301811. See Section IV and Table II.
2. R. Gabrys, E. Yaakobi, and L. Dolecek, “Correcting Grain-Errors in Magnetic Media,” arXiv:1307.7087, first submitted 2013-07-26; later *IEEE Transactions on Information Theory* **61** (2015), 2256–2272, DOI: 10.1109/TIT.2015.2409860. See Definition 1 and Table II.
