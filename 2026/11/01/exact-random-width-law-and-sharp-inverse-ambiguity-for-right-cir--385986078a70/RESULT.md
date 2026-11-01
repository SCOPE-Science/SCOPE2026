# Exact random-width law and sharp inverse ambiguity for right circular cylinders

## Finding
Let a solid right circular cylinder in \(\mathbb R^3\) have radius \(R>0\) and height \(H>0\). For a uniformly random unoriented line direction, let \(W\) be the length of the cylinder's orthogonal projection onto that line. Set \(a=2R\), \(b=H\), \(s=\sqrt{a^2+b^2}\), and \(q(w)=\sqrt{s^2-w^2}\). Its **complete** cumulative distribution function is
\[
F_W(w)=\begin{cases}
0,&w\le\min(a,b),\\
(bw-aq(w))/s^2,&a<b,\quad a<w<b,\\
1-(bw+aq(w))/s^2,&b<a,\quad b<w<a,\\
1-2aq(w)/s^2,&\max(a,b)\le w<s,\\
1,&w\ge s.
\end{cases}
\]
The two intermediate branches are mutually exclusive, and when \(a=b\) neither is used. In every case \(W\) has no atoms and has support \([\min(a,b),s]\).

The distribution uniquely determines \(a\) and \(b\), hence radius and height. More strongly, its minimum \(m\), maximum \(s\), and mean \(\mu\) suffice. The first two support endpoints alone identify exactly the unordered pair \(\{a,b\}=\{m,\sqrt{s^2-m^2}\}\): they give one cylinder if \(s=\sqrt2m\) and exactly two distinct noncongruent cylinders otherwise. The means of these two candidates differ by the **exact gap**
\[
\Delta_\mu=\frac{\pi-2}{4}\sqrt{s^2-2m^2}.
\]
At fixed exact endpoints, any absolute mean measurement error less than \(\Delta_\mu/2\) permits error-free nearest-candidate discrimination. The square-root vanishing of this optimal discrimination margin is sharp at \(s=\sqrt2m\).

## Assumptions and scope
The cylinder includes its two planar circular caps; these do not affect width. Its direction is Haar-uniform on the sphere modulo reversal. The formulas concern one-dimensional projection lengths, not planar-shadow diameters, average point-pair distances, or material chord intercepts. All radii and heights are strictly positive, and all quantities are exact population observables. The symbol \(m\) means the essential lower support endpoint, not a finite-sample minimum.

## Proof
Translate the body to the origin and express it as the Minkowski sum of a radius-\(R\) disk in the horizontal plane and an axial interval of length \(H\). Additivity of support functions yields the exact width of a unit vector \(u\):
\[
w(u)=2R\sqrt{1-u_3^2}+H|u_3|=a\sqrt{1-t^2}+bt,
\qquad t=|u_3|.
\]
For uniform \(u\) on \(S^2\), the coordinate \(t\) is uniform on \([0,1]\). The strictly concave function \(g(t)=a\sqrt{1-t^2}+bt\) starts at \(a\), ends at \(b\), increases to its unique maximum \(s\) at \(t=b/s\), and then decreases. Solving \(g(t)=w\) gives the two algebraic candidates
\[
t_\pm(w)=\frac{bw\pm a\sqrt{s^2-w^2}}{s^2}.
\]
On each of the intervals cut out by \(\min(a,b)\), \(\max(a,b)\), and \(s\), count the length of the set \(\{t\in[0,1]:g(t)\le w\}\). Below \(\min(a,b)\) the length is zero. When \(a<b\) and \(a<w<b\), it is \(t_-(w)\). When \(b<a\) and \(b<w<a\), it is \(1-t_+(w)\). Above \(\max(a,b)\), it is \(t_-(w)+1-t_+(w)\). These identities give the stated CDF and its continuous matching at every endpoint.

The essential minimum and maximum are \(m=\min(a,b)\) and \(s=\sqrt{a^2+b^2}\), yielding exactly the two ordered parameter pairs except at equality. Integrating the width function against uniform \(t\) gives
\[
\mu=\int_0^1 g(t)\,dt=\frac\pi4 a+\frac12b.
\]
Swapping the two positive parameters changes this mean by exactly \((\pi-2)(a-b)/4\), nonzero whenever \(a\ne b\). Since \(|a-b|=\sqrt{s^2-2m^2}\), the sharp gap follows. Under absolute error \(\varepsilon<\Delta_\mu/2\), the observed mean lies closer to the true candidate. At the critical ratio the gap is exactly zero and scales as the square root of the support-endpoint discriminant, so no strictly larger uniform margin is possible.

For an additional shape signature, differentiating the intermediate branch shows the density starts at \(1/b\) when \(a<b\), but starts at zero with slope \(1/a^2\) when \(b<a\). At \(a=b\), the density begins at \(1/a\). Thus the full law distinguishes the two orientations even without computing the mean.

## Verification
The standalone `checker.py` compares every CDF branch against numerically determined monotone-branch roots on a deterministic grid across tall, squat and balanced cylinders. Separate high-accuracy quadrature verifies the mean and its swap gap. The program checks probability support and branch boundaries. Exact proofs above establish every dimensionless formula for all positive parameters; finite tests are diagnostic only.

## Relationship to prior work
Gesmundo and Meroni, *The Geometry of Discotopes* (arXiv:2111.01241v1, November 1, 2021), develop support-function and Minkowski-sum structure for disk-and-segment sums, but examine exposed faces and algebraic boundaries, not the isotropic one-dimensional width distribution or its inverse two-candidate classification. A related published result treats the unlabeled-width inverse problem for **right circular cones**, whose support functions and piecewise laws are different. Another concerns correlated planar **shadow area and perimeter** of a cylinder, not the width CDF. These comparisons do not assert universal historical novelty; an older stereology or Feret-diameter formula may exist.

## Limitations
This is an exact two-parameter cylinder result, not a general reconstruction theorem for all axially symmetric convex bodies. The error threshold assumes the support endpoints are known exactly; with noisy endpoints, additional uncertainty analysis is needed. No independent mathematical audit or comprehensive historical-priority determination has been performed.

## References
1. F. Gesmundo and C. Meroni, *The Geometry of Discotopes*, arXiv:2111.01241v1, posted November 1, 2021, https://arxiv.org/abs/2111.01241. Full available arXiv HTML, §§1–3, support functions and Minkowski sums.
2. *Unlabeled directional widths determine a right circular cone*, public mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-unlabeled-directional-widths-determine-a-right-circular-cone--30a3b32d19eb (indexed summary available; complete source not independently inspected).
3. *Exact cylinder shadow mixed moment and sharp positive covariance*, public mathematical research record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-cylinder-shadow-mixed-moment-and-sharp-positive-covariance--1feeb231b707 (indexed summary available; complete source not independently inspected).
