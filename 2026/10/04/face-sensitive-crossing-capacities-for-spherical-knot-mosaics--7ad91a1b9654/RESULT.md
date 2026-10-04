# Face-sensitive crossing capacities for spherical knot mosaics
## Finding
For a spherical knot \(n\)-mosaic with \(n\ge 2\), let its face support be the set of cube faces containing at least one non-empty tile. If the support has exactly \(f\) faces, then the number of crossing tiles is bounded by
\[
B_1=(n-2)^2,\quad
B_2=2(n-1)(n-2),\quad
B_3=3(n-1)^2,\quad
B_4=2(n-1)(2n-1),\quad
B_5=5n^2-4n
\]
for \(f=1,2,3,4,5\), respectively. For each of these five support sizes, \(B_f\) is the exact maximum number of tile positions that can carry crossing tiles while respecting only the requirement that no connection point may run from a non-empty face into an empty face.

Combining these bounds with the published six-face knot bound
\[
B_6=6n^2-3n+1
\]
gives, for every knot \(K\) admitting a spherical \(n\)-mosaic,
\[
sf_n(K)\ge \min\{f\in\{1,2,3,4,5,6\}:c(K)\le B_f(n)\}.
\]
At \(n=2\), the resulting capacity sequence is \((0,0,3,6,12,19)\). Thus any nontrivial crossing knot on a spherical \(2\)-mosaic uses at least three faces; crossing number at least \(4\), \(7\), or \(13\) forces at least four, five, or six non-empty faces, respectively.

## Assumptions and scope
A crossing tile means one of the two standard mosaic tiles with four connection points and an over/under crossing. The face support counts a cube face as non-empty exactly when it contains at least one non-empty mosaic tile. The five formulas above are positional capacities: they are sharp for the local empty-face boundary constraint, but they are not asserted to be sharp crossing numbers of one-component knot mosaics for every \((n,f)\). Global connectivity can lower the realizable knot maximum; the published six-face theorem is an example.

The statement concerns the spherical/cubic mosaic model with the standard eleven-tile set. Its primary subject is geometric topology, MSC \(57K10\).

## Proof
A crossing tile has a connection point on each of its four sides. Therefore, if a side of a selected cube face borders an empty neighboring face, no crossing tile can occupy a tile position touching that side: such a tile would have an unmatched connection point across the cube edge.

For one selected face, all four neighboring faces are empty. Only the interior \((n-2)\times(n-2)\) positions can be crossings, giving \(B_1=(n-2)^2\).

For two selected faces, the maximum occurs when they are adjacent. Each then has three forbidden boundary sides, leaving \((n-1)(n-2)\) admissible crossing positions per face. Hence \(B_2=2(n-1)(n-2)\). An opposite pair gives only \(2(n-2)^2\).

For three selected faces there are two cube-symmetry types. If the three faces meet at a cube vertex, each face has two adjacent forbidden sides and contributes \((n-1)^2\), for \(B_3=3(n-1)^2\). If the support consists of an opposite pair plus a third face, the capacity is \((n-2)(3n-2)\), smaller by \(2n-1\).

For four selected faces, classify by the two omitted faces. If the omitted faces are adjacent, two selected faces have one forbidden side and two have two adjacent forbidden sides. The capacity is
\[
2n(n-1)+2(n-1)^2=2(n-1)(2n-1)=B_4.
\]
If the omitted faces are opposite, every selected face has two opposite forbidden sides, giving \(4n(n-2)\), which is smaller by \(2(n+1)\).

For five selected faces, let \(F\) be the omitted face. The selected face opposite \(F\) has no forbidden sides and contributes \(n^2\). The other four selected faces each have one forbidden side and contribute \(n(n-1)\). Thus
\[
B_5=n^2+4n(n-1)=5n^2-4n.
\]

The published six-face theorem gives at most \(B_6=6n^2-3n+1\) crossing tiles for a spherical knot \(n\)-mosaic. Since any particular diagram has at least the knot crossing number \(c(K)\) crossings, a representation on exactly \(f\) non-empty faces requires \(c(K)\le B_f(n)\). Minimizing over feasible support sizes proves the lower bound for \(sf_n(K)\).

## Verification
A standalone exact enumerator represents the six cube faces and all face-adjacency cycles, enumerates every nonempty proper support among the six faces, counts positions avoiding sides incident to empty faces, and compares the maxima with the five symbolic formulas. It checks all \(62\) nonempty proper supports for each \(n\) from \(2\) through \(100\). The replay reports:

`VERIFY_OK n=2..100; all 62 nonempty proper face supports enumerated per n; formulas B1..B5 exact as positional capacities`

This finite replay checks the combinatorial case formulas over a broad range. The proof above, rather than the finite computation, establishes the formulas for all \(n\ge2\).

## Relationship to prior work
Nagasawa-Hinck and Wood introduced spherical knot mosaics and the spherical \(n\)-mosaic face number \(sf_n(K)\), and proved the global six-face crossing-tile maximum \(6n^2-3n+1\). Their paper explicitly identifies face-count invariants and crossing-number bounds as central objects, but the inspected definitions and bounds do not give support-size-sensitive crossing capacities for \(f<6\).

Howards, Li, and Liu give sharp crossing-number bounds for ordinary rectangular mosaics. Those results show in particular why the one-face formula here should be read as a positional capacity rather than a sharp knot-specific crossing maximum: global planar-mosaic connectivity can impose stronger restrictions. Their rectangular result does not classify supports across multiple cube faces.

A 2025 paper titled *Cubic knot mosaics* is cited by the spherical-mosaic paper as prior work on the equivalent cube-surface framework. Its full text was not available for complete comparison in this review. Available metadata and the later spherical-mosaic paper establish the model relationship, but this leaves a residual literature risk concerning whether an equivalent support-sensitive formula appears there.

## Limitations
The formulas \(B_1,\ldots,B_5\) are exact for the stated local boundary constraint, not asserted exact maxima over realizable one-component knot mosaics. They therefore provide necessary conditions and lower bounds for \(sf_n(K)\), not a complete classification of that invariant. The originality comparison is strongest against the fully inspected recent spherical-mosaic paper and the accessible rectangular-mosaic literature; the inaccessible full text of *Cubic knot mosaics* remains a named residual risk.

## References
1. Ally Nagasawa-Hinck and Peyton Phinehas Wood, *Spherical Knot Mosaics*, arXiv:2510.26469v2, first submitted 2025-10-30, MSC 57K10, https://arxiv.org/abs/2510.26469.
2. Hugh Howards, Jiong Li, and Xiaotian Liu, *Bounding Crossing Number in Rectangular and Hexagonal Knot Mosaics*, arXiv:2410.19570, first submitted 2024-10-25, https://arxiv.org/abs/2410.19570.
3. Samantha Pezzimenti, Trevor Meintel, and Aaron Shabon, *Cubic knot mosaics*, Involve 18 (2025), no. 4, 629–642, DOI:10.2140/involve.2025.18.629.
