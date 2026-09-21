# Finite ray fibers remove the injectivity hypothesis in algebraic complex-moment extensions

## Statement

Let
\[
\mathfrak N_+=\{(m,n)\in\mathbb Z^2:m+n\ge 0\},
\qquad
\psi(z)=\frac{z}{\bar z}\quad (z\in\mathbb C^*).
\]

The 2019 paper of Cichoń, Stochel and Szafraniec studies positive-definite
extensions of complex moment sequences from \(\mathbb N_0^2\) to
\(\mathfrak N_+\). Their Theorem 22 obtains strong determinacy conclusions
for measures supported on an algebraic zero set \(\mathcal Z_p\), but the
final injectivity step assumes that \(\psi|_{\mathcal Z_p}\) is injective,
equivalently that every line through the origin meets \(\mathcal Z_p\) in at
most one point.

The one-point condition can be replaced by finite fibers.

**Theorem 1 (finite-ray separation).**  
Let \(Z\subset\mathbb C^*\) be Borel and suppose every line through the origin
meets \(Z\) in finitely many points. Let \(\mu_1,\mu_2\) be finite positive
Borel measures carried by \(Z\), and suppose every monomial
\(z^m\bar z^n\), \((m,n)\in\mathfrak N_+\), is absolutely integrable for both
measures. If
\[
\int z^m\bar z^n\,d\mu_1
=
\int z^m\bar z^n\,d\mu_2
\qquad ((m,n)\in\mathfrak N_+),
\]
then \(\mu_1=\mu_2\).

This gives the following strengthening of Theorem 22(v) and Corollary 23 of
Cichoń--Stochel--Szafraniec.

**Corollary 2 (arbitrary algebraic support away from the origin).**  
Let \(p\in\mathbb C[z,\bar z]\) satisfy
\[
\mathcal Z_p\ne\varnothing,\qquad 0\notin\mathcal Z_p,
\]
and let \(\gamma\) be a complex moment sequence having a representing measure
supported in \(\mathcal Z_p\). Then the map
\[
\mathcal M(\gamma)\longrightarrow \mathsf{PDE}(\gamma),
\qquad
\mu\longmapsto \Gamma(\mu),
\]
where
\[
\Gamma_{m,n}(\mu)=\int_{\mathbb C^*}z^m\bar z^n\,d\mu(z),
\qquad (m,n)\in\mathfrak N_+,
\]
is bijective. Consequently:

1. every \(\Gamma\in\mathsf{PDE}(\gamma)\) is determinate;
2. if \(\gamma\) is indeterminate, then
   \(|\mathsf{PDE}(\gamma)|=\mathfrak c\);
3. if \(\mathsf{PDE}(\gamma)\) is a singleton, then \(\gamma\) is
   determinate.

Thus, within the algebraic-support class \(0\notin\mathcal Z_p\), the
injectivity hypothesis on \(\psi_p\) is unnecessary.

## Proof of Theorem 1

Write
\[
s(z)=|z|^2,\qquad u=\psi(z)\in\mathbb T.
\]

For \(q\ge0\), define finite positive measures on \(\mathbb T\) by
\[
\alpha_{i,q}(B)
=
\int_{\psi^{-1}(B)}s(z)^q\,d\mu_i(z),
\qquad i=1,2.
\]
For every \(k\in\mathbb Z\),
\[
\int_{\mathbb T}u^k\,d\alpha_{i,q}(u)
=
\int_{\mathbb C^*}
(z\bar z)^q\left(\frac z{\bar z}\right)^k d\mu_i(z)
=
\int_{\mathbb C^*}z^{q+k}\bar z^{q-k}\,d\mu_i(z).
\]
The index pair \((q+k,q-k)\) belongs to \(\mathfrak N_+\), because its sum is
\(2q\). Hence the two measures \(\alpha_{1,q}\) and \(\alpha_{2,q}\) have the
same Fourier coefficients. Uniqueness of finite measures on the circle from
their Fourier coefficients gives
\[
\alpha_{1,q}=\alpha_{2,q}\qquad(q\ge0).
\tag{1}
\]

We also retain the odd-total-degree information. Define finite complex
measures
\[
\beta_{i,q}(B)
=
\int_{\psi^{-1}(B)}z\,s(z)^q\,d\mu_i(z).
\]
Their total variations are finite because
\(\int |z|^{2q+1}\,d\mu_i<\infty\), which follows from Cauchy--Schwarz and
the even radial moments. For every \(k\in\mathbb Z\),
\[
\int_{\mathbb T}u^k\,d\beta_{i,q}(u)
=
\int z^{q+k+1}\bar z^{q-k}\,d\mu_i(z).
\]
Now the index sum is \(2q+1\), so the hypothesis again applies. Fourier
uniqueness for finite complex measures yields
\[
\beta_{1,q}=\beta_{2,q}\qquad(q\ge0).
\tag{2}
\]

Put
\[
\lambda=\alpha_{1,0}=\alpha_{2,0}
=\psi_*\mu_1=\psi_*\mu_2.
\]
Because \(\mathbb C^*\) and \(\mathbb T\) are standard Borel spaces,
disintegrate
\[
\mu_i=\int_{\mathbb T}\kappa_i(u,\cdot)\,d\lambda(u),
\]
where, for \(\lambda\)-almost every \(u\), \(\kappa_i(u,\cdot)\) is a
probability measure concentrated on
\[
F_u=Z\cap\psi^{-1}(\{u\}).
\]
The fiber \(F_u\) is finite by hypothesis.

Taking Radon--Nikodym derivatives in (1) and (2), and intersecting the
resulting countably many full-measure sets, gives for almost every \(u\) and
every \(q\ge0\)
\[
\int_{F_u}s^q\,d\kappa_1(u)
=
\int_{F_u}s^q\,d\kappa_2(u),
\tag{3}
\]
and
\[
\int_{F_u}z\,s^q\,d\kappa_1(u)
=
\int_{F_u}z\,s^q\,d\kappa_2(u).
\tag{4}
\]

Fix such a \(u\). Let
\[
a_1,\ldots,a_L
\]
be the distinct values of \(s=|z|^2\) on \(F_u\). Define
\[
A_{i,\ell}
=
\kappa_i\bigl(\{z\in F_u:s(z)=a_\ell\}\bigr),
\qquad
B_{i,\ell}
=
\int_{\{s=a_\ell\}}z\,d\kappa_i .
\]
Equations (3) for \(q=0,\ldots,L-1\) give
\[
\sum_{\ell=1}^L a_\ell^q A_{1,\ell}
=
\sum_{\ell=1}^L a_\ell^q A_{2,\ell}.
\]
The Vandermonde matrix on the distinct \(a_\ell\)'s is invertible, hence
\[
A_{1,\ell}=A_{2,\ell}\quad(\ell=1,\ldots,L).
\tag{5}
\]
Applying the same Vandermonde argument to (4) gives
\[
B_{1,\ell}=B_{2,\ell}\quad(\ell=1,\ldots,L).
\tag{6}
\]

For fixed \(u\) and \(a_\ell\), there are at most two points of \(\mathbb C^*\)
with \(\psi(z)=u\) and \(|z|^2=a_\ell\); if there are two, they are antipodal,
say \(\zeta\) and \(-\zeta\). In that case (5) gives the sum of their two
weights and (6) gives
\[
\zeta(w_+-w_-),
\]
so the two individual weights are determined. If only one point occurs,
(5) already determines its weight. Therefore
\[
\kappa_1(u,\cdot)=\kappa_2(u,\cdot)
\]
for \(\lambda\)-almost every \(u\). Integrating the conditional measures
against \(\lambda\) proves \(\mu_1=\mu_2\). \(\square\)

## Proof of Corollary 2

For each \(u\in\mathbb T\), choose \(t\in[0,\pi)\) with \(u=e^{2it}\).
The fiber of \(\psi|_{\mathcal Z_p}\) over \(u\) is contained in the line
\[
L_t=\{r e^{it}:r\in\mathbb R\setminus\{0\}\}.
\]
Restrict \(p\) to this line:
\[
Q_t(r)=p(re^{it},re^{-it}).
\]
This is a one-variable polynomial in \(r\). Since
\(0\notin\mathcal Z_p\),
\[
Q_t(0)=p(0,0)\ne0,
\]
so \(Q_t\) is not the zero polynomial. Hence each line through the origin
meets \(\mathcal Z_p\) in only finitely many points. Theorem 1 therefore
applies to any two representing measures whose upper-diagonal extensions
coincide.

Theorem 22(i)--(ii) of Cichoń--Stochel--Szafraniec already shows, under the
present algebraic-support hypotheses, that every representing measure of
\(\gamma\) is carried by \(\mathcal Z_p\), that every such measure produces
an element \(\Gamma(\mu)\in\mathsf{PDE}(\gamma)\), and that every
representing pair for an element of \(\mathsf{PDE}(\gamma)\) has zero
circle component. Thus \(\mu\mapsto\Gamma(\mu)\) is surjective. Theorem 1
makes it injective, hence bijective.

If two representing pairs represented the same \(\Gamma\), their circle
components vanish and Theorem 1 forces their \(\mathbb C^*\)-measures to be
equal; therefore every \(\Gamma\) is determinate. If \(\gamma\) is
indeterminate, its convex set of representing measures has cardinality at
least continuum, and the bijection transfers this cardinality to
\(\mathsf{PDE}(\gamma)\); the reverse inequality follows from
\(\mathsf{PDE}(\gamma)\subset\mathbb C^{\mathfrak N_+}\). Finally, a
singleton \(\mathsf{PDE}(\gamma)\) corresponds under the bijection to a
single representing measure, proving determinacy. \(\square\)

## Why this strengthens the known algebraic case

The 2019 theorem uses injectivity of
\[
\psi(z)=z/\bar z,
\]
which is equivalent to requiring at most one support point on every line
through the origin. The same paper explicitly notes that this condition is
not preserved by polynomial automorphisms: for example, the line \(y=1\)
has the required injectivity, whereas its polynomial image
\[
y=x^2+1
\]
does not. The new argument still applies to the latter parabola, because
every radial line meets it only finitely many times. More generally, the
finite-fiber property is automatic for every algebraic zero set avoiding the
origin, by the one-variable restriction argument above.

The mechanism is that total-degree \(2q\) extension moments recover, for each
angular fiber, all moments of the squared radius, while total-degree
\(2q+1\) moments recover the signed first angular coordinate needed to
distinguish antipodal points. Finiteness of the fiber turns those conditional
moment sequences into finite Vandermonde systems.

## Originality check

Cichoń, Stochel and Szafraniec explicitly leave the converse
\[
|\mathsf{PDE}(\gamma)|=1
\quad\Longrightarrow\quad
\gamma\text{ determinate}
\]
open in full generality. Their algebraic-support result assumes
\(\psi_p\) injective, and their discussion specifically records failures of
that geometric condition for standard curves and after polynomial
automorphisms.

Searches through the publication date covered the paper title and DOI,
\(\mathsf{PDE}(\gamma)\)-singleton determinacy, positive-definite
extensions on the upper-diagonal lattice, algebraic support, finite fibers
and finite intersections with radial lines, and the hyperbola/parabola
examples. A 2020 survey of Szafraniec's work discusses the
determinacy/extendibility paper but does not state this strengthening. A 2025
paper on a dynamic inverse formulation of a complex moment problem concerns
a different one-index moment setup and does not treat these positive-definite
extensions. No source located in these searches removes the injectivity
hypothesis in Theorem 22(v) for all algebraic zero sets avoiding the origin.

Accordingly, the originality claim is **to the best of our knowledge**.
A differently phrased, unpublished, or poorly indexed prior argument may
exist.

## Limitations

The result does not settle the 2019 open question in full generality.
The finite-ray theorem requires finite \(\psi\)-fibers, and the algebraic
corollary assumes an algebraic zero set avoiding the origin. The proof is
measure-theoretic and nonquantitative; it gives uniqueness but no stability
estimate for recovering a measure from perturbed extension moments.
Algebraic supports containing the origin or containing a whole radial line
are not covered by this argument. 

## References

1. D. Cichoń, J. Stochel, F. H. Szafraniec,
   *The complex moment problem: determinacy and extendibility*,
   Mathematica Scandinavica **124** (2019), 263--288.
   https://doi.org/10.7146/math.scand.a-112091

2. R. E. Curto, J.-P. Gazeau, A. Horzela, M. S. Moslehian, M. Putinar,
   K. Schmüdgen, H. de Snoo, J. Stochel, et al.,
   *Mathematical work of Franciszek Hugon Szafraniec and its impacts*,
   Advances in Operator Theory **5** (2020), 1297--1313.
   https://doi.org/10.1007/s43036-020-00089-z

3. A. S. Mikhaylov, V. S. Mikhaylov,
   *On the complex moment problem as a dynamic inverse problem for a discrete
   system*, arXiv:2509.02443v2 (2025).
   https://arxiv.org/abs/2509.02443
