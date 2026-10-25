# Exponential Schatten smoothing for separated composition cross-products

## Finding

An explicit uniform separation of two analytic disk self-maps from *simultaneous* boundary approach forces their cross-adjoint composition product into every Schatten ideal, even when neither factor is compact. In particular, the missing quasi-Schatten range for the unweighted Bergman linear-fractional cross-product is controlled by exponential singular-value decay.

Write \(\mathbb D=\{z\in\mathbb C:|z|<1\}\) and let \(dA\) be normalized planar area measure. For \(\alpha>-1\), define the analytic Hilbert space \(H_\alpha\) using
\[
d\mu_\alpha(z)=\frac{(-\log|z|^2)^\alpha}{\Gamma(\alpha+1)}\,dA(z),\qquad
\|f\|_{H_\alpha}^2=\int_{\mathbb D}|f(z)|^2\,d\mu_\alpha(z).
\]
Set \(H_{-1}=H^2(\mathbb D)\), with normalized boundary arc measure. The normalized monomial basis is, for every \(\alpha\ge-1\),
\[
e_n(z)=(n+1)^{(\alpha+1)/2}z^n,\qquad n\ge0.
\]

**Quantitative separation theorem.** Let \(\varphi,\psi:\mathbb D\to\mathbb D\) be analytic, and suppose that \(C_\varphi,C_\psi\) are bounded on the chosen \(H_\alpha\). Define
\[
\delta(\varphi,\psi)=\sup_{z\in\mathbb D}
\min\bigl\{|\varphi(z)|,|\psi(z)|\bigr\}.
\]
If \(\delta<1\), then for every \(r\) with \(\delta<r<1\) and integer \(N\ge1\),
\[
\boxed{\ s_{2N+1}(C_\psi^*C_\varphi)
\le (\|C_\varphi\|+\|C_\psi\|)
\left[\sum_{n=N}^{\infty}(n+1)^{\alpha+1}r^{2n}\right]^{1/2}.\ }
\tag{1}
\]
Singular values are numbered from one, with multiplicity. In particular,
\[
\boxed{\ \limsup_{j\to\infty}s_j(C_\psi^*C_\varphi)^{1/j}
\le\sqrt\delta<1,\qquad
C_\psi^*C_\varphi\in\bigcap_{p>0}\mathcal S_p(H_\alpha).\ }
\tag{2}
\]
The convention at \(\delta=0\) is that the exponential upper bound is zero; one of the two maps must then be constant, and the product has rank at most one.

**Complete linear-fractional criterion.** For two nonconstant linear-fractional disk self-maps, which are holomorphic past the closed disk, set
\[
F_\varphi=\{\zeta\in\partial\mathbb D:|\varphi(\zeta)|=1\},\qquad
F_\psi=\{\zeta\in\partial\mathbb D:|\psi(\zeta)|=1\}.
\]
For every \(\alpha\ge-1\) and every \(p>0\), the following are equivalent:
\[
\boxed{\ F_\varphi\cap F_\psi=\varnothing
\quad\Longleftrightarrow\quad
C_\psi^*C_\varphi\in\mathcal S_p(H_\alpha)
\quad\Longleftrightarrow\quad
C_\psi^*C_\varphi\in\bigcap_{q>0}\mathcal S_q(H_\alpha).\ }
\tag{3}
\]
The source condition for noncompactness in the converse is recalled explicitly below.

## Assumptions and scope

The maps are genuine analytic self-maps, meaning \(|\varphi(z)|,|\psi(z)|<1\) for every interior \(z\). The operators are assumed bounded for the quantitative theorem; boundedness holds for linear-fractional self-maps of these Hardy and logarithmic Bergman spaces. The letter \(\alpha\) denotes the *specific normalized logarithmic weight* above; replacing it by a norm-equivalent standard power weight changes adjoints, so the exact product must not be transported by norm equivalence without qualification. For \(\alpha=0\), this is the classical unweighted Bergman space. The term \(\mathcal S_p\) is the usual Schatten quasi-ideal for \(0<p<1\) and Schatten ideal for \(p\ge1\).

No claim of exact exponential rate is made; (2) is an explicit upper bound. The classification (3) uses nonconstant linear-fractional symbols; general analytic symbols with \(\delta=1\) are not classified here.

## Proof

**1. Moment normalization.** Writing \(t=|z|^2\) and using normalized area measure gives
\[
\int_{\mathbb D}|z|^{2n}\,d\mu_\alpha(z)
=\frac1{\Gamma(\alpha+1)}\int_0^1 t^n(-\log t)^\alpha\,dt
=(n+1)^{-\alpha-1}.
\]
Thus the displayed monomials are orthonormal. For \(\alpha=-1\), the Hardy circle integral gives norm one to every monomial. This justifies the basis and all powers in (1).

**2. Uniform two-region separation.** Fix \(\delta<r<1\). For \(\alpha>-1\), split the disk (up to null sets) into
\[
E=\{z:|\varphi(z)|\le r\},\qquad F=\mathbb D\setminus E.
\]
On \(F\) we necessarily have \(|\psi(z)|\le\delta<r\). For the Hardy case, take radial boundary values and make the same partition on \(\partial\mathbb D\). The pointwise interior bound \(\min\{|\varphi(z)|,|\psi(z)|\}\le\delta\) passes to the almost-everywhere radial boundary limits. For bounded Hardy composition operators the boundary identification \((C_\varphi f)^*=f^*\circ\varphi^*\) holds where the boundary value of \(\varphi\) lies on the circle, and otherwise the right side is ordinary analytic evaluation; it is first checked on polynomials and extended by boundedness. Hence the same restriction estimates apply in the circle model.

Let \(P_N\) project onto \(\operatorname{span}\{e_0,\ldots,e_{N-1}\}\) and put \(Q_N=I-P_N\). Write \(J\) for the isometric embedding of \(H_\alpha\) into its representing \(L^2\) space, and \(R_E,R_F\) for multiplication by the two indicator functions, followed by restriction. Then
\[
T=C_\psi^*C_\varphi
=(R_EJC_\psi)^*(R_EJC_\varphi)
 +(R_FJC_\psi)^*(R_FJC_\varphi).
\]
Since \(|\varphi|\le r\) on \(E\),
\[
\|R_EJC_\varphi Q_N\|_{\mathcal S_2}^2
=\sum_{n=N}^\infty\int_E|e_n(\varphi(z))|^2\,d\mu_\alpha(z)
\le\sum_{n=N}^\infty(n+1)^{\alpha+1}r^{2n}=:B_N(r)^2.
\]
For the Hardy circle case, use normalized arc measure in the same formula. Similarly \(\|R_FJC_\psi Q_N\|_{\mathcal S_2}\le B_N(r)\). Restriction cannot increase the norm, giving \(\|R_EJC_\psi Q_N\|\le\|C_\psi\|\) and \(\|R_FJC_\varphi Q_N\|\le\|C_\varphi\|\). Therefore
\[
\|Q_NTQ_N\|
\le(\|C_\varphi\|+\|C_\psi\|)B_N(r).
\tag{4}
\]
Here only the elementary inequalities \(\|A^*B\|\le\|A\|\|B\|\) and \(\|B\|\le\|B\|_{\mathcal S_2}\) for Hilbert–Schmidt operators are used.

**3. Rank and approximation numbers.** The operator
\[
T-Q_NTQ_N=P_NT+Q_NTP_N
\]
has rank at most \(2N\). For a bounded Hilbert-space operator, \(s_{2N+1}(T)\le\|T-Q_NTQ_N\|\). Together with (4), this proves (1). For each fixed \(0<r<1\), the ratio test or a geometric-series tail estimate gives
\[
B_N(r)=O_{\alpha,r}\bigl((N+1)^{(\alpha+1)/2}r^N\bigr).
\]
Monotonicity of singular values extends the odd-index estimates to every index, with \(\limsup_{j\to\infty}s_j(T)^{1/j}\le\sqrt r\); now decrease \(r\) to \(\delta\). Since exponential sequences belong to \(\ell^p\) for *every* \(p>0\), even \(0<p<1\), the Schatten conclusion follows. If \(\delta=0\), the product \(\varphi\psi\) vanishes identically, so analyticity forces at least one map to be constant and the product has rank at most one.

**4. Boundary-contact equivalence for linear fractions.** Every nonconstant linear-fractional disk map extends continuously to the closed disk, and its boundary-contact set is a closed subset of the unit circle. Compactness of the closed disk implies
\[
\delta<1\quad\Longleftrightarrow\quad F_\varphi\cap F_\psi=\varnothing.
\tag{5}
\]
(The forward direction is immediate. For the reverse direction, \(\min\{|\varphi|,|\psi|\}\) has maximum strictly below one on the compact closed disk.) Combining (5) with (1) proves all forward implications in (3).

For the converse with \(\alpha>-1\), use Clifford–Zheng, *Composition Operators on Bergman Spaces* (2003), Theorem 1.3: for nonconstant univalent disk maps, compactness of this same cross-adjoint product on the normalized logarithmic weighted Bergman space is equivalent to
\[
\lim_{|z|\to1^-}
\frac{(1-|z|)^2}{(1-|\varphi(z)|)(1-|\psi(z)|)}=0.
\tag{6}
\]
At a common boundary contact \(\zeta\), linear-fractional analyticity gives \(1-|\varphi(t\zeta)|=O(1-t)\) and \(1-|\psi(t\zeta)|=O(1-t)\) as \(t\uparrow1\). Thus the quotient in (6) stays bounded below by a positive constant along that radius, and the product is not compact. All Schatten operators are compact. For \(\alpha=-1\), the same exclusion follows directly from Leng–Zhao (2026), Theorem 3.4(b), which characterizes the full Hardy range \(0<p<\infty\). This proves (3), including the quasi-Schatten endpoint.

**5. An infinite-rank example with noncompact factors.** Set \(\varphi(z)=(1+z)/2\), \(\psi(z)=(1-z)/2\). Their boundary contacts are \(\{1\}\) and \(\{-1\}\), respectively, and
\[
|\varphi(z)|^2+|\psi(z)|^2=(1+|z|^2)/2.
\]
Hence \(\delta=1/\sqrt2\), with equality approached radially toward \(i\). Estimate (2) yields \(\limsup_{j\to\infty}s_j(T)^{1/j}\le2^{-1/4}\). Both individual composition operators are noncompact (they have finite angular derivatives at their own boundary-contact points). Nonetheless their cross-product lies in all Schatten ideals and has infinite rank. Indeed, \(C_\varphi\) is injective by the identity theorem and \(C_\psi\) has dense range because every polynomial \(q(z)\) equals \(g(\psi(z))\) for the polynomial \(g(w)=q(1-2w)\). Thus \(C_\psi^*\) is injective and so is \(T\); an injective operator on this infinite-dimensional space cannot have finite rank.

## Verification

The analytic proof above establishes the general infinite-dimensional result; numerical calculations are supplementary. The enclosed `verify.py` uses only the Python standard library to check exact normalized area moments, the affine example's separation identity and boundary equality, the finite matrix-element formula for the unweighted Bergman cross-product, and the prescribed tail rates in finite parameter tests. It never treats finite truncation as a proof of Schatten membership. Run: `python verify.py`.

## Relationship to prior work

Leng and Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (first posted 11 October 2026), Theorem 4.6(ii), characterizes \(C_\psi^*C_\varphi\in\mathcal S_p\) for linear-fractional Bergman symbols only when \(1<p<\infty\); their Lemma 4.5(b) explicitly explains that the auxiliary correction is controlled only in that range. Theorem 3.4(b) already settles *all* Schatten exponents on Hardy space; no Hardy qualitative classification is claimed here as new. Their Theorem 4.7 and Proposition 4.9 also supply general sufficient criteria and trace-class information, which are likewise not claimed as new. The contribution here is the direct, explicit exponentially decaying singular-value estimate, yielding every quasi-Schatten exponent \(0<p<1\) on the Bergman space and an extension to the normalized logarithmic weighted scales.

Clifford and Zheng, *Composition Operators on Bergman Spaces*, Chinese Annals of Mathematics Series B 24 (2003), 433–448, Theorem 1.3, already provide the relevant compactness criterion in the identical normalized logarithmic-weight Hilbert space. That classical theorem is used for necessity, not counted as a new compactness result. Earlier studies of weighted composition operators, including Čučković and Zhao (2004), concern individual weighted composition maps and general Schatten conditions; an equivalence via an unpublished or unindexed two-sided localization estimate cannot be excluded.

## Limitations

Equation (1) is a uniform *upper estimate*, not an exact singular-value asymptotic. The full equivalence (3) is asserted only for nonconstant linear-fractional disk maps; the separation theorem itself allows arbitrary bounded composition maps with \(\delta<1\). The Hardy endpoint \(\alpha=-1\) is treated through its boundary-measure model rather than as a limit of the logarithmic weight. The logarithmic measure normalization is essential to the displayed polynomial power and to the exact adjoint; replacing the measure with a norm-equivalent power weight is not an identity of operators. The proof uses a published compactness theorem for the necessity direction, and originality retains the usual possibility of equivalent formulations in unindexed earlier literature. No independent scientific validation is asserted.

## References

1. Q. Leng and X. Zhao, *Schatten class membership of products of composition operators and their adjoints*, arXiv:2610.15472v1 (11 October 2026), Sections 3–4, particularly Theorems 3.4 and 4.6, Lemma 4.5, and Proposition 4.9. https://arxiv.org/html/2610.15472v1
2. J. H. Clifford and D. Zheng, *Composition Operators on Bergman Spaces*, Chinese Annals of Mathematics Series B **24** (2003), 433–448, Theorem 1.3. https://math.vanderbilt.edu/zhengd/gen.pdf ; doi:10.1142/S0252959903000438
3. Ž. Čučković and R. Zhao, *Weighted Composition Operators on the Bergman Space*, Journal of the London Mathematical Society **70** (2004), 499–511, doi:10.1112/S0024610704005605 (related context; not used for the central proof).
