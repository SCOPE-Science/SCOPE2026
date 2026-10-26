# Complete distance-two mutual-visibility complex of binary hypercubes

## Finding
For every integer \(d\ge3\), let \(Q_d\) have vertex set \(\{0,1\}^d\), with edges joining words that differ in one coordinate. A subset \(S\) is **2-distance mutually visible** if every distinct pair in \(S\) has a shortest path of length at most two whose internal vertices avoid \(S\). Write \(\mathcal V_d\) for this hereditary family, and
\[
F_d(z)=\sum_{S\in\mathcal V_d}z^{|S|}.
\]
Then the **complete size enumerator** is
\[
\boxed{F_d(z)=1+2^dz+2^{d-1}\left(d+\binom d2\right)z^2
       +2^d\sum_{k=3}^{d+1}\binom{d+1}{k}z^k
       +2^{d-2}\binom d3z^4.}
\]
In particular, the coefficient of \(z^4\) includes the additional term \(2^{d-2}\binom d3\), not accounted for by radius-one balls. All coefficients outside the stated range vanish.

Every inclusion-maximal member of \(\mathcal V_d\) is exactly one of two explicitly classified kinds: a closed radius-one Hamming ball \(B_1(c)\), or an affine even/odd parity tetrahedron in a three-coordinate face. Thus the polynomial counting inclusion-maximal members is
\[
\boxed{H_d(z)=2^d z^{d+1}+2^{d-2}\binom d3 z^4.}
\]
The two types are distinct, including for \(d=3\). Therefore \(\mu_2(Q_d)=d+1\), and the smallest cardinality of an inclusion-maximal 2-distance mutual-visibility set is \(4\). For \(d\ge4\), the complex is nonpure, with maximal-set sizes exactly \(4\) and \(d+1\); at \(d=3\), both types have size \(4\).

## Assumptions and scope
All words, vertices, sets, and chosen coordinates are labeled. The Hamming distance \(\operatorname{dist}(x,y)\) is their number of unequal coordinates; translation means bitwise XOR. A radius-one ball is
\[
B_1(c)=\{c\}\cup\{c\oplus e_i:1\le i\le d\}.
\]
An affine parity tetrahedron chooses three distinct indices \(i,j,k\), fixes every other coordinate, and takes the four words of one fixed parity on \(i,j,k\). Equivalently it has the form
\[
T(c;i,j,k)=\{c,\ c\oplus e_i\oplus e_j,\ c\oplus e_i\oplus e_k,\ c\oplus e_j\oplus e_k\}.
\]
Different choices of \(c\) can represent the same tetrahedron. The theorem assumes \(d\ge3\); it does not concern unrestricted mutual visibility or distance thresholds beyond two.

## Proof
**1. Local visibility.** Every path of length two in \(Q_d\) between words \(x,y\) differing in coordinates \(i,j\) has exactly one of the two internal vertices \(x\oplus e_i\) and \(x\oplus e_j\). Consequently, \(S\) is 2-distance mutually visible if and only if (i) its Hamming diameter is at most two, and (ii) it never contains both two-step intermediates for a selected pair at distance two. This equivalence also handles the empty and singleton sets (vacuously).

**2. Complete structural dichotomy.** If \(S\) has no pair at distance two, it has size at most two because \(Q_d\) is triangle-free, and it lies in a radius-one ball. Otherwise select \(a,b\in S\) at Hamming distance two. Translating and permuting coordinates, assume \(a=0\) and \(b=e_1\oplus e_2\). Since all vertices of \(S\) have distance at most two from both, every other member belongs to
\[
\{e_1,e_2\}\cup\{e_1\oplus e_j,e_2\oplus e_j:3\le j\le d\}.
\]
The two intermediates \(e_1,e_2\) cannot both lie in \(S\), by step 1. If exactly \(e_1\) is selected, each \(e_2\oplus e_j\) is excluded by distance three from \(e_1\); all members of \(S\) therefore belong to \(B_1(e_1)\). The case with only \(e_2\) is symmetric.

If neither intermediate is selected, the nonzero members are vectors of weight two, identified with edges of a graph on the coordinate set \([d]\). The diameter constraint says that these edges pairwise intersect. Every pairwise-intersecting family of 2-element subsets is either a star (every edge contains one fixed coordinate) or a triangle consisting of its three edges. To check this fact, take intersecting distinct edges \(12,13\); any edge meeting both either contains \(1\) or equals \(23\). If \(23\) occurs, no fourth distinct edge can meet all three. A star puts \(S\) in the radius-one ball about the common unit vector. The triangle forces exactly \(S=\{0,e_1\oplus e_2,e_1\oplus e_j,e_2\oplus e_j\}\) for some \(j\ge3\), which is an affine parity tetrahedron. This proves that every feasible set is contained in a radius-one ball or is exactly a tetrahedron.

**3. Converse and maximal sets.** Every subset of \(B_1(c)\) is 2-distance mutually visible. For pairs of distinct leaves \(c\oplus e_i,c\oplus e_j\), the midpoint \(c\oplus e_i\oplus e_j\) of their two-step geodesic lies outside the entire ball; all other pairs are adjacent. Every pair of distinct vertices of an affine tetrahedron has distance two, and both its intermediates have the opposite parity on the three varying coordinates, so the tetrahedron is feasible.

Distinct radius-one balls meet in at most two vertices: they intersect in exactly two vertices when their centers have distance one or two, and otherwise have empty intersection. A tetrahedron is not contained in any radius-one ball: after translating one member to zero, a proposed ball center must be zero or a unit vector. The zero vector fails to cover the remaining weight-two vertices; a unit vector outside the three varying coordinates also fails; and each unit vector on the varying coordinates is at distance three from one remaining weight-two vertex. Thus, by the dichotomy, all balls and all tetrahedra are inclusion-maximal, and there are no other facets.

**4. Enumeration without overcounting.** There is one empty subset, \(2^d\) singletons, and \(2^{d-1}[\binom d1+\binom d2]\) unordered pairs at Hamming distance one or two. For \(k\ge3\), distinct radius-one balls cannot contain the same \(k\)-element set; hence they contribute exactly \(2^d\binom{d+1}{k}\) admissible subsets of size \(k\), for \(3\le k\le d+1\). The remaining admissible sets are precisely the full affine parity tetrahedra, each of size four. Their number is \(\binom d3\cdot2^{d-3}\cdot2=2^{d-2}\binom d3\): choose varying coordinates, fixed outside bits, and parity. None is contained in a ball. Summation gives \(F_d\). Counting the two facet types gives \(H_d\). The asserted extremal cardinalities and purity statements follow. No finite computation is needed for the general conclusion.

## Verification
The standalone `verify.py` checks the original shortest-path definition directly, using the two possible geodesics for every distance-two pair, independently of the structural counting calculation. It checks all \(256\) vertex subsets of \(Q_3\), all \(65{,}536\) vertex subsets of \(Q_4\), and every \(Q_5\) subset of cardinality at most six (\(1{,}149{,}017\) tests), for \(1{,}214{,}809\) inspected subsets overall. For \(Q_3,Q_4\), it also checks all inclusion-maximal sets against the facet-count polynomial. The output is recorded in `verification_output.txt`; the exhaustive finite tests do not substitute for the unrestricted proof.

For \(d=3\), the coefficients are \(1,8,24,32,10\), and all ten facets have size four. For \(d=4\), they are \(1,16,80,160,96,16\), with sixteen facets of size four and sixteen of size five. For \(d=5\), they are \(1,32,240,640,560,192,32\).

## Relationship to prior work
Cera López, García-Vázquez, Valenzuela-Tripodoro and Yero introduced the distance-limited mutual-visibility problem in arXiv:2408.03976 (first public version 7 August 2024), studying complexity, several graph classes, and bounds. Their Sections 1, 4 and 5 do not give this hypercube full size distribution or facet classification. Axenovich and Liu (arXiv:2402.04791) address classical unrestricted mutual visibility in hypercubes rather than the distance-two enumerator.

A publicly accessible mathematical result titled *Exact 2- and 3-distance mutual visibility in hypercubes* (30 September 2026; identifier `205d6ab586a0`) already proves the scalar equality \(\mu_2(Q_d)=d+1\), using a Hamming diameter bound and a witnessing radius-one ball. That scalar equality is **not claimed as new**. The earlier proof does not characterize all feasible sets, give their coefficient distribution, enumerate all inclusion-maximal sets, or identify the additional parity tetrahedra. The classical bounded-diameter/anticode problem is closely related, but the present proof independently classifies admissible sets and their multiplicities, including the geodesic obstruction that rules out full four-cycles. No claim of a new diameter bound or a new general hypercube visibility parameter is made.

## Limitations
The theorem is confined to binary hypercubes at distance threshold two and dimensions at least three. It makes no claim about other alphabets, distance thresholds three or more, or unrestricted mutual visibility. Bibliographic searches and inspections do not rule out an unindexed or historical enumeration of diameter-two Boolean anticodes or of maximal cliques in the square of a hypercube, from which parts of this result may be derivable. In particular, the established classification has a short proof and might be implicit in older coding-theory literature; independent bibliographic verification has not been performed. The verification program checks finitely many dimensions and selected subset sizes, not a proof of infinite scope.

## References
1. M. Cera López, P. García-Vázquez, J. C. Valenzuela-Tripodoro, I. G. Yero, *The k-Distance Mutual-Visibility Problem in Graphs*, arXiv:2408.03976 (v1, 7 August 2024); DOI:10.1007/s40840-024-01811-3.
2. M. Axenovich, D. Liu, *Visibility in Hypercubes*, arXiv:2402.04791 (2024); DOI:10.1007/s00373-026-03025-9.
3. P. Frankl, *A Stability Result for Families with Fixed Diameter*, Combinatorics, Probability and Computing 26 (2017), 506–516; DOI:10.1017/S0963548316000456 (diameter-bound and extremal background, not required for the proof).
4. *Exact 2- and 3-distance mutual visibility in hypercubes*, public mathematical record dated 30 September 2026, identifier `205d6ab586a0` (scalar extremal values; full `RESULT.md` inspected).
