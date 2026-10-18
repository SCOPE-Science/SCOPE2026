# The embedded theta line in the Perazzo cubic's Jacobian scheme

## Finding
Let \(k\) be an algebraically closed field of characteristic different from \(2\). In \(S=k[x_0,x_1,x_2,u,v]\), with the standard grading, set
\[
 f=x_0u^2+2x_1uv+x_2v^2,
 \qquad X=V(f)\subset\mathbb P_k^4.
\]
Let \(J=(\partial f/\partial x_0,\partial f/\partial x_1,\partial f/\partial x_2,\partial f/\partial u,\partial f/\partial v)\) and let \(\Sigma=\operatorname{Proj}(S/J)\) be the *scheme-theoretic*, rather than just reduced, singular locus. Write \(\Pi=V(u,v)\cong\mathbb P^2\), \(\Delta=x_0x_2-x_1^2\), and \(C=V(u,v,\Delta)\subset\Pi\), a smooth conic.

**Theorem.** The homogeneous ideal \(J\) is saturated and has exactly the two associated primes \((u,v)\) and \((u,v,\Delta)\), with an exact primary decomposition
\[
 J=(u,v)\cap\bigl(J+(\Delta)\bigr).
\]
The reduced scheme of \(\Sigma\) is \(\Pi\), but its nilradical is a square-zero sheaf supported *exactly* on \(C\). Writing \(i:C\hookrightarrow\Pi\) for the inclusion and using \(C\cong\mathbb P^1\), the structure sheaf, as an \(\mathcal O_\Pi\)-algebra, is the split square-zero extension
\[
 \mathcal O_\Sigma\cong\mathcal O_\Pi\oplus i_*\mathcal O_{\mathbb P^1}(-1).
\]
The nilpotent line bundle is the unique theta characteristic of the conic: its square is \(\omega_C\). Moreover
\[
 \operatorname{Hilb}_{S/J}(t)=\frac{1+2t-2t^2}{(1-t)^3},
 \qquad \dim_k(S/J)_d=\binom{d+2}{2}+2d\quad(d\geq1),
\]
with degree-zero dimension one. The coordinate ring \(S/J\) has depth two and is not Cohen–Macaulay. Along \(C\), the hypersurface \(X\) has the exact local form of a Whitney umbrella times a smooth curve, whereas at geometric points of \(\Pi\setminus C\) its transverse local branches are normal crossings.

## Assumptions and scope
The theorem concerns the *Jacobian singular scheme* of the classical vanishing-Hessian Perazzo cubic threefold, not the apolar Artinian Gorenstein algebra associated to its defining form. The characteristic restriction is essential: in characteristic \(2\), the displayed integral polynomial and its gradient specialize differently. Statements about local splitting of branches are made after passing to algebraically closed geometric points or étale neighborhoods; the global equation and all module identities are algebraic over any field of characteristic different from \(2\). The source defining the named cubic was publicly available before the historical cutoff: Gondim–Russo, arXiv:1312.1618v1, 2013-12-05.

## Proof
Set \(A=k[x_0,x_1,x_2]\), \(I=(u,v)\) and \(L_1=x_0u+x_1v\), \(L_2=x_1u+x_2v\). Differentiation (with \(2\) invertible) gives exactly
\[
 J=(u^2,uv,v^2,L_1,L_2).
\]
Also \(f=uL_1+vL_2\), so the gradient equations already define the singular scheme of the projective hypersurface, not a larger extraneous scheme. The relation \(I^2\subset J\) gives a graded, multiplicatively split square-zero decomposition
\[
 S/J\cong A\oplus M,\qquad M=I/J,
\]
where
\[
 0\longrightarrow A(-2)^2
 \xrightarrow{\left(\begin{smallmatrix}x_0&x_1\\x_1&x_2\end{smallmatrix}\right)}
 A(-1)^2\longrightarrow M\longrightarrow0.
 \tag{1}
\]
The first arrow is injective because its determinant \(\Delta\) is a nonzero polynomial in the integral domain \(A\). Its adjugate shows \(\Delta M=0\). The conic \(C=V(\Delta)\) is smooth and geometrically integral, and the matrix in (1) has rank exactly one at every point of \(C\). Consequently \(\widetilde M\) is a line bundle on \(C\), extended by zero to \(\Pi\).

One can identify the line bundle *explicitly*, rather than only from a Hilbert polynomial. Put \(B=A/(\Delta)\) and map the classes of \(u,v\) to \(x_1,-x_0\) in the homogeneous ideal \((x_0,x_1)B\). Both relations map to zero. Conversely, if \(a x_1-b x_0\) is a multiple \(c\Delta\) in \(A\), then
\[
 (a+cx_1)x_1=(b+cx_2)x_0.
\]
Coprimality of \(x_0,x_1\) implies \((a,b)\) belongs to the span of \((x_0,x_1)\) and \((x_1,x_2)\), proving
\[
 M\cong(x_0,x_1)B
\]
as graded \(B\)-modules. On \(C\), \((x_0,x_1)\) cuts out the unique point \([0:0:1]\), so \(\widetilde M\cong\mathcal O_C(-p)\cong\mathcal O_{\mathbb P^1}(-1)\). By adjunction \(\omega_C\cong\mathcal O_C(-1)\cong\mathcal O_{\mathbb P^1}(-2)\), and hence \(\widetilde M^{\otimes2}\cong\omega_C\).

The presentation (1) also proves \(M\) is Cohen–Macaulay of \(A\)-dimension two by Auslander–Buchsbaum, while \(A\) has depth three. In particular \(A\oplus M\) has no irrelevant-ideal torsion, so \(J\) is saturated. Because \(M\) is an ideal in the domain \(B\), it is torsion-free over \(B\), with unique associated prime \((\Delta)\) over \(A\). The split filtration \(0\to M\to S/J\to A\to0\) therefore gives precisely the associated primes \(I\) and \((I,\Delta)\) over \(S\), the latter embedded.

For the primary decomposition, the explicit identities
\[
 \Delta u=x_2L_1-x_1L_2,\qquad
 \Delta v=x_0L_2-x_1L_1
\]
show \(\Delta I\subset J\). As \(\Delta\notin I\), the modular law gives \(I\cap(J+(\Delta))=J+\Delta I=J\). The quotient \(S/(J+(\Delta))\cong B\oplus M\) is a square-zero extension of the domain \(B\) by a torsion-free \(B\)-module, so its zero ideal is primary and its sole associated prime is the square-zero radical. This establishes the displayed primary decomposition.

Taking Hilbert series in (1) and adding the contribution of \(A\) gives
\[
 \operatorname{Hilb}_M(t)=\frac{2t-2t^2}{(1-t)^3}=\frac{2t}{(1-t)^2},\qquad
 \operatorname{Hilb}_{S/J}(t)=\frac{1}{(1-t)^3}+\frac{2t}{(1-t)^2}.
\]
Hence \(\dim M_d=2d\) for every \(d\ge1\), while \(M_0=0\), and the exact Hilbert function follows. From the direct sum as \(A\)-modules, \(\operatorname{depth}(S/J)=\min(3,2)=2\), strictly less than its Krull dimension three.

Finally, on the projective chart \(x_0\ne0\), put \(U=u+(x_1/x_0)v\) and \(T=x_2-x_1^2/x_0\). Then
\[
 f=x_0U^2+Tv^2.
\]
After dividing by the unit \(x_0\) and rescaling \(T\), this is exactly \(U^2+Tv^2=0\), with \(x_1/x_0\) as an additional smooth parameter. The locus \(T=0\) is \(C\), and the equation is the Whitney umbrella there. If \(T\) is nonzero, the transverse quadratic has distinct linear factors étale-locally. The chart \(x_2\ne0\) gives the same conclusion at the remaining point of \(C\).

## Verification
The standalone `verify.py` differentiates the defining cubic symbolically using integer-coefficient sparse polynomials, verifies the two determinant-annihilator identities, and computes the full quotient-space rank of homogeneous Jacobian multiples for degrees through seven modulo \(101\) and through five modulo \(3\) and \(5\). It reports `VERIFY_OK`. These finite checks corroborate the equations, but the all-degree Hilbert series and the scheme statements are proved algebraically above using the injective presentation and associated-prime argument; neither relies on extrapolating numerical data.

To reproduce: from the directory containing the files, run `python3 verify.py`. Only the Python standard library is needed.

## Relationship to prior work
Gondim–Russo (2013), Theorems 4.1–4.2, classify this cubic, establish that its *reduced* singular locus is a plane, and identify a distinguished conic in that plane. The present claim does not assert novelty for either the cubic, the reduced plane, or that conic. It identifies the unreported **embedded sheaf structure of the gradient base locus**, including its half-canonical line bundle and precise Hilbert series. Fiorindo–Mezzetti–Miró-Roig (2022) compute Hilbert functions of the *apolar Artinian Gorenstein algebra*, a different ring. Gharahi–Ottaviani (2025), Proposition 37, recover the conic as a distinguished orbit within the singular plane, without a determination of the Jacobian scheme's nilradical. These explicit stronger-context comparisons do not themselves supply the two associated primes, the square-zero extension, or the all-degree Jacobian quotient dimensions.

## Limitations
This is a scheme-theoretic result for a single natural cubic, not a classification of all Perazzo hypersurfaces or all characteristics. Characteristic \(2\) is excluded. The statement concerns the Jacobian scheme, not the conductor, normalization, or apolar algebra of the cubic. The originality search cannot rule out an unindexed classical computation of this exact gradient scheme or an equivalent matrix-factorization calculation. The explicit presentation makes the deduction short once the question is posed; its value lies in resolving the scheme structure left invisible by the classical reduced-orbit classification.

## References
1. R. Gondim and F. Russo, *On cubic hypersurfaces with vanishing hessian*, arXiv:1312.1618v1, first posted 2013-12-05, especially Theorems 4.1–4.2. https://arxiv.org/abs/1312.1618
2. L. Fiorindo, E. Mezzetti and R. M. Miró-Roig, *Perazzo 3-folds and the weak Lefschetz property*, arXiv:2206.02723v2, originally posted 2022-06-06, especially Sections 1 and 6. https://arxiv.org/abs/2206.02723
3. M. Gharahi and G. Ottaviani, *Symmetric Persistent Tensors and their Hessian*, arXiv:2510.07404v1, first posted 2025-10-08, especially Proposition 37. https://arxiv.org/abs/2510.07404
