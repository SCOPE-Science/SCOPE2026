# Universal torus saturation of rational Nevanlinna extremals

## Finding

Let \(\varphi\) be any nonconstant real rational Herglotz–Nevanlinna function on the upper half-plane, and let \(m\geq1\) be its degree as a rational map of the Riemann sphere. Consider the two-variable function
\[
 h(z,w)=-\frac{1}{\varphi(z)+w-1/w}.
\]
Normalize at \((i,i)\) by
\[
 c=\operatorname{Re}h(i,i),\qquad \eta=\operatorname{Im}h(i,i)>0,
 \qquad f(s,t)=-\frac{i}{\eta}\bigl(h(\gamma(s),\gamma(t))-c\bigr),
 \quad \gamma(\zeta)=i\frac{1+\zeta}{1-\zeta}.
\]
Then \(f\) is an extreme element of the normalized positive-real-part class on the bidisk, and its rational inner Cayley transform has the form
\[
 \frac{f-1}{f+1}=\frac{\widetilde r}{r}
\]
for a scattering-stable polynomial \(r\) of bidegree \((m,2)\). **Every such \(r\) is \(\mathbb T^2\)-saturated**: the polynomials \(r\) and \(\widetilde r\) have precisely \(2m\) distinct common points, all on \(\mathbb T^2\), each of local intersection multiplicity \(2\). Their total intersection number is the maximal \(4m=2(m)(2)\).

More precisely, let \(\tau_1,\ldots,\tau_m\) be the poles of \(\varphi\) on the real projective line, counting the pole at infinity when present. The full common-zero set is
\[
 \bigl\{\bigl(\gamma^{-1}(\tau_j),-1\bigr),
            \bigl(\gamma^{-1}(\tau_j),1\bigr):1\leq j\leq m\bigr\}.
\]
Equivalently, if \(\varphi=B/A\) is written in coprime real homogeneous forms of degree \(m\) on \(\mathbb P^1\), the binary resultant associated with the original two-variable numerator and denominator equals \(-A^4\) under the coefficient convention of the proof. In particular, the pole divisor alone determines the entire base-point intersection divisor; the residues and regular part of \(\varphi\) do not affect its multiplicities.

## Assumptions and scope

A one-variable Herglotz–Nevanlinna function is holomorphic on \(\mathbb H=\{\operatorname{Im}z>0\}\) with nonnegative imaginary part. Here \(\varphi\) is nonconstant and real rational, meaning its rational coefficients may be chosen real. Such a function has the classical partial-fraction representation
\[
 \varphi(z)=a+bz+\sum_{j=1}^{k}\frac{c_j}{\tau_j-z},
 \qquad a\in\mathbb R,\quad b\geq0,\quad c_j>0,
 \quad \tau_j\in\mathbb R\ \text{distinct}.
\]
The rational degree is \(m=k+\mathbf1_{\{b>0\}}\): there are exactly \(m\) distinct simple poles on \(\mathbb{RP}^1\), with \(\infty\) added when \(b>0\). The original family \(h\) and the extremality of its representing Nevanlinna measure are established by Fagrell and Luger (2026); their result is used as a premise, not reproved here.

For a polynomial \(r\) of bidegree \((m,2)\), \(\widetilde r(s,t)=s^m t^2\overline{r(1/\overline s,1/\overline t)}\). Scattering stability means \(r\) has no zero in \(\mathbb D^2\) and \(r,\widetilde r\) have no common polynomial factor. A polynomial is \(\mathbb T^2\)-saturated if its intersection number with its reflection on \(\mathbb T^2\), counted scheme-theoretically, equals \(2m\cdot2=4m\). The result is about this specific family; it does not assert the saturation implication for arbitrary rational extreme points.

## Proof

**1. Reduced projective numerator and denominator.** Write \(\varphi(z)=B(z)/A(z)\) in coprime real polynomials, and homogenize both to coprime binary forms \(A(Z),B(Z)\) of degree \(m\) in \(Z=(Z_0:Z_1)\), where the affine coordinate is \(z=Z_1/Z_0\). Then the rational function \(h\), on \(\mathbb P^1\times\mathbb P^1\), is given by two bihomogeneous forms of bidegree \((m,2)\):
\[
 P(Z,W)=-A(Z)W_0W_1,\qquad
 Q(Z,W)=A(Z)(W_1^2-W_0^2)+B(Z)W_0W_1,
 \quad W=(W_0:W_1).
\]
Indeed, on \(W_0\ne0\), \(w=W_1/W_0\) and \(P/Q=-A(z)w/[A(z)(w^2-1)+B(z)w]\). The pair \((P,Q)\) is coprime: a common curve would lie in \(P=0\), hence in \(A(Z)=0\), \(W_0=0\), or \(W_1=0\). Along \(W_0=0\) or \(W_1=0\), \(Q\) is \(A(Z)W_1^2\) or \(-A(Z)W_0^2\), respectively; along \(A(Z)=0\), \(Q=B(Z)W_0W_1\), nonzero generically because \(A,B\) are coprime. Thus there is no common component.

**2. Exhaustive location of base points.** If \(P=Q=0\) and \(A(Z)\ne0\), then \(P=0\) forces \(W_0W_1=0\), where the displayed expression for \(Q\) is nonzero. Therefore \(A(Z)=0\). At each such \(Z\), the coprimality of \(A,B\) implies \(B(Z)\ne0\), and \(Q=B(Z)W_0W_1\). Hence the base points are exactly the pairs \((Z,[1:0])\) and \((Z,[0:1])\) for zeros \(Z\) of \(A\). Every zero of \(A\) is a distinct real projective pole of \(\varphi\); thus all \(2m\) points lie on \(\mathbb{RP}^1\times\mathbb{RP}^1\).

**3. Each local intersection has multiplicity two.** Fix a simple zero \(Z_*\) of \(A\). Take \(x=A(Z)\) as local coordinate near \(Z_*\); this is valid because the pole is simple. Write \(B(Z)=b(x)\), with \(b(0)\ne0\). Near \(W=[1:0]\), put \(w=W_1/W_0\). The equation \(Q=0\) reads
\[
 x(w^2-1)+b(x)w=0.
\]
Because its \(w\)-derivative at \((x,w)=(0,0)\) equals \(b(0)\ne0\), the implicit-function theorem gives \(w(x)=x/b(0)+O(x^2)\). Thus the restriction \(P|_{Q=0}=-xw(x)=-x^2/b(0)+O(x^3)\) vanishes to order exactly two. Hence the local intersection multiplicity is two.

Near \(W=[0:1]\), put \(u=W_0/W_1\). The equation \(Q=0\) is \(x(1-u^2)+b(x)u=0\), so \(u(x)=-x/b(0)+O(x^2)\). As \(P=-xu\) in this chart, it again has a zero of exact order two on \(Q=0\).

**4. A universal resultant certificate.** Set \(A=A(Z)\), \(B=B(Z)\), and regard the two forms as quadratics in the homogeneous \(W\)-coordinates. For the affine degree-two perturbation \(P_\varepsilon(w)=\varepsilon w^2-Aw\) and \(Q(w)=Aw^2+Bw-A\), the Sylvester determinant is
\[
 \operatorname{Res}_{w}(P_\varepsilon,Q)
 =A^2(\varepsilon^2-B\varepsilon-A^2).
\]
Setting \(\varepsilon=0\) gives the binary-form resultant, retaining the projective root at \(w=\infty\):
\[
 \boxed{\operatorname{Res}_{W}(P,Q)=-A(Z)^4.}
\]
The zero divisor of this resultant is exactly four times the pole divisor of \(\varphi\), in agreement with the two separate multiplicity-two intersections over each pole. Since the pair has bidegree \((m,2)\), the total projective intersection number is \(2m\cdot2=4m\); every intersection has been accounted for.

**5. Passage to the scattering-stable polynomial.** The coordinatewise Cayley map is an automorphism of the projective line, carrying \(\mathbb{RP}^1\) onto \(\mathbb T\). The normalized function \(f\) is obtained from \(P/Q\) by a real translation and nonzero complex scaling in the range, followed by coordinatewise Cayley transformations in the domain. In projective homogeneous coordinates these operations replace \((P,Q)\) by an invertible constant linear combination of \((P,Q)\), after invertible linear substitutions of both domain coordinates. They therefore preserve the full base-point scheme and each local intersection multiplicity.

Moreover, \(f(0,0)=1\), \(\operatorname{Re}f>0\) in \(\mathbb D^2\), and \(f\) has imaginary boundary values almost everywhere on \(\mathbb T^2\). Consequently \(F=(f-1)/(f+1)\) is rational inner and \(F(0,0)=0\). The rational-inner representation yields \(F=\widetilde r/r\) with \(r\) scattering stable. No extra coordinate monomial is present: \(F(0,t)\) and \(F(s,0)\) are not identically zero, because the original \(h\) is nonconstant in each variable. Since numerator and denominator of \(F\) are obtained from the coprime bihomogeneous pair \((P,Q)\) by invertible operations, their genuine bidegree is \((m,2)\), so this is also the bidegree of \(r\). Finally, \((r,\widetilde r)\) and \((P,Q)\) define isomorphic base-point schemes, establishing precisely the torus intersections claimed.

For completeness, extremality of \(f\) follows from the cited extremality of the measure representing \(h-c\). If \(f=(f_1+f_2)/2\) for normalized positive-real functions, transform back to Herglotz–Nevanlinna functions \(h_j\). The extremal-measure decomposition forces \(h_j=a_j+d_j(h-c)\) with real \(a_j\) and nonnegative \(d_j\); evaluation at \((i,i)\), where \(h_j(i,i)=i\eta\) and \((h-c)(i,i)=i\eta\), forces \(a_j=0\) and \(d_j=1\). Thus \(f_1=f_2=f\).

## Verification

The bundled `check.py` constructs the Sylvester determinant symbolically with independent formal variables \(A,B,\varepsilon\), verifies the exact identity \(A^2(\varepsilon^2-B\varepsilon-A^2)\), and checks the specialization \(-A^4\). It additionally evaluates representative affine numerator-denominator pairs, including the degree-two involution example and a degree-four composition. Execution with SymPy produced `CHECK_OK`. The script checks the polynomial identity; pole simplicity, global base-point enumeration, projective invariance, and extremality are established by the analytic argument above.

As a consistency check, \(\varphi(z)=z-1/z\) has the two projective poles \(0,\infty\). Under inverse Cayley these give the four points \((\pm1,\pm1)\), each with intersection multiplicity two. This agrees with the explicit polynomial \(2-s^2-t^2\) in the motivating paper, but the present theorem applies to arbitrary degree and all admissible rational \(\varphi\), including those with nonreducible denominators.

## Relationship to prior work

Fagrell and Luger (2026), Theorem 3.1, establish extremality of the representing Nevanlinna measure of \(h\) for every nonconstant rational Herglotz–Nevanlinna input; their Section 4 constructs the corresponding rational-inner bidisk functions and analyzes reducibility. Their Section 4.1 establishes torus saturation for the single example \(\varphi(z)=z-1/z\), invoking a substitution argument. The new assertion here is the universal degree-\((m,2)\) saturation theorem, with exact base-point scheme and degree-independent resultant for every rational input. This is not a claim of novelty for the originating extreme-point family itself.

Knese (2017 preprint; 2019 publication), Definition 1.4 and Conjecture 1.7, introduces saturation via the full \(2mn\) projective intersection count and conjectures its necessity for rational extreme points. Theorem 1.5 there gives a sufficient extremality criterion when saturation and an irreducibility hypothesis both hold; it does not imply saturation for the full Fagrell–Luger family. The latter family includes reducible cases which disprove the irreducibility component. Our theorem confirms the **saturation component within that full family** and does not claim a proof of Knese's global conjecture.

## Limitations

The result is restricted to nonconstant *real rational* one-variable Herglotz–Nevanlinna inputs and the associated two-variable extreme-point family. It does not classify all rational extreme points, does not imply a general saturation criterion for unrelated inner functions, and does not determine the singularity scheme of arbitrary scattering-stable polynomials. The conclusion uses the primary literature's extremality theorem as an external premise. Unindexed work on stable-polynomial projective base loci could contain an equivalent observation; independent priority assessment has not been performed.

## References

1. Ludvig Fagrell and Annemarie Luger, *Real rational Herglotz-Nevanlinna functions in two variables and a class of extremals*, arXiv:2610.02476v1, first posted 2026-10-01. Theorem 3.1 and Sections 4.1–4.2. https://arxiv.org/html/2610.02476v1
2. Greg Knese, *Extreme points and saturated polynomials*, arXiv:1703.00094v1 (2017), subsequently Illinois Journal of Mathematics 63 (2019), 47–74. Definition 1.4, Theorem 1.5, Conjecture 1.7. https://arxiv.org/abs/1703.00094
