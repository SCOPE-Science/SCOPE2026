# The missing \(q=2\) exception in the minimal \(\operatorname{AGL}(2,q)\)-invariant quartic pencil

## Finding

The family in Theorem 4.5 of Borges--Korchmáros--Speziali has a boundary exception at \(q=2\). In that case the affine quotient in their equation (8) is
\[
Q(x,y)=x^4+y^4+x^2y^2+x^2y+x^2+xy^2+xy+y^2+1.
\]
Writing the projective member \(Q-\lambda=0\) as
\[
F_\lambda=X^4+Y^4+X^2Y^2+X^2YZ+X^2Z^2+XY^2Z+XYZ^2+Y^2Z^2+(1+\lambda)Z^4,
\]
one obtains a sharp dichotomy: \(F_\lambda=0\) is smooth, hence geometrically irreducible, for every \(\lambda\ne1\), whereas
\[
F_1=(X(X+Z)+\alpha Y(Y+Z))(X(X+Z)+\alpha^2Y(Y+Z))
\]
for \(\alpha^2+\alpha+1=0\). The exceptional member is therefore the union of two smooth \(\mathbb F_4\)-conjugate conics. They meet transversely at exactly the four affine \(\mathbb F_2\)-points, so the reducible member has four ordinary transverse double points.

Consequently, in the \(q=2\) specialization, the irreducible curves in the displayed Theorem 4.5 pencil are exactly the members with \(\lambda\ne1\).

## Assumptions and scope

Work over an algebraic closure \(K\) of \(\mathbb F_2\). The parameter \(\lambda\) ranges over \(K\). The statement concerns the line-stabilizer \(\operatorname{AGL}(2,2)\) pencil appearing in Theorem 4.5 and does not identify it with the distinct point-stabilizer pencil considered later in the source.

The source equation is used exactly as printed. The division defining the quotient is performed in \(K[x,y]\); the quotient is a polynomial for \(q=2\), as verified below. No assertion is made here about other values of \(q\), about the source's separate lower-degree arguments, or about full automorphism groups of the quartics.

## Proof

Set
\[
N=(x^8-x)(y^2-y)-(y^8-y)(x^2-x),\qquad
D=(x^4-x)(y^2-y)-(y^4-y)(x^2-x).
\]
Polynomial division in characteristic \(2\) gives \(N=DQ\) with
\[
Q=x^4+y^4+x^2y^2+x^2y+x^2+xy^2+xy+y^2+1.
\]
Homogenizing \(Q-\lambda\) gives \(F_\lambda\) above.

In characteristic \(2\),
\[
\frac{\partial F_\lambda}{\partial X}=YZ(Y+Z),\qquad
\frac{\partial F_\lambda}{\partial Y}=XZ(X+Z),\qquad
\frac{\partial F_\lambda}{\partial Z}=XY(X+Y).
\]
The common zero locus of these three derivatives in \(\mathbb P^2_K\) is exactly \(\mathbb P^2(\mathbb F_2)\). Indeed, when \(Z=0\), the last equation leaves the three points \([1:0:0]\), \([0:1:0]\), and \([1:1:0]\). When \(Z\ne0\), normalize \(Z=1\); the first two equations force \(X,Y\in\mathbb F_2\), giving four affine points.

At each of the three points at infinity, \(F_\lambda=1\). At each of the four affine \(\mathbb F_2\)-points,
\[
F_\lambda=1+\lambda.
\]
Thus \(F_\lambda=0\) has no singular point when \(\lambda\ne1\). A reducible projective plane curve over an algebraically closed field has intersecting positive-degree components and is therefore singular at an intersection point; hence every smooth \(F_\lambda\) is geometrically irreducible.

For \(\lambda=1\), put
\[
U=X(X+Z),\qquad V=Y(Y+Z).
\]
Then \(F_1=U^2+UV+V^2\). If \(\alpha\in\mathbb F_4\setminus\mathbb F_2\) satisfies \(\alpha^2+\alpha+1=0\), then
\[
U^2+UV+V^2=(U+\alpha V)(U+\alpha^2V).
\]
For the first conic \(A=U+\alpha V\), its gradient is
\[
(A_X,A_Y,A_Z)=(Z,\alpha Z,X+\alpha Y).
\]
A common zero of the gradient would have \(Z=0\) and \(X=\alpha Y\); substituting into \(A\) gives \(Y^2\), so there is no projective singular point. The conjugate conic is smooth by the same argument.

The two conics meet where \(U=V=0\). There is no such projective point on \(Z=0\), while on \(Z=1\) the equations are \(X(X+1)=Y(Y+1)=0\). Hence the intersection consists of the four affine \(\mathbb F_2\)-points. At each one, the first two components of the two gradients form the matrix
\[
\begin{pmatrix}1&\alpha\\1&\alpha^2\end{pmatrix},
\]
whose determinant is \(\alpha+\alpha^2=1\). Therefore all four intersections are transverse.

## Verification

The supplied script `verification/verify.py` performs the quotient division over \(\mathbb F_2\), checks the three partial derivatives, checks the values at all seven derivative-critical projective points, verifies the \(\mathbb F_4\) factorization modulo \(\alpha^2+\alpha+1\), and verifies smoothness of both conic factors. A fresh replay with SymPy \(1.14.0\) returns:

`VERIFY_OK q=2_exception=lambda=1 factors=2_smooth_F4_conics smooth_else=all_lambda_ne_1`

The exhaustive geometric step is the symbolic derivative analysis in the proof; finite enumeration is used only after the derivative equations have proved that every possible singular point is \(\mathbb F_2\)-rational.

## Relationship to prior work

Borges--Korchmáros--Speziali state in Theorem 4.5 that the \(\operatorname{AGL}(2,q)\)-invariant irreducible curves of the displayed minimum degree are given by equation (8) with \(\lambda\in K\), without a \(q=2\) exclusion. Their later Theorem 4.9 concerns the non-conjugate point-stabilizer subgroup and prints a \(\lambda\ne1\) exclusion there; it does not state the present line-stabilizer \(q=2\) factorization.

Statement-level searches for the exact source, \(q=2\) specialization, \(\lambda=1\), \(\mathbb F_4\)-conjugate conics, and equivalent reducibility/smoothness formulations did not locate a published correction or a result implying this exact exceptional member. The closest indexed results concern unrelated quartics or finite-field group actions and do not imply the claim.

## Limitations

The claim is only about the \(q=2\) specialization of the displayed line-stabilizer pencil. It does not re-prove every part of the source's global minimum-degree theorem and does not assert that no informal, unpublished, or poorly indexed correction exists. The source metadata prints the primary automorphism-of-curves MSC code with an apparent extra leading digit; the valid subject code used here is \(14H37\).

## References

1. H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic \(p\)*, arXiv:2202.05765v1, submitted 11 February 2022; especially Theorems 4.3--4.5 and equation (8).
2. H. Borges, G. Korchmáros, P. Speziali, *Plane curves with a large linear automorphism group in characteristic \(p\)*, Finite Fields and Their Applications 96 (2024), 102402, DOI:10.1016/j.ffa.2024.102402.
