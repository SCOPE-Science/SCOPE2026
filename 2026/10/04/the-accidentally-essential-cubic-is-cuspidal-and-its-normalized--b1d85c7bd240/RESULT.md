# The accidentally essential cubic is cuspidal and its normalized kernel map is a conic

## Finding

For the symmetric determinantal plane cubic \(X=V(\det A)\subset\mathbb P^2\) from Kulkarni--Vemulapalli's explicitly "accidentally essential" example, over an algebraically closed field of characteristic zero, \(X\) is an irreducible rational cubic with a unique singular point \(p=[1:0:0]\), and that singularity is of type \(A_2\). Its Cayley variety is exactly the reduced point \(q=[1:0:0]\). The normalization \(\nu:\mathbb P^1\to X\) can be written \([u:v]\mapsto[-u^3+20u^2v-125uv^2+250v^3:u^3-6u^2v:u^2v]\); after normalization the kernel map extends across \(\nu^{-1}(p)\) to the quadratic morphism \([u:v]\mapsto[2(u-5v)^2:-u(2u-5v):u^2]\), which is an isomorphism onto the smooth conic \(Y_0Y_2=2(Y_1+Y_2)^2\) and sends the cusp preimage to \(q\).

## Assumptions and scope

Work over an algebraically closed field \(k\) of characteristic zero.  Let
\[
A=x_0\begin{pmatrix}0&0&0\0&0&0\0&0&1\end{pmatrix}
+x_1\begin{pmatrix}0&1&2\1&3&4\2&4&5\end{pmatrix}
+x_2\begin{pmatrix}0&6&7\6&8&9\7&9&10\end{pmatrix},
\]
the single-block tensor displayed by Kulkarni--Vemulapalli.  Their example records that \(p=[1:0:0]\) is essential, while \(q=[1:0:0]\) lies on the associated Cayley variety and satisfies the incidence condition.  The claim here concerns the exact global cubic, the scheme structure of that Cayley variety, and the extension of the kernel map after normalization.

## Proof

A direct determinant expansion gives
\[
F=-x_0x_1^2-12x_0x_1x_2-36x_0x_2^2-x_1^3+2x_1^2x_2+7x_1x_2^2+4x_2^3.
\]
The first partial derivative is \(F_{x_0}=-(x_1+6x_2)^2\).  On \(x_1=-6x_2\), the second partial becomes \(-125x_2^2\).  Hence the projective singular locus is exactly \(p=[1:0:0]\).

Put \(s=x_1+6x_2\), \(t=x_2\), and \(X=x_0+s-20t\).  Then
\[
F=-Xs^2-125st^2+250t^3.
\]
Since \(X(p)=1\), on the affine chart \(X=1\) the equation is equivalent to
\[
s^2+125st^2-250t^3=0.
\]
After \(w=s+\frac{125}{2}t^2\), this becomes
\[
w^2=250t^3\left(1+\frac{125}{8}tight).
\]
The factor in parentheses is a unit with a formal (equivalently analytic over \(\mathbb C\)) cube root, so a local coordinate change gives \(w^2-z^3=0\).  Thus \(p\) is an \(A_2\) cusp.

The following base-point-free cubic parametrization lies on \(X\):
\[

u([u:v])=[-u^3+20u^2v-125uv^2+250v^3:u^3-6u^2v:u^2v].
\]
Away from \(p\), its inverse is \([u:v]=[x_1+6x_2:x_2]\).  Therefore it is birational onto an irreducible cubic and is the normalization of \(X\).

Write Cayley coordinates as \([a:b:c]\).  Its three defining quadrics are
\[
c^2,
\]
\[
2ab+4ac+3b^2+8bc+5c^2,
\]
\[
12ab+14ac+8b^2+18bc+10c^2.
\]
Set-theoretically \(c=0\); the last two equations then force \(b=0\).  Thus the support is only \(q=[1:0:0]\).  On the affine chart \(a=1\), the Jacobian of the latter two quadrics with respect to \((b,c)\) at \(q\) has determinant \(-20\), so the local ideal is the maximal ideal.  Hence the full Cayley scheme is the single reduced point \(q\).

Along \(
u\), the adjugate factors exactly as
\[
\operatorname{adj}A(
u([u:v]))=-u^2yy^T,
\quad
y=\begin{pmatrix}2(u-5v)^2\-u(2u-5v)\u^2\end{pmatrix}.
\]
Consequently \(A(
u([u:v]))y=0\).  The three quadratic coordinates of \(y\) have no common zero, so they extend the kernel map to all of \(\mathbb P^1\).  They satisfy
\[
Y_0Y_2=2(Y_1+Y_2)^2,
\]
and this conic is smooth.  Since the morphism is given by a base-point-free degree-two system and its image has degree two, it has degree one onto the conic; hence it is an isomorphism.  At \(u=0\), \(y=[1:0:0]=q\).

## Verification

The bundled `verify_accidentally_essential.py` reconstructs \(F\), checks the singular-locus reductions, verifies the local coordinate identity, validates the normalization and its rational inverse, computes the Cayley quadrics and the nonzero Jacobian determinant \(-20\), proves the adjugate rank-one factorization entrywise, checks the conic equation and smoothness, and terminates with `VERIFY_OK`.

## Relationship to prior work

Kulkarni--Vemulapalli introduce this exact matrix to show that the closed conditions defining essential singularities and Cayley incidence can overlap; they state that \(p\) is essential, \(q\) belongs to the Cayley variety, and \(A(p,q,\cdot)=0\).  Their surrounding results describe kernel and Gauss maps away from essential singularities, but the example does not identify the cubic's unique singularity type, the Cayley scheme as a reduced singleton, or the normalized kernel map and its conic image.  Kerner--Vinnikov give a general theory of kernel sheaves for singular determinantal hypersurfaces; that framework does not compute these explicit invariants for this tensor.  Targeted database and literature searches for the exact example, its matrix coefficients, \(A_2\)-cusp language, normalization, and kernel-conic formulation did not locate a statement implying the combined result.

## Limitations

The proof is for this explicit tensor and characteristic zero.  Several displayed reductions use coefficients divisible by \(2\) and \(5\), so no positive-characteristic uniformity is claimed.  The \(A_2\) designation is a local analytic/formal classification; the normalization and conic statements are global for this cubic.  Absence from the searches is not a proof that no equivalent classical description exists under different terminology.

## References

1. A. Kulkarni and S. Vemulapalli, *On intersections of symmetric determinantal varieties and theta characteristics of canonical curves*, arXiv:2109.08740v1 (17 September 2021), especially the example following Theorem 4.0.4 and Section 4.1.
2. D. Kerner and V. Vinnikov, *Determinantal representations of singular hypersurfaces in \(\mathbb P^n\)*, Adv. Math. 231 (2012), 1619--1654; arXiv:0906.3012.
