# Exact initial ternary profile for correcting a burst of at most two deletions

## Finding
For the alphabet \(\Sigma_3=\{0,1,2\}\), let \(D_k(x)\) be the set of distinct words obtained from \(x\in\Sigma_3^n\) by deleting \(k\) consecutive symbols, and put \(D_{\le 2}(x)=D_1(x)\cup D_2(x)\). Let \(A^{\mathrm{burst}}_{3,\le 2}(n)\) be the maximum size of a code \(C\subseteq\Sigma_3^n\) such that \(D_{\le 2}(x)\cap D_{\le 2}(y)=\varnothing\) for every two distinct \(x,y\in C\). Then
\[
(A^{\mathrm{burst}}_{3,\le 2}(2),A^{\mathrm{burst}}_{3,\le 2}(3),A^{\mathrm{burst}}_{3,\le 2}(4),A^{\mathrm{burst}}_{3,\le 2}(5))=(1,3,7,13).
\]
Thus the complete initial ternary profile through length five is exact.

## Assumptions and scope
A burst of length one deletes one symbol; a burst of length two deletes two adjacent symbols. The receiver knows only the shortened word, not the deletion location. Outputs produced by one and two deletions have different lengths, so a pair of source words is confusable exactly when either their one-deletion balls intersect or their two-consecutive-deletion balls intersect. The result concerns the ternary alphabet and lengths \(2\le n\le5\). It makes no assertion for \(n\ge6\), and it does not concern two arbitrary, nonconsecutive deletions.

## Proof
For each \(n\in\{2,3,4,5\}\), form a graph \(G_n\) on all \(3^n\) ternary words. Two vertices are adjacent when both their one-deletion balls and their two-consecutive-deletion balls are disjoint. By definition, a set of words is a code correcting a burst of at most two deletions exactly when it is a clique in \(G_n\). Hence \(A^{\mathrm{burst}}_{3,\le2}(n)=\omega(G_n)\).

The accompanying verifier constructs every deletion ball twice, once by slicing and once by explicitly filtering deleted coordinates, and asserts equality of the two constructions for every source word. It then constructs \(G_n\) in full and runs an exact branch-and-bound maximum-clique algorithm. At each search node a greedy proper coloring of the current candidate-induced graph provides an upper bound on the number of additional clique vertices; a branch is pruned only when that bound cannot improve the best clique already found. This is a valid exhaustive upper-bound certificate because every clique uses at most one vertex from each color class, while each recursive branch explicitly includes one remaining candidate and restricts the continuation to its neighbors.

Explicit attaining codes, written as ternary strings, are:

- \(n=2\): `22`;
- \(n=3\): `222`, `121`, `020`;
- \(n=4\): `2222`, `2020`, `2121`, `1111`, `1010`, `0112`, `0000`;
- \(n=5\): `22222`, `22120`, `21110`, `12121`, `11111`, `10101`, `20202`, `20001`, `10002`, `02122`, `01112`, `02010`, `00000`.

The exact clique search returns sizes \(1,3,7,13\), respectively, so the witnesses meet matching exhaustive upper bounds.

## Verification
Run `python3 verify.py`. The verifier uses only the Python standard library. It enumerates all \(3^n\) source words for each \(2\le n\le5\), compares two independent deletion-ball constructors word by word, verifies each displayed witness is a clique, and computes the exact clique number. The expected terminal line is `VERIFY_OK profile=1,3,7,13`. The corresponding explored search-node counts are \(2,4,18,23770\).

## Relationship to prior work
Wang, Sima, and Farnoud introduced the nonbinary at-most-two-burst-deletion setting at ISIT 2021. The extended treatment by Wang, Tang, Sima, Gabrys, and Farnoud defines the same consecutive-burst model, studies maximum-cardinality burst-error-correcting codes, gives nonasymptotic bounds, and develops constructions with logarithmic redundancy. Its nonasymptotic bound for an exact two-symbol burst, when specialized to \(q=3,t=2,n=4\), gives the upper bound \(9\); the exact at-most-two-burst value here is \(7\), so that bound does not determine this finite case. Song and Cai give broader nonbinary burst-deletion constructions and redundancy bounds, not an exact finite ternary table. Targeted searches for exact profiles, the length-five value \(13\), compatibility-graph formulations, and equivalent finite-table descriptions did not locate a published statement implying these four maxima.

## Limitations
The proof is a complete finite computation only for \(2\le n\le5\). A search attempt beyond this range is not evidence about larger lengths and is not part of the claim. The originality assessment cannot rule out an unindexed finite table, thesis computation, or differently phrased prior result. The 2021 conference record was bibliographically verified, while the materially inspected same-channel full text is the later open extended treatment.

## References
1. S. Wang, J. Sima, and F. Farnoud, “Non-binary Codes for Correcting a Burst of at Most 2 Deletions,” IEEE International Symposium on Information Theory, 2021, DOI 10.1109/ISIT45174.2021.9517917.
2. S. Wang, Y. Tang, J. Sima, R. Gabrys, and F. Farnoud, “Non-binary Codes for Correcting a Burst of at Most \(t\) Deletions,” arXiv:2210.11818.
3. W. Song and K. Cai, “Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes,” arXiv:2210.14006.
