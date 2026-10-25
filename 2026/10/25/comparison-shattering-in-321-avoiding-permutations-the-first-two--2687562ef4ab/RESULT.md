# Comparison shattering in 321-avoiding permutations: the first two-round gap and an unbounded separation

## Finding

For each integer \(n\ge1\), let \(\operatorname{Av}_n(321)\) consist of the permutations \(\pi\) of \([n]\) having no indices \(i<j<k\) with \(\pi(i)>\pi(j)>\pi(k)\). Regard each permutation as the Boolean concept
\[
 h_\pi(i,j)=\mathbf1[\pi(i)<\pi(j)]\qquad(1\le i<j\le n).
\]
Write \(\mathcal C_n=\{h_\pi:\pi\in\operatorname{Av}_n(321)\}\), with VC and Littlestone dimensions taken on the complete domain of pairwise position comparisons.

**Theorem.** For every \(n\ge1\),
\[
 \operatorname{VCdim}(\mathcal C_n)=n-1.
\]
For \(n=1,2,\ldots,8\), the exact Littlestone dimensions are, in order,
\[
 (0,1,2,3,4,6,7,9).
\]
Consequently, the first strict VC–Littlestone gap occurs at \(n=6\), and the first gap of at least two occurs at \(n=8\). Moreover, for every integer \(s\ge1\),
\[
 \operatorname{Ldim}(\mathcal C_{8s})\ge9s,
 \quad \operatorname{VCdim}(\mathcal C_{8s})=8s-1,
 \quad \operatorname{Ldim}(\mathcal C_{8s})-\operatorname{VCdim}(\mathcal C_{8s})\ge s+1.
\]
Thus a single natural permutation-avoidance class has an unbounded difference between adaptive and nonadaptive comparison-query shattering.

## Assumptions and scope

All permutations have distinct entries and positions are fixed and labeled. The query \((i,j)\), with \(i<j\), asks whether the entry at position \(i\) is smaller than the entry at position \(j\); it does **not** ask for the value at a position, a pattern occurrence, or a comparison of two specified values. The first eight Littlestone values are exact; for larger \(n\), only the stated lower bound on the subsequence of lengths divisible by eight is claimed. The class is nonempty for every \(n\ge1\).

## Proof

**1. VC upper bound.** Let \(Q\) be a shattered set of position-pair comparisons. Draw a simple undirected graph on \([n]\) with edge set \(Q\). If this graph contained a cycle, select answers along the cycle that orient its edges into a directed cycle. No strict total order realizes that assignment. Hence \(Q\) is a forest and has at most \(n-1\) edges. This upper bound applies even to the class of *all* permutations.

**2. VC lower bound using 321-avoidance.** Select the \(n-1\) star comparisons \((1,j)\), for \(2\le j\le n\). For any requested bit vector, let \(z\) be the number of zero bits and set \(\pi(1)=z+1\). In the remaining positions, insert the values \(1,2,\ldots,z\), in increasing order of their positions, wherever the desired bit is zero; insert the values \(z+2,\ldots,n\), also in increasing order of their positions, wherever it is one. Every target bit is realized. The low and high subsequences are each increasing; the pivot occurs at the first position and is between them in value. No three entries form a decreasing subsequence. Thus this construction belongs to \(\operatorname{Av}_n(321)\) and shatters all \(n-1\) star comparisons.

**3. Finite exact adaptive dimensions.** For any nonempty finite family \(F\) of distinct Boolean hypotheses, and each query \(q\), let \(F_0(q)\) and \(F_1(q)\) be the two answer fibers. Define
\[
 R(F)=\begin{cases}
 0,&|F|=1,\\
 \max\limits_{q:\,F_0(q),F_1(q)\ne\varnothing}
       \bigl(1+\min\{R(F_0(q)),R(F_1(q))\}\bigr),&|F|>1.
 \end{cases}
\]
A nonempty family with distinct hypotheses and size larger than one always has a separating query. Induction on \(|F|\) proves that \(R(F)\) is precisely the maximal depth of a complete binary shattered decision tree: at its root both subfamilies must support the entire remaining depth. A necessary pruning inequality is \(R(F)\le\lfloor\log_2|F|\rfloor\).

Enumerating exactly the 321-avoiders and applying this recurrence gives:

| \(n\) | Number of avoiders | \(\operatorname{VCdim}\) | \(\operatorname{Ldim}\) |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 0 |
| 2 | 2 | 1 | 1 |
| 3 | 5 | 2 | 2 |
| 4 | 14 | 3 | 3 |
| 5 | 42 | 4 | 4 |
| 6 | 132 | 5 | 6 |
| 7 | 429 | 6 | 7 |
| 8 | 1430 | 7 | 9 |

The attached `build_cert.py` implements exact recurrence ranks on bitset fibers, starting from lexicographically enumerated avoiders. The separate `verify_independent.py` builds the same avoider sets by insertion of the new maximum, and tests the depth-feasibility predicate rather than using the rank recurrence. Both reproduce the table. The attached `tree_depth9.json` contains all \(511\) internal pair queries and \(512\) distinct leaf permutations of a complete depth-nine tree at \(n=8\). The independent verifier checks each of the \(512\) length-nine answer paths from its actual leaf permutation. In particular the lower bound at eight is witnessed independently of the upper-bound search.

**4. Unbounded gap by direct sums.** For \(s\ge1\), take \(s\) independent blocks of eight positions and restrict attention to permutations of the form \(\pi_1\oplus\cdots\oplus\pi_s\), where each \(\pi_t\in\operatorname{Av}_8(321)\) and later blocks have uniformly larger values than earlier blocks. A decreasing three-term subsequence cannot traverse different blocks, so every such direct sum avoids 321. Questions involving positions inside one block depend on that block alone. Running the verified depth-nine decision tree consecutively within the \(s\) blocks creates a complete depth-\(9s\) shattered decision tree: every answer path admits compatible independent choices of its \(s\) block permutations. Hence \(\operatorname{Ldim}(\mathcal C_{8s})\ge9s\). Step 2 gives its exact VC dimension \(8s-1\), proving the gap bound.

## Verification

The standalone proof-certificate and finite upper-bound package comprises `build_cert.py`, `verify_independent.py`, `tree_depth9.json`, `dimensions.json`, `build_output.txt`, and `verify_output.txt`. In a directory containing these files, execute `python3 build_cert.py` and `python3 verify_independent.py`. Both use only the Python standard library. The first script creates the certificate and finite dimension table; the second independently enumerates the hypothesis families, tests all feasible depths through the information bound, and replays every leaf of the depth-nine tree. The recorded independent output ends with `ALL_321_AVOIDING_CHECKS_PASS`. The infinite-family statement is a deductive theorem; finite computation is used only for the base rank at eight and the claimed small-size cutoff.

## Relationship to prior work

The connection between 321-avoiders, Catalan structures, and two-row tableaux is classical, and is developed from a dynamical perspective by Adenbaum and Elizalde [1]. That paper studies rowmotion, RSK, and homomesy of permutation statistics, not adaptive comparison shattering. Guingona, Kolesnikov, Nierwinski, and Soucy [2] provide general results on VC and Littlestone dimensions for linear zero-set families; those hypotheses do not identify these pattern-restricted comparison concepts. Manurangsi [3] proves computational hardness for dimension estimation of explicitly presented generic concept classes, rather than the special exact profile or the direct-sum separation here. Standard facts about finite shattering are used as background, not claimed as innovations.

## Limitations

The finite Littlestone classification stops at eight positions; no formula for \(\operatorname{Ldim}(\mathcal C_n)\) at every larger \(n\) is established. The infinite result proves a lower bound, not an exact larger-size Littlestone value. Exhaustive computational searches establish finitely many rank values under a fully specified recurrence; the proof does not assume that small enumerations themselves establish an asymptotic formula. Historical publication priority outside the accessed and inspected literature cannot be ruled out, and the result has not undergone an independent audit.

## References

[1] B. Adenbaum and S. Elizalde, *Rowmotion on 321-avoiding permutations*, arXiv:2212.11347, first public version 2022-12-21, https://arxiv.org/abs/2212.11347.

[2] V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805, first public version 2021-09-10, https://arxiv.org/abs/2109.04805.

[3] P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443, first public version 2022-11-02, https://arxiv.org/abs/2211.01443.
