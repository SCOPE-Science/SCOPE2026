# Exact color-refinement depth of asymmetric double Bethe trees
## Finding
Fix an integer \(d\ge2\). Let \(D_d(a,b)\) be the tree obtained by taking two perfect rooted \(d\)-ary trees of edge-heights \(a,b\ge1\) and joining their roots by one edge. Put
\[
m=\min\{a,b\},\qquad M=\max\{a,b\}.
\]
For ordinary color refinement from the uniform coloring, let \(\operatorname{Stab}(G)\) be the least round whose induced vertex partition is stable. Then
\[
\operatorname{Stab}(D_d(a,b))=
\begin{cases}
m,&M=m,\\[1mm]
M,&M=m+1,\\[1mm]
\max\!\left\{2m+3,\left\lfloor\frac{m+M+2}{2}\right\rfloor\right\},&M\ge m+2.
\end{cases}
\]
The value is independent of the branching factor \(d\) as soon as \(d\ge2\).

Moreover, in every case the stable color partition is exactly the automorphism-orbit partition.

The third regime has two simultaneous refinement clocks. A defect caused by the unequal halves first appears at the central core and then needs \(m+1\) further rounds to propagate back through the shorter half, producing the term \(2m+3\). Independently, the unresolved core of the taller half is refined from both ends, producing \(\lfloor(m+M+2)/2\rfloor\).

## Assumptions and scope
Graphs are finite, simple, undirected, and initially uncolored. A perfect rooted \(d\)-ary tree of edge-height \(h\) has one root, every nonleaf vertex has exactly \(d\) children, and every leaf is at distance \(h\) from the root. The two roots in \(D_d(a,b)\) remain distinct and are connected by a new edge.

Round \(0\) is the uniform coloring. Each later round replaces a vertex color by its old color together with the multiset of old colors on its neighbors. Stabilization concerns the induced partition rather than literal color names.

For each half, index levels by distance from its leaves: \(A_0,\ldots,A_a\) and \(B_0,\ldots,B_b\), with \(A_a,B_b\) the two joined roots. Vertices in one such level are automorphic.

## Proof
Color refinement respects these level classes, and the quotient dynamics are exact. In the \(A\)-half, every representative of \(A_i\), \(0<i<a\), sees \(d\) neighbors in \(A_{i-1}\) and one in \(A_{i+1}\); \(A_0\) has one neighbor in \(A_1\); and \(A_a\) sees \(d\) neighbors in \(A_{a-1}\) and one in \(B_b\). The \(B\)-half is symmetric. Thus the whole refinement process reduces to a weighted path, with the multiplicity \(d\) marking the direction toward the leaves.

Assume \(a\le b\). If \(a=b\), the weighted path is symmetric about its central edge. Each round exposes one new leaf-distance layer from both ends, and after round \(a\) no further split is possible. Hence \(\operatorname{Stab}=a\). The stable classes are \(A_i\cup B_i\), exactly the orbits under the automorphism swapping the two halves.

If \(b=a+1\), the root \(B_b\) of the taller half is the unique center of the unrooted tree. Its \(d\) ordinary child branches and the branch through \(A_a\) are all perfect \(d\)-ary trees of height \(a\). Therefore \(D_d(a,a+1)\) is the radius-\(a+1\) ball in the infinite \((d+1)\)-regular tree. Refinement peels one distance layer from the leaves in every round and stabilizes exactly at the center in round \(a+1=b\). The stable classes are the distance spheres about \(B_b\), which are the automorphism orbits.

Now suppose \(b\ge a+2\). A direct induction on the weighted path shows that after round \(a+1\) the partition consists of
\[
P_i=A_i\cup B_i\quad(0\le i\le a)
\]
together with one unresolved core
\[
C=\{B_{a+1},B_{a+2},\ldots,B_b\}.
\]
Indeed, through round \(a+1\) refinement has only propagated inward from the two leaf boundaries, so equal leaf-distance layers remain paired.

At round \(a+2\), the two endpoints \(B_{a+1}\) and \(B_b\) of \(C\) receive different colors. Both are adjacent to the paired class \(P_a\), but \(B_{a+1}\) has \(d\) neighbors toward \(P_a\), whereas \(B_b\) has only one neighbor toward \(P_a\). This is where the assumption \(d\ge2\) is used.

Write \(L=b-a\), so \(C\) has \(L\) vertices. Once its two endpoint colors differ, refinement propagates inward from both ends of this path one layer per round. Consequently the entire core becomes discrete, at the level-class scale, exactly by
\[
T_{\rm core}=a+1+\left\lfloor\frac{L}{2}\right\rfloor
=\left\lfloor\frac{a+b+2}{2}\right\rfloor.
\]

In parallel, the unequal endpoint colors of \(C\) split the two members of \(P_a\) in round \(a+3\). That split then propagates outward through the paired classes one per round:
\[
P_a,\ P_{a-1},\ldots,P_0.
\]
The last paired class \(P_0\) therefore splits in round
\[
T_{\rm pair}=2a+3.
\]
Both displayed times are genuine strict-split times whenever they dominate, and after both processes finish every level class on both halves is distinct. Thus
\[
\operatorname{Stab}(D_d(a,b))
=\max\{T_{\rm pair},T_{\rm core}\}
=\max\!\left\{2a+3,\left\lfloor\frac{a+b+2}{2}\right\rfloor\right\}.
\]

Finally, when \(b\ge a+2\), automorphisms cannot interchange the unequal halves, while the rooted automorphism group of a perfect \(d\)-ary tree is transitive on every level. Hence each \(A_i\) and each \(B_j\) is one orbit, exactly matching the stable partition. The equal and adjacent cases were identified above, proving refinability in all regimes.

## Verification
The accompanying standalone program `verify.py` implements the exact weighted quotient recurrence and also constructs full graphs for an independent small-parameter check. It verifies the stated depth formula for every
\[
2\le d\le5,\qquad 1\le a,b\le25,
\]
and compares full-graph stable partitions with the explicit orbit partitions for \(d\in\{2,3\}\) and \(1\le a,b\le4\).

It returns:

`VERIFY_OK quotient_depth_checks=2500 full_graph_checks=32 orbit_checks=32 d=2..5 a,b=1..25; full d=2,3 a,b=1..4`

The finite computation is corroborative only. The theorem for all parameters rests on the weighted-path proof above.

## Relationship to prior work
Krebs and Verbitsky formalize color-refinement stabilization and relate refinement rounds to truncated universal covers. Their framework explains why refinement on a tree is a local propagation process, but it does not give the double-Bethe formula above.

Bethe and generalized Bethe trees are standard rooted families in the spectral graph literature. Rojo and Medina study Bethe trees, while later generalized-Bethe work studies constructions made from rooted copies, including root-joining operations. Those sources concern spectra rather than color-refinement iteration depth.

The formula here differs sharply from the previously analyzed spider-tree situation: the two roots of \(D_d(a,b)\) have the same degree as all other internal vertices, so the joining edge is initially invisible to degree refinement. This produces the three-regime law and, for a height gap of at least two, the delayed \(2m+3\) defect-propagation term.

Targeted searches for double Bethe trees, joined perfect \(d\)-ary trees, color refinement, equitable partitions, \(1\)-WL, Weisfeiler--Leman stabilization, and orbit partitions did not locate an equivalent exact formula.

## Limitations
The theorem assumes equal branching factor \(d\ge2\) on the two perfect halves. It does not treat generalized Bethe trees with level-dependent branching, unequal branching factors, more than two root-joined components, higher-dimensional Weisfeiler--Leman refinement, or graph-pair distinguishing depth. The terminology “asymmetric double Bethe tree” is descriptive; the literature more often studies equal-height or generalized constructions. The literature search was targeted rather than exhaustive, and no independent audit has been performed.

## References
1. A. Krebs and O. Verbitsky, *Universal covers, color refinement, and two-variable counting logic: Lower bounds for the depth*, arXiv:1407.3175, first posted 11 July 2014.
2. O. Rojo and L. Medina, *Tight bounds on the algebraic connectivity of Bethe trees*, Linear Algebra and its Applications 418 (2006).
3. O. Rojo, *The spectra of a graph obtained from copies of a generalized Bethe tree*, Linear Algebra and its Applications 420 (2007), DOI: 10.1016/j.laa.2006.08.006.
