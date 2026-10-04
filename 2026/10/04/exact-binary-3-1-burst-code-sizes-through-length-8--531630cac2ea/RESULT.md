# Exact binary \((3,1)\)-burst code sizes through length \(8\)
## Finding
For the binary exact \((3,1)\)-burst channel, let \(A_{3,1}(n)\) be the largest size of a code \(C\subseteq\{0,1\}^n\) that corrects one burst. Then
\[
(A_{3,1}(3),A_{3,1}(4),A_{3,1}(5),A_{3,1}(6),A_{3,1}(7),A_{3,1}(8))=(1,1,2,2,4,8).
\]
The regular sphere-packing bound from the constant error-ball size gives the integer upper bounds \((1,1,2,3,5,9)\) on these six lengths. Hence it is tight through length \(5\) and is already non-tight at lengths \(6,7,8\).

## Assumptions and scope
A \((3,1)\)-burst deletes three consecutive symbols and inserts one arbitrary binary symbol at the same coordinate. For \(x\in\{0,1\}^n\), its error ball \(B_{3,1}(x)\) is the set of distinct length-\(n-2\) outputs from all legal burst positions and inserted bits. A code corrects this error exactly when the balls of distinct codewords are disjoint. The statement is only for the binary exact-burst model and only for \(3\le n\le8\); it makes no assertion about longer lengths, variable-length bursts, or nonbinary alphabets.

## Proof
Form the compatibility graph \(G_n\) on all \(2^n\) binary words of length \(n\), joining two vertices exactly when their \((3,1)\)-burst balls are disjoint. Correcting codes are precisely cliques of \(G_n\), so \(A_{3,1}(n)=\omega(G_n)\).

The lower bounds are witnessed by the following codes:

- \(n=3\): \(\{111\}\).
- \(n=4\): \(\{1111\}\).
- \(n=5\): \(\{11111,00100\}\).
- \(n=6\): \(\{111111,100100\}\).
- \(n=7\): \(\{1111111,1010100,0110010,0011001\}\).
- \(n=8\): \(\{11111111,11010100,10101010,10000001,01110010,01011001,00111000,00010011\}\).

For the upper bounds, `verify.py` constructs every error ball and every edge of \(G_n\), then runs an exhaustive maximum-clique branch-and-bound. At each recursive node it greedily partitions the current candidate set into independent color classes of \(G_n\). If there are \(k\) such classes, every clique in that candidate subgraph has size at most \(k\); therefore pruning when the current clique size plus \(k\) cannot beat the incumbent is sound. Each remaining candidate is then branched on and removed, so the finite search exhausts all cliques not excluded by a proved coloring upper bound. It returns clique numbers \((1,1,2,2,4,8)\).

## Verification
The verifier implements the channel twice: once by direct string slicing and once by explicit output-coordinate construction. These implementations agree for every one of the \(2^n\) source words at each \(3\le n\le8\). Every ball has \(n-1\) distinct outputs, agreeing with the constant-ball formula in Lu--Zhang for this specialization. The verifier checks every displayed witness for pairwise ball disjointness and independently recomputes the maximum clique. The replay output is stored in `verification_output.txt`; its terminal line is `VERIFY_OK profile=1,1,2,2,4,8`.

## Relationship to prior work
Lu and Zhang introduced the general \((t,s)\)-burst model, proved the constant error-ball size and the associated sphere-packing upper bound, and singled out \((3,1)\) for an explicit construction with redundancy within an additive constant of optimal. Their inspected paper develops general and asymptotic bounds rather than an exact short-blocklength table. Sun, Lu, Zhang, and Ge later gave asymptotically optimal \(q\)-ary constructions with \(\log n+O(1)\) redundancy for fixed channel parameters; that broader asymptotic result does not determine these six finite maxima. Targeted searches for the exact profile, its length-\(8\) endpoint, the equivalent disjoint-ball formulation, and finite tables found no inspected source stating or implying the profile.

## Limitations
The upper bounds are finite exhaustive computations, not an infinite-length theorem. The maximum-clique proof is independently replayable from the supplied standard-library program, but no independent external audit has been performed. Literature search cannot rule out an unindexed thesis, unpublished computation, or differently phrased finite table containing the same values. The result therefore asserts the mathematics and the scope of the performed comparison, not absolute historical priority.

## References
1. Z. Lu and Y. Zhang, *t-Deletion-s-Insertion-Burst Correcting Codes*, arXiv:2201.10259v1, 2022.
2. Y. Sun, Z. Lu, Y. Zhang, and G. Ge, *Asymptotically Optimal Codes for \((t,s)\)-Burst Error*, arXiv:2403.11750v1, 2024.
