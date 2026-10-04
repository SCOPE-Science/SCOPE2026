# An exact shared-edge defect identity for finite triangular tilings of convex polygons
## Finding
Let \(P\) be a convex polygon with a finite tiling by nondegenerate triangles. Let \(v_{\mathrm{bd}}\) be the number of tiling vertices on \(\partial P\), let \(v_{\mathrm{int}}\) be the number of tiling vertices in the interior of \(P\), and let \(v_{\mathrm{int}}^*\) be the number of interior vertices that lie in the relative interior of a side of a tile. A *stretch* is a minimal segment that admits two decompositions into tile sides, and its size is the total number of participating tile sides. Let \(q\) be the number of stretches of size \(2\), equivalently the number of geometric tile sides that are full sides of both adjacent triangles. For every stretch \(S\) of size at least \(3\), put \(e(S)=s(S)-3\), and set
\[
E=\sum_{S:\,s(S)\ge 3} e(S).
\]
Then
\[
q=v_{\mathrm{bd}}-3+3\bigl(v_{\mathrm{int}}-v_{\mathrm{int}}^*\bigr)+E.
\]
Consequently,
\[
q\ge v_{\mathrm{bd}}-3.
\]
If \(P\) is a convex \(k\)-gon, then \(v_{\mathrm{bd}}\ge k\), so
\[
q\ge k-3.
\]
The bound is sharp: every ordinary triangulation of a convex \(k\)-gon using only its \(k\) boundary vertices has exactly \(k-3\) interior shared edges. Equality \(q=v_{\mathrm{bd}}-3\) holds exactly when every interior tiling vertex subdivides a tile side and every stretch of size at least \(3\) has size exactly \(3\).

## Assumptions and scope
The tiling is finite, all tiles are nondegenerate Euclidean triangles, their interiors are pairwise disjoint, and their union is the convex polygon \(P\). A geometric segment shared as a full side by two tiles is counted once in \(q\). Convexity is used to ensure that a tile side lying on \(\partial P\) is one of the boundary edge pieces and that boundary sides do not enter an interior stretch.

The notion of stretch and the graph-counting framework are those used by Kupavskii, Pach, and Tardos in their proof that a finite triangular tiling of a convex polygon with more than three sides must contain a shared full side. Their proof treats the case \(q=0\); here size-\(2\) stretches are retained instead of excluded.

## Proof
Form the planar graph \(G\) whose vertices are all tile vertices and whose edges are the maximal subsegments of tile sides containing no other tile vertex. If the tiling has \(t\) triangles, then \(G\) has \(t+1\) faces. Hence Euler's formula gives
\[
e(G)=v_{\mathrm{bd}}+v_{\mathrm{int}}+t-1.
\]
As in the source proof, each interior subdividing vertex lies in the relative interior of precisely one tile side. Double-counting the atomic edges of \(G\) against triangle-side incidences gives
\[
2e(G)=3t+v_{\mathrm{int}}^*+v_{\mathrm{bd}},
\]
and therefore
\[
t+2=v_{\mathrm{bd}}+2v_{\mathrm{int}}-v_{\mathrm{int}}^*.
\tag{1}
\]

Every nonboundary tile side belongs to a unique stretch. Thus, if \(\Sigma\) is the sum of the stretch sizes,
\[
\Sigma=3t-v_{\mathrm{bd}}.
\tag{2}
\]
For a stretch of size \(s\), minimality of the two decompositions implies that its interior breakpoints from the two decompositions are disjoint; hence it contains exactly \(s-2\) subdividing vertices. Each subdividing interior vertex belongs to exactly one stretch. Size-\(2\) stretches contribute no subdividing vertices. Write the remaining stretch sizes as \(3+e_1,\ldots,3+e_p\), where \(e_i\ge0\) and \(E=\sum_i e_i\). Then
\[
v_{\mathrm{int}}^*=p+E
\]
and
\[
\Sigma=2q+3p+E
       =2q+3v_{\mathrm{int}}^*-2E.
\tag{3}
\]
On the other hand, substituting (1) into (2) yields
\[
\Sigma
=3\bigl(v_{\mathrm{bd}}+2v_{\mathrm{int}}-v_{\mathrm{int}}^*-2\bigr)-v_{\mathrm{bd}}
=2v_{\mathrm{bd}}+6v_{\mathrm{int}}-3v_{\mathrm{int}}^*-6.
\tag{4}
\]
Equating (3) and (4) and dividing by \(2\) gives
\[
q=v_{\mathrm{bd}}-3+3\bigl(v_{\mathrm{int}}-v_{\mathrm{int}}^*\bigr)+E.
\]
Since \(v_{\mathrm{int}}^*\le v_{\mathrm{int}}\) and \(E\ge0\), the lower bounds follow. Equality \(q=v_{\mathrm{bd}}-3\) is equivalent to both nonnegative defect terms vanishing.

## Verification
The proof was checked by deriving the identity in two independent countings of \(\Sigma\): one through the planar graph and one through the stretch decomposition. The formula agrees with standard conforming triangulations: for a convex \(k\)-gon triangulated without additional vertices, \(v_{\mathrm{bd}}=k\), \(v_{\mathrm{int}}=v_{\mathrm{int}}^*=E=0\), and \(q=k-3\). It also agrees with a fan from one interior vertex, where \(v_{\mathrm{int}}=1\), \(v_{\mathrm{int}}^*=0\), and the extra \(3\) in the defect identity accounts for the additional full-edge adjacencies.

No computational experiment is used as a substitute for the proof.

## Relationship to prior work
Kupavskii, Pach, and Tardos proved that if \(k\ge4\), every finite triangular tiling of a convex \(k\)-gon contains two triangles sharing a full side. Their proof introduces the same planar graph, the same quantity \(v_{\mathrm{int}}^*\), and stretches; under the contradiction hypothesis that no full side is shared, every stretch has size at least \(3\). The identity above keeps the size-\(2\) stretches rather than excluding them and preserves the exact excess \(s-3\) of longer stretches. It therefore gives a quantitative sharp strengthening \(q\ge k-3\) and an exact defect decomposition, rather than only the existence conclusion \(q\ge1\).

A later paper by the same authors cites the earlier shared-side theorem in its study of plane tilings, and Richter and Wirth cite the existence theorem in their work on incongruent equilateral triangular tilings. The inspected versions of these sources do not state the exact identity or the \(k-3\) lower bound.

## Limitations
The statement is finite and planar. It does not extend verbatim to infinite tilings because Euler counting acquires boundary-at-infinity terms. Convexity is used in the boundary accounting; for nonconvex polygonal regions additional boundary phenomena can occur. The literature comparison covered the primary source, two closely related papers, targeted searches using the terms shared side, stretch, non-edge-to-edge tiling, T-junction, hanging node, and quantitative lower bound, and a semantic index of published findings. This does not logically exclude an unindexed or differently phrased prior occurrence of the same identity.

## References
1. Andrey Kupavskii, János Pach, and Gábor Tardos, *Tilings with noncongruent triangles*, European Journal of Combinatorics 73 (2018), 72–80. arXiv:1711.04504. DOI: 10.1016/j.ejc.2018.05.005.
2. Andrey Kupavskii, János Pach, and Gábor Tardos, *Tilings of the plane with unit area triangles of bounded diameter*, Acta Mathematica Hungarica 155 (2018), 162–173. arXiv:1712.03118.
3. Christian Richter and Melchior Wirth, *Tilings of convex sets by mutually incongruent equilateral triangles contain arbitrarily small tiles*, Discrete & Computational Geometry 63 (2020), 703–721. arXiv:1711.08903. DOI: 10.1007/s00454-019-00061-6.
