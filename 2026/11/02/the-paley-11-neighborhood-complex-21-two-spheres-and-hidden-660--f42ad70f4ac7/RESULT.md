# Full-biplane symmetry on the homology of the Paley-11 out-neighborhood complex

## Finding

Orient the tournament on \(\mathbb F_{11}\) by \(a\to b\) if \(b-a\in Q=\{1,3,4,5,9\}\), and let \(K\) be its out-neighborhood complex, whose faces are subsets of the translates \(a+Q\). The full simplicial automorphism group \(G\) is the classical \(2\)-\((11,5,2)\) biplane group \(\operatorname{PSL}_2(11)\). Its character on \(\widetilde H_2(K;\mathbb Q)\) is

| Element order | Count | Trace |
|---:|---:|---:|
| 1 | 1 | 21 |
| 2 | 55 | −3 |
| 3 | 110 | 0 |
| 5 | 264 | 1 |
| 6 | 110 | 0 |
| 11 | 120 | −1 |

On complexification the module is the sum of the unique eleven-dimensional irreducible and the ten-dimensional irreducible *other than* the augmentation module for the natural eleven-point permutation action. In particular, \(|K|/G\) has zero reduced rational homology. This contrasts with the known one-dimensional second rational homology of the quotient by the natural affine tournament subgroup \(H=\mathbb F_{11}\rtimes Q\) of order \(55\).

## Assumptions and scope

Faces are unordered subsets with a common predecessor; this is not the directed flag complex. Quotients are geometric orbit spaces, not collections of face orbits claimed to be simplicial complexes on the original vertices. The full-group character is over \(\mathbb Q\), with irreducibility assertions over \(\mathbb C\). The previously established ordinary homotopy type \(\bigvee^{21}S^2\) is an input to the character computation, not a new claim here.

## Proof

**Ordinary homotopy input.** The eleven translates have downward closure with face vector \((11,55,110,55,11)\). For a reproducible proof of the ordinary wedge type, start with all nonempty faces unmatched. For pivots \(v=0,\ldots,10\), scan faces in increasing dimension and then lexicographic order, matching an unmatched face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) whenever the latter is an unmatched face. There are \(110\) pairs, leaving one vertex and \(21\) triangles. Orient all codimension-one incidences down except matched edges, which are oriented up. The accompanying enumeration topologically sorts the entire graph of \(242\) nodes and \(715\) incidences. Acyclicity gives a Morse CW model with one vertex and \(21\) two-cells and no others, so each two-cell is attached to the point. The only reduced homology is therefore free of rank \(21\) in degree two.

**Full group.** The facets are the eleven translates themselves, so simplicial automorphisms are exactly the permutations preserving the design blocks. Each pair of distinct points is in exactly two translates, giving the symmetric \(2\)-\((11,5,2)\) design identified by Devillers–Praeger, Example 3.2, whose full automorphism group is \(\operatorname{PSL}_2(11)\). For the permutation action used below, exhaustively assign images to vertices in the order \(0,\ldots,10\), discarding any partial injection that changes face membership on a set of already assigned vertices. No automorphism can be pruned by this criterion; conversely every terminal permutation preserves the facets. The depth counts are \((1,11,110,660,660,660,660,660,660,660,660,660)\).

**Character.** For each terminal permutation \(g\), sum \((-1)^{|\sigma|-1}\operatorname{sgn}(g|_\sigma)\) over nonempty faces \(\sigma\) preserved setwise, and subtract one. This is the degree-two trace by the simplicial Lefschetz identity, since \(H_0\) has trivial character and the only other nonzero rational homology is in degree two. The finite signed sum on all \(660\) permutations gives the table. Its total is \(0\) and its sum of squares is \(1320\); hence there are two distinct multiplicity-one constituents and neither is trivial. Among the irreducible degrees \(1,5,5,10,10,11,12,12\), the only such dimensions summing to \(21\) are \(10,11\). For the permutation augmentation character \(a(g)=\#\operatorname{Fix}(g)-1\), the same permutation enumeration gives \(\sum_g a(g)^2=660\), so the augmentation is irreducible. The sum of the products of our trace with \(a(g)\) over all \(g\) is zero. This excludes that ten-dimensional constituent.

**Quotients.** Barycentric subdivision removes inversions. Over \(\mathbb Q\), the chain complex of the geometric quotient, with cells the orbits of oriented subdivided simplices, identifies with the coinvariants of the subdivided chains. Averaging makes coinvariants exact and identifies them with invariants. Thus reduced rational quotient homology is the invariant homology, of dimension equal to the character average in degree two. This average is zero for \(G\); for \(H\) it is \((21-10+44)/55=1\), because the nonidentity translations have order \(11\) and the other nonidentity elements order \(5\). The other reduced rational groups vanish for both quotients.

## Verification

The accompanying `verify_paley11.py` reproduces the face and Morse counts, directed acyclicity, permutation enumeration, signed Lefschetz sums and character inner products. Run it with Python 3.10 or later; the final marker is `PALEY11_BIPLANE_21S2_FULL660_EQUIVARIANT_CHECKS_OK`. The character calculation uses the ordinary Morse model only to isolate the homology degree; the matching is not asserted to be equivariant.

## Relationship to prior work and limitations

The [October 18 Paley-11 record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-the-homotopy-type-and-affine-homology-character-of-the-paley-11--baff484d9f6d) and the [October 25 Paley-11 record](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-paley-eleven-vertex-tournament-out-neighborhood-spheres-and-affi--70ec12667504) already give the same ordinary wedge type, the affine-subgroup character, and the affine quotient homology. The biplane and its group are classical. The distinct calculation here is the full-group homology character, including the distinction between the two ten-dimensional constituents. An [indexed November 8 biplane record](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-the-eleven-point-biplane-has-21-two-spheres-with-a-multiplicity--d28df67c2de6) gives the same full-group calculation and quotient comparison; catalog dates alone do not settle priority.

Dochtermann–Singh give the out-neighborhood construction and its directed Hom description; a directed flag simplex instead requires a transitive subtournament. A common predecessor does not force transitivity: \(\{0,1,2\}\) is a cyclic triple contained in \(8+Q\). No equivariant wedge equivalence, integral representation decomposition, or integral quotient acyclicity is claimed.

## References

- A. Devillers and C. E. Praeger, *Pairwise transitive 2-designs*, Example 3.2, https://arxiv.org/abs/1405.3030.
- A. Dochtermann and A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, Definition 4.1 and Theorem 4.3, https://arxiv.org/abs/2108.10948.
- *Irreducible complex-character degrees of PSL(2,11)*, OEIS A003882 with ATLAS reference, https://oeis.org/A003882.
