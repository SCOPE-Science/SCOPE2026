# Exact optimal 2-coalition partition profiles of narrow complete bipartite graphs

## Finding

Let \(K_{s,t}\) have disjoint, distinguishable shores \(A,B\) with \(|A|=s\) and \(|B|=t\). For every integer \(s\in\{3,4,5\}\) and \(t\ge s+1\), the maximum number of blocks in a 2-coalition partition is \(t+1\). More strongly, *every* optimal partition is described by exactly one of the nonsingleton-block profiles in the following table. An occupancy pair \((a,b)\) denotes a block containing \(a\) vertices of \(A\) and \(b\) of \(B\). All other vertices are singleton blocks.

| \(s\) | Exhaustive nonsingleton block profiles | Number of distinct optimal partitions |
|---|---|---|
| \(3\) | \(((2,1))\) | \(3t\) |
| \(4\) | \(((3,1))\), \(((2,0),(2,1))\) | \(10t\) |
| \(5\) | \(((4,1))\), \(((2,0),(3,1))\), \(((2,1),(3,0))\), \(((1,2),(2,1))\) | \(25t+15t(t-1)(t-2)\) |

Graph vertices are labeled and partition blocks are unlabeled. The cubic leading term at shore size five, compared with the linear counts at shore sizes three and four, is a genuine change in optimal-partition multiplicity, even though the maximum cardinality remains \(t+1\).

## Assumptions and scope

A subset \(S\) *2-dominates* when every vertex outside \(S\) has at least two neighbors in \(S\); vertices inside \(S\) face no neighbor requirement. Two disjoint **non-2-dominating** sets are coalition partners if their union 2-dominates. A 2-coalition partition partitions all vertices into nonempty blocks such that each block is either a 2-dominating set of exactly two vertices or has a coalition partner among the other blocks. We count partitions up to permutation of blocks (but not relabeling of vertices). Set \(\mathcal N_{s,t}\) to be the number of such partitions with the maximum possible block count. We consider only \(s=3,4,5\), \(t\ge s+1\), and no analogous assertion is made for balanced shores or larger \(s\).

For a block with occupancy \((a,b)\), direct inspection of the two shores gives the exact criterion
\[
 \operatorname{Dom}_{s,t}(a,b)\ \Longleftrightarrow\ (a=s\ \text{or}\ b\ge2)\ \text{and}\ (b=t\ \text{or}\ a\ge2).
\]
For the stated parameter range no set of size two is 2-dominating. Therefore *each block* of a valid partition must be non-2-dominating and must have a distinct coalition partner.

## Proof

**Cardinality and excess.** The formula \(C_2(K_{s,t})=t+1\) for \(3\le s\le5\) is known from Brešar–Henning–Samadi (Theorem 5.2, 2025); we use it as a credited input, not as a new result. Thus every optimal partition \(\Pi\) has exactly \(t+1\) blocks and excess
\[
 E(\Pi):=\sum_{P\in\Pi}(|P|-1)=(s+t)-(t+1)=s-1\le4.
\]
Call a block *large* if it has size at least two. Every large block consumes at least one unit of excess. Hence there are at most \(E\) large blocks, with at most \(2E\) vertices altogether, and each large block has size at most \(E+1\). All unlisted vertices are singleton blocks. A large block is completely characterized for the coalition test by its two occupation counts \((a,b)\); the exact test for every block and pair is the formula in the preceding section.

**Finite exhaustive occupancy certificate.** A large-block profile is a multiset of pairs \((a,b)\) satisfying \(0\le a\le s\), \(0\le b\le t\), \(2\le a+b\le E+1\), \(\sum(a+b-1)=E\), \(\sum a\le s\), and \(\sum b\le t\). Appending \(s-\sum a\) copies of \((1,0)\) and \(t-\sum b\) copies of \((0,1)\) gives a complete occupancy multiset. For each such multiset, check every block \(P\) using \(\operatorname{Dom}_{s,t}(P)\) and requiring another block \(Q\ne P\) with both \(P,Q\) non-dominating and \(\operatorname{Dom}_{s,t}(P+Q)\). The supplied standalone checker implements these instructions literally. It enumerates *all* candidate multisets, not graph samples, for \(s\in\{3,4,5\}\) and every \(s+1\le t\le2(s-1)+2\). All surviving profiles are precisely those in the stated table; in total only 423 feasible-budget candidate occupancy multisets require checking over those 12 parameter pairs. This is an exhaustive finite calculation, independently reproducible from the provided program; no random search, black-box solver or unrecorded certificate is needed.

**Why the finite certificate proves the unbounded ranges.** Fix \(s\) and \(E=s-1\), and put \(T=2E+2\). For every \(t\ge T\), any profile of excess \(E\) has at least \(t-2E\ge2\) singleton blocks of type \((0,1)\). No union of two blocks can contain all \(t\) vertices of shore \(B\): the combined large blocks have at most \(2E<t\) vertices, a large block plus a \(B\)-singleton has at most \(2E+1<t\), and two singleton blocks cannot cover \(B\) because \(t\ge6\). Therefore the disjunct \(b=t\) in the domination criterion is *never* decisive for any block or any two-block union. Validity then depends only on the multiset of large-block profiles and the existence (not the number) of singleton blocks of each shore type. The number of \(A\)-singletons is unchanged when \(t\) varies; there are always at least two \(B\)-singletons. Thus a profile is valid at \(t\ge T\) if and only if the same large-block multiset is valid at \(t=T\). This is a bijective stabilization of possible templates, not an extrapolation from finitely many graph orders. The exhaustive checks through \(T\) consequently prove that the table lists **all** possible optimal-partition types for every allowed \(t\).

**Counting labeled realizations.** For any fixed multiset of large-block profiles, let \(m_{a,b}\) be the multiplicity of \((a,b)\), and put \(\alpha=\sum a m_{a,b}\), \(\beta=\sum b m_{a,b}\). Choosing and distributing labeled vertices among these unlabeled blocks gives exactly
\[
 \frac{(s)_{\alpha}(t)_{\beta}}{\displaystyle\prod_{a,b}(a!b!)^{m_{a,b}}m_{a,b}!},
\]
where \((q)_r=q!/(q-r)!\); the remaining vertices are singleton blocks. The formula corrects for indistinguishability of repeated occupancy types and for permutations within each block. For \(s=3\) the single profile contributes \(3t\). For \(s=4\) the two profiles contribute \(4t\) and \(6t\). For \(s=5\), in the table order, the four contributions are
\[
 5t,\qquad10t,\qquad10t,\qquad30t\binom{t-1}{2}.
\]
Their sum is \(25t+15t(t-1)(t-2)\). Every profile is valid by the same coalition test, so these are attained counts, and the exhaustive classification prevents omitted terms or double counting.

## Verification

Run `python3 coalition_template_verifier.py` with Python 3 and the standard library. The program checks the exact list of survivor profiles for 12 finite base parameter pairs and independently computes the labeled realization numbers using factorials; it then checks two further orders per shore size. A separate restricted-growth-string generator enumerates **all labeled vertex partitions**, rather than just occupancy profiles, for \((s,t)=(3,4),(4,5),(5,6)\), giving respectively \(12,50,1950\) optimal partitions. The program prints a `VERIFY_OK` line. The exhaustive base enumeration and the mathematical stabilization lemma jointly support the universal quantifiers; finite test runs alone would not.

## Relationship to prior work

Jafari, Alikhani and Bakhshesh (2024, arXiv:2407.09332v1) introduced the 2-coalition partition and established initial complete-bipartite bounds. Brešar, Henning and Samadi (2025, arXiv:2507.18306v1, Theorem 5.2) **already determine the exact optimal number of blocks** for all complete bipartite graphs, including \(t+1\) here, and explicitly correct an earlier biclique-bound issue. That scalar classification, and its witness constructions, are not presented as new. Their paper does not enumerate all optimal partitions by labeled vertex sets or state the present seven structural profiles and cubic-versus-linear multiplicity transition. The source comparison is about implication: knowing \(C_2(K_{s,t})\) specifies the permitted excess but not how that excess is distributed or the number of maximizing partitions. The present classification supplies that missing information for three natural narrow-shore regimes.

## Limitations

This theorem does not count nonmaximum coalition partitions, does not classify the balanced cases \(t=s\), and does not describe shore sizes \(s\ge6\) or general \(k\)-coalitions. Its novelty is an exact enumerative refinement, not a new formula for the previously known 2-coalition number. Priority remains subject to undiscovered equivalent enumeration results. The 12 finite profile checks are essential finite certificates, and the infinite step is separately proved by a stabilization argument.

## References

1. A. Jafari, S. Alikhani, D. Bakhshesh, *\(k\)-Coalitions in Graphs*, arXiv:2407.09332v1, first posted 2024-07-12. https://arxiv.org/abs/2407.09332
2. B. Brešar, M. A. Henning, B. Samadi, *On \(k\)-coalition in graphs: bounds and exact values*, arXiv:2507.18306v1, first posted 2025-07-24, Theorem 5.2 and proof, pp. 13–15. https://arxiv.org/abs/2507.18306
3. M. A. Henning, D. A. Mojdeh, *Double Coalitions in Graphs*, *Bull. Malays. Math. Sci. Soc.* 48, article 51 (2025), DOI:10.1007/s40840-025-01831-7. The double-coalition notion imposes a different condition on selected vertices and is not conflated with 2-coalition here.
