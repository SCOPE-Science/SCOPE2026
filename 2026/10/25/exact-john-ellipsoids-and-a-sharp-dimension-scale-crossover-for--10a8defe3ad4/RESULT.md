# Exact John ellipsoids and a sharp dimension-scale crossover for symmetric two-ball lenses

## Finding

For any integer \(d\ge2\) and any \(0<h<1\), consider the intersection of two unit Euclidean balls whose centers are separated by \(2h\):

\[
L_{d,h}=B_2^d(he_1,1)\cap B_2^d(-he_1,1)
=\{(x,y)\in\mathbb R\times\mathbb R^{d-1}:(|x|+h)^2+\|y\|^2\le1\}.
\]

The unique maximum-volume inscribed ellipsoid is

\[
E_{d,h}=\left\{(x,y):\frac{x^2}{a_{d,h}^2}+\frac{\|y\|^2}{b_{d,h}^2}\le1\right\},
\qquad
 a_{d,h}=\frac{2(1-h^2)}{\sqrt{4+\frac{(d-1)^2}{d}h^2}+\frac{d+1}{\sqrt d}h},
\qquad b_{d,h}=\sqrt{a_{d,h}^2+h a_{d,h}\sqrt d}.
\]

Its contact set with the lens boundary consists **exactly** of the two latitude orbits

\[
 x=\pm\frac{a_{d,h}}{\sqrt d},\qquad
 \|y\|=b_{d,h}\sqrt{\frac{d-1}{d}}.
\]

The corresponding unit-ball normalized volume is the explicit \(R_d(h)=a_{d,h}b_{d,h}^{d-1}\), which decreases strictly as the center separation increases. Its dimension-dependent limit has a sharp crossover at center half-separations of order \(d^{-1/2}\). Put

\[
 A_\tau=\frac{\sqrt{\tau^2+4}-\tau}{2},\qquad
 \mathcal F(\tau)=A_\tau\exp\left[-\frac{\tau(A_\tau+\tau)}{2}\right].
\]

For every sequence \(0<h_d<1\),

\[
\begin{aligned}
 h_d\sqrt d\longrightarrow\tau\in[0,\infty)
 &\quad\Longrightarrow\quad R_d(h_d)\longrightarrow\mathcal F(\tau),\
 h_d\sqrt d\longrightarrow\infty
 &\quad\Longrightarrow\quad R_d(h_d)\longrightarrow0.
\end{aligned}
\]

In particular, \(\mathcal F(0)=1\), while \(0<\mathcal F(\tau)<1\) for every \(\tau>0\). At every fixed \(h\in(0,1)\) there is the sharper asymptotic

\[
R_d(h)\sim\frac{e^{-1/2}(1-h^2)^{(d+1)/2}}{h\sqrt d}.
\]

## Assumptions and scope

Euclidean dimension is any integer at least two. Both generating balls have radius one and distinct centers whose distance is strictly between zero and two. The lens is a full-dimensional compact convex body. The limiting statements concern \(d\to\infty\); no uniform fixed-separation approximation is asserted when the separation itself approaches either endpoint. The case \(h=0\) is the unit ball, for which \(a=b=R_d=1\) and every boundary point contacts.

## Proof

**Positive parameters and feasibility.** Abbreviate \(a=a_{d,h}\) and \(b=b_{d,h}\). Rationalizing the positive quadratic root proves

\[
 a^2+\frac{d+1}{\sqrt d}ha+h^2=1,
 \qquad b^2=a^2+ha\sqrt d.
\]

In particular both semiaxes are positive. Every point on the boundary of \(E_{d,h}\) has the form \((aq,b\sqrt{1-q^2}\,w)\), where \(-1\le q\le1\) and \(w\) is any unit vector in \(\mathbb R^{d-1}\). Setting \(u=|q|\) and substituting the two identities gives the **exact containment certificate**

\[
 1-\big[(h+au)^2+b^2(1-u^2)\big]
 =ha\sqrt d\left(u-\frac1{\sqrt d}\right)^2\ge0.
\]

The lens is convex, so containing the ellipsoid's boundary also contains its interior. Because \(ha>0\), equality holds precisely when \(u=1/\sqrt d\), yielding the stated complete contact set.

**Global optimality and uniqueness.** Apply the invertible diagonal linear change \((x,y)\mapsto(x/a,y/b)\). It takes \(E_{d,h}\) to the unit ball, and its contact points with the transformed lens include

\[
 u_{\sigma,j,\varepsilon}=
 \left(\frac{\sigma}{\sqrt d},\;
 \varepsilon\sqrt{\frac{d-1}{d}}\,e_j\right),
 \quad \sigma,\varepsilon\in\{-1,1\},\quad j=2,\dots,d.
\]

Here \(e_j\) is the \(j\)-th coordinate vector, and \(2(d-1)\) is the number of independent sign-pairs. Assign to **each** of these \(4(d-1)\) contact points the positive weight \(\lambda=d/[4(d-1)]\). Opposite signs cancel the first moments, while direct diagonal calculation shows

\[
 \sum_{\sigma,j,\varepsilon}\lambda u_{\sigma,j,\varepsilon}=0,
 \qquad
 \sum_{\sigma,j,\varepsilon}\lambda
 u_{\sigma,j,\varepsilon}u_{\sigma,j,\varepsilon}^{\mathsf T}=I_d.
\]

Fritz John's contact characterization therefore makes the transformed unit ball the **unique** maximal-volume inscribed ellipsoid of the transformed convex lens. Applying the inverse affine transformation proves the assertion for \(E_{d,h}\). No assumption that the ellipsoid is rotationally symmetric is needed to exclude competitors: the contact conditions prove global optimality over *all* inscribed ellipsoids.

**Strict monotonicity.** If \(0<h_1<h_2<1\), then \(L_{d,h_2}\subsetneq L_{d,h_1}\). If their John ellipsoids had equal volume, the smaller lens's John ellipsoid would also maximize volume in the larger lens. Uniqueness would force both ellipsoids to coincide, contradicting the strictly positive boundary contact deficit when the first ellipsoid is tested against the more distant centers. Hence \(R_d(h_2)<R_d(h_1)\).

**Critical scaling.** Write \(h=\tau/\sqrt d\). The quadratic relation becomes

\[
 a^2+\tau\left(1+\frac1d\right)a+\frac{\tau^2}{d}=1.
\]

For fixed \(\tau\ge0\), its positive solution converges to the positive root \(A_\tau\) of \(A_\tau^2+\tau A_\tau=1\). Expanding the equation once more gives

\[
 a=A_\tau-\frac{\tau(A_\tau+\tau)}{(2A_\tau+\tau)d}+O_\tau(d^{-2}),
 \qquad
 b^2=1-\frac{\tau(A_\tau+\tau)}d+O_\tau(d^{-2}).
\]

Consequently \(a b^{d-1}\to\mathcal F(\tau)\). If \(h_d\sqrt d\to\tau<\infty\), monotonic comparison with \(h=(\tau\pm\varepsilon)/\sqrt d\) and continuity of \(\mathcal F\) extend the fixed-parameter limit to the varying sequence (using \(0\) as the lower endpoint). If \(h_d\sqrt d\to\infty\), monotonicity bounds \(R_d(h_d)\) above by the limit at each fixed positive \(\tau\), and \(\mathcal F(\tau)\to0\) as \(\tau\to\infty\).

**Fixed-separation regime.** Fix \(h\in(0,1)\). The same quadratic relation, after setting \(t=\sqrt d\,a\), gives

\[
 a=\frac{1-h^2}{h\sqrt d}\bigl(1+O_h(d^{-1})\bigr),
 \qquad
 b^2=(1-h^2)\left(1-\frac1d+O_h(d^{-2})\right).
\]

Raising the second identity to the power \((d-1)/2\) yields the factor \(e^{-1/2}\), completing the asserted asymptotic.

## Verification

The analytic containment certificate and the explicit John weights are finite symbolic identities valid for every permitted dimension and separation; they constitute the universal proof. The accompanying standalone script `verify_lens.py` checks these identities on broad parameter grids, recomputes the entire John contact covariance matrix, and compares the limiting expressions at large finite dimensions. Run it with `python verify_lens.py` using Python's standard library. No finite test is construed as proof of the quantified theorem.

## Relationship to prior work

Fritz John's classical theorem characterizes maximal-volume inscribed ellipsoids; it is the optimality criterion used here, not a pre-existing computation of these semiaxes. Güler and Gürtuna (arXiv:0709.0707, especially Sections 3, 5, and 7) provide general ellipsoid optimality conditions and explicit results for Euclidean balls truncated by **parallel hyperplanes**, rather than by a second ball. Finch (arXiv:1301.5515, Section 1) treats a symmetric two-ball lens through volume, surface area, and mean width, but not its maximum-volume ellipsoid. Paouris and Pivovarov (arXiv:1510.07292, introduction and main results) address intrinsic-volume inequalities for random intersections of congruent balls, not the lens's John axes or their dimension-dependent volume crossover. Earlier geometric discussions of spherical dihedra are acknowledged; the historical priority of the precise present ellipsoid formula has not been independently certified.

## Limitations

Only **two congruent** Euclidean balls are treated; no claim extends to unequal radii, larger finite ball systems, or general ball-polyhedra. Optimality is proved analytically, not by numerical maximization. The asymptotic statements are pointwise or along specified dimension-dependent sequences. The case of disjoint balls, \(h\ge1\), is excluded. This manuscript has undergone self-review but no independent scientific audit; an equivalent treatment in older specialist literature cannot be ruled out categorically.

## References

- F. John, *Extremum problems with inequalities as subsidiary conditions*, 1948.
- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707, first posted 2007-09-05.
- S. R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515, first posted 2013-01-23.
- G. Paouris and P. Pivovarov, *Random ball-polyhedra and inequalities for intrinsic volumes*, arXiv:1510.07292, first posted 2015-10-25.
