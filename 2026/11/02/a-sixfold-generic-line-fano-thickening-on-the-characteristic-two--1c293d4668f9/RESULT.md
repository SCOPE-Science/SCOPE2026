# A sixfold generic line-Fano thickening on the characteristic-two Segre cubic cone

## Finding

Let \(k=\overline{\mathbb F}_2\). In the symmetric six-coordinate model, set
\[
X=V\left(\sum_{i=0}^{5}x_i,\sum_{i=0}^{5}x_i^3\right)\subset\mathbb P^5_k,
\qquad \mathscr L=F_1(X)=\operatorname{Hilb}_{t+1}(X).
\]
The scheme \(\mathscr L_{\mathrm{red}}\) has **exactly twenty-eight geometric irreducible components**: one copy of the smooth cubic surface \(S\) parametrizing lines through the vertex of \(X\), and twenty-seven copies of \((\mathbb P^2)^\vee\), one for each geometric line on \(S\), parametrizing lines in its cone plane. The latter twenty-seven components are generically reduced.

At the generic point \(\eta\) of the component \(S\), with residue field \(K=k(S)\), the geometric completed local ring of the **unreduced** line-Fano scheme satisfies
\[
\widehat{\mathcal O}_{\mathscr L,\eta}\widehat\otimes_K\overline K
\cong\overline K[u,v]/(u^2,v^3).
\]
In particular the component \(S\) is generically nonreduced with length-six transverse Artin algebra and Hilbert function \((1,2,2,1)\). The assertion concerns the geometric generic local ring, not a global product structure or the scheme structure along intersections of components.

For \(q=2^n\) and every integer \(n\geq1\), the number of \(\mathbb F_q\)-rational geometric lines on this specified cubic threefold is
\[
\#\mathscr L(\mathbb F_q)=
\begin{cases}
16q^2+5q+1,&n\text{ odd},\\
28q^2+7q+1,&n\text{ even}.
\end{cases}
\]
The nilpotent structure does not alter these field-valued point counts. The zeta function of the reduced line scheme over \(\mathbb F_2\) is
\[
Z(\mathscr L_{\mathrm{red}}/\mathbb F_2,T)=
\frac1{(1-T)(1-2T)^6(1+2T)(1-4T)^{22}(1+4T)^6}.
\]
The degree-six local algebra is the central new assertion; the characteristic-two cone, the twenty-seven base-surface lines, and their fields of definition were known independently.

## Assumptions and scope

All geometric assertions are in characteristic \(2\) for the displayed symmetric model. This model is the reduction of the six-coordinate Segre cubic; it should **not** be identified without qualification with other characteristic-two modular models also called the Segre cubic. The Hilbert scheme is the ordinary scheme of **lines** (Hilbert polynomial \(t+1\)); it is not the finite Fano scheme of maximal **planes**. The geometric generic local ring is taken after extending the residue field to its algebraic closure, which is necessary for splitting the quasilinear quadratic normal form in characteristic two. Statements about point counts hold over every \(\mathbb F_{2^n}\).

Write \(V=k^4\), \(s=y_0+y_1+y_2+y_3\), and
\[
F(y)=y_0^3+y_1^3+y_2^3+y_3^3+s^3,
\qquad S=V(F)\subset\mathbb P(V).
\]
The cubic threefold \(X\) is linearly isomorphic to the projective cone \(V(F)\subset\mathbb P(k\oplus V)\), with vertex \(v=[1:0:0:0:0]\).

## Proof

**1. Cone model and smooth base.** In the hyperplane \(\sum x_i=0\), put \(x_5=t\), \(x_i=t+y_i\) for \(0\leq i\leq4\), and eliminate \(y_4=\sum_{i=0}^3y_i\). The characteristic-two binomial expansion gives \(\sum x_i^3=F(y_0,y_1,y_2,y_3)\), independent of \(t\). Furthermore
\[
\frac{\partial F}{\partial y_i}=(y_i+s)^2\quad (0\leq i\leq3).
\]
Vanishing of all four partials implies \(y_i=s\) for all \(i\), hence \(s=4s=0\) and \(y=0\), impossible in projective space. Thus \(S\) is a smooth cubic surface.

**2. Geometric support of the line scheme.** A line through \(v\) is uniquely \(\langle v,[0:s]\rangle\) with \([s]\in S\), giving a closed family isomorphic to \(S\). A line \(L\subset X\) not through \(v\) projects isomorphically from \(v\) onto a line \(\ell\subset S\), and hence lies in its cone plane \(\Pi_\ell=\langle v,\ell\rangle\). Conversely every line in \(\Pi_\ell\) lies in \(X\). The classical twenty-seven-line theorem for smooth cubic surfaces (valid also in characteristic two) gives exactly twenty-seven such plane families \((\Pi_\ell)^\vee\cong\mathbb P^2\), together with the vertex-line family \(S\). Their generic points are disjoint, so all twenty-eight are distinct components of the reduced support.

For a generic line \(L\subset\Pi_\ell\) avoiding \(v\), projection from \(v\) identifies infinitesimal deformations of \(L\subset X\) with deformations of \(\ell\subset S\), together with motions of \(L\) inside \(\Pi_\ell\). The former are trivial because \(N_{\ell/S}\cong\mathcal O_{\mathbb P^1}(-1)\) and \(H^0(N_{\ell/S})=0\). Thus the local dimension of the tangent space is the two dimensions of \((\Pi_\ell)^\vee\), and these components are generically reduced.

**3. Scheme equations near a vertex line.** On a Grassmannian chart near the line \(L_{[s]}=\langle v,[0:s]\rangle\), fix a complement \(U\) to \(ks\subset V\). Write the moving line as the span of \((1,a)\) and \((0,s+b)\), where \(a,b\in U\). Its containment in the cubic is equivalent to the vanishing of the coefficients of \(F(ra+t(s+b))\), namely
\[
F(s+b)=0,\qquad A_1(s+b,a)=0,\qquad A_2(s+b,a)=0,\qquad F(a)=0,
\]
where, setting \(s_z=\sum_i z_i\),
\[
A_1(z,a)=\sum_{i=0}^3(z_i+s_z)^2a_i,\qquad
A_2(z,a)=\sum_{i=0}^3(z_i+s_z)a_i^2.
\]
As \(S\) is smooth, the first equation cuts out the base component regularly in the \(b\)-coordinates. Work at its generic point over \(K=k(S)\), then extend to \(\overline K\). The two forms \(A_1(s,a)\) and \(\sqrt{A_2(s,a)}\) are linear in \(a\) over \(\overline K\). They are independent at the generic point: otherwise the rank-drop locus, which is closed in \(S\), would contain the exact witness in Step 4 below. Thus, after using \(A_1=0\) to eliminate one transverse coordinate, an invertible linear change of transverse variables yields \(A_2=u^2\).

The remaining transverse form is a binary cubic \(F(a)=c v^3+d uv^2+e u^2v+f u^3\). At generic \([s]\), \(c\ne0\): otherwise the direction \(v\) would satisfy \(A_1=A_2=F=0\), giving a line on \(S\) through the generic point, which is impossible because a smooth cubic has only twenty-seven lines. Modulo \(u^2\), the substitution \(v\mapsto v+(d/c)u\) removes the mixed term \(d uv^2\) (the characteristic is two), producing
\[
\overline K[u,v]_{(u,v)}/(u^2,v^3).
\]
This is Artinian local of length \(2\cdot3=6\), with associated graded dimensions \((1,2,2,1)\). The displayed algebra also describes the completion.

**4. Explicit nondegeneracy certificate.** In \(\mathbb F_{32}=\mathbb F_2[\alpha]/(\alpha^5+\alpha^2+1)\), represent coefficients by five-bit polynomials in \(\alpha\). The pairs
\[
s=(1,2,6,16),\qquad w=(0,1,22,31)
\]
are verified exactly by the supplied standalone checker to satisfy
\[
F(s)=0,\quad A_1(s,w)=0,\quad A_2(s,w)=0,\quad F(w)=19\ne0,
\]
while the two linear forms \(A_1(s,\cdot)\) and \(\sqrt{A_2(s,\cdot)}\) are independent. Thus the independence and nonvanishing conditions simultaneously hold on a nonempty Zariski-open subset of \(S\). Any line of \(S\) through this \([s]\) would provide a nonzero transverse vector annihilating all three \(A_1,A_2,F\); the checked condition excludes it. The computer arithmetic here is an exact finite-field witness for nonvanishing of polynomial conditions, not an inference of an infinite statement from samples.

**5. Arithmetic.** Exact enumerations of projective lines in \(\mathbb P^3(\mathbb F_2)\) and \(\mathbb P^3(\mathbb F_4)\), with all four binary-cubic line-restriction coefficients required to vanish, give respectively \(15\) and \(27\) lines on \(S\). The full geometric set therefore splits into fifteen fixed lines and six Frobenius transpositions; all twenty-seven base lines are defined over \(\mathbb F_4\). The geometric lines generate \(\operatorname{Pic}(S_{\overline{\mathbb F}_2})\), on which Frobenius has eigenvalues \(1\) six times and \(-1\) once: Frobenius squared is the identity and its trace is \(5\), as also seen from \(\#S(\mathbb F_2)=15\) and the cubic-surface trace formula. Consequently
\[
\#S(\mathbb F_{2^n})=q^2+(6+(-1)^n)q+1.
\]
Over \(\mathbb F_q\), the number of base lines equals \(21+6(-1)^n\). Each such plane has \(q^2\) lines not through its cone vertex (since there are \(q^2+q+1\) total lines and \(q+1\) through that vertex). Every line not through \(v\) appears in exactly one plane. Adding the vertex-line count proves the claimed formulas and the zeta factorization.

## Verification

The standalone pure-Python program `verify_segre.py` performs exact field arithmetic (not floating-point approximations). It tests all \(35\) lines in \(\mathbb P^3(\mathbb F_2)\) and all \(357\) lines in \(\mathbb P^3(\mathbb F_4)\) against the four cubic restriction coefficients. It also tests all \(155\) lines in \(\mathbb P^4(\mathbb F_2)\) and \(5797\) lines in \(\mathbb P^4(\mathbb F_4)\), obtaining \(75\) and \(477\) lines in the cone, respectively. It identifies fifteen fixed base lines and six Frobenius two-cycles, and checks the explicit \(\mathbb F_{32}\) witness and its nonzero transverse cubic coefficient. The reported final assertion is `SEGRE_CHAR2_CONE_FANO_28_COMPONENTS_6FOLD_VERTEX_75_477_PASS`.

These computations certify specific finite-field facts and the nonempty genericity locus. The description of all geometric components, the nilpotent local algebra, and the formulas over all extensions are supplied by the symbolic and geometric arguments in the Proof section, not asserted solely from enumeration.

## Relationship to prior work

The symmetric Segre equation, its complex geometry, the characteristic-two cone interpretation, the classical twenty-seven lines on a smooth cubic surface, and the splitting of the base lines are pre-existing results; none is claimed as a new standalone finding. Karaoglu's published classification supplies the arithmetic setting of the smooth cubic surface in characteristic two. Cheltsov–Tschinkel–Zhang analyze the Segre cubic in characteristic zero. Dolgachev explains a distinct characteristic-two modular model, so the present claim is explicitly restricted to the symmetric cubic reduction. The contribution here is the **line-Fano Hilbert scheme's generic nonreduced local algebra of length six**, and its integration with the complete geometric component and extension-field count classification. An earlier analysis of the **plane** Fano scheme of the same reduction does not determine this different Hilbert scheme's infinitesimal structure.

## Limitations

This result does not determine the global scheme structure of \(\mathscr L\) along the curves where a vertex line also belongs to one or several of the twenty-seven cone-plane components, nor the intersection multiplicities of those components. The displayed local normal form is geometric-generic, and its square-root coordinate change need not be defined over the unextended function field \(k(S)\). The finite-field verifier establishes no theorem for arbitrary characteristics other than two. Searches and comparisons do not exclude an equivalent treatment hidden in unindexed classical literature. No independent mathematical audit has been performed.

## References

1. E. Karaoglu, *Non-Singular Cubic Surfaces over \(\mathbb F_{2^k}\)*, Turkish Journal of Mathematics (2021), DOI: 10.3906/mat-2102-10. Online publication date 2021-09-29; relevant arithmetic classification of cubic surfaces and rational lines.
2. I. Cheltsov, Y. Tschinkel, Z. Zhang, *Equivariant Geometry of the Segre Cubic and Burkhardt Quartic*, arXiv:2308.15271, first posted 2023-08-29; the characteristic-zero Segre model and its plane geometry.
3. I. Dolgachev, *K3 surfaces of Kummer type in characteristic two*, 2024, DOI: 10.1112/blms.13033; distinction between characteristic-two models.
4. Classical twenty-seven-line theorem for smooth cubic surfaces and the associated Picard/Frobenius trace formula.
