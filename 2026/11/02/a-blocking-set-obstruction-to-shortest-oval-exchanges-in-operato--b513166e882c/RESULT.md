# A blocking-set obstruction to shortest oval exchanges in \(\operatorname{PG}(2,3)\)

## Finding
Let \(P\) be the thirteen rational points of the Desarguesian projective plane \(\operatorname{PG}(2,3)\). An **oval** here is a four-point subset of \(P\) with no three collinear, equivalently the four rational points of a geometrically nonsingular rational conic. Define the **one-point exchange graph** \(\mathcal R\): its vertices are all such ovals, with \(A,B\) joined exactly when \(|A\cap B|=3\).

A point set \(U\subseteq P\) is **nontrivially blocking** when it meets each of the thirteen projective lines but contains no entire projective line. Then for any two *distinct* ovals \(A,B\),
\[
d_{\mathcal R}(A,B)=4-|A\cap B|+\mathbf 1_{\{A\cup B\text{ is nontrivially blocking}\}}.
\]
The graph is connected, has \(234\) vertices and \(1404\) edges, is \(12\)-regular, and has radius and diameter both \(4\). Every vertex has distance-sphere sizes \((1,12,60,114,47)\) at distances \(0,1,2,3,4\).

Exactly \(1638\) unordered pairs need one more exchange than their set-difference lower bound. Of these, \(702\) pairs have two common points (distance \(3\)), and \(936\) have one common point (distance \(4\)). From **each** oval, there are exactly six exceptional partners sharing two points, one for each of its six two-point subsets, and eight exceptional partners sharing one point, two for each of its four points. The full unordered-pair spectrum is:

| Common points \(k\) | Distance \(d\) | Number of unordered pairs |
| ---: | ---: | ---: |
| 3 | 1 | 1404 |
| 2 | 2 | 7020 |
| 2 | 3 | 702 |
| 1 | 3 | 12636 |
| 1 | 4 | 936 |
| 0 | 4 | 4563 |

The counting of smooth conics and of pairs with nontrivially blocking unions was investigated previously; the proposed contribution here is **their exact equivalence to a strict shortest-path detour**, the full exchange metric, and the per-oval distribution of obstructed exchanges.

## Assumptions and scope
Represent rational points by nonzero triples in \(\mathbf F_3^3\) modulo nonzero scalar. A line is the kernel of a nonzero linear form modulo scalar, so there are thirteen points and thirteen lines, each line contains four points, and every point pair lies on a unique line. A four-arc is a four-element point set meeting each line in at most two points. All ovals, unions, lines, exchanges, and distances are over the rational point set, not over points of any extension field. Distance means an ordinary unweighted shortest path in the graph of ovals, and an exchange removes one old point and inserts one new point. The indicator equals \(1\) precisely when *both* blocking conditions hold. All statements are for this fixed finite plane, not arbitrary order.

## Proof
**Arc enumeration.** There are \(\binom{13}{3}-13\binom43=234\) noncollinear triples. Each lies on three joining lines. Those three lines together contain nine rational points, leaving exactly four candidates that extend the triple to a four-arc. Counting four-arc/triple incidences yields \(234\cdot4/4=234\) ovals. Conversely any such oval is a nonsingular conic's rational point set: a projective transformation takes its four points to a standard projective frame; among the four rational conics through that frame, the three reducible pair-of-lines members are singular and the remaining conic is nonsingular. Therefore the finite four-arc list is complete.

**Degree.** Each oval has four three-point subsets. For each, its three additional admissible extensions other than the existing fourth point give distinct neighbouring ovals. Hence every degree is \(4\cdot3=12\), and the edge count is \(234\cdot12/2=1404\).

**Shortest-path lower bound and exact finite certificate.** Every one-point exchange can increase the number of points shared with a fixed target by at most one; consequently \(d_{\mathcal R}(A,B)\ge4-|A\cap B|\). To decide sharpness and the exact diameter, the following finite exhaustive procedure enumerates *all* objects and all pairs. This is a complete certificate for the specified 13-point plane, not an inference from a sample.

1. Generate the 13 normalized nonzero vectors \(v\in\mathbf F_3^3\) and the 13 kernels \(L_v=\{p:v\cdot p=0\}\). Assert every line has four points and every two points lie together on exactly one line.
2. Generate every one of the \(\binom{13}{4}=715\) four-point subsets; retain precisely those whose four triple determinants are nonzero. Assert 234 remain. Equivalently, retain those meeting every enumerated line in at most two points.
3. For all pairs of retained subsets, insert an undirected edge exactly when they share three points; assert degree twelve and 1404 edges. Run ordinary breadth-first search from each of the 234 vertices, recording all 234 distances and their complete distance spheres.
4. For each of the \(\binom{234}{2}=27,261\) unordered pairs, compute \(k=|A\cap B|\), \(U=A\cup B\), and the predicate \(\left(\forall L, U\cap L\ne\varnothing\right)\wedge\left(\forall L,L\not\subseteq U\right)\). Assert **equality** between that predicate and the distance excess \(d_{\mathcal R}(A,B)-(4-k)=1\); assert the excess otherwise vanishes. The complete six-entry intersection/distance table is asserted, not estimated.
5. From each oval, count exceptional partners by their common two-point subset and by their common singleton; assert one partner per pair and two partners per point, uniformly over all 234 starting ovals.

The standalone `projective_check.py` is the complete implementation using modular determinants and unordered sets; `affine_check.py` independently builds the plane as nine affine points plus four directions at infinity, generating incidence with bit masks, moves by remove/add, and independently computed shortest paths. Both require only the Python standard library. Each contains assertions covering every stage and every configuration pair. Together they establish the exact distance identity and the stated graph invariants. The two constructions do not rely on a database of ovals or blocking sets.

**Uniformity.** The complete check verifies the same sphere distribution and exceptional-partner multiplicities for *every* oval. These uniformities are also compatible with the transitive action of \(\operatorname{PGL}_3(\mathbf F_3)\) on projective frames, each oval being a four-point projective frame. The transitive action is a conceptual explanation, not a replacement for the distance certificate.

## Verification
With `python3` and its standard library, run `python3 projective_check.py` and `python3 affine_check.py` from the extracted directory. Both independently assert all claimed exact counts and the central blocker/detour equivalence for every unordered oval pair; both print a named PASS marker upon completing all assertions. The direct finite universe has 13 points, 13 lines, 715 candidate four-sets, 234 ovals, and 27,261 unordered oval pairs. Breadth-first search from each of the 234 vertices exhausts all graph distances. No randomized tests, external data, unavailable software, or claims for unbounded field orders are used.

## Relationship to prior work
Coolsaet and Sticker (2010) study projective arcs and conical subsets, establishing the natural old finite-geometric setting; their auxiliary incompatibility graph is **not** the one-point oval-exchange graph. Coolsaet and Sticker's 2011 treatment of larger-plane complete arcs likewise addresses arc classification and generation, not the present smallest-plane geodesic metric. The later classification of small-plane minimal blocking sets by Coolsaet, Botteldoorn and Fack (2022) is relevant to the static blocking predicate but is not evidence of the exchange-distance equivalence. The published abstract and author repository page were accessible; its full paper was not, so detailed exclusion cannot be asserted.

A separate earlier exact census of unordered smooth ternary conic pairs already reported \(234\) four-point smooth conics, the \(1638\) pairs with nontrivially blocking union, and their \(702+936\) intersection split. **Those static counts are explicitly not an originality claim here.** Even knowing that classification does not by itself determine shortest paths, degree, radius, or the formula coupling a metric defect to the blocking predicate. Separate earlier work on exchanges of *six-point minimal blocking sets* studies a different state space, with 234 six-point states, degree six and diameter six; it does not imply the degree-twelve oval graph's metric. Searches for one-point oval swaps, four-arc exchanges, equivalent ternary MDS-code column replacement, and prior finite-plane classifications yielded no identified covering geodesic theorem.

## Limitations
This is an exact finite-plane theorem for \(\operatorname{PG}(2,3)\) only; the identity is not asserted for larger projective planes, and it is not an asymptotic or general MDS-code theorem. The proof of the exact distances is a reproducible *exhaustive finite certificate*, with two independent incidence representations, rather than a short conceptual classification of all geodesics. A historical unindexed result under projective conics, projective-frame exchange, or MDS code terminology could overlap. The complete 2022 small-plane blocking-set classification could not be read through the available access and might contain unanticipated equivalent combinatorial detail. No external independent audit has occurred.

## References
1. K. Coolsaet and H. Sticker, *Arcs with Large Conical Subsets*, Electronic Journal of Combinatorics **17** (2010), R112, DOI 10.37236/384; first published 2010-08-09, open-access full text.
2. K. Coolsaet and H. Sticker, *The complete \(k\)-arcs of \(\operatorname{PG}(2,27)\) and \(\operatorname{PG}(2,29)\)*, Journal of Combinatorial Designs (2011), DOI 10.1002/jcd.20261; open-access author manuscript.
3. K. Coolsaet, A. Botteldoorn, and V. Fack, *Classification of minimal blocking sets in small Desarguesian projective planes*, Journal of Combinatorial Designs **30** (2022), 561–580, DOI 10.1002/jcd.21842; abstract available, full text unavailable in the present access.
