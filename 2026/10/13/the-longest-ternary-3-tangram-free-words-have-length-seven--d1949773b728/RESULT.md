# The longest ternary 3-tangram-free words have length seven
## Finding
A word is \(3\)-tangram-free when none of its factors has cut number at most \(3\). Over a ternary alphabet, every \(3\)-tangram-free word has length at most \(7\), and this bound is sharp.

More precisely, the numbers of labeled ternary \(3\)-tangram-free words of lengths \(1\) through \(8\) are
\[
3,\ 6,\ 12,\ 18,\ 30,\ 24,\ 18,\ 0.
\]
Hence exactly \(18\) labeled words attain the maximum length \(7\).

Under arbitrary permutations of the three alphabet symbols together with reversal, these \(18\) words form exactly three orbits, each of size \(6\). Representatives are
\[
\mathtt{0102010},\qquad
\mathtt{0102101},\qquad
\mathtt{0121012}.
\]
Equivalently, every ternary word of length \(8\) contains a factor whose cut number is at most \(3\).

## Assumptions and scope
A tangram is a finite word in which every letter occurs an even number of times. Following Dębski, Grytczuk, Pawlik, Przybyło, and Śleszyńska-Nowak, the cut number \(\mu(T)\) of a tangram \(T\) is the least \(k\ge1\) for which
\[
T=F_1F_2\cdots F_{k+1}
\]
with all \(F_i\) nonempty, and for some permutation \(\sigma\) and some \(1\le j\le k\),
\[
F_{\sigma(1)}\cdots F_{\sigma(j)}
=
F_{\sigma(j+1)}\cdots F_{\sigma(k+1)}.
\]
For a nontangram, \(\mu(T)=\infty\).

The claim concerns finite ternary words and the threshold \(k=3\). It does not determine whether the infinite-word alphabet parameter \(t(3)\) equals \(4\) or \(5\).

## Proof
The proof is an exhaustive finite classification directly from the cut-number definition.

For a candidate factor \(T\), and each \(k\in\{1,2,3\}\), enumerate every choice of \(k\) internal cut positions. This produces \(k+1\) nonempty pieces. Enumerate every permutation of those pieces and every split between successive permuted pieces. The factor has cut number at most \(3\) exactly when one such split gives identical concatenations on its two sides.

A ternary word is accepted precisely when this test fails for every factor. Direct enumeration of all ternary words through length \(8\) gives
\[
3,\ 6,\ 12,\ 18,\ 30,\ 24,\ 18,\ 0
\]
accepted words at successive lengths.

Completeness is independently checked by an incremental enumeration. Starting from the empty word, append one of the three symbols. Since the previous prefix is already \(3\)-tangram-free, the only new forbidden factors are suffixes ending at the newly appended position. Testing exactly those suffixes reproduces the same complete set at every length through \(8\).

The absence of any accepted word at length \(8\) proves the upper bound \(7\). The \(18\) accepted words at length \(7\) prove sharpness and give the complete equality layer.

For the symmetry classification, apply all six alphabet permutations and reversal to each of the \(18\) maximizers and canonicalize by the lexicographically least resulting word. This gives exactly three orbits, represented by the three words in the finding, each with six labeled members.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier uses two independent cut-number predicates. One implements cuts, piece permutations, and equality across a piece-boundary split literally. The other asks whether a permutation of two, three, or four pieces forms a square whose midpoint lies on a piece boundary. The predicates agree on every ternary word of length at most \(8\).

It then compares a full brute-force census of all \(3^n\) words for \(1\le n\le8\) with an independent incremental suffix-checking census. The complete accepted sets agree, including all \(18\) length-\(7\) maximizers and the empty length-\(8\) layer. Finally, it recomputes the three symmetry orbits.

## Relationship to prior work
Dębski, Grytczuk, Pawlik, Przybyło, and Śleszyńska-Nowak introduced the cut-number avoidance problem and the function \(t(k)\). They prove that every ternary word of length \(8\) contains a tangram, without requiring that its cut number be at most \(3\). For \(k=3\), their Proposition 2 proves only that every sufficiently long ternary word contains a tangram of cut number at most \(3\), yielding \(4\le t(3)\le5\).

Their proof of that lower bound proceeds through unavoidable short palindromes and low-cut extensions, but it does not state the sharp finite cutoff \(8\), the complete count of \(18\) length-\(7\) extremizers, or their three symmetry classes. The paper explicitly leaves determination of \(t(3)\) as an open problem.

The present result sharpens only the ternary finite obstruction: it shows that the vague “sufficiently long” threshold can be replaced by length \(8\), and classifies every maximum avoiding word. It does not resolve the quaternary-versus-five-letter infinite avoidance problem.

## Limitations
This is a complete finite ternary classification for cut number at most \(3\). It gives no construction of arbitrarily long quaternary \(3\)-tangram-free words and therefore does not settle \(t(3)\).

The exhaustive method is intended for the first unresolved low-cut case and is not claimed to scale efficiently to larger alphabets or larger cut thresholds.

An unindexed computational note could contain the same finite cutoff or equality-layer census even though the inspected primary publication and targeted searches do not report it.

## References
1. M. Dębski, J. Grytczuk, B. Pawlik, J. Przybyło, and M. Śleszyńska-Nowak, “Words Avoiding Tangrams,” arXiv:2407.03819v1, first public version 2024-07-04; Annals of Combinatorics 29 (2025), 905–920, DOI 10.1007/s00026-024-00736-9.
