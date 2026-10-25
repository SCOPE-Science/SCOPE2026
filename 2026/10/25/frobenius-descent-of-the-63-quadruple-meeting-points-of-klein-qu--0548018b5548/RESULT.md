# Frobenius descent of the 63 quadruple meeting points of Klein quartic bitangents in characteristic three

## Finding
For the **specified** plane Klein quartic \(C/\mathbb F_3\) with equation
\[
X^3Y+Y^3Z+Z^3X=0,
\]
the **previously determined** reduced bitangent scheme and the **newly classified** reduced singular-point scheme of their union have, respectively, the decompositions
\[
B(C)\cong\operatorname{Spec}\mathbb F_3\amalg\operatorname{Spec}\mathbb F_{27}\amalg\coprod_{4}\operatorname{Spec}\mathbb F_{729}
\]
and
\[
I(B(C))\cong\coprod_{3}\operatorname{Spec}\mathbb F_{27}\amalg\coprod_{9}\operatorname{Spec}\mathbb F_{729}.
\]
All 28 bitangents are hyperflex tangents. Every one of the 378 unordered pairs of distinct bitangents meets at one of precisely 63 points **off the quartic**; exactly four of the lines pass through each such point. Therefore the line-arrangement singular points are all ordinary quadruple points, and their arithmetic Frobenius cycles have lengths \(3,6\), with respective multiplicities \(3,9\). The earlier bitangent Frobenius cycles have lengths \(1,3,6\), with respective multiplicities \(1,1,4\); this bitangent orbit count and the hyperflex polynomial are prerequisite background. The **new incidence scheme** has no rational point, even over \(\mathbb F_9\), and its complete extension-field point count is
\[
\#I(B(C))(\mathbb F_{3^n})=9\mathbf 1_{3\mid n}+54\mathbf1_{6\mid n}\qquad(n\ge1).
\]
The arithmetic claim concerns the written \(\mathbb F_3\)-model, not all its twists.

## Assumptions and scope
All geometric points and lines are considered over the algebraic closure of \(\mathbb F_3\); arithmetic Frobenius is \([a:b:c]\mapsto[a^3:b^3:c^3]\). A bitangent includes the degenerate case of fourfold contact at one smooth point (a hyperflex). The objects \(B(C)\) and \(I(B(C))\) denote **reduced** zero-dimensional schemes, with their induced \(\mathbb F_3\)-structures; no assertion is made about the nonreduced scheme structure of a discriminant construction. The 28 geometric hyperflexes, their root polynomial, and their Frobenius orbits are previously established. Geometric Hermitian-unitary incidence is known; the specific new target is the full arithmetic Frobenius refinement of the 63 meeting points for this explicit twist.

Smoothness is immediate: the three first partial derivatives of \(F=X^3Y+Y^3Z+Z^3X\) are \(Z^3,X^3,Y^3\), and they cannot vanish simultaneously at a projective point. Thus \(C\) is a smooth, nonhyperelliptic plane quartic of genus three.

## Proof
**1. Previously established hyperflex parameterization, recalled to make the incidence calculation self-contained.** In characteristic three the Taylor expansion along a vector \(V=(a,b,c)\) at a point \(P=(x,y,z)\) reads
\[
F(P+sV)=F(P)+s(z^3a+x^3b+y^3c)
 +s^3(ya^3+zb^3+xc^3)+s^4F(V).
\]
The tangent line at \(P\) is \(T_P:z^3X+x^3Y+y^3Z=0\). Hence every tangent has contact multiplicity at least three. A tangent line is a fourfold tangent precisely when the linear forms \(z^9X+x^9Y+y^9Z\) and \(yX+zY+xZ\) are proportional. Indeed the cubic Taylor coefficient is the cube of the linear form \(y^{1/3}a+z^{1/3}b+x^{1/3}c\), which vanishes at \(P\) because \(F(P)=0\). It vanishes along the entire tangent line exactly when that linear form is proportional to the tangent linear form \(z^3a+x^3b+y^3c\); cubing this coefficientwise proportionality gives the displayed condition. Thus
\[
P^{(9)}=[z:x:y]. \tag{1}
\]
No coordinate of such a point may vanish: if one vanishes, the quartic equation makes a coordinate vertex, and no vertex satisfies (1). Consequently write \(P=[1:t:z]\) with \(t\ne0\). Equation (1) gives \(z=t^{-9}\) and \(t^{91}=1\). Substitution in \(F(P)=0\) yields
\[
h(t)=t^{28}+t^{21}+1=0. \tag{2}
\]
Conversely the polynomial identity in \(\mathbb F_3[t]\)
\[
t^{91}-1=h(t)(t^{63}-t^{56}+t^{49}-t^{42}+t^{28}+t^{21}-1)
\]
shows that every nonzero zero of (2) satisfies (1) and therefore is a hyperflex. The derivative \(h'(t)=t^{27}\) makes \(h\) separable. A direct comparison of the tangent coefficients \([t^{-27}:1:t^3]\) shows they are pairwise distinct: normalization fixes the middle coordinate, and equality implies both \(t^3=s^3\), hence \(t=s\). Accordingly these 28 points give 28 distinct hyperflex bitangents. The classical odd theta-characteristic count of 28 geometric bitangents in characteristic different from two, or equivalently the elementary degree/genus bound, proves there are no others. Moreover every bitangent is forced to be a hyperflex since any two distinct contact points would contribute multiplicity at least six to a quartic line section.

**2. Previously established bitangent Frobenius action, recalled only as input.** The polynomial in (2) has the following monic irreducible factorization over \(\mathbb F_3\):
\[
\begin{aligned}
h(t)={}&(t-1)(t^3-t-1)\\
&\cdot(t^6+t^4+t^3+1)\\
&\cdot(t^6+t^5-t^3+t^2+t+1)\\
&\cdot(t^6+t^5+t^4+t^3+t^2+t+1)\\
&\cdot(t^6-t^5+t^4-t^2+t+1).
\end{aligned}
\]
Irreducibility can be checked by the usual finite-field gcd test \(\gcd(h_i,t^{3^j}-t)=1\) for each proper divisor \(j\) of the degree of each factor. Because \(P(t)=[1:t:t^{-9}]\) is injective and defined over \(\mathbb F_3\), its tangent construction is Frobenius-equivariant, so the bitangent Frobenius cycles are \(1,3,6,6,6,6\). The unique rational hyperflex point is \([1:1:1]\) and its tangent is \(X+Y+Z=0\).

**3. New quadruple-incidence and Frobenius-descent certificate.** All roots of \(h\) lie in \(\mathbb F_{3^6}=\mathbb F_{729}\), since their factor degrees divide six; they give the full line list \(L_t=[t^{-27}:1:t^3]\). The attached `verify.py`, requiring only Python's standard library, builds this field exactly as
\[
\mathbb F_{27}=\mathbb F_3[u]/(u^3-u-1),\qquad
\mathbb F_{729}=\mathbb F_{27}[v]/(v^2+1).
\]
Here the cubic has no root in \(\mathbb F_3\), and \(-1\) is not a square in \(\mathbb F_{27}\) because \(27\equiv3\pmod4\), so these are fields. The program visits each of the 728 nonzero field elements, obtains exactly the 28 roots of (2), and tests all \(\binom{28}{2}=378\) pairs. For each pair it computes a projectively normalized cross product. Exactly 63 distinct projective cross products occur, each exactly six times; each lies on exactly four distinct bitangent lines. It independently checks that the 63 points lie off \(C\), and closes them under coordinatewise cubing. Their Frobenius cycle-length multiset is three cycles of length three and nine of length six. This exhaustive finite computation constitutes a finite, completely specified proof of the remaining incidence and descent assertions, not a statistical test. The program's assertions reject any discrepancy. The exact arithmetic assertions are reproducible from the displayed equations and attached code.

## Verification
Run `python3 verify.py` with Python 3. The script uses exact modular integer arithmetic; no package installation, random numbers, internet access or other input is needed. It verifies the full field tables, tangent and curve incidence, 28 distinct bitangents, 378 pair intersections, 63 quadruple points, and both Frobenius permutations. Expected terminal line:

`VERIFY_OK: bitangents 1+3+4*6; quadruple intersections 3*3+9*6`

All enumerations are proved exhaustive by the prior 28-root parametrization and the 728-element nonzero field enumeration. The irreducible polynomial factorization supplies an independent arithmetic route to the bitangent cycles. These checks do not certify any claim about characteristic zero or about another \(\mathbb F_3\)-twist.

## Relationship to prior work
Elkies, *The Klein Quartic in Number Theory*, section 3, identifies the characteristic-three Klein quartic geometrically with the Hermitian/Fermat quartic, discusses its 28 fourfold tangents over a suitable field/model, and the enlargement to the unitary automorphism group. Those geometric facts are prerequisites, not new claims. Auer–Top treat genus-three quartics over fields of characteristic three. Meagher–Top note that the written Klein model is a twist of the Hermitian quartic, while their detailed Klein-curve classification in section 8 explicitly assumes characteristic different from two, three and seven. Thus its enumerations cannot directly be used as the stated characteristic-three Frobenius incidence computation. Later work on complex Klein bitangent arrangements gives a different characteristic-zero incidence basket (21 quadruple plus 252 double points), and cannot imply this characteristic-three arithmetic incidence. An earlier explicit calculation already supplied the 28-bitangent root polynomial and orbit multiset for this very \(\mathbb F_3\)-model; both are treated here as established input. The **only new arithmetic refinement asserted** is the Frobenius cycle multiset \(3^3 6^9\) for the complete 63-point concurrence scheme. The underlying geometric Hermitian configuration is not claimed as new.

## Limitations
Only the reduced arrangement singular locus is newly classified; infinitesimal structures, theta-coordinate choices, full automorphism actions, and all other arithmetic twists are outside scope. The 63-point incidence is certified by finite exhaustive arithmetic, not by an independent closed-form classification of all 63 coordinate triples. Equivalence to an unlocated older unitary-polarity or Galois-twist table cannot be ruled out; thus priority beyond the inspected sources is not claimed. The source whose first dated preprint can be verified precisely is Auer–Top (2002-01-16); Elkies' earlier volume is dated by year only and explicitly precedes that preprint.

## References
1. Noam D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (volume dated 1998; later book publication), section 3, especially pp. 79–81. https://library.slmath.org/books/Book35/files/elkies.pdf
2. Roland Auer and Jaap Top, *Some genus 3 curves with many points*, arXiv:math/0201320, initial submission 2002-01-16. https://arxiv.org/abs/math/0201320
3. Stephen Meagher and Jaap Top, *Twists of genus three curves over finite fields* (2010), especially sections 4 and 8. https://home.mathematik.uni-freiburg.de/arithgeom/TwistsGenThreeCurve.pdf
4. M. Janasz, P. Pokora and M. Zieliński, *On arrangements of smooth plane quartics and their bitangents* (2023), Proposition 3.1 for characteristic-zero contrast. https://www.researchgate.net/publication/373551488_On_arrangements_of_smooth_plane_quartics_and_their_bitangents
