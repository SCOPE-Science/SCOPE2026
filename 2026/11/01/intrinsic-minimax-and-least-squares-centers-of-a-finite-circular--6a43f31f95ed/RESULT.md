# Intrinsic minimax and least-squares centers of a finite circular cone

## Finding

Let \(C_{L,t}\) denote the **lateral surface only** of a nondegenerate right circular cone of slant length \(L>0\) and base radius \(tL\), where \(0<t<1\). Include its apex and circular rim, exclude its base disk, and use intrinsic shortest-path distance. Write \(\beta=\pi t\). For a source point with slant distance \(r\in[0,L]\) from the apex, its eccentricity is
\[
 e_t(r)=\max\left\{r,\sqrt{r^2+L^2-2rL\cos\beta}\right\}.
\]
Its **Chebyshev radius** \(\rho_C=\min_p\max_q d(p,q)\), together with the complete set of minimizing points, is
\[
 \frac{\rho_C}{L}=\begin{cases}
 (2\cos\beta)^{-1},&0<t\le1/4,\\
 \sin\beta,&1/4\le t\le1/2,\\
 1,&1/2\le t<1,
 \end{cases}
 \qquad
 \frac{r_C}{L}=\begin{cases}
 (2\cos\beta)^{-1},&0<t\le1/4,\\
 \cos\beta,&1/4\le t\le1/2,\\
 0,&1/2\le t<1.
 \end{cases}
\]
For \(t<1/2\), **every** point of the parallel circle at slant radius \(r_C\), and no other point, is a Chebyshev center. For \(t\ge1/2\), the apex is the unique Chebyshev center. At \(t=1/4\) the two formulas coincide; at \(t=1/2\) the circle collapses continuously to the apex.

For an independently sampled point \(X\) that is uniform with respect to intrinsic area, let \(F_t(p)=\mathbb E[d(p,X)^2]\). The complete set of **intrinsic Fréchet least-squares centers** is always a nonapical parallel circle, of slant radius
\[
 \frac{r_F}{L}=\frac23\frac{\sin\beta}{\beta},\qquad
 \min_p F_t(p)=L^2\left(\frac12-\frac49\frac{\sin^2\beta}{\beta^2}\right).
\]
The two center sets coincide for **exactly two** cone shapes: \(t=\beta_1/\pi=0.203033659985\ldots\), where \(\beta_1\in(0,\pi/4)\) is the unique positive solution of \(2\sin(2\beta_1)=3\beta_1\), and \(t=\beta_2/\pi=0.307933823651\ldots\), where \(\beta_2\in(\pi/4,\pi/2)\) is the unique solution of \(2\tan\beta_2=3\beta_2\). At every other \(0<t<1\) the minimax and least-squares center sets are disjoint.

The intrinsic diameter and its sharp comparison with the Chebyshev radius are
\[
 \operatorname{diam}(C_{L,t})=L\max\left\{1,2\sin\frac\beta2\right\},\qquad
 \frac12<\frac{\rho_C}{\operatorname{diam}(C_{L,t})}\le\frac{\sqrt3}{2}.
\]
Equality in the upper bound occurs **if and only if** \(t=1/3\); the lower bound is an unattained infimum approached as \(t\to0^+\) or \(t\to1^-\). This is a sharp cone-family metric covering-to-diameter inequality, not a universal inequality for arbitrary geodesic spaces.

## Assumptions and scope

The physical cone has positive perpendicular height \(L\sqrt{1-t^2}\) and positive base radius \(tL\). Intrinsic paths are constrained to the cone's lateral surface. The source and the farthest target may lie on the apex or rim. In polar coordinates \((r,\theta)\), the metric off the apex is \(ds^2=dr^2+t^2r^2d\theta^2\), with \(0\le r\le L\) and \(\theta\) modulo \(2\pi\). There is no identification of the rim to a point and no base disk. The parameter \(t\) ranges over the entire open interval \((0,1)\); all endpoint equalities for transition values inside this interval are included.

The Fréchet objective averages *squared intrinsic lengths* against normalized surface area. The Chebyshev objective takes a maximum over the whole surface, rather than over a prescribed finite set. A center set is a set of physical surface points, not an ambient Euclidean center inside the solid cone.

## Proof

**1. Exact intrinsic distance.** Choose two surface points at slant radii \(r,s\) and let \(\delta\in[0,\pi]\) be their smaller physical azimuthal separation. Unfolding the cone multiplies the angular separation by \(t\), hence \(t\delta\in[0,\pi t)\subset[0,\pi)\). The planar segment joining the developed representatives stays inside the sector of angle less than \(\pi\), and inside the radius-\(L\) disk by convexity. Thus it gives a surface path of length
\[
 d_0=\sqrt{r^2+s^2-2rs\cos(t\delta)}.
\]
To prove global minimality, lift any competing surface path that avoids the apex to the universal developed plane, with signed total developed angular change \(\gamma=t(\pm\delta+2k\pi)\), \(k\in\mathbb Z\). If \(|\gamma|<\pi\), its Euclidean length is at least the corresponding chord, which is no shorter than \(d_0\), because \(|\gamma|\ge t\delta\) and chord length increases with angular difference up to \(\pi\). If \(|\gamma|\ge\pi\), the path has length at least \(r+s\): in the lifted angular coordinate, cut the path upon first reaching angle \(\operatorname{sgn}(\gamma)\pi/2\) and subsequently reaching \(\gamma-\operatorname{sgn}(\gamma)\pi/2\). The initial and final portions have Euclidean lengths at least \(r\) and \(s\) respectively, and the intermediate portion has nonnegative length. A path through the apex also has length at least \(r+s\). Since \(d_0\le r+s\), no competitor is shorter. For an endpoint at the apex, \(d=r+s\) is immediate. Consequently,
\[
 \boxed{d((r,\theta),(s,\phi))^2=r^2+s^2-2rs\cos(t\delta)}.
\]
This argument covers arbitrary winding, rim contact, the apex, and the complete parameter range \(0<t<1\).

**2. Eccentricity and complete minimax-center locus.** For fixed \(r,s>0\), the squared distance is increasing in \(\delta\in[0,\pi]\), so its maximum occurs at angular separation \(\pi\). For fixed \(r\), the resulting squared distance is a strictly convex quadratic function of the target slant radius \(s\in[0,L]\), hence its maximum occurs at \(s=0\) (the apex) or \(s=L\) (the antipodal point on the rim). This yields the displayed two-barrier formula for \(e_t(r)\).

Put \(c=\cos\beta\) and \(h(r)=\sqrt{r^2+L^2-2rLc}\). If \(0<\beta<\pi/4\), \(h(r)=r\) at \(r_0=L/(2c)\), and \(r_0<Lc\). On \([0,r_0]\), \(e_t=h\) is strictly decreasing; on \([r_0,L]\), \(e_t=r\) is strictly increasing. Therefore \(r_C=r_0\) is the unique minimizing slant radius. If \(\pi/4<\beta<\pi/2\), the strictly convex square of \(h\) has its unique minimum at \(r=Lc\), where \(h(Lc)=L\sin\beta\ge Lc\); thus \(e_t\ge h\ge h(Lc)=e_t(Lc)\). For \(\pi/2\le\beta<\pi\), \(h\) is strictly increasing on \([0,L]\), so its unique minimum is at \(r=0\), which also minimizes \(e_t\). Direct substitution treats \(\beta=\pi/4\) and \(\beta=\pi/2\). Rotational invariance then gives precisely the stated circle or apex as the complete center set.

For \(\beta\le\pi/4\) a minimax center has two kinds of farthest points: the apex and the antipodal rim point. For \(\pi/4<\beta<\pi/2\), only the antipodal rim point is farthest. For \(\beta\ge\pi/2\), the apex is the center and all rim points are farthest.

**3. Intrinsic Fréchet centers.** Normalized area measure on the lateral cone makes the target slant radius \(s\) have density \(2s/L^2\) on \([0,L]\), independently of the uniform physical azimuth. Relative to a fixed source azimuth, the smaller separation \(\delta\) is uniform on \([0,\pi]\). Hence
\[
 \mathbb E[s]=\frac{2L}{3},\quad\mathbb E[s^2]=\frac{L^2}{2},\quad
 \mathbb E[\cos(t\delta)]=\frac{\sin\beta}{\beta}.
\]
Integrating the *exact* distance identity yields
\[
 F_t(r)=r^2+\frac{L^2}{2}-\frac{4rL}{3}\frac{\sin\beta}{\beta}
 =\bigl(r-r_F\bigr)^2+\frac{L^2}{2}-r_F^2.
\]
Since \(0<r_F<2L/3<L\), strict convexity proves that exactly the complete parallel circle of slant radius \(r_F\) minimizes \(F_t\).

**4. Exactly two coincidence angles.** For \(0<\beta\le\pi/4\), equality \(r_F=r_C\) is equivalent to \(\sin(2\beta)/(2\beta)=3/4\). The left side strictly decreases from \(1\) to \(2/\pi<3/4\), giving exactly one root \(\beta_1\). For \(\pi/4\le\beta<\pi/2\), equality is \(\tan\beta/\beta=3/2\). This function strictly increases from \(4/\pi<3/2\) to infinity, giving exactly one root \(\beta_2\). Both monotonicity claims follow respectively from \(\sin x-x\cos x=\int_0^x u\sin u\,du>0\) for \(0<x<\pi\), and \(\beta-\sin\beta\cos\beta>0\) for \(0<\beta<\pi/2\). When \(\beta\ge\pi/2\), \(r_C=0\) but \(r_F>0\), so no further coincidence exists.

**5. Diameter and sharp ratio.** For nonapical points, diameter is attained at maximal angular separation \(\delta=\pi\). The function \(r^2+s^2-2rs\cos\beta\) is convex in \((r,s)\in[0,L]^2\), so its maximum occurs at corners. Comparing apex-to-rim distance \(L\) and antipodal rim-to-rim distance \(2L\sin(\beta/2)\) gives the diameter formula, switching exactly at \(\beta=\pi/3\). Substituting the Chebyshev formula gives
\[
 \frac{\rho_C}{\operatorname{diam}}=
 \begin{cases}
 (2\cos\beta)^{-1},&0<\beta\le\pi/4,\\
 \sin\beta,&\pi/4\le\beta\le\pi/3,\\
 \cos(\beta/2),&\pi/3\le\beta\le\pi/2,\\
 (2\sin(\beta/2))^{-1},&\pi/2\le\beta<\pi.
 \end{cases}
\]
The first two branches increase strictly, the last two decrease strictly. They meet at \(\beta=\pi/3\) with value \(\sqrt3/2\). All interior ratios exceed \(1/2\), approached only at the two degenerate ends.

## Verification

The accompanying pure-Python file `verify_cone_center.py` reconstructs the analytic candidate radii and the distance formula, checks 66 opening ratios (including both internal transitions and near-degenerate cases), numerically maximizes over target grids, tests 2,857,130 counted finite checks, compares direct two-variable quadrature of the area-integrated squared distance with the closed form, and brackets both coincidence angles by bisection. It prints `PASS` with no failures. These finite tests are consistency diagnostics and are not used to establish the statements for all opening ratios. The universal quantifiers, optimization, branch equalities, and uniqueness follow from the above proof.

## Relationship to prior work

The classical developability of cone geodesics, illustrated by Slavík's *Cone Geodesics* (2010) and by the general Clairaut relation, provides the local geometric starting point. Ahn, Barba, Bose, de Carufel, Korman and Oh (2015) study the geodesic minimax center of *simple planar polygons*, a different metric domain with unique center. Aronov, van Kreveld, van Oostrum and Varadarajan (2001 report; published 2003) study facility locations for finite site sets on polyhedral terrains and surfaces. The geodesic-circle exposition at MathCurve describes local circles on cones, not the global all-target optimization. None of those examined statements gives the full finite-cone minimax center locus, its transition values, or the two coincidence angles with intrinsic area Fréchet centers.

The cone's pairwise distance formula and its averaged second-moment integral are elementary consequences of development; those are **not** claimed independently as new. Existing calculations of cone pair-distance energy and of frustum diameters also do not state the complete minimax-center locus or the two center-coincidence angles. The asserted contribution is the **joint complete exact classification** of the intrinsic minimax and least-squares center sets, together with its sharp radius-to-diameter law. A potential earlier unindexed treatment of the same one-center optimization is a residual priority risk.

## Limitations

No claim is made for the closed cone including its base disk, noncircular cones, conical frusta, nonuniform area measures, arbitrary distributions, or arbitrary higher-dimensional cones. The lower diameter-ratio endpoint is not attained by a nondegenerate cone. The root values shown numerically are diagnostic approximations to rigorously defined unique transcendental roots, not algebraic values. The uniqueness and literature comparison are relative to the examined accessible sources; exhaustive historical priority is not established. 

## References

1. Antonín Slavík, *Cone Geodesics*, Wolfram Demonstrations Project (2010): https://demonstrations.wolfram.com/ConeGeodesics/ . Developability and geodesic curves; no one-center optimization presented in the inspected description.
2. Hee-Kap Ahn, Luis Barba, Prosenjit Bose, Jean-Lou de Carufel, Matias Korman, Eunjin Oh, *A linear-time algorithm for the geodesic center of a simple polygon*, arXiv:1501.00561, first submitted 2015-01-03: https://arxiv.org/abs/1501.00561 .
3. Boris Aronov, Marc van Kreveld, René van Oostrum, Kasturi Varadarajan, *Facility Location on Terrains*, Utrecht technical report UU-CS-2001-56 (2001): https://ics-archive.science.uu.nl/research/techreps/repo/CS-2001/2001-56.pdf .
4. *Geodesic Circle of a Surface*, MathCurve, section on the cone of revolution: https://mathcurve.com/courbes3d.gb/cercle_geodesique/cercle_geodesique.shtml .
5. *Clairut’s Relation: Geodesics on Surfaces of Revolution*, originally dated 2010-01-16 (later revised), section on cone geodesics: https://surya-teja.com/2010/01/16/clairuts-relation-geodesics-on-surfaces-of-revolution/ .
