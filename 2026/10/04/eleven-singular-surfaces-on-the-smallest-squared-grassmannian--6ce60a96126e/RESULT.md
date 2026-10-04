# Eleven singular surfaces on the smallest squared Grassmannian
## Finding
Let \(k\) be an algebraically closed field with \(\operatorname{char}(k)\neq 2\), and write
\[
a=q_{12},\quad b=q_{13},\quad c=q_{14},\quad d=q_{23},\quad e=q_{24},\quad f=q_{34}.
\]
The squared Grassmannian \(X=\operatorname{sGr}(2,4)\subset\mathbb P^5_k\) is the quartic hypersurface
\[
F=a^2f^2+b^2e^2+c^2d^2-2abef-2acdf-2bcde=0.
\]
Its reduced singular locus has exactly eleven irreducible components: eight coordinate planes and three smooth quadric surfaces. The planes are
\[
P_{\epsilon_1\epsilon_2\epsilon_3}=V(\bar\epsilon_1,\bar\epsilon_2,\bar\epsilon_3),
\]
where, independently, \(\epsilon_1\in\{a,f\}\), \(\epsilon_2\in\{b,e\}\), \(\epsilon_3\in\{c,d\}\), and \(\bar\epsilon_i\) denotes the other member of the same pair. Equivalently, one keeps exactly one coordinate from each of \(\{a,f\},\{b,e\},\{c,d\}\). The three quadrics are
\[
Q_A=V(a,f,be-cd),\qquad Q_B=V(b,e,af-cd),\qquad Q_C=V(c,d,af-be).
\]
At a general point of every one of these eleven surfaces, the completed local ring is
\[
\widehat{\mathcal O}_{X,p}\simeq k[[t_1,t_2,x,y,z]]/(x^2+yz).
\]
Thus the generic transverse singularity is an \(A_1\) surface singularity. In particular \(\operatorname{Sing}(X)\) has codimension two in the fourfold \(X\), and \(X\) is normal.

Moreover, after normality is known, the coordinatewise squaring morphism identifies \(X\) with the finite quotient \(\operatorname{Gr}(2,4)/(\mathbb Z/2)^3\). The eleven singular surfaces are precisely the images of the positive-dimensional fixed loci of the seven nontrivial sign involutions: eight \(\mathbb P^2\)'s from the four \(1|3\) splittings of the coordinates and three \(\mathbb P^1\times\mathbb P^1\)'s from the three \(2|2\) splittings.

## Assumptions and scope
The field is algebraically closed and has characteristic different from \(2\). The statement classifies the **reduced** singular locus and the generic completed local type along each irreducible component. It does not claim a primary decomposition of the Jacobian scheme, nor does it classify the more degenerate local types at intersections of the eleven surfaces.

The equation for \(X\) is the one obtained by squaring Plücker coordinates. Al Ahmadieh--Vinzant identify this quartic with the slice \(a_{\emptyset}=a_{123}=0\) of Cayley's \(2\times2\times2\) hyperdeterminant. Devriendt--Friedman--Reinke--Sturmfels identify the same quartic as the determinant of the zero-diagonal symmetric \(4\times4\) matrix and prove the general determinantal description of \(\operatorname{sGr}(2,n)\).

## Proof
Put
\[
L_1=af-be-cd,\qquad L_2=af-be+cd,\qquad L_3=af+be-cd.
\]
Direct differentiation gives the factorization
\[
\begin{aligned}
\tfrac12F_a&=fL_1,&\tfrac12F_f&=aL_1,\\
\tfrac12F_b&=-eL_2,&\tfrac12F_e&=-bL_2,\\
\tfrac12F_c&=-dL_3,&\tfrac12F_d&=-cL_3.
\end{aligned}
\]
Group the coordinates into the three opposite pairs \(A=(a,f)\), \(B=(b,e)\), and \(C=(c,d)\). If all three pair-vectors are nonzero at a singular point, then \(L_1=L_2=L_3=0\). Since the characteristic is not \(2\), subtraction gives \(cd=be=0\), and then \(af=0\). Each pair-vector is nonzero while its product is zero, so exactly one coordinate in each pair is nonzero. The point therefore lies on one of the eight planes \(P_{\epsilon_1\epsilon_2\epsilon_3}\).

If exactly two pair-vectors are nonzero, say \(A\) and \(B\), then \(C=0\) and the gradient equations reduce to \(af-be=0\), which is \(Q_C\). The other two cases give \(Q_A\) and \(Q_B\). If only one pair-vector is nonzero, its product must vanish and the point lies in the closure of two of these quadric cases. Hence no further projective singular points occur. Each listed plane and each listed quadric is directly contained in the Jacobian zero set; the quadrics are smooth because, for example, the gradient of \(af-be\) in \((a,b,e,f)\) is \((f,-e,-b,a)\). Generic support patterns show that no listed surface is contained in another. Thus the reduced singular locus has exactly the stated eleven irreducible components.

For the generic local type, take first the plane \(V(f,e,d)\) at a point with \(abc\neq0\). As a quadratic form in the three normal variables \((f,e,d)\), the Hessian determinant of \(F\) equals
\[
-32a^2b^2c^2,
\]
which is a unit there. The formal Morse lemma therefore gives a nondegenerate ternary quadratic transverse equation, hence the completed local form \(x^2+yz=0\).

For the generic point of \(Q_C\), where \(c=d=0\), \(af=be\), and \(abef\neq0\), the exact identity
\[
F=(af-be-cd)^2-4be\,cd
\]
shows the same result. Indeed \(u=af-be\) is a regular transverse parameter; after replacing \(u\) by \(u-cd\) and rescaling one of \(c,d\) by the unit \(4be\), the transverse equation is \(x^2+yz=0\). Symmetry handles the other ten components.

The defining ideal of \(X\) is prime, so \(X\) is an irreducible hypersurface and therefore Cohen--Macaulay, hence satisfies Serre's condition \(S_2\). Its singular locus has dimension two while \(\dim X=4\), so \(X\) is regular in codimension one. Serre's criterion gives normality.

Finally, column sign changes on \(\operatorname{Gr}(2,4)\) modulo the global sign form \((\mathbb Z/2)^3\), and the squaring map has generic degree \(8\). It therefore factors through a finite birational map \(\operatorname{Gr}(2,4)/(\mathbb Z/2)^3\to X\); both sides are normal, so this map is an isomorphism. A nontrivial sign involution comes from a coordinate splitting. A \(1|3\) splitting has two positive-dimensional fixed components, both \(\mathbb P^2\), while a \(2|2\) splitting has one positive-dimensional fixed component \(\mathbb P^1\times\mathbb P^1\). Their squared Plücker images are exactly the eight planes and three quadrics above.

## Verification
The accompanying `verify.py` reconstructs the determinant of the zero-diagonal symmetric matrix, checks every factored partial derivative, verifies all eight coordinate planes and all three quadrics lie in the Jacobian zero set, verifies the nonzero normal Hessian determinant on a representative plane, and checks the exact local rewrite along a representative quadric. It terminates with `VERIFY_OK` using exact symbolic arithmetic.

The component exhaustion in the proof is symbolic rather than numerical: every singular point is split according to which of the three opposite coordinate pairs vanish, and each case is solved by the factored gradient equations. No finite sampling is used to infer the global classification.

## Relationship to prior work
Al Ahmadieh and Vinzant, Example 6.5 of arXiv:2105.13444, give this quartic and identify it with the linear slice \(a_{\emptyset}=a_{123}=0\) of Cayley's hyperdeterminant. Devriendt, Friedman, Reinke and Sturmfels, Theorem 3.5 and Example 3.6 of arXiv:2401.03684, prove the zero-diagonal symmetric determinantal description and record that the squaring map has degree \(2^{n-1}\). Neither inspected source states the eleven-component singular-locus decomposition or the generic transverse \(A_1\) type.

Weyman and Zelevinsky classify irreducible components of the singular locus of the **ambient** hyperdeterminant hypersurface. That result does not by itself classify singularities of the codimension-two linear slice used here: a linear section may acquire singularities at points where the ambient hypersurface is smooth but tangent to the section. The present argument works directly on the sliced quartic and exhausts its Jacobian locus.

Targeted searches for the equation together with “singular locus”, “eight planes”, “three quadrics”, quotient sign flips, and ordinary-double-point terminology did not locate a published statement equivalent to the claim. This is evidence of non-coverage, not a proof of absolute novelty.

## Limitations
The local normal form is asserted only at a general point of each component; intersection strata can have more complicated singularities. The result is not stated in characteristic \(2\), where the derivative factorization loses the divisions and sign-quotient geometry changes. The Jacobian **scheme** may carry additional nonreduced structure at component intersections; only its reduction is classified here.

A residual literature risk remains that the same quartic slice has been analyzed under hyperdeterminant, three-qubit, or finite-quotient terminology not returned by the searches performed. The full ambient hyperdeterminant singularity literature was compared, but no claim of exhaustive bibliographic uniqueness is made.

## References
1. A. Al Ahmadieh and C. Vinzant, *Characterizing principal minors of symmetric matrices via determinantal multiaffine polynomials*, arXiv:2105.13444v1 (2021), later J. Algebra 638 (2024), 255--278. Example 6.5.
2. K. Devriendt, H. Friedman, B. Reinke and B. Sturmfels, *The Two Lives of the Grassmannian*, arXiv:2401.03684v1 (2024). Theorem 3.5, Example 3.6, Remark 4.4.
3. J. Weyman and A. Zelevinsky, *Singularities of hyperdeterminants*, Ann. Inst. Fourier 46 (1996), 591--644, DOI:10.5802/aif.1526.
