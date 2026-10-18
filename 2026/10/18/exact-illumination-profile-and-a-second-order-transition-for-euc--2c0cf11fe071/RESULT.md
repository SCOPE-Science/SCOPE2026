# Exact illumination profile and a second-order transition for Euclidean ball-convex disks

## Finding

For any disk \(K=B_r(0)\subset\mathbb R^2\) with \(0<r<R\), the volume profile of the Euclidean \(R\)-ball convex hull of \(K\) and an external point has a closed elementary expression over its *entire* domain. Consequently its \(R\)-ball illumination body is a concentric disk with a unique sharp threshold for ceasing to be \(R\)-ball convex. Its small-parameter volume excess has an explicit two-term expansion, whose second coefficient changes sign exactly at \(r/R=2-2\sqrt3/3\).

For \(r\le s\le 2R-r\), put \(q=R-r\) and
\[
\beta(s)=\arccos\frac{R^2+q^2-s^2}{2Rq},\qquad
\theta(s)=\arccos\frac{R^2-q^2-s^2}{2sq}.
\]
With \(\operatorname{bh}_R\) denoting the intersection of all closed radius-\(R\) disks containing a set,
\[
F_{R,r}(s):=\left|\operatorname{bh}_R(B_r(0)\cup\{s e_1\})\right|-\pi r^2
=R^2\beta(s)-Rq\sin\beta(s)-r^2\theta(s).
\]
This strictly increases from \(0\) to \(\pi(R^2-r^2)\). An exterior point with \(s>2R-r\) has no containing radius-\(R\) disk together with \(K\).

Define the \(R\)-ball illumination body by
\[
I^R_\delta(K)=\{x:|\operatorname{bh}_R(K\cup\{x\})|-|K|\le\delta\},
\]
where the volume cost is \(+\infty\) if no radius-\(R\) disk contains \(K\cup\{x\}\). For \(0\le\delta\le\pi(R^2-r^2)\),
\[
I^R_\delta(B_r)=B_{F_{R,r}^{-1}(\delta)};
\]
for larger \(\delta\), it is \(B_{2R-r}\). The sharp \(R\)-ball convexity threshold is
\[
\delta_*(R,r)=(R^2+r^2)\arccos\frac{R-r}{2R}
-R(R-r)\sqrt{1-\frac{(R-r)^2}{4R^2}}-\pi r^2:
\quad I^R_\delta(B_r)\text{ is }R\text{-ball convex if and only if }\delta\le\delta_*.
\]

Put \(k=r/R\),
\[
A(k)=\frac{2\sqrt{2k}}{3\sqrt{1-k}},\qquad
\eta=\left(\frac{\delta}{R^2A(k)}\right)^{2/3},\qquad
C(k)=\frac{3k^2-12k+8}{5(1-k)}.
\]
For each fixed \(0<k<1\), as \(\delta\downarrow0\),
\[
\left|I^R_\delta(B_r)\right|-\pi r^2
=\pi R^2\left(2k\eta+C(k)\eta^2+O_k(\eta^3)\right).
\]
In particular the coefficient of \(\delta^{4/3}\) is positive for \(0<k<2-2\sqrt3/3\), zero exactly at the critical ratio, and negative for \(2-2\sqrt3/3<k<1\). This sign statement concerns the correction relative to the leading \(\delta^{2/3}\) term, not the positivity of the total illumination excess.

## Assumptions and scope

All disks are closed Euclidean disks, \(0<r<R\), and the illumination cost uses ordinary planar Lebesgue area and unweighted \(R\)-ball convex hull. The expansion is for each fixed ratio \(k\in(0,1)\) and is not asserted uniformly as \(k\to0\) or \(k\to1\). The threshold statement includes \(\delta=0\), the degeneracies \(s=r\) and \(s=2R-r\), and the saturated range. Reflection and rotation reduce the position of an added point to \(s e_1\), with \(s=\|x\|\).

## Proof

**1. Feasible centers and boundary arcs.** A radius-\(R\) disk centered at \(c\) contains \(B_r(0)\) exactly when \(|c|\le q\). Thus for an exterior point \(s e_1\) its feasible centers form the lens
\[
\mathcal C_s=B_q(0)\cap B_R(s e_1).
\]
This lens is nonempty exactly for \(s\le R+q=2R-r\). For \(r<s<2R-r\), the two intersection points of the boundary circles are \(c_\pm=-q(\cos\theta,\pm\sin\theta)\). The disks centered at these points are tangent to the original disk at \(r(\cos\theta,\pm\sin\theta)\) and meet at \(s e_1\). The angular spans from the respective tangencies to the added point are \(\beta\), as follows from the cosine rule in the triangle of side lengths \(R,q,s\) and the sine rule \(s\sin\theta=R\sin\beta\).

Here is a direct justification that these arcs are the entire hull boundary. The hull is \(H_s=\bigcap_{c\in\mathcal C_s}B_R(c)\), and it lies in \(\{x_1\le s\}\), because \((s-R)e_1\in\mathcal C_s\). For a proposed point \(p=(u,v)\) with \(v\ge0\), reflecting a feasible center across the horizontal axis can only increase its distance to \(p\) if the reflected center has nonpositive second coordinate. On the lower part of the feasible-center circle \(|c-se_1|=R\), write \(c=se_1-R(\cos\alpha,\sin\alpha)\) with \(0\le\alpha\le\alpha_*<\pi/2\). Since \(u\le s\) and \(v\ge0\), the squared distance \(|p-c|^2\) is nondecreasing in \(\alpha\); therefore its maximum is at the lower corner center. On the lower feasible arc of \(|c|=q\), the squared distance is an affine function of \(\cos\alpha,\sin\alpha\); its maximum occurs either at the same corner or at \(c=-q p/|p|\) if that antipodal center is feasible. In the latter case \(|p-c|=|p|+q\), so the condition \(|p-c|\le R\) is equivalent to \(|p|\le r\). Thus outside \(B_r\) the only active constraint is the lower-corner radius-\(R\) disk, for points in the upper half-plane. The lower half-plane is symmetric. This establishes one rear radius-\(r\) arc between contact angles \(\theta\) and \(2\pi-\theta\) and the two radius-\(R\) joining arcs. Endpoint cases follow continuously.

**2. Exact area.** Use Green's formula \(2|H_s|=\oint(x\,dy-y\,dx)\). The rear arc contributes \(r^2(2\pi-2\theta)\). Each joining arc has a circle contribution \(R^2\beta\) and a translation contribution \(-qs\sin\theta\). Therefore
\[
|H_s|=\pi r^2-r^2\theta+R^2\beta-qs\sin\theta,
\]
which becomes the asserted formula by \(s\sin\theta=R\sin\beta\). Nesting \(H_{s_1}\subsetneq H_{s_2}\) for \(r\le s_1<s_2\le2R-r\) follows since \(s_1e_1\) lies between \(re_1\) and \(s_2e_1\), whereas the rightmost point of \(H_{s_1}\) is \(s_1e_1\). Thus the area is continuous and strictly increasing. At \(s=r\), the hull is \(B_r\); at \(s=2R-r\), it is the sole radius-\(R\) disk containing \(B_r\) and the added point, of area \(\pi R^2\).

**3. Illumination disk and exact convexity threshold.** The cost depends only on \(s\), is zero for \(s\le r\), is strictly increasing up to \(2R-r\), and is infinite thereafter. Hence its sublevel sets are the stated concentric disks. A disk of radius \(t\) is an intersection of radius-\(R\) disks exactly when \(t\le R\): for \(t\le R\), \(B_t=\bigcap_{|c|\le R-t}B_R(c)\); for \(t>R\), no radius-\(R\) disk contains it. Put \(s=R\) in the area formula. Here \(\beta=\arccos(q/(2R))\) and \(\theta=\pi-\beta\), giving \(\delta_*\) exactly. In particular \(0<\delta_*<\pi(R^2-r^2)\).

**4. Second-order expansion.** With \(k=r/R\), \(b=\beta\), and \(z=s/R-k\), the cosine rule yields
\[
\frac{s}{R}=\sqrt{k^2+2(1-k)(1-\cos b)}
=k+\frac{1-k}{2k}b^2+\frac{(k-1)(k^2-3k+3)}{24k^3}b^4+O_k(b^6).
\]
Set \(\phi=\arcsin((1-k)\sin b/(s/R))\), so \(\theta=b+\phi\), and the exact normalized area is
\[
\frac{F_{R,r}(s)}{R^2}=(1-k^2)b-(1-k)\sin b-k^2\phi.
\]
Expansion at \(b=0\), including cancellation of the linear terms, gives
\[
\frac{F_{R,r}(s)}{R^2}
=\frac{1-k}{3k}b^3+
\frac{(k-1)(7k^2-18k+12)}{60k^3}b^5+O_k(b^7).
\]
Eliminating \(b\) and writing \(z=(s-r)/R\) gives
\[
\frac{F_{R,r}(r+Rz)}{R^2}
=A(k)z^{3/2}\left[1+\frac{3(3k^2-7k+3)}{20k(k-1)}z+O_k(z^2)\right].
\]
The inverse Puiseux series gives \(z=\eta-\frac23 B(k)\eta^2+O_k(\eta^3)\), where \(B(k)=3(3k^2-7k+3)/(20k(k-1))\). Finally \(|I^R_\delta(B_r)|-\pi r^2=\pi R^2(2kz+z^2)\), giving \(C(k)=1-4k B(k)/3=(3k^2-12k+8)/(5(1-k))\). Its numerator has exactly one root in \((0,1)\), namely \(2-2\sqrt3/3\), proving the sharp sign change.

## Verification

The accompanying self-contained symbolic checker `verify.py` reconstructs the \(b^2,b^4,b^3,b^5\) series coefficients directly with exact symbolic algebra, derives \(A,B,C\), checks the threshold trigonometric identity, and compares the analytic area formula with high-precision numerical values for several dimensions-free radius ratios. It runs under Python with SymPy and mpmath. The global geometric statement follows from the feasible-center arc argument; numerical samples are only supplemental and are not used to infer a continuum statement.

## Relationship to prior work

Oliva, Werner, and Yalikun (arXiv:2607.13714v1, first public 2026-07-15) introduced \(R\)-ball illumination bodies, proved convexity and the qualitative relative-affine-area asymptotic, and discussed examples in which illumination does not preserve \(R\)-ball convexity. The exact full-parameter disk profile, unique nonconvexity threshold in illumination volume, second-order coefficient, and its sign transition are distinct from their stated main results. Schütt, Werner, and Yalikun (arXiv:2504.15488v1) developed the related \(R\)-ball floating-body theory; Werner and Yalikun (arXiv:2512.19836v1) developed relative surface areas. Ordinary illumination on space forms is a different convex-hull operation and does not cover the present \(R\)-ball hull. No older equivalent disk formula was identified in the checked accessible sources; unindexed or inaccessible literature remains a possible overlap risk.

## Limitations

This theorem concerns Euclidean disks in the plane, fixed \(R>r>0\), unweighted illumination, and a second-order asymptotic only for fixed ratios. It does not prove a corresponding formula for arbitrary smooth \(R\)-ball convex bodies, higher dimensions, or the critical double-scaling limits \(r/R\to0,1\). Equality of the critical coefficient to zero does not specify the next nonzero term there. All historical-priority statements are qualified; no independent scientific audit has been performed.

## References

1. B. Oliva, E. M. Werner, D. Yalikun, *Illumination bodies for ball-convex bodies*, arXiv:2607.13714v1, publicly posted 2026-07-15, https://arxiv.org/abs/2607.13714.
2. C. Schütt, E. M. Werner, D. Yalikun, *Floating bodies for ball-convex bodies*, arXiv:2504.15488v1, publicly posted 2025-04-21, https://arxiv.org/abs/2504.15488.
3. E. M. Werner, D. Yalikun, *Ball-convex bodies and \(L_p\) relative surface areas*, arXiv:2512.19836v1, publicly posted 2025-12-22, https://arxiv.org/abs/2512.19836.
4. R. Assouline, F. Besau, E. M. Werner, *Illumination Bodies in Projective Geometries*, arXiv:2605.25122v1, publicly posted 2026-05-24, https://arxiv.org/abs/2605.25122.
