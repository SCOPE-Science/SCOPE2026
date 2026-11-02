# Three hundred simple third-order Weierstrass points on the generic Ciani quartic

## Finding
For a nonempty Zariski-open set of parameters \(a\in\mathbb C\), the smooth genus-three quartic
\[
 C_a:\quad X^4+Y^4+Z^4+a(X^2Y^2+Y^2Z^2+Z^2X^2)=0
\]
has precisely **300 distinct third-order Weierstrass points**, each of third-order weight one. Under the natural signed-permutation group \(G\cong S_4\) of order \(24\), their orbit sizes are
\[
 \underbrace{12+12+12}_{36\ \text{sextactic points on involution axes}}
 +\underbrace{24+\cdots+24}_{11\ \text{orbits, }264\ \text{dectactic points}}=300.
\]
The 264 dectactic points are disjoint from the second-order Weierstrass divisor. Equivalently, the degree-300 third-canonical Wronskian divisor is reduced and has three size-twelve orbits and eleven free size-twenty-four orbits. No assertion is made for all smooth parameters, and the exceptional parameter set is not fully classified.

## Assumptions and scope
Work over \(\mathbb C\). The curve is smooth whenever \(a\notin\{-1,-2,2\}\). Indeed, with \(U=X^2+Y^2+Z^2\), \(T=X^2Y^2+Y^2Z^2+Z^2X^2\), the defining equation is \(U^2+(a-2)T=0\); the partial derivatives show that a singular point requires one of the three excluded values. Its canonical bundle is \(K_{C_a}=\mathcal O_{C_a}(1)\), and \(h^0(C_a,3K_{C_a})=10\).

A third-order Weierstrass point is a zero of the Wronskian of the complete series \(|3K_{C_a}|\); its weight is the zero multiplicity. The Wronskian has degree \(300\), since \(\deg(3K)=12\), \(g=3\), and \((10)(12+9(2))=300\). A *dectactic point* here is a point outside the second-order Weierstrass divisor at which a plane cubic has contact of order at least ten.

Let \(G\) be the projective image of determinant-one signed permutation matrices. It has order \(24\). Put
\[
 U=X^2+Y^2+Z^2,\qquad V=X^2Y^2Z^2,\qquad
 B=XYZ(X^2-Y^2)(Y^2-Z^2)(Z^2-X^2).
\]
The zero divisor of \(B\) on \(C_a\) is the union of the intersections with the nine axes of involutions. For generic \(a\), all 36 such points are distinct, split into three \(G\)-orbits of size 12.

## Proof
**1. Forced axis divisor.** The natural \(G\)-actions on \(H^0(C_a,2K)\cong\operatorname{Sym}^2\mathbb C^3\) and \(H^0(C_a,3K)\cong\operatorname{Sym}^3\mathbb C^3\) both have determinant one, so the corresponding Wronskians \(\Omega_2\) and \(\Omega_3\) are invariant sections represented by forms of degrees 27 and 75. At an axis point of an involution, the vector representative has eigenvalue \(-1\); every invariant odd-degree form vanishes there. The axes meet the smooth curve transversely in 36 points for generic \(a\), hence, as sections on the curve,
\[
 \Omega_2=BQ_2,\qquad \Omega_3=BQ_3,
\]
where \(Q_2\) and \(Q_3\) are invariant sections of \(\mathcal O_{C_a}(18)\) and \(\mathcal O_{C_a}(66)\), respectively. Multiplication and division here are identities in the graded coordinate ring of the curve, not assertions of divisibility in the unrestricted polynomial ring.

**2. Quotient and one-variable forms.** Every invariant section of even degree lifts to an invariant plane form: projective normality supplies a lift, and averaging over the finite group supplies an invariant lift. An even-degree form invariant under the determinant-one signed permutations has only even exponents in every monomial and is symmetric in \(X^2,Y^2,Z^2\). It is therefore a polynomial in \(U,T,V\). On \(C_a\), \(T=U^2/(2-a)\). Consequently, for \(a\ne2\), there exist polynomials \(P_{2,a}\) and \(P_{3,a}\) with degree at most 3 and 11 such that
\[
 Q_2=U^9P_{2,a}(V/U^3),\qquad
 Q_3=U^{33}P_{3,a}(V/U^3).
\]
These expressions denote homogeneous polynomial sections after clearing denominators. The rational function \(t=V/U^3\) induces a degree-24 map \(\rho:C_a\to\mathbb P^1\): the equation \(U=0\) cuts out eight distinct points, with \(V\ne0\), each a pole of order three. Since \(|G|=24\) and \(t\) is invariant, \(\rho\) is the \(G\)-quotient. Its branch fibres are \(t=0\) (one orbit of 12), the two values
\[
 t=\frac r{(2+r)^3},\qquad r^2+2ar+(a+2)=0
\]
(two more orbits of 12), and \(t=\infty\) (one orbit of eight points with stabilizer order three). Their contributions to Riemann–Hurwitz total \(3(12)+8(2)=52\), equal to \(2g-2+2(24)=52\), so no other branch values occur for generic \(a\).

**3. An exact specialization proves generic transversality.** Over the prime field \(\mathbb F_{1009}\) at \(a=1\), the accompanying dependency-free script evaluates the two Wronskians at 35 distinct rational points of the quotient, reconstructs both polynomials from 4 and 12 exact evaluations, and independently checks the remaining evaluations. Its polynomial coefficients, listed in increasing powers of \(t\), are
\[
 P_{2,1}=(353,959,322,857),
\]
\[
 P_{3,1}=(879,326,508,141,914,387,343,133,815,401,47,498)
 \quad\text{in }\mathbb F_{1009}[t].
\]
The latter has degree 11, is squarefree, and is coprime to \(P_{2,1}\). The three finite branch values specialize to \(0,889,270\), on which \(P_{3,1}\) evaluates to \(879,682,112\), all nonzero. The leading coefficient \(498\) is also nonzero, so the infinity fibre is avoided. These are exact finite-field calculations, not numerical approximations. Their relevance over characteristic zero is that the Wronskian, quotient polynomial coefficients, discriminant, resultants, and branch-avoidance conditions are rational algebraic in \(a\); the calculations take place in a smooth integral model with denominators invertible modulo 1009. Their nonzero specializations give nonzero characteristic-zero functions of \(a\), hence a nonempty Zariski-open locus satisfying every condition.

**4. Orbit and geometric classification.** For parameters in that open locus, \(B\) has 36 distinct zeros, and \(P_{3,a}\) has 11 distinct simple roots disjoint from all branch values. Each root lifts to a free \(G\)-orbit of 24 points. Thus \(\Omega_3\) has \(36+11(24)=300\) distinct simple zeros, exhausting its degree. The 36 axis zeros are sextactic rather than hyperflex points, since a hyperflex on an involution axis has third-order weight at least five. The resultant of \(P_{2,a}\) and \(P_{3,a}\) is nonzero by the specialization, so none of the 264 residual zeros is second-order Weierstrass; hence they are dectactic. This proves the stated orbit profile, reducedness, and weights.

## Verification
Run `python3 verify_ciani.py` with Python 3.11 or later; no third-party packages are required. The script prints `VERIFY_OK` only after exact implicit-power-series determinants for \(|2K|\) and \(|3K|\), 35 quotient-point checks, interpolation, polynomial-gcd tests, and branch evaluations succeed. It uses the formula \(\Omega_q\propto f_y^{r(r-1)/2}\det([t^i]s_j(x+t,y(t)))\), where \(r=6\) or 10 and \(f(x,y)=x^4+y^4+1+x^2y^2+x^2+y^2\). Factorial constants are invertible modulo 1009 and irrelevant to vanishing. The proof, not the finite enumeration alone, establishes the uniform generic characteristic-zero assertion.

## Relationship to prior work
Kamel and Sakai (2009) study the second-order Weierstrass points of this quartic pencil and the signed-permutation group, but do not compute the generic third-order divisor. Kamel and Elshareef (2019) develop the classification and Wronskian approach for third-order points on arbitrary smooth plane quartics, with worked Fermat and Picard cases, not this generic pencil's orbit distribution. Nawara (2026) computes third-order divisors for four special quartics, including the special member \(a=3\); her general involution-axis theorem explains the mandatory 36 potential axis contributions but neither their generic simplicity nor the additional eleven free orbits. Moreno Vega and Reyes-Carocca (2025) investigate a generalization of the underlying pencil and automorphism groups rather than the generic \(|3K|\) Weierstrass divisor. Thus the full generic orbit profile is not an implication of the inspected calculations, even though the general method and some symmetry-forced support were already known.

## Limitations
The theorem is about a nonempty Zariski-open set, not every smooth value of \(a\). Exceptional values, where roots collide or meet branch fibres, are not classified. The finite-field computation certifies nonvanishing of generic discriminants/resultants when combined with the invariant-theoretic proof; it does not itself enumerate every point over \(\mathbb C\). Independent mathematical review has not been performed. An older implicit computation of the same generic third-order divisor remains a literature-priority risk.

## References
1. E. Nawara, *Third-Order Weierstrass Points on Plane Quartics*, arXiv:2610.30992v1 (first posted 2026-10-22), https://arxiv.org/abs/2610.30992 .
2. A. Kamel and W. K. Elshareef, *Weierstrass points of order three on smooth quartic curves*, *Journal of Algebra and Its Applications* **18** (2019), 1950020, https://doi.org/10.1142/S0219498819500208 .
3. A. Kamel and F. Sakai, *Geometry and computation of 2-Weierstrass points on Kuribayashi quartic curves*, *Saitama Mathematical Journal* **26** (2009), 67–82.
4. V. Moreno Vega and S. Reyes-Carocca, *A generalisation of the pencil of Kuribayashi-Komiya quartics*, arXiv:2507.03128v1 (2025), https://arxiv.org/abs/2507.03128 .
