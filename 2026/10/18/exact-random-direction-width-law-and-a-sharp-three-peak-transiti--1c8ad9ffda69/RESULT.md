# Exact random-direction width law and a sharp three-peak transition for Euclidean kites

## Finding
Let \(Q\) be any nondegenerate Euclidean kite, let \(\Theta\) be uniform on unoriented line directions, and let \(W_Q(\Theta)\) be the length of its orthogonal projection. After a similarity and a possible reflection, write
\[
Q=Q_{a,b}=\operatorname{conv}\{(0,-a),(1,0),(0,b),(-1,0)\},\qquad 0<a\le b.
\]
The complete cumulative distribution function of \(W_Q\), at every real threshold, is given below by elementary inverse trigonometric functions. In addition, its directional-width profile has **three strict local maxima on the compact symmetry-reduced direction interval** precisely in the open phase
\[
b>1\quad\text{and}\quad ab<1;
\]
otherwise it has only its two endpoint maxima. In the three-maximum phase, the extra maximum at \(\theta_*=\arctan b\) has value \(M=\sqrt{1+b^2}\) and contributes an explicit inverse-square-root density peak. The exact transition conditions apply to every strictly convex kite, including limits on the phase boundaries.

## Assumptions and scope
For \(0<a\le b\), introduce
\[
p=\arctan(1/b),\quad q=\arctan(1/a),\quad M=\sqrt{1+b^2},\quad s=a+b,
\]
where \(0<p\le q<\pi/2\). For \(u\le v\), set
\[
\operatorname{clip}(z;u,v)=\max\{u,\min\{z,v\}\}.
\]
The formulas that follow apply to \(t\ge0\). Set \(F_{a,b}(t)=0\) for \(t<0\), and define
\[
\alpha(t)=\arccos\!\left(\min\{1,t/2\}\right),\qquad
\beta(t)=\arcsin\!\left(\min\{1,t/s\}\right).
\]
Set
\[
A_1(t)=\operatorname{clip}(p-\alpha(t);0,p),\qquad
A_3(t)=\operatorname{clip}(\beta(t)-q;0,\pi/2-q).
\]
Define \(A_2(t)=q-p\) when \(t\ge M\). When \(0\le t<M\), put \(\phi(t)=\arcsin(t/M)\), \(\ell=2p\), and \(h=p+q\), and define
\[
A_2(t)=\max\{0,\min\{h,\phi(t)\}-\ell\}
+\max\{0,h-\max\{\ell,\pi-\phi(t)\}\}.
\]
**The exact law** is
\[
\boxed{F_{a,b}(t)=\mathbb P(W_Q(\Theta)\le t)=\frac2\pi\bigl(A_1(t)+A_2(t)+A_3(t)\bigr).}
\]
It is valid without generic-position assumptions, including \(a=b\), \(b=1\), and \(ab=1\).

The support interval is exactly \([m,H]\), where
\[
m=\min\!\left\{\frac{2b}{\sqrt{1+b^2}},\frac{a+b}{\sqrt{1+a^2}}\right\},
\]
and \(H=\max\{2,s,M\}\) in the open three-maximum phase, while \(H=\max\{2,s\}\) otherwise. The mean-width consistency identity is
\[
\mathbb E[W_Q]=\frac2\pi\left(\sqrt{1+a^2}+\sqrt{1+b^2}\right).
\]

## Proof
**Reduction to one quadrant.** Width is invariant under reversal of direction, and reflection of the kite in its vertical symmetry axis sends an angle \(\theta\) to \(\pi-\theta\). Thus its width distribution under a uniform angle on \([0,\pi)\) equals that of an angle uniform on \([0,\pi/2]\), with density \(2/\pi\). For \(0\le\theta\le\pi/2\), the four vertex projections onto \((\cos\theta,\sin\theta)\) are
\[
-a\sin\theta,\quad\cos\theta,\quad b\sin\theta,\quad-\cos\theta.
\]
Hence, exactly,
\[
W(\theta)=\max\{\cos\theta,a\sin\theta\}
+\max\{\cos\theta,b\sin\theta\}.
\]
Since \(p\le q\), the switch angles are \(p\) and \(q\), giving the exact three-branch formula
\[
W(\theta)=\begin{cases}
2\cos\theta,&0\le\theta\le p,\\
\cos\theta+b\sin\theta=M\sin(\theta+p),&p\le\theta\le q,\\
s\sin\theta,&q\le\theta\le\pi/2.
\end{cases}
\]
The branches agree at both junctions, and the middle branch is absent when \(p=q\).

**The distribution.** For \(t\ge0\), the first branch satisfies \(2\cos\theta\le t\) precisely when \(\theta\ge\alpha(t)\); intersecting with \([0,p]\) gives angular measure \(A_1(t)\). The final branch satisfies \(s\sin\theta\le t\) precisely when \(\theta\le\beta(t)\); intersecting with \([q,\pi/2]\) gives \(A_3(t)\). On the middle branch let \(y=\theta+p\in[2p,p+q]=[\ell,h]\subset(0,\pi)\). If \(t\ge M\) every such direction qualifies. For \(0\le t<M\), the inequality \(M\sin y\le t\) is equivalent to
\[
y\in[0,\phi(t)]\cup[\pi-\phi(t),\pi].
\]
The two intersection lengths with \([\ell,h]\) are exactly the two terms in \(A_2(t)\). Summing and multiplying by the reduced angular density \(2/\pi\) proves the CDF formula. This derivation also proves all boundary cases by continuity; the inversion splits only a measure-zero set when \(t=M\).

**Extrema and sharp phase boundary.** On the first interval \(W\) decreases strictly; on the last it increases strictly. On the middle interval the derivative is \(M\cos(\theta+p)\), strictly decreasing through at most one zero, at \(\theta_*=\pi/2-p=\arctan b\). Its zero is strictly interior precisely when \(\theta_*>p\) and \(\theta_*<q\). Since arctangent is increasing, these are precisely \(b>1\) and \(ab<1\), respectively. In that phase the middle interval rises and then falls; its adjoining switch points are strict local minima and the stationary point is a strict local maximum. Otherwise there is no third strict local maximum, including when the middle branch degenerates. This also shows that the global minimum is at \(p\) or \(q\), with values displayed in \(m\), and that the global maximum is one of the two endpoints or the possible interior critical value, yielding the asserted \(H\).

**Density singularity.** In the open three-maximum phase,
\[
W(\theta)=M-\frac M2(\theta-\theta_*)^2+O((\theta-\theta_*)^4).
\]
For levels \(t\uparrow M\), two nearby inverse images contribute to the density. The corresponding **additional local contribution** is
\[
\boxed{f_{\mathrm{middle,peak}}(t)\sim\frac2\pi\sqrt{\frac2M}\,(M-t)^{-1/2}.}
\]
If another branch has a singularity at the same numerical level (for example, if \(M=2\) or \(M=s\)), its coefficient adds; the formula above deliberately describes the middle-branch contribution, not necessarily the full density. Exactly on either boundary \(b=1\) with \(a<1\), or \(ab=1\) with \(b>1\), only one middle-side inverse image remains, giving half of this coefficient. When \(a=b=1\), the middle interval is empty and contributes none. These limiting cases distinguish a one-sided singularity at a switch from a genuine interior third maximum.

Finally, Cauchy's planar perimeter formula gives \(\mathbb E W=\operatorname{per}(Q)/\pi\); the perimeter here is \(2(\sqrt{1+a^2}+\sqrt{1+b^2})\), proving the mean identity.

## Verification
The accompanying standard-library `checker.py` independently computes each width directly from the four vertex projections, rather than by using the three-branch formula. It numerically compares the predicted CDF with midpoint-angle quadrature for 70 kite shapes and 51 thresholds per shape, sampling 12,000 angles per shape. It additionally checks the mean-width identity and critical-angle phase criterion. The observed largest CDF discrepancy was below \(10^{-4}\), consistent with deterministic angular discretization. The all-parameter theorem relies on the exact proof above, not the finite tests.

## Relationship to prior work
Akiyama and Kamae (2022), *Width deviation of convex polygons* (arXiv:2201.06736, original public date 2022-01-18), develop mean and variance methods for random directional width, and in Section 7 give a numerically distinguished asymmetric kite with \(a\approx0.2421333\), \(b\approx1.675026\). Their results concern the first two moments and polygonal width-deviation extremization; the present claim gives the full law across every kite and its sharp change in critical-point multiplicity. In particular their displayed kite lies in the open three-maximum phase. For the reported values, its distinct local-maximum levels are approximately \(1.9171592980\), \(1.9508234187\), and \(2\), so its angular-width density has three separately located inverse-square-root peaks. The minimum width in the same normalization is approximately \(1.7172502208\).

Martirosyan (2023), *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, determines chord-length distributions for **random translated lines conditional on a fixed orientation**, and related covariogram data, for arbitrary quadrilaterals. That is a different random experiment from the pushforward of uniform **orientation** through orthogonal projection width; no all-kite angular width CDF or three-maxima classification was located in its full available article. Other published or indexed exact random-direction width laws for particular bodies (for example, triangles, parallelotopes, cubes, or octahedra) do not imply this two-parameter kite formula by a stated specialization.

## Limitations
The width random variable uses uniform **unoriented directions**, not random chords and not random points in the kite. The formula characterizes kites, not arbitrary nonsymmetric convex quadrilaterals. Inverse-square-root coefficients refer to identifiable local branches of the density; when critical values coincide, all contributing branch coefficients must be added. Bibliographic noncoverage is based on accessible primary literature and targeted similarity searches, not a proof that an unindexed equivalent calculation cannot exist. Independent mathematical validation has not been conducted.

## References
1. S. Akiyama and T. Kamae, *Width deviation of convex polygons*, arXiv:2201.06736, first submitted 18 January 2022; https://arxiv.org/html/2201.06736v1 ; https://arxiv.org/abs/2201.06736 .
2. D. M. Martirosyan, *Orientation-Dependent Chord Length Distribution in a Convex Quadrilateral*, Journal of Contemporary Mathematical Analysis 58 (2023), 416–430; https://doi.org/10.3103/S1068362323060055 .
