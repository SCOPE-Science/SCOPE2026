# The embedded conormal quadric in the characteristic-two binary-quadratic resultant

## Finding
Let \(k\) be an algebraically closed field of characteristic \(2\), and let \(S=k[a,b,c,d,e,f]\). The resultant of the two universal binary quadratic forms
\[
P=aX^2+bXY+cY^2,\qquad Q=dX^2+eXY+fY^2
\]
defines a quartic hypersurface \(X=V_+(R)\subset\mathbb P^5_k\). Put
\[
U=ae+bd,\quad V=af+cd,\quad W=bf+ce,\quad I=(U,V,W).
\]
Then the reduced singular support of \(X\) is the smooth Segre threefold \(Z=V_+(I)\simeq\mathbb P^1\times\mathbb P^2\), but the intrinsic Jacobian singular scheme \(Y\) is nonreduced. More precisely,
\[
R=V^2+UW,\qquad J_Y=I^2+(b,e)I=(b,e)I+(V^2),\qquad\sqrt{J_Y}=I.
\]
The nilpotent ideal of \(Z\) inside \(Y\) is supported on the smooth quadric \(T=V_+(b,e,V)\simeq\mathbb P^1\times\mathbb P^1\subset Z\). There is a natural exact sequence of sheaves on \(\mathbb P^5\)
\[
0\longrightarrow i_*\bigl(\mathcal O_T(-2,-2)\oplus\mathcal O_T(-2,-1)\bigr)
\longrightarrow \mathcal O_Y\longrightarrow \mathcal O_Z\longrightarrow 0.
\]
Here \(i:T\hookrightarrow\mathbb P^5\), and the two bidegrees refer first to the proportionality parameter of the two quadratics and second to the line of their square-term coefficients. The kernel is square-zero. The homogeneous coordinate ring of \(Y\) has Hilbert series
\[
H_{S/J_Y}(t)=\frac{1-6t^3+6t^4-t^6}{(1-t)^6}
=\frac{1+2t+3t^2-2t^3-t^4}{(1-t)^4},
\]
and its Hilbert polynomial is \(P_Y(n)=\frac12n^3+4n^2-\frac12n+2\).

## Assumptions and scope
All schemes, radicals and projective varieties are over an algebraically closed field of characteristic exactly \(2\). The Jacobian singular scheme is the homogeneous ideal of the quartic and all six first partial derivatives (not merely its reduced support). No claim is made about arbitrary degrees, other characteristics, the full non-saturated affine cone, or a characteristic-zero analogue. The twists \(\mathcal O_T(r,s)\) use the product polarization \(\mathcal O_T(1,1)\).

## Proof
**1. Resultant and first derivatives.** The Sylvester matrix is
\[
\begin{pmatrix}a&b&c&0\\0&a&b&c\\d&e&f&0\\0&d&e&f\end{pmatrix}.
\]
Expanding its determinant in characteristic two gives \(R=V^2+UW\). The ordered partial derivatives with respect to \(a,b,c,d,e,f\) are precisely \(eW,eV,eU,bW,bV,bU\). Consequently
\[
J_Y=(V^2,\,eU,eV,eW,\,bU,bV,bW).
\]
Since \(U\) and \(W\) lie in \((b,e)\), the ideal \(I^2\) lies in \(J_Y\), while \(J_Y\subset I^2+(b,e)I\); both inclusions yield the displayed equality \(J_Y=I^2+(b,e)I\).

**2. Support and embedded component.** The minors \(U,V,W\) are the \(2\times2\) minors of the matrix with rows \((a,b,c)\) and \((d,e,f)\), so \(I\) is the prime Segre ideal of \(Z\). Because \(I^2\subset J_Y\subset I\), the radical is exactly \(I\). The restriction of the coefficient hyperplanes \(b=e=0\) to \(Z\) is the Segre embedding of \(\mathbb P^1\times\mathbb P^1\): two proportional quadratics each have zero mixed coefficient. Its ideal in \(S\) is \((b,e,V)\), which is prime.

For the chart \(a=1\), introduce \(u=e+db\) and \(v=f+dc\). These form part of polynomial coordinates \((b,c,d,u,v)\); the resultant becomes \(R=v^2+buv+cu^2\). Direct differentiation gives
\[
J_Y=(u^2,uv,v^2,bu,bv)=(u,v)\cap(b,u,v)^2.
\]
Thus \(Y\) is reduced along \(Z\setminus T\), whereas near the generic point of \(T\) its intrinsic singular ideal has the additional embedded associated prime \((b,u,v)\). The symmetry interchanging the two quadratics and the two square coefficients covers all points of \(T\); alternatively the conormal calculation below is global.

**3. Conormal square-zero extension.** The ideal of \(Z\) inside \(Y\) is \(I/J_Y\). Since \(I^2\subset J_Y\), its product with itself is zero. The ideal equality induces
\[
I/J_Y\simeq (I/I^2)\otimes_{\mathcal O_Z}\mathcal O_T
\]
as coherent sheaves. The normal bundle of the Segre embedding \(Z=\mathbb P^1\times\mathbb P^2\subset\mathbb P^5\) is \(p_1^*T_{\mathbb P^1}\otimes p_2^*T_{\mathbb P^2}\) (a direct description by the quotient of the tensor product tangent space). On \(T\), the second factor is a line \(L\subset\mathbb P^2\), and \(T_{\mathbb P^2}|_L\simeq\mathcal O_L(2)\oplus\mathcal O_L(1)\). Hence \(N^*_{Z/\mathbb P^5}|_T\simeq\mathcal O_T(-2,-2)\oplus\mathcal O_T(-2,-1)\), proving the exact sequence.

**4. Hilbert series.** Exact polynomial division in characteristic two with graded reverse-lexicographic order \(a>b>c>d>e>f\) gives the following leading monomials of a Gröbner basis of \(J_Y\):
\[
c^2d^2,\quad b^2d,\quad bcd,\quad bce,\quad bde,\quad cde,\quad ce^2.
\]
They are obtained from the seven generators in step 1; all \(21\) Buchberger pair reductions vanish, as checked by the standalone script. Counting monomials not in this leading ideal (equivalently inclusion-exclusion over the seven monomial cones) gives numerator \(1-6t^3+6t^4-t^6\) over \((1-t)^6\). Combining this with the standard Segre ring series \(H_{S/I}=(1+2t)/(1-t)^4\) gives
\[
H_{I/J_Y}(t)=\frac{t^2(3+t)}{(1-t)^3}.
\]
The Hilbert polynomial of \(Z\) is \((n+1)\binom{n+2}{2}\), while that of \(I/J_Y\) is \((n-1)(2n-1)\); their sum is the asserted polynomial. This also checks the rank-two embedded excess against the conormal calculation.

## Verification
The included `verify.py` runs using the Python standard library; execute `python3 verify.py` after extracting the files. It confirms the characteristic-two Sylvester determinant, all six first derivatives, all pair reductions of the explicit Gröbner generators, the Hilbert numerator and the affine local normal form. These finite symbolic identities are exact, not sampling. Geometric statements about the Segre embedding and the conormal splitting are separately proved above; they are not implied by the script alone.

## Relationship to prior work
Classical resultant hypersurfaces and sparse-resultant formulas are established by Choudary (1990), Esterov (2011), and D'Andrea–Sombra (2013). The proposed new content is **not** the quartic resultant, its determinantal definition or its reduced rank-one support; it is the characteristic-two intrinsic scheme structure: the embedded conormal quadric, the square-zero bundle and the explicit Hilbert series. Kazarian–Kerner–Némethi (2013) study a different transversal discriminant in a characteristic-zero setting and explicitly distinguish that discriminant from a Jacobian singular scheme. Their statements do not imply the present characteristic-two formula. Literature equivalence remains subject to independent checking.

## Limitations
There is no independent audit. The literature search is not a mathematical proof of novelty; equivalent char-2 singular-scheme descriptions could exist in older resultant and modular invariant theory. The asserted exact sequence describes the intrinsic sheaf structure of the singular scheme but does not claim a canonical splitting of \(\mathcal O_Y\) as \(\mathcal O_Z\)-algebras. The Gröbner check is limited to the explicitly stated polynomial ideal.

## References
1. A. D. Raza Choudary, *On the resultant hypersurface*, Pacific Journal of Mathematics 142 (1990), 259–263. https://doi.org/10.2140/pjm.1990.142.259
2. A. Esterov, *Discriminant of system of equations*, arXiv:1110.4060, first submitted 2011-10-18. https://arxiv.org/abs/1110.4060
3. M. Kazarian, D. Kerner and A. Némethi, *Discriminant of ordinary transversal singularity type*, arXiv:1308.6045, first submitted 2013-08-28. https://arxiv.org/abs/1308.6045
4. C. D'Andrea and M. Sombra, *A Poisson formula for sparse resultants*, arXiv:1310.6617, first submitted 2013-10-24. https://arxiv.org/abs/1310.6617
