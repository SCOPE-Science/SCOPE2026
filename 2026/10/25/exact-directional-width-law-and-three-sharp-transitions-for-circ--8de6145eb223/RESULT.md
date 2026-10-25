# Exact directional-width law and three sharp transitions for circular frusta

## Finding

Let a right circular frustum be the convex hull of two filled, concentric-in-projection disks in parallel horizontal planes: the disk of radius \(R\) at height \(0\) and the disk of radius \(r\) at height \(H\), where \(R>r>0\) and \(H>0\). Let \(W\) be the length of its projection onto a uniformly oriented random line in \(\mathbb R^3\) (equivalently, its width in a Haar-uniform unit direction). **The entire distribution of \(W\) is given by the following elementary formula for every positive triple \((R,r,H)\).**

Put
\[
 a=R+r,\qquad d=R-r,\qquad
 M=\sqrt{a^2+H^2},\qquad t_0=\frac d{\sqrt{d^2+H^2}}.
\]
For any \(w\geq0\), define
\[
 D(w)=\begin{cases}
 \min\left\{t_0,\sqrt{1-\dfrac{w^2}{4R^2}}\right\},&0\leq w<2R,\\
 0,&w\geq2R,
 \end{cases}
\]
\[
 \ell(w)=\frac{Hw-a\sqrt{M^2-w^2}}{M^2},\qquad
 u(w)=\begin{cases}
 1,&0\leq w<H,\\
 \dfrac{Hw+a\sqrt{M^2-w^2}}{M^2},&H\leq w<M,
 \end{cases}
\]
and
\[
 E(w)=\begin{cases}
 \max\big\{0,\min\{1,u(w)\}-\max\{t_0,\ell(w)\}\big\},&0\leq w<M,\\
 0,&w\geq M.
 \end{cases}
\]
Then the exact survival function and CDF are
\[
 \boxed{\Pr(W>w)=D(w)+E(w),\quad F_W(w)=1-D(w)-E(w)\quad(w\geq0),}
\]
with \(F_W(w)=0\) for \(w<0\). The law has no atoms. This formula handles all overlapping branch ranges, with no generic-position or noncritical-height restrictions.

The law exhibits **three distinct, sharp height thresholds** in every genuine frustum \(R>r>0\):
\[
 H_1=\sqrt{R^2-r^2},\quad
 H_2=\sqrt{(R-r)(3R+r)},\quad
 H_3=\sqrt{(R+r)(3R-r)},
 \qquad 0<H_1<H_2<H_3<2R.
\]
When \(H\leq H_1\), width decreases with the absolute axial cosine. At \(H_1\) a new oblique local width maximum is born (strictly present for \(H>H_1\)). At \(H_2\) that oblique maximum ties, then overtakes, the equatorial global maximum. At \(H_3\) the global minimum passes from the axial viewing direction to the support-switch latitude. More explicitly,
\[
 \boxed{\operatorname*{ess\,sup}W=\max\{2R,\sqrt{a^2+H^2}\},\qquad
 \operatorname*{ess\,inf}W=\min\left\{H,\frac{2RH}{\sqrt{H^2+d^2}}\right\}.}
\]
The maximum is attained at absolute axial cosine \(t=0\) for \(H<H_2\), at both \(t=0\) and \(t=H/M\) for \(H=H_2\), and only at \(t=H/M\) for \(H>H_2\). The minimum is attained at \(t=1\) for \(H<H_3\), at both \(t=1\) and \(t=t_0\) for \(H=H_3\), and only at \(t=t_0\) for \(H>H_3\). Here uniqueness is in \(t\), not in azimuth: each oblique latitude consists of an axial-symmetry circle of directions.

The sharp probability that a random width **exceeds the equatorial diameter \(2R\)** is
\[
 \boxed{\Pr(W>2R)=\begin{cases}
 0,& H\leq H_2,\\[2pt]
 \dfrac{2a\sqrt{H^2-H_2^2}}{a^2+H^2},&H_2<H\leq2R,\\[6pt]
 1-\dfrac{2RH-a\sqrt{H^2-H_2^2}}{a^2+H^2},&H>2R.
 \end{cases}}
\]
In particular, for fixed \(R>r>0\) and \(\varepsilon\downarrow0\),
\[
 \boxed{\Pr_{H=H_2+\varepsilon}(W>2R)
 =\frac{(R+r)\sqrt{2H_2}}{2R^2}\sqrt{\varepsilon}
 +O_{R,r}(\varepsilon^{3/2}).}
\]
The square-root onset sharply distinguishes an emerging *positive-probability* set of super-equatorial directions from the earlier birth of an oblique stationary direction at \(H_1\).

The expected directional width, a consistency benchmark for the complete law, is also exact:
\[
 \boxed{\mathbb E W=\frac{\pi(R+r)}4+\frac H2
 +\frac{R-r}{2}\arctan\frac{R-r}{H}.}
\]

## Assumptions and scope

Both disks are solid and coaxial; the smaller has strictly positive radius and the planes are distinct. The body is their three-dimensional convex hull, including the sloping ruled boundary, not a hollow surface. All lengths use a common Euclidean scale. The measure on unoriented lines is the rotation-invariant probability measure (equivalently the pushforward of normalized spherical area). The full CDF applies even at the three threshold heights; exceptional direction sets have measure zero. The local/global extremizer statements concern axial cosine \(t=|u_z|\in[0,1]\), with its natural rotational multiplicity.

The one-disk cone limit \(r=0\) and the equal-disk cylinder limit \(r=R\) are excluded from the three-**distinct**-threshold claim: two thresholds coalesce in each respective limit. They are permitted only as checks of the algebraic formulas by continuity.

## Proof

**1. A geometric two-support decomposition.** Let \(u\in S^2\) and write \(t=|u_z|\), \(s=\sqrt{1-t^2}\). The two disks give positive-direction supports \(Rs\) and \(rs+Ht\), after choosing the sign of the axis without loss of width symmetry. In the opposite direction, the larger disk has support \(Rs\) because \(Rs>rs-Ht\). Since the support function of the convex hull is the maximum of the supports,
\[
 W(t)=Rs+\max\{Rs,rs+Ht\}=\max\{2Rs,as+Ht\}.
 \tag{1}
\]
The two terms coincide exactly when \(Ht=ds\), at the unique latitude \(t=t_0=d/\sqrt{H^2+d^2}\). Hence
\[
 W(t)=\begin{cases}
 2R\sqrt{1-t^2},&0\leq t\leq t_0,\\
 a\sqrt{1-t^2}+Ht,&t_0\leq t\leq1.
 \end{cases}
 \tag{2}
\]
For a Haar-uniform direction in three dimensions, the signed axial cosine is uniform on \([-1,1]\); consequently its absolute value \(t\) is uniform on \([0,1]\). Width is thus the pushforward of ordinary uniform Lebesgue measure by (2).

**2. Inversion and all CDF branches.** For \(w\in[0,2R)\), the first branch of (2) exceeds \(w\) precisely when \(t<\sqrt{1-(w/2R)^2}\). Intersecting that interval with \([0,t_0]\) gives length \(D(w)\). At \(w\geq2R\) its length is zero.

For the second branch write \(g(t)=a\sqrt{1-t^2}+Ht\). It is strictly concave on \((0,1)\) and has its unconstrained maximum \(M\) at \(t_*=H/M\). Thus every strict superlevel set \(\{t:g(t)>w\}\cap[t_0,1]\) is an interval, possibly empty. The quadratic equation obtained from \(g(t)=w\) has formal roots
\[
 t_\pm(w)=\frac{Hw\pm a\sqrt{M^2-w^2}}{M^2}.
 \tag{3}
\]
The smaller root \(t_-(w)\) is genuine whenever it lies in \([0,1]\), because
\[
 w-Ht_-(w)=\frac{a(aw+H\sqrt{M^2-w^2})}{M^2}>0.
\]
The larger root is genuine if and only if \(w\geq H\): its unsquared condition \(w-Ht_+(w)\geq0\) reduces, by squaring nonnegative factors, precisely to \(w\geq H\). For \(0\leq w<H\) the superlevel interval extends to \(t=1\), since \(g(1)=H>w\). Consequently the superlevel interval has lower endpoint \(\ell(w)=t_-(w)\) and upper endpoint \(u(w)\) as stated, clipped to \([t_0,1]\). Its length is exactly \(E(w)\), while for \(w\geq M\) it is empty. The two intervals occupy the disjoint parameter ranges \([0,t_0]\) and \([t_0,1]\), so their measures add. This proves the CDF for every height and threshold. The function \(W(t)\) has only finitely many monotonic segments and no constant segment, so the pushforward law has no atoms.

**3. Local critical point and its birth.** The first branch in (2) is strictly decreasing away from \(t=0\). The second branch satisfies
\[
 g'(t)=H-\frac{at}{\sqrt{1-t^2}},\qquad
 g''(t)=-\frac{a}{(1-t^2)^{3/2}}<0.
\]
Its unique stationary point is \(t_*=H/M\). This lies in \([t_0,1]\) exactly when
\[
 \frac{H^2}{a^2+H^2}\geq\frac{d^2}{d^2+H^2}
 \quad\Longleftrightarrow\quad H^2\geq ad=R^2-r^2=H_1^2.
\]
For \(H\leq H_1\), the full width profile decreases (allowing a zero one-sided derivative at the junction when equality holds). For \(H>H_1\), \(t_0\) is a strict local minimum and \(t_*\) a strict oblique local maximum.

**4. Two global extremum switches and sharp order.** The equatorial endpoint gives \(W(0)=2R\). When the oblique critical point is admissible its width is \(g(t_*)=M\). It exceeds the equatorial value exactly when
\[
 M^2>4R^2\ \Longleftrightarrow\ H^2>4R^2-a^2=d(3R+r)=H_2^2.
\]
At equality both latitudes attain the global maximum. The first branch has minimum at \(t_0\), and the second branch is concave, so its minimum is at one of its two endpoints. Thus the only global-minimum candidates are
\[
 W(t_0)=\frac{2RH}{\sqrt{H^2+d^2}}
 \quad\text{and}\quad W(1)=H.
\]
The first is smaller exactly when \(H^2>4R^2-d^2=a(3R-r)=H_3^2\). This proves the two global extremum switches and all equality cases. The strict ordering follows from
\[
 H_2^2-H_1^2=2Rd>0,
 \qquad H_3^2-H_2^2=4Rr>0,
 \qquad 4R^2-H_3^2=d^2>0.
\]
These differences are strictly positive for every genuine frustum and account for three distinct transitions rather than the two coalescing transitions of a full cone.

**5. Widths exceeding the base diameter.** The first branch never exceeds \(2R\), and the second does so on a nonempty interval exactly when \(M>2R\), i.e. \(H>H_2\). Set \(w=2R\) in (3). For \(H_2<H\leq2R\), both crossing roots lie in \([t_0,1]\), so their separation is
\[
 t_+(2R)-t_-(2R)=\frac{2a\sqrt{H^2-H_2^2}}{M^2}.
\]
For \(H>2R\), the right endpoint itself has width \(H>2R\), so the superlevel interval is \((t_-(2R),1]\), of length \(1-t_-(2R)\). The formulas match at \(H=2R\). For \(H\downarrow H_2\), write \(H=H_2+\varepsilon\). Then \(H^2-H_2^2=2H_2\varepsilon+\varepsilon^2\) and \(M^2=4R^2+2H_2\varepsilon+\varepsilon^2\), giving the stated leading square-root term with an \(O_{R,r}(\varepsilon^{3/2})\) remainder.

**6. Mean-width check.** Integration of (2) over uniform \(t\) gives
\[
 \int_0^1W(t)\,dt
 =a\int_0^1\sqrt{1-t^2}\,dt
 +d\int_0^{t_0}\sqrt{1-t^2}\,dt
 +H\int_{t_0}^1t\,dt.
\]
The first integral is \(\pi/4\), the second is \((t_0\sqrt{1-t_0^2}+\arcsin t_0)/2\), and \(\arcsin(t_0)=\arctan(d/H)\). The terms involving \(t_0\sqrt{1-t_0^2}\) and \(1-t_0^2\) combine into \(H/2\), proving the expectation formula. This derivation is independent of any numerical integration.

## Verification

The included standalone, standard-library script `verify.py` is executable using `python3 verify.py` from the folder containing this document. It performs direct support calculations for finite samples on **both original disks** (rather than the derived width branches), compares empirical CDF values from uniformly sampled axial cosines with the closed formula, checks the mean by independent quadrature, compares extrema to the sharp formulas on dense direction grids, tests threshold ordering and exact super-equatorial tail identities, and tests the asymptotic onset coefficient across decreasing perturbations. The recorded execution completed with all checks passing and the final message `ALL_FRUSTUM_WIDTH_LAW_CHECKS_OK`.

This checker uses finite approximations only for corroboration. The rigorous statements for all \(R>r>0\), \(H>0\), and all real CDF thresholds follow from the continuous derivations in the proof. Sampling resolution does not establish universal correctness or exclude a counterexample by itself.

## Relationship to prior work

Finch's 2012 paper studies volume, surface area, and **mean width** for oblique cylinders and cones, including right circular special cases. The mean above agrees with the cone and cylinder endpoint specializations but does not follow as a complete distribution from the scalar mean. This paper does not provide the interior unequal-radius frustum law.

Kim, Yaskin, and Zvavitch (2015) formulate geometric tomography based on **unlabeled hyperplane-section areas and two-dimensional projection areas**. Those distributions are distinct from the one-dimensional line-projection length studied here, and their principal theorems concern general nonuniqueness and comparison phenomena rather than the exact frustum law.

The public result *Unlabeled directional widths determine a right circular cone* supplies a complete distribution and an inverse theorem for **the disk-plus-apex family** \(r=0\). That limiting family is disjoint from the stipulated \(R>r>0\) and has a coalescence \(H_2=H_3\), so its distribution theorem does not state the present three-distinct-threshold frustum classification. The present claim does **not** assert a new result for cones, an inverse reconstruction theorem, or a general convex-body width distribution. It treats the genuinely intermediate geometry of two unequal positive coaxial disks.

Vickers and Brown (2001) treat projected planar **area and perimeter** distributions of ellipsoidal, cylindrical, and conical particles. Their available abstract does not specify directional line-width laws of positive-radius frusta. That full publication was not inspected and remains an explicit priority risk; the two-dimensional observables in its abstract do not directly imply the formula established here.

## Limitations

The exact probability law assumes coaxial, filled circular bases with unequal positive radii and Haar-uniform viewing directions in three dimensions. It does not apply automatically to oblique frusta, hollow shells, elliptical bases, non-Haar observations, or randomly translated section planes. Three distinct threshold heights do not persist at the cone and cylinder endpoints. The theorem does not determine a frustum from partial or noisy width data and makes no assertion about planar projected-area distributions. Historical originality remains provisional, particularly with respect to any unavailable prior treatment of one-dimensional frustum widths. No independent mathematical audit has been performed.

## References

1. Steven R. Finch, *Oblique Circular Cones and Cylinders*, arXiv:1212.5946v1, first public 2012-12-24, https://arxiv.org/abs/1212.5946v1 .
2. Jaegil Kim, Vladyslav Yaskin, Artem Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 2015-12-22, https://arxiv.org/abs/1512.07289v1 .
3. *Unlabeled directional widths determine a right circular cone*, publicly available in https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-unlabeled-directional-widths-determine-a-right-circular-cone--30a3b32d19eb .
4. G. T. Vickers and D. J. Brown, *The Distribution of Projected Area and Perimeter of Convex, Solid Particles*, Proceedings of the Royal Society A **457** (2001), 283–306, DOI:10.1098/rspa.2000.0667 .
