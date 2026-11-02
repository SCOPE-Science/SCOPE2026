# Two Frobenius isogeny types of smooth plane-filling quintics over \(\mathbb F_3\)

## Finding
Put \(U=Y^3Z-YZ^3\), \(V=Z^3X-ZX^3\), and \(W=X^3Y-XY^3\). Every geometrically smooth plane quintic over \(\mathbb F_3\) containing all thirteen points of \(\mathbb P^2(\mathbb F_3)\) belongs to one of exactly two projective-equivalence classes. These contain respectively \(144\) and \(432\) scalar-normalized quintic equations. The projective classification follows from the established Tallini/Homma--Kim normal form; the additional assertion here is their complete Weil-polynomial and Jacobian isogeny distinction.

Representatives are
\[
 C_s:\quad YU+ZV+(2X+Y)W=0,\qquad
 C_g:\quad YU+ZV+(X+2Z)W=0.
\]
Both are smooth genus-six curves. Their Hasse--Weil numerators \(P_C(T)=\exp(\sum_{n\ge1}(\#C(\mathbb F_{3^n})-3^n-1)T^n/n)\) are
\[
 P_{C_s}(T)=(1+3T+5T^2+9T^3+9T^4)^3
\]
and
\[
\begin{aligned}
P_{C_g}(T)={}&1+9T+42T^2+131T^3+308T^4+601T^5+1067T^6\\
&+1803T^7+2772T^8+3537T^9+3402T^{10}+2187T^{11}+729T^{12}.
\end{aligned}
\]
The polynomial \(P_{C_g}\) is irreducible over \(\mathbb Q\), while the quartic factor of \(P_{C_s}\) is irreducible. Hence the ordinary Jacobian of \(C_g\) is a simple abelian sixfold over \(\mathbb F_3\); the Jacobian of \(C_s\) is \(\mathbb F_3\)-isogenous to the cube of a simple ordinary abelian surface. In particular their Jacobian group orders are respectively \(16589\) and \(19683\).

## Assumptions and scope
All curves, coordinate changes, polynomial coefficients, isogenies, and point counts in this statement are defined over \(\mathbb F_3\). The curve must be smooth geometrically, not merely at its thirteen rational points. Equation counts are counts of scalar-normalized homogeneous equations in fixed coordinates; they are not counts of abstract isomorphism classes. Two curves related by a rational projective transformation have the same Weil polynomial. No claim about all genus-six curves over \(\mathbb F_3\) is made.

## Proof
1. The space of quintic forms vanishing on the thirteen rational projective points has the form \(F_A=[X,Y,Z]A[U,V,W]^t\) for a \(3\times3\) matrix \(A\) over \(\mathbb F_3\). Its matrix kernel is exactly the scalar matrices. The geometric smoothness criterion in Homma--Kim is that the characteristic polynomial of \(A\) be irreducible of degree three. The eight monic irreducible cubics occur as characteristic polynomials of exactly \(432\) matrices each, because an irreducible matrix has centralizer \(\mathbb F_{27}^{\times}\). Replacing \(A\) by \(uA+vI\) for \(u\in\mathbb F_3^{\times}\), \(v\in\mathbb F_3\), does not alter the scalar-normalized equation. The eight irreducible cubics form two affine-root orbits of sizes \(2\) and \(6\), yielding \(144\) and \(432\) equations. The projective transformation law makes matrices equivalent by similarity up to this affine-scalar operation; therefore precisely two projective classes occur. The representative matrices are companions of \(t^3+2t+1\) and \(t^3+t^2+2\).
2. Count projective solutions to each displayed homogeneous quintic over \(\mathbb F_{3^n}\), for \(1\le n\le6\), by exact arithmetic in polynomial-basis fields. Independently compute the same counts by evaluating the companion form with primitive-power multiplication tables. Both methods yield
\[
\begin{array}{c|rrrrrr}
n&1&2&3&4&5&6\\\hline
\#C_s(\mathbb F_{3^n})&13&13&55&13&208&913\\
\#C_g(\mathbb F_{3^n})&13&13&16&117&273&640
\end{array}
\]
In each computation every affine point \((x,y,1)\) and each point \((1,y,0)\), \((0,1,0)\) is included once; each finite-field operation is exact.
3. For \(S_n=3^n+1-\#C(\mathbb F_{3^n})\), the first six coefficients of \(P_C(T)=\sum_{k=0}^{12}a_kT^k\), \(a_0=1\), follow from Newton's formula \(na_n=-\sum_{j=1}^n a_{n-j}S_j\). The genus-six functional equation fixes the rest: \(a_{12-k}=3^{6-k}a_k\) for \(0\le k\le5\). Direct integer reconstruction yields exactly the two polynomials above, establishing their values over every extension field, not merely the six counted extensions.
4. The quartic \(1+3T+5T^2+9T^3+9T^4\) and the degree-twelve polynomial \(P_{C_g}\) are each irreducible modulo \(2\), as the standalone Euclidean/GF(2) irreducibility certificate checks. Thus both are irreducible over \(\mathbb Q\). The first is an ordinary abelian-surface Weil polynomial, because its middle coefficient \(5\) is prime to \(3\); the generic degree-twelve polynomial is ordinary because its middle coefficient \(1067\) is prime to \(3\). By the Tate/Honda--Tate isogeny classification, the corresponding Jacobians have respectively the stated cube and simple isogeny structures. Summing the Weil coefficients evaluates the group orders.

## Verification
The standalone standard-library scripts `verify_orbits.py`, `verify_points_polynomial.py`, `verify_points_independent.py`, and `verify_weil.py` reconstruct the matrix classification, the two degree-\(1\) through degree-\(6\) point-count arrays, both full Weil polynomials, and GF(2) irreducibility. Run each with `python3 <filename>` in any directory. Expected final lines are `MATRIX_CLASSIFICATION_OK`, `POLYNOMIAL_BASIS_COUNTS_OK`, `INDEPENDENT_POINT_COUNTS_OK`, and `WEIL_CERTIFICATE_OK`. No downloaded tables or previous scripts are required. The independent point counters use different polynomial bases and evaluation routes; neither deduces a general statement by extrapolating finite experiments. The geometric classification and smoothness criterion are established published theorems, explicitly cited below.

## Relationship to prior work
Homma and Kim supply the plane-filling matrix normal form, smoothness test, and the underlying projective-equivalence mechanism. Cunha proves ordinarity of the relevant prime-field Tallini curves; thus ordinarity and the two projective types are not proposed as discoveries here. The additional content is the exact two-polynomial zeta classification, its arithmetic separation of a simple sixfold from the cube of an abelian surface, and the resulting all-extension point formulas. Asgarli and Ghioca study nearby plane-filling existence questions, but not this Frobenius-polynomial census.

## Limitations
The arithmetic computations pertain to the precise smooth degree-five, thirteen-point family over \(\mathbb F_3\). The full extension-point conclusions use the smooth genus-six functional equation and the cited classification, not an unsupported infinite inference from six counts. An unindexed earlier computation of this zeta spectrum would overlap the claimed contribution; no global originality certification is asserted. Independent external validation has not been performed.

## References
1. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, arXiv:0903.1918 (2009), https://arxiv.org/abs/0903.1918.
2. D. Cunha, *Curves containing all points of the projective plane over a finite field*, Journal of Pure and Applied Algebra, first online 21 November 2017, DOI: 10.1016/j.jpaa.2017.11.008; open preprint arXiv:1805.07345.
3. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree*, arXiv:2307.03072 (2023).
4. J. Tate, *Endomorphisms of abelian varieties over finite fields*, Invent. Math. 2 (1966), 134--144; Honda--Tate classification of finite-field isogeny classes.
