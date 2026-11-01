# Integral persistence phase diagram for height-deformed hexagonal antiprisms

## Finding
Let \(t>0\). Take twelve Euclidean points in two horizontal rings of circumradius one: the upper six at angles \(j\pi/3\), the lower six at angles \(j\pi/3+\pi/6\), with vertical separation \(\sqrt t\), where \(j=0,\ldots,5\). Let \(K_r(t)\) be the inclusive Euclidean Vietoris–Rips complex: a finite vertex set spans a simplex if all its pairwise distances are at most \(r\). All reduced homology below uses integral coefficients.

Write
\[
 A=\sqrt{t+2-\sqrt3},\qquad B=\sqrt{t+2},\qquad C=\sqrt{t+2+\sqrt3},\qquad
 a=2-\sqrt3,\quad b=\sqrt3-1.
\]
An interval \([u,v)\) below is omitted when \(u=v\); multiplicities are specified. **The entire reduced integral persistence barcode**, for all \(t>0\), is:

* **Degree zero.** For \(0<t\le b\): eleven \([0,A)\). For \(t>b\): ten \([0,1)\) and one \([0,A)\).
* **Degree one.** For \(0<t\le b\): one \([A,\sqrt3)\). For \(t>b\): one \([1,\min(A,\sqrt3))\) and one \([1,\sqrt3)\).
* **Degree two.** For \(0<t<a\): three \([\sqrt3,C)\). For \(a\le t\le2\): three \([\sqrt3,2)\). For \(t>2\): two \([\sqrt3,2)\) and one \([\max(\sqrt3,A),B)\).
* **Degree three.** For \(t>a\): two \([\max(2,B),C)\); otherwise none.
* **Degree five.** For \(0<t<a\): one \([C,2)\); otherwise none.

All other positive degrees have no bars. Every group is free abelian, and all nonzero persistence maps have primitive images. In particular, crossing the exact height parameter \(t=2-\sqrt3\) exchanges a degree-five terminal phase for a two-dimensional degree-three homology phase. There are six geometric ordering walls \(2-\sqrt3,\sqrt3-1,1,2,1+\sqrt3,2+\sqrt3\), and the formulas also hold exactly on all walls.

## Assumptions and scope
The horizontal radius is exactly one, the relative angular twist is exactly \(\pi/6\), and \(t\) denotes the *squared* ring separation, not the height. Thresholds are inclusive; an interval ends at its death threshold. The theorem covers all real \(t>0\) and all \(r\ge0\). It does not claim a classification of other twists, radii, or continuous antiprism surfaces.

Interleave the vertices in angular order as \(v_0,\ldots,v_{11}\), with the even indices in the upper ring. For two vertices of circular index gap \(\delta=\min(|i-j|,12-|i-j|)\), the exact squared-distance table is

| Gap \(\delta\) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|
| Squared distance | \(t+2-\sqrt3\) | \(1\) | \(t+2\) | \(3\) | \(t+2+\sqrt3\) | \(4\) |

Call these six distance classes O1, E2, O3, E4, O5, E6 respectively. The table gives the *full* complex at every real parameter pair without approximation or tie-breaking. The following list exhausts the possible sets of classes present as \(r\) increases (including equal-distance walls):

| Distance classes present | Homotopy type |
|---|---|
| none | twelve discrete points |
| O1 | \(S^1\) |
| E2 | \(S^1\sqcup S^1\) |
| E2,E4 | \(S^2\sqcup S^2\) |
| E2,O1 | \(S^1\) |
| E2,E4,E6 | two contractible components |
| E2,E4,O1 | \(\bigvee^3 S^2\) |
| E2,O1,O3 | \(S^1\) |
| E2,E4,E6,O1 | \(S^2\) |
| E2,E4,O1,O3 | \(\bigvee^3 S^2\) |
| E2,E4,E6,O1,O3 | \(\bigvee^2 S^3\) |
| E2,E4,O1,O3,O5 | \(S^5\) |
| all six classes | a point |

The table is a homotopy classification; it is not, on its own, a barcode calculation. The persistence maps are determined separately below.

## Proof
**Geometry and completeness of cases.** In the two-ring coordinates, gaps two, four and six lie within a regular hexagon and have squared lengths \(1,3,4\). Gaps one, three and five cross rings and have squared lengths \(t+2-\sqrt3,t+2,t+2+\sqrt3\). Each odd-distance class is strictly ordered, as is each even class. Comparing the three affine functions with the three constants yields the six displayed positive crossing values and precisely the thirteen prefix subsets in the table, even when two thresholds coincide.

**Homotopy types.** The complex on O1 is the twelve-cycle. E2 consists of the two separate six-cycles. E2+E4 gives the boundary of an octahedron on each ring, and adding E6 fills each ring to a simplex. E2+O1 is the twelve-triangle lateral annulus joining the two six-cycles; hence its homotopy type is \(S^1\). The complexes E2+O1+O3 and E2+E4+O1+O3 are respectively the clique complexes of the third and fourth powers of the twelve-cycle. The established cycle-power theorem gives \(S^1\) and \(\bigvee^3S^2\) respectively (Adamaszek, Corollary 6.7, arXiv:1104.0433).

For the two remaining two-dimensional types, start from the same lateral annulus, whose two circular boundaries lie in their respective rings. With E2+E4 present, glue to its ends two octahedral two-spheres along null-homotopic equatorial circles. The homotopy pushout is \(S^2\vee S^2\vee S^2\). If E6 is present as well, both octahedral spheres are replaced by filled five-simplices, and the same homotopy pushout is the suspension of a circle, \(S^2\). This also describes the relevant inclusion maps, not just the abstract homotopy types.

For E2+E4+E6+O1+O3, the only missing pairs have gap five. Since five is relatively prime to twelve, the missing-pair graph is a twelve-cycle, so the flag complex is its independence complex. The standard cycle-independence calculation gives \(S^3\vee S^3\) (also follows from the cycle theorem). For E2+E4+O1+O3+O5, the only missing pairs have gap six, a perfect matching of six edges; its flag complex is the join of six zero-spheres, namely \(S^5\). With all pairs present it is a simplex.

**Persistence maps.** On adding E2 to O1, and on adding O3 to E2+O1, the larger complex collapses onto the smaller. These two collapses use exactly 12 and 24 free-face pairs, respectively. A similarly explicit sequence of 60 free-face pairs collapses E2+E4+O1+O3 onto E2+E4+O1. These are *relative* simplicial collapses, so each induced integral homology map is an isomorphism, not merely an equality of Betti numbers. The pair sequences are checked afresh by `verify.py`.

When O1 joins the two previously disjoint rings, the lateral annulus identifies their integral loop generators up to sign, giving a surjection \(\mathbb Z^2\twoheadrightarrow\mathbb Z\) with primitive image; its kernel is rank one. When the annulus is adjoined to two octahedral spheres, their two fundamental classes inject primitively as direct summands of the three-sphere wedge's degree-two homology. Filling the two caps with E6 annihilates precisely those two summands and leaves the annular suspension class primitive. These assertions follow from the indicated homotopy pushout, and supply the only non-obvious maps between stages with overlapping positive-degree homology. All other positive-degree maps between successive differing stages have zero source or zero target, except the relative-collapse isomorphisms.

Reading the inclusions in increasing distance order now yields the displayed barcodes. At each of the six tie parameters, simultaneous classes are included together, so formally zero-length bars are simply omitted. The maps are split on every surviving summand, and no torsion occurs.

## Verification
Run `python3 verify.py` using the Python 3 standard library. It enumerates all cliques from the exact six gap classes, checks the thirteen face vectors and every possible strict/tied threshold order, and reconstructs the two crucial relative collapse sequences. It also independently checks the integral homology of the two lateral-gluing complexes by exact unit-pivot chain cancellation, and proves their fundamental groups trivial by a spanning-tree/triangle-relation elimination. Expected final line: `VERIFY_OK`; recorded output is in `verification_output.txt`.

The 36 and 74 integral unit cancellations respectively leave one degree-zero cell plus three and one degree-two cells, with zero residual differential; the simple-connectivity checks turn these homology results into the claimed wedge homotopy types. All loops and matrices are finite and fully enumerated. The infinite quantification over \(t\) is settled by the six symbolic distance functions and the finite exact wall comparison, not by numerical sampling.

## Relationship to prior work
Adamaszek (2011, arXiv:1104.0433, Section 6) already classifies the clique complexes of powers of cycles and the associated nonequivariant sphere-wedge stages. This is used as a theorem, not relabeled as new. Kozlov's cycle-independence calculation provides the other standard ingredient; the 2026 Möbius-ladder independence results also overlap one fixed stage, but do not supply the varying-height Euclidean filtration. Existing fixed-geometry Platonic/polyhedral Vietoris–Rips calculations do not give the six height-dependent wall crossings, the thirteen-state atlas, or the primitive connecting maps for this family. The new assertion is the complete *coupled* height-versus-radius integral persistence classification.

## Limitations
This result is for a specific one-parameter, twelve-point shape family, not arbitrary regular or irregular antiprisms. The abstract homotopy types of several individual stages are established in earlier work. The new contribution is the full exact parameter phase diagram and its integral inclusion maps, for which no directly covering treatment was located in the checked literature or research records. Unindexed or inaccessible equivalent analyses remain a publication-priority risk. This work has not undergone independent mathematical validation.

## References
1. M. Adamaszek, *Clique complexes and graph powers*, first publicly posted April 3, 2011, arXiv:1104.0433, especially Section 6 and Corollary 6.7. https://arxiv.org/abs/1104.0433
2. D. Kozlov, *Complexes of directed trees*, 1999 (cycle independence complexes, cited in Adamaszek's Section 6).
3. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, first posted August 31, 2026, arXiv:2608.30601 (overlapping fixed graph family only). https://arxiv.org/abs/2608.30601
4. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (different point sets and graph-distance filtrations). https://arxiv.org/abs/2302.14388
