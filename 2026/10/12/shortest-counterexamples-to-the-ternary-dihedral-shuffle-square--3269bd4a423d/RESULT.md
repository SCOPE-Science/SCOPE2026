# Shortest counterexamples to the ternary dihedral shuffle-square conjecture
## Finding
A conjecture of Grytczuk, Pawlik, and Pleszczyński states that every even ternary word is a dihedral shuffle square. The conjecture is false.

The shortest counterexamples have length \(8\). Exactly \(48\) labeled even ternary words of length \(8\) fail to be dihedral shuffle squares. Under permutations of the alphabet together with reversal, these \(48\) words form four classes of size \(12\), represented by

`00011022`, `00110220`, `00111221`, and `01112210`.

In particular, `00011022` is a counterexample.

## Assumptions and scope
An even word is a word in which every symbol occurs an even number of times. A shuffle split of a length-\(2n\) word is a partition of its positions into two sets of size \(n\); reading each set in increasing position order gives subwords \(U\) and \(V\).

For a word \(x=x_1\cdots x_n\), its \(D_n\)-orbit consists of the rotations of \(x\) and the rotations of its reversal. A dihedral shuffle square is a word admitting a shuffle split whose two subwords lie in the same \(D_n\)-orbit.

The classification here is only for the shortest failing length. It makes no claim about the number or structure of counterexamples at larger lengths.

## Proof
Consider
\[
W=\mathtt{00011022}.
\]
Any shuffle split that could possibly be dihedral must give the two subwords the same multiset of letters. Since \(W\) has four \(0\)'s, two \(1\)'s, and two \(2\)'s, each subword must have multiset \(\{0,0,1,2\}\).

The fourth zero is at position \(6\). Whichever half contains this zero must also contain one earlier zero, one of the \(1\)'s at positions \(4,5\), and one of the \(2\)'s at positions \(7,8\). Read in increasing position order, that half is therefore `0102`. The complementary half uses two of the first three zeros, the other \(1\), and the other \(2\), and is therefore `0012`. Thus every balanced split gives, up to order, exactly the pair
\[
\{\mathtt{0012},\mathtt{0102}\}.
\]

The \(D_4\)-orbit of `0012` is
\[
\{\mathtt{0012},\mathtt{0120},\mathtt{1200},\mathtt{2001},
\mathtt{2100},\mathtt{1002},\mathtt{0021},\mathtt{0210}\}.
\]
It does not contain `0102`. Hence \(W\) is not a dihedral shuffle square.

It remains to show that length \(8\) is minimal. Length \(2\) is immediate. An even ternary word of length \(4\) uses at most two symbols, so after renaming symbols it is an even binary word. The published binary theorem says that every even binary word is a cyclic shuffle square, and every cyclic permutation belongs to the corresponding dihedral group. Hence length \(4\) cannot fail.

For length \(6\), distribute half of the occurrences of each symbol to each side of a shuffle split. This is possible because every multiplicity is even. The resulting subwords have length \(3\) and equal multisets. Any two length-\(3\) words with equal multisets are related by a permutation of their three positions, and
\[
D_3=S_3.
\]
Thus every even ternary word of length \(6\) is a dihedral shuffle square.

Therefore the first possible failing length is \(8\), and `00011022` proves that it occurs.

For completeness, the exact length-\(8\) classification is obtained by enumerating all \(1641\) labeled even ternary words. For each word, all \(\binom84=70\) position splits are tested and the two subwords are compared under the eight elements of \(D_4\). Exactly \(48\) words fail. Canonicalizing these failures under the six alphabet permutations and reversal gives precisely four classes, each of size \(12\), with the representatives listed above.

## Verification
The bundled `verify.py` regenerates every even ternary word at lengths \(2,4,6,8\), checks every equal-size position split against the corresponding dihedral orbit, and obtains
\[
3,21,183,1641
\]
even words at those lengths and
\[
0,0,0,48
\]
failures.

It then independently recomputes the four symmetry classes at length \(8\), checks their sizes, and verifies the structural certificate for `00011022`: there are \(24\) oriented balanced splits and every one gives the same unordered pair `0012`/`0102`.

The finite enumeration is exhaustive over the stated finite domains. Minimality below length \(8\) also has the direct proof above, so it does not rely only on computation.

## Relationship to prior work
Grytczuk, Pawlik, and Pleszczyński introduced the permutation-based generalized shuffle-square framework, proved that every even binary word is a cyclic shuffle square, observed that cyclic permutations no longer suffice over a ternary alphabet, and explicitly conjectured that dihedral permutations do suffice for every even ternary word. The present result directly refutes that conjecture at the first possible length.

A later paper by the same authors, *More Variations on Shuffle Squares*, develops a broader constraint-graph framework and cutting-distance conjectures. Its stated conjectures are different: they concern bounded cutting and rearrangement, not the assertion that the two shuffled halves are related by one dihedral permutation. Thus those results do not imply or preclude the counterexample above.

Targeted searches using the exact counterexample, the conjecture wording, “dihedral shuffle square”, “ternary”, “length 8”, and “counterexample” did not locate a published statement of this refutation or this shortest-length classification. The current arXiv text of the original paper still states the conjecture.

## Limitations
The exhaustive classification is restricted to length \(8\). It does not enumerate longer counterexamples or determine their asymptotic density.

A literature search cannot exclude an unindexed note, unpublished computation, or differently phrased observation. The mathematical counterexample itself is independent of that residual originality risk.

## References
1. J. Grytczuk, B. Pawlik, and M. Pleszczyński, “Variations on shuffle squares,” arXiv:2308.13882, first public version 2023-08-26, MSC 68R15.
2. J. Grytczuk, B. Pawlik, and M. Pleszczyński, “More Variations on Shuffle Squares,” *Symmetry* 15 (2023), 1982, DOI 10.3390/sym15111982.
