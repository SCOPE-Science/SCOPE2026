# Exact Euclidean distance of the Day--James \(\ell_p-\ell_\infty\) planes above the Hilbert exponent
## Finding
For every real \(2<p<\infty\), let \(X_p\) be the Day--James plane on \(\mathbb R^2\) with
\[
\|(x,y)\|_{X_p}=
\begin{cases}
\bigl(|x|^p+|y|^p\bigr)^{1/p},&xy\ge0,\\
\max\{|x|,|y|\},&xy\le0.
\end{cases}
\]
Put \(\tau_p=2^{-2/p}\). Then
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2=1+\tau_p=1+2^{-2/p}.
\]
An optimal Euclidean pullback is
\[
|(x,y)|_{p,*}^2=(x+y)^2+\tau_p(x-y)^2.
\]
Moreover, the known James-constant formula
\[
J(X_p)=1+2^{-1/p}
\]
therefore satisfies the exact affine identity
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2=1+\bigl(J(X_p)-1\bigr)^2.
\]

Thus the optimal ellipse is anisotropic in the diagonal and anti-diagonal coordinates. As \(p\downarrow2\), the squared distance tends to \(3/2\); as \(p\to\infty\), it tends to \(2\).

## Assumptions and scope
The scalar field is real, the dimension is exactly two, and \(2<p<\infty\). The Day--James norm is the classical quadrant-dependent norm displayed above. The Banach--Mazur distance is taken over all invertible real linear maps, equivalently over all positive-definite quadratic Euclidean pullbacks. No assertion is made here for \(1\le p<2\), for arbitrary Day--James \(\ell_p-\ell_q\) planes, or in higher dimension.

## Proof
Write
\[
U=x+y,\qquad V=x-y.
\]
The coordinate swap \((x,y)\mapsto(y,x)\) is an isometry of \(X_p\). If a positive-definite quadratic form \(Q\) satisfies
\[
m\|w\|_{X_p}^2\le Q(w)\le M\|w\|_{X_p}^2
\]
for all \(w\in\mathbb R^2\), averaging \(Q\) with its coordinate-swapped conjugate preserves the same inequalities. The averaged form has equal diagonal entries and therefore, after a positive scalar rescaling, is
\[
E_t(x,y)^2=U^2+tV^2,\qquad t>0.
\]
Hence the global Banach--Mazur optimization reduces without loss to minimizing the ratio of the largest and smallest values of \(E_t^2/\|\cdot\|_{X_p}^2\).

On the sector \(xy\ge0\), equivalently \(|U|\ge|V|\), put
\[
r=\frac{|V|}{|U|}\in[0,1].
\]
Then
\[
R_p(r;t)=\frac{E_t(x,y)^2}{\|(x,y)\|_{X_p}^2}
=
\frac{4(1+tr^2)}
{\bigl((1+r)^p+(1-r)^p\bigr)^{2/p}}.
\]

On the sector \(xy\le0\), equivalently \(|V|\ge|U|\), put
\[
s=\frac{|U|}{|V|}\in[0,1].
\]
Since
\[
\|(x,y)\|_{X_p}=\frac{|U|+|V|}{2}
\]
there,
\[
R_\infty(s;t)=
\frac{E_t(x,y)^2}{\|(x,y)\|_{X_p}^2}
=
\frac{4(s^2+t)}{(1+s)^2}.
\]

Set
\[
\tau=2^{-2/p}.
\]
Because \(p>2\), one has \(1/2<\tau<1\). On the \(\ell_\infty\) sector,
\[
\frac{\partial}{\partial s}R_\infty(s;\tau)
=
\frac{8(s-\tau)}{(1+s)^3},
\]
so the unique minimum occurs at \(s=\tau\):
\[
m_*=\frac{4\tau}{1+\tau}.
\]
The endpoint values are
\[
R_\infty(0;\tau)=4\tau,\qquad
R_\infty(1;\tau)=1+\tau.
\]
Since \(\tau>1/2\), the maximum on this sector is
\[
M_*=4\tau.
\]

It remains to bound the \(\ell_p\) sector between the same two values. For \(p\ge2\), the sharp two-dimensional norm comparison gives
\[
2^{1/p-1/2}\sqrt{a^2+b^2}
\le
(a^p+b^p)^{1/p}
\le
\sqrt{a^2+b^2}
\]
for \(a,b\ge0\). With \(a=1+r\) and \(b=1-r\), this yields
\[
2^{2/p}(1+r^2)
\le
\bigl((1+r)^p+(1-r)^p\bigr)^{2/p}
\le
2(1+r^2).
\]
Therefore
\[
R_p(r;\tau)
\le
4\tau\frac{1+\tau r^2}{1+r^2}
\le
4\tau=M_*,
\]
and
\[
R_p(r;\tau)
\ge
2\frac{1+\tau r^2}{1+r^2}
\ge
1+\tau.
\]
Finally,
\[
1+\tau-\frac{4\tau}{1+\tau}
=
\frac{(1-\tau)^2}{1+\tau}>0,
\]
so \(R_p(r;\tau)\ge m_*\). Thus the candidate quadratic form has exact squared distortion
\[
\frac{M_*}{m_*}=1+\tau.
\]

To prove global optimality, let \(t>0\). If \(0<t\le1\), the \(\ell_\infty\)-sector function \(R_\infty(s;t)\) has its minimum at \(s=t\), namely
\[
\frac{4t}{1+t}.
\]
At the anti-diagonal it has value \(4t\), while at the diagonal point in the \(\ell_p\) sector,
\[
R_p(0;t)=2^{2-2/p}=4\tau.
\]
Hence every such \(t\) has squared distortion at least
\[
\frac{\max\{4t,4\tau\}}{4t/(1+t)}
\ge1+\tau,
\]
with equality possible only at \(t=\tau\).

If \(t\ge1\), then \(R_\infty(s;t)\) decreases on \([0,1]\), so its endpoint ratio alone is
\[
\frac{4t}{1+t}\ge2>1+\tau.
\]
Thus \(t=\tau\) is the unique optimal parameter among the symmetry-averaged quadratic forms, and the averaging reduction proves
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2=1+2^{-2/p}.
\]

The published James-constant formula for the same family is
\[
J(\ell_p-\ell_\infty)=1+2^{-1/p}.
\]
Substitution gives
\[
d_{\mathrm{BM}}(X_p,\ell_2^2)^2
=
1+\bigl(J(X_p)-1\bigr)^2.
\]

## Verification
The proof treats an arbitrary Euclidean pullback before symmetry averaging, so it does not assume a diagonal or axial ellipse. The two sectors \(|U|\ge|V|\) and \(|V|\ge|U|\) exhaust the plane. On the \(\ell_\infty\) sector the unique critical point is computed explicitly, and on the \(\ell_p\) sector the standard sharp two-coordinate comparison between \(\ell_p\) and \(\ell_2\) gives global upper and lower bounds. The lower-bound argument for arbitrary \(t>0\) is piecewise exhaustive: \(0<t\le1\) and \(t\ge1\).

Numerical consistency checks give
\[
p=3:\qquad d_{\mathrm{BM}}^2=1+2^{-2/3}=1.6299605249\ldots,
\]
and
\[
p=4:\qquad d_{\mathrm{BM}}^2=1+2^{-1/2}=1.7071067811\ldots.
\]
These decimals are checks only and are not used as proof.

## Relationship to prior work
Nilsrakoo and Saejung introduced the relevant generalized Day--James framework and proved the exact James constant
\[
J(\ell_p-\ell_\infty)=1+2^{-1/p}
\]
for \(1\le p\le\infty\). Their inspected full text studies James constants and uniform nonsquareness; it does not state an exact Euclidean Banach--Mazur distance for the full \(p>2\) family.

Alonso's open-access paper defines the classical Day--James \(\ell_p-\ell_q\) spaces explicitly and classifies the subject under MSC 46B20. Its purpose is the representation of arbitrary normed planes as generalized Day--James spaces, not the computation of distance ellipsoids.

The closest exact-distance comparisons located concern isolated Day--James examples, including the \(\ell_2-\ell_1\) plane, the \(\ell_\infty-\ell_1\) endpoint, a conjugate \(\ell_3-\ell_{3/2}\) plane, and a generalized octagonal example. None gives the quantified \(\ell_p-\ell_\infty\) formula for every \(p>2\). The \(p=2\) endpoint is already implied by an earlier exact-distance computation through duality and is intentionally excluded from the present claim.

## Limitations
The theorem is restricted to \(2<p<\infty\). It does not determine the corresponding distance for \(1\le p<2\), where the same two-coordinate estimates no longer order the \(\ell_p\) sector in the required direction. It also does not classify every nonsymmetric optimal quadratic form; the theorem identifies the globally optimal distortion and an optimal symmetry-averaged ellipse.

Searches did not locate the displayed family formula, but absence from indexed sources is not a proof of worldwide novelty. A differently notated older affine-distance computation remains a residual bibliographic risk.

## References
1. W. Nilsrakoo and S. Saejung, “The James constant of normalized norms on \(\mathbb R^2\),” *Journal of Inequalities and Applications* 2006, Article ID 26265, DOI 10.1155/JIA/2006/26265; published 2006-05-04.
2. J. Alonso, “Any two-dimensional Normed space is a generalized Day-James space,” *Journal of Inequalities and Applications* 2011, Article 2, DOI 10.1186/1029-242X-2011-2; published 2011-06-15.
