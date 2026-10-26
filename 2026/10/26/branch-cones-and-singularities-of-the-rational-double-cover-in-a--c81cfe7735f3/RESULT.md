# Branch cones and singularities of the rational double cover in a cubic-threefold parametrization

## Finding

Let \(X\subset\mathbb P^4_{\mathbb C}\) be the smooth cubic threefold
\[
X:\quad w^2x_2+x_1^2x_3+x_2^3+x_3^3+x_4^3=0.
\]
This is the projective completion of the affine cubic in Example 53 of Sendra-Arranz, Sendra and Sendra [1]. Let \(H=\mathcal O_X(1)\). Define the degree-two cover
\[
\pi:Y=\operatorname{Spec}_X\bigl(\mathcal O_X\oplus\mathcal O_X(-H)\bigr)\longrightarrow X,
\qquad s^2=-x_2x_3,
\]
where the indicated multiplication on the second summand is given by the quadratic form \(-x_2x_3\in H^0(X,2H)\).

**Theorem.** The cover \(Y\) is connected, normal, rational, finite flat and Gorenstein. Its reduced branch divisor has two irreducible components
\[D_2=X\cap\{x_2=0\},\qquad D_3=X\cap\{x_3=0\}.\]
Each is an elliptic cubic cone whose plane cubic base is smooth and equianharmonic (\(j=0\)); their vertices are respectively \(P=[1:0:0:0:0]\) and \(Q=[0:1:0:0:0]\). Their scheme-theoretic intersection on \(X\) equals \(3L\), where \(L=\{x_2=x_3=x_4=0\}\simeq\mathbb P^1\). The reduced singular locus of \(Y\) is exactly the line \(\widetilde L=\pi^{-1}(L)_{\mathrm{red}}\). At a general point of \(\widetilde L\), the transverse surface singularity is \(A_5\), analytically \(UV=z^6\); at the two points over \(P,Q\), explicit transverse surface sections have simple-elliptic \(\widetilde E_7\) singularities. Finally,
\[
K_Y=-\pi^*H,\qquad (-K_Y)^3=6.
\]

The function field of \(Y\) is the source rational function field of the degree-two rational parametrization in [1, Example 53], and its nontrivial birational deck involution is explicitly calculated below.

## Assumptions and scope

All schemes, fibers, branches, and analytic classifications are over \(\mathbb C\). Singularities are asserted for the reduced singular locus and transverse **surface** sections, not as a classification of the complete three-dimensional analytic germs at the two vertices. \(Y\) is the canonical finite normalization of \(X\) in the quadratic function-field extension, not the graph of the rational map from \(\mathbb A^3\).

## Proof

**1. The smooth base and elliptic branch cones.** The five partial derivatives of the defining cubic are
\[
(2wx_2,\ 2x_1x_3,\ w^2+3x_2^2,\ x_1^2+3x_3^2,\ 3x_4^2).
\]
Their common zero is the origin, hence the projective cubic is smooth. Setting \(x_2=0\) yields
\(x_1^2x_3+x_3^3+x_4^3=0\), independent of \(w\), so \(D_2\) is the cone with vertex \(P\). Setting \(x_3=0\) yields \(w^2x_2+x_2^3+x_4^3=0\), independent of \(x_1\), so \(D_3\) has vertex \(Q\). Each base cubic is projectively equivalent to \(u^2v+v^3+z^3=0\). Its derivatives \((2uv,u^2+3v^2,3z^2)\) have no common projective zero. The automorphism \([u:v:z]\mapsto[u:v:\zeta_3 z]\) has order three and fixes an origin, whence the elliptic \(j\)-invariant is zero (equivalently write the affine plane equation as \(y^2=-(1+t^3)\)). Intersecting the two hyperplanes within \(X\) leaves the equation \(x_4^3=0\) on the plane \(\{x_2=x_3=0\}\); therefore the intersection as a scheme is the triple line \(3L\).

**2. The cover, rationality and involution.** The rank-two algebra makes \(\pi\) finite flat of degree two. In the function field one may write \(a=s/x_3\) (on \(x_3\ne0\)), giving \(a^2=-x_2/x_3\). The source's rational parametrization, with independent parameters \((a,b,c)\), is
\[
Q_0=a^6-b^3-1,\quad \Delta=Q_0c^2-1,
\]
\[
(x_1,x_2,x_3,x_4)=
\left(\frac{a(1+Q_0c^2)}{\Delta},
\frac{-2a^3c}{\Delta},
\frac{2ac}{\Delta},
\frac{2abc}{\Delta}\right)
\]
in the chart \(w=1\). Direct cancellation shows that these functions satisfy the cubic equation. Conversely,
\[
a^2=-x_2/x_3,\quad b=x_4/x_3,\quad c=x_3/(x_1-a).\]
Thus \(\mathbb C(Y)=\mathbb C(a,b,c)\) is purely transcendental, proving rationality, and the original map has generic degree two. The nonidentity deck transformation is
\[
(a,b,c)\longmapsto\left(-a,\ b,\frac1{(a^6-b^3-1)c}\right);
\]
substitution fixes all four \(x_i\), and a second application is the identity. Divisors of \(x_2\) and \(x_3\) are the reduced Cartier prime divisors \(D_2,D_3\), each with multiplicity one, so \(-x_2/x_3\) is nonsquare by its valuation at \(D_2\). The cover is therefore connected. The quadratic Kummer cover has simple ramification precisely along \(D_2+D_3\); no other divisorial branch component occurs.

**3. Normality, the singular line and generic transverse type.** Locally \(Y\) is the hypersurface \(s^2+x_2x_3=0\) over the smooth threefold \(X\). Away from \(L\), at most one smooth branch cone is encountered, except at its cone vertex, which lies in \(L\), so the cover is smooth. On \(L\), \(s=x_2=x_3=0\), and the differential of the quadratic-cover equation vanishes, proving that every point of \(\widetilde L\) is singular. Since the singular set has codimension two, the hypersurface is \(S_2\) and regular in codimension one, hence normal by Serre's criterion. It is Gorenstein because it is a finite flat double cover of a smooth Gorenstein variety with invertible quadratic trace summand.

At a general point of \(L\), take the affine chart \(w=1\) with \(u=x_1\ne0\). Use local parameters \(u,v=x_3,z=x_4\), eliminating \(p=x_2\) by the implicit-function theorem from
\[
p+u^2v+p^3+v^3+z^3=0.
\]
On the branch cone \(p=0\), one has \(u^2v+v^3+z^3=0\), hence its local branch curve has \(v=\phi(z)\) with \(\phi(z)=-z^3/u^2+O(z^9)\). Since \(p\) vanishes simply on this curve, \(p=\varepsilon(v,z)(v-\phi(z))\) for an analytic unit \(\varepsilon\). On a transverse slice \(u=u_0\ne0\), an analytic square-root rescaling of \(s\) yields \(s'^2+v(v-\phi(z))=0\). Completing the square and changing a unit in \(z\) gives \(UV=z^6\), i.e. an \(A_5\) surface singularity.

**4. Exceptional transverse sections.** At \(P\), work in the chart \(w=1\) and slice \(x_1=0\). The cubic equation implies \(p+p^3+v^3+z^3=0\), so \(p=-(v^3+z^3)\varepsilon(v,z)\) for an analytic unit \(\varepsilon(0)=1\). The double-cover slice is analytically
\[
s'^2=v(v^3+z^3).
\]
At \(Q\), use the chart \(x_1=1\) and slice \(w=0\). The same argument gives \(s'^2=p(p^3+z^3)\). Both branch binary quartics have four distinct linear factors over \(\mathbb C\), so these weighted-homogeneous double-plane surface singularities are of simple-elliptic type \(\widetilde E_7\). These descriptions concern the stated transverse slices only.

**5. Canonical class.** The adjunction formula on a smooth cubic threefold gives \(K_X=-2H\). The canonical-sheaf formula for a finite flat double cover with trace line \(\mathcal O_X(-H)\) gives \(K_Y=\pi^*(K_X+H)=-\pi^*H\); this Cartier class is antiample and its cube equals \(2H^3=6\).

## Verification

The accompanying `verify.py` is standalone Python with SymPy. It checks the full source parametrization against the cubic, its rational inverse in the quadratic field, the involution substitution, the two branch equations and the triple intersection, the exact Jacobian, and the quartic's distinct tangent directions. The normality, infinite-family local claims and canonical formula are mathematical proofs above rather than inferred from finite tests.

To replay after extracting the file from this package, run `python3 verify.py` with SymPy installed. The expected terminal line is `VERIFY_OK rational_double_cover_branch_profile`.

## Relationship to prior work

Sendra-Arranz, Sendra and Sendra [1, Example 53] provide the rational functions and their degree-two map to this cubic threefold. Their focus is the theory of radical towers and unirationality, not the resolution of the branch geometry. The present result starts from their specific parametrization and classifies the associated quadratic field cover, ramification divisors and transverse singularities. General double-cover adjunction and ramification formulas are standard (see [2]); they do not supply the explicit identification of two elliptic cones meeting as a triple line or the exceptional transverse singularities. Search and priority comparisons are documented in `AUDIT.json` and `REVIEW.md`.

## Limitations

The theorem is specific to the displayed cubic and its indicated double cover; it does not classify arbitrary degree-two unirational parametrizations of cubic threefolds. It determines transverse surface sections at the two vertices, not complete local analytic types of the ambient threefold singularities or their resolutions. The finite checker is corroborating evidence, not independent validation. No independent mathematical audit has been performed.

## References

[1] J. Sendra-Arranz, J. R. Sendra and J. Sendra, *On the Structure of Radical Towers and their Parametrizations*, arXiv:2610.20404v1 (first posted 2026-10-14), Example 53; https://arxiv.org/html/2610.20404v1.

[2] R. Pardini, *Abelian covers of algebraic varieties*, Journal für die reine und angewandte Mathematik 417 (1991), 191–213. General background on abelian/double-cover constructions; not a source for the explicit cubic classification.
