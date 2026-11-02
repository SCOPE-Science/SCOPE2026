# Three even interpoint-distance moments reconstruct a solid right circular cone

## Finding
Let \(C(R,H)\subset\mathbb R^3\) be the **solid** right circular cone with base radius \(R>0\) and perpendicular height \(H>0\). Sample \(X,Y\) independently and uniformly by three-dimensional volume from \(C(R,H)\), and put \(D=\|X-Y\|_2\). The three scalar observations
\[
M_1=\mathbb E D^2,\qquad M_2=\mathbb E D^4,\qquad M_3=\mathbb E D^6
\]
uniquely determine \(R,H\), hence the cone up to Euclidean congruence. Three is the smallest number of *consecutive even distance moments* that works for every positive aspect ratio.

There is an exact phase classification for the first two observations. Define \(q=M_2/M_1^2\) and \(r=H^2/R^2\). All physically attainable \(q\) satisfy
\[
\frac{6260}{4137}\le q<\frac{64}{21}.
\]
For \(6260/4137<q<113/63\), precisely two noncongruent cones give the same first two moments. At \(q=6260/4137\) and for \(113/63\le q<64/21\), the first two moments already identify the cone uniquely. Thus the two-to-one regime and its two thresholds are sharp.

## Assumptions and scope
The base is a filled Euclidean disk, the apex lies on its perpendicular central axis, and the cone includes its whole interior. The apex, base, and boundary have sampling probability zero. No orientations, point coordinates, signed differences, volume or projection measurements are supplied: only the exact *population* second, fourth and sixth powers of interpoint Euclidean distance. Distances are not intrinsic paths along the cone surface. All parameters \(R,H\) are strictly positive; flattened or infinitely tall limiting shapes do not count as cones in the theorem.

## Proof
**1. Exact moment formula.** Place the apex at the origin and the base at axial height \(H\). A volume-uniform point has the independent representation
\[
Z=(RSU_1,RSU_2,HS),
\qquad f_S(s)=3s^2\ \ (0<s<1),
\]
where \(U=(U_1,U_2)\) is area-uniform on the unit disk. For an independent pair \((S,U),(T,V)\), write \(A=R^2\), \(B=H^2\), \(J=\|SU-TV\|^2\), and \(Q=(S-T)^2\). Then \(D^2=AJ+BQ\). Conditional on \(S=s,T=t\), direct angular and radial integration over the two independent unit disks gives
\[
\begin{aligned}
\mathbb E[J\mid s,t]&=(s^2+t^2)/2,\\
\mathbb E[J^2\mid s,t]&=(s^4+t^4)/3+s^2t^2,\\
\mathbb E[J^3\mid s,t]&=(s^6+t^6)/4+3(s^4t^2+s^2t^4)/2.
\end{aligned}
\]
Expanding \((AJ+BQ)^k\) for \(k=1,2,3\), multiplying by the joint axial density \(9s^2t^2\), and integrating \(0<s,t<1\) yields the exact rational polynomials
\[
\boxed{M_1=\frac{3}{40}(8A+B)},
\]
\[
\boxed{M_2=\frac{226A^2+27AB+6B^2}{350}},
\]
\[
\boxed{M_3=\frac{788A^3+83A^2B+21AB^2+5B^3}{840}}.
\]
Every integral here is a finite integral of a polynomial, with \(\int_0^1s^j\,ds=1/(j+1)\); the supplied checker performs this expansion independently using exact rational arithmetic.

**2. First-two-moment inversion and sharp ambiguity.** Let \(r=B/A>0\). Normalizing by \(M_1\) eliminates overall scale:
\[
q=\frac{M_2}{M_1^2}=\frac{32}{63}\,F_2(r),\qquad
F_2(r)=\frac{226+27r+6r^2}{(r+8)^2}.
\]
Differentiation gives \(F_2'(r)=(69r-236)/(r+8)^3\). Therefore \(F_2\) strictly decreases to its unique minimum at \(r_*=236/69\), then strictly increases. Its values at that minimum, the excluded flat limit \(r\downarrow0\), and the excluded needle limit \(r\to\infty\) give respectively \(q_*=6260/4137\), \(q_0=113/63\), and \(q_\infty=64/21\). The claimed one-versus-two preimage classification follows by monotonicity, keeping both endpoints \(r=0,\infty\) excluded.

For any two positive ratios \(r,u\), the equality \(F_2(r)=F_2(u)\) is equivalent to either \(r=u\), or
\[
69ru+158(r+u)-1888=0,
\qquad
u=\frac{2(944-79r)}{69r+158}.
\]
When the latter expression gives a distinct positive \(u\), fixing \(M_1\) sets \(A=40M_1/[3(8+r)]\) and \(B=rA\), generating the two genuine cones with identical \(M_1,M_2\). For instance, the pair \(r=1\) and \(u=1730/227\), at matched \(M_1\), supplies a strict two-moment counterexample. This proves global necessity of a third even moment.

**3. The sixth moment separates the two branches.** Set
\[
F_3(r)=\frac{788+83r+21r^2+5r^3}{(r+8)^3},
\qquad
\frac{M_3}{M_1^3}=\frac{1600}{567}F_3(r).
\]
An exact polynomial identity, valid whenever \(u=2(944-79r)/(69r+158)\), is
\[
F_3(r)-F_3(u)
=\frac{3(69r-236)\left(224479r^2-1356188r+3036792\right)}{30581492(r+8)^3}.
\]
The displayed quadratic is strictly positive for all real \(r\): its leading coefficient is positive and its discriminant is \(-887538234128<0\). The right-hand side is consequently zero exactly at \(r=236/69\), when \(u=r\); for every *distinct* positive pair of first-two-moment alternatives, the third moments differ. Thus \((M_1,M_2,M_3)\) is globally injective in \((R,H)\), as asserted. A constructive inverse solves the scalar equation for \(F_2\), keeps positive candidates, uses \(F_3\) to select one, then sets \(R=\sqrt{40M_1/[3(8+r)]}\) and \(H=R\sqrt r\).

## Verification
The standalone, standard-library Python 3 program `verify.py` exactly re-integrates the three moments with rational coefficients, verifies the two-branch algebra and the strictly positive discriminant certificate, constructs a distinct-cone equal-two-moment example, and simulates genuinely independent volume-uniform point pairs at three different aspect ratios. Executing `python3 verify.py` in the package directory prints `ALL_CHECKS_PASSED`. Exact polynomial identities and the analytic proof establish the infinite statements; simulations are only independent numerical checks.

## Relationship to prior work
Bonnet–Gusakova–Thäle–Zaporozhets (arXiv:2010.03351, originally submitted 2020-10-07) prove sharp mean-*distance* inequalities for convex bodies and give a universal integral representation for distance powers. These broad forward identities apply to cones but do not give the present explicit low-order cone polynomials, the inverse aspect-ratio phase diagram, or global three-moment injectivity. Bäsel (arXiv:2101.03815) analyzes distance moments within regular *planar polygons*, a different family and dimension. Mémoli–Needham (arXiv:1810.09646) frame the general challenge of recovering shapes from distance distributions; this result settles a finite-moment subproblem for solid circular cones.

A previously published analysis of the **direction-unlabeled projection widths** of a right circular cone reconstructs cone parameters from a different random observable; it cannot imply the interpoint-moment formulas. Known exact moment reconstructions for cylinders and ellipsoids likewise assume different sampling solids and do not specialize to a cone. The novelty assertion concerns the stated three-dimensional solid-cone inverse and sharp two-moment phase diagram, not generic moment calculus, the second-moment inertia identity, or the broad distance-inversion program.

## Limitations
These results assume known uniform volume sampling and exact population moments. They do not give confidence intervals from finitely many distances, noise-robust error constants, recovery of noncircular/oblique cones, or uniqueness among arbitrary convex bodies. No assertion is made that the full source literature on all historical cone integral formulas is exhausted; an older equivalent exact inverse result remains a residual priority risk. The proof is mathematical and includes finite rational calculations reproducible from the supplied program; no independent external audit is claimed.

## References
1. G. Bonnet, A. Gusakova, C. Thäle, and D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351 (first public 2020-10-07), https://arxiv.org/abs/2010.03351.
2. U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815 (first public 2021-01-11), https://arxiv.org/abs/2101.03815.
3. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646 (first public 2018-10-23), https://arxiv.org/abs/1810.09646.
4. *Unlabeled directional widths determine a right circular cone*, published-finding corpus research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-unlabeled-directional-widths-determine-a-right-circular-cone--30a3b32d19eb.
5. *A sharp beta stochastic bound for difference-body distances*, published-finding corpus research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-sharp-beta-stochastic-bound-for-difference-body-distances--4609b4d88176.
