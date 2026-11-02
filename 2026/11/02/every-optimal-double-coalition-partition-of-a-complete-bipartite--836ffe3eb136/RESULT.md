# Every optimal double-coalition partition of a complete bipartite graph

## Finding

Let \(K_{r,s}\) be a complete bipartite graph with **labeled** vertices in shores \(A\) and \(B\), where \(3\le r\le s\). A *double-dominating set* \(D\) contains at least two vertices in every closed neighborhood. A *double-coalition partition* is a partition into nonempty, **unlabeled blocks**, none double-dominating individually, such that each block has a different block whose union with it is double-dominating. A partition is *optimal* if it has the largest possible number of blocks. Let \(\mathcal N(r,s)\) count all optimal partitions, retaining the vertex labels but ignoring the order of blocks.

**Classification theorem.** Every optimal partition belongs to exactly one of the following mutually disjoint families, and all listed partitions are optimal:

1. **\(A\)-hub.** If \(r\le5\), either the whole shore \(A\) is one block and every vertex of \(B\) is a singleton, or choose \(a\) with \(2\le a\le r-1\), choose \(a\) vertices of \(A\) and one vertex of \(B\) for a mixed block, put the remaining \(r-a\) vertices of \(A\) into one block (a singleton when \(r-a=1\)), and make all other vertices of \(B\) singleton blocks.
2. **\(B\)-hub.** The shore-exchanged family is allowed only when \(r=s\le5\).
3. **Two bridge triples.** If \(r,s\ge5\), take exactly two nonsingleton blocks, of shore occupancies \((1,2)\) and \((2,1)\); every other vertex is a singleton.

The number of distinct optimal partitions is
\[
\boxed{\begin{aligned}
\mathcal N(r,s)={}&\mathbf1_{\{r\le5\}}\left(1+s\sum_{a=2}^{r-1}\binom ra\right)\\
&+\mathbf1_{\{r=s\le5\}}\left(1+r\sum_{b=2}^{s-1}\binom sb\right)\\
&+\mathbf1_{\{r\ge5\}}\,9\binom r3\binom s3.
\end{aligned}}
\]
For example, \(\mathcal N(3,3)=20\), \(\mathcal N(4,4)=82\), \(\mathcal N(5,5)=1152\), and \(\mathcal N(6,6)=3600\). When the shores are unequal and \(r\le4\), the answer is \(1+s(2^r-r-2)\). When \(r=5<s\), the answer is \(1+25s+90\binom{s}{3}\), while when \(r\ge6\) it is \(9\binom r3\binom s3\).

The known optimal number of blocks is \(s+1\) for \(3\le r\le5\) and \(r+s-4\) for \(r\ge6\). A self-contained proof of these optimal sizes is included below; the new assertion is the **complete equality classification and its enumeration**.

## Assumptions and scope

All graphs are finite, simple and undirected. A double-dominating set means a set \(D\) with \(|D\cap N[v]|\ge2\) for **every** vertex \(v\). No block of a double-coalition partition can itself be double-dominating. Blocks are not named or ordered. Vertices are distinct and labeled, so changing which vertices form a block generally changes the partition. Parameters are arbitrary integers \(3\le r\le s\), with no upper bound. The formulas apply to complete bipartite graphs, not arbitrary complete multipartite graphs or to other coalition notions.

For a subset meeting \(A\) in \(a\) vertices and \(B\) in \(b\) vertices, the complete-bipartite neighborhood structure gives the exact criterion
\[
\tag{1} DD(a,b)\iff a\ge1,\ b\ge1,\ (a=r\ \text{or}\ b\ge2),\ (b=s\ \text{or}\ a\ge2).
\]
This criterion will also be used in the exhaustive finite certificate.

## Proof

**1. The optimal block number (included to verify the premise independently).** If a partition has \(k\) blocks on \(r+s\) vertices, set its *excess* to \(e=r+s-k\). Every nonsingleton block \(U\) contributes \(|U|-1\) to \(e\), so at most \(2e\) vertices are in nonsingleton blocks. The union of any two blocks has at most \(e+2\) vertices.

Suppose \(e<\min\{r-1,4\}\). Then \(e\le3\) and \(r\ge e+2\). Any double-dominating union of two blocks cannot contain one *entire* shore plus a vertex of the other shore, because that would require at least \(r+1\ge e+3\) vertices. By (1), such a union must therefore contain at least two vertices from each shore.

There must be a singleton, because the number of vertices exceeds \(2e\). If all singleton vertices were in \(B\), take a singleton \(y\in B\). Any partner block has occupancy \((a,1)\), with \(a\ge2\); otherwise it is itself double-dominating or cannot complete \(y\). This block uses excess \(a\). Under the hypothesis that \(A\) has no singleton, at least \(r-a\ge e+2-a\) additional \(A\)-vertices must lie in nonsingleton blocks. Yet the remaining excess \(e-a\) can support at most \(2(e-a)\) vertices in nonsingleton blocks, and \(e+2-a>2(e-a)\) for \(a\ge2\) and \(e\le3\). This is impossible. Exchanging the shores proves that **both shores have singleton vertices**.

A singleton in \(A\) needs a partner with at least one \(A\)-vertex and two \(B\)-vertices; by (1) this partner must have exactly one \(A\)-vertex, or it would already be double-dominating. A singleton in \(B\) similarly needs a different partner with exactly one \(B\)-vertex and at least two \(A\)-vertices. These two distinct partners each contribute excess at least two, contradicting \(e\le3\). Therefore \(e\ge\min\{r-1,4\}\).

When \(r\le5\), the all-\(A\) hub with \(s\) singleton \(B\)-vertices has excess \(r-1\). When \(r\ge5\), two bridge triples with all other vertices singleton have excess \(4\). All these partitions obey (1), so the minimum possible excess is exactly \(\min\{r-1,4\}\). This recovers the previously published optimal block count.

**2. Rigidity for \(r\ge6\).** Now optimality gives \(e=4\). At least four vertices are singleton, since at most eight vertices belong to nonsingleton blocks. Suppose, for contradiction, that \(A\) has no singleton and that \(y\in B\) is singleton. Its partner must have occupancy \((a,1)\), where \(2\le a\le4\), because a nontrivial block has at most five vertices and no double-dominating block is permitted. For \(a\in\{3,4\}\), the remaining excess \(4-a\) supports fewer than \(r-a\) remaining \(A\)-vertices in nonsingleton blocks. If \(a=2\), the remaining excess is two, so the only way to avoid \(A\)-singletons is \(r=6\) with two pure \(A\)-doubletons. But each such doubleton has no coalition partner: joining it to the \((2,1)\) block yields only four \(A\)-vertices and one \(B\)-vertex, and all other possible partners provide even less. Thus \(A\) has a singleton; by symmetry \(B\) does too.

Each singleton type requires a different partner of size at least three, with respective occupancies \((1,\ge2)\) and \((\ge2,1)\). The two partners consume the whole excess of four, so both are triples, with occupancies \((1,2)\) and \((2,1)\). There can be no further nonsingleton block. This proves uniqueness of the *profile*, not of the labeled partition.

**3. Unequal shores with \(r\le5\) and \(s>2(r-1)\).** Put \(e=r-1\). At most \(2e\) vertices can lie in nonsingleton blocks, so a vertex \(y\in B\) must be singleton. Let \(W\) be a partner block. Using (1), the fact that \(|W|\le e+1=r<s\), and the prohibition on individually double-dominating blocks, \(W\) must have one of the profiles \((r,0)\) or \((a,1)\) with \(2\le a\le r-1\).

If \(W=(r,0)\), it consumes all the excess and gives the whole-shore hub. Otherwise write \(m=r-a\), so \(1\le m\le3\) and the remaining excess is \(m-1\). If \(m=1\), the remaining \(A\)-vertex is a singleton and gives a split hub. For \(m\in\{2,3\}\), suppose an \(A\)-singleton exists. The block \(W\) cannot partner it, since their union has fewer than \(r\) vertices in \(A\) and only one in \(B\). Such a singleton needs another partner with at least one \(A\)-vertex and two \(B\)-vertices, costing excess at least two. Since \(m-1\le2\), the only possibility is \(r=5,a=2,m=3\), with exactly a \((1,2)\) triple using the remaining excess. This is the two-bridge-triples family.

If no \(A\)-singleton exists, all \(m\) leftover \(A\)-vertices must occur in nonsingleton blocks. For \(m=2\) and one remaining unit of excess, the sole possibility is a pure \((2,0)\) doubleton. For \(m=3\) and two units of excess, the possibilities are one pure \((3,0)\) triple or two doubletons of types \((2,0)\) and \((1,1)\). In the latter case the pure \(A\)-doubleton has no coalition partner, since its union with \(W\) has only one \(B\)-vertex and fewer than \(r\) \(A\)-vertices; it cannot partner the other doubleton or a singleton either. Hence only a pure \((m,0)\) block survives. Together with \(W\), this gives exactly the split hubs listed in the theorem.

**4. Finite boundary cases.** The preceding argument covers all \(r\le5\) with \(s>2(r-1)\). Every remaining pair is in the following **finite, exhaustive** table. Its columns report the number of valid nonsingleton-block occupancy profiles in the \(A\)-hub, \(B\)-hub, and bridge-triple families, respectively:

| \((r,s)\) | \(A\)-hub profiles | \(B\)-hub profiles | Bridge profile | Total optimal partitions |
|---|---:|---:|---:|---:|
| \((3,3)\) | 2 | 2 | 0 | 20 |
| \((3,4)\) | 2 | 0 | 0 | 13 |
| \((4,4)\) | 3 | 3 | 0 | 82 |
| \((4,5)\) | 3 | 0 | 0 | 51 |
| \((4,6)\) | 3 | 0 | 0 | 61 |
| \((5,5)\) | 4 | 4 | 1 | 1152 |
| \((5,6)\) | 4 | 0 | 1 | 1951 |
| \((5,7)\) | 4 | 0 | 1 | 3326 |
| \((5,8)\) | 4 | 0 | 1 | 5241 |

Here is a finite exhaustive certification, rather than an inference from sample values. For each listed pair compute \(e=r-1\). Enumerate **every** unordered multiset of pairs \((a,b)\) with \(2\le a+b\le e+1\), total \(\sum(a+b-1)=e\), and coordinate sums at most \(r,s\). The residual vertices are forced singleton blocks. Apply (1) to reject any double-dominating block and to require a double-dominating union partner for every block. The exact exhaustive implementation appears in `verify.py`, function `profiles`, and checks the above nine cases. The loops cover all integer partitions of the excess, all shore occupancies and all possible singleton residues; hence this is an exhaustive bounded proof, not a heuristic search. The surviving multiset profiles are exactly the displayed hub and bridge families. No infinite extrapolation is made: the other parameter values were already proved in Steps 2–3.

**5. Enumeration of labeled partitions.** An \(A\)-hub with one whole-shore block is unique. For a split hub, selecting \(a\) vertices of \(A\) and one of \(B\) gives \(\binom ra s\) partitions. A bridge pair consists of distinguishable block types \((1,2)\) and \((2,1)\), and there are
\[
\binom r1\binom s2\binom{r-1}2\binom{s-2}1
=9\binom r3\binom s3
\]
choices. The \(B\)-hub is a separate, shore-swapped family only if the shores are equal and at most five vertices each. Adding the disjoint counts gives the displayed formula.

## Verification

`verify.py` is a standalone Python 3 program using only the standard library. Running `python3 verify.py` reproduces exact occupancy-multiset enumeration for 68 parameter pairs with \(3\le r\le10\), \(r\le s\le14\); explicitly checks every one of the nine finite boundary pairs required by the proof; and independently enumerates all vertex-labeled set partitions (using restricted-growth strings and actual closed neighborhoods) for \((r,s)=(3,3),(3,4),(4,4),(5,5)\). It checks the closed counting formula without floating-point arithmetic. The verified output is `VERIFY_OK 68 exact occupancy parameter pairs; 9 finite exceptional parameter pairs; 4 independent labeled-partition enumerations`. The infinite family is justified by Steps 1–3 and the exhaustive finite certificate in Step 4, not by observing these larger computational tests.

## Relationship to prior work

Golmohammadi introduced double coalitions and considered complete bipartite graphs in the manuscript first posted **2024-07-31**, arXiv:2407.21472. The definitive complete-bipartite **maximum block count** is proved in Henning and Mojdeh, *Double Coalitions in Graphs*, *Bulletin of the Malaysian Mathematical Sciences Society* **48**, article 51 (published 2025-02-10), Theorem 6: \(s+1\) blocks when \(r\le5\), and \(r+s-4\) blocks when \(r\ge6\). That scalar result is cited and credited, not asserted as new. Their article exhibits certain sharp constructions, but does **not** provide the classification of *all* maximizing partitions or the vertex-labeled multiplicity formula proved here. Henning and Mojdeh, *Double Coalitions in Regular Graphs*, *Graphs and Combinatorics* **41**, article 74 (published 2025-06-02), restates the scalar formula as known and addresses other graph families, not these multiplicities.

A separate notion of a \(2\)-coalition uses \(2\)-dominating sets only for vertices *outside* the selected set, rather than the closed-neighborhood double-domination condition. The two notions and their optimal partition families differ; results about \(2\)-coalitions do not imply this theorem.

## Limitations

The classification concerns only optimum-size partitions of complete bipartite graphs with both shores at least three. It says nothing about nonoptimal double-coalition partitions, or about complete multipartite graphs with three or more shores. It is a deterministic proof and exact finite certificate, **not** an independently reviewed publication-priority assertion. The scalar optimum was already known; the asserted contribution is its equality structure and multiplicity. Relevant but unindexed literature might still contain an equivalent enumeration.

## References

1. H. Golmohammadi, *Introduction to double coalitions in graphs*, arXiv:2407.21472, first posted 2024-07-31. https://arxiv.org/html/2407.21472
2. M. A. Henning and D. A. Mojdeh, *Double Coalitions in Graphs*, Bulletin of the Malaysian Mathematical Sciences Society 48, article 51 (2025), published 2025-02-10, Theorem 6. https://link.springer.com/article/10.1007/s40840-025-01831-7
3. M. A. Henning and D. A. Mojdeh, *Double Coalitions in Regular Graphs*, Graphs and Combinatorics 41, article 74 (2025), published 2025-06-02, Section 2. https://link.springer.com/article/10.1007/s00373-025-02937-2
