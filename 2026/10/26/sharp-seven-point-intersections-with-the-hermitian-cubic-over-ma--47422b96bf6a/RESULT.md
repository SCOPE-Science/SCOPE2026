# Sharp seven-point intersections with the Hermitian cubic over \(\mathbb F_4\)

## Finding
Let \(k=\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\), and fix the Hermitian cubic
\[
H:\quad X^3+Y^2Z+YZ^2=0\quad\text{in }\mathbb P^2_k.
\]
For every geometrically integral plane cubic \(C\ne H\) over \(k\),
\[
\#(C\cap H)(k)\le 7,
\]
and equality occurs for geometrically smooth cubics. Exactly **180** distinct cubics \(C\) attain equality, counting equations up to multiplication by \(k^\times\) in the fixed projective coordinates. For each of the \(\binom92=36\) unordered pairs \(\{A,B\}\subset H(k)\), exactly **five** such cubics omit precisely \(A,B\). Of these five, exactly two have \(\#C(k)=7\) and contact divisor \(3P+Q_1+\cdots+Q_6\) on \(H\); exactly three have \(\#C(k)=8\) and contact divisor \(2P+2Q+R_1+\cdots+R_5\). All points in these expressions are distinct rational points of \(H\). In particular, the 180 smooth extremizers split into counts **72** and **108** according to their \(k\)-rational point counts and contact patterns.

The smooth cubic
\[
C_0:\quad X^3+XY^2+XYZ+XZ^2+Y^3=0
\]
provides an explicit extremizer: it omits \([0:1:0]\) and \([0:1:1]\) among the nine points of \(H(k)\) and has eight \(k\)-points.

## Assumptions and scope
All forms are homogeneous ternary cubics with coefficients in the named four-element field, in one fixed projective plane with fixed \(H\). Cubic curves are counted as subschemes, so multiplying a defining equation by a nonzero scalar does not create another curve. No quotient by projective automorphisms is taken. Intersections count distinct \(k\)-rational geometric points rather than scheme length; the full intersection divisors stated above have scheme length nine. The upper bound concerns geometrically integral cubics distinct from \(H\); reducible cubics are not constrained by seven.

## Proof
**1. Nine points and the eight-point obstruction.** Put
\[
G=X(Y^2+YZ+Z^2).
\]
The scheme \(V(H,G)\) consists of nine transverse \(k\)-points. Indeed, on \(X=0\) they are \([0:1:0]\), \([0:0:1]\), and \([0:1:1]\). On \(Y^2+YZ+Z^2=0\), write \(Z=1\), choose \(Y\in\{\alpha,\alpha^2\}\), and choose \(X\in k^\times\), so \(X^3=1\); this gives six further points. Their gradients are transverse: at \(X=0\) the \(X\)-derivative of \(G\) is one, and at \(X\ne0\) the \(X\)-derivative of \(H\) is nonzero while that of \(G\) is zero. These are all nine \(H(k)\)-points since the Hermitian elliptic curve has \(2^3+1=9\) points over \(\mathbb F_4\).

The complete-intersection ideal of these reduced points is \((H,G)\); its degree-three part is exactly \(kH+kG\). Cayley–Bacharach for a transverse complete intersection of two cubics says that any cubic through eight of its nine points passes through the ninth. Equivalently, the nine point-evaluation functionals on ternary cubics have rank eight, with their unique linear dependence having no zero coefficient; the supplied linear-algebra verifier independently checks these ranks for each eight-point subset.

A cubic through all nine points is a projective member of \(kH+kG\). Apart from \(H\), all five members are reducible. Specifically,
\[
G=X(Y+\alpha Z)(Y+\alpha^2Z),
\]
and for \(\lambda\in k^\times\), choosing \(\tau\in k^\times\) with \(\tau^2=\lambda\) gives
\[
H+\lambda G=(X+\tau Y)(X+\tau Z)(X+\tau(Y+Z)),
\]
since \(\tau^3=1\). Hence no geometrically integral \(C\ne H\) can pass through eight or nine points of \(H(k)\), proving the sharp **upper bound seven**.

**2. An explicit smooth sharp example.** For \(C_0\), the three partial derivatives are
\[
(C_0)_X=X^2+Y^2+YZ+Z^2,\qquad
(C_0)_Y=XZ+Y^2,\qquad
(C_0)_Z=XY.
\]
If all vanish over an algebraic closure, then \(XY=0\). The case \(X=0\) forces \(Y=Z=0\); the case \(Y=0\) forces either \(X=0\), or \(Z=0\) and then \(X=0\). Neither is a projective point. Thus \(C_0\) is geometrically smooth. Direct evaluation at the nine listed Hermitian points shows it omits precisely \([0:1:0]\) and \([0:1:1]\). Its eighth rational point off \(H\) is \([1:0:1]\).

**3. Finite classification, with two complementary exhaustive methods.** There are ten degree-three monomials, hence \((4^{10}-1)/3=349525\) projective cubic equations. The first verifier evaluates every equation on all 21 points of \(\mathbb P^2(k)\). There are 576 equations vanishing at exactly seven \(H(k)\)-points, none at exactly eight, and five at all nine. Testing whether a form vanishes at all five points of any rational line detects an actual linear factor: its line restriction has degree three and cannot have five zeros without being identically zero. Exactly 180 of the 576 seven-point forms have no rational line factor.

The second verifier independently constructs the nullspace of the seven-by-ten monomial evaluation matrix for each of the 36 omitted pairs. This nullspace has dimension three. Its projective points comprise exactly 16 forms vanishing at exactly the seven retained Hermitian points, of which exactly five have no rational line factor. Two of the five have seven rational plane points and three have eight. It additionally computes their tangent gradients: the two seven-point companions have a single common tangent point with \(H\); the three eight-point companions have two common tangent points. This proves the announced 36-by-5 refinement, not merely the aggregate 180.

**4. Why the finite tests certify smoothness and the contact divisors.** A cubic with no \(k\)-rational line factor and at least seven \(k\)-points cannot be geometrically reducible: otherwise, in the absence of a rational line component, it would split as three Galois-conjugate geometric lines; all its rational points would lie in their at most three pairwise intersections. It is therefore geometrically integral. A singular geometrically integral cubic has normalization \(\mathbb P^1\) over \(k\) and at most one singular geometric point; it has at most \(\#\mathbb P^1(k)+1=6\) rational points. Consequently all 180 identified companions are geometrically smooth.

Because \(H\) is maximal over \(k=\mathbb F_4\), its Frobenius eigenvalues are both \(-2\). Thus \(\#H(\mathbb F_{16})=17-8=9=\#H(k)\): \(H\) has no closed points of degree two. For a cubic meeting \(H\) in seven distinct rational points, Bézout leaves residual intersection length two. No two-degree closed point can occur, and neither of the two omitted rational points belongs to \(C\). Therefore the extra length is supported among the seven rational intersection points, with only two multiplicity patterns possible: one multiplicity three, or two multiplicities two. For two smooth curves, contact multiplicity at least two is equivalent to coincidence of tangent lines. The exact tangent-gradient computation above distinguishes the two patterns and completes the classification.

## Verification
From the directory containing the supplied code, run:

```sh
g++ -O2 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive
./verify_exhaustive
python3 verify_linear_algebra.py
```

Expected final markers: `VERIFY_EXHAUSTIVE_OK` and `VERIFY_LINEAR_ALGEBRA_OK`. The C++ program traverses all nonzero coefficient vectors modulo \(k^\times\); its independent Python counterpart traverses only the rank-three nullspaces of the 36 seven-point constraints. Both use exact polynomial arithmetic in \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\). Neither relies on probabilistic tests, external computational systems, precomputed tables, or floating point arithmetic. The formulas for \(H\), \(G\), and \(C_0\) are also independently verified by the algebraic arguments above.

## Relationship to prior work
Beelen, Datta, Montanucci and Niemann explicitly report the failure of full nine-point intersection for irreducible cubics in the exceptional case \((q,d)=(2,3)\) (arXiv:2407.13521, introduction). This finding strengthens that binary failure to the sharp bound seven and classifies **all** smooth extremizers, their omitted pairs, ambient point totals and intersection-multiplicity patterns. The general construction displayed in their Theorem 2.2 specializes in this small case to \(H+G=(X+Y)(X+Z)(X+Y+Z)\), which is reducible, so it supplies no competing integral cubic here. Homma's classification of maximal plane cubics over \(\mathbb F_4\) concerns cubics with nine rational points and is not a classification of their intersections with a fixed Hermitian cubic; no maximal eight- or nine-point companion is asserted by that work. The Cayley–Bacharach obstruction itself is classical and not claimed as new; the sharp extremal construction and complete refined census are the assessed contribution.

## Limitations
The numerical classification is for the single small field \(\mathbb F_4\) and cubics in fixed projective coordinates; it is not a parameter-uniform theorem in \(q\), and 180 is not an isomorphism-class count. The finite programs supply a reproducible exact certificate of the enumerative portion; the accompanying geometric proof is needed to justify irreducibility, smoothness and the intersection scheme. Global novelty cannot be proved from searchable literature, and independently repeated external audit has not been performed.

## References
- P. Beelen, M. Datta, M. Montanucci, J. T. Niemann, *Intersection of irreducible curves and the Hermitian curve*, arXiv:2407.13521 (first public version July 18, 2024); *Journal of Algebra* **671** (2025), 75–94, DOI 10.1016/j.jalgebra.2025.02.036.
- M. Homma, *On maximal plane curves of degree 3 over F4, and Sziklai's example of degree q−1 over Fq*, *J. Algebra Comb. Discrete Appl.* **11** (2024), 127–138, DOI 10.13069/jacodesmath.v11i2.273.
- Cayley–Bacharach theorem for plane complete intersections, in its classical \((3,3)\) nine-point case.
