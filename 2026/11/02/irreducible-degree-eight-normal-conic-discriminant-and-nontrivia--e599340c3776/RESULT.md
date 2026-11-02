# Irreducible degree-eight normal-conic discriminant of a quartic strength degeneration

## Finding
For every integer \(m\ge3\), consider the quartic hypersurface \(X_m\subset\mathbb P^{4m+2}_{\mathbb C}\) obtained by substituting four disjoint sums of squares into the Baily–Danelon quartic. Its distinguished singular component \(S_m\) carries an irreducible, reduced, degree-eight divisor \(\Delta_m\) where the transverse normal conic degenerates. At the generic point of this divisor, the conic is a pair of conjugate lines; the two lines are exchanged by a **nontrivial connected quadratic cover**. This is a global property of the normal-cone geometry, not a statement about the strength of every finite truncation.

More precisely, on a dense open subset of \(S_m\), the normal quadratic form has rank three outside \(\Delta_m\) and rank two along \(\Delta_m\). On a dense smooth open subset of \(\Delta_m\), the cover selecting one of the two lines is finite étale of degree two, with quadratic function-field extension given in the proof below.

## Assumptions and scope
Work over \(\mathbb C\). Fix an integer \(m\ge3\) and homogeneous coordinates
\[
 x,y,w,\quad P_1,\ldots,P_m,\quad Q_1,\ldots,Q_m,\quad U_1,\ldots,U_m,\quad V_1,\ldots,V_m
\]
on \(\mathbb P^{4m+2}\). Define
\[
 p=\sum_{i=1}^{m}P_i^2,\quad q=\sum_{i=1}^{m}Q_i^2,\quad u=\sum_{i=1}^{m}U_i^2,\quad v=\sum_{i=1}^{m}V_i^2,
\]
\[
 H=x^2u+xyv+y^2q+p(p-yw),\qquad X_m=V(H),\qquad S_m=V(x,y,p).
\]
Here \(S_m\) is a subvariety of \(X_m\), and the normal quadratic form means the degree-two initial form of \(H\) with respect to the ideal \((x,y,p)\) at a point where \(p\) is an ambient local coordinate. The theorem makes no assertion that \(S_m\) is the whole singular locus. The assertion about the cover is made on a dense smooth open subset of the discriminant.

## Proof
**1. Distinguished singular component.** Every first derivative of \(H\) vanishes when \(x=y=p=0\), so \(S_m\subseteq\operatorname{Sing}(X_m)\). The polynomial \(p\) has rank \(m\ge3\), hence is irreducible, so \(S_m\) is irreducible of dimension \(4m-1\). The locus where \((P_1,\ldots,P_m)\ne0\) is dense in \(S_m\); there, \(dp\ne0\) and \(x,y,p\) are three independent ambient local coordinates normal to \(S_m\).

The full equation, not merely its initial form, is quadratic in these normal coordinates:
\[
 Q_{\mathrm{nor}}(x,y,p)=u x^2+vxy+qy^2-wyp+p^2.
\]
Its symmetric matrix is
\[
 M=\begin{pmatrix}u&v/2&0\\v/2&q&-w/2\\0&-w/2&1\end{pmatrix},
 \qquad 4\det M=D:=4uq-uw^2-v^2.
\]
At the generic point of \(S_m\) this determinant is nonzero. The Jacobian ideal is therefore precisely the ideal of \(S_m\) in a formal neighborhood of that generic point, proving that \(S_m\) is an irreducible component of the singular locus. The generic transverse hypersurface singularity is an ordinary quadratic double point (transverse \(A_1\)).

**2. Irreducibility and degree of the discriminant.** Set \(\Delta_m=V(x,y,p,D)\). To prove \(D\) irreducible, regard it as a polynomial in the \(Q_i\) over the UFD \(B=\mathbb C[w,U_i,V_i]\). Its coefficient content is one: \(u\) and \(u w^2+v^2\) are coprime because \(u\) is irreducible for \(m\ge3\) and the variables in \(v\) are disjoint from those in \(u\). Over the fraction field of \(B\), the polynomial \(D/(4u)\) is \(\sum Q_i^2-c\) for nonzero \(c\). Its homogenization is a quadratic form of rank \(m+1\ge4\), hence irreducible. Gauss's lemma gives irreducibility of \(D\) in the polynomial ring.

In the domain \(R=\mathbb C[w,Q_i,U_i,V_i]/(D)\), the polynomial \(p=\sum P_i^2\) remains irreducible over \(\operatorname{Frac}(R)\) because its quadratic rank is at least three. Since it is monic in \(P_1\), the quotient \(R[P_1,\ldots,P_m]/(p)\) injects into its domain localization over \(\operatorname{Frac}(R)\). Thus \((p,D)\) is prime. Consequently \(\Delta_m\) is irreducible, reduced, and a complete intersection of degrees \(2,4\) inside \(V(x,y)\cong\mathbb P^{4m}\), so
\[
 \deg\Delta_m=2\cdot4=8.
\]
At its generic point \(P\ne0\), \(u\ne0\), and some \(Q_i\ne0\); then \(S_m\) and \(\Delta_m\) are smooth because \(dp\ne0\) and \(\partial D/\partial Q_i=8uQ_i\ne0\). The matrix \(M\) has rank exactly two there, while it has rank three off \(\Delta_m\).

**3. Explicit local form and component cover.** On the open \(u\ne0\), the polynomial identity
\[
 4uH=(2ux+vy)^2+u(2p-wy)^2+Dy^2
\]
completes the square in the normal variables. Where \(S_m\) and \(\Delta_m\) are smooth and \(D\) is a local parameter, analytic square roots of units give the transverse family normal form
\[
 z_1^2+z_2^2+t z_3^2=0.
\]
Over the generic point of \(\Delta_m\), the conic is
\[
 \left(p-\frac{wy}{2}\right)^2+u\left(x+\frac{vy}{2u}\right)^2=0.
\]
Its two lines are individually defined after adjoining \(\sqrt{-u}\). To express this intrinsically on projective space, use the dense chart \(w\ne0\), so the quadratic extension is \(\mathbb C(\Delta_m)(\sqrt{-u/w^2})\).

It remains essential to show that this extension is nontrivial. Work on \(w=1\). In the rational function field \(F=\mathbb C(U_1,\ldots,U_m,Q_1,\ldots,Q_m)\), the polynomials \(u=\sum U_i^2\) and \(r=4\sum Q_i^2-1\) are distinct irreducibles, so their square classes are independent. The relation \(D=0\) is \(v^2=ur\). Write \(P_+=P_1+iP_2\) and \(V_+=V_1+iV_2\). On the dense open where these are nonzero, \(p=0\) eliminates \(P_1-iP_2\), and \(\sum V_i^2=v\) eliminates \(V_1-iV_2\). Hence \(\mathbb C(\Delta_m)\) is a purely transcendental extension of \(F(v)\), where \(v^2=ur\). Since neither \(u\) nor \(r\) is a square in \(F\), \(u\) remains nonsquare in the quadratic extension \(F(\sqrt{ur})\): otherwise writing a square root as \(a+b\sqrt{ur}\) would force either \(u\) or \(r\) to be a square in \(F\). It stays nonsquare after a purely transcendental extension. Therefore the two lines are not separately defined over \(\mathbb C(\Delta_m)\).

Over the smooth open of \(\Delta_m\) on which \(w\ne0\), \(u\ne0\), and the normal matrix has rank two, the line-component selector is a finite étale double cover. Its function field is a quadratic field, not a product, so the cover is connected and the two lines have nontrivial monodromy.

## Verification
The standalone script `verify_normal_conic.py` uses only the Python standard library and exact rational polynomial arithmetic. It checks the completion-of-squares identity, the symmetric-matrix determinant, and weighted homogeneity of the defining quartic and discriminant. Running `python3 verify_normal_conic.py` prints `VERIFY_OK`. Irreducibility, dimension, smoothness and nonsquareness are established by the field-theoretic arguments above, not by finite sampling.

## Relationship to prior work
Baily and Danelon [1, §3, Theorem 3.2] introduced the displayed quartic as a degeneration witnessing nonclosedness of the strength-at-most-two locus for sufficiently many variables. They prove the strength assertion but do not describe the normal-conic discriminant or its line-component cover. Ballico, Bik, Oneto and Ventura [2, Theorem 1.3] treated a different quartic witnessing failure of closedness at strength three. Standard conic-bundle theory relates corank-one degenerations to component double covers; the particular irreducible degree-eight divisor and the nontrivial generic cover for this quartic are calculations made here. These comparisons do not establish an exhaustive publication-priority claim.

## Limitations
The classification is for the specified disjoint-squares realization with \(m\ge3\), over \(\mathbb C\). It does not determine the entire singular locus of \(X_m\), the scheme structure of other singular components, all higher-corank strata, or a finite threshold at which the quartic has strength three. The singularity normal form and étale cover are asserted on dense smooth opens only. The algebraic irreducibility proof requires the specified disjoint variable blocks. Independent mathematical validation has not been performed.

## References
[1] B. Baily and A. Danelon, *Closedness of bounded strength and partition rank loci*, arXiv:2610.28792v1 (first submitted 20 October 2026), especially §3. https://arxiv.org/html/2610.28792v1

[2] E. Ballico, A. Bik, A. Oneto and E. Ventura, *The set of forms with bounded strength is not closed*, arXiv:2012.01237v2; *Comptes Rendus Mathématique* 360 (2022), 371–380. https://arxiv.org/abs/2012.01237
