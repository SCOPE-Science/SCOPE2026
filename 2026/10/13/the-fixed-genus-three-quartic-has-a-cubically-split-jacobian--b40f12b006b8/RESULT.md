# The fixed genus-three quartic has a cubically split Jacobian
## Finding
Let \(C\subset \mathbb P^2_{\mathbb C}\) be the genus-three fixed curve from Example 4.1 of Comparin--Montero--Prieto-Montañez--Troncoso:
\[
x_0^4+x_1^4+x_2^4+6(x_0^2x_1^2-x_1^2x_2^2+x_0^2x_2^2)=0.
\]
The three nonidentity coordinate-sign involutions form a Klein four group \(G\). Their quotient curves are elliptic. One quotient is
\[
E_+: w^2=t^4+3t^2+1,
\]
and the other two are
\[
E_-: w^2=t^4-3t^2+1.
\]
The change \(t\mapsto it\) gives \(E_+\cong E_-\) over \(\mathbb C\). Both have \(j=148176/25\). Moreover,
\[
\operatorname{Jac}(C)\sim E^3
\]
over \(\mathbb C\), where \(E\) is either quotient elliptic curve.

## Assumptions and scope
The base field is \(\mathbb C\). The curve is exactly the fixed plane quartic printed in Example 4.1 of arXiv:2312.14722. The statement concerns unpolarized isogeny of abelian varieties; it does not identify the principal polarization with a product polarization and it does not claim an isomorphism \(\operatorname{Jac}(C)\cong E^3\).

## Proof
Write
\[
F=x^4+y^4+z^4+6(x^2y^2-y^2z^2+x^2z^2).
\]
The coordinate sign changes are projective involutions, and their product is scalar, so their images form \(G\cong (\mathbb Z/2\mathbb Z)^2\).

First quotient by \(x\mapsto -x\). On \(z=1\), set \(t=y\) and \(X=x^2\). The invariant function field satisfies
\[
X^2+6(t^2+1)X+t^4-6t^2+1=0.
\]
Completing the square gives a genus-one model with right side \(32(t^4+3t^2+1)\), so after rescaling the square coordinate the quotient is \(E_+\). Quotienting by \(y\mapsto-y\), and likewise by \(z\mapsto-z\), gives discriminant \(32(t^4-3t^2+1)\), hence \(E_-\). Since \(9-4\ne0\), both quartics on the right have distinct roots. Substitution \(t=is\) turns \(t^4+3t^2+1\) into \(s^4-3s^2+1\), giving \(E_+\cong E_-\) over \(\mathbb C\).

For
\[
E_a:\quad w^2=t^4+a t^2+1,
\]
use \(u=(w+1)/t^2\), \(v=t(u^2-1)\), \(X=2u\), and \(Y=2v\). This gives
\[
Y^2=(X^2-4)(X+a)=X^3+aX^2-4X-4a.
\]
Its Weierstrass invariants are
\[
c_4=16(a^2+12),\qquad \Delta=256(a^2-4)^2,
\]
so
\[
j(E_a)=\frac{16(a^2+12)^3}{(a^2-4)^2}.
\]
At \(a=\pm3\) this is \(148176/25\).

The full \(G\)-quotient is obtained from \([x:y:z]\mapsto[x^2:y^2:z^2]\). Its image is
\[
Q:\quad X^2+Y^2+Z^2+6XY-6YZ+6XZ=0.
\]
The associated symmetric matrix has determinant \(-80\), so \(Q\) is a smooth conic and has genus zero. Let \(q_i:C\to E_i\) be the three degree-two quotient maps. Each \(q_i^*H^0(E_i,\Omega^1)\) is the one-dimensional invariant subspace for the corresponding involution. Because \(H^0(C,\Omega_C^1)^G=H^0(Q,\Omega_Q^1)=0\), the three nontrivial characters of \(G\) account for all three dimensions of \(H^0(C,\Omega_C^1)\). Hence the sum map
\[
E_1\times E_2\times E_3\longrightarrow \operatorname{Jac}(C)
\]
induced by pullback has an isomorphism on tangent spaces and is therefore an isogeny. Since the three \(E_i\) are isomorphic over \(\mathbb C\), \(\operatorname{Jac}(C)\sim E^3\).

## Verification
The standalone verifier checks the two quotient discriminants, the determinant \(-80\) of the conic matrix, the Weierstrass invariants for \(a=\pm3\), and the exact value \(j=148176/25\). Running `python verification/verify.py` returns the recorded `VERIFY_OK` line. The isogeny step is a representation-theoretic proof, not a finite experiment.

## Relationship to prior work
Comparin--Montero--Prieto-Montañez--Troncoso give the K3 surface, the fixed smooth genus-three quartic, its degree-two del Pezzo quotient, its Néron--Severi lattice, and the large projective automorphism group of the ambient K3 surface. They do not state the three elliptic quotient models, their common \(j\)-invariant, or the resulting cube isogeny for the fixed curve. Howe--Leprévost--Poonen develop general split-Jacobian constructions for genus-three curves; general Ciani-quartic work explains the three-factor mechanism. The present statement is the equation-level specialization for this fixed curve, including the coincidence of all three factors and the exact \(j\)-invariant.

## Limitations
The result is over \(\mathbb C\). Although the displayed curve and quotient equations are defined over \(\mathbb Q\), the explicit identification \(E_+\cong E_-\) used here employs \(i\). No claim is made about the minimal field over which all factors become mutually isomorphic, the exact kernel of the product isogeny, the induced polarization type, or arithmetic ranks and torsion.

## References
1. P. Comparin, P. Montero, Y. Prieto-Montañez, S. Troncoso, *On strictly elliptic K3 surfaces and del Pezzo surfaces*, arXiv:2312.14722, first posted 2023-12-22; Example 4.1.
2. E. W. Howe, F. Leprévost, B. Poonen, *Large torsion subgroups of split Jacobians of curves of genus two or three*, arXiv:math/9809210; Forum Math. 12 (2000), 315--364.
