# Strict angular-gap majorization of Mahler products for rotational polygon intersections

## Finding

Fix integers \(n\ge3\), \(k\ge2\), and put \(\alpha=2\pi/n\). Let \(P_n\subset\mathbb R^2\) be the centered regular \(n\)-gon whose incircle has radius one. For a gap vector \(g=(g_1,\ldots,g_k)\) with \(g_i\ge0\) and \(\sum_i g_i=\alpha\), set \(\theta_0=0\), \(\theta_j=\sum_{i=1}^j g_i\) for \(1\le j<k\), and form
\[
K(g)=\bigcap_{j=0}^{k-1}R_{\theta_j}P_n.
\]
Repeated rotations are allowed when some gaps vanish. Let \(K(g)^\circ=\{y:\langle x,y\rangle\le1\ \text{for all }x\in K(g)\}\). Its Santaló point is the origin. The Mahler product has the exact expression
\[
\boxed{\mathcal M_{n,k}(g)=\operatorname{area}(K(g))\operatorname{area}(K(g)^\circ)
=\frac{n^2}{2}\left(\sum_{i=1}^k\tan\frac{g_i}{2}\right)\left(\sum_{i=1}^k\sin g_i\right).}
\]
The symmetric function \(g\mapsto\mathcal M_{n,k}(g)\) is **strictly Schur-concave** on the closed simplex of permitted gaps: if \(g\) majorizes \(h\) and \(h\) is not a permutation of \(g\), then
\[
\boxed{\mathcal M_{n,k}(g)<\mathcal M_{n,k}(h).}
\]
In particular, the globally sharp endpoints are
\[
\boxed{n^2\sin^2(\pi/n)\le \mathcal M_{n,k}(g)
\le (nk)^2\sin^2(\pi/(nk)).}
\]
The lower equality holds precisely when all rotations coincide (one gap equals \(\alpha\)); the upper equality holds precisely when the rotations are equally spaced (every gap is \(\alpha/k\)). The product depends only on the multiset of gaps, even though the polygons themselves need not be congruent for different cyclic orders of those gaps.

For \(\bar g=2\pi/(nk)\), the equal-gap configuration has the sharp local expansion, for real \(\varepsilon_i\) summing to zero,
\[
\mathcal M_{n,k}(\bar g+\varepsilon_1,\ldots,\bar g+\varepsilon_k)
=(nk)^2\sin^2\frac{\pi}{nk}
-\frac{n^2k}{4}\cos\bar g\,\tan^2\frac{\bar g}{2}\sum_{i=1}^k\varepsilon_i^2
+O_{n,k}(\|\varepsilon\|^3).
\]
The displayed quadratic coefficient is positive for every permitted \(n,k\).

## Assumptions and scope

All angles are in radians. Majorization has its standard meaning: after sorting both vectors in nonincreasing order, every initial partial sum of \(g\) is at least the corresponding partial sum of \(h\), with equality for the full sum. Rotations are ordinary Euclidean rotations about the origin. The comparison concerns fixed \(n\) and fixed \(k\) and may compare arbitrary nonuniform angular configurations, including limit configurations with repeated rotations. No area normalization is needed because Mahler product is scale invariant.

The \(n\)-fold rotation symmetry of \(K(g)\), together with the uniqueness of its Santaló point, puts that point at the origin. The theorem is therefore about the standard affine-invariant Mahler product, not an arbitrarily centered polar volume. The normal gaps around the entire polygon consist of \(n\) repetitions of \(g_1,\ldots,g_k\).

## Proof

**1. The two areas.** Put \(A(g)=\sum_i\tan(g_i/2)\) and \(B(g)=\sum_i\sin g_i\). The supporting lines of \(K(g)\) are all tangent to the unit circle at the rotated facet normals. Consecutive tangent lines whose normals make an angle \(x\in[0,\alpha]\) meet at radial distance \(\sec(x/2)\). Each such interval of normals contributes \(\tan(x/2)\) to the area, by dividing the polygon into triangles with vertex at the center. Consequently
\[
\operatorname{area}(K(g))=n A(g).
\]
Polarity turns the intersection of the half-planes \(\langle x,u\rangle\le1\) into the convex hull of the corresponding unit normals \(u\). Consecutive normals of angular separation \(x\) contribute \(\sin x/2\) to that convex hull's area, giving
\[
\operatorname{area}(K(g)^\circ)=\frac n2 B(g).
\]
Both formulas remain valid by continuity when some gaps vanish. Their product proves the exact identity.

**2. A strict pairwise derivative inequality.** First suppose all \(g_i>0\). Fix distinct coordinates \(i,j\) with \(g_i>g_j\), abbreviate \(c_i=\cos g_i\), \(c_j=\cos g_j\), and set \(D=(1+c_i)(1+c_j)\). Direct differentiation gives
\[
\frac{2}{n^2}\left(\frac{\partial\mathcal M}{\partial g_i}-\frac{\partial\mathcal M}{\partial g_j}\right)
=(c_j-c_i)\left(\frac{B(g)}D-A(g)\right).
\]
Since \(c_j>c_i\), it suffices to establish \(DA>B\).

The identity \(\tan(x/2)=\sin x/(1+\cos x)\) yields, upon combining the two selected indices,
\[
DA(g)-B(g)=\sin(g_i+g_j)
+\sum_{\ell\ne i,j}\sin g_\ell
\left(\frac{D}{1+\cos g_\ell}-1\right).
\]
Write \(s=g_i+g_j\). Elementary cosine addition shows
\[
D=4\cos^2(g_i/2)\cos^2(g_j/2)
\ge4\cos^2(s/2)=2(1+\cos s).
\]
If \(s\le\pi/2\), then \(D\ge2\), each summand is nonnegative, and \(\sin s>0\). If \(s>\pi/2\), the constraint \(s\le\alpha\le2\pi/3\) gives \(D\ge1\) and hence every bracket in the sum is at least \(-1/2\). Also \(\sum_{\ell\ne i,j}\sin g_\ell\le\alpha-s\le\pi/6\) and \(\sin s\ge\sqrt3/2\). Thus
\[
DA(g)-B(g)\ge\frac{\sqrt3}{2}-\frac{\pi}{12}>0.
\]
Therefore \(\partial_i\mathcal M<\partial_j\mathcal M\) whenever \(g_i>g_j\).

**3. Strict majorization.** The function \(\mathcal M\) is symmetric and continuously differentiable. The preceding inequality is the strict Schur–Ostrowski derivative criterion on the positive simplex. Equivalently, transferring a positive amount from a larger gap to a smaller one, without reversing their order, strictly increases \(\mathcal M\). Standard finite transfer characterizations of majorization give the strict global result in the positive interior. For boundary vectors the same transfer argument applies along its nontrivial open segments, using the one-sided derivative formula at zero gaps, and continuity. Every vector is majorized by a vertex \((\alpha,0,\ldots,0)\), and every vector majorizes the equal-gap vector; strictness determines all equality cases. Inserting these two vectors in the exact area formula gives the sharp endpoint values.

**4. Quadratic stability coefficient.** Write \(g_i=\bar g+\varepsilon_i\), \(\sum_i\varepsilon_i=0\), and Taylor-expand the two one-variable sums. Their first-order terms vanish. At \(x=\bar g\), the second derivatives of \(\tan(x/2)\) and \(\sin x\) are respectively \(\tfrac12\sec^2(x/2)\tan(x/2)\) and \(-\sin x\). The quadratic term in the product is
\[
\frac{n^2k}{4}\left[\frac12\sec^2(\bar g/2)\tan(\bar g/2)\sin\bar g
-\tan(\bar g/2)\sin\bar g\right]\sum_i\varepsilon_i^2
=-\frac{n^2k}{4}\cos\bar g\tan^2(\bar g/2)\sum_i\varepsilon_i^2.
\]
Smoothness near the positive equal-gap vector gives the stated cubic remainder.

**5. Two rotated copies.** When \(k=2\), put \(g=(\theta,2\pi/n-\theta)\), with \(0\le\theta\le\pi/n\). The formula simplifies to
\[
\mathcal M_{n,2}(g)
=2n^2\sin^2(\pi/n)\,
\frac{\cos(\theta-\pi/n)}{\cos(\theta-\pi/n)+\cos(\pi/n)},
\]
which grows strictly from the regular \(n\)-gon value to the regular \(2n\)-gon value. The many-rotation majorization theorem is stronger than this single interpolation.

## Verification

An accompanying standalone standard-library Python program, `check_geometry.py`, independently constructs the tangent-line intersection polygon and the convex hull of its unit normals, and computes their areas by shoelace determinants. It compares both with the analytical formulas. It also tests gap permutations, strict balancing transfers, derivative signs, endpoint formulas and the local quadratic coefficient over deterministic configurations with \(n=3,4,5,7,12\) and \(k=2,3,4,6\). Execution returned `PASS 12100 independent numerical comparisons`. This is finite corroboration only: the arguments above prove the quantified statement for all integers and all real gap vectors.

## Relationship to prior work

Meyer and Reisner (2011) established that a regular planar polygon maximizes Mahler product among polygons with a bounded number of vertices. That implies the upper endpoint here but does not order two arbitrary nonregular angular-gap configurations. Böröczky, Makai, Meyer and Reisner (2013) established a sharp lower bound for all bodies with prescribed \(n\)-fold rotational symmetry, including the lower endpoint here; their stability inequality is not the present pairwise majorization comparison. Alexander, Fradelizi and Zvavitch (2019) revisited regular-polygon maximality, again an endpoint statement. Published research on random rotations of tangential polygons examines expected intersection **area**, not the deterministic product of intersection area and polar area.

The additional mathematical assertion here is that the product of one strictly Schur-convex factor and one strictly Schur-concave factor has a definite, strict global order on these restricted angular simplices. Its direct proof is the pairwise derivative estimate above. A search of relevant accessible records did not identify an equivalent angular-gap majorization theorem; this is not a claim of exhaustive worldwide priority.

## Limitations

The theorem requires regular starting polygons with a common inradius, rotations about a common center, and at least threefold rotational symmetry. It does not assert the same majorization law for arbitrary tangential polygons, for unequal inradii, or for dimensions greater than two. The quadratic expansion holds locally near equally spaced rotations with \(n,k\) fixed; no uniform remainder bound across all \(n,k\) is claimed. Finite checks are not a substitute for proof. Older or differently indexed literature might contain an equivalent angular smoothing statement, so historical priority remains a residual risk; independent audit has not been performed.

## References

- M. Meyer and S. Reisner, *On the volume product of polygons*, Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **81** (2011), 93–100. DOI: 10.1007/s12188-011-0054-3. First public online date verified as 2011-04-05.
- K. J. Böröczky, E. Makai Jr., M. Meyer and S. Reisner, *On the volume product of planar polar convex bodies—lower estimates with stability*, Studia Scientiarum Mathematicarum Hungarica **50** (2013), 159–198. DOI: 10.1556/SScMath.50.2013.2.1235; open version arXiv:1507.01481.
- M. Alexander, M. Fradelizi and A. Zvavitch, *Polytopes of maximal volume product*, Discrete & Computational Geometry **62** (2019), 583–600. DOI: 10.1007/s00454-019-00072-3; preprint arXiv:1708.07914.
