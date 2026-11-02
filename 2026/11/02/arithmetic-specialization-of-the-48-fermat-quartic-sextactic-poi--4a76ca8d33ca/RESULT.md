# Arithmetic specialization of the 48 Fermat-quartic sextactic points

## Finding

Let \(\mathscr Z\subset\mathbb P^2_{\mathbb Z}\) be the projective complete intersection
\[
 F=X^4+Y^4+Z^4=0,\qquad
 G=(X^4-Y^4)(Y^4-Z^4)(Z^4-X^4)=0.
\]
Over \(\mathbb C\), this is the published reduced configuration of 48 proper sextactic points of the Fermat quartic. Its **specified integral complete-intersection model** is finite flat of degree 48 over \(\mathbb Z\). Its geometric special fibers have exactly the following structures:

* In characteristic different from \(2\) and \(3\), \(\mathscr Z\) is 48 distinct reduced geometric points.
* In characteristic \(3\), \(\mathscr Z\) is the triple Cartier thickening \(3D\) of a reduced 16-point divisor \(D\) on the smooth Hermitian quartic \(F_3\). Every local Artin ring of \(\mathscr Z_3\) is \(k[[t]]/(t^3)\). The 16 points are precisely the \(\mathbb F_9\)-rational Hermitian points with all three coordinates nonzero; the remaining 12 of the 28 \(\mathbb F_9\)-points have a zero coordinate. The 16 points are also exactly the triple intersection points of the twelve lines belonging to the three pencils \(X^4=Y^4\), \(Y^4=Z^4\), \(Z^4=X^4\).
* In characteristic \(2\), the special fiber is the fourth-Frobenius-power complete intersection
\[
 \mathscr Z_2=V\big((X+Y+Z)^4,\,((X+Y)(Y+Z)(Z+X))^4\big).
\]
It is supported at exactly the three \(\mathbb F_2\)-rational points \([1:1:0]\), \([1:0:1]\), \([0:1:1]\). Each completed local ring is \(k[[u,v]]/(u^4,v^4)\), of length 16 and Hilbert function \((1,2,3,4,3,2,1)\).

Consequently \(2\) and \(3\) are **exactly** the characteristics in which this integral length-48 configuration ceases to be geometrically reduced. The special fibers describe specialization of a characteristic-zero sextactic-point scheme; they are **not** asserted to equal the intrinsically defined sextactic schemes of the characteristic-\(2\) or characteristic-\(3\) quartics.

## Assumptions and scope

All geometric point and completed-local-ring statements use an algebraically closed residue field \(k\). The integral model is defined by the two displayed homogeneous forms, without any saturation or redefinition after reduction. Set \(A=X^4\), \(B=Y^4\), \(C=Z^4\); thus \(F=A+B+C\) and \(G=(A-B)(B-C)(C-A)\). A point of \(\mathbb P^2(\mathbb F_9)\) is called Hermitian rational when it lies on \(X^4+Y^4+Z^4=0\) over \(\mathbb F_9\); the fourth power is the norm to \(\mathbb F_3\).

## Proof

**1. Generic fibers and all characteristics other than \(2,3\).** Let \(k\) have characteristic unequal to \(2,3\). The quartic \(F\) is smooth, since its partial derivatives \(4X^3,4Y^3,4Z^3\) cannot vanish simultaneously at a projective point. Each of the three quartic factors of \(G\) splits into four distinct lines. On any line \(X=\zeta Y\) with \(\zeta^4=1\), the restriction of \(F\) reads \(2Y^4+Z^4\), giving four distinct points because \(2\) and \(4\) are units. Similarly each of the other eight lines meets \(F\) in four distinct points. If a point lies on lines in two different pencils, then \(A=B=C\); together with \(A+B+C=0\), the invertibility of \(3\) forces all coordinates to vanish, impossible in projective space. Hence the twelve groups of four points are disjoint and \(\mathscr Z_k\) is reduced of length 48.

**2. The characteristic-three scheme identity.** In \(\mathbb F_3[A,B,C]\) the following polynomial identity holds:
\[
 (A-B)(B-C)(C-A)-(A-B)^3
 =(A+B+C)(-A^2-AC+B^2+BC).
\]
Thus in characteristic three, as homogeneous ideals,
\[
 (F,G)=(F,(X^4-Y^4)^3).
\]
Define \(D=V(F,X^4-Y^4)\) on the smooth quartic \(F=0\). The equations force \(A=B=C\), and no coordinate can be zero. Upon scaling \(X=1\), the two equations are \(Y^4=Z^4=1\); their roots are four distinct elements each in \(\mathbb F_9\). Hence \(D\) consists of exactly 16 reduced \(\mathbb F_9\)-rational points. Transversality also follows from the independent gradients of \(F\) and \(X^4-Y^4\), the former having a nonzero \(Z\)-component at every point of \(D\). Therefore the divisor cut out on \(F\) by \(G\) is exactly \(3D\), and each completed local intersection algebra is \(k[[t]]/(t^3)\).

The quartic \(F_3\) is Hermitian because the \(\mathbb F_9/\mathbb F_3\) norm is the fourth power. A rational projective point has fourth powers in \(\{0,1,-1\}\). At a point of \(F_3\) with all coordinates nonzero, three nonzero norms sum to zero in \(\mathbb F_3\) only if all three agree; after normalization this is the just-described 16-point set \(D\). A point with a zero coordinate has exactly one zero coordinate, and on each coordinate axis its two nonzero coordinates have opposing norms. There are four such points on each of the three axes, hence 12. This gives \(16+12=28\) rational Hermitian points and the stated partition. The three four-line pencils have their cross-pencil triple intersections exactly where \(A=B=C\); these are precisely \(D\).

**3. The characteristic-two scheme identity.** In characteristic two the Frobenius fourth-power identity gives
\[
 F=(X+Y+Z)^4,
 \quad G=((X+Y)(Y+Z)(Z+X))^4.
\]
Write \(L=X+Y+Z\) and \(H=(X+Y)(Y+Z)(Z+X)\). The reduced intersection \(V(L,H)\) comprises the three displayed distinct \(\mathbb F_2\)-points. At each such point \(L\) is transverse to exactly one factor of \(H\), and the other factors are units. They therefore form regular local parameters \(u,v\). Passing to completed local rings changes the ideal \((L^4,H^4)\) into \((u^4,v^4)\). This local algebra has monomial basis \(u^iv^j\), \(0\leq i,j\leq3\), and Hilbert series \((1+t+t^2+t^3)^2\); its length is 16.

**4. Finite flatness.** Every geometric fiber is a proper complete intersection of two plane curves of degrees 4 and 12, so has scheme length 48 by Bézout; there is no common curve component, including in characteristic two. The morphism \(\mathscr Z\to\operatorname{Spec}\mathbb Z\) is projective with finite fibers, hence finite. The generic fiber has degree 48 and every fiber has length 48. Locally at every prime, a finite module over a discrete valuation ring is the sum of a free module and a torsion module; the latter would strictly enlarge the special-fiber dimension beyond the generic rank. Thus the torsion part vanishes and \(\mathscr Z\) is finite flat of rank 48. The three characteristic cases exhaust all primes.

## Verification

The standalone Python 3 standard-library script `verify_sextactic.py` checks the characteristic-three polynomial identity over \(\mathbb F_3\), the two characteristic-two Frobenius identities over \(\mathbb F_2\), and independently enumerates all 91 projective points of \(\mathbb P^2(\mathbb F_9)\) using \(\mathbb F_9=\mathbb F_3[i]/(i^2+1)\). It verifies that exactly 28 points lie on the Hermitian quartic, partitioned into the stated 16 non-coordinate and 12 coordinate points, and checks the three characteristic-two support points. Run `python3 verify_sextactic.py` from the directory containing the two files. This is an exact finite calculation, not a substitute for the proof that no other characteristic is exceptional or for the finite-flatness argument.

## Relationship to prior work

Merta and Zieliński identify the 48 complex proper sextactic points of the Fermat quartic with exactly this complete-intersection ideal (their Section 4.1), and compute their coordinates. Those **complex results and the defining ideal are prior work**, not claimed here. Toft and Moe describe sextactic points and the three four-line pencils for general Fermat curves over the complex numbers (Section 2.2.4 and Section 3.1); their general complex pencil geometry is also prior work. The new claim is the **full arithmetic scheme-theoretic specialization**, including the exact two exceptional characteristics, the distinct 16-times-three and 3-times-sixteen local structures, and the Hermitian rational-point partition in characteristic three. The cited literature works in characteristic zero and does not assert these special-fiber ring structures. The finite-field Hermitian point count itself is classical; the point-count value alone is not claimed as new.

## Limitations

The flat integral model is one natural model determined by the published defining ideal, not a characterization of the intrinsic positive-characteristic sextactic locus. In characteristic two the Fermat quartic is nonreduced; in characteristic three some characteristic-zero osculating-conic formulas may fail upon specialization. No result about intrinsic positive-characteristic osculation or about lifting individual special-fiber tangent directions is asserted. The universal conclusion depends on the displayed integral equations; an unrelated integral model may have different fibers. No independent external mathematical audit has been performed.

## References

1. Ł. Merta and M. Zieliński, *On quartics with the maximal number of maximal tangency lines*, arXiv:2410.13997, first posted 2024-10-17, Section 4.1, Proposition 4.2; journal version *Periodica Mathematica Hungarica* 91 (2025), 309–319. https://arxiv.org/abs/2410.13997 ; https://doi.org/10.1007/s10998-025-00648-y .
2. N. P. A. Toft and T. K. Moe, *The Fermat curves and arrangements of lines and conics*, arXiv:2412.16993, first posted 2024-12-22, Sections 2.2.4 and 3.1. https://arxiv.org/abs/2412.16993 .
