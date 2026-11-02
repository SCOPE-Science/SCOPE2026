# Arithmetic bitangents of the Klein quartic in characteristic five

## Finding
Let \(C\subset\mathbf P^2_{\mathbf F_5}\) be the smooth plane quartic
\[
 C:\quad X^3Y+Y^3Z+Z^3X=0.
\]
Let \(B\) denote its reduced geometric bitangent-line locus in the dual projective plane. Its scheme of geometric points is finite étale of degree \(28\) over \(\mathbf F_5\). In affine dual coordinates \([a:b:1]\) representing the line \(aX+bY+Z=0\), the entire bitangent locus is given by the exact equations
\[
 b=a^{26},\qquad P(a)=a^{28}-a^{21}+2a^{14}+2a^7+1=0.
\]
The polynomial \(P\) is squarefree and its six irreducible factors over \(\mathbf F_5\) have degrees \(1,3,6,6,6,6\). Thus geometric Frobenius on the \(28\) bitangent lines has exactly these six orbit lengths. Equivalently,
\[
 Z(B/\mathbf F_5,T)=\frac1{(1-T)(1-T^3)(1-T^6)^4},\qquad
 \#B(\mathbf F_{5^m})=1+3\mathbf1_{3\mid m}+24\mathbf1_{6\mid m}\quad(m\ge1).
\]
The unique rational bitangent is \(X+Y+Z=0\). All the bitangents are rational over \(\mathbf F_{5^6}\), with this the minimal common field of definition.

## Assumptions and scope
All polynomials, ideal computations, and factorization assertions are over \(\mathbf F_5\). A bitangent means a line whose intersection divisor with the smooth plane quartic is twice an effective divisor of degree two, allowing coincident contact points. The locus \(B\) here is the *reduced* geometric finite locus with its natural Galois descent; no claim is made about an arbitrary nonreduced contact scheme or about integral models other than the displayed equation. The quartic is smooth because if its three partial derivatives vanish, no homogeneous coordinate can vanish, and multiplying their nonzero-coordinate relations gives \(1=(-3)^3=3\) in \(\mathbf F_5\), a contradiction.

## Proof
**1. Square-of-quadratic criterion.** For the line \(Z=-aX-bY\), the restricted quartic is \(Q(X,Y)=\sum_{i=0}^{4}c_iX^{4-i}Y^i\) with
\[
(c_0,c_1,c_2,c_3,c_4)=(-a^3,\ 1-3a^2b,\ -3ab^2,\ -a-b^3,\ -b).
\]
If \(c_0\ne0\), the form is a nonzero scalar times a square of a quadratic over an algebraic closure if and only if
\[
 8c_0^2c_3=c_1(4c_0c_2-c_1^2),\qquad
 64c_0^3c_4=(4c_0c_2-c_1^2)^2.
\]
Indeed, normalizing the quadratic leading coefficient to one determines its other two coefficients from \(c_0,c_1,c_2\) because \(2\) is invertible; the remaining two equations are exactly those displayed. Write their left-minus-right sides as \(f,g\).

**2. Exact elimination.** Polynomial arithmetic over \(\mathbf F_5\) gives the reduced lexicographic Gröbner basis (with \(b\) eliminated first)
\[
 (f,g)=(b-a^{26},\ P(a)),\qquad P(a)=a^{28}-a^{21}+2a^{14}+2a^7+1.
\]
The supplied verifier checks equality of the full Gröbner bases rather than merely checking that proposed roots satisfy the equations. Since \(P(0)=1\), all roots have \(a\ne0\), so the square-of-quadratic criterion applies without dividing by zero. The Euclidean calculation \(\gcd(P,P')=1\) shows that there are exactly \(28\) distinct geometric solutions. These are \(28\) distinct bitangent lines. The classical odd-theta-characteristic count gives exactly \(28\) bitangents for any smooth nonhyperelliptic genus-three curve in characteristic unequal to two; therefore the solutions already exhaust the dual plane, including the omitted affine chart \(c=0\).

**3. Frobenius factorization.** The irreducible factors of \(P\) over \(\mathbf F_5\) are
\[
\begin{aligned}
 &(a-1),\\
 &(a^3-a^2-1),\\
 &(a^6-2a^4-a^3+a^2-a+1),\\
 &(a^6+a^5+a^4+a^3+a^2+a+1),\\
 &(a^6+2a^5-a^3+2a^2-a+1),\\
 &(a^6-a^5+a^3-a^2+2a+1).
\end{aligned}
\]
The verifier recomputes their product and establishes irreducibility by the finite-field Rabin criterion using modular polynomial powers and gcd calculations, not by testing a bounded sample of elements. The coefficients \(b=a^{26}\) lie in the same residue field as \(a\); the six factor degrees are exactly the closed-point degrees of \(B\), proving the orbit lengths, the zeta function, and all extension-field counting formulas.

**4. Rational check.** The only root of \(P\) in \(\mathbf F_5\) is \(a=1\), and then \(b=1\). Direct substitution gives the identity
\[
 F(X,Y,-X-Y)=-(X^2+XY+Y^2)^2\quad\text{in characteristic }5.
\]
This proves directly that \(X+Y+Z=0\) is a rational bitangent.

## Verification
Run \(\texttt{python verify.py}\) with Python 3 and SymPy 1.13 or later. The source is standalone apart from SymPy. It derives the restricted coefficients, checks the exact Gröbner basis, squarefreeness and factor degrees, verifies factor irreducibility using polynomial modular powering, checks smoothness and the rational-line identity, and prints `VERIFY_OK`. The included `verify.out` records one completed successful run. These exact symbolic checks certify the finite polynomial identities; the general statement for all field extensions additionally uses the proved correspondence between irreducible factors and Frobenius orbits.

## Relationship to prior work
The classical \(28\) bitangents of the Klein quartic, the line \(X+Y+Z=0\), and their complex automorphism-group orbit geometry are **not** new (Elkies, 1998, especially the proposition on the \(28\) Sylow-three subgroups). Plaumann–Sturmfels–Vinzant (public preprint 2010-08-24) develop the classical bitangent algorithms and theta-characteristic geometry; their treatment does not give the above characteristic-five Frobenius decomposition. The later explicit bitangent equations in Janasz–Pokora–Zieliński concern a different complex normal form; converting these to arithmetic data for the specified \(\mathbf F_5\) model requires control of the descent, and the inspected account does not provide this particular factorization. The distinct characteristic-three hyperflex scheme of this quartic has the same *numerical* orbit-length multiset but concerns a different prime and a different geometric locus: it does not imply this bitangent classification. The contribution assessed here is strictly the displayed finite-field dual equation and associated Galois orbit, zeta, and field-of-definition classification.

## Limitations
Historical priority remains provisional: an unindexed source or a previously implicit rational bitangent table could cover the stated arithmetic decomposition; no claim of exhaustive historical uniqueness is made. Only the reduced bitangent-line locus for the specified \(\mathbf F_5\) plane model is classified. No independent scientific audit or independent validation has been performed.

## References
1. N. D. Elkies, *The Klein Quartic in Number Theory*, MSRI Publications 35 (1998), particularly the 28-bitangent proposition: https://library.slmath.org/books/Book35/files/elkies.pdf (full text, pp. 64–65 inspected).
2. D. Plaumann, B. Sturmfels, C. Vinzant, *Quartic Curves and Their Bitangents*, arXiv:1008.4104, first posted 2010-08-24: https://arxiv.org/abs/1008.4104 (introductory and algorithmic sections inspected).
3. J. Janasz, P. Pokora, K. Zieliński, *On arrangements of smooth plane quartics and their bitangents* (2025), Section 3.1 and bitangent equations inspected: https://www.researchgate.net/publication/388786535_On_arrangements_of_smooth_plane_quartics_and_their_bitangents.
