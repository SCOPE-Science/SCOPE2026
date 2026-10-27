# Frobenius pinching of the naïve characteristic-three Schur quartic

## Finding

Let \(k\) be an algebraically closed field of characteristic \(3\). The *coefficientwise* reduction of Schur's integral quartic equation is
\[
X=V(x^4-xy^3-z^4+zw^3)\subset\mathbb P^3_k.
\]
With \(a=x-y\) and \(b=z-w\), its equation becomes \(xa^3-zb^3=0\). The following statements hold together.

1. \(X\) is geometrically integral, with scheme-theoretic Jacobian singular locus \(V(a^3,b^3)\subset\mathbb P^3_k\). Thus the reduced singular locus is the line \(L=V(a,b)\), and the Jacobian scheme is a complete intersection of two cubic hypersurfaces, of degree \(9\), with generic transverse length \(9\). In particular \(X\) is nonnormal.
2. The normalization is the Hirzebruch surface \(\mathbb F_2\cong\mathbb P_{\mathbb P^1}(\mathcal O(3)\oplus\mathcal O(1))\). The finite normalization map is a universal homeomorphism. It is an isomorphism away from \(L\); its inverse-image section over \(L\) maps by degree-three purely inseparable Frobenius.
3. Over \(\mathbb F_3\), for every integer \(r\ge1\),
\[
\#X(\mathbb F_{3^r})=(3^r+1)^2,
\qquad
Z(X/\mathbb F_3,T)=\frac{1}{(1-T)(1-3T)^2(1-9T)}.
\]

The specified coefficientwise model is essential: a *different* integral model of Schur's complex quartic has good characteristic-three reduction projectively equivalent, over an extension, to the smooth Fermat quartic. This theorem does not identify their special fibres.

## Assumptions and scope

All geometric assertions are over an algebraically closed field \(k\) of characteristic exactly \(3\). The arithmetic assertion concerns the explicitly displayed quartic over \(\mathbb F_3\) and all its finite extensions. Here \(\mathbb F_2\) denotes the *Hirzebruch ruled surface*, not the finite field. The scheme-theoretic singular locus is defined by the intrinsic projective hypersurface Jacobian ideal.

## Proof

**Equation and integral structure.** In characteristic \(3\), the identity \((x-y)^3=x^3-y^3\) gives
\[
x^4-xy^3-z^4+zw^3=x(x-y)^3-z(z-w)^3=xa^3-zb^3.
\]
The linear coordinate change from \((x,y,z,w)\) to \((x,z,a,b)\) is invertible. As a polynomial in \(x\) over \(k[z,a,b]\), \(xa^3-zb^3\) is primitive (since \(\gcd(a^3,zb^3)=1\)) and of degree one over the fraction field. Gauss's lemma proves absolute irreducibility. The four partial derivatives in \((x,z,a,b)\) are \(a^3,-b^3,0,0\). They cut out the complete intersection \((a^3,b^3)\), since the defining quartic lies in that ideal. Its reduced support is \(L=\{a=b=0\}\). At its generic point the regular parameters \(a,b\) give \(k(L)[a,b]/(a^3,b^3)\), of length \(9\). The projective complete intersection has degree \(3\cdot3=9\). As \(L\) has codimension one in the integral hypersurface \(X\), the hypersurface fails the normality condition \(R_1\).

**Normalization.** Let \(B=\mathbb P^1_k\) have homogeneous coordinates \([s:t]\), and put
\[
Y=\mathbb P_B\bigl(\mathcal O_B(3)\oplus\mathcal O_B(1)\bigr).
\]
The four relative-hyperplane sections \(t^3,s^3\) of \(\mathcal O(3)\), and \(s,t\) of \(\mathcal O(1)\), have no common zero. They define a morphism \(\nu:Y\to\mathbb P^3\) expressed in local fibre coordinates \([\lambda:\mu]\) as
\[
[x:z:a:b]=[\lambda t^3:\lambda s^3:\mu s:\mu t].
\]
The bundle transitions make this formula independent of local trivializations. It satisfies \(xa^3-zb^3=0\), so \(\nu(Y)\subset X\). Whenever \((a,b)\ne(0,0)\), the base parameter is \([s:t]=[a:b]\), and the relation \(xa^3=zb^3\) uniquely determines the fibre point. Thus \(\nu\) is an isomorphism over \(X\setminus L\), hence birational.

The inverse image of \(L\) is exactly the section \(E=\{\mu=0\}\cong\mathbb P^1\). Along \(E\), the map is
\[
[s:t]\longmapsto[x:z]=[t^3:s^3],
\]
the relative Frobenius (followed by coordinate exchange), finite purely inseparable of degree \(3\). Every geometric fibre of \(\nu\) has one point: off \(L\) this follows from the explicit inverse, and on \(L\) from injectivity of Frobenius on algebraically closed fields. Hence \(\nu\) is quasi-finite. It is projective, thus finite. The source is smooth and normal, so this finite birational morphism is the normalization. Its geometric-fibre uniqueness after arbitrary field extension makes it radicial; being finite and surjective, it is a universal homeomorphism. Finally, tensoring the displayed rank-two bundle by \(\mathcal O(-1)\) identifies \(Y\) with \(\mathbb P_B(\mathcal O(2)\oplus\mathcal O)=\mathbb F_2\).

**Arithmetic.** The construction and the finite universal homeomorphism are defined over \(\mathbb F_3\). Finite radicial maps induce bijections on rational points over each perfect finite extension field, because purely inseparable extensions of finite fields are trivial. Since \(Y\to\mathbb P^1\) is a \(\mathbb P^1\)-bundle, its point count over \(\mathbb F_q\), for \(q=3^r\), is \((q+1)^2\). The exponential definition of the zeta function then gives
\[
\exp\Bigl(\sum_{r\ge1}(3^{2r}+2\cdot3^r+1)T^r/r\Bigr)
=(1-9T)^{-1}(1-3T)^{-2}(1-T)^{-1}.
\]

## Verification

The attached standalone `check_schur3.py` checks the coordinate identity, all four Jacobian derivatives, and the parametrization identity modulo \(3\) by exact polynomial arithmetic. It also exhaustively checks \(X(\mathbb F_3)\) and \(X(\mathbb F_9)\) using a direct field model \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\), obtaining respectively \(16\) and \(100\) points and \(4\) and \(10\) rational points on the singular line. These finite enumerations corroborate, but do not prove, the all-extension-field point formula; the normalization proof supplies that implication. The finite morphism and universal-homeomorphism properties are proved above, not assumed from computational output.

## Relationship to prior work

Rams and Schütt (arXiv:1212.3511, introduction) write Schur's quartic in precisely this equation, establish its 64-line property away from characteristics \(2,3\), and explicitly distinguish a characteristic-three *good-reduction model* isomorphic to the Fermat quartic. Their characteristic-three study (arXiv:1409.7485, §4.3, Remark 4.4) concerns that smooth model, not the coefficientwise integral equation's singular scheme or normalization. Veniani's study of characteristic-three K3 quartics (doi:10.1007/s00229-021-01284-9) concerns normal quartics with rational double points and mentions the classical Schur equation; the present nonnormal model is outside that class. The precise Frobenius-normalization, length-nine Jacobian thickening, and zeta formula are the asserted additions. No uniqueness claim concerning the entire historical literature is made.

## Limitations

This is a theorem about the displayed naïve projective integral model. It does not describe good, stable, or semistable reduction of Schur's smooth quartic after changing its integral coordinates. The normalization is not a resolution of the entire arithmetic total space. Originality comparisons are limited to the inspected sources and record searches; an equivalent older monomial-surface calculation cannot be excluded. Independent mathematical validation has not been performed.

## References

1. S. Rams and M. Schütt, *64 lines on smooth quartic surfaces*, arXiv:1212.3511 (first posted 2012-12-14), introduction and §1.
2. S. Rams and M. Schütt, *112 lines on smooth quartic surfaces (characteristic 3)*, arXiv:1409.7485 (first posted 2014-09-26), §4.3 and Remark 4.4.
3. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, Manuscripta Math., doi:10.1007/s00229-021-01284-9, introduction and main results.
