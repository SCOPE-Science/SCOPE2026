# Exact area profile and two-endpoint asymptotics of ball illumination of a disk

## Finding

Fix \(0<r<R\), write \(a=R-r\), and let \(K=B_r(0)\subset\mathbb R^2\). For a compact set \(E\) contained in a radius-\(R\) disk, define its \(R\)-ball convex hull as the intersection of every closed radius-\(R\) disk containing \(E\). Put \(H_s=[K,(s,0)]_R\) for \(r\le s\le 2R-r\), and \(\Delta(s)=\operatorname{area}(H_s)-\pi r^2\).

For each \(0\le\alpha\le\pi\), define
\[
\beta(\alpha)=\arcsin\!\left(\frac aR\sin\alpha\right),\qquad
s(\alpha)=R\cos\beta(\alpha)-a\cos\alpha.
\]
The map \(s(\alpha)\) increases strictly from \(r\) to \(2R-r\), and the **exact global area cost** is
\[
\boxed{\Delta(s(\alpha))=R^2(\alpha-\beta)-Ra\sin(\alpha-\beta)-r^2\alpha.}
\]
It increases strictly from \(0\) to \(\delta_*=\pi(R^2-r^2)\). Thus, for every \(0\le\delta\le\delta_*\), the unweighted \(R\)-ball illumination body
\[
I_R^\delta(K)=\{x:\operatorname{area}([K,x]_R\setminus K)\le\delta\}
\]
is exactly the concentric disk \(B_{s_\delta}(0)\), where \(s_\delta\) is the unique solution of \(\Delta(s_\delta)=\delta\), with radius \(s_0=r\) and \(s_{\delta_*}=2R-r\). Points not contained with \(K\) in any radius-\(R\) disk are excluded from the illumination body.

The next correction after the known leading relative-affine-area law is explicit. As \(\delta\downarrow0\),
\[
\operatorname{area}(I_R^\delta(K))-\pi r^2
=A_1\delta^{2/3}+A_2\delta^{4/3}+O_{r,R}(\delta^2),
\]
where
\[
A_1=\pi3^{2/3}r^{2/3}\left(\frac{R-r}{R}\right)^{1/3},
\quad
A_2=\frac{\pi3^{4/3}(8R^2-12Rr+3r^2)}{20R(R-r)}
\left(\frac{R-r}{rR}\right)^{2/3}.
\]
The second coefficient changes sign at the **unique ratio in \((0,1)\)**
\[
\boxed{\frac rR=2-\frac{2\sqrt3}{3}.}
\]
It is positive below that ratio, zero at it, and negative above it.

At the opposite endpoint, put \(s_*=2R-r\). Then
\[
\delta_*-\Delta(s)\sim C_*\sqrt{s_*-s},\qquad
C_*=4R\sqrt{\frac{2R(R-r)}{2R-r}},
\]
and consequently
\[
\boxed{\pi s_*^2-\operatorname{area}(I_R^\delta(K))
\sim \frac{\pi(2R-r)^2}{16R^3(R-r)}(\delta_*-\delta)^2}
\quad(\delta\uparrow\delta_*).
\]
The \(2/3\) onset and quadratic terminal saturation are two distinct sharp scaling regimes of the same exact curve.

## Assumptions and scope

All disks are closed Euclidean disks in the plane. Their radii satisfy \(0<r<R<\infty\). The illumination parameter satisfies \(0\le\delta\le\delta_*\); no statement concerns ordinary convex illumination, weighted illumination, higher dimensions, or the degenerate parameter \(r=R\). The exact curve uses \(s\) in the full feasible interval \([r,2R-r]\). Outside that interval the specified exterior point cannot be accommodated with \(K\) inside any radius-\(R\) disk.

## Proof

**1. Centers and tangency geometry.** A radius-\(R\) disk with center \(c\) contains \(K\) exactly when \(\|c\|\le a\). It also contains \(x_s=(s,0)\) exactly when \(\|c-x_s\|\le R\). Thus the permissible center set is \(\mathcal C_s=B_a(0)\cap B_R(x_s)\). For \(r<s<2R-r\), the two center-circle intersection points are
\[
c_\pm=(-a\cos\alpha,\ \pm a\sin\alpha),\qquad
\cos\alpha=\frac{R^2-a^2-s^2}{2as}.
\]
The upper tangency point of \(K\) is \(T_+=(r\cos\alpha,r\sin\alpha)\), touching the radius-\(R\) disk centered at \(c_-\). The lower point \(T_-\) analogously touches the disk centered at \(c_+\). The polar argument of \(x_s-c_-\) is \(\beta\): the vertical and horizontal components yield \(R\sin\beta=a\sin\alpha\) and \(s=R\cos\beta-a\cos\alpha\). In particular \(0<\beta<\alpha<\pi\).

**2. Exact hull boundary.** The upper shorter radius-\(R\) circular arc from \(x_s\) to \(T_+\), centered at \(c_-\), belongs to the \(R\)-spindle of its endpoints. Every disk containing \(K\cup\{x_s\}\) contains this spindle, so the arc belongs to \(H_s\); because \(B_R(c_-)\) is one of the defining disks, the arc lies on \(\partial H_s\). The reflected lower arc has the same property. For every \(\theta\in[\alpha,2\pi-\alpha]\), the disk centered at \(-a(\cos\theta,\sin\theta)\) contains both \(K\) and \(x_s\) (the squared distance to the latter is \(s^2+a^2+2as\cos\theta\le R^2\)); its boundary touches \(K\) at \(r(\cos\theta,\sin\theta)\). Thus the remainder of the original circle is also on \(\partial H_s\). These three arcs join into a simple closed curve, entirely on the boundary of the convex disk-intersection \(H_s\), hence constitute its entire boundary.

**3. Area and strict monotonicity.** Applying \(\frac12\oint(x\,dy-y\,dx)\) to these three arcs gives the two equal upper/lower circular-arc contributions \(R^2(\alpha-\beta)-Ra\sin(\alpha-\beta)\), and the remaining original-circle contribution \(r^2(\pi-\alpha)\). Subtracting \(\pi r^2\) proves the boxed formula. Since \(\beta'=a\cos\alpha/(R\cos\beta)\), differentiation yields
\[
\frac{ds}{d\alpha}=\frac{a\sin(\alpha-\beta)}{\cos\beta}>0.
\]
For fixed \(\|c\|\le a<R\), the condition \(\|c-x_s\|\le R\) is equivalent to
\(c_1\ge(s^2+\|c\|^2-R^2)/(2s)\), whose right side increases strictly with \(s>0\). Thus \(\mathcal C_s\) decreases, so \(H_s\) increases by inclusion. The disk centered at \((s-R,0)\) is feasible and bounds \(H_s\) by the support line \(x_1\le s\). Since \(H_{s'}\) contains \((s',0)\) for \(s'>s\), strict convex-body inclusion implies a strict area increase. The endpoint center sets are, respectively, \(B_a(0)\) and the singleton \(\{(a,0)\}\), giving \(H_r=K\) and \(H_{2R-r}=B_R((a,0))\). Rotational symmetry proves the illumination-body statement.

**4. Small-parameter expansion.** Put \(k=a/R\) and \(t=\alpha\). Expanding \(\beta=\arcsin(k\sin t)\) gives
\[
\frac{s-r}{R}=\frac{k(1-k)}2t^2+
\frac{k(1-k)(3k^2+3k-1)}{24}t^4+O(t^6),
\]
\[
\frac{\Delta}{R^2}=\frac{k(1-k)^2}{3}t^3+
\frac{k(1-k)^2(3k^2+6k-1)}{60}t^5+O(t^7).
\]
Hence, with \(h=s-r\),
\[
\Delta=C h^{3/2}\left(1+Lh+O(h^2)\right),\quad
C=\frac{2\sqrt2}{3}\sqrt{\frac{rR}{a}},\quad
L=-\frac{3(3R^2-7Rr+3r^2)}{20Rar}.
\]
Put \(w=(\delta/C)^{2/3}\). Series inversion gives \(h=w-\frac23Lw^2+O(w^3)\). Substitution into \(\pi((r+h)^2-r^2)\) yields \(A_1,A_2\). The quadratic polynomial \(8-12(r/R)+3(r/R)^2\) has exactly one root in \((0,1)\), establishing the sign classification.

**5. Terminal expansion.** Write \(t=\pi-\alpha\downarrow0\). Since \(\beta=(a/R)t+O(t^3)\),
\[
s_*-s=\frac{a(R+a)}{2R}t^2+O(t^4),\qquad
\delta_*-\Delta=4Ra\,t+O(t^3).
\]
Eliminating \(t\) gives \(C_*\), then expanding \(\pi(s_*^2-s^2)\) proves the quadratic terminal law.

## Verification

Run `python verify.py` using SymPy and mpmath. The script verifies four exact Taylor coefficients and the inverse-series coefficient symbolically, then independently evaluates the two endpoint regimes for three different radius ratios at high precision. This is a finite algebraic and numerical replay, **not** a substitute for the general geometric boundary argument above. The exact geometry was also stress-tested by independently intersecting sampled admissible radius-\(R\) disks for multiple admissible \((r,s)\); their measured areas agreed with the formula within discretization errors below \(10^{-5}\) at unit scale.

## Relationship to prior work

Oliva, Werner and Yalikun (2026, arXiv:2607.13714, first public 2026-07-15) define the \(R\)-ball illumination construction, prove its convexity and derive a universal leading volume asymptotic. Their planar results include an isoperimetric inequality for relative affine surface area. The coefficient \(A_1\) agrees with that known leading law and is **not claimed as new**. The contribution here is the exact full-parameter disk cost, the second coefficient with its sign transition, and the distinct saturation exponent at the far endpoint.

Schütt, Werner and Yalikun (2025, arXiv:2504.15488) study the inward \(R\)-ball floating construction, not this outward disk profile. Werner and Yalikun (2025, arXiv:2512.19836) study relative \(L_p\) surface measures and weighted floating bodies. Classical planar \(R\)-spindle geometry supplies the two-point arc construction; those elementary geometric facts are not claimed as new. Available mathematical-record summaries concerning local Hessians of relative affine area and hyperbolic illumination disks address different invariants and do not imply the global Euclidean \(R\)-ball curve.

## Limitations

The analysis is restricted to Euclidean disks with strict \(r<R\), and the terminal asymptotic is a fixed-radius statement. The \(r\uparrow R\) limit is singular, so the expansion is not asserted uniformly there. Full coverage of historical spindle-hull formulas is uncertain; an equivalent exact global formula in obscure older literature remains a priority risk. No independent mathematical audit has been performed.

## References

1. B. Oliva, E. M. Werner and D. Yalikun, *Illumination bodies for ball-convex bodies*, arXiv:2607.13714 (2026), first posted 2026-07-15; online full text, Definition 1, Section 2, and proofs.
2. C. Schütt, E. M. Werner and D. Yalikun, *Floating bodies for ball-convex bodies*, arXiv:2504.15488 (2025), online full text.
3. E. M. Werner and D. Yalikun, *Ball-convex bodies and \(L_p\) relative surface areas*, arXiv:2512.19836 (2025), online full text.
4. K. Bezdek, R. Connelly and B. Csikós, *On the perimeter of the intersection of congruent disks* (2006), for standard ball-hull/spindle notation and geometric context.
