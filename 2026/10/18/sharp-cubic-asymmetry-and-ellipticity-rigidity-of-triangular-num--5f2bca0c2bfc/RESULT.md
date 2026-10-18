# Sharp cubic asymmetry and ellipticity rigidity of triangular numerical ranges on \(\ell_p^2\)

## Finding

For every \(1<p<\infty\), consider the complex spatial numerical range \(W_p(T)\) of
\[
T=\begin{pmatrix}a&b\\0&d\end{pmatrix}\quad\text{on }\ell_p^2(\mathbb C).
\]
The following classification is exact:

**Theorem.** If \(b\ne0\), the range is a convex body bounded by a real-analytic, strictly convex Jordan curve of everywhere strictly positive curvature. If also \(a\ne d\), this body is centrally symmetric **if and only if** \(p=2\). Consequently, among nondegenerate triangular ranges, an elliptic numerical range occurs exactly at the Hilbert exponent. The remaining cases are complete: \(b=0\) gives the diagonal line segment, and \(a=d\), \(b\ne0\) gives a disk at every exponent.

There is a quantitative obstruction to central symmetry. Let \(a\ne d\), \(b\ne0\), put \(L=|a-d|\), \(B=|b|\), \(\alpha=(p-1)/p\), \(\beta=1/p\), and normalize the planar set to \(K=\overline{(a-d)}(W_p(T)-d)/|a-d|\). Its support function in direction \(e^{i\theta}\) is \(h(\theta)=G(L\cos\theta)\), where
\[
F=\alpha^\alpha\beta^\beta,\qquad
G(c)=\max_{0\le t\le1}\left\{ct+B t^\alpha(1-t)^\beta\right\}.
\]
The exact cubic asymmetry invariant is
\[
\boxed{G'''(0)=\frac{2\alpha\beta(\beta-\alpha)}{B^2F^2}}
=\frac{2(p-1)(2-p)}{p^3B^2F^2}.
\]
For instance, when \(p=4\) and \(B=1\), the derivative equals \(-1/\sqrt3\), independent of the nonzero diagonal gap \(L\). This nonzero cubic term precludes every possible symmetry centre.

**Sharp quantitative asymmetry.** For a compact plane set \(K\), let \(d_{\mathrm H}\) denote Euclidean Hausdorff distance and define its central-symmetry defect by
\[
\mathfrak s(K)=\inf_{\zeta\in\mathbb C}d_{\mathrm H}(K,2\zeta-K).
\]
In the nondegenerate triangular case, as the diagonal gap \(L=|a-d|\) tends to zero relative to \(B=|b|>0\),
\[
\boxed{\mathfrak s(W_p(T))=\frac{|\alpha\beta(\beta-\alpha)|}{6F^2}\frac{L^3}{B^2}+O_p\!\left(\frac{L^5}{B^4}\right).}
\]
The coefficient is sharp; it is strictly positive precisely for \(p\ne2\). For \(p=4\), the leading term is \(L^3/(12\sqrt3 B^2)\). Thus central asymmetry first appears at cubic rather than linear or quadratic order under a small diagonal split.

## Assumptions and scope

The scalar field is complex and \(1<p<\infty\) is fixed. For unit vectors \(x=(x_1,x_2)\), the unique norming functional has coordinates \(\overline{x_j}|x_j|^{p-2}\) (with the continuous value zero at a zero coordinate), and \(W_p(T)=\{\langle Tx,J_p(x)\rangle:\|x\|_p=1\}\). No restriction is imposed on the complex phases of \(a,b,d\), and endpoints \(b=0\), \(a=d\), and \(p=2\) are included separately.

## Proof

**1. Exact circle and disk descriptions (used as previously known geometry).** Set \(t=|x_1|^p\) and choose the relative phase of the two coordinates freely. Direct evaluation gives
\[
W_p(T)=\bigcup_{0\le t\le1}\left\{d+(a-d)t+B t^\alpha(1-t)^\beta e^{i\phi}:0\le\phi<2\pi\right\}.
\]
Write \(f(t)=t^\alpha(1-t)^\beta\). Every circle's entire filled disk is included in this union: if \(|z-d-(a-d)t_0|\le Bf(t_0)\), the continuous function \(\Phi(t)=|z-d-(a-d)t|-Bf(t)\) satisfies \(\Phi(0)\ge0\) and \(\Phi(t_0)\le0\). The intermediate-value theorem produces \(s\in[0,t_0]\) with \(\Phi(s)=0\). Thus
\[
W_p(T)=\bigcup_{0\le t\le1}\overline D\bigl(d+(a-d)t,Bf(t)\bigr).
\]
The function \(f\) is strictly concave on \((0,1)\) because
\[
f''(t)=-\frac{\alpha\beta f(t)}{t^2(1-t)^2}<0.
\]
Therefore this filled-disk union is convex. Convexity of the entire triangular class is already established in Mandal--Bhanja--Bag--Paul (2020 preprint/2022 journal, Corollary 2.6.1); the disk argument is included only to fix the normalization and derive the new curvature/rigidity statements.

**2. Unique analytic support and positive curvature.** Assume \(B>0\). Since \(f'(0+)=+\infty\), \(f'(1-)=-\infty\), and \(f''<0\), for every finite \(c\in\mathbb R\) the unique maximizer \(t(c)\in(0,1)\) of \(ct+Bf(t)\) is determined by
\[
c+Bf'(t(c))=0.
\]
Implicit differentiation shows that \(t(c)\) and \(G(c)\) are real analytic, with
\[
G'(c)=t(c),\qquad G''(c)=\frac1{-Bf''(t(c))}>0.
\]
If \(L=0\), the numerical range is the disk of radius \(BF\), so the claim is immediate. If \(L>0\), rotate and translate to the set \(K\) in the statement. Its support is \(h(\theta)=G(L\cos\theta)\). By differentiation, with \(c=L\cos\theta\),
\[
\boxed{h(\theta)+h''(\theta)
=Bf(t(c))+\frac{L^2\sin^2\theta}{-Bf''(t(c))}>0.}
\]
The normal-parametrized boundary \(z(\theta)=e^{i\theta}(h(\theta)+i h'(\theta))\) is real analytic and has derivative \(z'(\theta)=i e^{i\theta}(h+h'')\), never zero. Hence it is a real-analytic strictly convex closed curve with positive radius of curvature \(h+h''\); the corresponding curvature is its positive reciprocal. This also proves that all exposed points and supporting lines are unique.

**3. Exact third-derivative obstruction to central symmetry.** At \(c=0\), the unique maximizer is \(t(0)=\alpha\) and \(F=f(\alpha)=\alpha^\alpha\beta^\beta\). Direct differentiation yields
\[
Bf''(\alpha)=-\frac{BF}{\alpha\beta},\qquad
Bf'''(\alpha)=\frac{2BF(\beta-\alpha)}{\alpha^2\beta^2}.
\]
Implicit differentiation of \(c+Bf'(t(c))=0\) gives
\[
G'''(0)=\frac{-Bf'''(\alpha)}{(Bf''(\alpha))^3}
=\frac{2\alpha\beta(\beta-\alpha)}{B^2F^2}.
\]
It vanishes exactly when \(p=2\). If \(p\ne2\), suppose for contradiction that \(K\) is centrally symmetric. It has nonempty interior, so its centre is unique. Because \(K\) is invariant under complex conjugation, that centre must be a real number \(x_0\). Central symmetry forces the odd support difference
\[
h(\theta)-h(\theta+\pi)=2x_0\cos\theta.
\]
Equivalently \(G(c)-G(-c)=2x_0c/L\) for every \(-L\le c\le L\), contradicting the nonzero third derivative at zero. Therefore \(K\), and so \(W_p(T)\), is not centrally symmetric for \(p\ne2\). No ellipse has this property. At \(p=2\), the maximization gives
\[
G(c)=\tfrac12\bigl(c+\sqrt{c^2+B^2}\bigr),
\]
and hence the standard filled elliptic range (with axis of symmetry along \(a-d\)). The cases \(b=0\) (segment) and \(a=d\) (disk) follow from the circle formula.

**4. Sharp Hausdorff asymmetry law.** For compact convex sets, Hausdorff distance equals the uniform distance of support functions. The normalized set \(K\) is symmetric across the real axis, so averaging the errors for directions \(\theta\) and \(-\theta\) shows that allowing a complex reflection centre cannot improve over a real centre. With \(x=\cos\theta\), one therefore has the exact identity
\[
\mathfrak s(K)=\inf_{z\in\mathbb R}\max_{-1\le x\le1}
\left|G(Lx)-G(-Lx)-2zx\right|.
\]
Taylor's theorem at zero, uniformly for \(x\in[-1,1]\), gives
\[
G(Lx)-G(-Lx)=2\alpha Lx+\frac{G'''(0)}3L^3x^3
+O_p(L^5/B^4)
\]
when \(L/B\) is sufficiently small. The unique best uniform approximation to \(x^3\) by a multiple of \(x\) on \([-1,1]\) is \((3/4)x\), with minimax error \(1/4\). Indeed,
\[
x^3-\tfrac34x=\tfrac14(4x^3-3x),
\]
whose absolute value is at most \(1/4\); any smaller uniform error would force the proposed slope to be simultaneously greater and less than \(3/4\) when evaluated at \(x=1\) and \(x=1/2\). The distance to a linear subspace in the uniform norm changes by at most the uniform size of a perturbation. Thus
\[
\mathfrak s(K)=\frac{|G'''(0)|}{12}L^3+O_p(L^5/B^4)
=\frac{|\alpha\beta(\beta-\alpha)|}{6F^2}\frac{L^3}{B^2}
+O_p(L^5/B^4).
\]
Translation and rotation preserve Euclidean Hausdorff distance, so \(\mathfrak s(K)=\mathfrak s(W_p(T))\). The explicit centre \(z=\alpha L+G'''(0)L^3/8\) in the normalized coordinates is asymptotically optimal to the displayed order. The coefficient vanishes at \(p=2\), when the exact defect is zero.

## Verification

The proof is independent of finite sampling. The included `checker.py` uses only the Python standard library and verifies the critical derivative identity, supporting-point uniqueness numerically, strict positive curvature, the Hölder-conjugate circle reflection, representative direct norming-functional values, and the leading symmetry-defect coefficient at shrinking diagonal gaps. Its test thresholds are stated in its code. Reproduce with `python3 checker.py` from the same extracted package directory. Exact formulas for the derivative and curvature are proved above; finite numerical tests are supplementary.

## Relationship to prior work

Mandal, Bhanja, Bag, and Paul (arXiv:2005.01288, 2020; Journal of Convex Analysis 2022) already proved **convexity of every triangular complex \(\ell_p^2\) numerical range** (Corollary 2.6.1), an envelope description for the trace-zero triangular class (Theorem 2.7), and conjugate-exponent transpose relations (Theorems 2.10--2.11). These statements are prior results, not claims of novelty here. In particular, convexity and the circle parametrization are not new.

Müller and Tomilov (arXiv:2606.22693, first public 2026-06-21) obtained a general circle parametrization and proved star-shapedness of triangular ranges (Proposition 2.8); that is also prior work. Their discussion highlights the contrast with nonconvex \(2\times2\) nontriangular examples. The additional claim here is the **sharp cubic Hausdorff symmetry-defect law**, **complete symmetry/ellipticity classification** and **uniform positive-curvature regularity**, with an explicit nonzero cubic invariant valid for arbitrary complex diagonal data. Existing boundary envelopes do not state this equivalence or obstruction.

## Limitations

The classification concerns complex \(2\times2\) **triangular** operators in the canonical \(\ell_p\) coordinate norm, not arbitrary matrices or higher dimensions. In this setting a disk or segment may arise from degenerate diagonal or coupling data at any exponent. The cubic formula and Hausdorff asymptotic are for a fixed exponent with a small diagonal gap relative to a nonzero off-diagonal coupling; they are not presented as general invariants of all Banach-space numerical ranges. The priority comparison includes the accessible full texts of the two directly relevant papers; previously unnoticed equivalent classifications remain possible and independent audit has not been carried out.

## References

- K. Mandal, A. Bhanja, S. Bag, K. Paul, *On the numerical range of operators on some special Banach spaces*, arXiv:2005.01288 (first public 2020-05-04); *Journal of Convex Analysis* 29 (2022), 371--380, DOI:10.68381/jca29023. In particular Corollary 2.6.1, Theorem 2.7, and Theorems 2.10--2.11.
- V. Müller and Yu. Tomilov, *Numerical and essential numerical ranges on \(\ell_p\)*, arXiv:2606.22693 (first public 2026-06-21), Section 2.3, especially Proposition 2.8.
