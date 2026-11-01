# Sharp one-third erasure threshold for the Löwner ellipse of a regular polygon

## Finding
For integers \(n\ge 6\) and \(1\le k\le n-3\), let \(P_{n,k}\) be the convex hull of the vertices of the regular unit-circumradius \(n\)-gon after deleting \(k\) consecutive vertices. Its unique minimum-area enclosing ellipse equals the original unit disk **if and only if**
\[
\boxed{3(k+1)\le n.}
\]
Consequently the maximum number of consecutive vertices that can be erased without changing the Löwner ellipse is exactly \(\lfloor n/3\rfloor-1\). If the inequality fails, the minimum enclosing ellipse has strictly smaller area than \(\pi\). Whenever the disk remains optimal, an explicit nonnegative contact certificate is supported on at most eight surviving vertices (and an existential certificate on at most six).

## Assumptions and scope
The ambient space is Euclidean \(\mathbb R^2\). The original vertices are
\[
 v_j=(\cos(2\pi j/n),\sin(2\pi j/n)),\qquad j=0,\ldots,n-1,
\]
and the deleted block is \(j=0,\ldots,k-1\); rotation shows that any consecutive block gives the same answer. The remaining \(n-k\ge3\) points are noncollinear. The phrase “minimum enclosing ellipse” refers to arbitrary translated, rotated and anisotropic ellipses, not merely disks or axis-aligned ellipses. The result concerns whether the original unit disk is unchanged; it does not give the semiaxes of the smaller optimizer outside the threshold.

## Proof
**1. A contact criterion.** The Löwner–John contact characterization specializes as follows: the unit disk is the unique minimum-area ellipsoid containing a finite set of points on the unit circle precisely when there are weights \(w_j\ge0\) on those points with
\[
\sum_jw_j=1,\qquad\sum_jw_jv_j=0,\qquad
\sum_jw_jv_jv_j^{\mathsf T}=\tfrac12 I_2.
\]
Indeed, multiplying the latter two identities by two gives the standard isotropic contact decomposition. Conversely, the usual necessary optimality theorem supplies such weights if the unit disk is optimal. Equivalently, the first two nonconstant Fourier moments vanish:
\(\sum_jw_j e^{2\pi i j/n}=\sum_jw_j e^{4\pi i j/n}=0\).

**2. Reflect and reduce to one dimension.** Reflection through the bisector of the deleted block preserves the surviving vertices; average a proposed contact measure with its reflection. The reflection axis has angle \(\phi=\pi(k-1)/n\). For a symmetrized surviving point set write \(c=\cos(2\pi j/n-\phi)\). All sine and sine–cosine moments automatically vanish. The two required conditions become
\[
\mathbb E c=0,\qquad \mathbb E c^2=\tfrac12.
\]
The greatest and least available \(c\)-values are
\[
 C=\cos\!\left(\frac{\pi(k+1)}n\right),\qquad -B,
\quad B=\begin{cases}1,&n+k\text{ odd},\\
\cos(\pi/n),&n+k\text{ even}.
\end{cases}
\]
To see this, the surviving relative angles are \(\pi(2j-k+1)/n\) for \(j=k,\ldots,n-1\); the nearest ones to zero lie at \(\pm\pi(k+1)/n\), while the nearest ones to \(\pi\) are either exactly \(\pi\) or \(\pi\pm\pi/n\).

**3. The sharp obstruction.** If \(C\le0\), no zero first moment exists. Otherwise every \(c\in[-B,C]\) obeys \((c+B)(C-c)\ge0\), so every measure with \(\mathbb Ec=0\) satisfies
\[
\mathbb Ec^2\le BC.
\]
If \(3(k+1)>n\), then \(C<1/2\) and \(B\le1\), hence \(BC<1/2\). A disk contact certificate is impossible, so the original disk cannot be a minimum-area ellipse. Since it is feasible and the Löwner ellipse exists and is unique for a nondegenerate polygon, the actual optimum has strictly smaller area.

**4. Enough variance under the threshold.** Assume \(3(k+1)\le n\), and put \(t=\pi/n\). If \(n+k\) is odd, \(B=1\) and \(C\ge1/2\). If \(n+k\) is even, equality \(3(k+1)=n\) is impossible (it would give \(n+k=4(k+1)-1\), odd). Therefore \(3(k+1)\le n-1\), and
\[
 BC\ge \cos t\cos\!\left(\frac{\pi-t}3\right)\ge\frac12.
\]
For the final inequality, the logarithm of the product is concave in \(0\le t\le\pi/6\), so its minimum is at an endpoint. At \(t=0\) the product is \(1/2\), and at \(t=\pi/6\) it exceeds \(1/2\); the latter follows from \(\cos(5\pi/18)>\cos(3\pi/10)>1/\sqrt3\), since \(\cos^2(3\pi/10)=(5-\sqrt5)/8>1/3\).

Now make a zero-mean distribution supported only at \(-B\) and \(C\), with masses \(C/(B+C)\) and \(B/(B+C)\), respectively. Its second moment is exactly \(BC\ge1/2\). To obtain a smaller second moment, select adjacent available values \(a\le0\le b\) on either side of \(c=0\); these exist because the surviving angular arc runs from \(\alpha=\pi(k+1)/n\le\pi/3\) to \(2\pi-\alpha\). The angular mesh size is \(2\pi/n\). The zero-mean two-point distribution with masses \(b/(b-a)\) at \(a\) and \(-a/(b-a)\) at \(b\) has second moment
\[
-ab\le\sin^2(\pi/n)\le\frac14<\frac12.
\]
If either of these nodes equals zero, use the point mass there instead. A convex mixture of this low-variance measure and the endpoint high-variance measure attains exactly \(\mathbb E c^2=1/2\). Divide each orbit mass equally between its reflected vertices (or leave it at the fixed vertex). The resulting weights meet both contact identities, proving the disk's global optimality and uniqueness. At most four reflected orbits, hence eight vertices, are used. By planar Carathéodory applied to the points \((c,c^2)\), at most three orbits (six vertices) suffice in principle.

The two directions together prove the equivalence and the maximal admissible \(k\). On the boundary \(n=3(k+1)\), the three equally spaced surviving vertices already give a particularly simple equilateral-triangle contact certificate.

## Verification
The accompanying self-contained `verify_erasure.py` uses only the Python standard library. Run `python verify_erasure.py`. It enumerates all \(60{,}375\) pairs with \(6\le n\le350\) and \(1\le k\le n-3\); for all \(20{,}010\) threshold-passing pairs it constructs nonnegative symmetric contact weights and checks the first two complex Fourier moments to numerical tolerance. A separate finite linear-program feasibility comparison using SciPy examined \(10{,}875\) cases with \(6\le n\le150\), agreeing throughout. Finite experiments are corroboration, not proof for arbitrary \(n\): the preceding inequalities and exact contact construction are the proof.

## Relationship to prior work
The unit-disk contact criterion follows the classical Löwner–John theory, stated for general convex bodies by Güler and Gürtuna (arXiv:0709.0707). Rublev and Petunin's 1998 treatment of minimum-area enclosing ellipses supplies constructions for arbitrary finite polygons and analyzes when an inscribed trapezoid has the unit circle as its optimal ellipse; these are closely related general and small-support methods. Peherstorfer (arXiv:1001.2451) develops positive trigonometric quadrature with vanishing low-frequency Fourier moments on prescribed nodes; Kutyniok, Okoudjou and Philipp (arXiv:1310.8107) develop scalable-frame moment cones. These works supply concepts capable of testing instances but the inspected statements do not specify the uniform exact consecutive-erasure cutoff \(3(k+1)\le n\), nor its sparse certificate for every permitted pair. This assessment is a comparison of stated implications, not a claim that no equivalent older calculation exists.

## Limitations
The theorem assumes regularly spaced unit-circle vertices, deletion of a **single contiguous block**, and at least three surviving vertices. It does not classify arbitrary scattered deletions or identify the smaller optimizer's shape beyond the cutoff. General finite-polygon algorithms and older optimal-design or quadrature literature could contain equivalent results under different wording; an independent historical-priority audit has not been performed. The numerical verifier uses floating-point tolerances and has no role as an infinite proof.

## References
- O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (first posted 2007-09-05), https://arxiv.org/abs/0709.0707.
- B. V. Rublev and Yu. I. Petunin, *Minimum-Area Ellipse Containing a Finite Set of Points. II*, Ukrainian Mathematical Journal 50(8) (1998), pp. 1253–1261, https://www.mit.edu/~hlb/ellipse-paper.pdf. Exact first-public day not established.
- F. Peherstorfer, *Positive Trigonometric Quadrature Formulas and Quadrature on the Unit Circle*, arXiv:1001.2451 (first posted 2010-01-14), https://arxiv.org/abs/1001.2451.
- G. Kutyniok, K. A. Okoudjou and F. Philipp, *Scalable Frames and Convex Geometry*, arXiv:1310.8107 (first posted 2013-10-30), https://arxiv.org/abs/1310.8107.
