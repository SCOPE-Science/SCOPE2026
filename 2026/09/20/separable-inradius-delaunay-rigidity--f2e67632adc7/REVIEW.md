# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The necessity argument uses only four-point configurations. If a continuous separable inradius functional is universally maximized (or minimized) by Delaunay triangulations, perturbing one vertex of a cyclic quadrilateral to the two sides of its circumcircle gives opposite Delaunay choices. Continuity therefore forces exact equality of the two separable two-triangle sums on the cyclic limit.

The cyclic-kite computation was checked algebraically. With
\[
A=(\lambda,0),\ C=(-\lambda,0),\ B=\lambda(\cos2\alpha,\sin2\alpha),\ D=\lambda(\cos2\alpha,-\sin2\alpha),
\]
the two inradii for diagonal \(AC\) are both \(u=\lambda(\sin\alpha+\cos\alpha-1)\), while those for diagonal \(BD\) are
\[
v=2\lambda\cos\alpha(1-\cos\alpha),\qquad
w=2\lambda\sin\alpha(1-\sin\alpha).
\]
They satisfy \(v=u(1+\delta)\), \(w=u(1-\delta)\) with \(\delta=\sin\alpha-\cos\alpha\). Scaling and varying \(\alpha\) realizes every positive midpoint pair, so cyclic invariance is exactly the midpoint Jensen equation. Continuity then gives affinity.

The sign witness was also checked exactly. For
\[
(-1,0),(0,1),(1,0),(0,-2),
\]
diagonal \(AC\) is uniquely Delaunay and its inradius sum exceeds the alternative by
\[
\frac{3(\sqrt2+\sqrt{10}-4)}{2(3+\sqrt2+\sqrt5)}>0.
\]
Thus an affine transform has the correct universal maximizing sign exactly when its slope is nonnegative, and the minimizing sign exactly when its slope is nonpositive. Lambert's theorem proves the converse because the number of triangles is fixed for a given point set.

The power-law corollary follows from strict convexity or concavity at a non-isospectral midpoint pair in the cyclic kite, followed by an arbitrarily small radial perturbation that makes the desired diagonal uniquely Delaunay without reversing the strict power inequality. The supplied verification script independently checks the coordinate formulas and representative perturbations; it is supplementary rather than part of the proof.

## Originality

**PASS, to the best of our knowledge.**

The classical Japanese theorem gives linear inradius-sum invariance for cyclic polygons, and the classical converse characterizes cyclicity by triangulation-independent inradius sum. Lambert (1994) proves that the Delaunay triangulation maximizes the arithmetic mean, equivalently the sum, of triangle inradii for every finite planar point set. These linear statements are explicitly excluded from the novelty claim.

Minculete, Barbu and Szöllősy, *About the Japanese Theorem* (Crux Mathematicorum 38(5), 2012, 188–193), was inspected because it is a close nonlinear near-match. It proves additional identities involving reciprocal and squared inradii, but the identities carry factors of the two diagonal lengths. They do not state invariance of an unweighted separable sum \(\varphi(r_1)+\varphi(r_2)\), nor an affine-rigidity classification.

Klyachin and Grigorieva (2017) give general sufficient conditions for functionals minimized by \(\Phi\)-triangulations. Their Delaunay corollary includes \(\sum \mu(R_\Delta)\) for arbitrary increasing transforms of circumradius. This is an important nearby result, but it concerns circumradius and in fact emphasizes the contrast with the inradius classification here. Dolbilin, Edelsbrunner and Musin (2012) study transfer of finite-set functional optimality to density optimality over infinite Delaunay sets, not this scalar-transform classification.

Searches covered exact and synonymous formulations involving Delaunay inradius functionals, convex or concave functions of inradius, powers of inradii, separable mesh-quality objectives, and functional-equation variants of the Japanese theorem. No located source states the theorem that continuous unweighted separable transforms are forced to be affine, nor the explicit conclusion that \(\sum r^p\) fails universal Delaunay maximization for every \(p\ne1\).

The strongest residual originality risk is Timothy Lambert, *The Delaunay Triangulation Maximizes the Mean Inradius* (CCCG 1994, 201–206). The bibliographic record, abstract, proceedings listing, computational-geometry textbook summaries, and later optimality summaries were checked and state the linear arithmetic-mean/sum criterion. The full paper itself was not directly inspectable here. A historical discussion also indicates that Lambert treats the converse Japanese theorem, so the full paper could contain an unadvertised argument close to part of the cyclic perturbation mechanism. Because the present rigidity proof is short, equivalent folklore in classical Euclidean-geometry or mesh-quality literature is also possible.

## Value

**PASS.**

The contribution explains a structural asymmetry between two standard Delaunay quality measures. Circumradius admits broad nonlinear monotone transforms in known minimization results, whereas inradius admits no nonlinear continuous unweighted separable transform at all under universal extremality. The classification simultaneously identifies the Japanese theorem as a rigid linear invariant and supplies arbitrarily near-cyclic counterexamples for every nonlinear power objective.

## Limitations

- The scalar transform is assumed continuous; no optimal regularity hypothesis is claimed.
- Only ordinary Euclidean planar finite point sets are covered.
- No constrained, weighted, surface, or higher-dimensional Delaunay analogue is claimed.
- Lambert 1994 was not directly inspected in full text and is the principal literature uncertainty.
- The theorem classifies unweighted separable objectives only; diagonal-weighted or other coupled objectives can satisfy nonlinear cyclic identities.

## Sources checked

- R. A. Johnson, *Modern Geometry: An Elementary Treatise on the Geometry of the Triangle and the Circle* (1929), Japanese theorem as summarized at https://mathworld.wolfram.com/JapaneseTheorem.html
- T. Lambert, *The Delaunay Triangulation Maximizes the Mean Inradius*, CCCG 1994, 201–206. https://dblp.org/rec/conf/cccg/Lambert94
- N. Minculete, C. Barbu, G. Szöllősy, *About the Japanese Theorem*, Crux Mathematicorum 38(5) (2012), 188–193. https://cms.math.ca/wp-content/uploads/crux-pdfs/CRUXv38n5.pdf
- V. A. Klyachin, E. G. Grigorieva, *Description of functionals that are minimized by Φ-triangulations*, 2017. https://www.mathnet.ru/eng/into220
- N. P. Dolbilin, H. Edelsbrunner, O. R. Musin, *On the Optimality of Functionals over Triangulations of Delaunay Sets*, Russian Mathematical Surveys 67(4) (2012), 781–783. https://arxiv.org/abs/1209.3541
