# A finite flat length-seven square-contact scheme on characteristic-two Picard quartics

## Finding
Let \(k\) be algebraically closed of characteristic two. Consider the smooth Picard plane quartic
\[
C_{a,b,c,d}:\quad Y^3Z+X^4+aX^3Z+bX^2Z^2+cXZ^3+dZ^4=0,
\]
where \(c\ne0\) and \(f(x)=x^4+ax^3+bx^2+cx+d\) has no repeated root. Define the square-contact scheme \(B(C)\) on the dual projective plane: a line belongs to it scheme-theoretically exactly when the restriction of the quartic equation to the line is the square of a binary quadratic. Then
\[
\boxed{ B(C)\simeq\operatorname{Spec} k[v]/(v^7+(a/c^3)v). }
\]
The isomorphism is induced by the line \(Z=cv^3X+vY\). Over the smooth-coefficient base with \(c\) and \(\operatorname{Res}(f,f')\) inverted, these equations define a finite flat family of degree seven. When \(a\ne0\), its geometric support consists of one reduced point and three curvilinear double points. When \(a=0\), all seven units of length collide into a single curvilinear point of length seven, whose maximal-ideal Hilbert function is \((1,1,1,1,1,1,1)\).

## Assumptions and scope
The base ring is \(R=\mathbb F_2[a,b,c,d,c^{-1},\operatorname{Res}(f,f')^{-1}]\), with \(f\) as above. The family is smooth: its affine equation is \(y^3=f(x)\), and a simultaneous vanishing of both partial derivatives on this affine chart would give \(f(x)=f'(x)=0\); the unique point at infinity is smooth because the derivative with respect to \(Z\) there equals \(Y^3\). The scheme \(B(C)\) is the closed square-contact locus, **not** the theta-characteristic moduli scheme or a claim about its scheme structure. In characteristic two a binary quartic is a square precisely when its two odd mixed coefficients vanish; this condition is compatible with changes of basis of the binary linear space, so defines a scheme on the dual plane.

## Proof
A line is written \([U:V:W]\in(\mathbb P^2)^\vee\) as \(UX+VY+WZ=0\). First show that every square-contact line lies in the chart \(W\ne0\), scheme-theoretically. On \(W=0,V\ne0\), substitute \(Y=\lambda X\); the odd mixed coefficient of \(XZ^3\) in the restricted quartic is \(c\), a unit. On \(W=V=0\), the line is \(X=0\), where the odd mixed coefficient of \(Y^3Z\) is \(1\). The square-contact locus misses \(W=0\) entirely.

Normalize \(W=1\), and write \(Z=uX+vY\) (the signs agree in characteristic two). Direct binomial expansion yields the two odd mixed coefficients
\[
[X^3Y]\big(F(X,Y,uX+vY)\big)=v(a+cu^2),
\quad
[XY^3]\big(F(X,Y,uX+vY)\big)=u+cv^3.
\]
Thus the ideal of \(B(C)\) in this affine dual chart is \((v(a+cu^2),u+cv^3)\). Eliminate \(u\) by its second generator, obtaining \((av+c^3v^7)\). Since \(c\) is invertible, this is \((v^7+(a/c^3)v)\). This proves the asserted complete, not merely set-theoretic, scheme identity. The monic degree-seven polynomial gives a free \(R\)-basis \(1,v,\ldots,v^6\), proving finite flatness.

For \(a\ne0\), choose \(s\ne0\) with \(s^2=a/c^3\). In characteristic two the equation factors as \(v(v^3+s)^2\). The cubic \(v^3+s\) is separable because its derivative is \(v^2\), nonzero at every root. Hence the disjoint local Artinian factors have lengths \(1,2,2,2\). For \(a=0\), the equation is \(v^7\), so the unique factor has length seven and associated graded basis \(1,v,\ldots,v^6\). The reduced point \(v=0\) represents the hyperflex line \(Z=0\) in every fibre, since its intersection divisor is the fourth power of the point at infinity.

## Verification
Run the included self-contained symbolic program \(\texttt{VERIFY\_picard2\_bitangent.py}\) with Python 3 and SymPy. It checks the two odd coefficients, the complementary dual charts, elimination of \(u\), and the polynomial degrees; it prints \(\texttt{VERIFY\_OK}\). The complete flatness and geometric local-length argument follow from the monic quotient and factorization given above; finitely many sample calculations are not invoked as proof of the family-wide statement.

## Relationship to prior work
Nart and Ritzenthaler classify genus-three non-hyperelliptic curves in characteristic two and their geometric bitangent support counts, including the cases of four distinct and one distinct bitangent. This result is an exact calculation of a different and more refined invariant: the square-contact **scheme** and its flat degree-seven collision along a natural Picard-quartic subfamily. Its support counts agree with the established classification, which by itself does not specify these local scheme lengths. Wall's historical treatment of quartics in characteristic two is a significant potential source of equivalent descriptions, but its full text was not available for a decisive comparison.

## Limitations
This calculation concerns this explicit Picard coefficient family on the locus \(c\ne0\) and smooth \(f\); it does not classify arbitrary plane quartics in characteristic two, nor the moduli scheme of theta characteristics. The characteristic-two square-contact functor may differ from flat limits of bitangent schemes in mixed characteristic. Full-text access to all relevant historical literature was incomplete, so priority is not independently established. No independent scientific audit has been performed.

## References
1. E. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, preprint publicly posted 2003-12-18, arXiv:math/0312366, especially Proposition 2.1 and the bitangent normal forms.
2. C. T. C. Wall, *Quartic curves in characteristic 2*, Mathematical Proceedings of the Cambridge Philosophical Society **117** (1995), 393–414, DOI: 10.1017/S0305004100073254 (full-text comparison outstanding).
