# Unlabeled directional widths determine a right circular cone

## Finding

The full distribution of the length of a uniformly oriented line projection determines every nondegenerate solid right circular cone in three-dimensional Euclidean space up to rigid motion. This remains true without recording the projection directions. A sharp contrast holds for the distribution's support alone: every feasible, noncritical pair of minimum and maximum widths comes from **exactly two** noncongruent circular cones, one broad and one slender.

Here are explicit distribution and reconstruction formulas. Write \(K(r,h)=\operatorname{conv}(\{(x,y,0):x^2+y^2\le r^2\}\cup\{(0,0,h)\})\), with \(r,h>0\), and let \(W\) be the length of its orthogonal projection onto a line with Haar-uniform unoriented direction. Set
\[
k=\frac hr,\quad T=\sqrt{1+k^2},\quad b=\frac{2k}{T},\quad w=\frac sr.
\]
For positive \(w\) away from the finitely many breakpoints, introduce the nonnegative expressions
\[
C_k(w)=\frac{w}{2\sqrt{4-w^2}},\qquad
B_k(w)=\frac{w/\sqrt{T^2-w^2}-k}{T^2},\qquad
A_k(w)=\frac{k+w/\sqrt{T^2-w^2}}{T^2}.
\]
The probability density of \(W/r\) is given *exactly* by the following indicator expression, where \(\mathbf{1}_{I}(w)\) means one if \(w\in I\) and zero otherwise:
\[
g_k(w)=\begin{cases}
C_k(w)\mathbf{1}_{(b,2)}(w)+B_k(w)\mathbf{1}_{(k,b)}(w),&0<k\le1,\\[3pt]
C_k(w)\mathbf{1}_{(b,2)}(w)+B_k(w)\mathbf{1}_{(k,T)}(w)
 +A_k(w)\mathbf{1}_{(b,T)}(w),&k>1.
\end{cases}
\]
Each constituent expression is evaluated **only** when its indicator interval is active. Values of the density at the finitely many interval endpoints are immaterial. The dimensional density is \(f_{r,h}(s)=g_k(s/r)/r\).

The exact support endpoints \(L=\operatorname{ess\,inf}W\) and \(U=\operatorname{ess\,sup}W\) are
\[
(L,U)=\begin{cases}(h,2r),&h/r\le\sqrt3,\\
(2rh/\sqrt{r^2+h^2},\sqrt{r^2+h^2}),&h/r\ge\sqrt3.
\end{cases}
\]
They necessarily satisfy \(U/L\ge 2/\sqrt3\), with equality precisely when \(h/r=\sqrt3\). The lower-edge density distinguishes the branches:
\[
\lim_{s\downarrow L}f_{r,h}(s)
=\begin{cases}0,&h/r<\sqrt3,\\
\displaystyle\frac1r\left(\frac{k}{2}+\frac{k}{k^2-1}\right),&h/r\ge\sqrt3.
\end{cases}
\]
Equivalently, the displayed limit is the intrinsic law statistic \(\lim_{\varepsilon\downarrow0}\mathbb P(L\le W\le L+\varepsilon)/\varepsilon\), because the density has the indicated one-sided limit. Thus no choice of pointwise density representative is involved.

Consequently, whenever this density limit vanishes the unique reconstruction is \((r,h)=(U/2,L)\). Otherwise it is
\[
\boxed{
 r=\frac U{\sqrt2}\sqrt{1-\sqrt{1-(L/U)^2}},\qquad
 h=\frac U{\sqrt2}\sqrt{1+\sqrt{1-(L/U)^2}}.
}
\]
In particular the full unlabeled projection-width law is injective on the family of solid right circular cones.

If only the endpoints \((L,U)\) are retained, every feasible pair \(0<L<U\) with \(U/L>2/\sqrt3\) has *exactly two* realizations: the broad cone \((r,h)=(U/2,L)\) and the slender cone displayed in the boxed formula. Their width laws differ at the lower edge. At the boundary \(U/L=2/\sqrt3\), these two realizations coincide and are the only one.

## Assumptions and scope

The cone is the **solid convex hull of a filled circular disk and an apex directly above its center**, not a hollow surface or an infinite cone. Radius and altitude are positive, measured in one common Euclidean length unit. Direction is Haar-uniform on unoriented lines in \(\mathbb R^3\); no directional labels are observed. The distribution and uniqueness statements hold for **every** pair \(r,h>0\), including \(h/r=1\) and \(h/r=\sqrt3\). The density is an almost-everywhere density; removable choices at transition points do not change the law. No claim about arbitrary convex bodies, oblique cones, or higher-dimensional cones is made.

## Proof

**1. Direction reduction and support.** By rotational and reflection symmetry the absolute axial cosine \(z=|u_3|\) for a Haar-uniform unit vector \(u\) is uniform on \([0,1]\). The support of the base disk in transverse direction \(u\) is \(r\sqrt{1-z^2}\). In the axial positive direction, the apex contributes \(hz\) to the maximum support value, while the opposite support value is always that of the base. Therefore, writing \(a=\sqrt{1-z^2}\),
\[
\frac{W(z)}r=a+\max(a,kz).
\]
The competing supports switch at \(z_0=1/T\), giving
\[
\frac{W(z)}r=\begin{cases}
2\sqrt{1-z^2},&0\le z\le z_0,\\
\sqrt{1-z^2}+kz,&z_0\le z\le1.
\end{cases}
\tag{1}
\]
At \(z_0\) the common value is \(b=2k/T\). The first branch strictly decreases from \(2\) to \(b\). The derivative of the second is \(k-z/\sqrt{1-z^2}\). For \(k\le1\) it is nonpositive throughout its interval (strict except possibly at the junction). For \(k>1\) the second branch rises to its unique peak \(T\) at \(z_m=k/T\), then descends to \(k\) at \(z=1\).

**2. Exact change of variables.** The first branch has inverse \(z=\sqrt{1-w^2/4}\) on \(b<w<2\). Since \(z\) is uniform, its absolute inverse derivative is \(C_k(w)\). Solving \(w=\sqrt{1-z^2}+kz\) gives the two algebraic inverse branches
\[
z_\pm(w)=\frac{kw\pm\sqrt{T^2-w^2}}{T^2}.
\]
The descending branch \(z_+(w)\) has inverse-Jacobian \(-z_+'(w)=B_k(w)\), on \(k<w<b\) if \(k\le1\), or on \(k<w<T\) if \(k>1\). When \(k>1\), the ascending branch \(z_-(w)\) contributes \(z_-'(w)=A_k(w)\) for \(b<w<T\). These are the *only* monotone pieces of (1), so summing inverse Jacobians gives the stated exact density without omissions, even when their image intervals overlap. Since the three source intervals partition \([0,1]\), the density integrates to one; branch junctions carry no atoms.

**3. Sharp support transition.** The only candidate global minima in (1) are the endpoint values \(2\), \(k\), and the junction value \(b\); the possible interior stationary point is a maximum. For \(k\le\sqrt3\) the global minimum is \(k\), and for \(k\ge\sqrt3\) it is \(b\), because \(b<k\) precisely when \(T>2\). The global maximum is \(2\) when \(T\le2\) and \(T\) when \(T\ge2\). Rescaling gives the two endpoint formulas. In the broad regime \(U/L=2/k\ge2/\sqrt3\); in the slender regime \(U/L=(k+1/k)/2\ge2/\sqrt3\), with the latter inequality strict for \(k>\sqrt3\). Both meet at the critical ratio.

**4. Edge behavior and inverse uniqueness.** For \(k<\sqrt3\), the sole preimage of the minimum \(w=k\) is the axial endpoint \(z=1\). The descending-branch Jacobian \(B_k(w)\) tends to zero as \(w\downarrow k\), while all other branch images begin strictly above \(k\). Thus the density tends to zero. For \(k\ge\sqrt3\), the minimum is the transverse/apical-support switch \(w=b\), and the two immediately active branch contributions are the disk term and the ascending-apex term. Direct substitution at \(b\) yields
\[
 C_k(b+)=\frac k2,\qquad A_k(b+)=\frac{k}{k^2-1}.
\]
There is no third positive contribution at this edge: for \(k>\sqrt3\) the descending apex starts later at \(w=k>b\), and for equality its inverse Jacobian vanishes at \(w=k=b\). Therefore the asserted positive density limit is exact. The two regimes can be read off from the distribution itself, so there is no prior information about aspect ratio in the reconstruction.

In the zero-limit case the support equations immediately give \(h=L\), \(r=U/2\). In the positive-limit case, solve
\[
r^2+h^2=U^2,\qquad 2rh=LU.
\]
The quadratic whose roots are \(r^2,h^2\) gives precisely the boxed formula, choosing the larger root for \(h^2\) since \(k\ge\sqrt3\). The resulting dimensions determine congruence. Finally, for each strict feasible ratio the two formulas produce one \(k<\sqrt3\) and one \(k>\sqrt3\); each reproduces the same endpoints and these exhaust the cases. At criticality the roots correspond to the same cone. This proves both the injectivity of the full law and the sharp two-to-one ambiguity of endpoints alone.

## Verification

The standalone script `verify.py` implements the geometric support function, its piecewise inverse-image cumulative distribution, its exact density, and both reconstruction branches using only Python's standard library. Run `python3 verify.py` from the directory containing this document. It uses 35 aspect ratios (including both critical ratios and near-critical perturbations), independently enumerates 180001 evenly spaced axial cosines per ratio, compares the resulting empirical CDF to the exact analytic inverse-image formula, checks density by numerical differentiation away from breakpoints, and checks both inverse solutions and exact support endpoints. Its recorded run completed **11140 finite checks**, printing `VERIFY_OK`. These computations test explicit formulas; they are not substitutes for the all-parameter analytic argument above.

## Relationship to prior work

Kim, Yaskin and Zvavitch (2015, arXiv:1512.07289v1) study geometric tomography when the distribution of sizes of central sections or hyperplane projections is known but the orientation labels have been discarded. Their general nonuniqueness results motivate asking whether a natural restricted convex-body family admits a sharp inverse law. Their stated projection observable is the area of a *two-dimensional hyperplane projection* in \(\mathbb R^3\), not the *one-dimensional line-projection length* studied here; their inspected full manuscript contains no right-circular-cone width density or corresponding reconstruction theorem. Pennell and Deignan (1989) compute a cone's two-dimensional projected area for a given direction, another distinct observable. Vickers and Brown (2001) address the distribution of projected *planar area and perimeter* of convex particles including cones. Their abstract does not state an unlabeled **line-width** inverse theorem; their full paper was not available for a definitive comparison. The present result claims only the explicit one-dimensional width law, the all-aspect-ratio inverse rule, and the sharp endpoints-only ambiguity; elementary support identities and known two-dimensional projection results are not asserted to be new.

## Limitations

The family must be a solid, right, circular cone with positive radius and height; the argument uses its axial symmetry. The proof is specific to three-dimensional uniform random directions. Observing only extremal widths loses the cone shape except at the critical ratio. The density distinction is exact and requires the ideal mathematical distribution, not a finite sample or a noisy density estimate; no statistical reconstruction rate is proved. Historical coverage remains uncertain because the potentially relevant full text of Vickers and Brown (2001), on different planar observables, could not be examined. An unlocated equivalent width-density derivation would limit originality, independently of the proved identities.

## References

1. Jaegil Kim, Vladyslav Yaskin, Artem Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, public 2015-12-22, https://arxiv.org/abs/1512.07289v1 .
2. S. Pennell, J. Deignan, *Computing the Projected Area of a Cone*, SIAM Review **31** (1989), 299–302, DOI:10.1137/1031052 .
3. G. T. Vickers, D. J. Brown, *The Distribution of Projected Area and Perimeter of Convex, Solid Particles*, Proceedings of the Royal Society A **457** (2001), 283–306, DOI:10.1098/rspa.2000.0667 .
