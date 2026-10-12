# A double-spider family with color-refinement depth one below its diameter
## Finding
For every integer \(a\ge1\), let \(T_a\) be the tree with adjacent degree-three vertices \(x,y\), where \(x\) has two pendant arms \(A,B\) of length \(a\), while \(y\) has pendant arms \(C,D\) of lengths \(a\) and \(a+1\). Arm lengths are measured in edges from the corresponding center to the leaf. Then \(|V(T_a)|=4a+3\), \(\operatorname{diam}(T_a)=2a+2\), and ordinary color refinement from the uniform coloring has exact stabilization depth
\[
\operatorname{Stab}(T_a)=2a+1=\operatorname{diam}(T_a)-1=\frac{|V(T_a)|-1}2.
\]
Thus even on trees, color refinement may require almost the full diameter, and the excess over the radius is unbounded:
\[
\operatorname{Stab}(T_a)-\operatorname{rad}(T_a)=a.
\]

More precisely, write \(A_i,B_i,C_i\) for the vertices at distance \(i\) from their center on the three length-\(a\) arms and \(D_j\) for the vertices at distance \(j\) from \(y\) on the length-\(a+1\) arm. After round \(a+1\), the color classes are exactly
\[
\{x\},\quad \{y\},\quad \{A_i,B_i,C_i\}\ (1\le i\le a),\quad \{D_j\}\ (1\le j\le a+1).
\]
For \(1\le k\le a\), after round \(a+1+k\), the triples with \(i\le k\) have split into \(\{A_i,B_i\}\) and \(\{C_i\}\), while every triple with \(i>k\) is still intact. Hence the final strict split occurs in round \(2a+1\).

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. Round \(0\) is the uniform coloring. In every subsequent round a vertex is recolored by its previous color together with the multiset of previous colors of its neighbors. The stabilization depth is the least \(s\) for which rounds \(s\) and \(s+1\) induce the same vertex partition.

The family \(T_a\) is a double-spider tree: deleting the central edge \(xy\) leaves two subdivided stars. The statement concerns stabilization on a single tree, not graph-pair distinguishing depth.

## Proof
Krebs and Verbitsky prove that after \(r\) rounds, two vertices have the same color exactly when their rooted universal covers truncated at depth \(r\) are isomorphic. For a tree, the universal cover is the tree itself, so the color is exactly the isomorphism type of the rooted depth-\(r\) truncation.

First consider the two centers. Through depth \(a\), the rooted truncations at \(x\) and \(y\) are isomorphic. Each center has two branches that are simple paths of visible length \(a\), and a third branch through the other center; at depth at most \(a\), the extra edge at the end of the \(D\)-arm is not yet visible from the root in a way that breaks this correspondence. At depth \(a+1\), the \(D\)-arm reaches one level farther from \(y\) than either length-\(a\) arm does from \(x\), so the rooted truncations differ. Hence \(x\) and \(y\) split exactly in round \(a+1\).

At that same round, every vertex \(D_j\) has a unique color. Indeed, before the centers split, the degree-one leaf color and the common degree-three center color propagate inward from the two ends of the \(D\)-arm. By round \(a+1\), every position on this path has seen both endpoint types, and its ordered pair of distances \((j,a+1-j)\) is unique. On each of the three length-\(a\) arms, the corresponding positions \(A_i,B_i,C_i\) have identical rooted truncations through round \(a+1\): the three arms have the same length, and from position \(i\) only depth \(a+1-i\le a\) remains after reaching its center, while the two center truncations agree through depth \(a\). Thus the displayed round-\(a+1\) partition is exact.

Now the split propagates from the centers down the three equal-length arms. In round \(a+2\), \(C_1\) sees the color of \(y\), whereas \(A_1,B_1\) see the color of \(x\), so \(C_1\) separates from \(A_1,B_1\). Inductively, suppose that after round \(a+1+k\), all positions up to \(k\) have the asserted split and positions farther out remain triples. Then in the next round \(C_{k+1}\) sees the already distinguished color of \(C_k\), while \(A_{k+1},B_{k+1}\) see the common color of \(A_k,B_k\). Hence the next triple splits. No farther triple can split in that round because both of its neighbors still have matching colors in the three arms. This proves the round-by-round statement.

At round \(2a+1\), every \(C_i\) has separated from \(A_i,B_i\). The remaining pairs \(A_i,B_i\) are exchanged by the automorphism swapping the two arms at \(x\), while every other displayed class is a singleton. Therefore the coloring has reached the orbit partition and is stable. At round \(2a\), the last triple \(\{A_a,B_a,C_a\}\) is still unsplit, so stabilization cannot occur earlier. Thus \(\operatorname{Stab}(T_a)=2a+1\).

## Verification
The accompanying standalone checker directly implements color refinement. For every \(1\le a\le100\), it verifies the exact depth \(2a+1\), the complete partition at round \(a+1\), and every subsequent partition through stabilization. It returns:

`VERIFY_OK depth_checks=100 partition_checks=5150 a=1..100`

This finite computation is a consistency check; the proof above is uniform for all \(a\ge1\).

## Relationship to prior work
Krebs and Verbitsky introduced the stabilization parameter \(\operatorname{Stab}(G)\) in this setting and proved the exact correspondence between round colors and truncated rooted universal covers. Their 2014 preprint also shows that general graphs can require \((1-o(1))n\) rounds. The construction above uses their local interpretation to isolate a tree-specific mechanism: a one-edge arm imbalance first separates the two adjacent degree-three centers and then forces a second propagation phase along the equal arms.

Targeted searches for double-spider trees, tree-specific iteration numbers, and path-extremal color-refinement bounds did not locate this family or the exact law \(\operatorname{Stab}(T_a)=\operatorname{diam}(T_a)-1\). Later work of Kiefer and McKay proves that arbitrary graphs can require \(n-1\) rounds but does not state a tree-family result of this form in the inspected material.

## Limitations
The theorem gives an explicit infinite family and not an extremal theorem over all trees of a fixed order or diameter. In particular, it does not claim that \(\operatorname{diam}(T)-1\) is a universal upper bound for trees. The literature search was targeted rather than exhaustive, so an unindexed tree-specific occurrence remains a priority risk.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014; LICS 2015, DOI: 10.1109/LICS.2015.69.
2. S. Kiefer and B. D. McKay, *The Iteration Number of Colour Refinement*, arXiv:2005.10182; ICALP 2020, DOI: 10.4230/LIPIcs.ICALP.2020.73.
