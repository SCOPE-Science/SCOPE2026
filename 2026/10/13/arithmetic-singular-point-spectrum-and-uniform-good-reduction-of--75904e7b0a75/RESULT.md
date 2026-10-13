# Arithmetic singular-point spectrum and uniform good reduction of the XR conic–line arrangement
## Finding
Let \(D\subset\mathbb P^2_{\mathbb Z}\) be the degree-18 divisor obtained by multiplying the twelve primitive integral forms below. Over \(\overline{\mathbb Q}\), its singular support has exactly 21 points, comprising nine ordinary sixfold intersections and twelve ordinary nodes. Their smallest common field of definition is \(K=\mathbb Q(i,\sqrt3)=\mathbb Q(i,\sqrt{-3})\) of degree four, and the Galois orbit decomposition is seven rational singleton orbits, one conjugate pair over \(\mathbb Q(\sqrt{-3})\), three conjugate pairs over \(\mathbb Q(i)\), and three conjugate pairs over \(\mathbb Q(\sqrt3)\).

For every prime \(p\ge5\), the geometric reduction of the **same integral model** retains all twelve distinct smooth components, all 21 distinct intersections, and precisely the same ordinary intersection multiplicities (nine sixfold and twelve double). There are no exceptional reduction primes \(p\ge5\). The exact number of \(\mathbb F_p\)-rational points of its geometric singular support is
\[
N_p=\begin{cases}
21 & p\equiv1\pmod{12},\\
13 & p\equiv5\pmod{12},\\
9 & p\equiv7\pmod{12},\\
13 & p\equiv11\pmod{12}.
\end{cases}
\]
The sets of primes giving \(N_p=21,13,9\) have respective natural densities \(1/4,1/2,1/4\).

## Assumptions and scope
Use homogeneous coordinates \([x:y:z]\). The six conic forms, in the exact order relevant to the incidence certificate, are
\[
\begin{aligned}
Q_1&=x^2+2xy+y^2-xz, &Q_2&=x^2+xy+2yz-z^2,\\
Q_3&=x^2+xz+yz,&Q_4&=x^2+xy+z^2,\\
Q_5&=x^2+2xy-xz+yz,&Q_6&=x^2-y^2+xz+2yz.
\end{aligned}
\]
The six lines are
\[
L_1=y,\quad L_2=x+z,\quad L_3=x+y-z,\quad L_4=x+y+z,\quad L_5=x-z,\quad L_6=2x+y.
\]
The originating published arrangement uses \(x+\frac12y\) for the final line; multiplying it by two gives a primitive integral equation defining the same characteristic-zero arrangement. Reduction means reduction of these particular primitive integer polynomials; no claim is made for other integral presentations or the excluded primes two and three. A geometric ordinary \(m\)-fold point consists of \(m\) smooth components with pairwise distinct tangent lines over an algebraic closure. The count \(N_p\) concerns points of the geometric singular support fixed by Frobenius, not scheme length and not rational branches.

## Proof
**1. Explicit points and their incidence.** Work in the degree-four biquadratic field \(K\), with \(i^2=-1\), \(r^2=3\), and \(h=ir=\sqrt{-3}\). Seven sixfold points are rational:
\[
[0:0:1],\ [0:1:0],\ [1:-2:-1],\ [1:-2:1],\ [1:-1:0],\ [1:0:-1],\ [1:0:1].
\]
The other two sixfold points are \([2:-1\pm h:-1\pm h]\), with correlated signs. The twelve double points are the following six conjugate pairs (in each displayed pair, the plus and minus signs are linked):
\[
\begin{aligned}
&[1:0:\pm i],\\
&[-1\mp i:2:1\pm i],\quad[-1\pm i:2:1\pm i],\\
&[-1\mp r:2:-1\pm r],\quad[-1\pm r:2:-1\pm r],\\
&[-1:2:2\pm r].
\end{aligned}
\]
Direct substitution into the twelve displayed forms gives exactly nine points on six components and twelve points on two components. In the same coordinate order, the seven rational sixfold-point incidence index sets, using zero-based indices for \((Q_1,\ldots,Q_6,L_1,\ldots,L_6)\), are
\[
\begin{gathered}
(0,2,4,5,6,11),\ (1,2,3,4,7,10),\ (3,4,5,7,8,11),\\
(0,2,3,9,10,11),\ (0,1,3,5,8,9),\\
(1,2,5,6,7,9),\ (0,1,4,6,8,10).
\end{gathered}
\]
Each nonrational sixfold point lies on all six conics. The companion verifier determines the remaining incidence lists directly from the displayed coordinates and component polynomials, without assuming them.

**2. Exact good-reduction obstruction certificate.** The determinants of the six conic Hessian matrices are
\[
(-2,-6,-2,-2,-6,-6).
\]
Thus all six conics are smooth in every characteristic at least five. To compare coordinates and tangents simultaneously, calculate in the integral order \(R=\mathbb Z[i,r]\), where the field norm of \(u=a+bi+cr+dir\) is
\[
\operatorname{N}(u)=\bigl(a^2+b^2+3c^2+3d^2\bigr)^2-12(ac+bd)^2.
\]
For each pair of different listed projective points, take the three coordinates of their cross product, compute their integer norms, and take their greatest common divisor (in absolute value). There are exactly \(\binom{21}{2}=210\) tests. For each listed point and every form not vanishing there, take the norm of the nonzero evaluation: 174 tests. For every pair of component branches through every listed point, form the cross product of their two gradient vectors, then take the gcd of its three coordinate norms: 147 tests. Exact evaluation finds that each of these 531 positive integers has prime support contained in \(\{2,3\}\). All cross-product tests are nonzero, and every listed point has primitive coordinates at primes at least five.

For any prime \(p\ge5\), a field element whose norm is a unit modulo \(p\) cannot vanish at any prime over \(p\). The gcd certificates therefore ensure respectively that no two points merge, no unexpected component passes through an enumerated point, and all enumerated intersecting component branches remain transverse. Combined with the nonzero Hessian determinants, the reduced components are smooth and remain pairwise distinct.

**3. Exhaustion.** Each of the 66 unordered component pairs contributes exactly \(\deg(C_i)\deg(C_j)\) distinct transverse intersection points among the 21 listed points. The sum of these pairwise intersection counts is
\[
15\cdot4+36\cdot2+15\cdot1=147=9\binom62+12\binom22.
\]
These equalities hold in every characteristic \(p\ge5\), by Step 2. Bézout's theorem applied to each pair of distinct plane components forbids any further intersections, proving the universal geometric singular-support assertion (and reestablishing the characteristic-zero census without relying on the original report alone).

**4. Arithmetic splitting and densities.** The coordinate list is stable under sign changes of \(i\) and \(r\). Its orbit decomposition is visibly \(7\cdot1+7\cdot2\), distributed across the three quadratic subfields as claimed. The presence of the points \([1:0:i]\) and \([-1:2:2+r]\) forces both \(i\) and \(r\) into any common field of definition; hence the minimal common field is precisely \(K\). For primes \(p\ge5\), Frobenius fixes a quadratic pair if and only if its quadratic radical belongs to \(\mathbb F_p\). Hence the numbers of rational sixfold and double points are, respectively,
\[
7+2\,\mathbf1_{(-3/p)=1}\quad\text{and}\quad
6\,\mathbf1_{(-1/p)=1}+6\,\mathbf1_{(3/p)=1}.
\]
The quadratic-residue criteria modulo 12 yield the displayed formula. Dirichlet's theorem on the four reduced residue classes modulo 12 gives the three natural densities.

## Verification
The accompanying `verify.py` is a complete Python 3 program requiring only the standard library. It reconstructs the 21 points in \(\mathbb Z[i,\sqrt3]\), checks all 12 component equations, calculates the six Hessian determinants, tests all 66 component pairs against Bézout degrees, and verifies exactly 210 point noncollision, 174 excluded-incidence, and 147 pairwise tangent obstructions. It also independently enumerates \(\mathbb P^2(\mathbb F_p)\) for the twelve primes \(p=5,7,11,13,17,19,23,29,31,37,41,43\). Run `python verify.py` and expect `VERIFY_OK`.

## Relationship to prior work
Măcinic and Pokora's *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228v1 Example 2.7 (final v3 Example 2.8), prints these same twelve geometric components, records nine sixfold intersections and twelve nodes over \(\mathbb C\), and proves the arrangement is free with exponents \((4,13)\). These published characteristic-zero facts are **not** claimed as new. This result instead identifies the entire number-field Galois spectrum of those 21 points and proves exact good reduction and rational-singular-point counts across all primes \(p\ge5\). The originating paper's geometry and freeness do not by themselves determine the arithmetic splitting or the complete exceptional-characteristic boundary.

## Limitations
The claim is about the reduced singular-point support and pairwise transversality of a fixed integral model; characteristics two and three, other integral models, ramified arithmetic schemes, deformation-theoretic invariants and freeness after reduction are not classified. The algebraic checker supplies exhaustive finite algebraic calculations, not an independent formal proof assistant or independent review. Unindexed historical calculations could still overlap the arithmetic classification.

## References
1. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, arXiv:2309.15228v1 (first public version 2023-09-26), Example 2.7; revised arXiv:2309.15228v3, Example 2.8.
2. A. Măcinic and P. Pokora, *On plus-one generated conic-line arrangements with simple singularities*, Rend. Lincei Mat. Appl. 35 (2024), 349–364, DOI:10.4171/RLM/1044; primary MSC2020 14H50.
