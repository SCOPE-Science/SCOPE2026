# Exact binary \(r=2\) length-limited composition reconstruction
## Finding
For a binary word \(x\in\{0,1\}^n\), let \(C_{\le 2}(x)\) be the multiset of compositions of every contiguous substring of length one or two. A composition records only how many zeros and ones occur in the substring, not their order. Let \(R_2(n)\) be the largest size of a length-\(n\) code whose codewords have pairwise distinct \(C_{\le2}\)-multisets.

For every \(n\ge1\),
\[
R_2(2m)=3m^2-2m+2\quad(m\ge1),
\qquad
R_2(2m+1)=3m^2+m+2\quad(m\ge0).
\]
Equivalently, for \(n\ge2\),
\[
R_2(n)-R_2(n-1)=\left\lfloor\frac{3(n-1)}2\right\rfloor.
\]
Thus the exact optimum is \(\frac34 n^2+O(n)\).

There is also a complete ambiguity-class formula. If a nonconstant word has \(z\) zeros, \(o=n-z\) ones, \(r_0\) zero-runs, and \(r_1\) one-runs, then its \(C_{\le2}\)-class has size
\[
2\binom{z-1}{k-1}\binom{o-1}{k-1}
\]
when \(r_0=r_1=k\); it has size
\[
\binom{z-1}{k}\binom{o-1}{k-1}
\]
when \(r_0=k+1\) and \(r_1=k\), with the symmetric formula when \(r_1=r_0+1\). The two constant classes have size one.

Consequently, the individually reconstructible words are exactly the two constant words; for \(n\ge3\), the two palindromes \(0 1^{n-2}0\) and \(1 0^{n-2}1\); and, for odd \(n\ge5\), the two alternating words. At \(n=3\), the alternating words are already the two displayed palindromes.

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\), multiplicities are retained, and only compositions of contiguous substrings of lengths at most two are observed. The model is the \(r\)-length limited composition multiset model with \(r=2\), not an ordered substring-spectrum model: the length-two substrings \(01\) and \(10\) have the same observed composition.

For a word \(x\), write \(z\) and \(o\) for its zero and one counts. Let \(a\) be the number of length-two substrings of composition \(0^2\), let \(b\) be the number of composition \(1^2\), and let \(t\) be the number of mixed length-two compositions \(0^1 1^1\). The length-one part of the observation gives \(z,o\), and the length-two part gives \(a,t,b\).

## Proof
Let \(r_0\) and \(r_1\) be the numbers of zero-runs and one-runs. Every zero-run of length \(L\) contributes \(L-1\) adjacent \(00\) pairs, so
\[
a=z-r_0.
\]
Similarly,
\[
b=o-r_1.
\]
For a nonconstant word, every boundary between consecutive runs contributes exactly one mixed adjacent composition, hence
\[
t=r_0+r_1-1.
\]
Therefore \(C_{\le2}(x)\) determines \((z,r_0,r_1)\). Conversely, an alternating run sequence exists exactly when
\[
1\le r_0\le z,
\qquad
1\le r_1\le o,
\qquad
|r_0-r_1|\le1.
\]
For every such triple, distribute the \(z\) zeros into \(r_0\) positive run lengths and the \(o\) ones into \(r_1\) positive run lengths and alternate the runs. Hence every feasible triple occurs and two nonconstant words have the same observation exactly when they have the same \((z,r_0,r_1)\).

To count observations, separate the possible run-count pairs. If \(r_0=r_1=k\), then \(z\) may range from \(k\) through \(n-k\), giving \(n-2k+1\) signatures. If \(r_0=k+1,r_1=k\), then \(z\) ranges from \(k+1\) through \(n-k\), giving \(n-2k\) signatures; the opposite imbalance contributes the same number. Including the two constant words,
\[
R_2(n)=2+\sum_{k=1}^{\lfloor n/2\rfloor}(n-2k+1)
+2\sum_{k=1}^{\lfloor(n-1)/2\rfloor}(n-2k).
\]
For \(n=2m\), the balanced sum is \(m^2\) and the two imbalanced sums total \(2m(m-1)\), which gives \(3m^2-2m+2\). For \(n=2m+1\), the balanced sum is \(m(m+1)\) and the imbalanced sums total \(2m^2\), which gives \(3m^2+m+2\).

The class-size formulas follow from positive compositions of symbol counts into run lengths. When \(r_0=r_1=k\), either symbol may start, producing the factor two. When \(r_0=k+1,r_1=k\), the word must start and end in zero, so only the two independent positive-composition choices remain. The symmetric case is identical with zeros and ones exchanged.

For singleton classes, the balanced case is never singleton because of the two start-symbol orientations. In the zero-heavy case, the class-size product equals one exactly when all zero-runs have length one and either there is only one one-run or all one-runs also have length one. This gives \(0 1^{n-2}0\) and the odd alternating word; exchanging symbols gives the other two families. Constants are singleton separately.

A maximum code contains one representative from each ambiguity class, so the number of classes is exactly the maximum code size.

## Verification
The accompanying `verify.py` computes the observation literally from all length-one and length-two substrings for every binary word through length \(16\). It independently computes the run-parameter signature, checks that the two induced partitions of \(\{0,1\}^n\) are identical, verifies every class-size formula and every singleton word, and confirms the closed form for the number of classes.

The exhaustive pass examines \(131070\) words and \(1020\) ambiguity classes. A separate arithmetic pass counts feasible run triples and checks the closed forms through \(n=500\). Successful replay ends with `VERIFY_OK words=131070 n=1..16 classes=1020 formulas_n<=500`.

The finite computation is corroborative. The proof above establishes the formulas for all \(n\).

## Relationship to prior work
Ye and Elishco introduced the \(r\)-length limited composition multiset model and defined \(C_{\le r}(x)\). Their treatment gives a Lyndon-word-based code construction and concentrates on the regime in which \(r\) scales with word length; their conclusion explicitly lists constant \(r\) and capacity bounds as further questions. The result here resolves the complete fixed-length extremum and every ambiguity-class size for the first nontrivial constant value \(r=2\).

Acharya, Das, Milenkovic, Orlitsky, and Pan study reconstruction from the full substring-composition multiset, containing all substring lengths. That richer observation does not imply the exact quotient by \(C_{\le2}\). Their work is indexed under combinatorics on words, MSC 68R15, which is also the natural ownership of the present finite-word classification.

The observation here is also strictly coarser than an ordered adjacent-pair multiset: \(01\) and \(10\) are merged into one composition. Results that retain their separate multiplicities therefore do not state the class count or ambiguity sizes proved here.

## Limitations
The theorem is binary and specific to \(r=2\). It does not determine exact maxima for \(r\ge3\), nonbinary alphabets, corrupted composition multisets, or efficient canonical ranking of one representative per ambiguity class. Although targeted searches did not locate a prior statement of the formulas, this base case is elementary enough that an unindexed note, exercise, or unpublished computation remains a residual originality risk.

## References
1. Z. Ye and O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963v1 (2022); later published in IEEE Transactions on Information Theory 70(6), 3922--3940 (2024).
2. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, SIAM Journal on Discrete Mathematics 29(3), 1340--1371 (2015), DOI:10.1137/140962486.
