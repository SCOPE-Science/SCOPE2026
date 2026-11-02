# Open threefold inverse ambiguities for intrinsic distances on flat conical disks

## Finding

Consider the compact flat conical disk \(C(t,R)\) with slant radius \(R>0\), total cone angle \(2t\), and \(0<t<\pi\). Its intrinsic metric is obtained from the Euclidean radius-\(R\) sector of angle \(2t\) by identifying the two radial sides. For independent area-uniform points \(X,Y\), let \(D=d(X,Y)\), and let \(A\) denote area. This family has **two robust, distinct threefold inverse ambiguities**:

**Area plus mean square:** Define
\[
F(t)=1-\frac89\frac{\sin t}{t},\qquad Q(t)=\frac{F(t)}{t}.
\]
For every number \(q\) in the nonempty open interval
\[
\frac1\pi<q<Q(9\pi/10),
\]
and every prescribed \(A>0\), at least three pairwise nonisometric conical disks have area \(A\) and \(\mathbb E D^2=Aq\). Their half-angles lie respectively in \((0,\pi/2)\), \((\pi/2,9\pi/10)\), and \((9\pi/10,\pi)\).

**Second and fourth distance moments:** Define
\[
H(t)=\frac53+\frac{\sin(2t)}{4t}-\frac{32}{15}\frac{\sin t}{t},\qquad K(t)=\frac{H(t)}{F(t)^2}.
\]
For every number \(k\) in the nonempty open interval
\[
\frac53<k<K(2\pi/3),
\]
and every prescribed \(m>0\), at least three pairwise nonisometric conical disks have \(\mathbb E D^2=m\) and \(\mathbb E D^4=km^2\). Their half-angles lie respectively in \((0,\pi/2)\), \((\pi/2,2\pi/3)\), and \((2\pi/3,\pi)\).

The two ambiguity regions are open in their corresponding two-dimensional observation spaces because \(A\) and \(m\) may vary freely. The assertion is **at least three**, not an unproved upper bound on the total number of solutions.

## Assumptions and scope

Take \(R>0\), \(0<t<\pi\), and the intrinsic shortest-path metric on the sector quotient \(C(t,R)\). Points are sampled independently from normalized two-dimensional Hausdorff (surface-area) measure. The apex is included and has measure zero. The boundary at slant radius \(R\) is included. All moments are exact population moments, not sample estimators. The cone's total angle \(2t\) is an intrinsic invariant, so different values of \(t\) yield nonisometric cones regardless of radius. At \(t=\pi\), the space is a flat Euclidean disk; it is used only to evaluate a limiting endpoint.

## Proof

**1. Exact intrinsic distance and sampling law.** The area element in polar sector coordinates is \(r\,dr\,d\theta\); thus \(A=tR^2\). A uniform point has independent radial coordinate of density \(2r/R^2\) on \([0,R]\) and angular coordinate uniform modulo \(2t\). For two uniform angles, their shortest angular separation \(\delta\) is uniform on \([0,t]\), independently of the radii. Because \(t<\pi\), the shortest path between points with radii \(r,s\) unfolds to a straight segment with angular difference \(\delta\); the segment remains within the radius-\(R\) disk. A path through the apex is no shorter, and any alternative winding has a larger angular sweep. Hence
\[
D^2=r^2+s^2-2rs\cos\delta.
\]
The radial moments are \(\mathbb E r^j=2R^j/(j+2)\) for all integers \(j\ge0\); the angular moments are \(\mathbb E\cos\delta=\sin t/t\) and \(\mathbb E\cos^2\delta=1/2+\sin(2t)/(4t)\). Expansion yields exactly
\[
\mathbb E D^2=R^2 F(t),\qquad \mathbb E D^4=R^4 H(t).
\]
As nonzero squared-distance moments, \(F(t),H(t)>0\). They extend continuously to \([0,\pi]\), with \(F(0)=1/9\), \(H(0)=1/30\), \(F(\pi)=1\), and \(H(\pi)=5/3\).

**2. Threefold ambiguity at fixed area.** The scale-free observable is \(\mathbb E D^2/A=Q(t)\). Since \(Q(t)\sim 1/(9t)\) as \(t\downarrow0\), its limit at zero is infinite, whereas \(Q(\pi)=1/\pi\). Direct substitution gives
\[
Q(\pi/2)-\frac1\pi=\frac{9\pi-32}{9\pi^2}<0
\]
using \(\pi<22/7<32/9\). Also \(\sin(9\pi/10)=\sin(\pi/10)=(\sqrt5-1)/4\), so
\[
Q(9\pi/10)-\frac1\pi=\frac{81\pi-200(\sqrt5-1)}{729\pi^2}>0.
\]
Indeed \(\pi>31/10\) and \(\sqrt5<9/4\) imply the numerator exceeds \(81(31/10)-200(5/4)>0\). By continuity, for any \(q\) strictly between \(1/\pi\) and \(Q(9\pi/10)\), there is a root of \(Q(t)=q\) in each of the three disjoint intervals stated in the Finding. For any prescribed area \(A>0\), choose \(R=\sqrt{A/t}\) at each root. This fixes both area and the second distance moment while changing the cone angle.

**3. Threefold ambiguity from two even moments.** Set \(K(t)=H(t)/F(t)^2\). Its endpoint values are \(K(0)=27/10\) and \(K(\pi)=5/3\). At the two interior test angles, direct algebra gives
\[
H(\pi/2)-\frac53F(\pi/2)^2
=\frac{32(63\pi-200)}{1215\pi^2}<0,
\]
since \(\pi<22/7<200/63\). Setting \(b=\sqrt3/\pi\), one likewise obtains
\[
H(2\pi/3)-\frac53F(2\pi/3)^2
=\frac{b(939-1600b)}{2160}>0.
\]
Here \(b<7/12<939/1600\), because \(\pi>3\) and \(\sqrt3<7/4\). The three strict sign changes between \(0,\pi/2,2\pi/3,\pi\) give, by the intermediate value theorem, one solution of \(K(t)=k\) in each of the three disjoint intervals for every \(5/3<k<K(2\pi/3)\). Choosing \(R=\sqrt{m/F(t)}\) fixes \(\mathbb E D^2=m\) and therefore \(\mathbb E D^4=km^2\). Different cone angles exclude isometry.

## Verification

A standalone checker, `verification/cone_moments_check.py`, symbolically verifies the endpoint factorization identities; independently quadratures the original three-variable geodesic distance expression at five test angles; finds illustrative triples using bracketing root solves; and independently samples point pairs. Running `python verification/cone_moments_check.py` in an environment with NumPy, SciPy, and SymPy prints `ALL_CHECKS_PASSED`. These computations corroborate, but do not replace, the analytical identity and intermediate-value arguments above.

For illustration, when \(\mathbb E D^2=1\) and \(\mathbb E D^4=1.69\), three numerically located half-angles are approximately \(0.677128\), \(1.936879\), and \(2.891207\). The rigorous theorem does not rely on those decimal approximations. For area \(1\) and \(\mathbb E D^2=0.31865\), three illustrative half-angles are approximately \(0.436394\), \(2.736548\), and \(3.109010\).

## Relationship to prior work

Mémoli and Needham [1] establish a broad inverse-problem framework for global distance distributions and give explicit noninjectivity examples for plane curves; their examples and results do not concern low-order intrinsic distance moments of conical disks. Rukhovich [2] studies distributions of distances between **singular vertices across random flat cone spheres**, whereas here the cone is fixed and the randomness comes from two uniformly sampled ordinary points on one disk. Fu [3] studies the lengths and self-intersections of trajectories on flat cone surfaces, not area-sampling moments. The stated threefold open ambiguity regions are not consequences of these comparisons. Historical priority remains subject to wider literature checking, especially alternative terminology for conical metric disks.

## Limitations

This result proves only lower bounds of three on the number of inverse solutions in the specified observation regions. It does not prove those regions are maximal, that any triple exhausts all solutions, or that an additional moment always restores global identifiability. Cones with total angle larger than \(2\pi\), nonuniform sampling, truncated annular cones, extrinsic chord distances, and statistical noise are outside the statement. Independent assessment has not been performed.

## References

1. F. Mémoli and T. Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, first posted 2018-10-23; full preprint at https://arxiv.org/pdf/1810.09646.
2. A. Rukhovich, *How close are cone singularities on a random flat surface?*, arXiv:2212.12806, first posted 2022-12-24; https://arxiv.org/abs/2212.12806.
3. K. Fu, *Uniform Length Estimates for Trajectories on Flat Cone Surfaces*, arXiv:2409.14188, first posted 2024-09-21; https://arxiv.org/abs/2409.14188.
