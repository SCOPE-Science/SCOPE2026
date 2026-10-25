# Two visibility transitions and a critical hole-area tail for torus shadows

## Finding
Fix a solid circular ring torus of major radius \(R>0\) and tube radius \(0<r<R\), formed as the Euclidean distance-\(r\) neighborhood of a circle. Let \(u\) be a uniformly oriented viewing axis and set \(c=|u_z|\), \(s=r/R\). Orthographic projection onto \(u^\perp\) has the following three, **exhaustive** regimes, apart from their zero-probability equality boundaries:

1. If \(\sqrt{s}<c\le1\), the shadow is an embedded two-sided radius-\(r\) planar tube about an ellipse and contains a bounded central hole. Its area is exactly \(2rP(R,Rc)\), where \(P(a,b)\) denotes the perimeter of the ellipse with semiaxes \(a,b\).
2. If \(s<c<\sqrt{s}\), the hole persists, but the planar normal-coordinate tube map has self-overlap; the actual shadow area is **strictly less** than \(2rP(R,Rc)\).
3. If \(0\le c\le s\), the shadow is simply connected (at equality the hole collapses to a point); its area is again strictly below \(2rP(R,Rc)\). The ellipse at \(c=0\) is interpreted as a doubled segment with perimeter limit \(4R\).

Consequently, under Haar-uniform viewing axes, the respective probabilities are
\[
1-\sqrt{s},\qquad \sqrt{s}-s,\qquad s.
\]
The annular-but-normal-overlapping regime has maximum probability \(1/4\), attained uniquely for \(r/R=1/4\).

Let \(H(c)\) denote the area of the central hole, defined as zero for \(c\le s\). Then
\[
H(c)\sim R^2 C_s(c-s)^{3/2},\qquad
C_s=\frac83\sqrt{\frac{2(1-s^2)}s},\quad c\downarrow s.
\]
In particular, the random hole-area law has an atom of size \(s\) at zero and the sharp continuous onset
\[
\lim_{h\downarrow0}
\frac{\Pr\{0<H(c)\le h\}}{(h/R^2)^{2/3}}=C_s^{-2/3}.
\]

## Assumptions and scope
The torus is the *solid* set \(T_{R,r}=\{x\in\mathbb R^3:\operatorname{dist}(x,\{(R\cos t,R\sin t,0)\})\le r\}\); the observer uses parallel orthographic rays, and the shadow is the set-theoretic planar projection, with overlapping rays counted only once. All assertions hold for each fixed \(R>r>0\). Degenerate planar ellipse at \(c=0\) is interpreted by continuity. The critical tail is for fixed \(s\in(0,1)\), not uniform as \(s\to0\) or \(s\to1\).

## Proof
**Projection and hole.** Orthogonal projection commutes with Minkowski addition. The core circle projects to the boundary \(\Gamma_c\) of an ellipse \(E_c\) with semiaxes \(a=R\) and \(b=Rc\); the projected ball is the radius-\(r\) planar disk \(B_r\). Hence the shadow is exactly \(\Gamma_c+B_r\). For \(c>0\), letting \(E_{c,-r}=\{x\in E_c:\operatorname{dist}(x,\partial E_c)\ge r\}\), we obtain up to area-null boundaries
\[
\Gamma_c+B_r=(E_c+B_r)\setminus\operatorname{int}(E_{c,-r}),
\qquad
S(c)=\pi ab+rP(a,b)+\pi r^2-\operatorname{area}(E_{c,-r}).
\]
The first equality follows by separating points inside from points outside the convex ellipse. Its inradius is \(b\), attained only at the center when \(a>b\). Thus the hole is nonempty precisely for \(b>r\), i.e. \(c>s\), with a point collapse at equality.

**The earlier focal threshold.** Parameterize a planar smooth convex curve by arclength and inward unit normal; the normal-map Jacobian at distance \(t\) is \(1-t\kappa\). The ellipse has curvature radius
\[
\rho(\tau)=\frac{(a^2\sin^2\tau+b^2\cos^2\tau)^{3/2}}{ab},\qquad
\rho_{\min}=\frac{b^2}{a}.
\]
For \(0<r\le\rho_{\min}\), its two-sided normal tube is injective in the interior, and integrating the Jacobian over distances \((-r,r)\) gives \(S(c)=2rP(a,b)\) exactly. For \(\rho_{\min}<r<b\), a nonempty open arc of boundary normals has focal points before distance \(r\); in particular the inner erosion no longer satisfies the quadratic inward Steiner area expression. The following inequality proves the strict area gap without relying on pictures. If \(K_t=K\ominus t B\), then \(K_t+tB\subset K\); monotonicity of planar convex perimeter and the Minkowski perimeter formula give \(P(K_t)\le P(K)-2\pi t\). Coarea for inner parallel sets yields
\[
\operatorname{area}(K_r)=\operatorname{area}(K)-\int_0^rP(K_t)\,dt
\ge \operatorname{area}(K)-rP(K)+\pi r^2.
\]
For a noncircular ellipse and \(r>\rho_{\min}\), \(E_r+rB\subsetneq E\) with positive width difference (the high-curvature tips cannot be recovered by radius-\(r\) rolling disks), so perimeter monotonicity is strict on a nonempty interval of \(t\), making the area inequality strict. Substitution in the displayed shadow area proves \(S(c)<2rP(a,b)\). The focal condition \(r>b^2/a=Rc^2\) is exactly \(c<\sqrt{s}\).

If \(r\ge b\), the erosion has zero area. For noncircular ellipses \(P(a,b)>\pi(a+b)\), since the integrand \(\sqrt{a^2\sin^2 t+b^2\cos^2 t}\) strictly exceeds \(a\sin^2t+b\cos^2t\) on a positive-measure set. Therefore, using \(b\le r<a\),
\[
\pi ab-rP+\pi r^2
=\pi(a-r)(b-r)-r\{P-\pi(a+b)\}<0.
\]
Again \(S(c)<2rP\). At \(c=0\), direct projection yields a stadium of area \(4Rr+\pi r^2<8Rr\).

**Haar probabilities.** For uniformly distributed \(u\in S^2\), \(c=|u_z|\) is uniform on \([0,1]\); the lengths of the three intervals yield the stated probabilities. The strictly concave function \(\sqrt{s}-s\) has its unique maximum at \(s=1/4\).

**Critical hole-area law.** Write \(\delta=b-r\downarrow0\), with \(a=R\) fixed. Near the upper minor-axis vertex, write the ellipse as \(y=f(x)=b\sqrt{1-x^2/a^2}\). Its inward distance-\(r\) offset has coordinates
\[
X=x+\frac{rf'(x)}{\sqrt{1+f'(x)^2}},\qquad
Y=f(x)-\frac{r}{\sqrt{1+f'(x)^2}}.
\]
As \(x\to0\), \(X=(1-rb/a^2)x+O(x^3)\); using \(b\to r<a\) and inverting,
\[
Y=\delta-\frac{r}{2(a^2-r^2)}X^2+O(\delta X^2+X^4).
\]
The eroded ellipses shrink to the unique incenter, and their boundary in this scaling is precisely this upper offset and its lower reflection. Thus \(|X|\le\sqrt{2(a^2-r^2)\delta/r}\,[1+o(1)]\) and integration between upper and lower graphs yields
\[
\operatorname{area}(E_{c,-r})
\sim \frac83\sqrt{\frac{2(a^2-r^2)}r}\,\delta^{3/2}.
\]
Since \(\delta=R(c-s)\), this is the claimed \(R^2C_s(c-s)^{3/2}\). The hole area is strictly increasing with \(c\) because the ellipses are strictly nested and their inner erosions strictly expand after becoming nonempty. Inverting the local asymptotic and using the uniform distribution of \(c\) gives the \(2/3\)-exponent probability law.

## Verification
Run `python verify_torus_shadow.py` with Python, NumPy and Shapely 2.x. This script independently approximates ellipses by 12,000-vertex polygons, forms their Minkowski dilation and erosion through planar polygon buffering, and checks the three regimes for three aspect ratios, the \(3/2\) area law near hole extinction, probability normalization, and the exact maximum. See VERIFICATION.md for the executed output. The universal proof above does **not** depend on discretization or numerical sampling.

## Relationship to prior work
Slepian's *Average Projected Area Theorem* (2011, arXiv:1109.0595) covers projected area for **convex** solids and motivates the nonconvex shadow-obscuration question. Egan's *Average Shadows* (2021–2022) explicitly discusses torus multiple ray crossings but does not give the torus's three viewing regimes or the closing-hole distribution. Schwartz's (2021) parallel-ellipse discussion gives the outer-offset area term, but not the inward erosion/two-threshold behavior. Standard rolling-radius and Steiner facts are used as premises rather than claimed as new. A separate study of average numbers of ellipse normals concerns different observables; its indexed summary has not been treated as full-text verification. Direct targeted source and record searches found no result implying the stated joint phase diagram and \(2/3\) hole-area law, though absence of matches does not prove priority.

## Limitations
The result covers solid *circular* ring tori and orthographic shadows; it does not analyze perspective imaging, elliptical torus cores, noncircular cross-sections, ray transparency, or a closed elementary formula for shadow area throughout the intermediate regime. Neither the finite computations nor source searches constitute an independent mathematical audit or exhaustive historical-priority certification.

## References
- Z. Slepian, *The Average Projected Area Theorem – Generalization to Higher Dimensions*, arXiv:1109.0595, first posted 2011-09-03, https://arxiv.org/abs/1109.0595.
- G. Egan, *Average Shadows*, section “Non-convex solids,” 2021–2022, https://www.gregegan.net/SCIENCE/AverageShadows/AverageShadows.html.
- J. Schwartz, *An ellipse's parallel curve: length, area, and torus volume*, 2021-04-06, https://jaschwartz.net/journal/parallel-ellipse-torus.html.
