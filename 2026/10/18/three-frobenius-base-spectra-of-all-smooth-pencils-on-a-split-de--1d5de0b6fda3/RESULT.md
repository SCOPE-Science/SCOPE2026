# Three Frobenius base spectra of all-smooth pencils on a split degree-seven del Pezzo surface

## Finding

Let \(S=\operatorname{Bl}_{P_1,P_2}\mathbf P^2_{\mathbf F_2}\), with \(P_1=[1:0:0]\) and \(P_2=[0:1:0]\). This is the split degree-seven del Pezzo surface. A *rationally all-smooth anticanonical pencil* is a two-dimensional \(\mathbf F_2\)-linear subspace \(W\subset H^0(S,-K_S)\) for which all three nonzero sections cut out geometrically smooth genus-one curves on \(S\). Smoothness is over an algebraic closure; no assertion is made about all geometric members of the pencil.

**Theorem (complete reduced base-scheme and Frobenius classification).** There are exactly \(104\) such pencils. Every one has a *geometrically reduced* base scheme of length \(7\), and the degrees of its closed points over \(\mathbf F_2\) form exactly one of the following three partitions. The pencils form exactly \(13\) orbits of size \(8\) under \(\operatorname{Aut}_{\mathbf F_2}(S)\), of order \(8\):

| Base closed-point degrees on \(S\) | Number of pencils | Automorphism orbits | Point-count multisets of the three smooth members (numbers of pencils) |
|---|---:|---:|---|
| \((7)\) | 32 | 4 | \((3,3,5)\): 8; \((2,4,5)\): 24 |
| \((2,5)\) | 24 | 3 | \((3,4,4)\): 24 |
| \((1,6)\) | 48 | 6 | \((3,5,5)\): 24; \((4,4,5)\): 24 |
| **Total** | **104** | **13** | **Five joint strata** |

In particular, the rational-point-count multiset of the three genus-one members determines the Frobenius splitting partition of the entire scheme-theoretic base locus. Exactly \(32\) pencils have a single degree-seven closed base point, and exactly \(24\) have no rational base point but two closed base points of distinct degrees \(2\) and \(5\).

There is **no** three-dimensional \(\mathbf F_2\)-linear subspace of \(H^0(S,-K_S)\) all of whose nonzero members are geometrically smooth: these pencils have the maximal possible projective dimension on this surface.

The already-recorded complete census of smooth binary plane-cubic pencils gives the total \(104\) indirectly from a global rational-basepoint table. The new assertion here is the *scheme-theoretic reducedness and complete Frobenius splitting distribution on the blown-up surface*, refined simultaneously by anticanonical-member point counts. The mere total \(104\), the ambient \(37\)-orbit plane-cubic census, and the existence of smooth pencils are not claimed as novel.

## Assumptions and scope

Fix coordinates \([X:Y:Z]\) on \(\mathbf P^2_{\mathbf F_2}\). Let \(H\) be a line class and \(E_1,E_2\) the exceptional divisors of the two blowups. Then \(-K_S=3H-E_1-E_2\) and \((-K_S)^2=7\). An anticanonical section is represented uniquely by a ternary cubic vanishing at both \(P_1,P_2\). Its eight-dimensional space has the ordered monomial basis
\[
\mathcal B=(X^2Y,\ X^2Z,\ XY^2,\ Y^2Z,\ XZ^2,\ YZ^2,\ XYZ,\ Z^3).
\]
For an integer mask \(m\in\{1,\ldots,255\}\), its \(i\)-th binary digit is the coefficient of the \(i\)-th displayed monomial, counting from zero. Addition of sections is bitwise exclusive-or of masks. Thus the complete parameter space has \(255\) nonzero equations, and one pencil is canonically the ascending triple \((a,b,a\mathbin{\mathrm{xor}}b)\).

A cubic that is geometrically smooth at every point is equivalent to its proper transform being a geometrically smooth anticanonical divisor: a smooth cubic remains smooth when its two smooth marked points are blown up. Conversely, a cubic singular away from the marked points remains singular on the blowup; a cubic singular at a marked point gives a total-transform anticanonical divisor containing the corresponding exceptional curve, meeting its residual part, hence not smooth. The statement concerns *divisors in the complete anticanonical system*, not abstract elliptic curves under arbitrary isomorphism.

The automorphism group of \(S\) is the subgroup of \(\operatorname{PGL}_3(\mathbf F_2)\) preserving the unordered pair \(\{P_1,P_2\}\): the other \((-1)\)-curve, the strict transform of the line \(P_1P_2\), is the unique \((-1)\)-curve meeting both exceptional curves, and hence is fixed. There are exactly eight such projective transformations. All equivalences in the theorem use this *full* rational automorphism group.

## Proof

**1. Geometric smoothness, exactly.** For any cubic \(F\) in the eight-dimensional space, let \(F_X,F_Y,F_Z\) be its homogeneous quadratic partial derivatives. Euler's identity in characteristic two gives \(XF_X+YF_Y+ZF_Z=F\). Thus \(F\) is singular over an algebraic closure precisely when the three partials have a common projective zero.

Consider the homogeneous multiplication map
\[
\Phi_F:\mathbf F_2[X,Y,Z]_2^{\oplus3}\longrightarrow\mathbf F_2[X,Y,Z]_4,
\qquad(A,B,C)\longmapsto AF_X+BF_Y+CF_Z.
\]
This map has a \(15\)-row, \(18\)-column matrix. If the partials have no common projective zero, the ideal they generate has height three; because the polynomial ring is Cohen--Macaulay, these quadrics form a regular sequence, with quotient Hilbert series \((1+t)^3\). Its degree-four component vanishes and \(\operatorname{rank}(\Phi_F)=15\). If there is a projective common zero, evaluation there gives a nonzero functional on degree-four forms annihilating the image, so the rank is below \(15\). This proves the exact equivalence
\[
F\text{ geometrically smooth}\quad\Longleftrightarrow\quad
\operatorname{rank}_{\mathbf F_2}(\Phi_F)=15.
\]
Exact binary elimination of all \(255\) masks produces \(60\) geometrically smooth anticanonical equations. An independently coded affine-chart Gröbner calculation recovers precisely the same masks (see verification files).

**2. Exhaustive pencils and automorphism orbits.** Among the \(\binom{60}{2}\) pairs of distinct smooth equations, retain exactly those whose sum is smooth, then identify the three generators of each two-dimensional subspace by sorting its nonzero masks. This yields exactly \(104\) different pencils. The eight matrices that either preserve or swap \(P_1,P_2\), and send the third coordinate vector to one of the four vectors \((a,b,1)\), act on the cubics by exact substitution. There are precisely \(13\) orbits, *each of cardinality eight*. Every orbit is represented in `orbit_frobenius.csv`, with coefficient masks, group size, closed-point degrees and member point counts. Direct evaluation on the seven rational points of \(\mathbf P^2\) gives \(56\) pencils with two rational plane base points and \(48\) with three; the first two points are the prescribed blown-up points.

**3. Explicit reduced geometric base schemes.** Fix a representative triple \((a,b,c)\) from the CSV. In the plane chart \(Z=1\), form the two dehomogenized cubic equations. For eleven representatives, choose the parameter \(t=Y\) and eliminate \(X\); for the remaining two representatives \((25,47,54)\) and \((29,107,118)\), choose \(t=X+Y\) and eliminate \(Y\). Exact lexicographic Gröbner calculations yield a triangular basis
\[
u+P(t)=0,\qquad Q(t)=0,
\]
where \(u\) is the eliminated coordinate, and \(Q\in\mathbf F_2[t]\) is monic, **squarefree and of degree seven** in every case. The companion file `verification_elimination.json` records all thirteen exact bases and irreducible factorizations. Representative factorization witnesses are:
\[
\begin{array}{c|c|c}
(a,b)&Q(t)&\text{factor degrees}\\\hline
(25,39)&t(t^6+t^5+t^4+t+1)&(1,6)\\
(25,166)&t^7+t^3+t^2+t+1&(7)\\
(25,198)&(t^2+t+1)(t^5+t^4+t^3+t+1)&(2,5).
\end{array}
\]
Because the quotient ring in this chart is \(\mathbf F_2[t]/(Q)\), the chart contains exactly seven *distinct geometric* common zeros, with the stated Frobenius orbits. Both original cubics also pass through \(P_1,P_2\) on the line \(Z=0\). They have no common irreducible component, since they are distinct geometrically smooth plane cubics. Bézout's theorem therefore gives total scheme length \(9\). The seven distinct affine points together with the two prescribed points already account for this entire length. Thus the complete plane intersection is reduced, and every intersection at either blown-up point is transverse. Its strict transform on \(S\) has exactly the seven affine geometric base points, all simple. Automorphisms preserve these properties, completing the theorem for all \(104\) pencils.

For an independent finite-field check of the Frobenius degrees, `verify_frobenius.py` counts the intersection points over each \(\mathbf F_{2^k}\), \(1\le k\le7\), for all thirteen representatives. Möbius inversion of these counts yields the same three partitions and shows that all nine plane base points are reduced. The field polynomials are verified to define fields by exact multiplication-table tests.

**4. Simultaneous point-count refinement.** Evaluating all three smooth cubic equations of each pencil at all seven plane rational points gives one of precisely five multisets listed in the theorem. Blowup does not change the rational-point count of a smooth cubic through the two marked rational points, so these are also the point counts of the smooth anticanonical sections. The orbit table establishes the exact joint frequencies. In particular, membership in the \((2,5)\)-base stratum is equivalent to having the smooth-member point multiset \((3,4,4)\).

**5. Maximality.** Suppose a three-dimensional vector space of anticanonical cubics had all seven nonzero equations geometrically smooth. Every member vanishes at \(P_1\). The differential-evaluation map at \(P_1\) has target the two-dimensional cotangent space, so a three-dimensional source has a nonzero element in its kernel. That element would define a cubic singular at \(P_1\), a contradiction. Hence no all-smooth anticanonical net exists.

## Verification

Run `python3 verify_exact.py` from the directory containing the supplied files. This standard-library program checks the rank criterion for every mask, counts every pencil, reconstructs the eight-element automorphism action and its orbits, computes rational point-count multisets, and confirms absence of nets. The reproducible reference output is `verification_exact.json`.

Run `python3 verify_elimination.py` with SymPy 1.12 or later to recompute all thirteen independent triangular Gröbner and irreducible-factorization certificates, and compare to `verification_elimination.json`. Run `python3 verify_frobenius.py` with only the standard library to reproduce the projective finite-field extension counts, `verification_frobenius.json` and `orbit_frobenius.csv`. An independently written affine-chart smoothness and substitution checker is `verify_groebner.py` (SymPy), whose output is `verification_groebner.json`. All four tests were run from the delivered source contents and agreed. Exact algorithms, the two complete finite enumerations, and the scheme-theoretic elimination certificates support the proof; finite-field agreement alone is not treated as a proof of geometric smoothness.

## Relationship to prior work

Asgarli and Ghioca's 2022 paper *Smoothness in pencils of hypersurfaces over finite fields* (arXiv:2203.07169) asks whether every rational member of a pencil can be smooth and proves general existence results for sufficiently large finite fields. Asgarli, Ghioca and Reichstein's 2022 paper *Linear families of smooth hypersurfaces over finitely generated fields* (arXiv:2207.00918) proves general existence and dimension bounds. Neither inspected paper provides the special anticanonical scheme-theoretic classification on the split degree-seven del Pezzo surface.

Blache and collaborators' 2019 paper *Anticanonical codes from del Pezzo surfaces with Picard rank one* (arXiv:1903.09397) explains anticanonical divisors, Picard lattices and related finite-field surface constructions, but studies Picard-rank-one degree-four, -five and -six cases, not this split degree-seven pencil geometry. A previously recorded exact binary plane-cubic pencil census lists all \(5544\) ambient pencils in \(37\) projective orbits with rational-basepoint and extension statistics. Its rational-basepoint totals already imply the numerical count here:
\[
\frac{1176\binom 22+336\binom 32}{\binom72}=104.
\]
Its representative table also contains enough equations to recover the restricted pencil list. These facts are **not** novel. However, the earlier census does not tabulate the *geometric scheme-theoretic base structures* or their complete Frobenius partition and elliptic point-count correspondence. Their exact derivation and the reducedness theorem are the present contribution. Earlier unindexed computations or consequences of a broader complete intersection classification remain possible priority risks.

## Limitations

The classification applies only to the **split** blowup of two distinct \(\mathbf F_2\)-points, the complete anticanonical system, and geometric smoothness of its three \(\mathbf F_2\)-rational pencil members. It neither claims all geometric pencil members to be smooth nor treats nonsplit degree-seven forms, larger ground fields, arbitrary genus-one fibrations, or classification of abstract isomorphism classes. The earlier ambient pencil-orbit list contains explicit equations and reduces the incremental priority claim to the scheme-theoretic and arithmetic refinement, not to re-enumeration of pencils. A later independent external audit has not been performed; the results have only the documented self-review and reproducible finite calculations.

## References

1. Shamil Asgarli and Dragos Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first publicly posted 2022-03-14. https://arxiv.org/abs/2203.07169
2. Shamil Asgarli, Dragos Ghioca and Zinovy Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields*, arXiv:2207.00918, first publicly posted 2022-07-02. https://arxiv.org/abs/2207.00918
3. Régis Blache, Alain Couvreur, Emmanuel Hallouin, David Madore, Jade Nardi, Matthieu Rambaud and Hugues Randriam, *Anticanonical codes from del Pezzo surfaces with Picard rank one*, arXiv:1903.09397, first publicly posted 2019-03-22. https://arxiv.org/abs/1903.09397
4. Previous exact computational census, *Extension incidence and projective classes of smooth plane-cubic pencils over \(\mathbf F_2\)*, 37 projective orbits and 5544 pencils. Read for numerical comparison only; independent external audit not asserted.
