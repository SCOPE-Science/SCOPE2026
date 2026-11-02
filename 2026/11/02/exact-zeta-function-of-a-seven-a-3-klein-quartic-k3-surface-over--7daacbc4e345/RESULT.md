# Exact zeta function of a seven-\(A_3\) Klein quartic K3 surface over \(\mathbb F_2\)

## Finding
Let \(V\subset\mathbb P^3_{\mathbb F_2}\), with coordinates \([x:y:z:w]\), be the quartic
\[
V:\quad w^4+x^3y+y^3z+z^3x=0.
\]
Let \(S\to V\) be its minimal resolution. For every integer \(n\ge1\), write \(q=2^n\) and \(\delta_d(n)=1\) when \(d\mid n\), and zero otherwise. Then \(V\) is geometrically normal, with exactly seven \(A_3\) singularities, and \(S\) is a K3 surface. Its point counts are
\[
\#S(\mathbb F_{2^n})=q^2+1+q\bigl(2+2\delta_2(n)+6\delta_3(n)+12\delta_6(n)\bigr).
\]
In particular, these counts for \(n=1,2,3,4,5,6\) are respectively \(9,33,129,321,1089,5505\). The exact Hasse–Weil zeta function is
\[
Z(S/\mathbb F_2,T)=\frac{1}{(1-T)(1-4T)(1-2T)^2(1-4T^2)(1-8T^3)^2(1-64T^6)^2}.
\]
The geometric exceptional curves have Frobenius cycle type \(1^1 2^1 3^2 6^2\) on their 21 components. Together with the hyperplane class this yields the displayed degree-22 Frobenius factor.

## Assumptions and scope
All schemes and fields have characteristic two. A *geometric singularity* means a point over an algebraic closure; rational points and zeta functions refer to the indicated finite base field. The assertion concerns the **minimal smooth resolution** \(S\), not the singular quartic \(V\). No assertion about the Artin invariant or complete Néron–Severi lattice is made. The exponent notation on Frobenius cycle types denotes multiplicities of cycles, not exponentiation of a point count.

## Proof
**1. The seven singularities.** Put \(B=x^3y+y^3z+z^3x\). The dehomogenized polynomial \(B(1,y,z)\) is not a square in \(\overline{\mathbb F}_2(y,z)\): its derivative with respect to \(y\) is \(1+y^2z\ne0\). Hence \(w^4+B\) is irreducible over the rational-function field and \(V\) is geometrically integral. The partial derivatives of \(V\) are
\[
B_x=x^2y+z^3,\qquad B_y=x^3+y^2z,\qquad B_z=y^3+z^2x,\qquad (w^4)_w=0.
\]
At a projective singularity \(x\ne0\), since \(x=0\) would successively force \(z=0\) and \(y=0\). Set \(x=1\) and \(y=t\). The derivative conditions yield \(t\ne0\), \(z=t^{-2}\), and \(t^7=1\); the third derivative then vanishes automatically. At these points,
\[
B(1,t,t^{-2})=t+t+t^{-6}=t
\]
since \(t^7=1\) and \(3=1\) in characteristic two. Because fourth powers are bijective on every finite extension and on the algebraic closure, the unique singular point above this parameter is
\[
P_t=[1:t:t^{-2}:t^2],\qquad t^7=1.
\]
The roots of \(t^7-1\) are distinct, so there are exactly seven. Their Frobenius action is \(t\mapsto t^2\). It fixes \(t=1\) and acts in two three-cycles on the other six roots. Thus exactly \(s_n=1+6\delta_3(n)\) singular points are rational over \(\mathbb F_{2^n}\).

**2. Their local analytic type and arithmetic tangent cones.** In the affine chart \(x=1\), write \(y=t+u\), \(z=t^{-2}+v\), and \(w=t^2+s\). The linear part vanishes and the quadratic tangent form is
\[
Q_t(u,v)=t^{-1}u^2+t^2uv+t^{-2}v^2.
\]
The coefficient of \(uv\) is nonzero, so this is a nondegenerate binary quadratic form. By the formal Morse lemma for a two-variable nondegenerate critical point in characteristic two, over the algebraic closure one may replace \(u,v\) with formal local coordinates \(U,V\) in which \(B-B(P_t)=UV\). The completed local equation is therefore \(UV+s^4=0\), an \(A_3\) rational double point. In particular, \(V\) has only isolated rational double points, is normal by Serre's criterion, and its minimal resolution is a smooth K3 surface by adjunction and crepantness.

The tangent directions are obtained by putting \(h=u/v\) in \(Q_t=0\). With \(h=t^3j\), the equation becomes
\[
j^2+j+1=0.
\]
This is irreducible over \(\mathbb F_2\), has roots in \(\mathbb F_4\), and has roots in \(\mathbb F_{2^n}\) precisely when \(n\) is even. Thus every rational singularity has nonsplit tangent directions over an odd-degree extension, and split directions over an even-degree extension. This conclusion includes both the degree-one singular point and the two degree-three orbits.

**3. Rational points of the exceptional fibers.** The minimal resolution of \(UV+s^4=0\) is obtained by blowing up the singular point and then the single residual \(A_1\) singularity. The first exceptional tangent cone consists geometrically of two lines, and the second blowup inserts a central \(\mathbb P^1\) between their strict transforms, giving an \(A_3\)-chain of three \((-2)\)-curves. The two outer components are distinguished by the two factors of \(Q_t\); the central component is defined over the residue field of the singular point. Over a field containing that residue field, the outer components are interchanged by Frobenius exactly when \(Q_t\) is nonsplit.

Fix \(q=2^n\) and a \(\mathbb F_q\)-rational singular point. If \(n\) is odd, the outer components are exchanged, are disjoint, and have no \(\mathbb F_q\)-points. The central rational exceptional curve has \(q+1\) points, so the exceptional fiber replaces the singular point by \(q+1\) points, a net gain of \(q\). If \(n\) is even, all three components are \(\mathbb P^1\)'s over \(\mathbb F_q\), and their two transverse intersection points are rational; the exceptional fiber has \(3(q+1)-2=3q+1\) points, a net gain of \(3q\). A singular point not rational over \(\mathbb F_q\) contributes no rational points to its exceptional fiber. Consequently
\[
\#S(\mathbb F_q)=\#V(\mathbb F_q)+q(1+2\delta_2(n))(1+6\delta_3(n)).
\]

**4. The purely inseparable projection and zeta function.** Projection \([x:y:z:w]\mapsto[x:y:z]\) is defined everywhere on \(V\): the point \([0:0:0:1]\) does not lie on \(V\). For every point of \(\mathbb P^2(\mathbb F_q)\), there is exactly one fourth root \(w\in\mathbb F_q\) of \(B(x,y,z)\), and the result is compatible with rescaling homogeneous coordinates. Hence \(\#V(\mathbb F_q)=q^2+q+1\) for every \(q=2^n\). Substitution into the previous formula gives
\[
\#S(\mathbb F_q)=q^2+1+q\bigl(2+2\delta_2(n)+6\delta_3(n)+12\delta_6(n)\bigr).
\]
For \(d\ge1\), the formal power-series identity
\[
\exp\left(\sum_{n\ge1}\frac{d\delta_d(n)(2T)^n}{n}\right)=\frac{1}{1-(2T)^d}
\]
then gives the exact zeta function stated above. The exceptional-center components have Frobenius cycles \(1^1 3^2\); the outer components have cycles \(2^1 6^2\). Adding the invariant pullback of a hyperplane gives \(1^2 2^1 3^2 6^2\) on the 22-dimensional span of divisor classes. The intersection matrix of the seven \(A_3\) chains and the hyperplane class is nondegenerate, and a K3 surface has second Betti number 22, so this also accounts for all of \(H^2_{\mathrm{\acute et}}(S_{\overline{\mathbb F}_2},\mathbb Q_\ell)\) for \(\ell\ne2\).

## Verification
The accompanying standalone Python 3 file `verify_klein_k3.py` implements the fields \(\mathbb F_{2^n}\) by polynomial arithmetic, \(1\le n\le6\). It exhaustively evaluates the original homogeneous quartic on **every** projective \(\mathbb F_{2^n}\)-point, extracts all singular points by the three partial derivatives, checks the predicted \(7\)-th-root parametrization, and counts the rational factors of the local quadratic tangent cone. It separately reconciles the local two-blowup point correction with the closed formula. Its success marker is `KLEIN_SEVEN_A3_FROBENIUS_ZETA_CHECKS_PASS`. These finite checks corroborate, but do not replace, the proof for all \(n\).

## Relationship to prior work
Catanese and Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078 (first public version October 6, 2021), establish in §3.2 the general construction \(w^4+B(x,y,z)=0\) and prove that a general plane quartic \(B\) produces seven \(A_3\) singularities; their §3.5 also uses the cyclic quartic form \(x^3y+y^3z+z^3x\) in another model. These geometric facts and the general theory of rational double points are *prior results*. Here the additional claim is the exact Frobenius behavior of the seven specified singularities and their outer exceptional components, which yields the zeta function of this explicitly defined \(\mathbb F_2\)-model. Katsura and Kondō, arXiv:1010.5835, describe other configurations on a supersingular characteristic-two K3 surface of Artin invariant one, without identifying the same arithmetic model or establishing this zeta expression. An isomorphism to a separately studied model could potentially furnish an equivalent computation and remains a historical-priority risk.

## Limitations
This is a mathematical proof for the displayed quartic and its minimal resolution, not for arbitrary members of Catanese–Schütt's 7-\(A_3\) family. The Hasse–Weil zeta function depends on the particular \(\mathbb F_2\)-descent, even when geometric K3 surfaces are isomorphic over an algebraic closure. The field models in the checker cover only six finite extensions; they are not evidence of universal correctness without the local and geometric proof. No claim is made about the Artin invariant, automorphism group, the full Néron–Severi lattice integrally, or a complete priority census. Independent mathematical validation has not been performed.

## References
1. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078, original submission 2021-10-06, especially §§3.2 and 3.5. https://arxiv.org/abs/2110.03078
2. F. Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988, original submission 2021-06-18. https://arxiv.org/abs/2106.09988
3. T. Katsura and S. Kondō, *A note on a supersingular K3 surface in characteristic 2*, arXiv:1010.5835, original submission 2010-10-28. https://arxiv.org/abs/1010.5835
