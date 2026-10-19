# Four shortest unique substrings of finite period-doubling words

## Finding
For each integer \(n\geq3\), define the binary word \(D_n=\varphi^n(0)\), where \(\varphi(0)=01\) and \(\varphi(1)=00\). A factor is *unique* if it has exactly one contiguous occurrence in \(D_n\); different occurrences are counted by starting position.

The least length of a unique factor is exactly
\[
L_n=2^{n-2}+1.
\]
There are exactly four distinct factors of this length occurring uniquely. Using zero-based starting positions, their complete set of occurrences is
\[
\left\{a\,2^{n-3}-1:a\in\{2,3,4,6\}\right\}.
\]
No factor of any smaller positive length occurs uniquely. Thus the theorem determines the length, number, and positions of **all** globally shortest unique substrings of every finite period-doubling word from order three onward.

## Assumptions and scope
The alphabet is \(\{0,1\}\), the morphism is exactly \(0\mapsto01,\,1\mapsto00\), and occurrences are contiguous (not scattered), counted with overlaps. Here \(D_0=0\) and \(|D_n|=2^n\). Positions are zero-based. The result concerns the complete words \(D_n\), not arbitrary prefixes or other morphisms.

## Proof
Write \(N=|D_{n-1}|\) and \(s(0)=1\), \(s(1)=0\). Each morphic block is \(\varphi(x)=0s(x)\).

**Parity lemma.** Any length-at-least-three factor of any \(D_j\), \(j\geq3\), begins always at positions of the same parity. Indeed, a three-letter factor beginning at an even zero-based index has form \(0s(x)0\), hence is either \(000\) or \(010\). A three-letter factor beginning at an odd index has form \(s(x)0s(y)\), where \(xy\) is a length-two factor of \(D_{j-1}\). Since \(11\) never occurs in a period-doubling word, these factors belong to \(\{001,100,101\}\). The two sets are disjoint. This also justifies aligned desubstitution of any occurrence of \(D_t\) of length at least four.

**Three-copy suffix lemma.** For every \(j\geq3\), the suffix \(D_{j-2}\) of \(D_j\), of length \(2^{j-2}\), occurs exactly at zero-based positions \(0,2^{j-1},3\cdot2^{j-2}\). To see this, \(D_j=\varphi^{j-3}(D_3)\), and \(D_{j-2}=\varphi^{j-3}(D_1)\). The length-two word \(D_1=01\) occurs in \(D_3=01000101\) precisely at positions \(0,4,6\). Every \(D_t\) with \(t\geq2\) begins with \(010\), an even-start-only factor by the parity lemma. Thus any occurrence of \(D_{j-2}\) in \(D_j\) starts at an even position until one desubstitutes to a shorter \(D_t\); the argument applies at every stage with \(t\geq2\). At the last stage occurrences of \(01\) begin at even positions because \(1\) occurs only at odd positions in \(D_3\). Consequently each occurrence starts at a multiple of \(2^{j-2}\), and repeated aligned desubstitution gives exactly the three stated occurrences. In particular, the suffix of any length \(1\leq k\leq2^{j-2}\) occurs at least three times.

**Factor correspondence.** For a factor of length \(2k\geq4\) in \(D_j=\varphi(D_{j-1})\), occurrences at even positions correspond bijectively, including multiplicities, to occurrences of length-\(k\) factors in \(D_{j-1}\). Occurrences at odd positions correspond to occurrences of length-\(k\) factors of \(D_{j-1}\) **except** the occurrence beginning at its last possible start \(N-k\). The even factor is \(\varphi(x_1\cdots x_k)\); the odd factor consists of \(s(x_1)\), the full blocks of \(x_2,\ldots,x_k\), and the constant first bit \(0\) of the following block. Both encodings are injective. For a factor of length \(2k+1\geq3\), the even-position factors correspond bijectively to length-\(k\) factors with their last possible start omitted, while odd-position factors correspond bijectively to **all** length-\(k+1\) factors. These encodings are respectively \(\varphi(x_1\cdots x_k)0\) and \(s(x_1)\varphi(x_2\cdots x_{k+1})\). By the parity lemma, values from the even and odd classes cannot coincide.

**Induction.** The base word \(D_3=01000101\) has no unique factors of length one or two. Its four unique length-three factors start at \(1,2,3,5\). Assume the assertion for \(D_{j-1}\), where \(j\geq4\), and put \(K=2^{j-3}\). Its shortest unique-factor length is \(K+1\). Hence every factor of length at most \(K\) occurs at least twice. Furthermore, by the three-copy suffix lemma applied to \(D_{j-1}\), its suffix of length \(K\) occurs exactly three times; every shorter suffix occurs at least three times. Removing the last occurrence of any length-at-most-\(K\) factor therefore cannot produce a singleton: the only potentially affected factor is the suffix, originally of multiplicity at least three.

The factor correspondence now implies that every factor of \(D_j\) of length less than \(2K+1\) is nonunique: its desubstitution uses only length-at-most-\(K\) factors, including in the boundary-truncated class. At length \(2K+1\), the even-position class still contains no unique factor, whereas the odd-position class is in multiplicity-preserving bijection with the unique length-\(K+1\) factors of \(D_{j-1}\). Thus exactly four unique factors first occur at length \(2K+1=2^{j-2}+1\). Their zero-based starting positions satisfy \(p_j=2p_{j-1}+1\). Iterating from \(\{1,2,3,5\}\) at \(j=3\) yields precisely \(\{a2^{j-3}-1:a\in\{2,3,4,6\}\}\), completing the induction.

## Verification
The standalone program `CHECKER.py` constructs \(D_n\) directly and counts all overlapping factors of the predicted length and of the preceding length for \(3\leq n\leq13\). It also checks exact suffix occurrence starts. `CHECK_OUTPUT.txt` records the executed results. These are finite independent checks; the preceding induction proves the infinite statement.

## Relationship to prior work
Charalampopoulos, Mohamed, Pissis, Verbeek, and Zuba (2026) study general algorithms for computing shortest unique substrings and shortest absent substrings, not this exact morphic family classification. Banbara, Bannai, Guo, Köppl, Mieno, and Okamoto (2026) completely characterize size-two **string attractors** of period-doubling words and prove a parity-of-occurrences observation; their attractor classification is a different invariant and does not state the four shortest unique-factor lengths and starts. Here parity is independently proved, and the additional suffix-multiplicity and factor-correspondence arguments determine the complete global shortest-unique spectrum. A broader prior full-factor-frequency theorem could imply the result, so originality is limited to the identified and inspected literature.

## Limitations
The theorem does not characterize longer minimal unique substrings, arbitrary non-dyadic prefixes, or complexity of general SUS algorithms. Full bibliographic coverage of unindexed literature is not guaranteed. No independent proof audit has been performed.

## References
1. P. Charalampopoulos, M. Mohamed, S. P. Pissis, H. Verbeek, W. Zuba, *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826, first posted 2026-05-06. https://arxiv.org/abs/2605.04826
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152, first posted 2026-02-18; CPM 2026, DOI 10.4230/LIPIcs.CPM.2026.33. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2026.33
