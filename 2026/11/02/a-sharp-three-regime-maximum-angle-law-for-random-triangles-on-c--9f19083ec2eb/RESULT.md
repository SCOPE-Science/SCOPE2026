# A sharp three-regime maximum-angle law for random triangles on circular arcs

## Finding

Fix an angular length \(L\in(0,2\pi]\). Independently choose three points uniformly by arclength on one circular arc of angular length \(L\). Let \(M_L\) denote the largest interior angle of their Euclidean triangle. The circle's radius and the arc's position do not affect this distribution.

Put \(m_0(L)=\max\{\pi/3,\pi-L/2\}\), and, for a real \(z\), write \(z_+=\max\{z,0\}\). The support of \(M_L\) is exactly \([m_0(L),\pi]\), with endpoints attained only in the topological-support sense. For \(m<m_0(L)\), \(F_L(m)=0\); for \(m\ge\pi\), \(F_L(m)=1\). For \(m_0(L)\le m<\pi\), put \(h=2m\), \(a=2\pi-h\). Then the complete distribution function is

\[
\boxed{F_L(m)=\frac{L^3-3La^2+2a^3-2(L-h)_+^3+(L-2h)_+^3+6(L-a)(a-h)_+^2+2(a-h)_+^3}{L^3}.}
\]

In particular, the probability of an acute triangle is exactly

\[
\boxed{\Pr(M_L<\pi/2)=\begin{cases}0,&0<L\le\pi,\\(L-\pi)^2(4\pi-L)/L^3,&\pi<L\le2\pi.\end{cases}}
\]

It increases strictly in \(L\) on \((\pi,2\pi)\), reaches the classical full-circle value \(1/4\), and turns on quadratically: \(\Pr(M_{\pi+\varepsilon}<\pi/2)\sim3\varepsilon^2/\pi^2\).

The lower tail has a sharp three-regime transition. Set \(\delta=m-m_0(L)\downarrow0\). For every fixed \(L\),

\[
\boxed{F_L(m_0(L)+\delta)\sim\begin{cases}
12\delta^2/L^2,&0<L\le\pi,\\
12(4\pi-3L)\delta^2/L^3,&\pi<L<4\pi/3,\\
64\delta^3/L^3,&L=4\pi/3,\\
108(L-4\pi/3)\delta^2/L^3,&4\pi/3<L\le2\pi.
\end{cases}}
\]

Thus the onset is quadratic except at exactly \(L=4\pi/3\), where it is cubic. This critical angle is the least arc length allowing an equilateral inscribed triangle.

## Assumptions and scope

Uniform sampling means three independent arclength-uniform points from the same fixed (possibly full) arc of a Euclidean circle of positive radius. Angular lengths are in radians; \(0<L\le2\pi\). Points are distinct and the triangle is nondegenerate almost surely. Right-angle events have probability zero. The CDF is given for all real \(m\). The asymptotics keep \(L\) fixed except in the explicitly stated acute onset \(L=\pi+\varepsilon\).

## Proof

Parameterize the arc by angles \(X_1,X_2,X_3\), independently uniform on \([0,L]\), and order them as \(X_{(1)}<X_{(2)}<X_{(3)}\). Define positive consecutive gaps \(u=X_{(2)}-X_{(1)}\), \(v=X_{(3)}-X_{(2)}\), and the complementary circular gap \(w=2\pi-u-v\). The inscribed-angle theorem gives the unordered three interior angles as \(u/2,v/2,w/2\), hence

\[M_L=\tfrac12\max\{u,v,2\pi-u-v\}.\]

The ordered sample density is \(6/L^3\). For each \((u,v)\) satisfying \(u,v>0\) and \(u+v<L\), the first sample can lie on an interval of length \(L-u-v\). Consequently, the joint gap density is exactly \(6(L-u-v)/L^3\). Let \(r=u+v\). At fixed \(r\), the event \(M_L\le m\) requires \(r\ge a=2\pi-2m\), \(u\le h=2m\), and \(r-u\le h\). The allowed length of the \(u\)-interval is

\[\ell_h(r)=r-2(r-h)_++(r-2h)_+.\]

Therefore, for \(m_0(L)\le m<\pi\),

\[\boxed{F_L(m)=\frac6{L^3}\int_{a}^{L}(L-r)\ell_h(r)\,dr}.\]

The interval is nonempty because \(a\le L\), and \(h\ge2\pi/3\), hence \(a\le2h\). Directly integrating the three linear-positive-part terms yields the displayed CDF. In particular, the contribution from \((r-h)_+\) truncated below at \(a\) is proportional to \((L-h)_+^3-3(L-a)(a-h)_+^2-(a-h)_+^3\), which accounts for the lower-bound corrections. No limiting or numerical approximation enters the identity.

Any three nonnegative gaps totaling \(2\pi\) have maximum at least \(2\pi/3\); also \(w\ge2\pi-L\). Thus \(M_L\ge m_0(L)\). For \(L\le4\pi/3\), the triple \((u,v,w)=(L/2,L/2,2\pi-L)\) achieves this lower bound in the closure of the parameter domain. For \(L\ge4\pi/3\), the equal-gap triple \((2\pi/3,2\pi/3,2\pi/3)\) is feasible in that closure. Any nonempty open neighborhood of either feasible configuration has positive probability. Conversely, clustering all sampled points gives values of \(M_L\) arbitrarily close to \(\pi\). This proves the exact support.

For acute triangles, substitute \(h=\pi\), \(a=\pi\) into the CDF. When \(L\le\pi\) the support starts at or above \(\pi/2\); for \(\pi<L\le2\pi\), simplifying gives \((L-\pi)^2(4\pi-L)/L^3\). Its derivative is \(6\pi(L-\pi)(2\pi-L)/L^4>0\) in the stated interval. Substitution and expansion at the endpoints yield the claimed acute threshold and full-circle value.

For the lower-tail exponents, write \(m=m_0(L)+\delta\). If \(L\le\pi\), then for sufficiently small \(\delta\), the admissible interval has \(r\in[L-2\delta,L]\) and \(\ell_h(r)=r\). Integration gives \(F_L=12\delta^2/L^2-16\delta^3/L^3\). If \(\pi<L<4\pi/3\), the same interval has \(\ell_h(r)=2h-r\), giving \(F_L=12(4\pi-3L)\delta^2/L^3+64\delta^3/L^3\). At \(L=4\pi/3\) the quadratic coefficient vanishes exactly, leaving \(64\delta^3/L^3\). If \(L>4\pi/3\), the admissible \(r\)-interval shrinks around \(r=4\pi/3\): its endpoints are \(4\pi/3-2\delta\) and \(4\pi/3+4\delta\). Integrating the triangular width \(\ell_h(r)=4\pi/3+4\delta-r\) gives the asserted quadratic leading term \(108(L-4\pi/3)\delta^2/L^3\). All statements follow.

## Verification

A standalone Python 3 standard-library checker is supplied as `arc_max_angle_verify.py`. Run `python arc_max_angle_verify.py`. It compares the closed CDF against a separate gap-integral implementation (piecewise cubic integration), performs direct three-angle sampling with a fixed pseudorandom seed, checks the lower-tail coefficients in all regimes, and checks the full-circle acute benchmark. Its completed run printed `ALL_CHECKS_PASSED`. These checks corroborate, but do not replace, the exact integration proof.

## Relationship to prior work

The full-circle acute-triangle probability of \(1/4\) is classical and is explicitly not asserted as new. Khan's 2017 study of acute random triangles treats independently sampled points from the **area** of convex regions, not from a circular arc. Kabluchko's 2019 work treats expected internal angles and face vectors for spherically symmetric full-ball or full-sphere sampling, not the maximum-angle CDF for a truncated circle arc. Greenwell's 2026 work on three points sampled from full concentric circles discusses the classical full-circle uniform-angle law and computes a different (radially heterogeneous) obtuse probability. The present contribution is the two-parameter truncated-arc maximum-angle distribution, including the sharp critical cubic onset. The distinction is sampling support and the exact statistic, not a rebranding of the classical full-circle value.

## Limitations

Only independent uniform sampling from one circular arc and Euclidean interior angles are treated. No assertion is made for nonuniform angular densities, general smooth curves, samples from planar regions, or the entire joint angle law under general sampling. The full-circle special case is previously known. Priority outside the inspected literature is provisional; the analytic expressions alone do not establish historical novelty.

## References

- G. Khan, *Hall's Conjecture on Extremal Sets for Random Triangles*, arXiv:1704.05913 (first posted 2017-04-19), https://arxiv.org/html/1704.05913v4 .
- Z. Kabluchko, *Angles of Random Simplices and Face Numbers of Random Polytopes*, arXiv:1909.13335 (first posted 2019-09-29), https://arxiv.org/abs/1909.13335 .
- B. M. Greenwell, *Random Triangles on Concentric Circles*, arXiv:2608.06591 (first posted 2026-08-06), https://arxiv.org/abs/2608.06591 .
- E. W. Weisstein, *Circle Triangle Picking*, MathWorld, https://mathworld.wolfram.com/CircleTrianglePicking.html .
