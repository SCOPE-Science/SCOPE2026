# Residue-three nodal transition on cyclic Frobenius-quadric sections

## Finding
For every prime \(p\geq5\), over \(k=\overline{\mathbb F}_p\) consider the projective complete-intersection curve \(X_p\subset\mathbb P^3_k\), with coordinates \([W:X:Y:Z]\), defined by
\[
Q=W^2+XY+YZ+ZX=0,\qquad
S_p=W^{p+1}+XY^p+YZ^p+ZX^p=0.
\]
The curve is reduced, has degree \(2(p+1)\) and arithmetic genus \(p^2\). Its complete geometric singularity classification is:

* If \(p\equiv2\pmod 3\), the curve is smooth (and consequently geometrically irreducible).
* If \(p\equiv1\pmod 3\), the curve has exactly \(4p\) distinct geometric singular points, all ordinary nodes; exactly four of those nodes are \(\mathbb F_p\)-rational.

The arithmetic point counts are
\[
\#X_p(\mathbb F_p)=(p+1)^2,\qquad
\#\widetilde X_p(\mathbb F_p)=
\begin{cases}
(p+1)^2,&p\equiv2\pmod3,\\
(p+1)^2+4,&p\equiv1\pmod3,
\end{cases}
\]
where \(\widetilde X_p\) is the normalization, taken componentwise if necessary. For \(p=5\), the smooth example has genus \(25\) and exactly \(36\) rational points.

## Assumptions and scope
The prime is any ordinary prime \(p\ge5\), not an arbitrary prime power. All geometric singularities are taken over the algebraic closure. The equations define the entire scheme-theoretic intersection of a smooth quadric and a smooth degree-\(p+1\) surface. The degree-six surface and quadric in Arakelian--Speziali, Example 3.10, are exactly the \(p=5\) specialization. Their paper studies Frobenius nonclassicality rather than this residue-class singularity classification.

## Proof
**1. Preliminary geometry.** The gradients in coordinate order \((W,X,Y,Z)\) are
\[
\nabla Q=(2W,Y+Z,X+Z,X+Y),\qquad
\nabla S_p=(W^p,Y^p,Z^p,X^p).
\]
Thus \(S_p=0\) is a smooth surface. The quadratic form \(Q\) is nonsingular in odd characteristic. It is split over \(\mathbb F_p\): the two distinct intersecting lines \(Y=-Z, W=Z\) and \(Y=-Z,W=-Z\) lie on it. Hence \(Q\simeq\mathbb P^1\times\mathbb P^1\) over \(\mathbb F_p\). Their intersection is a Cartier divisor of bidegree \((p+1,p+1)\). The calculations below show its singular set is finite, so its one-dimensional local complete-intersection ring is generically regular, hence reduced. Adjunction gives
\[
p_a(X_p)=1+\frac{2(p+1)((p+1)+2-4)}2=p^2.
\]

**2. Affine singularities.** Work where \(W=1\), and write \(x=X/W\), \(y=Y/W\), \(z=Z/W\), \(s=x+y+z\) and \(r=xy+yz+zx\). Since the \(W\)-partials are \(1\) and \(2\), the two gradients are proportional precisely when
\[
2x^p=x+y,\qquad2y^p=y+z,\qquad2z^p=z+x.
\tag{1}
\]
Euler's homogeneous identities give \( (p+1)S_p=\sum V_i\partial_{V_i}S_p\) and \(2Q=\sum V_i\partial_{V_i}Q\); therefore proportional gradients with \(W=1\) and \(Q=0\) automatically imply \(S_p=0\), so no extraneous critical candidates are counted. These equations imply \(s^p=s\), so \(s\in\mathbb F_p\), and the exact identity
\[
4r^p=(x+y)(y+z)+(y+z)(z+x)+(z+x)(x+y)=s^2+r.
\tag{2}
\]
On \(Q\), \(r=-1\). Equation (2) forces \(s^2=-3\). For \(p\equiv2\pmod3\), \(-3\) is a nonsquare in \(\mathbb F_p\), because it is the discriminant of \(T^2+T+1\), which has no root in \(\mathbb F_p\). There are no affine singular points.

For \(p\equiv1\pmod3\), choose a primitive cube root \(\omega\in\mathbb F_p\). With \(e_0=(1,1,1)\), \(e_1=(1,\omega,\omega^2)\), \(e_2=(1,\omega^2,\omega)\), write \((x,y,z)=ae_0+be_1+ce_2\). Equation (1) is equivalent to
\[
a^p=a,\quad b^p=\frac{1+\omega}{2}b,\quad c^p=\frac{1+\omega^2}{2}c.
\]
Also \(r=3a^2-3bc\). Since \(r=-1\), \(bc=a^2+1/3\in\mathbb F_p\), while taking the \(p\)-th power gives \((bc)^p=bc/4\). As \(p\ne3\), we obtain \(bc=0\) and \(a^2=-1/3\). There are exactly two values of \(a\); each of the two additive equations for \(b\) and \(c\) has exactly \(p\) distinct roots, and the union of their coordinate axes has \(2p-1\) points. Thus there are exactly \(2(2p-1)=4p-2\) affine singular points. Precisely the two with \(b=c=0\) are \(\mathbb F_p\)-rational: the nonzero solutions of either equation cannot lie in \(\mathbb F_p\), since neither eigenvalue equals \(1\).

**3. Singularities at infinity.** In the plane \(W=0\), the equation \(Q=0\) is a smooth conic with parametrization
\[
(X:Y:Z)=(u(u+v):v(u+v):-uv).
\]
For \(u\ne0\), let \(t=v/u\). Restricting \(S_p\) to this conic yields \(t(1+t)H_p(t)\), where
\[
H_p(t)=t^{p-1}(1+t)^p-t^p-(1+t)^{p-1}.
\]
The roots \(t=0\), \(t=-1\), and the omitted point \(u=0\) are simple (the binary form has degree \(2p+2\), while the displayed affine polynomial has degree \(2p+1\)). For \(t\ne0,-1\),
\[
H'_p(t)=(1+t)^{p-2}\bigl[1-t^{p-2}(1+t)^2\bigr].
\]
If \(H'_p(t)=0\), then \(t^p=t^2/(1+t)^2\); substitution into \(H_p\) gives \(H_p=-(t^2+t+1)^2/(1+t)^4\). Consequently a multiple root must be a primitive cube root and satisfy \(t^p=t\), which holds exactly when \(p\equiv1\pmod3\). Both roots are precisely double: differentiating the bracket in \(H'_p\) at such a root gives \(2t^{p-3}(1+t)\ne0\). Thus there are exactly two further singular points for \(p\equiv1\pmod3\) and none for \(p\equiv2\pmod3\). The two exceptional points are rational over \(\mathbb F_p\). No other infinity singularities occur because the \(W\)-derivatives of both defining forms vanish on \(W=0\), making the multiple roots of the conic restriction exactly the intersection singularities there.

**4. All singularities are nodes.** At any singular point the gradients satisfy \(dS_p=\lambda\,dQ\) for a nonzero scalar \(\lambda\). Every second ordinary partial derivative of \(S_p\) vanishes in characteristic \(p\). On the smooth quadric \(Q\), its local equation therefore has quadratic initial form \(-\lambda\) times the second fundamental form of \(Q\). A smooth quadric in \(\mathbb P^3\) has nondegenerate rank-two second fundamental form, yielding an ordinary node at every singular point. The finite singular locus also proves reducedness of the complete intersection as used above. The point counts and genus statements concern this reduced scheme.

**5. Rational points and normalization.** At each \(\mathbb F_p\)-point, \(S_p\) and \(Q\) have identical values because each coordinate satisfies \(a^p=a\). Hence \(X_p(\mathbb F_p)=Q(\mathbb F_p)\), which has \((p+1)^2\) points. If \(p\equiv1\pmod3\), the four rational nodes are split: the ordinary-node tangent cone is a nonzero scalar multiple of the split rank-two second fundamental form of the split quadric at an \(\mathbb F_p\)-point. Normalization replaces each such point with two rational points. The nonrational nodes introduce no additional rational normalization points. The formula follows. If \(p\equiv2\pmod3\), the curve is smooth; a smooth connected divisor of positive bidegree on \(\mathbb P^1\times\mathbb P^1\) is irreducible and equals its normalization.

## Verification
The accompanying self-contained `check_frobenius_quadric.py` performs exact integer finite-field tests for \(p=5,7,11,13,17,19\): all \(\mathbb F_p\)-points of the split quadric lie on the degree-\(p+1\) hypersurface; the rational singular-point counts are \(0\) or \(4\) in the prescribed residue classes; the conic-restriction polynomial has derivative gcd either \(1\) or \(t^2+t+1\); each rational node has precisely two isotropic tangent directions. The program is finite corroboration. Statements about geometric singularities for every prime follow from the symbolic equations (1)--(2), Fourier decomposition, and infinity-root computation; the finite tests alone do not establish those universal claims.

## Relationship to prior work
Arakelian and Speziali, *Curves on Frobenius nonclassical loci of hypersurfaces* (arXiv:2512.08874, Example 3.10), introduced the \(p=5\) degree-six surface and quadric and proved Frobenius nonclassicality of their curve model. They did not state a formula for a prime-variable family, its residue-three smoothness dichotomy, geometric node count, or rational point counts of the normalization. Berardini and Nardi, *Curves on Frobenius classical surfaces in \(\mathbb P^3\) over finite fields* (2022), establish upper bounds for rational points in a broader setting rather than an exact singularity calculation for these equations. The standard adjunction and nodal normalization facts are used as prior tools, not claimed as novel.

## Limitations
No geometrical irreducibility or genus-of-each-normalization-component claim is made in the nodal \(p\equiv1\pmod3\) case. The result does not address \(p=2,3\), prime powers as exponents, the zeta functions, or automorphism groups. Other equivalent formulations of these explicit cyclic Frobenius forms in older literature remain a residual bibliographic risk. Same source equations are previously known for \(p=5\); novelty concerns their uniform arithmetic-geometric extension and exact singularity/normalization behavior.

## References
1. N. Arakelian and P. Speziali, *Curves on Frobenius nonclassical loci of hypersurfaces*, arXiv:2512.08874v1 (first public 2025-12-09); *Mathematische Zeitschrift* 314 (2026), article 21, DOI:10.1007/s00209-026-04128-y, especially Example 3.10.
2. E. Berardini and J. Nardi, *Curves on Frobenius classical surfaces in \(\mathbb P^3\) over finite fields*, *Acta Arithmetica* 205 (2022), 323--340, arXiv:2111.09578, DOI:10.4064/aa211118-12-9.
3. Standard facts: complete-intersection adjunction, geometry of a smooth split quadric, and normalization of ordinary double points.
