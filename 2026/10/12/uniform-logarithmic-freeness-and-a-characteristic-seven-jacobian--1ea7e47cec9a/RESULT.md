# Uniform logarithmic freeness and a characteristic-seven Jacobian jump for an equilateral conic–line arrangement

## Finding
Let \(k\) be any field of characteristic zero or of prime characteristic \(p\geq5\), and set \(R=k[x,y,z]\). Consider the degree-seven reduced divisor \(D_k\subset\mathbb P^2_k\) defined by
\[
F=(3x^2+y^2-3z^2)(3x^2+y^2-12z^2)(x-z)(x+y+2z)(-x+y-2z).
\]
This is an integral coordinate presentation of the equilateral two-conic, three-line arrangement described by Dimca and Pokora. Put \(J_F=(F_x,F_y,F_z)\),
\[
\operatorname{Der}(-\log F)=\{(a,b,c)\in R^3:aF_x+bF_y+cF_z\in(F)\},
\quad
\operatorname{AR}(F)=\{(a,b,c)\in R^3:aF_x+bF_y+cF_z=0\}.
\]
The degree of a triple means its common homogeneous coefficient degree.

**Uniform logarithmic freeness.** For every such \(k\), \(\operatorname{Der}(-\log F)\) is free with one generator of degree one and two of degree three. An explicit integral basis \(E,U,V\) is given below; its coefficient determinant is exactly \(-3F\). In particular, there are no failures of logarithmic freeness at any prime \(p\geq5\).

**Exceptional Jacobian behavior.** The minimal degrees of a homogeneous free basis for \(\operatorname{AR}(F)\) are
\[
\begin{cases}(3,3),&\operatorname{char}(k)=0\text{ or }p\geq5,\ p\ne7,\\
(1,5),&\operatorname{char}(k)=7.
\end{cases}
\]
Thus characteristic seven is exactly the exceptional prime in the indicated range for the **Jacobian syzygy degrees**, despite uniform logarithmic freeness.

Writing \(H_k(t)=\sum_{n\geq0}\dim_k(R/J_F)_n\,t^n\) for the Hilbert series of the gradient (Milnor) algebra, one has
\[
H_k(t)=\begin{cases}
\dfrac{1-3t^6+2t^9}{(1-t)^3},&\operatorname{char}(k)\ne7,\\[5pt]
\dfrac{1-3t^6+t^7+t^{11}}{(1-t)^3},&\operatorname{char}(k)=7,
\end{cases}
\]
within the stated field range. Their difference is \(t^7(1+t)^2/(1-t)\); in particular, the projective gradient scheme has length \(27\) in the first case and \(31\) in characteristic seven. This is a gradient-ideal statement, not an assertion that local Tjurina numbers jump.

## Assumptions and scope
The source arrangement is the corrected \(\mathcal{CL}_7\) equation in Dimca–Pokora (2022). Its original coordinates \((x,y,z)\) have conics \(x^2+y^2-z^2\) and \(x^2+y^2-4z^2\) and three tangent lines; replacing the second coordinate by \(Y=\sqrt3\,y\), clearing nonzero constants, and renaming \(Y\) as \(y\) yields precisely the displayed integral \(F\). This is a specified integral model: arithmetic claims are not asserted for every alternative integral coordinate presentation.

For \(\operatorname{char}(k)=0\) or \(p\ge5\), the two conics have nonzero diagonal quadratic determinants \(-9\) and \(-36\); they differ by \(9z^2\), hence are distinct. Each is smooth and irreducible over an algebraic closure. The three displayed lines are pairwise distinct, and no line is a factor of either conic. Hence \(F\) is squarefree over every such field. These observations are needed to apply the divisibility arguments below. Characteristics two and three are excluded because this integral product has nonreduced factors there.

## Proof
Define the Euler derivation coefficient triple \(E=(x,y,z)\), the quadrics
\[
A=y(3x-z),\qquad B=2x^2-xz-3y^2,
\]
and the homogeneous cubic triples
\[
\begin{aligned}
U={}&(-xyz+y^3,\;9x^3+27x^2z+8y^2z-36z^3,\\
&\hspace{35mm}3x^2y+3xyz+y^3-7yz^2),\\[4pt]
V={}&(-x^3+8x^2z-2xy^2+3y^2z-12z^3,\\
&\hspace{16mm}5x^2y-xyz,\;3x^3-x^2z+xy^2-7xz^2).
\end{aligned}
\]
Direct polynomial expansion over \(\mathbb Z[x,y,z]\), independently replayable by `verify.py`, gives four identities:
\[
E\cdot\nabla F=7F,\quad U\cdot\nabla F=AF,\quad V\cdot\nabla F=BF,
\qquad \det(E,U,V)=-3F. \tag{1}
\]
Here the three triples are the rows of the determinant. Since \(-3\) is a unit in every allowed characteristic, they are linearly independent over the fraction field and all belong to \(\operatorname{Der}(-\log F)\).

To show they generate that module, let \(T\) be any logarithmic derivation. Along the generic smooth point of each irreducible factor of \(F\), every logarithmic derivation (including \(T,E,U,V\)) preserves that factor and is tangent to its two-dimensional tangent hyperplane. Thus the determinant of any three of these logarithmic triples is divisible by each irreducible factor, hence by squarefree \(F\). Cramer's rule applied to (1) therefore expresses \(T\) as an \(R\)-linear combination of \(E,U,V\) with denominator \(-3F\) cancelled. This proves their claimed free basis for \(\operatorname{Der}(-\log F)\) over **every** allowed field, without specializing a characteristic-zero freeness computation.

For Jacobian syzygies, set
\[
P=7U-AE,\qquad Q=7V-BE,\qquad W=BU-AV.
\]
Identity (1) implies that \(P,Q,W\) annihilate \(F\). With \(\times\) denoting the usual cross product of triples, the determinant and logarithmic identities also give the exact integral relations
\[
P\times Q=-21\nabla F,\qquad
E\times W=-3\nabla F-7(U\times V). \tag{2}
\]
These can alternatively be verified by expansion. For \(p\ne7\), the scalar \(-21\) is invertible in every allowed characteristic. Consequently \(P,Q\) generate \(\operatorname{AR}(F)\) freely; their coefficient degrees are \((3,3)\). In characteristic seven, \(E\cdot\nabla F=0\), and the second identity in (2) becomes
\[
E\times W=-3\nabla F\qquad\text{in characteristic }7.
\]
The scalar \(-3\) is nonzero modulo seven, so \(E,W\) freely generate \(\operatorname{AR}(F)\), with degrees \((1,5)\).

For completeness, the generation argument in the preceding paragraph does not require a characteristic-zero syzygy criterion. First, the three partial derivatives have greatest common divisor one in every allowed characteristic. When \(p\ne7\), Euler's identity makes any common irreducible divisor of the partials divide \(F\); no factor of squarefree \(F\) divides all partials, because each component is generically smooth. In characteristic seven, suppose an irreducible \(g\) divides all partials. If \(g\mid F\), generic smoothness again rules it out. Otherwise the identities \(U(F)=AF\) and \(V(F)=BF\) force \(g\mid A\) and \(g\mid B\). But \(A=y(3x-z)\) and \(B=2x^2-xz-3y^2\) are coprime modulo seven: the restrictions of \(B\) to \(y=0\) and \(z=3x\) are respectively \(2x^2-xz\) and \(-x^2-3y^2\), both nonzero. Thus \(\gcd(F_x,F_y,F_z)=1\) also in characteristic seven. Whenever two syzygies \(P_0,Q_0\) satisfy \(P_0\times Q_0=c\nabla F\) for \(c\in k^*\), an arbitrary syzygy is a rational linear combination of them. Taking cross products with either generator shows that both rational coefficients multiply the primitive triple \(\nabla F\) to give polynomial triples. Coprimality of its three components forces those coefficients to lie in \(R\). The two syzygies are therefore a free basis. This applies to both cases of (2).

Finally, \(J_F\) has height two: its generators have no common divisorial factor and the arrangement has component intersections, so its projective gradient scheme is nonempty and zero-dimensional. The two free syzygy generators produce the minimal Hilbert–Burch resolution
\[
0\longrightarrow R(-6-a)\oplus R(-6-b)
\longrightarrow R(-6)^3\longrightarrow R\longrightarrow R/J_F\longrightarrow0,
\]
with \((a,b)=(3,3)\) or \((1,5)\) as above. Taking Hilbert series gives the stated formulas and the difference
\[
\frac{t^7+t^{11}-2t^9}{(1-t)^3}=\frac{t^7(1+t)^2}{1-t}.
\]
Their eventual graded dimensions are respectively \(27\) and \(31\), the lengths of the zero-dimensional projective schemes defined by \(J_F\).

## Verification
The accompanying standalone `verify.py` is pure Python (standard library only) and works with exact integer coefficient dictionaries. It reconstructs \(F\) from its five factors, differentiates it, checks all four identities in (1), checks both identities in (2), and checks their reductions in several finite characteristics. A separate exact linear-algebra check of the first graded Milnor pieces in characteristics five, seven, and eleven gave dimensions in degrees \(6,7,8,9,10,11\): \((25,27,27,27,27,27)\) for characteristics five and eleven, and \((25,28,30,31,31,31)\) in characteristic seven, consistent with the proven Hilbert-series formula. The all-characteristic conclusions follow from the integer identities and the algebraic generation arguments, not from the finite tests.

Reproduce the complete symbolic certificate with `python3 verify.py`; no external packages or unpublished files are required.

## Relationship to prior work
Dimca and Pokora classified complex conic–line configurations with nodes, tacnodes, and ordinary triple points, and established freeness of this complex arrangement, with characteristic-zero syzygy exponents \((3,3)\). Their published correction supplies the corrected three-line equation. A separate public mathematical note establishes that its complex projective stabilizer is \(S_3\) and describes the eight singular points. Neither the complex freeness computation nor the geometric stabilizer computation establishes the integral determinant \(-3F\), its simultaneous applicability to all fields of characteristic at least five, or the exceptional characteristic-seven Jacobian/Hilbert-series behavior.

In particular, a characteristic-zero free resolution cannot simply be reduced modulo a prime without verifying its rank and exactness. The displayed cubic syzygy pair itself has cross-product factor \(-21\) and therefore fails to be a basis in characteristic seven, whereas the integral logarithmic basis stays unimodular there. This separation of two notions of freeness is the additional arithmetic phenomenon.

## Limitations
The universal claim is restricted to the displayed integral model and fields of characteristic zero or at least five; it does not claim good behavior in characteristics two or three, or for integral presentations related by coordinate changes whose denominators are not units. The change at seven concerns the **gradient** Jacobian ideal and its syzygies, not a new count of geometric singular points or the local Tjurina algebra \(R/(F,F_x,F_y,F_z)\). No claims are made about other conic–line arrangements or characteristic-dependent topology.

## References
1. A. Dimca and P. Pokora, “On conic-line arrangements with nodes, tacnodes, and ordinary triple points,” arXiv:2111.12349, first public 24 November 2021; *Journal of Algebraic Combinatorics* 56 (2022), 403–424. https://arxiv.org/abs/2111.12349 ; https://doi.org/10.1007/s10801-022-01116-3 .
2. A. Dimca and P. Pokora, “Correction: On conic-line arrangements with nodes, tacnodes, and ordinary triple points,” *Journal of Algebraic Combinatorics* 56 (2022), 1339. https://doi.org/10.1007/s10801-022-01151-0 .
3. “Projective stabilizer of the unique free two-conic three-line arrangement,” a public mathematical result on the same complex configuration. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-projective-stabilizer-of-the-unique-free-two-conic-three-line-ar--5f6d49c915dc .
4. A. Dimca and E. Sernesi, “Syzygies and logarithmic vector fields along plane curves,” *Journal de l’École polytechnique — Mathématiques* 1 (2014), 247–267. https://doi.org/10.5802/jep.10 .
