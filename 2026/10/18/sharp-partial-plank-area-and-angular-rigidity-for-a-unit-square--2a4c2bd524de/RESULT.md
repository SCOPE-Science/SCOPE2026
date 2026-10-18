# Sharp partial-plank area and angular rigidity for a unit square

## Finding

Let \(Q=[-1/2,1/2]^2\). A **plank** of Euclidean width \(w>0\) is a set \(P(u,t,w)=\{x\in\mathbb R^2:|u\cdot x-t|\le w/2\}\), with \(u\in S^1\). For \(0<W<1\), define
\[
M(W)=\sup\left\{\operatorname{area}\left(Q\cap\bigcup_{i=1}^m P(u_i,t_i,w_i)\right):m\ge1,\ w_i>0,\ \sum_iw_i\le W\right\}.
\]
The following sharp formula and contact-direction transition hold:
\[
\boxed{M(W)=\begin{cases}
\sqrt2W-W^2/2,&0<W\le1/\sqrt2,\\
(1+W^2)/2,&1/\sqrt2\le W<1.
\end{cases}}
\]
At every \(W\), a **single central plank** realizes the maximum. Up to reflections and coordinate interchange, its unit normal is \(u=(\cos\theta,\sin\theta)\) with
\[
\boxed{\theta(W)=\begin{cases}
\pi/4,&0<W\le1/\sqrt2,\\
\pi/4-\arccos\!\bigl(1/(\sqrt2 W)\bigr),&1/\sqrt2<W<1.
\end{cases}}
\]
For a single plank this normal, up to square symmetries and reversal, and the central offset are necessary for maximizing its covered area. The change of optimal normal occurs exactly when the best covered fraction passes \(3/4\).

There is also a **family-level angular rigidity inequality**. For any finite family whose total width is exactly \(W\), set
\[
q_i=(|u_{i1}|,|u_{i2}|),\quad a=\sum_iw_i|u_{i1}|,\quad b=\sum_iw_i|u_{i2}|,
\quad \Delta=\sum_{i<j}w_iw_j\|q_i-q_j\|_2^2.
\]
Then \(\Delta=W^2-a^2-b^2\ge0\). Writing \(C\) for the square area covered by the family, one has
\[
M(W)-C\ge\begin{cases}
\frac12\bigl[\Delta+(\sqrt2 W-a-b)(2-\sqrt2 W-a-b)\bigr],&0<W\le1/\sqrt2,\\
\frac12\bigl[\Delta+(1-a-b)^2\bigr],&1/\sqrt2\le W<1.
\end{cases}
\]
In particular, \(M(W)-C\ge\Delta/2\). Thus every nearly optimal family must concentrate its width-weighted absolute normal-coordinate vectors; the inequality does not assert that arbitrary multi-plank extremizers are uniquely parallel.

Equivalently, the minimum total plank width for covering a target area \(c\in(0,1)\) of \(Q\) is
\[
W_{\min}(c)=\begin{cases}
\sqrt2-\sqrt{2-2c},&0<c\le3/4,\\
\sqrt{2c-1},&3/4\le c<1.
\end{cases}
\]

## Assumptions and scope

All areas are ordinary planar Lebesgue areas. Plank directions and offsets are unrestricted, and families are finite but have no bound on the number of planks. The admissible budget is \(0<W<1\), where the side length and minimum width of the square are both \(1\). Boundary choices (open versus closed planks) do not change area. Rigidity inequalities use **exact** total width \(W\); the extremal formula allows total width at most \(W\). No claim is made about uniqueness of arbitrary families of more than one plank.

## Proof

**1. A measured uncovered core for every plank family.** Write \(v_i=(w_i/2)u_i\), and let \(Z=\sum_i[-v_i,v_i]\) be the Minkowski sum of the centered segments. The Bang-map bound for plank families gives
\[
\operatorname{area}\left(Q\setminus\bigcup_iP_i\right)\ge \operatorname{area}(Q\ominus Z),
\]
where \(Q\ominus Z=\{x:x+Z\subset Q\}\). For completeness, the underlying area-preservation argument is reconstructed here. For each sign vector \(\varepsilon\in\{-1,1\}^m\), put \(z_\varepsilon=\sum_i\varepsilon_i v_i\) and choose, for a given \(x\), a lexicographically first maximizer of
\[
\Phi_x(\varepsilon)=\|x+z_\varepsilon\|^2-2\sum_i\varepsilon_i\|v_i\|t_i.
\]
Write \(F(x)=x+z_{\varepsilon(x)}\). Comparing a maximizing sign vector with the vector obtained by flipping its \(j\)-th sign gives
\[
\varepsilon_j\bigl(u_j\cdot F(x)-t_j\bigr)\ge w_j/2.
\]
Thus \(F(x)\) belongs to the complement of every *open* plank. The regions associated with distinct maximizing sign vectors map into disjoint sign-separated regions; on each measurable region the map is a translation. Therefore \(F\) is injective and preserves area. Moreover, for \(x\in Q\ominus Z\), every signed sum \(z_\varepsilon\) belongs to \(Z\), so \(F(x)\in Q\). The inequality follows; replacing open planks by closed ones does not alter area.

Since \(Q\) is a coordinate square and \(Z\) has coordinate halfwidths \(a/2\) and \(b/2\),
\[
Q\ominus Z=[-(1-a)/2,(1-a)/2]\times[-(1-b)/2,(1-b)/2].
\]
Here \(0\le a,b\le\sum_iw_i\le W<1\), so its area is \((1-a)(1-b)\). Consequently
\[
\boxed{C\le a+b-ab.}\tag{1}
\]
This is a direction-sensitive strengthening, for the square, of the general Bang-map reduction underlying Bakaev and Polyanskii's partial-cover theorem.

**2. Optimization and rigidity.** First suppose \(\sum_iw_i=W\). Each \(q_i\) lies on the unit circle in the first quadrant. Hence, with \(s=a+b\),
\[
\rho^2:=a^2+b^2=\left\|\sum_iw_iq_i\right\|^2\le W^2,
\qquad s\le\sqrt2\rho\le\sqrt2W.
\]
Expanding the norm gives the exact identity
\[
W^2-\rho^2=\sum_{i<j}w_iw_j\|q_i-q_j\|^2=\Delta.
\]
The elementary identity
\[
a+b-ab=\frac{1+\rho^2-(1-s)^2}{2}\tag{2}
\]
now yields two regimes. If \(W\le1/\sqrt2\), then \(s\le\sqrt2W\le1\), and subtracting (1)–(2) from \(\sqrt2W-W^2/2\) gives
\[
M_{\mathrm{cand}}(W)-C\ge\frac{\Delta+(\sqrt2W-s)(2-\sqrt2W-s)}2\ge0.
\]
If \(W\ge1/\sqrt2\), then (1)–(2) immediately imply
\[
\frac{1+W^2}{2}-C\ge\frac{\Delta+(1-s)^2}{2}\ge0.
\]
All stated rigidity estimates follow. If a family has total width \(T<W\), the same inequalities with \(T\) give \(C\le M_{\mathrm{cand}}(T)<M_{\mathrm{cand}}(W)\), because both candidate branches are strictly increasing on their assigned intervals.

**3. Exact attainment by a central strip.** Let \(u=(\alpha,\beta)\), where \(\alpha\ge\beta>0\) and \(\alpha^2+\beta^2=1\). For the centered strip \(P(u,0,W)\), the projection of a point uniformly sampled from \(Q\) is the sum of independent uniforms on intervals of lengths \(\alpha\) and \(\beta\). Its density is even, has a constant middle portion, and then decreases linearly. If
\[
\alpha-\beta\le W\le\alpha+\beta,
\]
the uncovered square area is exactly the area of the two triangular projection tails:
\[
\boxed{1-C=\frac{(\alpha+\beta-W)^2}{4\alpha\beta}.}\tag{3}
\]
For \(0<W\le1/\sqrt2\), choose \(\alpha=\beta=1/\sqrt2\), which satisfies the displayed range and makes (3) equal \((1-\sqrt2W)^2\); hence \(C=\sqrt2W-W^2/2\).

For \(1/\sqrt2\le W<1\), put \(r=\sqrt{2W^2-1}\) and take
\[
\alpha=\frac{1+r}{2W},\qquad \beta=\frac{1-r}{2W}.
\]
They satisfy \(\alpha^2+\beta^2=1\), \(\alpha+\beta=1/W\), and \(\alpha-\beta=r/W\le W\), while \(W\le\alpha+\beta\). Formula (3) therefore gives \(1-C=(1-W^2)/2\), so \(C=(1+W^2)/2\). This matches the global upper bound in each regime.

**4. Single-strip angular and central-offset uniqueness.** For a central plank, the upper-bound equality identities in part 2 with a single \(q_1\) force \(s=\sqrt2W\) in the first regime and \(s=1\) in the second. The first condition says \(\alpha=\beta\), while the second says \(\alpha+\beta=1/W\). Together with \(\alpha^2+\beta^2=1\), these characterize the stated angles, up to symmetries. At those angles \(W>\alpha-\beta\) and \(W<\alpha+\beta\). The density of the projection variable is even, constant only on its middle plateau, and strictly decreasing outside it. Sliding a length-\(W\) projection interval away from the origin therefore strictly decreases its mass; so the unique maximizing offset is \(t=0\). The two area branches coincide at \(W=1/\sqrt2\), with value \(3/4\), and both strictly increase. Inverting the branches proves the width-versus-coverage formula.

## Verification

The standalone script `checks/verify.py` checks five exact SymPy identities for the upper bounds, dispersion, and wide-regime contact configuration. It independently constructs actual planar strip–square intersection polygons with Shapely to check the predicted optimal areas at 49 widths, and tests the global bound plus dispersion identity on 340 pseudorandom multi-plank families and 340 separate single-plank configurations. It returned `VERIFY_OK symbolic_identities=5 attaining_directions=49 families=340 random_single_planks=340`. The analytic argument above, especially the area-preserving Bang map, establishes the result for **all** finite families; finite numerical trials are not treated as a proof.

## Relationship to prior work

Bakaev and Polyanskii's 2026 theorem proves that for every planar convex body there exists an optimal partial-plank covering using a single plank. Their Lemma 5 supplies the Bang-map uncovered-volume principle used here; it does not state the complete square-specific optimal area function, its unique optimal direction transition, the exact inverse coverage-width profile, or the quantitative dispersion bound for arbitrary families. The present contribution concerns those stronger square-specific statements, not the general planar one-plank existence theorem. The plank-covering stability literature deals with covering an annulus or controlling overlap under near-complete coverage, rather than the sharp fixed-budget square-area profile. Comparisons of accessible research records and keyword/implication searches found no directly covering statement, but search incompleteness and earlier unindexed work remain possible.

## Limitations

The formula is proved for a Euclidean unit square, not arbitrary rectangles or higher-dimensional cubes. The weighted dispersion uses absolute normal-coordinate vectors: it does not force actual unoriented plank directions to be identical when the covered-area deficit is small, and it does not classify all optimal multi-plank families. No independent historical-priority or external scientific audit is asserted.

## References

1. E. Bakaev and A. Polyanskii, *Optimal partial plank coverings*, arXiv:2607.27483, first posted July 29, 2026, https://arxiv.org/abs/2607.27483. Relevant: Section 2, Lemma 5 and Section 4, Theorem 12.
2. E. Bakaev and A. Yehudayoff, *Volume stability of plank covers*, arXiv:2609.30409, first posted September 24, 2026, https://arxiv.org/abs/2609.30409. Relevant: stability for covering rather than optimal partial square-area profiles.
