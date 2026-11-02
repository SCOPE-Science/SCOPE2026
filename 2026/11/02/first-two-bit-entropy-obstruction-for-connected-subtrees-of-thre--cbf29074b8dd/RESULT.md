# First two-bit entropy obstruction for connected subtrees of three-arm spiders

## Finding

Let \(S_m\) be the tree with one degree-three center and three disjoint arms, each containing exactly \(m\) edges, where \(m\ge1\). Let \(\mathcal C_m\) consist of the indicator functions of **all nonempty, connected, induced vertex sets** of \(S_m\), queried by individual vertex membership. Then
\[
\operatorname{VCdim}(\mathcal C_m)=3\quad(m\ge1),\qquad
\operatorname{Ldim}(\mathcal C_m)\ge3\lfloor\log_2(m+1)\rfloor.
\]
The exact online dimensions for \(1\le m\le12\) are, in order,
\[
3,4,6,6,7,8,9,9,9,9,9,9.
\]
In particular, \(\lvert\mathcal C_{12}\rvert=2431\), but
\[
\operatorname{Ldim}(\mathcal C_{12})=9<11
=\lfloor\log_2\lvert\mathcal C_{12}\rvert\rfloor.
\]
This is the **first two-bit deficit from the concept-cardinality bound** in this one-parameter equal-arm family: for each \(1\le m<12\) the corresponding deficit is at most one. The VC dimension remains three while online dimension grows without bound.

| Arm length \(m\) | Number of concepts | VC | Littlestone | Cardinality upper bound | Deficit |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 11 | 3 | 3 | 3 | 0 |
| 2 | 36 | 3 | 4 | 5 | 1 |
| 3 | 82 | 3 | 6 | 6 | 0 |
| 4 | 155 | 3 | 6 | 7 | 1 |
| 5 | 261 | 3 | 7 | 8 | 1 |
| 6 | 406 | 3 | 8 | 8 | 0 |
| 7 | 596 | 3 | 9 | 9 | 0 |
| 8 | 837 | 3 | 9 | 9 | 0 |
| 9 | 1135 | 3 | 9 | 10 | 1 |
| 10 | 1496 | 3 | 9 | 10 | 1 |
| 11 | 1926 | 3 | 9 | 10 | 1 |
| 12 | 2431 | 3 | 9 | 11 | 2 |

## Assumptions and scope

All graphs are finite, simple, and labeled by their vertex positions. The center is vertex \(0\); the vertex at distance \(j\) on arm \(a\in\{0,1,2\}\) has code \(1+am+j-1\), for \(1\le j\le m\). A concept is a nonempty vertex set inducing a connected subgraph of this fixed spider. A query chooses any of its \(3m+1\) vertices and returns the membership bit. Empty vertex sets, disconnected unions of arms, edge-membership queries, and arbitrary trees are not part of this concept class. An adaptive Littlestone tree must be full and all root-to-leaf label sequences realizable.

## Proof

**Exhaustive description and counts.** A connected vertex set not containing the center lies wholly within a single arm and is a nonempty interval. These contribute \(3m(m+1)/2\) sets. A connected vertex set containing the center independently selects a prefix of length \(0,\ldots,m\) on each arm. These contribute \((m+1)^3\) sets. These two forms are disjoint and exhaustive, so
\[
\lvert\mathcal C_m\rvert=(m+1)^3+\frac{3m(m+1)}2.
\]
The verifier constructs these sets directly and independently reconstructs them by growing vertex-connected sets from singletons.

**Static dimension.** The three leaves are shattered: the hull of any nonempty selection of leaves contains exactly those selected leaves, and the center alone realizes the empty trace. Conversely, among any four vertices of a three-arm spider, one lies on the unique path between two others. Every connected vertex set containing those two endpoints also contains the intermediate marked vertex, so the trace with the two endpoints positive and the intermediate vertex negative is impossible. Hence the VC dimension is exactly three for every positive arm length. This static observation is background; the new finite obstruction concerns online dimension.

**All-size online lower bound.** Put \(r=\lfloor\log_2(m+1)\rfloor\). Restrict to center-containing sets whose three arm-prefix lengths independently belong to \(\{0,1,\ldots,2^r-1\}\). On any one arm, membership at distance \(j\) asks whether its prefix length is at least \(j\). Balanced threshold queries give a complete depth-\(r\) binary search tree on these \(2^r\) choices. Concatenating the three arm searches gives depth \(3r\), with distinct concept witnesses at its \(2^{3r}\) leaves. Thus \(\operatorname{Ldim}(\mathcal C_m)\ge3r\), including depth nine for \(m=12\).

**Finite exact upper bound.** For a nonempty version space \(H\) of indicator concepts define \(P_0(H)\) to be true. For \(k\ge1\), let
\[
P_k(H)\iff \exists v\in V(S_m):
P_{k-1}(\{h\in H:h(v)=0\})\ \wedge\
P_{k-1}(\{h\in H:h(v)=1\}).
\]
The empty space makes every \(P_k\) false, including \(P_0\). Induction on \(k\) proves that \(P_k(H)\) holds exactly when \(H\) shatters a complete binary adaptive tree of depth \(k\). The necessary bound \(\lvert H\rvert\ge2^k\) permits exact pruning. Both distributed programs compute this recurrence on **every** possible vertex query at each state; one uses integer bitsets and the other frozen sets of concepts. They agree on all twelve exact dimensions, not merely sampled decisions. In particular, \(P_9(\mathcal C_{12})\) is true and \(P_{10}(\mathcal C_{12})\) is false.

A more local exact obstruction is supplied as `spider_root_profile.csv`: for every possible first-query distance \(j\in\{0,1,\ldots,12\}\), it records exact conditioned Littlestone dimensions on both answers. Arm permutation symmetry makes the distance alone sufficient. The maximum over these thirteen root positions of one plus the smaller branch dimension is exactly nine, excluding all depth-ten trees. Values in the profile are independently reproducible by `spider_root_profile.py`.

**First threshold.** The complete verified table explicitly checks every smaller positive integer arm length. The deficits are \(0\) or \(1\) through length eleven, and become \(2\) at length twelve. No inference about the first occurrence of larger deficits is made.

## Verification

With Python 3.10 or later and no third-party libraries, run `python3 spider_connected_verify.py` followed by `python3 spider_root_profile.py` from this directory. The first checks equality of both exhaustive concept enumerators at every arm length one through twelve, the closed concept-count formula, two independently represented adaptive-depth recurrences, a constructive product-threshold lower bound, and the first two-bit cutoff. Its terminal message is `SPIDER_CONNECTED_SUBTREES_ALL_CHECKS_PASS`. The second reproduces all thirteen entries of the provided root-profile CSV from the same exact hypotheses. All computations are finite and terminate; they are not stand-ins for infinite assertions. The universal VC proof and online lower-bound construction are independent of finite experiments.

## Relationship to prior work

Work on connected-induced-subgraph counts (Dossou-Olory, arXiv:1910.04552, 2019) motivates the combinatorial concept family and treats enumeration, but not adaptive membership shattering. Munaro (arXiv:1302.6500, 2013) surveys earlier connected-subgraph VC bounds and studies other graph-subgraph shattering questions; static VC facts are not claimed new here. Krishna and coauthors (arXiv:2302.08557, 2023) study discrepancy of tree-subtree families, not adaptive Littlestone depth. General binary-class closure bounds of Ghazi and coauthors (PMLR 132, 2021) do not themselves supply this exact twelve-arm cutoff. These are distinctions in statements, not assertions that all possible prior literature has been searched.

## Limitations

Exact online dimensions are established only through twelve edges per arm. No closed formula for arbitrary arm lengths, no claim about unequal arm lengths, and no external independent scientific validation are provided. The specific historical-priority risk is an unlocated equivalent classification under connected-tree range queries or mistake-bound terminology. The computational upper bound is rigorous relative to the displayed recurrence and exhaustive enumeration, but merits independent code and mathematical review.

## References

- A. A. V. Dossou-Olory, *Cut and pendant vertices and the number of connected induced subgraphs of a graph*, arXiv:1910.04552v1 (first posted 2019-10-08), https://arxiv.org/abs/1910.04552.
- A. Munaro, *The VC-Dimension of Graphs with Respect to k-Connected Subgraphs*, arXiv:1302.6500 (first posted 2013-02-26), https://arxiv.org/abs/1302.6500.
- T. Krishna, P. Michaeli, M. Sarantis, F. Wang, and Y. Wang, *Discrepancies of subtrees*, arXiv:2302.08557v1 (first posted 2023-02-16), https://arxiv.org/abs/2302.08557.
- B. Ghazi, N. Golowich, R. Kumar, and P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, PMLR 132 (2021), https://proceedings.mlr.press/v132/ghazi21a.html.
