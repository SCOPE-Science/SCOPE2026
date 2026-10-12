# Exact color-refinement depth of standard barbell graphs
## Finding
For integers \(m\ge 3\) and \(k\ge 0\), let \(B(m,k)\) be the standard barbell graph consisting of two disjoint copies of \(K_m\), with one distinguished vertex in each clique, and \(k\) additional path vertices inserted between the two distinguished vertices. Thus \(k=0\) means that the distinguished clique vertices are joined directly, and \(|V(B(m,k))|=2m+k\).

Run ordinary color refinement from the uniform coloring, and let \(\operatorname{Stab}(G)\) be the least round \(s\) for which rounds \(s\) and \(s+1\) induce the same vertex partition. Then
\[
\operatorname{Stab}(B(m,k))=
\begin{cases}
\max\{1,\lceil k/2\rceil\},&m\ge4,\\
1,&m=3,\ k=0,\\
2,&m=3,\ k=1,\\
1,&m=3,\ k=2,\\
\max\{3,\lceil k/2\rceil\},&m=3,\ k\ge3.
\end{cases}
\]

There is one further sharp structural exception. The stable color partition equals the automorphism-orbit partition for every \(B(m,k)\) except \(B(3,2)\). In \(B(3,2)\), color refinement stabilizes after one round and merges the four non-distinguished triangle vertices with the two internal path vertices into one six-vertex color class, although the path vertices and triangle vertices lie in different automorphism orbits.

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. The convention for \(B(m,k)\) is the common one in which two equal cliques are joined through a path containing \(k\) vertices outside the cliques; when \(k=0\) the two distinguished clique vertices are adjacent.

In each refinement round, the new color of a vertex is its old color together with the multiset of old colors of its neighbors. Color names themselves are irrelevant; only the induced partition matters.

## Proof
Write \(u\) and \(v\) for the distinguished clique vertices, \(L\) and \(R\) for the sets of the other \(m-1\) clique vertices, and, when \(k\ge1\), write the connecting path as
\[
u-p_1-p_2-\cdots-p_k-v.
\]

Assume first that \(m\ge4\). In round \(1\), the structural types are already separated by degree: \(u,v\) have degree \(m\), vertices of \(L\cup R\) have degree \(m-1\ge3\), and every \(p_i\) has degree \(2\). The two clique ends are symmetric, so \(u,v\) have one common color, and all path vertices initially have one common color.

From round \(2\) onward, refinement on the path is exactly the symmetric inward wave from its two ends. At each strict round one new symmetric pair of path positions peels away from the unresolved middle block. The process stops as soon as the middle block has size at most two, because those one or two positions are already preserved by the reflection exchanging the two cliques. Hence for \(k\ge1\) the stabilization round is \(\lceil k/2\rceil\), with one round still required when \(k=0\). This gives \(\max\{1,\lceil k/2\rceil\}\).

Now let \(m=3\). The four non-distinguished clique vertices have degree \(2\), exactly the same degree as every path vertex. This creates the exceptional cases.

If \(k=0\), round \(1\) separates the two distinguished degree-\(3\) vertices from all four degree-\(2\) clique vertices, and the resulting partition is stable.

If \(k=1\), the sole path vertex \(p_1\) shares the round-\(1\) color of the four ordinary clique vertices. In round \(2\), however, \(p_1\) sees two distinguished vertices, while each ordinary clique vertex sees one distinguished vertex and one ordinary clique vertex. Thus \(p_1\) splits off, and the coloring is stable.

If \(k=2\), the two path vertices and the four ordinary clique vertices all have degree \(2\). Every one of these six vertices has, after round \(1\), one neighbor in the distinguished-vertex color class and one neighbor in its own degree-\(2\) color class. Therefore the degree partition is already equitable and color refinement stabilizes after one round. Yet a path vertex lies in no triangle, while every ordinary clique vertex lies in a triangle, so these vertices cannot be automorphic.

Finally suppose \(k\ge3\). In round \(1\), all degree-\(2\) vertices are merged. In round \(2\), the four ordinary clique vertices and the endpoint path vertices \(p_1,p_k\) remain together, because each sees one distinguished vertex and one degree-\(2\) vertex; the deeper path vertices form the other degree-\(2\) color class. In round \(3\), \(p_1,p_k\) separate from the ordinary clique vertices, since their non-distinguished neighbor now has the deeper-path color rather than the ordinary-clique color. Simultaneously the usual symmetric path wave reaches the second path layer. From this point on, the same inward-wave induction as for \(m\ge4\) applies. Thus stabilization cannot occur before round \(3\), and the path itself requires exactly \(\lceil k/2\rceil\) rounds when this is larger. Hence
\[
\operatorname{Stab}(B(3,k))=\max\{3,\lceil k/2\rceil\}
\]
for \(k\ge3\).

Outside \(B(3,2)\), the final color classes are exactly the obvious symmetry classes: the pair \(\{u,v\}\), the set \(L\cup R\), and the symmetric path-position pairs, with a singleton middle path vertex when \(k\) is odd. Each is an automorphism orbit under the reflection exchanging the two cliques together with arbitrary permutations inside each clique. Hence the stable partition equals the orbit partition in all remaining cases.

## Verification
The accompanying standalone program `verify.py` implements color refinement directly, with no graph-library dependency. It verifies the depth formula for every
\[
3\le m\le20,\qquad 0\le k\le80,
\]
and separately checks the exceptional six-vertex stable color cell in \(B(3,2)\). It returns:

`VERIFY_OK depth_checks=1458 anomaly_checks=1 m=3..20 k=0..80`

The computation is a finite consistency check. The all-parameter result rests on the proof above.

## Relationship to prior work
Krebs and Verbitsky formalize the stabilization parameter for color refinement and prove the correspondence between refinement rounds and truncated universal-cover types. Their result supplies the general local-propagation framework used here, but does not state an exact formula for barbell graphs. The same paper traces the counting-game connection back to Immerman and Lander's finite-model-theoretic treatment of graph canonization.

Barbell graphs are a standard named family consisting of two complete graphs connected through a path. Targeted searches for barbell graphs together with color refinement, \(1\)-WL, Weisfeiler--Leman iteration number, stabilization depth, equitable partitions, and the exceptional \(B(3,2)\) orbit phenomenon did not locate this formula.

The result complements general extremal work on color-refinement iteration counts by giving a closed form on a natural family and isolating a singular case where the stable equitable partition is strictly coarser than the automorphism-orbit partition.

## Limitations
The theorem concerns two equal cliques. Unequal clique sizes, multiple parallel connecting paths, arbitrary initial colors, higher-dimensional Weisfeiler--Leman refinement, and graph-pair distinguishing depth are not covered. The literature search was targeted rather than exhaustive, so an unindexed family-specific calculation remains a residual priority risk.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
2. N. Immerman and E. Lander, *Describing Graphs: A First-Order Approach to Graph Canonization*, in *Complexity Theory Retrospective*, 1990, DOI: 10.1007/978-1-4612-4478-3_5.
3. E. W. Weisstein, *Barbell Graph*, MathWorld; and the NetworkX documentation for `barbell_graph`, for the standard equal-clique/path convention.
