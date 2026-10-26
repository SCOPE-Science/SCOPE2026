# Frobenius cycles and the zeta function of a cyclic 21-node inseparable sextic

## Finding

Let \(k=\mathbb F_2\), and let \(Y\subset\mathbb P_k(1,1,1,3)\) be the double plane
\[
 w^2=G(x,y,z):=x^5y+y^5z+z^5x.
\]
For the minimal resolution \(X\longrightarrow Y\), the 21 geometric singularities are ordinary double points, with explicit weighted-projective representatives
\[
 Q_u=[1:u^5:u:u^{13}],\qquad u^{21}=1.
\]
Their arithmetic Frobenius orbit lengths are \(1,2,3,3,6,6\). For all \(n\ge1\),
\[
 \#X(\mathbb F_{2^n})=2^{2n}+2^n+1+2^n\gcd(21,2^n-1),
\]
and consequently its full Hasse–Weil zeta function is
\[
 Z(X,T)=\frac{1}{(1-T)(1-4T)(1-2T)^2(1-4T^2)(1-8T^3)^2(1-64T^6)^2}.
\]
The exceptional curves are simultaneously defined over \(\mathbb F_{64}\), and no smaller finite extension defines all of them.

## Assumptions and scope

The ground field is exactly \(\mathbb F_2\), with arithmetic Frobenius acting on coordinates by squaring. The hypersurface equation is weighted homogeneous of degree six with weights \((1,1,1,3)\). The map \(Y\to\mathbb P^2\) is the finite purely inseparable double plane, and \(X\) denotes the canonical minimal resolution of its rational double points. Zeta functions use the normalization \(Z(X,T)=\exp(\sum_{n\ge1}\#X(\mathbb F_{2^n})T^n/n)\). All assertions about points hold for every positive integer \(n\), not merely the checked small fields.

## Proof

**The geometric critical scheme.** In characteristic two, the homogeneous derivatives are
\[
 G_x=x^4y+z^5,\quad G_y=x^5+y^4z,\quad G_z=y^5+z^4x.
\]
A projective critical point cannot have \(x=0\): then \(G_z=y^5=0\) and \(G_x=z^5=0\), contradicting projectivity. Put \(x=1\), and write \(t=y\), \(u=z\). The equations are
\[
 t+u^5=0,\qquad 1+t^4u=0,\qquad t^5+u^4=0.
\]
The first gives \(t=u^5\); the second becomes \(u^{21}=1\), and the third then becomes \(u^{25}+u^4=u^4(u^{21}+1)=0\). Conversely each of the 21 roots of \(u^{21}=1\) gives a critical point. Because the derivative of \(u^{21}-1\) is \(u^{20}\), nonzero at every root, the critical scheme is reduced of length 21. At such a point,
\[
 G(1,u^5,u)=u^5+u^{26}+u^5=u^{26}=u^5.
\]
The unique square root of \(u^5\) is \(u^{13}\), since \(u^{26}=u^5\). Therefore the singular points of \(Y\) are exactly the displayed \(Q_u\).

**Local singularity type and resolution.** In local coordinates centered at \((t,u)=(u_0^5,u_0)\), the mixed quadratic coefficient of \(G\) is \(\partial_t\partial_u G=t^4=u_0^{20}\ne0\). In characteristic two the quadratic part of the surface equation consists of \(w'^2\), two possible pure squares, and a nonzero mixed term. Over the algebraic closure a linear change of the fiber coordinate removes the pure squares, giving the nondegenerate double-point tangent cone \(w'^2+st\), hence an \(A_1\) rational double point. Equivalently, Shimada's Proposition 3.4 states that a reduced zero-dimensional critical scheme of a purely inseparable sextic double plane is equivalent to precisely these \(A_1\) singularities. The resolution replaces each point by a smooth geometrically irreducible exceptional conic (a \((-2)\)-curve); it is defined over the residue field of its singular point. All the blowups and the resolution descend to \(\mathbb F_2\). By the known general theorem for these 21-node sextic double planes, \(X\) is a supersingular K3 surface. No new proof of that general theorem is asserted here.

**Frobenius arithmetic.** Arithmetic Frobenius sends \(Q_u\) to \(Q_{u^2}\). For a root of order \(d\) dividing 21, its orbit length is the multiplicative order of 2 modulo \(d\). At \(d=1,3,7,21\) these lengths are respectively \(1,2,3,6\); there are \(\varphi(d)=1,2,6,12\) roots of each order. Thus the orbit profile is
\[
 1+2+(3+3)+(6+6)=21.
\]
In particular all nodes and exceptional curves split over \(\mathbb F_{2^6}\), and a 6-cycle excludes a smaller common extension. Equivalently the number of nodes rational over \(\mathbb F_{2^n}\) is \(r_n=\gcd(21,2^n-1)\).

**Point counts.** For each finite extension \(\mathbb F_q/\mathbb F_2\), the squaring map is a bijection on \(\mathbb F_q\). Hence every \(\mathbb F_q\)-point of \(\mathbb P^2\) has exactly one point lying above it on the purely inseparable double plane: \(\#Y(\mathbb F_q)=q^2+q+1\). A rational node is replaced in its minimal resolution by a smooth conic over \(\mathbb F_q\); such a conic has \(q+1\) rational points, contributing exactly \(q\) more than the removed node. Non-rational singular points make no contribution to this \(\mathbb F_q\)-count. Therefore
\[
 \#X(\mathbb F_q)=q^2+q+1+q\,r_n,\qquad q=2^n.
\]
Finally the Frobenius permutation of the 21 nodes has cycles of lengths \(1,2,3,3,6,6\). Its fixed-point counts satisfy
\[
 r_n=\sum_{\ell\in\{1,2,3,3,6,6\}\,,\ \ell\mid n}\ell.
\]
The identity \(\exp(\sum_{n\ge1}\ell\mathbf1_{\ell\mid n}(2T)^n/n)=(1-(2T)^\ell)^{-1}\) gives
\[
 Z(X,T)=\frac1{(1-T)(1-2T)(1-4T)}
 \prod_{\ell\in\{1,2,3,3,6,6\}}\frac1{1-2^\ell T^\ell},
\]
which simplifies to the displayed formula. Its degree-22 middle factor agrees with the Betti number of a K3 surface.

**Natural cyclic symmetry.** Over \(\overline{\mathbb F}_2\), an element \(a\) with \(a^{21}=1\) acts on the double-plane model through
\[
 [x:y:z:w]\longmapsto[x:ay:a^{-4}z:a^{11}w].
\]
Each monomial of \(G\) scales by \(a\), and \(w^2\) scales by \(a^{22}=a\). The action on nodes is \(u\mapsto a^{-4}u\), a regular action because 4 is invertible modulo 21. This identifies the critical scheme as a natural cyclic torsor, rather than an arbitrarily chosen 21-point configuration.

## Verification

The accompanying standalone script `verify_cyclic_k3.py` implements exact binary-polynomial arithmetic for \(\mathbb F_{2^n}\) with \(n\in\{1,2,3,4,6\}\), enumerates all projective-plane rational points, recomputes the Jacobian critical scheme, tests the nonzero mixed quadratic coefficient, checks the unique square root, and directly computes the Frobenius orbits over \(\mathbb F_{64}\). It reports \((q,\#X(\mathbb F_q))=(2,9),(4,33),(8,129),(16,321),(64,5505)\), the cycle list \((1,2,3,3,6,6)\), and `VERIFY_OK`. The proof above establishes the claims for every extension; finite enumeration is only a cross-check.

## Relationship to prior work

Dolgachev–Kondō (public arXiv version 2001-12-27, §4.2) construct a characteristic-two supersingular K3 via the different sextic \(x_0x_1x_2(x_0^3+x_1^3+x_2^3)\). Its critical points are all 21 points of \(\mathbb P^2(\mathbb F_4)\), with Frobenius behavior different from the present cyclic 21-torsor. The prior source establishes the special 21-node geometry but does not print this model's arithmetic formula. Shimada (2003, especially Example 1.3, Examples 1.4–1.6, Proposition 3.4 and Proposition 3.13) develops the general singularity-to-K3 framework and other explicit sextics. These results imply the K3 and supersingularity statements here; the claimed computation is specifically the cyclic model's critical scheme, Frobenius cycle type, and all-extension zeta function. Kedlaya–Sutherland (2015) study zeta functions for a different projective family, smooth quartic K3 surfaces over \(\mathbb F_2\). Comparisons use mathematical statements and the actual displayed equations, not merely titles or the number 21.

## Limitations

The Artin invariant, full geometric automorphism group, and geometric isomorphism class are not determined. The finite-field arithmetic of the displayed model is established, but an equivalent zeta calculation hidden in less-accessible literature or an arithmetic twist/table under a different coordinate presentation is a residual originality risk. The cycle type distinguishes the displayed model from the cited \(\mathbb F_2\)-presentation of the Dolgachev–Kondō double plane, not necessarily their geometric surfaces over an algebraic closure. No claim of independent review or machine-certified infinite reasoning is made.

## References

1. I. Dolgachev and S. Kondō, *A supersingular K3 surface in characteristic 2 and the Leech lattice*, arXiv:math/0112283, first public 2001-12-27; §4.2. https://arxiv.org/html/math/0112283v2
2. I. Shimada, *Supersingular K3 surfaces in characteristic 2 as double covers of a projective plane*, arXiv:math/0311073, first public 2003-11-06; §1, Proposition 3.4, Proposition 3.13, Examples 1.3–1.6. https://arxiv.org/html/math/0311073v1
3. K. S. Kedlaya and A. V. Sutherland, *A census of zeta functions of quartic K3 surfaces over* \(\mathbb F_2\), arXiv:1511.06945, first public 2015-11-22; §§1–3. https://arxiv.org/html/1511.06945v3
