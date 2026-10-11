# Exact Euclidean Banach–Mazur distance of conjugate Day–James planes
## Finding
For every real \(p>2\), let \(q=p/(p-1)\) and \(\alpha=(p-2)/p\). Define the conjugate Day–James norm on \(\mathbb R^2\) by
\[
N_p(x,y)=
\begin{cases}
(|x|^p+|y|^p)^{1/p},&xy\ge 0,\\
(|x|^q+|y|^q)^{1/q},&xy\le 0.
\end{cases}
\]
There is a unique \(s_p\in(0,1)\) satisfying
\[
\frac{1-s_p^{p-1}}{1-s_p}=2^{\alpha}(1+s_p^p)^{\alpha}.
\]
Put
\[
\rho_p=-\frac{s_p(1-s_p^{p-2})}{1-s_p^p}.
\]
Then, up to multiplication by a positive scalar, the Euclidean norm
\[
H_p(x,y)=\sqrt{x^2+y^2+2\rho_pxy}
\]
is an optimal Euclidean pullback for \(X_p=(\mathbb R^2,N_p)\), and
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2
=2^{2\alpha}\frac{1+\rho_p}{1-\rho_p}
=2^{2\alpha}\frac{(1-s_p)(1+s_p^{p-1})}{(1+s_p)(1-s_p^{p-1})}.
\]
For the natural even exponent \(p=4\), this becomes
\[
\rho_4=-\frac1{1+\sqrt6},
\qquad
d_{\mathrm{BM}}(X_4,\ell_2^2)^2=6-2\sqrt6.
\]

## Assumptions and scope
The result is over the real scalars and concerns \(2<p<\infty\). The conjugate exponent is exactly \(q=p/(p-1)\). The Banach–Mazur distance is the multiplicative distance. The endpoint \(p=2\) is not part of the quantified claim; there the two quadrant norms coincide and the space is Euclidean.

The source family is classical: Martini and Swanepoel identify the mixed \(\ell_p\)-\(\ell_q\) norm with conjugate exponents as a Radon norm, and Alonso records the Day–James construction and its generalized form. The argument below independently derives the Euclidean distortion and does not assume an unpublished distance formula.

## Proof
Let \(S(x,y)=(y,x)\). Since \(N_p(Sz)=N_p(z)\), any positive definite quadratic form \(Q\) used to compare \(N_p\) with a Euclidean norm can be averaged with \(S^TQS\). If
\[
m\,z^TQz\le N_p(z)^2\le M\,z^TQz
\]
holds for all \(z\), the same inequalities hold after this averaging. Hence an optimal Euclidean norm may be taken, after scaling, in the one-parameter form
\[
H_\rho(x,y)^2=x^2+y^2+2\rho xy,
\qquad -1<\rho<1.
\]

The conjugacy \(1/p+1/q=1\) makes \(N_p\) a normalized Radon norm for the determinant form. This can also be checked directly from Hölder duality: in a same-sign quadrant the determinant supremum is the \(\ell_p\) norm because the maximizing vector lies in an opposite-sign \(\ell_q\) quadrant, and conversely. Thus the antinorm of \(N_p\) equals \(N_p\). The antinorm of \(H_\rho\) is
\[
(H_\rho)_a=\frac{H_\rho}{\sqrt{1-\rho^2}}.
\]
If
\[
m_\rho=\inf_{z\ne0}\frac{N_p(z)^2}{H_\rho(z)^2},
\qquad
M_\rho=\sup_{z\ne0}\frac{N_p(z)^2}{H_\rho(z)^2},
\]
dualizing the two comparison inequalities gives both opposite product bounds and therefore the exact reciprocity
\[
m_\rho M_\rho=\frac1{1-\rho^2}.
\]
Consequently
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2
=\inf_{-1<\rho<1} M_\rho^2(1-\rho^2).
\]

By the coordinate-swap symmetry it suffices in a same-sign quadrant to put \(t=|y/x|\in[0,1]\). There
\[
R_{p,\rho}(t)
=\frac{(1+t^p)^{2/p}}{1+t^2+2\rho t}.
\]
For \(-\alpha<\rho<0\), an interior critical point satisfies
\[
-\rho=f_p(t):=\frac{t(1-t^{p-2})}{1-t^p}.
\]
The function \(f_p\) is strictly increasing from \(0\) to \(\alpha\). One direct verification is to set \(r=(p-2)/2\), \(z=t^2\), and note that the numerator controlling \(f_p'(t)\) is
\[
1-(p-1)(1-z)z^r-z^{p-1}.
\]
The complementary quantity
\[
h(z)=(p-1)(1-z)z^r+z^{p-1}
\]
has derivative
\[
h'(z)=(p-1)z^{r-1}\bigl(r-(r+1)z+z^{r+1}\bigr)>0
\]
for \(0<z<1\), because the parenthesis decreases to \(0\) at \(z=1\). Hence \(h(z)<1\).

Now define
\[
G_p(s)=\frac{1-s^{p-1}}{(1-s)(1+s^p)^\alpha}.
\]
The same inequality gives
\[
\frac{G_p'(s)}{G_p(s)}=
\frac{1-(p-1)(1-s^2)s^{p-2}-s^{2p-2}}
{(1-s)(1-s^{p-1})(1+s^p)}>0.
\]
Moreover, \(G_p(0)=1\) and
\[
\lim_{s\uparrow1}G_p(s)=\frac{p-1}{2^\alpha}>2^\alpha.
\]
The last strict inequality is equivalent to
\[
\frac{1+\alpha}{1-\alpha}>2^{2\alpha},
\]
whose logarithm has positive derivative on \(0,1)\). Therefore there is a unique \(s_p\in(0,1)\) with \(G_p(s_p)=2^\alpha\).

Set \(s=s_p\) and \(\rho=\rho_p=-f_p(s)\). At this critical point,
\[
1+s^2+2\rho s
=\frac{(1-s^2)(1+s^p)}{1-s^p},
\]
so the same-sign quadrant maximum is
\[
M_+(\rho)=\frac{1-s^p}{(1-s^2)(1+s^p)^\alpha}.
\]
We also need the lower endpoint in that quadrant. The root lies in the regime \(1+\rho>2^{-\alpha}\). To verify this without approximation, use the elementary inequality, valid for \(0<a<1\) and \(0<z<1\),
\[
\frac{1-z^{1+a}}{1-z}>(1+z)^a.
\]
Indeed, after logarithmic differentiation its numerator is
\[
(1-a)(1-z^{a+1})-(1+a)(z^a-z),
\]
which decreases to \(0\) at \(z=1\); the sign of its derivative follows from the weighted AM–GM inequality
\[
a+(1-a)z\ge z^{1-a}.
\]
Apply this with \(a=\alpha\) and \(z=s^p\), and use the defining equation for \(s\). It follows that
\[
R_{p,\rho}(1)=\frac{2^{-\alpha}}{1+\rho}<1,
\]
so this diagonal value is the same-sign minimum.

Radon reciprocity now turns that minimum into the opposite-sign maximum:
\[
M_-(\rho)
=\frac1{(1-\rho^2)R_{p,\rho}(1)}
=\frac{2^\alpha}{1-\rho}.
\]
The equation \(G_p(s)=2^\alpha\) is exactly the balancing condition
\[
M_+(\rho)=M_-(\rho).
\]
Thus the two quadrant maxima equioscillate at \(\rho=\rho_p\).

It remains to check that this balance is globally optimal, rather than merely stationary. For \(\rho>\rho_p\) up to \(0\), the opposite-sign maximum dominates, so the squared distortion is
\[
2^{2\alpha}\frac{1+\rho}{1-\rho},
\]
which strictly increases with \(\rho\). For \(-\alpha<\rho<\rho_p\), the same-sign interior maximum dominates. If \(s=f_p^{-1}(-\rho)\) and \(u=s^{p-2}\), the envelope derivative is
\[
\frac{d}{d\rho}\log\bigl(M_+(\rho)^2(1-\rho^2)\bigr)
=-\frac{2s(1+u)(1-s^2u)^2}
{(1-s^2)(1-s^2u^2)(1+s^2u)}<0.
\]
Hence moving \(\rho\) upward toward \(\rho_p\) strictly decreases the distortion on that branch. For \(\rho\ge0\), the two diagonal directions already give a distortion at least \(2^{2\alpha}\), larger than the balanced value. For \(\rho\le-\alpha\), \(R_{p,\rho}\) is increasing on \([0,1]\), and the lower bound \(R_{p,\rho}(1)^2(1-\rho^2)\) grows as \(\rho\) moves left from \(-\alpha\); continuity with the preceding branch again puts it above the balanced value. This proves global optimality.

Finally,
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2
=2^{2\alpha}\frac{1+\rho_p}{1-\rho_p}.
\]
Substituting the expression for \(\rho_p\) gives the displayed formula in \(s_p\). For \(p=4\), the root equation reduces to
\[
s^4-2s^3-3s^2-2s+1=0,
\]
so \(s+s^{-1}=1+\sqrt6\), \(\rho_4=-1/(1+\sqrt6)\), and the squared distance simplifies to \(6-2\sqrt6\).

## Verification
The proof is analytic; finite computation is not used to establish the quantified statement. As sanity checks, direct numerical minimization of the two directional ratio functions at \(p=2.1,2.5,3,4,6,10\) agreed with the formula to displayed floating-point precision. The special case \(p=3\) gives \(s_3=2-\sqrt3\), \(\rho_3=-1/5\), and
\[
d_{\mathrm{BM}}(X_3,\ell_2^2)^2=\frac{2^{5/3}}3,
\]
matching the independently recorded exact special case. The \(p=4\) radical simplification above provides a second symbolic check.

The critical proof dependencies independently checked here are: the symmetry reduction to quadratic forms with equal diagonal entries; determinant/Hölder verification that the conjugate Day–James norm equals its antinorm; the reciprocal extremum identity \(m_\rho M_\rho=(1-\rho^2)^{-1}\); strict monotonicity of \(f_p\) and \(G_p\); and the branch derivative giving global minimization.

## Relationship to prior work
Martini and Swanepoel give the antinorm formalism and state that the conjugate mixed \(\ell_p\)-\(\ell_q\) norm is a Radon norm. Alonso records the Day–James family and its generalized representation of normed planes. Those sources supply the natural object and duality structure, but the inspected text does not state the Euclidean Banach–Mazur distance of this one-parameter conjugate family or the balance equation above.

A previously recorded exact \(p=3\) special case is contained in the present theorem. It does not imply the all-\(p\) formula: the new content is the one-parameter minimization, uniqueness of \(s_p\), the optimal ellipse for every \(p>2\), and the closed \(p=4\) consequence. Searches for aliases involving Radon planes, mixed/conjugate Day–James norms, Euclidean distortion, distance ellipsoids, and Banach–Mazur distance did not reveal a statement with equivalent coverage.

## Limitations
No claim is made for nonconjugate exponent pairs, for complex scalars, or for higher-dimensional mixed-quadrant constructions. The theorem gives \(s_p\) implicitly for general \(p\); only special exponents need simplify algebraically. The literature comparison cannot exclude an unindexed historical equivalent formulation, especially in older convex-geometry work on distance ellipsoids, so that remains a residual originality risk.

## References
1. H. Martini and K. J. Swanepoel, “Antinorms and Radon curves,” arXiv:math/0409200, first submitted 13 September 2004; later Aequationes Mathematicae 72 (2006), 110–138.
2. J. Alonso, “Any two-dimensional Normed space is a generalized Day-James space,” Journal of Inequalities and Applications 2011, article 2, published 15 June 2011, DOI 10.1186/1029-242X-2011-2.
3. A. Defant and C. Michels, “Norms of tensor product identities,” Note di Matematica 25 (2005/2006), 129–166, DOI 10.1285/i15900932v25n1p129. The inspected Banach–Mazur formula for spaces with enough orthogonal symmetries does not cover the mixed Day–James plane for \(p\ne2\).
