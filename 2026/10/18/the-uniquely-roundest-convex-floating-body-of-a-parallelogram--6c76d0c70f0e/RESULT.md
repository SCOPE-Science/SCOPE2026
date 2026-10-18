# The uniquely roundest convex floating body of a parallelogram

## Finding

For every nondegenerate parallelogram \(P\subset\mathbb R^2\), let \(P_\alpha\) be its convex floating body, the intersection of all closed halfplanes whose complementary caps have area at most \(\alpha|P|\), where \(0<\alpha<1/2\). Then the Banach--Mazur distance from \(P_\alpha\) to a Euclidean disk has a unique minimum, independent of the shape of \(P\), at
\[
\boxed{\alpha_*=\frac32-\sqrt2=0.0857864376\ldots.}
\]
The sharp minimum is
\[
\boxed{\min_{0<\alpha<1/2}d_{\rm BM}(P_\alpha,B_2^2)=\frac{2(\sqrt2-1)}{\sqrt{4\sqrt2-5}}=1.0221621690\ldots.}
\]
The entire distance profile is explicit. Set \(Q=[-1,1]^2\), and define \(R(\alpha)\) and \(r(\alpha)\) as the centered Euclidean circumradius and inradius of \(Q_\alpha\). Then
\[
R(\alpha)=\max\{1-2\alpha,\sqrt2-2\sqrt\alpha\},\qquad
r(\alpha)=\begin{cases}\sqrt{1-4\alpha},&0<\alpha\le1/8,\\ \sqrt2-2\sqrt\alpha,&1/8\le\alpha<1/2.\end{cases}
\]
For **every** \(\alpha\) in that range, not merely at the optimum,
\[
\boxed{d_{\rm BM}(P_\alpha,B_2^2)=R(\alpha)/r(\alpha).}
\]
The circumradius contact directions switch from the four diagonals to the four coordinate axes at \(\alpha_*\). The inradius contact directions switch from eight oblique normals to the four diagonals at \(1/8\). These are distinct sharp transitions.

## Assumptions and scope

All parallelograms are full-dimensional and carry normalized two-dimensional Lebesgue measure. The cap parameter \(\alpha\) is a **fraction of the original area**, so \(Q_\alpha\) removes caps of area \(4\alpha\). At \(\alpha=0\) the untrimmed parallelogram is understood only as a limit; at \(\alpha=1/2\) the floating body degenerates, and neither endpoint is included. \(d_{\rm BM}\) is the multiplicative affine Banach--Mazur distance, allowing arbitrary invertible affine transformations and translations. The result concerns the classical **convex** floating body, not the Ulam floating body, Schneider separation body, or illumination body.

The known exact square contour has the convenient global form
\[
Q_\alpha=\{(x,y):|x|\le1,\ |y|\le1,\ (1-|x|)(1-|y|)\ge2\alpha\}. \tag{1}
\]
The hyperbolic contour itself was described earlier by Gupta for the square (in her unit-square normalization); equation (1) is included for normalization and the full-parameter proof, **not as a priority claim**. The claimed new fact is the complete sharp affine-roundness profile and its unique global optimum.

## Proof

**1. Cap quantiles and the exact contour.** By dihedral symmetry, consider a unit normal \(u=(a,b)\) with \(a\ge b\ge0\). For a threshold \(q\) close to the maximum \(a+b\), the cap of \(Q\) cut off by \(ax+by\ge q\) is a corner triangle. Dividing its area by \(|Q|=4\) gives \((a+b-q)^2/(8ab)\). Once the cutting line meets the opposite horizontal side, the cap is a trapezoid of normalized area \((a-q)/(2a)\). Solving for a cap fraction \(\alpha\) yields the upper quantile
\[
h_\alpha(u)=\begin{cases}
a(1-2\alpha),&b\le2\alpha a,\\
a+b-\sqrt{8\alpha ab},&b\ge2\alpha a.
\end{cases}\tag{2}
\]
These branches agree on their boundary, and when \(b=0\) only the first branch is used.

The candidate on the right of (1) has in the first quadrant the boundary \(y=1-2\alpha/(1-x)\), with \(0\le x\le1-2\alpha\). Maximizing \(ax+by\) on it gives either the axis endpoint \((1-2\alpha,0)\), when \(b\le2\alpha a\), or the smooth point
\[
(x,y)=\left(1-\sqrt{2\alpha b/a},\ 1-\sqrt{2\alpha a/b}\right)
\]
when \(b\ge2\alpha a\). The maximum values are exactly (2). Thus the candidate's support function agrees in **every** direction with the cap-quantile support function, and consequently (1) equals the intersection defining \(Q_\alpha\). This direct argument works for the entire \(0<\alpha<1/2\) range.

**2. Inradius and contacts.** The largest centered disk in a symmetric convex body has radius equal to the minimum of its support function. Put \(b/a=\tan\theta\) with \(0\le\theta\le\pi/4\). In the trapezoid branch, (2) decreases up to the switching angle. In the corner branch, set \(s=a+b\in[1,\sqrt2]\). Using \(2ab=s^2-1\), the support value becomes
\[
f_\alpha(s)=s-2\sqrt\alpha\sqrt{s^2-1}.
\]
Its critical point is \(s=(1-4\alpha)^{-1/2}\), which lies in the corner branch and before \(\sqrt2\) exactly when \(\alpha\le1/8\). Its value is \(\sqrt{1-4\alpha}\). Otherwise the minimum is at the diagonal, \(f_\alpha(\sqrt2)=\sqrt2-2\sqrt\alpha\). For \(0<\alpha<1/8\), the oblique minimizing normal satisfies \(\sin(2\theta)=4\alpha/(1-4\alpha)\); reflection produces eight normals. At and beyond \(1/8\), the diagonal directions minimize.

**3. Circumradius and contacts.** In the first quadrant, write \(t=x+y\) along the hyperbola \((1-x)(1-y)=2\alpha\). Then \(xy=t-1+2\alpha\), hence
\[
x^2+y^2=(t-1)^2+1-4\alpha.
\]
Since the right side is convex in \(t\), its maximum over the boundary arc occurs at an endpoint, which is either the axis point \((1-2\alpha,0)\) or the diagonal point \((1-\sqrt{2\alpha},1-\sqrt{2\alpha})\). This proves the formula for \(R\). The two candidate radii agree in the open parameter interval only when \(\sqrt\alpha=1-1/\sqrt2\), i.e. at \(\alpha_*\), giving the asserted switch and eight total outer contact directions there.

**4. Why tilted or translated ellipses cannot improve the ratio.** The body \(Q_\alpha\) is centrally symmetric and invariant under the dihedral symmetry group \(D_4\) of the square. Any affine ellipsoidal sandwich \(E\subset Q_\alpha\subset\lambda E\) can first be centered at the origin without increasing \(\lambda\): the original and reflected sandwiches, followed by averaging their two centers, give a sandwich with the same positive-definite ellipsoidal shape matrix centered at zero. Write that matrix as \(M\succ0\), so \(E=\{x:x^{\mathsf T}M^{-1}x\le1\}\). The inner containment \(E\subset Q_\alpha\) is equivalent to \(u^{\mathsf T}Mu\le h_{Q_\alpha}(u)^2\) for all unit \(u\), a constraint linear in \(M\). The outer containment is \(x^{\mathsf T}M^{-1}x\le\lambda^2\) for all \(x\in Q_\alpha\), a convex constraint in \(M\). Conjugate \(M\) by every matrix in \(D_4\) and average. Both containments persist, and the average is a scalar multiple of the identity. Thus a concentric circular ellipsoid is optimal. Its best sandwich factor is exactly \(R(\alpha)/r(\alpha)\). The affine equivariance of floating bodies and affine invariance of \(d_{\rm BM}\) extend this conclusion to every parallelogram.

**5. Unique optimum.** On \(0<\alpha\le\alpha_*\), the distance is \((\sqrt2-2\sqrt\alpha)/\sqrt{1-4\alpha}\). Its derivative with respect to \(z=\sqrt\alpha\) has the sign of \(4\sqrt2 z-2<0\). Between \(\alpha_*\) and \(1/8\), it is \((1-2\alpha)/\sqrt{1-4\alpha}\), whose derivative is \(4\alpha/(1-4\alpha)^{3/2}>0\). Between \(1/8\) and \(1/2\), it is \((1-2\alpha)/(\sqrt2-2\sqrt\alpha)\); its derivative with respect to \(z=\sqrt\alpha\) has the sign of \(2(1-\sqrt2z)^2>0\). Hence there is exactly one minimizer, at \(\alpha_*\). Substitution gives the boxed exact minimum.

## Verification

The accompanying standalone Python 3 checker `check_floating_square.py` (standard library only) compares the analytic cap fraction and support quantiles over 45,009 direction/parameter samples; independently maximizes over 90,009 boundary samples; tests the sharp contact conditions and the exact candidate optimum. On execution it printed:

`VERIFY_OK normalization_samples=45009 support_samples=45009 boundary_samples=90009 min_parameter=0.085786437626905 min_BM=1.022162169058788 max_support_discrepancy=4.44e-16`

The finite computations test formulas and normalization; steps 1--5 are the proof for all admissible \(\alpha\), all viewing directions, and every parallelogram.

## Relationship to prior work

Schütt--Werner (1990) and Bárány--Larman (1988) introduced and developed convex floating bodies. Gupta (2017), Proposition 3.3 proof, **already specifies hyperbolic boundary pieces of the square's floating body** and its exact semialgebraic contour near small cap fraction. The present result credits this antecedent; the old shape formula alone is **not** the new finding. Mordhorst--Werner (2019) study floating--illumination duality and related asymptotic metrics, not the full affine distance-to-disk profile of square depth contours. Grundbacher--Kobos (2026) give general affine-optimality criteria for distance ellipsoids rather than a floating-square depth-level minimizer. Brandenburg--De Loera--Meroni (2026), Section 5.2, establish semialgebraic floating bodies and the centerpoint-depth correspondence for polytopal measures, motivating exact optimization over all trimming levels. The new contribution is the global, dimensionless, uniquely optimized affine distortion profile with its two independent contact transitions, not the definition of floating bodies, their square contours, or the general ellipsoid criteria.

## Limitations

This is a planar parallelogram statement, with an affine transfer from the square; it does not optimize geometric depth contours of arbitrary polygons or in higher dimensions. It provides the exact global optimum over cap fractions \(0<\alpha<1/2\), not over alternative smoothing constructions. An older unindexed exact affine-roundness computation could exist, and an independent historical-priority audit has not been performed. No numerical experiment is used as a substitute for the continuous optimization proof.

## References

- M.-C. Brandenburg, J. A. De Loera, C. Meroni, *From Ham-Sandwich to Centerpoints: Semialgebraic Algorithms for Cutting Polytopal Measures*, arXiv:2607.02400v1 (first public July 2, 2026), Section 5.2. https://arxiv.org/abs/2607.02400
- P. Gupta, *Convex floating bodies as approximations of Bergman sublevel sets on tube domains*, Proc. Amer. Math. Soc. **145** (2017), 4385--4396, DOI:10.1090/proc/13573, proof of Proposition 3.3, pp. 4393--4394. https://math.iisc.ac.in/~purvigupta/TubeDom_offprint.pdf
- C. Schütt, E. Werner, *The convex floating body*, Math. Scand. **66** (1990), 275--290. https://journals.msp.org/mscand/article/download/1313/1312/1344
- O. Mordhorst, E. M. Werner, *Floating and Illumination Bodies for Polytopes: Duality Results*, arXiv:1709.02429, published 2019. https://arxiv.org/abs/1709.02429
- F. Grundbacher, T. Kobos, *John-type decompositions for affinely-optimal positions of convex bodies*, arXiv:2602.14847 (2026). https://arxiv.org/abs/2602.14847
