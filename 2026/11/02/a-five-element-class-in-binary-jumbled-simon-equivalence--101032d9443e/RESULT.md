# A five-element class in binary jumbled Simon equivalence

## Finding
Fix the alphabet \(\Sigma=\{0,1\}\). Under the jumbled Simon equivalence relation \(\sim^J_{4,1}\) of Fleischmann, Huch, Kammholz, and Koß, the complete equivalence class of the word \(\mathtt{00110}\), among **all finite binary words of any length**, is
\[
[\mathtt{00110}]^J_{4,1}
=\{\mathtt{00110},\mathtt{01001},\mathtt{01010},\mathtt{01100},\mathtt{10010}\}.
\]
In particular, its cardinality is \(5\), strictly between a singleton and the \(\binom52=10\) anagrams of the representative. The ten binary words containing three zeros and two ones comprise exactly six classes for this relation: one class of size five and five singleton classes. This exhibits a finite equivalence-class cardinality not among the three example types (singleton, complete anagram class, infinite) described in the source paper, answering its explicit existence question.

## Assumptions and scope
For a finite binary word \(w\), a target word \(u\) of length \(t\) is *one-jumbled* in \(w\) when (i) each symbol multiplicity of \(u\) is bounded by the corresponding multiplicity in \(w\), and (ii) some subsequence of \(u\) of length at least \(t-1\) is a subsequence of \(w\). Let \(J_t(w)\) be the set of such targets of length \(t\). Two finite words are \(\sim^J_{4,1}\)-equivalent precisely when \(J_t\) agrees for all \(0\le t\le4\), including the empty target at \(t=0\). These are the source paper's jumbled scattered-factor definitions specialized to one jumble; the proof below uses them directly, without assuming its class-size conclusions. Multiplicities and subsequences are not contiguous-factor counts.

## Proof
Let \(w=\mathtt{00110}\). Directly by the subsequence definition, its set of length-four targets is
\[
J_4(w)=T=\{\mathtt{0001},\mathtt{0010},\mathtt{0100},\mathtt{1000},
\mathtt{0011},\mathtt{0101},\mathtt{0110},\mathtt{1001},\mathtt{1010},\mathtt{1100}\}.
\]
All ten targets are one-jumbled: a target with three zeros shares \(\mathtt{000}\) with \(w\); each of the six targets with two zeros and two ones shares a length-three subsequence with \(w\), as verified by selecting three of its four positions. No other length-four target satisfies the multiplicity restriction.

**Global class restriction.** Suppose an arbitrary binary word \(v\) satisfies \(J_4(v)=T\). Because \(\mathtt{0001}\in T\), \(v\) has at least three zeros and one one. Because \(\mathtt{0011}\in T\), it has at least two ones. Because \(\mathtt{0000}\notin T\), it has at most three zeros: with four zeros this target would already be an ordinary subsequence. Finally \(\mathtt{0111}\notin T\) forces at most two ones: if \(v\) contained three ones, then \(\mathtt{111}\) would be a common subsequence of length three between \(\mathtt{0111}\) and \(v\), and its required zero would also be available. Thus \(v\) contains **exactly three zeros and two ones**, regardless of its initially unknown length. There are precisely ten such words.

**Complete finite comparison.** For each of those ten words the table lists the targets in \(T\) *not* one-jumbled in the word. The four targets with three zeros always belong to \(J_4\), because each shares \(\mathtt{000}\). For the other six, inspect the four possible length-three subsequences of each target and the ten possible length-three position choices in the source. This yields the following exhaustive table, reproducible by the attached independent checker.

| Source word | Missing targets from \(T\) |
|---|---|
| `00011` | `1010`, `1100` |
| `00101` | `1100` |
| `00110` | none |
| `01001` | none |
| `01010` | none |
| `01100` | none |
| `10001` | `0110` |
| `10010` | none |
| `10100` | `0011` |
| `11000` | `0011`, `0101` |

Exactly the five words asserted in the finding have \(J_4=T\). The other five have distinct missing-target sets. For **every** representative in the ten-word table, \(\mathtt{0001}\) is present and at least one target with two ones is present, while \(\mathtt{0000}\) and \(\mathtt{0111}\) are absent. Repeating the preceding four-pattern multiplicity argument (using whichever two-one target is present) forces any globally equivalent word to have the same composition \((3,2)\). Hence these five are genuine global singleton classes, and the six-class partition is exhaustive.

**Shorter layers.** Every word with exactly three zeros and two ones has the same one-jumbled targets in lengths below four. At length one both symbols occur; at length two, all four targets are admitted since each needs to match only one available letter. At length three, exactly the seven words other than \(\mathtt{111}\) satisfy the multiplicity restriction, and every admissible target contains \(\mathtt{00}\) or \(\mathtt{11}\) as a subsequence by pigeonhole; both pairs are present as subsequences of every such source word. The empty target also agrees. Thus equality of \(J_4\) among these ten words is equivalent to equality of the complete profile \(J_{\le4}\). Combined with the global class restriction, this proves the exact five-element class.

## Verification
The standalone file `check.py` constructs the one-jumbled target sets by directly enumerating all choices of three positions in each four-symbol target and testing the resulting subsequences. It independently computes longest-common-subsequence lengths by dynamic programming and confirms agreement for each candidate. It checks every binary source word of length up to ten for spurious class members, and separately checks the three shorter nonempty profile layers. `check_output.txt` contains the actual replay output. The proof of the global restriction is mathematical, not an extrapolation from the finite-length check.

## Relationship to prior work
Fleischmann, Huch, Kammholz, and Koß (2025) introduce jumbled Simon equivalence. Their Section 4 gives singleton, complete-anagram, and infinite class examples and explicitly leaves other class cardinalities open. Their special case at the maximal jumble allowance \(\ell=k-1\) does not determine the present \((k,\ell)=(4,1)\) class; nor do their class-structure propositions imply the five-element spectrum. The older \(k\)-abelian equivalence literature compares **contiguous factor frequencies**, a different relation, and does not imply this statement. No result of publication-priority completeness is asserted from search absence alone.

## Limitations
The finding establishes a complete finite class and a positive answer to the existence question, not a classification of all jumbled Simon equivalence classes or their possible cardinalities for arbitrary parameters. The published-source priority comparison is not independently certified. The attached verification code is a finite check, and the global assertion depends on the explicit multiplicity argument above.

## References
1. Pamela Fleischmann, Annika Huch, Melf Kammholz, Tore Koß, *Jumbled Scattered Factors*, arXiv:2506.03814, first posted June 4, 2025. https://arxiv.org/abs/2506.03814 ; especially Definitions 4 and 7 and Section 4.
2. Juhani Karhumäki, Svetlana Puzynina, Michaël Rao, Markus A. Whiteland, *On cardinalities of \(k\)-abelian equivalence classes*, Theoretical Computer Science 658 (2017), 190–204. https://doi.org/10.1016/j.tcs.2016.06.010 (different equivalence relation).
