# Exactly 102 rank-three theories of finite direct sums of at most three chains

## Finding
Let \(C_n\) denote a nonempty strict finite linear order of cardinality \(n\). For \(1\le k\le3\) and positive integers \(n_1,\ldots,n_k\), let
\[
P(n_1,\ldots,n_k)=C_{n_1}\mathbin{\sqcup}\cdots\mathbin{\sqcup}C_{n_k},
\]
where elements in different chains are incomparable. Work in first-order logic with equality and a **single strict order relation** \(<\), without constants or predicates naming the components. Write \(P\equiv_3 Q\) when the posets agree on every sentence of quantifier rank at most three.

**Theorem.** Among all nonempty finite direct sums of one, two, or three nonempty chains, there are exactly \(102\) distinct rank-three theories: \(7\) for one component, \(27\) for two, and \(68\) for three. Every poset in this family has a rank-three-equivalent representative on at most \(19\) vertices, and \(19\) is optimal within this family.

Here is a complete, finite decision rule. Replace every component length \(n\) by \(\min(n,7)\), and sort the resulting lengths into a nondecreasing tuple. Tuples of different lengths \(k\) are inequivalent. Within a fixed \(k\), two normalized tuples are equivalent if they are equal or belong to the same displayed merger group; no other mergers occur.

For two components the sole merger is
\[
(6,7)\sim(7,7).
\]
For three components the full merger table is:

| | Equivalent normalized triples |
|---|---|
| 1 | \((1,6,7)\sim(1,7,7)\) |
| 2 | \((2,6,7)\sim(2,7,7)\) |
| 3 | \((3,3,4)\sim(3,4,4)\) |
| 4 | \((3,3,5)\sim(3,5,5)\) |
| 5 | \((3,3,6)\sim(3,6,6)\) |
| 6 | \((3,3,7)\sim(3,6,7)\sim(3,7,7)\) |
| 7 | \((4,4,5)\sim(4,5,5)\) |
| 8 | \((4,4,6)\sim(4,6,6)\) |
| 9 | \((4,4,7)\sim(4,6,7)\sim(4,7,7)\) |
| 10 | \((5,5,6)\sim(5,6,6)\) |
| 11 | \((5,5,7)\sim(5,6,7)\sim(5,7,7)\) |
| 12 | \((6,6,7)\sim(6,7,7)\sim(7,7,7)\) |

The extremal classes have smallest representatives \(C_6\sqcup C_7\), of size \(13\), and \(C_6\sqcup C_6\sqcup C_7\), of size \(19\), for two and three components respectively. The one-component extremal representative is \(C_7\).

## Assumptions and scope
Every component is nonempty, has a finite positive cardinality, and carries its full transitive strict order (not merely the cover or successor relation). There are no order relations between distinct components. The number of components is one, two, or three; it is not externally named. All comparisons concern ordinary first-order quantifier rank, not counting logic, bounded-variable logic, or formulas with added component predicates. The empty poset and direct sums with four or more components are excluded.

## Proof
**1. Reduction to a finite parameter set.** The classical finite-linear-order Ehrenfeucht–Fraïssé theorem states that two nonempty chains are equivalent in three rounds precisely when their cardinalities are the same below seven, or both are at least seven. A direct induction proves the cutoff: with \(r\) moves remaining, corresponding unpebbled intervals have equal lengths below \(2^r-1\), or both have lengths at least \(2^r-1\). A move into a large interval can be met by a move leaving corresponding gaps equal when small and otherwise above the cutoff \(2^{r-1}-1\). The inequality \(2^r-1=2(2^{r-1}-1)+1\) ensures this is possible. With zero moves remaining, the pebbled order relations agree.

If each chain of one direct sum is matched with a three-round-equivalent chain of another sum, Duplicator combines the separate strategies: a move in a given chain is answered in its matched chain. Because any pair of points in different components is incomparable on both sides, the union strategy is a partial isomorphism after every move. Consequently, truncating each component length at seven preserves the rank-three theory. Sorting is valid because components are unnamed and interchangeable.

**2. Different component counts are distinct.** For \(j=2,3\), the sentence asserting the existence of \(j\) pairwise incomparable distinct elements has quantifier rank \(j\). It holds in a direct sum of \(k\) nonempty chains exactly when \(k\ge j\). Thus the component-count strata \(k=1,2,3\) have disjoint rank-three theories.

**3. Exact finite equivalence test.** For a finite structure \(A\), an ordered tuple \(\bar a\) and integer \(r\ge0\), define the canonical logical signature recursively:
\[
H_0^A(\bar a)=\operatorname{at}_A(\bar a),\qquad
H_{r+1}^A(\bar a)=\bigl(\operatorname{at}_A(\bar a),\{H_r^A(\bar a,b):b\in A\}\bigr).
\]
The atomic diagram \(\operatorname{at}_A\) records, for every ordered pair of tuple positions, precisely one of equality, strict less, strict greater, or incomparability. For the empty tuple its atomic diagram is empty. By induction on \(r\), equality of signatures for corresponding tuples is equivalent to a winning Duplicator strategy in the \(r\)-round game with those tuples already matched. The successor step follows because Spoiler may choose an element on either side, and the set of next-level signatures records all possible replies. This gives an exact—not heuristic—decision procedure: \(A\equiv_3 B\) if and only if \(H_3^A(())=H_3^B(())\).

The included executable `verify.py` enumerates **all** sorted tuples from \(\{1,\ldots,7\}^k\) for each \(k=1,2,3\), namely \(7\), \(28\), and \(84\) tuples. It computes these full recursive signatures and separately computes the equivalent three-layer signatures by directly assembling all atomic diagrams of ordered triples. The resulting partitions coincide exactly. The sole two-chain merger and twelve three-chain merger groups are listed above, and no other pairs share a signature. Hence the class counts are \(7\), \(28-1=27\), and \(84-16=68\), giving \(102\) in all.

**4. Sharp representative bounds.** In any signature class, the smallest canonical capped tuple has the least possible number of vertices: an uncapped representative has at least as many vertices as its capped tuple, and the finite class table lists all capped tuples in that theory. Taking the minimum sum of the tuple entries across each of the \(102\) signature classes gives maximal minima \(7\), \(13\), and \(19\) in the one-, two-, and three-component strata. The unique extremal capped classes have least members \((7)\), \((6,7)\), and \((6,6,7)\). Thus \(19\) is both sufficient and necessary within this family.

## Verification
Run `python3 verify.py` in the directory containing the included files. It uses only the Python standard library. The program computes two separately written versions of the exact three-round signature for every one of the \(119\) capped posets, asserts equality of the two resulting partitions, prints the complete nontrivial merger groups, and checks the sharp minima. It also performs ten supplementary boundary tests using chain lengths eight or nine. The saved output is `verify_output.txt`; its terminal status is `VERIFY_OK`. The merger-table SHA-256 in that output is a reproducibility checksum, not a substitute for the signature proof. The boundary samples are corroborative only; infinitude is handled by the preceding truncation argument.

## Relationship to prior work
Mwesigye and Truss develop finite coloured-chain equivalence and the recursive character approach. Their monochromatic chain cutoff supplies the reduction to component lengths at most seven, but their results concern a **single total order** and do not identify the exceptional mergers or the \(102\)-class spectrum for disjoint partial orders. General Feferman–Vaught disjoint-sum principles similarly explain why the reduction is reasonable but do not give this exact spectrum; naively retaining componentwise truncated lengths leaves \(119\), rather than \(102\), parameter patterns.

Abdi studies *siblings* (mutually embeddable direct sums of chains), an equivalence different from bounded-rank first-order equivalence. In particular, the merger \((6,7)\sim(7,7)\) is not an isomorphism or a sibling classification statement. Siders treats quantifier-rank equivalence of linear orders; full text was not available for this comparison, so hidden broader coverage remains a priority risk.

## Limitations
The classification is restricted to at most three nonempty components and exactly three rounds in the pure strict-order language. It does not provide a classification at rank four or with an unbounded number of components. The complete finite recursion has been checked reproducibly, but the result has not undergone independent mathematical review. The originality search cannot rule out equivalent statements in unindexed or inaccessible historical work.

## References
1. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, Order 28 (2011), 387–397; first published online 7 September 2010. DOI: 10.1007/s11083-010-9178-9.
2. R. Siders, *On quantifier-rank equivalence between linear orders*, Information and Computation 208 (2010), 417–432. DOI: 10.1016/j.ic.2009.11.006.
3. D. Abdi, *Siblings of Direct Sums of Chains*, arXiv:2209.03477 (first submitted 2022; revised 2025).
