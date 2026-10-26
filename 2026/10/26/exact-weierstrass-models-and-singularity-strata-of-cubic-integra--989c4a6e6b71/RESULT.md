# Exact Weierstrass models and singularity strata of cubic integration-root loci

## Finding

Let \(P(x)=a_0+a_1x+a_2x^2+a_3x^3\) be a complex cubic with \(a_0a_3\ne0\). Its reduced zero equation under repeated or Riemann–Liouville integration of order \(\alpha\), after removal of the forced factor at the origin and multiplication by a nonzero coefficient factor, has the algebraic continuation
\[
G(\alpha,x)=6a_3x^3+2a_2(\alpha+3)x^2+a_1(\alpha+2)(\alpha+3)x+a_0(\alpha+1)(\alpha+2)(\alpha+3)=0.
\]
Write \(\mathcal C_P\) for the projective closure of this affine locus. For its shifted projective coordinates \([T:X:W]=[\alpha+3:x:1]\), define
\[
[U:V:Z]=[X:\,4a_0W-a_1X-3a_0T:\,T].
\]
This is a projective linear isomorphism carrying \(\mathcal C_P\) **exactly** onto
\[
V^2Z=A U^3+B U^2Z+C UZ^2+D Z^3,
\quad A=-48a_0a_3,\quad B=a_1^2-16a_0a_2,\quad C=-2a_0a_1,\quad D=a_0^2.
\]
In particular, put \(f(u)=Au^3+Bu^2+Cu+D\), \(\delta=\operatorname{disc}(f)\), and \(E=B^2-3AC\). Then
\[
\delta=-64a_0^3\bigl(972a_0^3a_3^2+432a_0^2a_1a_2a_3-256a_0^2a_2^3-3a_0a_1^3a_3+32a_0a_1^2a_2^2-a_1^4a_2\bigr).
\]
The curve is irreducible and has no singularity except possibly one finite singular point. Its precise classification is:

* \(\delta\ne0\): the curve is smooth of genus one, with the distinguished flex corresponding to \((\alpha,x)=(-3,0)\), and its \(j\)-invariant is
\[
 j(\mathcal C_P)=\frac{256(B^2-3AC)^3}{A^2\delta}.
\]
* \(\delta=0\) and \(E\ne0\): there is exactly one ordinary node; the normalization has genus zero.
* \(\delta=E=0\): there is exactly one ordinary cusp; the normalization has genus zero. Equivalently, the cusp locus is
\[
 a_2=-\frac{a_1^2}{48a_0},\qquad a_1^3=162a_0^2a_3.
\]

The geometry therefore has an explicit algebraic coefficient-space discriminant, rather than merely a generic genus bound. For example, \(P(x)=1+x^3\) gives a nonsingular curve with \(j=0\); \(P(x)=1+\frac{27}{4}x^2+9x^3\) gives a node; and \(P(x)=1+6x-\frac34x^2+\frac43x^3\) gives a cusp.

## Assumptions and scope

All coefficients and curves are over \(\mathbb C\), and \(a_0a_3\ne0\); \(a_1\) and \(a_2\) may vanish. Algebraic order \(\alpha\) is complex in the projective curve, while the original integration problem uses positive real (or positive integer) \(\alpha\). The polynomial \(G\) is the algebraic continuation of the reduced zero polynomial, not a statement that a branch of fractional integration is defined at every complex order. Genus means the geometric genus of the smooth projective normalization. A node and a cusp refer to ordinary complex-plane singularities of types \(A_1\) and \(A_2\), respectively.

## Proof

**1. Reduced equation and homogenization.** For any nonnegative integer \(k\), the \(k\)-fold integral of the monomial \(x^j\) from zero equals \(j!x^{j+k}/(j+k)!\). For positive real order \(\alpha\), the Riemann–Liouville integral has the coefficient \(\Gamma(j+1)/\Gamma(j+\alpha+1)\) after factoring \(x^\alpha\). Multiplying the reduced equation by \(\Gamma(\alpha+4)\), and continuing coefficients polynomially in \(\alpha\), yields the displayed \(G\). With \(T=\alpha+3\), the homogenized equation is
\[
F(T,X,W)=6a_3X^3+2a_2TX^2+a_1T(T-W)X+a_0T(T-W)(T-2W)=0.
\]

**2. Projective transformation.** Since \(a_0\ne0\), the change \(U=X\), \(Z=T\), \(V=4a_0W-a_1X-3a_0T\) has the inverse
\[
T=Z,\quad X=U,\quad W=\frac{V+a_1U+3a_0Z}{4a_0}.
\]
Substitution and expansion, with no division by a variable or loss of boundary points, yields the exact homogeneous identity
\[
8a_0F\left(Z,U,\frac{V+a_1U+3a_0Z}{4a_0}\right)
=V^2Z-(AU^3+BU^2Z+CUZ^2+DZ^3).
\]
Thus the transformation identifies the *complete projective curves*, not merely dense affine charts.

**3. Singular points, irreducibility, and genus.** Since \(A\ne0\), setting \(Z=0\) in the Weierstrass equation forces \(U=0\); the sole point at infinity is \([U:V:Z]=[0:1:0]\). The derivative of the defining homogeneous equation with respect to \(Z\) is \(V^2\ne0\) at that point, which is therefore smooth. In the affine chart \(Z=1\), the equation is \(v^2=f(u)\). A singular point must satisfy \(v=0\), \(f(u)=0\), and \(f'(u)=0\). The cubic \(f\) cannot be a square in \(\mathbb C(u)\), since its degree at infinity is odd; consequently \(v^2-f(u)\) is irreducible. The same holds for the projective curve. There is at most one multiple *distinct* root of a nonzero cubic, so at most one singular point. Three distinct roots yield a smooth plane cubic of genus one. A double root and a simple root give a transverse quadratic crossing (node), whereas a triple root gives \(v^2\sim (u-r)^3\) (ordinary cusp). Both singular cubics have rational normalization. The projective point \([0:1:0]\) is a flex: its tangent \(Z=0\) intersects the irreducible cubic there with intersection multiplicity exactly three. Under the inverse transformation this is the marked \((\alpha,x)=(-3,0)\).

**4. Explicit coefficient stratification.** For \(f(u)=Au^3+Bu^2+Cu+D\), the standard cubic discriminant identity is
\[
\delta=B^2C^2-4AC^3-4B^3D-27A^2D^2+18ABCD.
\]
Substituting the stated coefficients and collecting terms gives the factored coefficient formula above. A cubic has a triple root precisely when \(\delta=0\) and \(E=B^2-3AC=0\) (after translation this says that both its linear and constant depressed-cubic coefficients vanish). Since \(a_0a_3\ne0\), these two equations are equivalent to \(a_2=-a_1^2/(48a_0)\) and \(a_1^3=162a_0^2a_3\): for \(a_1=0\), \(E=0\) forces \(a_2=0\) and then \(\delta\ne0\); for \(a_1\ne0\), eliminate \(a_3\) using \(E=0\) and factor the residual equation, discarding the impossible factor \(B=0\). The remaining vanishing condition is \(48a_0a_2+a_1^2=0\), and substitution into \(E=0\) gives the asserted cubic relation.

**5. \(j\)-invariant and examples.** In affine form \(v^2=Au^3+Bu^2+Cu+D\), set \(x'=Au\), \(y'=Av\). The monic Weierstrass equation is
\[
y'^2=x'^3+Bx'^2+ACx'+A^2D.
\]
Its conventional invariant satisfies \(c_4=16(B^2-3AC)=16E\) and \(\Delta_{\mathrm{ell}}=16A^2\delta\), giving \(j=c_4^3/\Delta_{\mathrm{ell}}=256E^3/(A^2\delta)\) for \(\delta\ne0\). With \((a_0,a_1,a_2,a_3)=(1,0,0,1)\), \(E=0\) but \(\delta=-62208\ne0\), so \(j=0\). With \((1,0,27/4,9)\), \(f(u)=-(6u+1)^2(12u-1)\), a node. With \((1,6,-3/4,4/3)\), \(f(u)=-(4u-1)^3\), a cusp. These factorization identities verify that all three strata occur.

## Verification

The accompanying standalone Python/SymPy checker uses exact symbolic polynomial arithmetic to verify the projective identity, discriminant factorization, the singular-cusp parametrization, and the monic Weierstrass invariant; it also tests the displayed smooth, nodal, and cuspidal examples. The generic geometric classification, irreducibility, genus assertions, and claims at infinity are proved above rather than inferred from finitely many tests. Run \(\texttt{python verify.py}\); it prints \(\texttt{VERIFY_OK}\) when the exact checks pass.

## Relationship to prior work

P. Lawless, *Asymptotic Root Dynamics under Repeated and Fractional Integration* (arXiv:2610.12498, first submitted September 28, 2026), supplies the reduced algebraic equation in general degree, proves its irreducibility when the constant coefficient is nonzero, and identifies the root trajectories as a plane curve (Proposition 11.1). His Remark 11.3 gives a generic genus bound and explicitly leaves open the exact genus and identification of the elliptic curve for a given cubic in Section 14. Those already known claims are inputs, not new assertions. The result here is the invertible **projective** Weierstrass model and the complete singularity/genus locus with \(j\)-invariant. A. Galligo (2013) developed earlier order-parameter curves for fractional **derivatives**, and T. Caparatta, S. Pauli, and F. Saidak (2023/2025) studied related fractional-derivative roots; their different coefficient families must not be conflated with the precise integration formula. The longstanding classification of smooth, nodal, and cuspidal plane cubics is also standard background.

## Limitations

The theorem assumes a genuinely cubic starting polynomial with nonzero constant term. It classifies the algebraic closure over complex orders, **not** the real root trajectories at each positive order, the monodromy of the order projection, or analytic continuation across singular branches. The calculation settles the exact-genus and elliptic-identification question for degree three, not the analogous question for degree four or higher. Priority relative to earlier fractional-derivative stem constructions remains a historical-literature risk because one cited 2013 full text was inaccessible during comparison. No independent mathematical audit is claimed.

## References

1. P. Lawless, *Asymptotic Root Dynamics under Repeated and Fractional Integration*, arXiv:2610.12498, v1 September 28, 2026; available at https://arxiv.org/abs/2610.12498. Especially equations (3.2), (10.1), Proposition 11.1, Remark 11.3, and Section 14.
2. A. Galligo, *Deformation of roots of polynomials via fractional derivatives*, Journal of Symbolic Computation 52 (2013), 35–50, https://doi.org/10.1016/j.jsc.2012.05.011.
3. T. Caparatta, S. Pauli, F. Saidak, *Zeros of fractional derivatives of polynomials*, Experimental Mathematics 34 (2025), 541–554; original arXiv:2301.08149, https://arxiv.org/abs/2301.08149.
4. J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Graduate Texts in Mathematics 106, Springer (2009): standard discriminant and Weierstrass-invariant conventions.
