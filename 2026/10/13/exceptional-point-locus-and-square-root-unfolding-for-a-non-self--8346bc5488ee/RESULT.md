# Exceptional-point locus and square-root unfolding for a non-self-adjoint relativistic point interaction
## Finding
Consider the massive one-dimensional relativistic point interaction introduced by Heriban and Tušek. Let
\[
A=\begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}\in\mathbb C^{2\times2},\qquad m\ne0,
\]
and let \(D_A\) be the closed Dirac operator defined by their transmission condition. Exclude the source's flooding case \(\alpha=\delta=0\) and \(\det A=4\), for which every point off the essential spectral rays is an eigenvalue and isolated-eigenvalue multiplicity is not the relevant notion.

For \(\alpha\ne0\), define
\[
\Delta_A=(\det A-4)^2+16\alpha\delta,
\qquad
\eta_*=-\frac{i(\det A-4)}{4\alpha}.
\]
Then an algebraically double isolated eigenvalue exists if and only if
\[
\Delta_A=0,
\qquad
\eta_*\notin\mathbb R,
\qquad
\operatorname{sgn}m=
\operatorname{sgn}\operatorname{Im}\!\left(\frac{\eta_*}{\eta_*^2-1}\right).
\]
Its energy is
\[
z_*=m\frac{\eta_*^2+1}{\eta_*^2-1}.
\]
Every isolated eigenvalue outside this locus is algebraically simple. In particular, the case \(\alpha=0\) has no isolated algebraically multiple eigenvalue.

There are two distinct kinds of double point on the locus. The double eigenvalue is semisimple exactly for
\[
A=\begin{pmatrix}\alpha&0\\0&-4/\alpha\end{pmatrix},\qquad \alpha\ne0,
\]
provided its repeated root satisfies the displayed admissibility condition. For every other admissible matrix with \(\Delta_A=0\), the eigenvalue has algebraic multiplicity two and geometric multiplicity one. Thus the non-decoupled part of the locus is an order-two exceptional-point locus, whereas the decoupled part is a diabolic, semisimple double point.

The coalescence has the expected square-root unfolding, now with an explicit coefficient for this operator. If \(A(s)\) is analytic, \(A(0)=A_*\), \(\alpha_*\ne0\), the repeated root at \(s=0\) is admissible, and
\[
\Delta_{A(0)}=0,
\qquad
\left.\frac{d}{ds}\Delta_{A(s)}\right|_{s=0}\ne0,
\]
then the two nearby isolated eigenvalues satisfy
\[
z_\pm(s)=z_*\mp
\frac{m\eta_*}{\alpha_*(\eta_*^2-1)^2}
\sqrt{-\Delta_{A(s)}}+O(s).
\]
The choice of square-root branch only exchanges the labels \(+\) and \(-\).

## Assumptions and scope
The statement uses exactly the coupling normalization, branch convention and transmission-condition model of arXiv:2205.05005. The spectral parameter lies in
\[
\mathbb C\setminus\bigl(( -\infty,-|m|]\cup[|m|,\infty)\bigr),
\]
where the source's function
\[
\zeta(z)=\frac{z+m}{\sqrt{z^2-m^2}}
\]
is analytic with its specified square-root branch. The theorem concerns isolated eigenvalues only. It does not assign an exceptional-point multiplicity to the source's spectral-flooding case, and it makes no claim at the threshold points \(z=\pm |m|\), which are not eigenvalues in this model.

## Proof
The source proves that off the essential rays the eigenvalue condition is
\[
F_A(z):=\det\!\left(I+\frac{i}{2}A Z(z)\right)=0,
\qquad
Z(z)=\operatorname{diag}(\zeta(z),\zeta(z)^{-1}),
\]
and, when \(\alpha\ne0\), rewrites it as the quadratic equation
\[
P_A(\eta):=
\alpha\eta^2+\frac{i(\det A-4)}2\eta+\delta=0,
\qquad \eta=\zeta(z).
\]
A direct determinant expansion gives the exact factorization
\[
F_A(z)=\frac{i}{2\zeta(z)}P_A(\zeta(z)).
\]
The quadratic discriminant is
\[
\operatorname{disc}P_A=-\frac14\bigl((\det A-4)^2+16\alpha\delta\bigr)
=-\frac14\Delta_A.
\]
Hence a repeated root occurs exactly when \(\Delta_A=0\), and then it is \(\eta_*=-i(\det A-4)/(4\alpha)\).

Heriban--Tušek's inversion lemma states that \(\zeta(z)=\eta\) has an off-ray solution exactly when
\[
\eta\notin\mathbb R,
\qquad
\operatorname{sgn}m=
\operatorname{sgn}\operatorname{Im}\!\left(\frac{\eta}{\eta^2-1}\right),
\]
and that the solution is uniquely
\[
z(\eta)=m\frac{\eta^2+1}{\eta^2-1}.
\]
For every admissible \(\eta\),
\[
\frac{dz}{d\eta}=-\frac{4m\eta}{(\eta^2-1)^2}\ne0,
\]
so \(\zeta\) is locally conformal at every isolated eigenvalue. Therefore the order of a zero of \(F_A\) equals the multiplicity of the corresponding root of \(P_A\).

For completeness, the passage from characteristic-zero order to algebraic eigenvalue multiplicity can be checked directly from the source's finite-dimensional Krein resolvent formula. With \(M_A(z)=I+iA Z(z)/2\), the ordinary boundary-triple Weyl identity gives the finite-rank trace relation
\[
\operatorname{Tr}\bigl((D_A-z)^{-1}-(D_0-z)^{-1}\bigr)
=-\frac{d}{dz}\log\det M_A(z).
\]
Integrating around a sufficiently small positively oriented contour enclosing one isolated eigenvalue and using the Riesz-projection formula shows that its algebraic multiplicity is the zero order of \(F_A=\det M_A\). Thus a simple root of \(P_A\) gives algebraic multiplicity one and a repeated root gives algebraic multiplicity two. When \(\alpha=0\), the source equation is linear in \(\zeta\) unless it is the excluded flooding case, so no isolated algebraically multiple eigenvalue is possible.

The source further proves that for \(m\ne0\) an eigenvalue has geometric multiplicity two exactly for
\[
A=\operatorname{diag}(\alpha,-4/\alpha).
\]
Consequently, an admissible double root is semisimple precisely in that decoupled family; every other admissible double root has algebraic multiplicity two but geometric multiplicity one, hence one Jordan chain of length two.

Finally, the two exact quadratic roots are
\[
\eta_\pm(s)=
\frac{-i(\det A(s)-4)\pm\sqrt{-\Delta_{A(s)}}}{4\alpha(s)}.
\]
For a transverse path this yields
\[
\eta_\pm(s)=\eta_*\pm\frac{\sqrt{-\Delta_{A(s)}}}{4\alpha_*}+O(s).
\]
Composing with \(z(\eta)\) and using the derivative above gives the stated Puiseux law.

## Verification
The algebraic factorization, discriminant, repeated-root formula, two representative matrix ranks and a transverse square-root splitting were independently replayed by the accompanying script. One defective example is
\[
m=1,
\qquad
A=\begin{pmatrix}1&3\\-3&-1\end{pmatrix},
\]
for which \(\det A=8\), \(\Delta_A=0\), \(\eta_*=-i\), \(z_*=0\), and \(I+iAZ(0)/2\) has rank one. A semisimple example at the same energy is
\[
m=1,
\qquad
A=\operatorname{diag}(-2,2),
\]
for which the same matrix vanishes identically at \(z=0\), giving geometric multiplicity two. These examples are checks of the symbolic proof, not substitutes for it.

## Relationship to prior work
Heriban and Tušek derive the exact characteristic equation, prove that at most two isolated eigenvalues occur in the massive non-flooding regime, and classify geometric multiplicity two by the decoupled family. They state only that algebraic multiplicity of an isolated eigenvalue is finite; the paper does not classify algebraic multiplicity, Jordan defect, exceptional points, or the square-root coalescence coefficient.

Cuenin and Siegl study weakly coupled eigenvalues and eigenvalue bounds for one-dimensional non-self-adjoint Dirac operators with regular complex matrix potentials. Their setting and conclusions do not classify the singular point-interaction coalescence above. Holzmann, Růžek and Tušek later develop a boundary-triple theory for non-self-adjoint Dirac operators on finite metric graphs and a Birman--Schwinger principle, but the inspected paper contains no exceptional-point, Jordan, or algebraic-multiplicity classification that specializes to the present formula.

## Limitations
The result is restricted to \(m\ne0\) and to isolated off-threshold eigenvalues of the exact one-point interaction. The spectral-flooding matrices are excluded because their point spectrum is non-discrete. The theorem does not address pseudospectral growth, dynamical encircling, regularized finite-width potentials, or stability of the exceptional-point locus under changes of the interaction model. The Puiseux expansion is local in parameter space.

## References
1. L. Heriban and M. Tušek, *Non-self-adjoint relativistic point interaction in one dimension*, arXiv:2205.05005v1; J. Math. Anal. Appl. 516 (2022), 126536, DOI 10.1016/j.jmaa.2022.126536.
2. J.-C. Cuenin and P. Siegl, *Eigenvalues of one-dimensional non-self-adjoint Dirac operators and applications*, arXiv:1705.04833v1; Lett. Math. Phys. 108 (2018), 1757--1778.
3. M. Holzmann, V. Růžek and M. Tušek, *Non-self-adjoint Dirac operators on graphs*, arXiv:2502.00480v2; J. Phys. A 58 (2025), 165205.
