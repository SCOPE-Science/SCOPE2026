# The exact John ellipsoid of a Euclidean spherical cap and its universal simplex contacts

## Finding
For every integer \(d\ge3\) and every \(-1<a<1\), consider the solid spherical cap
\[
K_{d,a}=\{(x,z)\in\mathbb R\times\mathbb R^{d-1}:x^2+\|z\|^2\le1,\ x\ge a\}.
\]
Set
\[
\Delta=\sqrt{a^2+\frac{4d(1-a^2)}{(d+1)^2}},\qquad
u=\frac{\Delta-a}{2},\qquad t=\frac{\Delta+a}{2},\qquad
v=\sqrt{u^2+dut}.
\]
The unique maximum-volume inscribed ellipsoid, with **no restrictions on the center or orientation of competing ellipsoids**, is
\[
E_{d,a}=\left\{(x,z):\frac{(x-t)^2}{u^2}+\frac{\|z\|^2}{v^2}\le1\right\}.
\]
Its volume is \(\kappa_d u v^{d-1}\), where \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\). Under the normalization \((x,z)=(t+us,vw)\), **every** contact of the ellipsoid with the curved spherical boundary has \(s=1/d\); its only flat-facet contact has \(s=-1\). One can choose exactly \(d+1\) contact points forming a regular unit-sphere \(d\)-simplex. This contact geometry is independent of \(a\).

Two exact benchmarks for the ratio \(R_d(a)=\operatorname{Vol}(E_{d,a})/\operatorname{Vol}(K_{d,a})\) are
\[
R_d(0)=\frac{2d^{d/2}}{(d+1)^{(d+1)/2}},\qquad
\lim_{a\uparrow1}R_d(a)=\frac{\kappa_d}{\kappa_{d-1}}\left(\frac d{d+1}\right)^d.
\]
At fixed \(a>0\), \(du\to(1-a^2)/a\), \(t\to a\), and \(v\to\sqrt{1-a^2}\) as \(d\to\infty\). At fixed \(a<0\), \(u\to-a\), \(dt\to(1-a^2)/(-a)\), and \(v\to1\). The boundary layer \(a=\sigma/\sqrt d\), for fixed real \(\sigma\), has
\[
\sqrt d\,u\to\frac{\sqrt{\sigma^2+4}-\sigma}{2},\quad
\sqrt d\,t\to\frac{\sqrt{\sigma^2+4}+\sigma}{2},\quad v\to1.
\]
This describes the dimensional transition between axial scales \(1\), \(d^{-1/2}\), and \(d^{-1}\).

## Assumptions and scope
The ambient norm is Euclidean; the ball has radius one; the cutting plane is \(x=a\) and the **retained solid** is \(x\ge a\). The strict range \(-1<a<1\) makes \(K_{d,a}\) full dimensional and ensures \(t,u,v>0\). Reflections, arbitrary orthogonal changes of the cutting direction, common rescalings, and nonsingular affine images follow by affine equivariance. No claim concerns nonconvex spherical shells or intersections with multiple independent halfspaces.

## Proof
**1. An exact containment identity.** The definitions give
\[
t-u=a,\qquad ut=\frac{d(1-a^2)}{(d+1)^2},\qquad v^2=u^2+dut,
\]
and hence
\[
t^2+v^2+\frac{ut}{d}
=(t-u)^2+\frac{(d+1)^2}{d}ut=1.
\]
Every boundary point of \(E_{d,a}\) can be written as
\((t+us,v\sqrt{1-s^2}\,\omega)\) with \(-1\le s\le1\) and \(\omega\in S^{d-2}\). Direct expansion yields the exact identity
\[
1-\left[(t+us)^2+v^2(1-s^2)\right]
=dut\left(s-\frac1d\right)^2\ge0.
\]
Also \(t+us\ge t-u=a\). Thus \(E_{d,a}\subseteq K_{d,a}\). Equality with the sphere occurs **only** when \(s=1/d\), because \(dut>0\). Equality with the cutting plane occurs only at \(s=-1\). By convexity, containment of the ellipsoid's boundary suffices for its interior.

**2. Full-dimensional optimality, without an orientation ansatz.** Let \(\omega_1,\ldots,\omega_d\) be the vertices of a regular unit-sphere \((d-1)\)-simplex in \(\mathbb R^{d-1}\), so that
\[\sum_j\omega_j=0,\qquad\sum_j\omega_j\omega_j^T=\frac d{d-1}I_{d-1}.\]
Under the affine map \((s,w)\mapsto(t+us,vw)\), the normalized body \(\widetilde K\) contains the Euclidean unit ball. Its boundary meets that ball at
\[
\xi_0=(-1,0),\qquad
\xi_j=\left(\frac1d,\sqrt{1-\frac1{d^2}}\,\omega_j\right),\quad j=1,\ldots,d.
\]
The first contact comes from the cutting plane, the others from the curved sphere. The displayed vectors are unit and satisfy \(\xi_i\cdot\xi_j=-1/d\) for distinct indices: they form a regular \(d\)-simplex, with
\[
\sum_{j=0}^d\frac d{d+1}\xi_j=0,
\qquad
\sum_{j=0}^d\frac d{d+1}\xi_j\xi_j^T=I_d.
\]
These are precisely the two positive-weight John contact identities. By the *sufficient* direction of John's ellipsoid theorem, the unit ball is the unique maximum-volume ellipsoid in \(\widetilde K\). Undoing the affine map proves that \(E_{d,a}\) is the unique global maximizer, not merely a maximizer among rotationally symmetric ellipsoids.

**3. Volume ratios.** Slicing perpendicular to the first coordinate gives
\[
\operatorname{Vol}(K_{d,a})=\kappa_{d-1}\int_a^1(1-x^2)^{(d-1)/2}\,dx.
\]
At \(a=0\), \(t=u=\sqrt d/(d+1)\), \(v^2=d/(d+1)\), and the cap has half the ball's volume; substitution proves the first ratio. With \(\varepsilon=1-a\downarrow0\), the explicit semiaxes satisfy
\[
u\sim\frac{2d}{(d+1)^2}\varepsilon,\qquad
v^2\sim\frac{2d^2}{(d+1)^2}\varepsilon.
\]
Changing variables \(x=1-\varepsilon y\) in the cap integral yields
\[
\operatorname{Vol}(K_{d,1-\varepsilon})
\sim\kappa_{d-1}\frac{2^{(d+1)/2}}{d+1}\varepsilon^{(d+1)/2}.
\]
Taking the ratio to \(\kappa_d u v^{d-1}\) proves the thin-cap expression.

**4. Dimension regimes.** At fixed \(a\ne0\), expand
\(\Delta=\sqrt{a^2+4d(1-a^2)/(d+1)^2}\) in powers of \(1/d\), choosing \(\sqrt{a^2}=|a|\). The stated positive/negative-cut regimes follow. At \(a=\sigma/\sqrt d\), multiply \(\Delta\) by \(\sqrt d\) before taking the limit, obtaining \(\sqrt{\sigma^2+4}\). Finally, \(v^2=u^2+dut\) proves the transverse limit. Each statement fixes \(a\) or \(\sigma\) before sending the integer \(d\) to infinity.

## Verification
The included `verify.py` checks the exact containment polynomial at varied coordinates and parameters, the regular-simplex Gram matrix and positive John moment identities, the hemisphere and thin-cap ratios by independent quadrature, the high-dimensional scaling limits, and the previously known planar half-disk special case. It requires only Python's standard library. Reproduce with `python3 verify.py`; the expected final line is `ALL_CHECKS_PASSED`. These finite checks provide reproducibility but do not replace the exact containment identity and John's theorem used above.

## Relationship to prior work
The classical John contact criterion supplies optimality once an admissible ellipsoid and a positive moment decomposition are exhibited. Ivanov and Naszódi (2022, later revised) develop much more general functional John–Löwner conditions; their statements do not specialize to the explicit spherical-cap semiaxes, separation-independent regular-simplex contacts, or high-dimensional transition derived here. The earlier planar half-disk maximum-area ellipse is known (2015); **its two-dimensional, zero-offset calculation is not claimed as new**. The assertions concern the all-cut, all-dimensional cap geometry, which the inspected predecessors do not directly compute.

## Limitations
The result treats one affine cut of a Euclidean ball. A full historical-priority search for older cap-ellipsoid formulae has not been completed, and equivalent classical descriptions may exist under the terms *circular segment* or *ball truncation*. The high-dimensional limits are pointwise in the stated fixed parameter regimes, not uniform over all \(-1<a<1\). The numerical checker is finite; the unrestricted optimum is established by the analytic John certificate.

## References
1. Grigory Ivanov and Márton Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781, first posted 2022-12-22, https://arxiv.org/abs/2212.11781.
2. *John Ellipsoid and the center of mass of a convex body*, arXiv:1605.06881, https://arxiv.org/abs/1605.06881; Section 2.1 states the positive John decomposition criterion.
3. *Need to find the ellipse of maximum area inscribed in a semicircle*, Mathematics Stack Exchange, question 2015-12-17 and substantive answers 2015-12-20 and 2015-12-23, https://math.stackexchange.com/questions/1579406/need-to-find-the-ellipse-of-maximum-area-inscribed-in-a-semicircle (pre-existing planar special case).
4. F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948; K. Ball, *Ellipsoids of maximal volume in convex bodies*, 1992.
