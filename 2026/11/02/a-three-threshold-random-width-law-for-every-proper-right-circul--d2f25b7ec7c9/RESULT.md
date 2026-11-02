# A three-threshold random-width law for every proper right circular frustum

## Finding

For a solid right circular frustum with unequal positive radii \(R>r>0\) and height \(h>0\), the entire law of its width in a uniformly random line direction is given explicitly below. Its directional-width geometry undergoes **three different and sharp height thresholds**
\[
H_1=(R-r)(R+r),\qquad H_2=(R-r)(3R+r),\qquad H_3=(R+r)(3R-r).
\]
These are strictly ordered: \(H_1<H_2<H_3\). At \(h^2=H_1\), an interior cusp minimum and a separate smooth local maximum first appear; at \(h^2=H_2\), the global maximum switches between transverse and oblique directions; at \(h^2=H_3\), the global minimum switches between the axial and cusp directions. In particular the two global-extremum transitions are separated by \(H_3-H_2=4Rr>0\), while they merge in the zero-small-radius cone limit.

Put \(D=R-r\), \(S=R+r\), \(\theta_0=\arctan(D/h)\), \(t_0=\sin\theta_0\), \(\alpha=\arctan(h/S)\), \(L=\sqrt{S^2+h^2}\), and \(w_0=2R\cos\theta_0\). Let \(W\) be the length of the orthogonal projection of the frustum onto an unoriented Haar-uniform line. For \(z\in\mathbb R\), its exact cumulative distribution function is \(F_W(z)=A(z)+B(z)\), with
\[
A(z)=\begin{cases}0&z<w_0,\\t_0-\sqrt{1-z^2/(4R^2)}&w_0\le z<2R,\\t_0&z\ge2R,\end{cases}
\]
and, writing \(\delta(z)=\arccos(z/L)\) when \(0<z<L\),
\[
B(z)=\begin{cases}
0&z\le0,\\
\left[\sin(\alpha-\delta(z))-t_0\right]_+
+\mathbf1_{\alpha+\delta(z)<\pi/2}\left[1-\sin(\max\{\theta_0,\alpha+\delta(z)\})\right]_+&0<z<L,\\
1-t_0&z\ge L,
\end{cases}
\]
where \([x]_+=\max\{x,0\}\). The formula is valid at all three transition heights; it specifies the full law, not merely moments or a finite catalogue of directions.

The exact essential support endpoints and mean are
\[
\operatorname{ess\,inf}W=\min\{h,w_0\},\qquad
\operatorname{ess\,sup}W=\max\{2R,L\},
\]
\[
\boxed{\mathbb EW=\frac\pi4(R+r)+\frac h2+\frac{R-r}{2}\arctan\!\frac{R-r}{h}.}
\]
In the phase \(h^2>H_1\), the direction-profile additionally has a genuine interior local minimum at \(\theta=\theta_0\), and an interior smooth local maximum at \(\theta=\alpha\). At equality \(h^2=H_1\) these stationary configurations meet at their junction and are not two distinct interior extrema. At \(h^2=H_2\) both maximum locations have the same value; at \(h^2=H_3\) both minimum locations have the same value.

## Assumptions and scope

The compact convex body is the convex hull of two parallel **filled** disks, with common axis, larger radius \(R\) at axial coordinate zero, smaller radius \(r\) at axial coordinate \(h\), and \(R>r>0\), \(h>0\). The random direction is uniform over unoriented Euclidean lines in three dimensions. Width is the length of the one-dimensional orthogonal projection onto that line; it is not the area of an orthogonal planar shadow. The exact distribution has no point masses. All extrema refer to directions (not spatial points). The proper-frustum restriction excludes the cone and cylinder endpoints, which are discussed only as limiting comparisons.

## Proof

**Support reduction and measure.** For a unit direction with absolute axial cosine \(t=|u_3|\), the transverse cosine is \(\sqrt{1-t^2}\). Since the convex hull support is the maximum of the supports of its two end disks, and the rim at height zero always supplies the smaller support in the opposite orientation, subtraction of opposite supports gives
\[
W(t)=\max\left\{2R\sqrt{1-t^2},\;S\sqrt{1-t^2}+ht\right\}.\tag{1}
\]
The axial sign can be reversed without changing this width. Haar probability on the sphere gives \(t\sim\mathrm{Uniform}[0,1]\). Put \(t=\sin\theta\) with \(0\le\theta\le\pi/2\). The two supports in (1) cross at \(D\cos\theta=h\sin\theta\), hence \(\theta=\theta_0\), where \(t_0=\sin\theta_0\). Consequently
\[
W(\sin\theta)=\begin{cases}2R\cos\theta,&0\le\theta\le\theta_0,\\S\cos\theta+h\sin\theta=L\cos(\theta-\alpha),&\theta_0\le\theta\le\pi/2.\end{cases}\tag{2}
\]

**Complete cumulative law.** The first profile in (2) is decreasing. Its sublevel interval in \(t\in[0,t_0]\) has uniform measure \(A(z)\), as written above. On the second profile, when \(0<z<L\), the inequality \(L\cos(\theta-\alpha)\le z\) is equivalent on \([0,\pi/2]\) to \(\theta\le\alpha-\delta(z)\) or \(\theta\ge\alpha+\delta(z)\). Intersecting these two intervals with \([\theta_0,\pi/2]\) and converting their lengths into \(t\)-measure via \(\int\cos\theta\,d\theta=\sin\theta\) gives exactly the two terms in \(B(z)\). At \(z\le0\) the second sublevel set is empty, and at \(z\ge L\) it fills the interval. Since the pieces of \([0,1]\) partition the full Haar parameter domain, this proves the CDF in every regime, with no omitted orientations.

**Three distinct bifurcations.** The first branch in (2) strictly decreases. The second is a shifted cosine, with stationary maximum at \(\theta=\alpha\). This point lies strictly beyond the junction iff \(\alpha>\theta_0\), equivalently \(h^2>DS=H_1\). If this holds, the branch derivative is strictly positive just beyond the junction, while the first derivative is negative just before it; the junction is a strict cusp minimum. Otherwise the full profile is nonincreasing. The global maximum of (2) can therefore only be \(2R\) or \(L\); these exchange order precisely at \(L^2=4R^2\), equivalent to \(h^2=D(3R+r)=H_2\). When \(h^2\le H_1\), the unattained formal peak \(L\) is already strictly below \(2R\), so this comparison remains valid. The global minimum can only be the endpoint value \(h\) or the cusp value \(w_0=2Rh/\sqrt{h^2+D^2}\); these exchange order precisely at \(h^2+D^2=4R^2\), equivalent to \(h^2=S(3R-r)=H_3\). Below \(H_1\) the cusp is just a junction, but its value is still above \(h\), so the comparison again remains valid. Finally
\[
H_2-H_1=2RD>0,\qquad H_3-H_2=4Rr>0,
\]
so all three thresholds are strictly distinct for every proper frustum. The equality directions and absence of additional extrema follow from strict monotonicity on the indicated intervals.

**Expectation.** Integrating (2) against the uniform \(t\)-law yields
\[
\mathbb EW=\int_0^{t_0}2R\sqrt{1-t^2}\,dt+\int_{t_0}^1\left(S\sqrt{1-t^2}+ht\right)dt.
\]
Using \(\int\sqrt{1-t^2}\,dt=(t\sqrt{1-t^2}+\arcsin t)/2\), \(t_0=D/\sqrt{h^2+D^2}\), and \(\sqrt{1-t_0^2}=h/\sqrt{h^2+D^2}\), the algebra simplifies to \(\pi S/4+h/2+(D/2)\arctan(D/h)\). This completes the proof.

## Verification

`verify.py` evaluates (1) on a deterministic, dense parameter grid, compares empirical sublevel proportions with the independent inverse-interval CDF above across 150 levels per parameter set, and verifies exact support-endpoint phase rules and the mean by numerical quadrature. The finite checks include parameter values in every phase, near cylinder and near cone, and near transition heights. Run `python3 verify.py` with Python 3 and NumPy. These checks are corroborative only: the complete continuum proof is the support and monotonicity argument above.

## Relationship to prior work

Finch (2011, arXiv:1111.4976v1) studies widths and moments of regular simplices, establishing the relevance of random line widths but not treating circular frusta. Kim, Yaskin and Zvavitch (2015, arXiv:1512.07289v1) study distributions of central-section and **hyperplane-projection areas**, not one-dimensional line-projection widths of a right frustum. A published 2026 study of the full random line-width law of a solid right circular **cone** (see reference 3) gives a lower-dimensional boundary case where the smaller radius is exactly zero: it does not determine the strict positive-radius frustum CDF or its two separated global-extremum thresholds. The current contribution is the complete proper-frustum directional-width law and its sharp three-threshold geometry. Elementary support-function calculus and the prior cone result are not claimed as new.

## Limitations

The statement is for right circular solid frusta in three dimensions with strictly positive unequal rim radii, and uniformly random line directions. It does not treat oblique frusta, planar shadow area, arbitrary convex solids, statistical estimation from finite samples, or all directions jointly. The new result uses elementary analytic machinery, and historical uniqueness is not proved by the absence of a search hit: a previously unindexed frustum-width calculation may exist. An accessible older article on distributions of projected **area and perimeter** of convex particles was not fully inspected; its stated observable differs, but historical-priority uncertainty remains. The numerical verifier does not establish the infinite-parameter theorem independently.

## References

1. Steven R. Finch, *Mean Width of a Regular Simplex*, arXiv:1111.4976v1, first public 2011-11-21, https://arxiv.org/abs/1111.4976 .
2. Jaegil Kim, Vladyslav Yaskin and Artem Zvavitch, *Distribution functions of sections and projections of convex bodies*, arXiv:1512.07289v1, first public 2015-12-22, https://arxiv.org/abs/1512.07289 .
3. *Unlabeled directional widths determine a right circular cone*, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-unlabeled-directional-widths-determine-a-right-circular-cone--30a3b32d19eb .
4. G. T. Vickers and D. J. Brown, *The Distribution of Projected Area and Perimeter of Convex, Solid Particles*, Proc. R. Soc. A 457 (2001), 283–306, DOI:10.1098/rspa.2000.0667; full text not inspected.
