# Arithmetic specialization of twelve undulation tangents on the Komiya–Kuribayashi quartic

## Finding

Let \(R=\mathbb Z[i]\) and let \(K_R\subset\mathbb P^2_R\) be the quartic
\[
F=x^4+y^4+z^4+3(x^2y^2+x^2z^2+y^2z^2)=0.
\]
Use the following twelve ordered linear forms from Edge's construction, as reproduced by Merta–Zieliński:
\[
\begin{aligned}
\ell_1&=-2ix-y+z,&\ell_2&=-2ix+y+z,&\ell_3&=2ix-y+z,&\ell_4&=2ix+y+z,\\
\ell_5&=-2iy-x+z,&\ell_6&=-2iy+x+z,&\ell_7&=2iy-x+z,&\ell_8&=2iy+x+z,\\
\ell_9&=-2iz-y+x,&\ell_{10}&=-2iz+y+x,&\ell_{11}&=2iz-y+x,&\ell_{12}&=2iz+y+x.
\end{aligned}
\]
The generic fiber consists of twelve distinct undulation tangents with all \(\binom{12}{2}=66\) pair intersections distinct. Over every geometric residue field of rational characteristic \(p\ge7\), the twelve specialized lines remain distinct and their arrangement still has precisely sixty-six double points and no higher intersections. **The only exceptional rational characteristics of this integral twelve-line configuration are \(2,3,5\).**

At the unique prime above \(3\), the twelve specialized lines remain distinct but have exactly thirty ordinary double points and six ordinary quadruple points; the six quadruple points are the reduced complete intersection
\[
xyz=0,\qquad x^2+y^2+z^2=0
\]
over \(\mathbb F_9\). The quartic specializes to the smooth Hermitian quartic \(x^4+y^4+z^4=0\). Its complete set of maximal-contact tangents at \(\mathbb F_9\)-rational points consists of twenty-eight lines, of which these twelve are a subset. The specialized twelve-line set equals the reduction of the **different** characteristic-zero line arrangement dual to the twelve undulation points.

At each of the two primes above \(5\), the quartic specializes to four lines in general position:
\[
F\equiv-(x+y+z)(x+y-z)(x-y+z)(-x+y+z)\pmod5.
\]
The original twelve labeled lines collapse in groups of three onto the four components. At the prime above \(2\), the quartic is the double of the conic
\[
Q=x^2+y^2+z^2+xy+xz+yz,
\quad F\equiv Q^2\pmod2,
\]
which splits into two distinct lines over \(\mathbb F_4\), and the twelve labeled lines collapse in groups of four to \(x+y=0\), \(x+z=0\), and \(y+z=0\).

There is a finer **marked pair-intersection specialization**. For each unordered distinct pair \(\{a,b\}\subset\{1,\ldots,12\}\), take the cross product of the coefficient vectors of \(\ell_a,\ell_b\), divide its three entries by their greatest common Gaussian-integer divisor, and regard the resulting primitive triple as a section of \(\mathbb P^2_R\). These sixty-six sections specialize to a weighted finite support cycle as follows; a point's weight is the number of labeled sections specializing there:

| Characteristic | Support points and section weights | Support cardinality |
| --- | --- | ---: |
| \(p\ge7\) | sixty-six of weight one | 66 |
| \(p=3\) | thirty of weight one and six of weight six | 36 |
| \(p=5\) | twelve of weight one and six of weight nine | 18 |
| \(p=2\) | three of weight two, three of weight four and one of weight forty-eight | 7 |

For \(p=5\), the six weight-nine points are the nodes of the four-line special fiber, and the twelve weight-one points are its remaining \(\mathbb F_5\)-rational points. Thus the support is exactly the set of eighteen rational points on the four components, for **either** prime of \(R\) above \(5\). For \(p=2\), the weight-forty-eight point is \([1:1:1]\); the three weight-four points are the coordinate vertices, and the three weight-two points are \([0:1:1]\), \([1:0:1]\), and \([1:1:0]\).

These weights count **marked generic pair sections**, not local lengths of an intrinsic singular scheme or the intersection cycle of the nonreduced special fiber.

## Assumptions and scope

All statements refer to the displayed **integral coordinate model**, the **ordered** twelve sections of the dual projective plane, and all geometric points after reduction at the stated primes of \(R\). At \(3\), the residue field of \(\mathbb Z[i]\) is \(\mathbb F_9\). At \(5\), the two primes correspond to the embeddings \(i\mapsto2\) and \(i\mapsto3\) into \(\mathbb F_5\). At \(2\), the unique prime is \((1+i)\), with residue field \(\mathbb F_2\). A primitive Gaussian coordinate triple is unimodular; hence at least one coordinate survives at every prime, defining a section everywhere. A section's special point may be distinct from the scheme-theoretic intersection of two coincident limiting lines; the claim expressly concerns the separately extended marked section.

In every characteristic other than \(2\) or \(5\), the quartic is smooth. In odd characteristic \(p\ne5\), this follows by examining the partial derivatives \(2x(2x^2+3y^2+3z^2)\) and their cyclic analogues. If three coordinates are nonzero, subtracting their equations forces all three squares equal, then \(8x^2=0\), impossible for odd \(p\); if exactly two coordinates are nonzero, the determinant of the two linear equations in their squares is \(-5\); one nonzero coordinate cannot lie on the quartic. The characteristic-three specialization is therefore smooth. The generic tangency identities remain valid over odd \(p\ne5\) with the fourth-contact coefficient \(5\) invertible, although no claim that these twelve exhaust *all* maximal-contact tangents is made in positive characteristic.

## Proof

**1. Integral lines, contact, and finite determinant obstruction.** For the twelve coefficient vectors \(v_j\in R^3\) displayed above, the source supplies corresponding undulation points \(P_j\in\mathbb P^2_R\). An explicit complement \(V_j\) to each \(P_j\) on the line satisfies the exact identity
\[
F(sP_j+tV_j)=5t^4\quad\text{in }R[s,t].
\]
Thus the lines are fourth-contact lines wherever the quartic is smooth and \(5\ne0\). The identity is checked coefficientwise in the accompanying verifier (evaluating a degree-four polynomial at five distinct integer values, with exact Gaussian coefficients). The generic pair intersections are all distinct because every determinant of three distinct coefficient vectors is nonzero. For all \(\binom{12}{3}=220\) unordered triples, exact Gaussian arithmetic gives the following exhaustive distribution of the positive integer norms of these determinants:

| Norm | Triple count |
| ---: | ---: |
| 4 | 8 |
| 20 | 48 |
| 36 | 24 |
| 40 | 24 |
| 64 | 12 |
| 80 | 48 |
| 100 | 48 |
| 200 | 8 |

The counts sum to \(220\). All prime divisors of all nonzero norms are in \(\{2,3,5\}\). If a determinant vanished at a prime above some rational prime \(p\ge7\), its norm would be divisible by \(p\), contradiction. Distinctness of every pair of specialized lines also follows: two proportional coefficient vectors would yield zero determinant with every third line. Hence all sixty-six intersections stay ordinary and distinct for \(p\ge7\). This establishes both the exact exceptional-prime **upper bound** and good reduction of the incidence configuration.

**2. Primitive sections.** For each pair, compute \(w_{ab}=v_a\times v_b\in R^3\), with \(w_{ab}\ne0\). The Euclidean algorithm in the Gaussian integers yields a gcd \(g_{ab}\) of its three coordinates; replacing \(w_{ab}\) by \(w_{ab}/g_{ab}\) gives a unimodular triple, unique up to multiplication by a unit. Reducing this triple at any prime gives a well-defined projective point. Its generic fiber is the pairwise intersection. The complete algorithm consists of 66 Euclidean gcds and residue reductions; the standalone verifier implements this directly without external packages.

**3. The characteristic-three jump.** Substitute \(3=0\) and regard \(i\) as a square root of \(-1\) in \(\mathbb F_9\). Direct reduction of the twelve lines shows they are all distinct and are, as an unordered set, exactly the reductions of the linear forms whose coefficient vectors are the original twelve undulation points \(P_j\). The corresponding **complex dual-point arrangement** was already shown by Merta–Zieliński to have six quadruple and thirty double points, with the six quadruple points on \(V(xyz,x^2+y^2+z^2)\). Alternatively, direct exact reduction of the sixty-six primitive sections gives thirty singleton classes and six classes of cardinality six. Their total weight is \(30+6\cdot6=66\), and the resulting twelve distinct lines meet in ordinary crossings with the claimed multiplicities. Each weight-six class arises from exactly four distinct lines, since \(\binom42=6\). The six weight-six points satisfy the displayed complete-intersection equations; the complete intersection consists of six distinct geometric points in characteristic three.

The smooth quartic \(x^4+y^4+z^4=0\) is Hermitian over \(\mathbb F_9\): its homogeneous degree is \(3+1\). At any \(\mathbb F_9\)-rational curve point \(a\), its polar tangent has fourfold contact: in a tangent direction \(v\), the cubic intermediate term \(\sum a_jv_j^3\) vanishes because Frobenius-nine fixes \(a\) and cubes the tangent relation \(\sum a_j^3v_j=0\). The Hermitian curve has exactly \(3^3+1=28\) rational points, and their polar lines are distinct. The twelve specialized lines are among them, as is verified explicitly by their coefficient vectors.

**4. The characteristic-five jump.** Substituting \(5=0\) gives the displayed factorization. The four component lines are in general position in \(\mathbb P^2_{\mathbb F_5}\); all four are defined over \(\mathbb F_5\). For each of the two roots \(i\equiv2,3\pmod5\), the twelve labeled original coefficient triples reduce into four equal groups of three. Their pair sections produce eighteen distinct rational points: the six two-component nodes receive \(3\times3=9\) cross-component labels each; each of the four groups produces its three within-group pair sections at three distinct nonsingular \(\mathbb F_5\)-points on its component. A projective \(\mathbb F_5\)-line has six rational points; four lines with six distinct pairwise nodes have exactly \(4\cdot6-6=18\) rational points on their union. Therefore the eighteen support points exhaust this set. The distribution sums to \(12+6\cdot9=66\).

**5. The characteristic-two jump.** In \(\mathbb F_2[x,y,z]\), the quartic equals the square of the stated quadratic form, and over \(\mathbb F_4\) the form splits as
\[
Q=(x+\omega y+\omega^2z)(x+\omega^2y+\omega z),\qquad\omega^2+\omega+1=0.
\]
Since \(i\equiv1\pmod{1+i}\), the twelve labeled linear forms specialize in groups of four to the three distinct lines \(x+y=0\), \(x+z=0\), and \(y+z=0\), concurrent at \([1:1:1]\). Cross-group pairs contribute \(3\binom42=48\) primitive section labels at the concurrence. Gaussian-primitive reductions of the within-group cross products yield the six other stated points, three of weight four and three of weight two. The seven weights sum to \(48+3\cdot4+3\cdot2=66\).

The three characteristic-specific changes are genuine, proving that \(2,3,5\) are not merely possible exceptional primes but the complete exceptional set.

## Verification

Run `python verify_reduction.py` using Python 3 and its standard library. The program recomputes every exact determinant and norm, all 66 primitive sections using Gaussian integer division, the complete residue-class multiplicity partitions at \(2,3\) and both primes at \(5\), the prime-seven good-reduction control, the two special-fiber polynomial identities, the complete \(\mathbb F_9\)-Hermitian point/tangent set, and the contact identity. Its output includes

`KOMIYA_KURIBAYASHI_PRIMITIVE_66_SECTION_ARITHMETIC_AND_HERMITIAN_JUMP_OK`.

The determinant norm exclusion applies over **all** primes of characteristic at least seven, rather than only the finite prime-seven experiment; the finite enumerations at characteristics two, three, and five are exhaustive over their actual residue fields, not extrapolated from a sample. A complete set of exact finite certificates for the enumerations is furnished by the reproducible source code.

## Relationship to prior work

Edge (1945) identified the undulation lines and their contact geometry. Merta and Zieliński (preprint dated 17 October 2024, later published in 2025), Section 3, give the twelve line forms, the sixty-six **complex** ordinary intersection points, and, for the **different dual arrangement** of the twelve undulation points, the thirty-double/six-quadruple incidence structure together with the six quadruple-point ideal. Those inputs and complex counts are **prior results**, not new assertions here. Their exact paper's full relevant Section 3 and adjoining discussion concern complex line configurations, not exceptional characteristics or the 66 primitive pair-section specializations. The new core is the arithmetic classification of the same *actual undulation tangent* lines at every rational prime, including the precise marked weight distributions and the characteristic-three coincidence with the previously known dual arrangement. Related arithmetic degeneration results on other line configurations do not imply this one because their coefficients, pair sections, and exceptional determinants differ.

## Limitations

This result is specific to the displayed integral equations and choice of twelve labeled undulation tangents. In characteristics two and five, the special fibers are not smooth quartics and the specialized labeled lines must not be characterized as twelve distinct tangent lines. The section-weight distribution is **not** an intrinsic singular-scheme length, and nothing is claimed about flat limits of the reduced 66-point subscheme or the full positive-characteristic flex/bitangent schemes. No classification of abstract isomorphism classes or Newton polygons is asserted. Although targeted literature comparisons did not identify the precise arithmetic marked-point result, historical priority remains uncertain, in particular because the complete 1945 original of Edge was not inspected; earlier unindexed arithmetic computations could exist. No independent external mathematical audit or validation has been performed.

## References

1. Ł. Merta and M. Zieliński, *On quartics with the maximal number of the maximal tangency lines*, arXiv:2410.13997, first public preprint 17 October 2024; later *Periodica Mathematica Hungarica* **91** (2025), 309–319, DOI 10.1007/s10998-025-00648-y. Section 3 is the principal source of the explicit lines and prior complex incidences.
2. W. L. Edge, *A plane quartic curve with twelve undulations*, *Edinburgh Mathematical Notes* **35** (1945), 10–13, DOI 10.1017/S0950184300000197. Historical original; only its accessible extract and bibliographic material were inspected.
