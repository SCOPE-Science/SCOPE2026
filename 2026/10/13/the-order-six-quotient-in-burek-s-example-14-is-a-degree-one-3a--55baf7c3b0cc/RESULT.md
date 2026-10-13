# The order-six quotient in Burek’s Example 14 is a degree-one \(3A_2\) del Pezzo tower
## Finding
For the complex K3 surface \(X\subset\mathbb P^4\) in Burek's Example 14, defined by
\[
x_0^2-x_1^2-x_2x_3+x_2x_4=0,\qquad
x_0^3+x_2^3+x_3^3+x_0x_2x_4+x_3x_4^2=0,
\]
with \(\sigma[x_0:x_1:x_2:x_3:x_4]=[x_0:-x_1:\omega x_2:\omega^2x_3:\omega^2x_4]\), where \(\omega^3=1\) and \(\omega\ne1\), let \(\iota=\sigma^3\). Then \(X/\langle\iota\rangle\) is the smooth cubic surface
\[
Y:\ a^3+b^3+c^3+abd+cd^2=0\subset\mathbb P^3_{[a:b:c:d]},
\]
and the residual automorphism \(\tau[a:b:c:d]=[a:\omega b:\omega^2c:\omega^2d]\) has exactly three fixed points on \(Y\), with tangent weights \((1,2)\) modulo \(3\). Consequently \(Z=X/\langle\sigma\rangle\cong Y/\langle\tau\rangle\) is a Gorenstein del Pezzo surface of degree \(1\) with exactly three \(A_2\) singularities. The double cover \(X\to Y\) is branched along the smooth genus-four curve \(C=Y\cap\{a^2-bc+bd=0\}\); all three \(\tau\)-fixed points lie on \(C\), and the quotient curve \(C/\langle\tau\rangle\) has genus \(1\).

## Assumptions and scope
Everything is over \(\mathbb C\). The statement concerns only the explicit complete-intersection K3 surface and order-six automorphism in Burek's Example 14. It does not classify quotients of arbitrary K3 surfaces with purely non-symplectic automorphisms of order six.

## Proof
Write
\[
F=a^3+b^3+c^3+abd+cd^2,\qquad Q=a^2-bc+bd.
\]
The involution \(\iota=\sigma^3\) changes only the sign of \(x_1\). On \(X\), the quadric equation is
\[
x_1^2=x_0^2-x_2x_3+x_2x_4.
\]
Hence the invariant coordinates
\[
[a:b:c:d]=[x_0:x_2:x_3:x_4]
\]
identify the quotient by \(\iota\) with the cubic surface \(Y=V(F)\subset\mathbb P^3\), and \(X\to Y\) is the double cover obtained by adjoining a square root of \(Q\). Its branch divisor is \(C=V(F,Q)\subset\mathbb P^3\).

The partial derivatives of \(F\) are
\[
F_a=3a^2+bd,\quad F_b=3b^2+ad,\quad F_c=3c^2+d^2,\quad F_d=ab+2cd.
\]
Solving \(F=F_a=F_b=F_c=F_d=0\) in the four standard affine charts gives no projective point, so \(Y\) is smooth. Likewise, the common zero locus of \(F,Q\) and all \(2\times2\) minors of the Jacobian matrix of \((F,Q)\) is empty; thus \(C\) is smooth. Since \(C\) is a smooth complete intersection of degrees \(2\) and \(3\) in \(\mathbb P^3\),
\[
2g(C)-2=2\cdot3\,(2+3-4)=6,
\]
so \(g(C)=4\).

The residual order-three automorphism is
\[
\tau[a:b:c:d]=[a:\omega b:\omega^2c:\omega^2d].
\]
Its projective fixed locus in \(\mathbb P^3\) is the union of the two eigenpoints \([1:0:0:0]\), \([0:1:0:0]\), and the eigenline \(L=\{a=b=0\}\). The two eigenpoints do not lie on \(Y\), because \(F=1\) there. On \(L\),
\[
F|_L=c(c^2+d^2),
\]
which has three distinct projective zeros. Thus \(\tau\) has exactly three fixed points on \(Y\). Also \(Q|_L=0\), so all three lie on \(C\).

At a fixed point on \(L\), divide the ambient eigenvalues by the eigenvalue \(\omega^2\) of the point. The three tangent directions in \(\mathbb P^3\) then have weights \(1,2,0\) modulo \(3\). The weight-zero direction is tangent to \(L\), but \(Y\cap L\) is reduced at each fixed point, so that direction is not tangent to \(Y\). Therefore
\[
T_pY\cong \chi_1\oplus\chi_2.
\]
The quotient germ is consequently the cyclic quotient \(\frac1{3}(1,2)\), which is the Du Val singularity \(A_2\). Away from these three points the order-three action is free in codimension one, so \(Z=Y/\langle\tau\rangle\) is normal and
\[
K_Y=\pi^*K_Z.
\]
The three quotient singularities are Gorenstein. Since \(-K_Y\) is ample and \(\pi\) is finite, \(-K_Z\) is ample. Moreover,
\[
K_Y^2=3,\qquad K_Z^2=\frac{K_Y^2}{3}=1.
\]
Thus \(Z\) is a Gorenstein del Pezzo surface of degree \(1\) with singularity basket \(3A_2\).

Finally, \(\tau|_C\) has precisely the same three fixed points. Each has ramification index \(3\). Riemann--Hurwitz for \(C\to C/\langle\tau\rangle\) gives
\[
2\cdot4-2=3\bigl(2g'-2\bigr)+3(3-1),
\]
hence \(g'=1\).

## Verification
The included script `verify_burek_quotient.py` performs exact symbolic checks. It verifies projective smoothness of \(Y\) chart by chart using Gröbner bases, verifies smoothness of \(C\) from the complete-intersection Jacobian minors, checks that \(c(c^2+d^2)\) is square-free, and checks the canonical-degree and Riemann--Hurwitz arithmetic. A fresh copy of the included script was replayed successfully and returned `VERIFY_OK`.

## Relationship to prior work
Burek's Example 14 supplies the explicit K3 model, the order-six automorphism, and the fixed loci of \(\sigma\), \(\sigma^2\), and \(\sigma^3\). The inspected source does not identify the involution quotient as a cubic surface, the residual quotient as a degree-one \(3A_2\) del Pezzo surface, or the genus of the branch-curve quotient.

Dolgachev and Martin give a broad classification framework for automorphisms of del Pezzo surfaces, including cubic surfaces and fixed-locus information. The inspected passages do not state this equation-level quotient tower for Burek's surface.

## Limitations
The result is specific to this explicit surface and automorphism. The originality search cannot exclude an older projectively equivalent presentation of the same cubic or degree-one del Pezzo quotient under different coordinates or terminology. The statement does not determine the full automorphism groups of \(Y\) or \(Z\), and it does not add a classification theorem beyond this concrete quotient tower.

## References
1. D. Burek, *Fixed-locus relations and purely non-symplectic automorphisms of order 6 on K3 surfaces*, arXiv:2312.07253.
2. I. Dolgachev and G. Martin, *Automorphisms of del Pezzo surfaces in odd characteristic*, arXiv:2303.16170; J. London Math. Soc. (2024), e12905.
