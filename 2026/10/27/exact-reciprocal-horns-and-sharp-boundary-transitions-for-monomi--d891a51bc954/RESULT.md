# Exact reciprocal horns and sharp boundary transitions for monomial Hardy composition operators

## Finding

Let \(m\ge2\) be an integer and let \(0<\alpha\le1\). For any complex \(a\) of modulus \(\alpha\), set \(\varphi(z)=az^m\) and let \(C_\varphi\) act on the classical Hardy space \(H^2(\mathbb D)\). Write \(B(C_\varphi)\) for its Berezin range, and let \(U=\{\zeta^{-1}:\zeta\in B(C_\varphi)\}\). Put \(\beta=(m+1)/2\) and, for \(s>1\), define
\[
R(s)=\alpha s(1-s^{-1})^\beta,\quad
X(s)=s-R(s)R'(s),\quad
Y(s)=R(s)\sqrt{1-R'(s)^2}.
\]
Extend \(X(1)=1\), \(Y(1)=0\). Both \(X\) and \(Y\) increase strictly from these values. Set \(Y_\infty=+\infty\) if \(\alpha<1\), and \(Y_\infty=\sqrt{\beta(\beta-1)}\) if \(\alpha=1\). For \(0\le y<Y_\infty\), let \(s_y\ge1\) be the unique solution \(Y(s_y)=y\), and define \(g(y)=X(s_y)\). For \(\alpha=1\) and \(y\ge Y_\infty\), set \(g(y)=\beta\).

**Exact range and boundary ownership:**
\[
U=\{x+iy:x\ge g(|y|)\}\setminus
\begin{cases}
\varnothing,&0<\alpha<1,\\
\{\beta+iy:|y|\ge\sqrt{\beta(\beta-1)}\},&\alpha=1.
\end{cases}
\]
The original range is exactly \(B(C_\varphi)=\{u^{-1}:u\in U\}\), and zero is never attained. Thus all finite reciprocal-envelope points are attained when \(\alpha<1\); when \(\alpha=1\), the two indicated vertical boundary rays, including their endpoints, are not attained. The limiting excluded rays invert to the open-from-zero portions of the circle with diameter \([0,1/\beta]\), beginning at \((\beta\pm i\sqrt{\beta(\beta-1)})^{-1}\).

**Sharp local geometry:** as \(y\downarrow0\),
\[
g(y)-1\sim(y/\alpha)^{2/(m+1)}.
\]
On the nonreal Berezin boundary tending to \(1\), this is equivalently
\[
|\operatorname{Im}z|\sim\alpha(1-\operatorname{Re}z)^{(m+1)/2}.
\]
The reciprocal envelope is strictly increasing and strictly concave on \((0,Y_\infty)\); for \(\alpha=1\) it continues as the constant \(\beta\). When \(0<\alpha<1\), its far-field asymptotic is
\[
g(y)=\beta+\frac{\sqrt{1-\alpha^2}}{\alpha}y+o(1),\quad y\to\infty.
\]
In particular, the boundary of the original range approaches zero at limiting angles \(\pm\arcsin\alpha\) if \(\alpha<1\), and at the vertical directions if \(\alpha=1\).

## Assumptions and scope

All kernels and inner products are those of classical \(H^2(\mathbb D)\), with normalized reproducing kernels \(k_w(z)=\sqrt{1-|w|^2}/(1-\overline w z)\). The composition symbol is a nonzero complex scalar multiple of one monomial of integral degree \(m\ge2\) and modulus at most one. All statements quantify over every such \(m,a\). The phase of \(a\) does not affect the range since multiplication by a phase only rotates the parameter circles. The zero scalar is excluded from the two-dimensional theorem: for \(a=0\) the range is the real interval \((0,1]\).

## Proof

**1. Reciprocal circles.** The reproducing-kernel identity gives
\[
\widetilde C_\varphi(w)=\frac{1-|w|^2}{1-\overline w\varphi(w)}
=\frac{1-r^2}{1-a r^{m+1}e^{i(m-1)t}}
\]
for \(w=re^{it}\). With \(s=(1-r^2)^{-1}\), the reciprocal \(u=1/\widetilde C_\varphi(w)\) traverses the circle \(|u-s|=R(s)\). Conversely all its points occur because \(m-1\) is a positive integer. Therefore
\[
U=\bigcup_{s\ge1}\{s-R(s)e^{i\theta}:0\le\theta<2\pi\}.
\]
The circles are legitimate throughout: \(R(s)<s\) for every finite \(s\ge1\), hence the reciprocal never vanishes.

**2. Strict envelope monotonicity.** Differentiation yields
\[
R'(s)=\alpha(1-s^{-1})^{\beta-1}
\left(1+\frac{\beta-1}{s}\right),\qquad
R''(s)=\frac{\alpha\beta(\beta-1)}{s^3}
(1-s^{-1})^{\beta-2}>0.
\]
Write \(k=\beta-1>0\) and \(v=s^{-1}\in(0,1)\). Then
\[
R'(s)^2+R(s)R''(s)
=\alpha^2(1-v)^{2k}
[1+2kv+k(2k+1)v^2]<\alpha^2\le1.
\]
Strictness follows because the bracket is exactly the degree-two truncation of the binomial series of \((1-v)^{-2k}\), whose omitted coefficients are positive. In particular \(0<R'(s)<1\). Setting \(D(s)=1-R'(s)^2-R(s)R''(s)>0\), direct differentiation gives
\[
X'(s)=D(s)>0,\qquad
Y'(s)=\frac{R'(s)D(s)}{\sqrt{1-R'(s)^2}}>0.
\]
The initial values and asymptotic limits follow from \(R(s)\sim\alpha s\), \(R'(s)\to\alpha\) if \(\alpha<1\), and from the sharper expansions \(R(s)=s-\beta+O(s^{-1})\), \(R'(s)=1-\beta(\beta-1)/(2s^2)+O(s^{-3})\) if \(\alpha=1\).

**3. Exact horizontal slices and ownership.** Fix \(y\ge0\). Since \(R\) increases without bound, the radii compatible with imaginary part \(y\) form a ray \(s\ge s_0\), where \(R(s_0)=y\). The two real coordinates on the circles are
\[
x_\pm(s)=s\pm\sqrt{R(s)^2-y^2}.
\]
They coincide at \(s_0\), and the upper branch runs continuously to infinity. Every real coordinate at least the infimum of the lower branch is therefore realized, except potentially that infimum when its minimizer escapes to infinity. On \(s>s_0\),
\[
\frac{d}{ds}x_-(s)
=1-\frac{R(s)R'(s)}{\sqrt{R(s)^2-y^2}},
\]
whose sign agrees with that of \(Y(s)-y\). If \(0\le y<Y_\infty\), this derivative changes from negative to positive exactly once at \(s=s_y\); for \(y=0\), the minimum is at \(s=1\). Hence the minimum is attained, with \(x_-(s_y)=X(s_y)=g(y)\). If \(\alpha=1\) and \(y\ge Y_\infty\), the derivative is strictly negative at every finite allowed \(s\), and \(x_-(s)\downarrow\beta\) as \(s\to\infty\); so the slice is \((\beta,\infty)\), not \([\beta,\infty)\). Reflection gives all negative heights. This proves the stated set equality including every boundary point's membership.

**4. Curvature, the cusp and infinity.** For \(0<y<Y_\infty\), the derivative of the envelope can be computed without inverting \(Y\):
\[
g'(y)=\frac{X'(s_y)}{Y'(s_y)}
=\frac{\sqrt{1-R'(s_y)^2}}{R'(s_y)}.
\]
Because \(R''>0\), this is positive and strictly decreasing, proving strict concavity. Write \(s=1+t\) near one. Then \(R(s)\sim\alpha t^\beta\), \(R(s)R'(s)=o(t)\), and \(Y(s)\sim\alpha t^\beta\). This proves the reciprocal-cusp asymptotic. Under inversion \(z=(g(y)+iy)^{-1}\), one has \(1-\operatorname{Re}z\sim g(y)-1\) and \(|\operatorname{Im}z|\sim y\), which yields the stated exponent and coefficient. For \(\alpha<1\), the expansions \(R(s)=\alpha(s-\beta)+O(s^{-1})\), \(R'(s)=\alpha+O(s^{-2})\) imply \(g(y)=\beta+\sqrt{1-\alpha^2}\,y/\alpha+o(1)\). These boundary rays invert to the asserted limiting arguments. When \(\alpha=1\), the vertical reciprocal tail inverts to the circle with diameter \([0,1/\beta]\), with the stated nonattainment.

## Verification

The standalone `checker.py` recomputes the two derivatives and the geometric envelope for a fixed grid of degrees, moduli and circle parameters, compares the supporting abscissa against explicit sampled circles, recovers boundary points independently from normalized kernels, and checks the cusp and full-modulus limiting cases. It uses ordinary floating-point arithmetic and is a diagnostic of derivations, not an exhaustive or computer-assisted proof of the infinite-parameter theorem. Execute `python3 checker.py` from the extracted package directory. The analytical argument above supplies all universal claims.

## Relationship to prior work

Bourdon, Le and Thompson, *Berezin Ranges of Composition Operators on* \(H^2\) (first public arXiv posting 2026-10-13), give general location/topology constraints, show that image circles and their interiors occur for symbols of the form \(z\psi(z^n)\) when \(\psi\) is a **nonconstant** linear-fractional disk map (Proposition 3.7), obtain complete descriptions for specific linear-fractional families, and characterize the linear-symbol convexity problem. Their Proposition 3.7 and its proof supply related circle-filling motivation; their Theorem 3.11 already establishes a qualitative corner at one for maps fixing zero. They do **not** evaluate the explicit monomial reciprocal envelope, its precise missing boundary rays at unit modulus, or its sharp arbitrary-degree cusp exponent and coefficient. These are the assessed claims, not the basic circle reduction or qualitative corner property. Cowen and Felder (2022), and Augustine, Garayev and Shankar (2023), consider related Berezin-range convexity questions, with different symbol families. No claim is made that absence of a located formula proves worldwide publication priority.

## Limitations

This is an exact classification only for one monomial of degree at least two. It does not classify general polynomials, finite Blaschke products, arbitrary weighted Hardy spaces, or all analytic composition symbols. The boundary of the original Berezin range includes zero as a closure point but never as an attained value. Literature-priority uncertainty remains possible for equivalent older envelope calculations under different terminology. All symbolic transformations and limit expansions are proved in the text; finite diagnostic computations do not establish them.

## References

1. Paul Bourdon, Trieu Le, Derek Thompson, *Berezin Ranges of Composition Operators on* \(H^2\), arXiv:2610.17634v1, first public 2026-10-13, https://arxiv.org/abs/2610.17634.
2. Carl C. Cowen and Thomas Felder, *Convexity of the Berezin range*, arXiv:2109.12095, https://arxiv.org/abs/2109.12095.
3. Augustine, Garayev and Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547, https://arxiv.org/abs/2302.12547.
