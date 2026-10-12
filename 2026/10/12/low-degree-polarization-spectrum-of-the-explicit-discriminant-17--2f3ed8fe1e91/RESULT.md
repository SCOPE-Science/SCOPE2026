# Low-degree polarization spectrum of the explicit discriminant-17 K3 surface
## Finding
For the explicit complex K3 surface \(X_4\) studied by Festi--Nijgh--Platt, let \(H\) be the quartic hyperplane class and \(C\) the genus-two quintic class. The source proves
\[
\operatorname{Pic}(X_4)=\mathbb ZH\oplus\mathbb ZC,\qquad
\begin{pmatrix}H^2&H\!\cdot\! C\\ H\!\cdot\! C&C^2\end{pmatrix}=
\begin{pmatrix}4&5\\5&2\end{pmatrix}.
\]
The complete list of primitive ample classes of square at most \(16\) is
\[
\begin{array}{c|l}
A^2&\text{primitive ample classes}\\ \hline
2&C\\
4&H,\;-H+5C\\
8&3H-C,\;-3H+14C\\
16&H+C,\;-H+6C.
\end{array}
\]
There are no primitive ample classes of square \(6\), \(10\), \(12\), or \(14\). Thus degree \(16\) is the first primitive polarization degree strictly above the source's degree-eight polarization, and the two square-\(16\) classes form one orbit under the source's involution.

## Assumptions and scope
The statement concerns the explicit smooth complex quartic \(X_4\) and Picard lattice computed in the cited source. The source also identifies the two \((-2)\)-curves
\[
D=2H-C,\qquad D'=-2H+9C,
\]
and gives an involution satisfying \(\iota^*C=C\) and \(\iota^*H=-H+5C\). The claim is only the polarization census through square \(16\); it does not assert a complete spectrum in all degrees.

## Proof
Write \(A=xH+yC\), and put
\[
p=A\!\cdot\!D=3x+8y,\qquad q=A\!\cdot\!D'=37x+8y.
\]
Solving gives
\[
x=\frac{q-p}{34},\qquad y=\frac{37p-3q}{272}.
\]
Substitution into the intersection form yields the exact identity
\[
A^2=4x^2+10xy+2y^2
   =\frac{p^2+66pq+q^2}{2176}.
\]
The source constructs \(D,D'\) as the two \((-2)\)-curves. For completeness, their exclusivity also follows directly from the lattice chamber: if an irreducible \((-2)\)-curve \(E\) distinct from both existed, then \(E\!\cdot\!D\ge0\) and \(E\!\cdot\!D'\ge0\); the displayed quadratic identity would force \(E^2\ge0\), a contradiction. Therefore, in the positive cone component containing \(H\), a class is ample exactly when
\[
p>0\quad\text{and}\quad q>0.
\]
Indeed \(H\!\cdot\!A=(9p+q)/16>0\) under these inequalities.

If \(A^2\le16\), then
\[
p^2+66pq+q^2\le34816,
\]
so \(pq\le527\). Hence there are only finitely many positive integer pairs \((p,q)\) to check. Imposing the two divisibility conditions that make \(x,y\) integral, then \(\gcd(x,y)=1\), gives precisely the classes in the table. Direct substitution gives their squares \(2,4,8,16\) and excludes \(6,10,12,14\).

Finally,
\[
\iota^*(xH+yC)=-xH+(5x+y)C,
\]
so the square-four, square-eight, and square-sixteen pairs above are exactly involution pairs, while \(C\) is fixed.

## Verification
The accompanying exact-integer verifier enumerates every positive pair \((p,q)\) allowed by \(pq\le527\), reconstructs \((x,y)\) from the inverse formulas, checks integrality, primitivity, the intersection identity, and the involution pairing, and compares the result with the displayed spectrum. No floating-point computation is used.

## Relationship to prior work
Festi--Nijgh--Platt compute the Picard lattice, the two involutions, degree-two, degree-four, and degree-eight polarizations, and explicitly observe that the lattice does not represent square \(6\). The source does not give the complete primitive ample spectrum through square \(16\). The present result closes that next natural low-degree window and shows that squares \(10\), \(12\), and \(14\) are absent while square \(16\) occurs in one involution orbit.

## Limitations
This is a finite low-degree classification inside one rank-two Picard lattice. It does not classify all primitive ample classes of \(X_4\), determine projective models for the square-\(16\) polarization, or claim that no equivalent lattice-theoretic observation appears in older literature under different terminology.

## References
1. D. Festi, W. Nijgh, D. Platt, *K3 surfaces with two involutions and low Picard number*, arXiv:2210.14623v1; later published in *Geometriae Dedicata*, DOI 10.1007/s10711-024-00900-8.
