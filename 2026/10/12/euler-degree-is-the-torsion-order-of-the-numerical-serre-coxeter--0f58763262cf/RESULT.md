# Euler degree is the torsion order of the numerical Serre–Coxeter coinvariants
## Finding
Let \(A\) be any positive \(4\times4\) Euler matrix in the Loginov--Orlov classification of three-dimensional minifolds, let \(B=A+A^{\mathsf T}\), and let \(T=-A^{-\mathsf T}A\), the integral matrix representing their numerical \(S^{-1}[3]\)-action. Then
\[
\operatorname{coker}(T-I)\cong\operatorname{coker}(B),
\qquad
\left|\operatorname{tors}\operatorname{coker}(T-I)\right|=D(A),
\]
where \(D(A)\) is the Euler degree of Loginov--Orlov. For the five mutation classes, ordered by \(D(A)=22,40,54,64,72\), the Smith normal forms of \(T-I\) are respectively
\[
\operatorname{diag}(1,1,22,0),\quad\operatorname{diag}(1,1,40,0),\quad\operatorname{diag}(1,3,18,0),\quad\operatorname{diag}(2,2,16,0),\quad\operatorname{diag}(1,1,72,0).
\]
Hence the corresponding coinvariant groups are \(\mathbf Z\oplus\mathbf Z/22\), \(\mathbf Z\oplus\mathbf Z/40\), \(\mathbf Z\oplus\mathbf Z/3\oplus\mathbf Z/18\), \(\mathbf Z\oplus\mathbf Z/2\oplus\mathbf Z/2\oplus\mathbf Z/16\), and \(\mathbf Z\oplus\mathbf Z/72\). In particular, the quadric-threefold and projective-three-space classes have noncyclic torsion coinvariants even though their torsion orders are the single Euler-degree numbers \(54\) and \(64\).

## Assumptions and scope
The statement concerns the five mutation classes of positive integral upper-unitriangular Euler matrices classified by Loginov--Orlov. Their convention is
\[
A=
\begin{pmatrix}
1&a&e&d\\
0&1&b&f\\
0&0&1&c\\
0&0&0&1
\end{pmatrix},
\qquad
B=A+A^{\mathsf T},
\qquad
T=-A^{-\mathsf T}A.
\]
The source proves that \(B\) has rank \(3\), that \(T\) represents the numerical action of \(S^{-1}[3]\), and that for a primitive generator \(p\in\ker(B)\cap\mathbf Z^4\),
\[
\operatorname{adj}(B)=D(A)pp^{\mathsf T}.
\]
No assertion is made for Euler matrices outside this classified positive rank-four setting, nor for a lift of the coinvariant group beyond numerical Grothendieck theory.

## Proof
Because \(A\) is upper unitriangular, \(A^{-\mathsf T}\in\operatorname{GL}_4(\mathbf Z)\). The source identity
\[
T-I=-A^{-\mathsf T}B
\]
therefore implies an isomorphism of integral cokernels
\[
\operatorname{coker}(T-I)\cong\operatorname{coker}(B).
\]

Since \(B\) has rank \(3\), this cokernel has free rank one. For a rank-three integral \(4\times4\) matrix, the order of the torsion subgroup of its cokernel is the third determinant divisor, namely the greatest common divisor of all \(3\times3\) minors. Those minors, up to signs and positions, are the entries of \(\operatorname{adj}(B)\). The source gives
\[
\operatorname{adj}(B)=D(A)pp^{\mathsf T},
\]
with \(p\) primitive. Hence the gcd of all adjugate entries is
\[
D(A)\,\gcd_{i,j}(p_ip_j)=D(A).
\]
Indeed, if a prime divided every \(p_ip_j\), then in particular it would divide every square \(p_i^2\), hence every \(p_i\), contradicting primitivity. Thus
\[
\left|\operatorname{tors}\operatorname{coker}(B)\right|=D(A),
\]
and the same holds for \(\operatorname{coker}(T-I)\).

For the five representatives in the source classification table, the parameter tuples
\[
(a,b,c,d,e,f)
\]
are
\[
(4,4,7,7,3,20),\ (5,5,5,5,3,18),\ (4,5,5,4,4,11),\
(4,4,4,4,6,6),\ (3,6,3,6,7,7).
\]
Taking gcds of minors of sizes \(1,2,3\) gives determinant divisors
\[
(1,1,22),\ (1,1,40),\ (1,3,54),\ (2,4,64),\ (1,1,72),
\]
so the Smith invariant factors are exactly
\[
(1,1,22),\ (1,1,40),\ (1,3,18),\ (2,2,16),\ (1,1,72).
\]
Appending the one free factor yields the five stated coinvariant groups.

## Verification
The accompanying `verify.py` reconstructs all five source matrices from the displayed parameter tuples using exact integer arithmetic. For each representative it:
1. constructs \(B=A+A^{\mathsf T}\);
2. computes the integral inverse of \(A\) from its nilpotent upper-triangular part;
3. reconstructs \(T=-A^{-\mathsf T}A\) and verifies \(T-I=-A^{-\mathsf T}B\);
4. computes every minor of sizes \(1,2,3,4\);
5. derives the Smith invariant factors from determinant divisors; and
6. checks both the advertised Smith form and that the torsion order equals the source Euler degree.

The saved replay output in `verification_output.txt` ends in `VERIFY_OK`. The finite computation is used only for the five classified representatives; the identity equating torsion order with \(D(A)\) for every positive matrix in the classified setting is proved symbolically above from the source adjugate formula.

## Relationship to prior work
Loginov--Orlov introduce the Euler degree \(D(A)\), prove the adjugate identity above, and use \(D(A)\) to distinguish the five braid-group mutation classes with degrees \(22,40,54,64,72\). Their checked full text also records the matrices \(B\), \(T\), and \(C=T^{-1}\). It does not state a Smith normal form, a cokernel computation, or an interpretation of \(D(A)\) as the order of torsion in numerical Serre--Coxeter coinvariants.

The present statement converts the source invariant into an intrinsic integral quotient of the numerical Grothendieck lattice and refines the scalar degree to the full abelian group for each class. The refinement is nontrivial for the quadric-threefold and projective-three-space classes, where the torsion is respectively \(\mathbf Z/3\oplus\mathbf Z/18\) and \(\mathbf Z/2\oplus\mathbf Z/2\oplus\mathbf Z/16\), rather than cyclic of orders \(54\) and \(64\).

## Limitations
The result is numerical: it computes the cokernel of the integral action on the rank-four numerical Grothendieck lattice and does not identify a categorical orbit construction or a topological invariant of an underlying threefold. It does not strengthen the source classification of mutation classes, since the scalar Euler degree already distinguishes the five classes. Its contribution is the integral interpretation of that degree and the complete Smith groups.

Older Coxeter-lattice literature could contain isolated computations for some commutative examples; targeted searches did not locate a theorem covering the uniform five-class statement or the new noncommutative degree-\(72\) case.

## References
1. A. Loginov and D. Orlov, *Non-commutative Fano varieties and three-dimensional minifolds*, arXiv:2609.39766v1, first public 30 September 2026. See the definitions of \(A,B,T,C\), the identity \(T-I=-A^{-\mathsf T}B\), the adjugate formula for \(D(A)\), and the five-class table.
