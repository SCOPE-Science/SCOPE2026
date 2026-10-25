# Twenty projective classes of tangent-filling smooth plane quartics over \(\mathbf F_2\)

## Finding
A plane curve is **tangent-filling** if the union of its tangent lines at smooth rational curve points contains every rational point of the ambient projective plane. Among all geometrically smooth plane quartics over \(\mathbf F_2\), exactly **2,656 distinct coefficient-normalized quartic equations** are tangent-filling, forming exactly **20 classes** under \(\operatorname{PGL}_3(\mathbf F_2)\). Exactly **616** of those equations have a rational curve-point set that is *not* blocking, even though their rational tangents cover the plane.

The exact joint distribution, with \(N=\#C(\mathbf F_2)\) and \(r\) the number of distinct rational tangent lines, is:

| \(N\) | \(r\) | Number of equations |
|---:|---:|---:|
| 3 | 3 | 364 |
| 4 | 3 | 84 |
| 4 | 4 | 1,176 |
| 5 | 4 | 252 |
| 5 | 5 | 588 |
| 6 | 6 | 168 |
| 7 | 7 | 24 |
| **Total** | | **2,656** |

In particular, the minimum possible number of rational points on a smooth tangent-filling plane quartic over \(\mathbf F_2\) is **three**. Exactly **364** quartic equations, in **four projective classes**, attain this minimum, with orbit sizes \(84,84,28,168\). A complete set of twenty projective representatives, their orbit sizes, rational point counts, distinct tangent counts, blocking properties, and stabilizer orders appears in `orbit_profiles.tsv`.

## Assumptions and scope
All equations are homogeneous forms of degree four in three variables with coefficients in \(\mathbf F_2\). Since the field has only one nonzero scalar, distinct nonzero coefficient vectors are distinct equations up to scalar. Smooth means smooth after extension to an algebraic closure, not merely nonsingular at the seven rational points. Projective equivalence is taken over \(\mathbf F_2\). The associated curves are nonhyperelliptic smooth genus-three curves in their canonical plane embeddings; the projective-orbit count is also their arithmetic isomorphism-class count.

To encode a coefficient mask, order the fifteen exponent triples \((a,b,4-a-b)\) by increasing \(a=0,1,2,3,4\), then increasing \(b=0,\ldots,4-a\). The coefficient of the monomial \(X^aY^bZ^{4-a-b}\) is bit \(i\) of the integer mask, with bit zero corresponding to the first triple. Thus the representative with mask `4114` is
\[
F=X^3Z+Y^4+YZ^3.
\]
The ordering is given explicitly in `enum_orbits.py` and the twenty masks in `orbit_profiles.tsv`.

## Proof
**1. Sharp minimum by projective incidence.** The plane \(\mathbf P^2(\mathbf F_2)\) has seven rational points, and every rational line contains three. Two distinct rational lines cover only five points. A tangent-filling curve must therefore have at least three distinct rational tangent lines, hence at least three smooth rational curve points. For sharpness, take \(F=X^3Z+Y^4+YZ^3\). The partial derivatives in characteristic two are
\[
F_X=X^2Z,\qquad F_Y=Z^3,\qquad F_Z=X^3+YZ^2.
\]
At any common projective zero of the three derivatives, \(Z=0\) and \(X=0\); the equation then forces \(Y=0\), which is impossible in projective space. The curve is geometrically smooth. Its three rational points are \([1:0:0]\), \([0:0:1]\) and \([0:1:1]\); their respective tangents are \(Z=0\), \(Y=0\), and \(Y+Z=0\). These are the three rational lines through \([1:0:0]\), and their union is every point of the rational plane.

**2. Exhaustive finite classification.** The vector space of ternary quartic forms over \(\mathbf F_2\) has dimension fifteen, so there are precisely \(2^{15}-1=32767\) nonzero forms. For each form and each of the seven nonzero homogeneous coordinate triples, the programs compute the value and the three partial derivatives in exact characteristic-two arithmetic. For a rational smooth zero \(P\), its tangent line is the nonzero gradient \((F_X(P),F_Y(P),F_Z(P))\). A form passes the rational-incidence sieve precisely when none of its rational zeros is singular and every one of the seven rational plane points lies on at least one of the computed tangent lines. Exactly **2,782** coefficient vectors pass this sieve; rational nonsingularity alone is insufficient for geometric smoothness.

To decide geometric smoothness, on each of the three affine charts \(X=1\), \(Y=1\), \(Z=1\), dehomogenize \(F\) to \(f(u,v)\) and compute a reduced Gröbner basis of the ideal \((f,f_u,f_v)\) over \(\mathbf F_2\). By the algebraic-closure Nullstellensatz, there is no geometric singular point on that chart exactly when this ideal contains \(1\). The curve is geometrically smooth if and only if all three chart ideals contain \(1\). This is an exact finite polynomial-ideal test, not a point search truncated at a field-extension degree.

The group \(\operatorname{GL}_3(\mathbf F_2)=\operatorname{PGL}_3(\mathbf F_2)\) has order \(168\), since \(\mathbf F_2^\times\) is trivial. The first program explicitly enumerates every invertible three-by-three matrix, substitutes the resulting linear forms into each quartic, and partitions all 32,767 nonzero forms into **279 complete orbits**. Exactly **78 orbits**, totaling **10,920 forms**, are geometrically smooth. Exactly **20 of those 78 orbits**, totaling **2,656 forms**, are tangent-filling. Subtracting the 2,656 tangent-filling smooth forms from the 2,782 rationally nonsingular tangent-filling candidates leaves **126** geometrically singular forms excluded by the Gröbner tests.

**3. Independent orbit and incidence reconstruction.** The second program enumerates all coefficient masks in a different monomial order and computes the rational-point and tangent incidences directly. It then generates projective-coordinate equivalence by three transformations (swap the first two coordinates, cyclically permute all three, and add the second coordinate to the first), which generate \(\operatorname{GL}_3(\mathbf F_2)\). It performs exact Gröbner tests on every candidate orbit. Without using the first program's orbit table, it recovers the same 2,782 incidence candidates, **20 smooth tangent-filling orbits**, **2,656 smooth tangent-filling equations**, **126 excluded geometric singularities**, and the seven-row distribution above. The independent construction thus checks the critical finite classification by a different group-generation and incidence route.

**4. Blocking distinction and completeness of the table.** For each qualifying orbit the first program also checks, among the seven rational lines, whether every line meets the curve's rational point set. Summing orbit sizes where the answer is negative gives \(364+84+168=616\) nonblocking tangent-filling quartic equations; the remaining \(2,040\) have blocking rational point sets. The four minimum-three-point orbits are the rows with masks `4114`, `4115`, `4309`, and `4383`, with sizes \(84,84,28,168\). These data and all twenty orbit representatives are exactly those of `orbit_profiles.tsv`.

## Verification
Run `python3 enum_orbits.py` and `python3 independent_enum.py` with Python 3 and SymPy 1.14 (any compatible implementation supporting polynomial Gröbner bases modulo two suffices). Both programs are self-contained, enumerate their own coefficient spaces, and print their results. The packaged `verification_a.txt` and `verification_b.txt` are reference outputs of executions of the two included scripts. The detailed orbit table is `orbit_profiles.tsv`.

The two implementations agree on the pair-distribution \((N,r)\), but deliberately use different monomial orders and orbit-generation methods. The independent implementation also computes geometric smoothness for every rational-incidence candidate orbit, without consulting the first implementation's 279-orbit census. The displayed smooth example has an additional direct derivative proof. No computation over finitely many extensions is used to infer smoothness over an algebraic closure.

## Relationship to prior work
Asgarli and Ghioca, *Tangent-filling plane curves over finite fields* (arXiv:2302.13420, first public version 26 February 2023), introduce the tangent-filling condition, general nonexistence bounds, a construction for sufficiently large odd characteristic, and a characteristic-two conic observation. Their inspected introduction, main theorems, and small-characteristic remarks do not provide an enumeration of smooth binary plane quartics or the twenty-orbit classification.

Nart and Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two* (arXiv:math/0312366, first public version 18 December 2003), classify the underlying smooth quartic curves and provide characteristic-two normal forms and arithmetic moduli counts. This broad classification gives models from which further incidence invariants can be computed; the inspected classification results do not state the tangent-covering subset, the minimum-three-point equality classification, or the joint orbit frequencies proved here. The prior classification of all 78 binary quartic classes is not claimed as new.

Earlier computational results also identify certain Gauss-bijective seven-point binary quartics, tangent-contact profiles, and projective symmetries. The 24 seven-point tangent-filling equations in this classification overlap the already-described Gauss-bijective locus and are not separately asserted as novel. Such special loci and marginal contact statistics do not imply the twenty-orbit tangent-covering partition of all smooth quartics, including the 364 three-point equality forms and the 616 nonblocking forms.

## Limitations
This is an exact arithmetic classification only over \(\mathbf F_2\), not a formula for arbitrary even fields or for higher-degree curves. The count of equations is not the count of geometric isomorphism classes over an algebraic closure. The smoothness and completeness checks are exact but implemented computationally, not reproduced as a printed 32,767-case hand table. Published quartic normal forms permit an alternative computation of these invariants; an unindexed earlier execution of that computation could affect historical publication priority. No independent external mathematical audit has been performed.

## References
1. S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420 (v1, 26 February 2023), https://arxiv.org/abs/2302.13420.
2. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (v1, 18 December 2003), https://arxiv.org/abs/math/0312366.
