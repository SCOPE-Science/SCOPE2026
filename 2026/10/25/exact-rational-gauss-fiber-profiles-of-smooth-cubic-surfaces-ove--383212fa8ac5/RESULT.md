# Exact rational Gauss-fiber profiles of smooth cubic surfaces over the binary field

## Finding

Let \(S=V(F)\subset\mathbf P^3_{\mathbf F_2}\) be a geometrically smooth cubic surface, where \(F\) is a nonzero homogeneous cubic with coefficients in \(\mathbf F_2\). Its rational Gauss map sends a rational point \(P\) to the rational tangent plane with homogeneous normal vector
\[
\gamma_F(P)=[F_{X_0}(P):F_{X_1}(P):F_{X_2}(P):F_{X_3}(P)].
\]
Define its *rational Gauss-fiber partition* \(\lambda(S)\) to be the decreasing sequence of cardinalities of nonempty fibers of \(\gamma_F:S(\mathbf F_2)\to(\mathbf P^3)^\vee(\mathbf F_2)\). There are exactly \(322{,}560\) nonzero cubic coefficient vectors defining geometrically smooth surfaces, and their entire distribution is:

| \(\#S(\mathbf F_2)\) | \(\lambda(S)\) | Number of coefficient vectors |
|---:|---|---:|
| 1 | \((1)\) | 840 |
| 3 | \((1^3)\) | 11,620 |
| 5 | \((1^5)\) | 74,592 |
| 5 | \((2,1^3)\) | 10,080 |
| 7 | \((1^7)\) | 69,300 |
| 7 | \((2,1^5)\) | 60,480 |
| 9 | \((1^9)\) | 7,000 |
| 9 | \((2,1^7)\) | 40,320 |
| 9 | \((2^2,1^5)\) | 25,200 |
| 9 | \((3,1^6)\) | 10,080 |
| 11 | \((1^{11})\) | 1,260 |
| 11 | \((3,2,1^6)\) | 10,080 |
| 13 | \((3^2,1^7)\) | 1,680 |
| 15 | \((1^{15})\) | 28 |
| **Total** | | **322,560** |

In particular, the largest rational Gauss fiber has cardinality three, exactly \(164{,}640\) equations have injective Gauss map on their rational points, and exactly \(21{,}840\) equations have a fiber of size three. These numerical statements concern *embedded cubic equations in fixed coordinates*, not unweighted projective-isomorphism classes.

## Assumptions and scope

Every nonzero form in the 20-dimensional vector space \(H^0(\mathbf P^3_{\mathbf F_2},\mathcal O(3))\) determines one distinct scalar-normalized cubic equation because \(\mathbf F_2^\times=\{1\}\). Geometric smoothness means smoothness over an algebraic closure, not merely nonsingularity at rational points. The Gauss partition includes only geometric tangent planes at rational surface points, and counts distinct plane *values* via their nonzero four-coordinate vectors over \(\mathbf F_2\).

## Proof

**Exhaustive orbit decomposition.** Enumerate the \(2^{20}-1=1{,}048{,}575\) nonzero cubic coefficient vectors. Each cubic is encoded by a 20-bit integer using the monomial ordering
\[
X_0^aX_1^bX_2^cX_3^{3-a-b-c},\qquad
0\le a\le3,\quad0\le b\le3-a,\quad0\le c\le3-a-b
\]
with ascending lexicographic nested loops in \((a,b,c)\). The three adjacent coordinate swaps and the shear \(X_0\mapsto X_0+X_1\) generate \(\operatorname{GL}_4(\mathbf F_2)=\operatorname{PGL}_4(\mathbf F_2)\), since conjugates of this shear give every elementary transvection. Their exact binary linear action on coefficient vectors gives 141 disjoint nonzero orbits whose sizes sum to \(1{,}048{,}575\). The file `orbit_representatives.csv` supplies the least coefficient mask and size of each orbit, produced by `orbit.cpp`.

**Geometric smoothness test.** Euler's relation for cubics in characteristic two is
\[
F=\sum_{i=0}^{3}X_iF_{X_i}.
\]
Consequently the projective singular locus equals the common projective zero locus of all four formal partial derivatives. For every orbit representative, on each of the four charts \(X_i=1\), compute a Gröbner basis in the remaining three variables of the four partial derivatives over \(\mathbf F_2\). There is no common geometric zero on a chart if and only if the resulting ideal contains \(1\); this is exact by the Nullstellensatz. A representative with an already detected rational singular point is rejected without the Gröbner calculation. Exactly 36 orbits, of combined size \(322{,}560\), pass all chart tests. This criterion is projectively invariant, so the test of one representative settles its entire orbit.

**Gauss partitions.** For each smooth representative and each of the 15 projective points \(P\in\mathbf P^3(\mathbf F_2)\), evaluate \(F(P)\) and the four partial derivatives. Retain those satisfying \(F(P)=0\), group them by the nonzero derivative normal, and sort the fiber cardinalities. A projective coordinate change acts bijectively on both the rational surface points and the rational dual planes (contragrediently), preserving the partition. Weighting each representative's partition by its full coefficient-orbit size gives the 14 rows in the table. The complete 141-representative certificate `cubic_orbit_certificate.csv` and the condensed `gauss_profile.csv` reproduce this sum.

**Independent derivative check.** `independent_gauss.py` computes each of the four formal derivatives by a separate monomial-by-monomial evaluation, without reusing the masks in `classify.py`. It matches the partition of each of the 36 smooth representatives and the weighted table. This corroborates the tangent-normal calculation; it does not independently reproduce the geometric smoothness tests or projective orbit decomposition.

## Verification

From a directory containing the included source and certificate files, run:

```sh
g++ -O3 -std=c++17 orbit.cpp -o orbit
./orbit > orbit_representatives.csv
python classify.py
python independent_gauss.py
python line_comparison.py
```

Python's `sympy` library is required. The checked outputs are `primary_output.txt`, `secondary_output.txt`, and `comparison_output.txt`. Exact certificates contain all 141 orbit representatives, all 36 smooth-orbit classifications, and each distribution cell; they are small enough to inspect directly. No random tests or floating-point calculations enter the proof.

## Relationship to prior work

Karaoğlu's classification of cubic surfaces over \(\mathbf F_2\) gives 141 projective classes, 36 nonsingular classes, and tables of rational points, rational lines, rational Eckardt points, double-line points, and stabilizers. These established underlying class counts are *not* asserted as new here. The presently computed Gauss-fiber partition is a different invariant: `line_comparison.py` verifies that the two smooth representatives with coefficient masks `66913` and `66920` each have nine rational points, three rational lines, one rational Eckardt point, and no rational point on exactly two rational lines, but their Gauss partitions are respectively \((1^9)\) and \((2^2,1^5)\). Thus the published tuple of tabulated point-line incidence invariants does not determine this partition.

Das computes Frobenius/Weyl-group statistics on smooth cubic surfaces and distributions of line configurations and points; these do not tabulate this characteristic-two Gauss-map statistic. Kadyrsizova and collaborators characterize non-Frobenius-split characteristic-two cubics by their geometric line configurations; this does not supply the stated arithmetic tangent-plane fiber table. The new assertion is precisely the *14-cell rational Gauss-fiber census*, not the known 141/36 class counts or known cubic-surface line combinatorics. The possibility of an earlier unindexed computation remains a priority risk.

## Limitations

This is an exact finite classification for embedded smooth cubics over \(\mathbf F_2\), not a statement for larger finite fields, singular cubics, all extension-field points, or the geometric degree of a Gauss map. The primary sources give classifications and arithmetic line statistics from which additional computations might in principle recover the new table, but no directly covering table was found in the material inspected. An associated historical cubic-surface data site could not be accessed; its absence is not evidence of novelty. Independent external audit has not been performed.

## References

1. R. Das, *Arithmetic statistics on cubic surfaces*, arXiv:2002.11183 (first posted 2020-02-25), especially Theorem 1.1 and the tables of Frobenius line configurations and point counts.
2. Z. Kadyrsizova et al., *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018 (first posted 2020-07-23), especially the non-Frobenius-split classification and line-triangle criterion.
3. F. Karaoğlu, *Nonsingular cubic surfaces over* \(\mathbf F_{2^k}\), Turkish Journal of Mathematics 45 (2021), 2492–2510, DOI:10.3906/mat-2102-10, especially Section 3 and Tables 1–2.
