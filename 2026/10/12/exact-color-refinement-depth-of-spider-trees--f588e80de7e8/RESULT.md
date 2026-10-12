# Exact color-refinement depth of spider trees
## Finding
Let \(d\ge 3\) and let \(S(L_1,\ldots,L_d)\) be a spider tree with one center and \(d\) legs of positive integer edge-lengths \(L_1,\ldots,L_d\). Let
\[
\lambda_1<\cdots<\lambda_s
\]
be the distinct leg lengths. Start ordinary vertex color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least round \(r\) such that round \(r+1\) induces the same vertex partition as round \(r\).

Then
\[
\operatorname{Stab}(S(L_1,\ldots,L_d))=
\begin{cases}
\left\lceil \lambda_s/2\right\rceil,&s=1,\\[1mm]
\max\!\left\{\left\lceil \lambda_s/2\right\rceil,\lambda_{s-1}+1\right\},&s\ge2.
\end{cases}
\]

Thus arbitrary multiplicities of intermediate leg lengths do not affect the depth beyond two statistics: the longest leg and the second-largest distinct leg length.

There is also a sharp fixed-order consequence. Among all \(d\)-leg spiders on \(N\ge d+1\) vertices,
\[
\max \operatorname{Stab}=\left\lfloor\frac{N-d}{2}\right\rfloor+1.
\]

## Assumptions and scope
All graphs are finite, simple, undirected, and initially uncolored. A spider tree here has exactly one vertex of degree at least \(3\), called the center, and every component left after deleting the center is a path. The length \(L_i\) of a leg is the number of edges from the center to its leaf, so each \(L_i\ge1\).

Round \(0\) is the uniform coloring. Each subsequent color consists of the previous color together with the multiset of previous colors on neighboring vertices. Stabilization concerns the induced partition, so irrelevant renaming of colors is ignored.

For a noncentral vertex on a leg of length \(L\), write \(x\) for its distance from the center. A leaf has \(x=L\); an internal vertex has \(1\le x\le L-1\).

## Proof
Because \(d\ge3\), the center, leaves, and internal leg vertices have degrees \(d\), \(1\), and \(2\), respectively. Hence round \(1\) separates these three vertex types.

For every round \(r\ge1\), define typed descriptors as follows:
\[
\delta_r(c)=(\mathrm{center}),
\]
for the center \(c\);
\[
\delta_r(v)=(\mathrm{leaf},\min\{L,r\})
\]
for the leaf of a leg of length \(L\); and
\[
\delta_r(v)=
(\mathrm{internal},\min\{x,r\},\min\{L-x,r\})
\]
for an internal vertex at center-distance \(x\) on a leg of length \(L\).

We claim that two vertices have the same color after round \(r\) exactly when their typed descriptors \(\delta_r\) are equal. The statement is true for \(r=1\) by the degree partition. For the inductive step, an internal leg vertex has one neighbor toward the center and one toward the leaf. Since the center type and leaf type were already separated in round \(1\), the two directions are ordered rather than interchangeable. One refinement step therefore increases by one the amount of visible distance toward each end, with distances already below the current radius remaining exact. This converts the two clipped coordinates at radius \(r\) into those at radius \(r+1\). The same one-sided propagation argument gives the leaf descriptor. Thus the descriptor characterization follows by induction.

It remains to determine when the descriptor partition stops splitting. Fix a leg length \(L\). Among its internal positions \(1,\ldots,L-1\), the ordered clipped pairs
\[
(\min\{x,r\},\min\{L-x,r\})
\]
become pairwise distinct exactly at
\[
r=\left\lceil\frac L2\right\rceil.
\]
Before that round, the unresolved middle interval contains at least two positions with descriptor \((r,r)\); at that round no two distinct positions remain clipped in both coordinates. Therefore within-leg refinement contributes the term \(\lceil\lambda_s/2\rceil\).

Now compare two distinct leg lengths \(L<M\). Their leaves have equal descriptors through round \(L\), because both are labeled \((\mathrm{leaf},r)\) there. In round \(L+1\), the shorter leaf has descriptor \((\mathrm{leaf},L)\) while the longer has \((\mathrm{leaf},L+1)\), so the two leaf classes split exactly then. Hence the last possible split between different leg lengths occurs at
\[
\lambda_{s-1}+1,
\]
where \(\lambda_{s-1}\) is the second-largest distinct length.

Internal vertices from different leg lengths never require a later round than this. Once radius \(r\ge L\) reaches the full shorter leg, every internal descriptor on that leg is untruncated and its two numerical coordinates sum to \(L\). An equal descriptor from a longer leg would have to have the same two coordinates, hence the same sum, contradicting the longer total length. Thus all cross-length internal collisions have disappeared by round \(L\), one round before the corresponding leaves necessarily split.

Taking the maximum of the within-longest-leg threshold and the last cross-length leaf split proves the formula.

For the fixed-order extremal statement, put
\[
T=N-1=\sum_{i=1}^d L_i.
\]
The longest length satisfies \(L_{\max}\le N-d\), so
\[
\left\lceil L_{\max}/2\right\rceil
\le
\left\lfloor\frac{N-d}{2}\right\rfloor+1.
\]
If at least two distinct lengths occur and \(S\) is the second-largest distinct length, then one leg has length at least \(S+1\), one has length \(S\), and the remaining \(d-2\) legs have length at least \(1\). Therefore
\[
N-1\ge (S+1)+S+(d-2)=2S+d-1,
\]
so
\[
S+1\le \left\lfloor\frac{N-d}{2}\right\rfloor+1.
\]
This proves the upper bound.

It is attained. If \(N=d+1\), all legs have length \(1\) and the depth is \(1\). Otherwise, write \(N-d=2q\) or \(2q+1\). In the even case, the leg multiset
\[
\{1^{\,d-2},q,q+1\}
\]
has order \(N\) and depth \(q+1\). In the odd case with \(q\ge1\), the multiset
\[
\{1^{\,d-2},q,q+2\}
\]
has order \(N\) and depth \(q+1\). This proves sharpness.

## Verification
The accompanying standalone checker constructs spiders directly and implements ordinary color refinement without external graph libraries.

It verifies the exact depth formula for every nondecreasing leg-length tuple with \(3\) through \(6\) legs and every leg length from \(1\) through \(10\), totaling \(7942\) spiders. On every one of these graphs it also compares each nonstable refinement round with the typed descriptor partition, for \(57570\) round-level checks.

Separately, it exhaustively verifies the fixed-order extremal formula for \(d=3,4,5\) over \(54\) order/leg-count pairs.

The checker returns:

`VERIFY_OK depth_checks=7942 descriptor_round_checks=57570 extremal_checks=54`

The finite computation is corroborative only. The theorem for all parameters rests on the proof above.

## Relationship to prior work
Bahls, Lake, and Wertheim use the standard spider-tree definition and study graceful labelings. Their paper defines a spider as a tree with at most one branch point and calls the center-to-leaf paths its legs. Their results concern graceful labeling, not color refinement.

Krebs and Verbitsky study color-refinement stabilization and its connection with rooted universal covers and two-variable counting logic. Their work supplies the general finite-model-theoretic setting for refinement depth but does not state a spider-family formula.

A prior calculation covers only the almost-equilateral subfamily in which all but one leg have one common length. Substituting that two-length pattern into the present formula recovers the earlier value. The new theorem is not a reparameterization of that special case: it allows an arbitrary multiset of leg lengths and proves that every intermediate multiplicity disappears from the final depth except through the second-largest distinct length. The fixed-order extremal law is also new relative to that restricted calculation.

Targeted published-finding corpus and web searches using the aliases spider tree, starlike tree, subdivided star, and generalized star together with color refinement, \(1\)-WL, Weisfeiler--Leman, equitable partitions, stabilization depth, and arm lengths did not locate an equivalent exact formula.

## Limitations
The theorem concerns ordinary one-dimensional color refinement from the uniform coloring. It assumes a genuine spider with at least three legs; paths are excluded. It does not cover trees with two or more branch points, higher-dimensional Weisfeiler--Leman refinement, or graph-pair distinguishing depth.

The finite checker covers a broad but finite parameter range and is not an exhaustive proof of the infinite statement. The literature search was targeted rather than exhaustive, so an unindexed family-specific occurrence remains a residual priority risk.

## References
1. P. Bahls, S. Lake, and A. Wertheim, *Gracefulness of families of spiders*, Involve 3(3) (2010), 241--247, DOI: 10.2140/involve.2010.3.241.
2. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
