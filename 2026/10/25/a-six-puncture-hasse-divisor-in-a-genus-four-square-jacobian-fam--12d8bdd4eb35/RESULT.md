# A six-puncture Hasse divisor in a genus-four square-Jacobian family

## Finding

Let \(k\) be algebraically closed of characteristic \(5\), and set
\[
Q_{u,v}(t)=v(t^4+1)+4(u+v)(t^3+t)+(8u+6v+16)t^2.
\]
Consider the smooth projective model of \(X_{u,v}:y^2=(x^2+1)Q_{u,v}(x^2)\). It is a smooth genus-four curve exactly on the parameter open set
\[
U=\{(u,v)\in\mathbb A^2_k:v(u^2+v)(1+u+v)\ne0\}.
\]
On this open set the Jacobian is nonordinary **if and only if**
\[
\Phi(u,v)=u^2(2u+1)-v(u^2+2u-2)=0.
\]
The nonordinary parameter curve \(N=U\cap V(\Phi)\) is geometrically smooth and isomorphic to
\[
\mathbb A^1_k\setminus\bigl(V(u(u-1)(u-2)(u-3))\cup V(u^2+2u-2)\bigr),
\]
under the projection to \(u\), with inverse \(v=u^2(2u+1)/(u^2+2u-2)\). The six omitted geometric points are distinct; four are defined over \(\mathbb F_5\), and two form one quadratic Frobenius orbit. For every \(m\ge1\), \(q=5^m\), the exact number of **smooth, ordered coordinate-marked** parameters with nonordinary Jacobian is
\[
\#N(\mathbb F_q)=q-4-2\mathbf1_{2\mid m}.
\]
The total smooth parameter count is \(q^2-3q+3\), so the ordinary count is \(q^2-4q+7+2\mathbf1_{2\mid m}\). In particular the only nonordinary member defined by parameters over \(\mathbb F_5\) is \((u,v)=(-1,2)\); its Jacobian is supersingular with \(5\)-rank \(0\) and \(a\)-number \(2\), but not superspecial.

## Assumptions and scope

All displayed equations and coefficients are reduced modulo \(5\). The parameters are ordered affine coordinates; the counts are **not** counts of isomorphism classes. Ordinarity is defined by maximal \(5\)-rank (equal to the Jacobian dimension). The result does not classify every nonordinary Newton polygon over \(\overline{\mathbb F}_5\); it classifies the *entire nonordinary divisor* and singles out one verified supersingular rational member.

## Proof

**Smoothness.** Since \(Q\) is reciprocal, put \(s=t+t^{-1}\). For \(t\ne0\),
\[
Q_{u,v}(t)=t^2\bigl(vs^2+4(u+v)s+8u+4v+16\bigr).
\]
The quadratic in \(s\) has discriminant \(16(u^2-4v)\), which modulo \(5\) vanishes exactly when \(u^2+v=0\). Furthermore \(Q(1)=16(1+u+v)\), \(Q(-1)=16=1\), and \(Q(0)=v\). Consequently \(Q\) is squarefree, has no zero root, and does not meet the factor \(x^2+1\) exactly when \(v(u^2+v)(1+u+v)\ne0\). In characteristic different from \(2\), each nonzero simple root of \(Q(t)\) gives two simple roots of \(Q(x^2)\), so the degree-ten hyperelliptic equation is smooth of genus four precisely on \(U\).

**A prime-to-five Jacobian-square isogeny.** The commuting involutions \(\alpha:(x,y)\mapsto(-x,y)\) and \(\beta:(x,y)\mapsto(-x,-y)\) have quotients
\[
D_{u,v}:Y^2=(t+1)Q_{u,v}(t),\qquad
E_{u,v}:W^2=t(t+1)Q_{u,v}(t).
\]
Both are smooth genus-two curves on \(U\). Because \(Q(t)=t^4Q(t^{-1})\), the substitution \(s=t^{-1},\ W=s^3Y\) defines an isomorphism \(D_{u,v}\simeq E_{u,v}\). The pullback maps give \(J(D)\times J(E)\to J(X)\). Their norm-map composite is multiplication by \(2\) on each factor with zero off-diagonal maps: the other quotient's pullback is anti-invariant under the first involution because their product is the hyperelliptic involution. Hence the pullback sum is an isogeny with kernel killed by \(2\). In characteristic \(5\), it identifies the \(5\)-divisible groups, proving
\[
J(X_{u,v})[5^\infty]\simeq J(D_{u,v})[5^\infty]^2.
\]
Thus \(J(X)\) is ordinary exactly when \(J(D)\) is ordinary.

**Hasse divisor.** Modulo \(5\), the quintic defining \(D\) is
\[
f(t)=v(t^5+1)-u(t^4+t)+(2u+1)(t^3+t^2).
\]
Writing \(f(t)^2=\sum_i c_i t^i\), the genus-two Hasse-Witt/Cartier matrix (up to the usual dual/transposition convention) is
\[
H=\begin{pmatrix}c_4&c_3\\c_9&c_8\end{pmatrix}
=\begin{pmatrix}
-2uv+2u+1&-2(u-v)(2u+1)\\
-2uv&u^2+4uv+2v
\end{pmatrix}.
\]
Direct multiplication in characteristic \(5\) gives
\[
\det H=u^2(2u+1)-v(u^2+2u-2)=\Phi(u,v).
\]
A genus-two Jacobian is ordinary if and only if its Hasse-Witt matrix is invertible; the same criterion holds for \(J(X)\) by the isogeny. This proves the exact nonordinary equation, not merely its containment.

**Geometry of the divisor.** Write \(d(u)=u^2+2u-2\), \(n(u)=u^2(2u+1)\). Over \(\mathbb F_5\), \(\gcd(d,n)=1\), so \(\Phi=0\) has no point over \(d=0\), and elsewhere \(v=n/d\). Substituting yields identities in \(\mathbb F_5[u,d^{-1}]\):
\[
 v=\frac{u^2(2u+1)}d,\qquad
u^2+v=\frac{u^2(u-3)^2}d,\qquad
1+u+v=\frac{3(u-1)(u-3)^2}d.
\]
Thus the smoothness conditions delete precisely \(u=0,1,2,3\) and the two roots of \(d\). The quadratic \(d\) has discriminant \(2\), a nonsquare in \(\mathbb F_5\), and does not vanish at \(0,1,2,3\). The projection is an isomorphism onto the indicated six-puncture affine line. Since \(\partial\Phi/\partial v=-d\) is nonzero on \(N\), the nonordinary divisor is reduced and smooth.

**Finite-field count.** Four removed parameters are rational over all \(\mathbb F_{5^m}\); the two roots of \(d\) become rational precisely when \(m\) is even, yielding the stated \(\#N\). For the full smooth open \(U\), the three forbidden values of \(v\) at each \(u\) are \(0,-u^2,-1-u\). Exactly \(u=0,-1,3\) cause collisions, and each then has two distinct forbidden values. Every other \(u\) has three; hence \(\#U(\mathbb F_q)=3(q-2)+(q-3)^2=q^2-3q+3\).

**The rational supersingular member.** For \(u=-1\), \(v=2\) the matrix is \(\left(\begin{smallmatrix}3&4\\4&2\end{smallmatrix}\right)\) over \(\mathbb F_5\), of rank one and square zero. Its genus-two quotient has \(5\)-rank zero and \(a\)-number one. Any genus-two abelian variety of \(p\)-rank zero has supersingular Newton polygon; the prime-to-five Jacobian-square isogeny gives \(J(X)\) slope \(1/2\) with multiplicity eight, \(5\)-rank zero and \(a\)-number two, so it is not superspecial.

## Verification

The standalone Python 3 program `verify.py` implements exact arithmetic in \(\mathbb F_5\), \(\mathbb F_{25}\), and \(\mathbb F_{125}\), checks the Hasse determinant against \(\Phi\) at every smooth parameter, and exhausts the nonordinary parameters. Results: respectively \(1\), \(19\), and \(121\) nonordinary parameter pairs, among \(13\), \(553\), and \(15253\) smooth pairs; all checks returned `VERIFY_OK`. The finite computations corroborate but do not replace the symbolic proof for arbitrary \(m\).

## Relationship to prior work

Bruin and Kulkarni (arXiv:2309.01959, first public 2023-09-05), Section 7.1 and Example 7.3, construct the two-parameter genus-four square-Jacobian model over characteristic different from two. Their geometric isogeny statement does not supply this characteristic-five Hasse divisor, its six-puncture structure, or finite-field parameter counts. Earlier characteristic-three arithmetic computations on an equivalent reciprocal genus-four model concern a different prime and do not imply the characteristic-five determinant or divisor geometry. General Cartier-Manin theory supplies the coefficient formula, not the present family-specific stratum. No claim of new isogeny construction or of a complete classification of nonordinary Newton polygons is made.

## Limitations

The classification is for the displayed coordinate-marked family, not its moduli quotient. The values of the \(5\)-rank on every geometric point of the nonordinary curve are not determined here; in particular, uniqueness of the exhibited supersingular \(\mathbb F_5\)-rational member is only within the rational parameter set, not a claim of geometric uniqueness. Potential unindexed calculations of this family remain a literature-overlap risk. No independent audit has been performed.

## References

1. N. Bruin and A. Kulkarni, *On (2,2)-decomposable genus 4 Jacobians*, arXiv:2309.01959, 2023, https://arxiv.org/html/2309.01959v1, Section 7.1 and Example 7.3.
2. E. W. Howe, *Supersingular genus-two curves over fields of characteristic three*, arXiv:math/0604413, 2006, https://arxiv.org/abs/math/0604413 (background only, different characteristic).
3. M. Kudo, S. Harashita and H. Senda, *The existence of supersingular curves of genus 4 in arbitrary characteristic*, Research in Number Theory 6 (2020), article 44, https://doi.org/10.1007/s40993-020-00217-x (general existence, not this divisor).
