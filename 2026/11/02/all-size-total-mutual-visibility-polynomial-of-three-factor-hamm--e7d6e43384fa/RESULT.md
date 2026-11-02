# All-size total mutual-visibility polynomial of three-factor Hamming graphs

## Finding
For integers \(a,b,c\ge 2\), let \(G_{a,b,c}=K_a\square K_b\square K_c\), and let \(\mathcal T_{a,b,c}(z)\) count its total mutual-visibility vertex sets by cardinality, including the empty set. The complete three-parameter sequence of polynomials has the trivariate exponential generating function
\[
\boxed{\sum_{a,b,c\ge0}\mathcal T_{a,b,c}(z)\frac{x^a y^b w^c}{a!b!c!}
=\exp\!\left(x+y+w+zxyw+yw(e^{zx}-1-zx)+xw(e^{zy}-1-zy)+xy(e^{zw}-1-zw)\right).}
\]
Here, for the formal coefficient-extraction extension, \(\mathcal T_{a,b,c}(z)=1\) whenever \(\min\{a,b,c\}=0\). This convention is not an assertion about nonempty Cartesian products with an empty factor.

Equivalently, \(\mathcal T_{a,b,c}\) is specified using only nonnegative integer operations by the recurrence below, with \(\mathcal T_{a,b,c}=1\) if a parameter is zero:
\[
\begin{aligned}
\mathcal T_{a,b,c}(z)={}&\mathcal T_{a-1,b,c}(z)
+bc\sum_{\ell=1}^a\binom{a-1}{\ell-1}z^\ell\mathcal T_{a-\ell,b-1,c-1}(z)\\
&+c\sum_{\ell=2}^b\binom b\ell z^\ell\mathcal T_{a-1,b-\ell,c-1}(z)
+b\sum_{\ell=2}^c\binom c\ell z^\ell\mathcal T_{a-1,b-1,c-\ell}(z),
\qquad a,b,c\ge1.
\end{aligned}
\]

The same classification yields exact counts of maximum configurations. If \(a\ge b\ge c\ge5\), the maximum size is \(a+b+c-6\), and exactly
\[
\boxed{a(a-1)b(b-1)c(c-1)}
\]
sets attain it; they form one orbit under independent coordinate relabelings. If \(a\ge b\ge3\) and \(c=2\), the maximum size is \(a+b-2\), attained by exactly \(\boxed{2ab}\) sets, again forming one coordinate-relabeling orbit. These extremal cardinalities were established previously; the exact counts and full polynomial are the contributions considered here.

## Assumptions and scope
A total mutual-visibility set \(X\subseteq V(G)\) is a vertex subset such that, for every two distinct vertices of \(G\), at least one shortest path joining them has no internal vertex in \(X\). Vertices of \(G_{a,b,c}\) are triples in \([a]\times[b]\times[c]\), and graph distance is Hamming distance (the number of differing coordinates). All sets are labeled: changing any coordinate value normally changes the counted set. The two special maximum-count formulas require precisely the stated parameter ranges. The full polynomial holds for every \(a,b,c\ge2\), including thin and equal-size boundaries. Zero parameters are allowed only in the formal recurrence and generating function.

## Proof
**1. The inherited distance-two criterion.** By Bujtás, Klavžar and Tian (2023, Theorem 6), a vertex set in a Hamming graph is total mutual-visible if and only if no two of its vertices are at graph distance exactly two. In three factors this means that distinct selected triples have Hamming distance either one or three. We use this published equivalence as a premise, not as a newly established theorem.

**2. Canonical component decomposition.** Form the graph induced by \(X\) in \(G_{a,b,c}\). If two selected vertices \(u,v\) are adjacent, they differ in a unique coordinate \(i\). Any selected neighbor \(w\) of \(v\) differing from \(v\) in another coordinate would have Hamming distance two from \(u\), which is forbidden. Following any induced path shows that every vertex of the component differs only in coordinate \(i\). Thus each nonsingleton connected component consists of an entire selected clique on one coordinate line; it occupies \(\ell\ge2\) coordinate labels in its varying direction and one label in each fixed direction. A singleton component occupies one label in each direction.

Vertices from distinct components are not adjacent, and selected pairs cannot be at distance two. They must therefore differ in all three coordinates. Equivalently, distinct components have pairwise disjoint sets of occupied labels in *each* coordinate. Conversely, any unordered collection of components of the described four types, with disjoint label supports in all coordinates, defines a selected set with all intracomponent distances one and all intercomponent distances three. This establishes a bijection, including the empty family.

**3. The generating function.** Treat labels in the three coordinate alphabets as three independent labeled sorts. An unused label contributes \(\exp(x+y+w)\). A singleton component has mixed exponential weight \(zxyw\). A component varying in the first coordinate with size \(\ell\ge2\) contributes \(z^\ell x^\ell yw/\ell!\), and the analogous second- and third-coordinate components contribute \(z^\ell xy^\ell w/\ell!\) and \(z^\ell xyw^\ell/\ell!\). Summing the first-coordinate contributions over \(\ell\ge2\) gives \(yw(e^{zx}-1-zx)\), with the other two sums analogous. As the components are an *unordered set* of distinguishable labeled-support components, the multitype labeled exponential formula exponentiates the sum of their weights. Unused labels are then included independently. This gives the displayed identity without multiplicities or duplicate representations: a nonsingleton component has a unique varying coordinate and every singleton occurs exactly once.

**4. Positive-coefficient recurrence.** Mark one fixed label from the first coordinate alphabet. If unused, remove it: this contributes \(\mathcal T_{a-1,b,c}\). If it lies in a first-coordinate component of length \(\ell\ge1\), choose the other \(\ell-1\) labels in that coordinate, one label in each other coordinate, and remove those supports. The factor is \(bc\binom{a-1}{\ell-1}z^\ell\). If it lies in a second-coordinate component of length \(\ell\ge2\), the factor is \(c\binom b\ell z^\ell\), and similarly for a third-coordinate component. In each case the remainder is another allowed component system on unused labels. Each configuration falls into exactly one of these cases, proving the recurrence. Setting any alphabet size to zero leaves only the empty selected set, giving the base condition.

**5. Maximum sets for large third factor.** Suppose \(a\ge b\ge c\ge5\), and let \(s\) denote the number of components. A one-component set has size at most \(a\). A two-component set has size at most \(a+b-2\): at most two varying coordinate directions are available, and if the directions differ, each loses at least one label to the other's fixed coordinate. For \(s\ge3\), every component uses at least one label in each coordinate; a component containing \(r_1,r_2,r_3\) labels contributes exactly \(r_1+r_2+r_3-2\) selected vertices. Since coordinate supports of distinct components are disjoint, \(|X|\le a+b+c-2s\le a+b+c-6\). The latter bound is larger than the one- or two-component bounds because \(b,c\ge5\).

It is attained by three components, one varying in each axis, consuming respectively \(a-2\), \(b-2\), \(c-2\) labels along their axes and one label on every other axis. Equality forces exactly three components and the use of *all* coordinate labels. Since each alphabet has at least five labels, each coordinate must be the varying direction of one component; hence the three varying directions are distinct. On coordinate \(i\) the two fixed labels occupied by the other two components form an ordered pair of distinct labels. There are \(n_i(n_i-1)\) ways to choose those labels, and the remaining labels belong uniquely to the varying component. Multiplying for \(n_1=a,n_2=b,n_3=c\) gives exactly \(a(a-1)b(b-1)c(c-1)\) distinct maxima, all equivalent under coordinate relabelings.

**6. Maximum sets with a two-label third factor.** Suppose \(a\ge b\ge3\) and \(c=2\). At most two components are possible. One component has size at most \(a\), while two components varying in the first and second directions can have \(a-1\) and \(b-1\) vertices, respectively. Because \(a+b-2>a\), this is the only maximum type. The first-axis line omits the fixed first coordinate of the second-axis line, and vice versa. There are \(a\) choices of one excluded first label, \(b\) choices of one excluded second label, and two ways to assign the third-coordinate labels to the two lines. The result is \(2ab\), and all are equivalent under coordinate relabeling.

## Verification
The standalone accompanying `verify.py` computes the integer recurrence without using symbolic-algebra software. It independently enumerates no-distance-two vertex families by a conflict-graph recursion for all dimension triples \((2,2,2)\), \((2,2,3)\), \((2,3,3)\), \((3,3,3)\), and \((3,3,4)\), comparing every coefficient. It separately tests the original *shortest-path definition* exhaustively for all vertex subsets on \((2,2,2)\) and \((2,2,3)\), and checks a deterministic random sample against the distance-two characterization for two larger boards. Boundary and large-alphabet top coefficients are checked using the independently stated closed counts. The program finishes with `VERIFY_OK`.

Some concrete complete polynomials are
\[
\begin{aligned}
\mathcal T_{2,2,2}(z)&=1+8z+16z^2,\\
\mathcal T_{3,3,3}(z)&=1+27z+189z^2+387z^3+162z^4,\\
\mathcal T_{4,4,4}(z)&=1+64z+1152z^2+7680z^3+19200z^4+13824z^5+2304z^6.
\end{aligned}
\]
These finite examples confirm, but do not prove, the infinite identities.

## Relationship to prior work
Bujtás, Klavžar and Tian (arXiv:2307.05168, first made public on 2023-07-11) proved the distance-two criterion and found the maximum *cardinality* for three-factor Hamming graphs. Their Section 3 already derives a closely related decomposition of compatible triples into disjoint base-edge classes; neither that structural premise nor their extremal cardinalities are claimed as new here. The new result is the complete all-cardinality enumerator, its positive recurrence, and the exact classification and number of maximum configurations in the two parameter regimes stated above.

Bujtás, Klavžar and Tian (2025, *Aequationes Mathematicae*, DOI 10.1007/s00010-025-01197-y) introduced visibility polynomials and computed examples on other graph classes, including complete bipartite graphs and the Petersen graph. Their general inclusion-exclusion principle does not supply this three-factor Hamming polynomial. Brešar and Yero (arXiv:2307.02951) investigate the *minimum cardinality among inclusion-maximal* total mutual-visibility sets, a different numerical question; their inspected Cartesian-product results concern two factors. The EGF and recurrence were not identified in these inspected sources or in targeted searches under distance-two-free ternary codes and multipartite triangle-family terminology.

## Limitations
Originality is assessed against inspected, available records, not certified as absolute publication priority. An unindexed enumeration of multipartite triangle families with no singleton intersections, or equivalently a length-three mixed-alphabet code avoiding Hamming distance two, could imply the formula. The large-third-factor orbit classification excludes \(c=2,3,4\); the full polynomial and integer recurrence remain valid at those boundaries, and the explicit two-label-third-factor classification covers \(c=2\) when \(b\ge3\). No formula for general products of four or more nontrivial factors is claimed. Independent mathematical audit has not been performed.

## References
1. Csilla Bujtás, Sandi Klavžar and Jing Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, first version 2023-07-11; later *Opuscula Mathematica* 45 (2025), 63–78. Theorem 6 and Section 3.
2. Csilla Bujtás, Sandi Klavžar and Jing Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, *Aequationes Mathematicae* 99 (2025), 1883–1901, DOI 10.1007/s00010-025-01197-y; Section 3.
3. Boštjan Brešar and Ismael G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, first version 2023-07-06; *Applied Mathematics and Computation* 465 (2024), 128411. Section 2.3 and concluding remarks.
