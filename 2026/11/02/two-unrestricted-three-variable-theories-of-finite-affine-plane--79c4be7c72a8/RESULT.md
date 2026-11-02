# Two unrestricted three-variable theories of finite affine-plane flat posets

## Finding
Let \(\Pi\) be any finite affine plane of order \(q\ge 2\), not necessarily Desarguesian. Define \(\mathcal A(\Pi)\) to be the inclusion poset whose elements are the empty set, all singleton point sets, all lines, and the full point set. The only nonlogical symbol is binary inclusion; there are no sort names, constants, counting quantifiers, or lattice operations in the signature.

For any finite affine planes \(\Pi,\Pi'\) of orders \(q,q'\ge2\),
\[
\mathcal A(\Pi)\equiv_{\mathrm{FO}^3}\mathcal A(\Pi')
\quad\Longleftrightarrow\quad
(q=2\ \Longleftrightarrow\ q'=2).
\]
Here \(\mathrm{FO}^3\) allows only three reusable variable symbols but arbitrarily deep quantifier nesting. **Exactly two unrestricted three-variable theories occur.** The minimum representatives have 12 and 23 elements, respectively, and 23 is the sharp uniform representative bound.

Moreover, all such planes agree on ordinary first-order sentences of quantifier rank at most three (no variable-width restriction); a three-variable sentence of quantifier rank four separates order two from every larger order. With only two reusable variables, *all* orders \(q\ge2\) agree, even at unrestricted quantifier depth.

## Assumptions and scope
An affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, exactly one line through every two distinct points, exactly one parallel line through a point external to a given line, \(q\) points per line, and \(q\) lines in each parallel class. Lines are disjoint or intersect in one point. The poset has exactly \(q^2+q(q+1)+2\) elements, with ranks zero, one, two, and three corresponding to the empty set, points, lines, and the whole plane.

No coordinate field, Desargues theorem, or transitivity of an automorphism group is assumed. The rank-four separation and the unrestricted three-variable assertion concern ordinary equality-and-inclusion logic without counting.

## Proof
### Persistent three-pebble invariant
Give a pair \((u,v)\) of flats the *pair profile* consisting of its two ranks; equality or strict containment, when applicable; and, when both are distinct lines, whether they are parallel or intersecting. There are 21 ordered profiles (14 up to reversal). Pair profiles determine all atomic inclusion and equality relations. Every one of the 21 profiles is realized relative to any first flat of the required rank in every affine plane of order at least two.

**One-point support lemma.** For any two affine planes of orders at least three, any anchored pairs of the same pair profile admit *identical sets* of possible ordered profile pairs
\[
\{\bigl(\operatorname{tp}(u,w),\operatorname{tp}(v,w)\bigr): w\text{ a flat}\}.
\]
The set depends only on the type of \((u,v)\), not on the affine plane or on the pair chosen. There are 148 ordered extension patterns in total across the 21 possible anchor profiles.

Here is a complete count table for the 14 profiles up to reversal. The entries are numbers of **distinct profile pairs**, not numbers of witness flats:

| Anchor profile, ranks and relation | Order two | Every order at least three |
|---|---:|---:|
| empty–empty (equal) | 4 | 4 |
| empty–point | 6 | 6 |
| empty–line | 7 | 7 |
| empty–whole | 4 | 4 |
| point–point (equal) | 6 | 6 |
| distinct points | 9 | 9 |
| point outside line | 9 | 10 |
| point on line | 9 | 9 |
| point–whole | 6 | 6 |
| line–line (equal) | 7 | 7 |
| two intersecting lines | 11 | 11 |
| two distinct parallel lines | 7 | 9 |
| line–whole | 7 | 7 |
| whole–whole (equal) | 4 | 4 |

To reconstruct the table without coordinates, classify \(w\) into the four ranks and use incidences with the anchors. For two distinct points there is one joining line, \(q\) other lines through each point, \(q^2-q-1\) lines through neither, and other points; all these classes are nonempty for \(q\ge2\). For a point on a line, additional points on and off it and additional lines through and not through it exist for every \(q\ge2\). If a point lies *off* a line, the lines parallel to the line but missing that point number \(q-2\); this is a new nonempty third-flat class exactly when \(q\ge3\). If two lines are parallel, flats outside their union include \(q(q-2)\) points and \(q-2\) other lines in their parallel class; these again exist exactly for \(q\ge3\). If two lines intersect, the unique intersection point, other points of either line, exterior points, lines through the intersection, lines parallel to either line, and lines of other directions not through the intersection are all realizable for \(q\ge2\). The remaining anchor cases contain the empty or whole flat and reduce to these counts. Every class occurs by the affine-plane axioms, and no further classes can occur, proving the lemma and table, including for non-Desarguesian planes.

Duplicator now maintains matching pair profiles for every pair among three corresponding pebbles. When a pebble moves, the other two are fixed; the lemma supplies a response whose profiles relative to both fixed flats match those of the new flat. All atomic formulas are therefore preserved after every move. This is a strategy for arbitrarily many moves, proving unrestricted \(\mathrm{FO}^3\)-equivalence for all orders \(q\ge3\).

### The exception and sharp logical depth
The order-two plane has no third line in a parallel class and no point outside two distinct parallel lines; every plane of order at least three has both. These are exactly the extra support classes in the table. Thus the displayed three-pebble invariant cannot extend to order two.

For a **quantifier-rank-three** comparison, Duplicator matches the rank and pair profile of the first two selected flats. If one more flat is chosen, only its atomic relationships with the first two matter. After erasing the third flat's rank and unobservable line-parallelism from the extension signatures, the two order-two and order-three support tables coincide in every anchor profile. The same holds for all larger orders by the lemma. Hence Duplicator wins three rounds even in the unrestricted-pebble game, giving universal agreement at quantifier rank at most three.

To establish separation at **quantifier rank four**, the independent finite type computation in `checks/verify_fo3_types.py` enumerates all assignments of three variables, including unassigned variables, over the complete order-two and order-three flat posets. At rank zero it records exact equality and inclusion atomic types. At each subsequent rank it replaces each coordinate by every element and records the *set* of previous types obtained, never their multiplicity. An induction on formula construction shows that this canonical refinement identifies precisely the same \(\mathrm{FO}^3\)-formulas of the stated quantifier rank, including sentences represented by three unassigned variables. Exhaustive comparison of the two initial unassigned assignments agrees at ranks zero through three and differs first at rank four. By finite-variable type duality, there exists a three-variable sentence of rank four distinguishing them. Since all planes of order at least three are unrestricted-\(\mathrm{FO}^3\)-equivalent to the order-three plane, rank four separates the order-two plane from all of them. The exact finite type calculation is a complete proof of this finite logical boundary, not a sample-based extrapolation.

With two pebbles, Duplicator need only preserve the rank of the currently held flats and the atomic relation between them. For each rank and atomic relation, a flat of the required new rank exists in every affine plane of order at least two. The exceptional parallel-line distinctions cannot be tracked with just two pebbles. This proves unrestricted \(\mathrm{FO}^2\)-equivalence across every order.

Finally the order-two affine plane has \(4+6+2=12\) flats, and the smallest other affine-plane order is three, with \(9+12+2=23\) flats. These are actual representatives in the two classes, and no smaller representative from this family belongs to the latter class.

## Verification
The standalone `checks/verify_incidence_profiles.py` builds affine planes over prime fields of orders 2, 3, 5, 7 and extension fields of orders 4 and 9, directly enumerates all flats and 21 pair profiles, and checks all 144 (order two) or 148 (orders at least three) distinct ordered one-point extension patterns. The output is `checks/incidence_profiles.out`.

Independently, `checks/verify_fo3_types.py` builds the order-two and order-three planes by a different line construction and performs exact, untruncated \(\mathrm{FO}^3\) type refinement through rank seven, including the no-free-variable state. It establishes agreement through rank three and first separation at rank four; the output is `checks/fo3_types.out`. Both programs use only Python's standard library. They are checks of finite cases; the all-plane statement is proved by the incidence-axiom support lemma.

## Relationship to prior work
Jun Guo, *Lattices Associated with Finite Vector Spaces and Finite Affine Spaces* (2008), examines geometricity properties of posets of flats over finite fields, but does not classify three-variable logical theories. Grohe and Otto, *Pebble Games and Linear Equations* (first public preprint 2012), develops general finite-variable pebble-game techniques and Boolean support methods, but does not give this affine-plane dichotomy. Earlier limited-depth comparisons between affine-flat and modular-subspace posets establish only bounded rank, and unrestricted three-variable field-blindness for **linear** subspace lattices is not a result for abstract affine planes. The present claim applies also to non-Desarguesian planes and makes a sharp order-two exception visible at quantifier rank four.

## Limitations
This is a classification relative to the family of finite affine-plane flat posets in the *pure inclusion* signature. It does not classify arbitrary geometric lattices or all affine spaces of higher dimension. Adding names, point/line sort predicates, lattice operations, counting quantifiers, or extra variables can change the equivalence. Historical priority is not independently certified: a stronger general result expressed in a different language might imply the theorem.

## References
- Jun Guo, *Lattices Associated with Finite Vector Spaces and Finite Affine Spaces*, Ars Combinatoria **88** (2008), 47–53, online July 31, 2008. https://combinatorialpress.com/article/ars/Volume%20088/volume-88-paper-5.pdf
- Martin Grohe and Martin Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first submitted April 9, 2012; CSL 2012, pp. 289–304. https://arxiv.org/abs/1204.1990
