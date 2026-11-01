# Minimal tangent-ball radii and far-contact foliation of Euclidean ellipsoids

## Finding

Let \(n\ge2\), let \(A\) be a real symmetric positive-definite \(n\times n\) matrix, and let \(E=c+A\mathbb B_2^n\). Denote the largest and smallest eigenvalues of \(A\) by \(a\) and \(b\), and its top eigenspace by \(W=\ker(A-aI)\). For each \(u\in\mathbb S^{n-1}\), set
\[
 s(u)=c+Au,\qquad q(u)=\|A^{-1}u\|_2,\qquad \nu(u)=\frac{A^{-1}u}{q(u)}.
\]
Here \(\nu(u)\) is the outward unit normal of \(E\) at \(s(u)\). Define \(R_*(u)\) to be the infimum of the radii \(r>0\) for which the *inward* tangent Euclidean ball \(\overline B(s(u)-r\nu(u),r)\) contains the entire ellipsoid. Then the infimum is attained and
\[
 \boxed{R_*(u)=a^2\|A^{-1}u\|_2.}\tag{1}
\]
Equivalently, writing the boundary point by its outward unit normal \(\nu\) and denoting the centered ellipsoid support by \(h_{E-c}(\nu)=\|A\nu\|_2\),
\[
 \boxed{R_*(\nu)h_{E-c}(\nu)=a^2,\qquad R_*(\nu)=\frac{a^2}{\|A\nu\|_2}.}\tag{2}
\]
Consequently the least enclosing tangent-ball radius ranges *exactly* over \([a,a^2/b]\) as the contact point varies. The sharp constant global supporting radius is \(a^2/b\); this global constant is a known earlier result, not a novelty claim here.

At the sharp radius, the set of *additional* ellipsoid–sphere contact points (different from \(s(u)\)) is exactly
\[
 \boxed{\left\{c+A\bigl(u-2\langle u,z\rangle z\bigr):
 z\in W,\ \|z\|_2=1,\ \langle u,z\rangle>0\right\}.}\tag{3}
\]
It is nonempty exactly when the orthogonal projection of \(u\) to \(W\) is nonzero. If \(a\) is simple there is exactly one additional contact for \(\langle u,e\rangle\ne0\), namely the reflection of \(u\) across the hyperplane perpendicular to a major-axis unit eigenvector \(e\). When \(u\perp W\), (1) is nevertheless sharp although there is *no* additional distinct contact: sharpness is attained only as a limit of short secants.

For the largest principal *local* radius of curvature at \(s(u)\), one has
\[
 R_{\mathrm{loc}}(u)=q(u)\max_{\substack{z\perp u\\\|z\|_2=1}}\|Az\|_2^2\ \le R_*(u).
\]
Equality holds if and only if \(W\cap u^\perp\ne\{0\}\); strict inequality is possible precisely for a simple top eigenvalue and a contact parameter with nonzero major-axis component. At a major-axis tip of an ellipsoid with strictly longest axis \(a>a_2\),
\[
 R_*=a,\qquad R_{\mathrm{loc}}=\frac{a_2^2}{a},\qquad \frac{R_*}{R_{\mathrm{loc}}}=\frac{a^2}{a_2^2}.
\]
This nonlocal-to-local gap is unbounded within ellipsoids of a fixed dimension. It demonstrates that local osculating curvature at a *single prescribed point* need not determine the minimal ball containing the *entire* body and tangent there.

## Assumptions and scope

The ambient norm is Euclidean; \(A\succ0\) is symmetric, with arbitrary eigenvalue multiplicities; the ellipsoid is full-dimensional. The center \(c\) may be any point. The result is pointwise for each contact location and holds in every dimension at least two. A tangent ball means its center lies on the inward normal ray and its boundary contains the prescribed boundary point. The radius \(R_*(u)\) is not the radius of the unconstrained minimum enclosing ball, and the extremal supporting ball does not generally have the same center as the ellipsoid.

The earlier global constant-radius strong-convexity threshold \(a^2/b\) is background. The substantive classification here concerns the minimal *variable* radius at every boundary point, all of its remote sharp-contact partners, and exactly when this pointwise global constraint exceeds the principal local curvature radius.

## Proof

**1. Exact containment quotient.** Fix \(u\in\mathbb S^{n-1}\), put \(s=c+Au\), \(q=\|A^{-1}u\|\), and \(\nu=A^{-1}u/q\). For \(v\in\mathbb S^{n-1}\) distinct from \(u\), set \(y=c+Av\) and \(w=u-v\). The elementary sphere inequality gives
\[
 y\in\overline B(s-r\nu,r)
 \quad\Longleftrightarrow\quad
 \|A(u-v)\|_2^2\le 2r\langle\nu,A(u-v)\rangle.
\]
Because \(\langle\nu,Aw\rangle=\langle u,w\rangle/q=\|w\|_2^2/(2q)\) for unit \(u,v\), this becomes
\[
 r\ge q\,\frac{\|Aw\|_2^2}{\|w\|_2^2}.\tag{4}
\]
Checking all \(v\) on the boundary suffices, because both the ellipsoid and the Euclidean ball are convex and the ellipsoid is the convex hull of its boundary.

**2. All secant directions and exact extremum.** Every normalized secant direction \(z=(u-v)/\|u-v\|\) satisfies \(\langle u,z\rangle>0\). Conversely, for every unit \(z\) with \(\langle u,z\rangle>0\), the reflection \(v=u-2\langle u,z\rangle z\) has norm one, differs from \(u\), and gives normalized secant direction \(z\). Thus the maximal quotient in (4) is
\[
 q\sup_{\substack{\|z\|=1\\\langle u,z\rangle>0}}\langle z,A^2z\rangle.
\]
The open hemisphere is dense up to its equator and contains a representative approaching every one-dimensional direction (if needed by perturbation); since \(A^2\) is positive-definite, the supremum is its largest eigenvalue \(a^2\), independently of \(u\). Therefore every prescribed tangent ball contains \(E\) exactly when \(r\ge a^2q\). This proves existence, sharpness and (1).

**3. Remote equality and complete contact set.** At the threshold \(r=a^2q\), equality for a distinct \(v\) in (4) holds precisely when the nonzero secant \(u-v\) lies in \(W\), the maximal eigenspace of \(A^2\). Applying the preceding bijective secant parametrization gives precisely (3). Such \(z\) exists if and only if \(P_Wu\ne0\). If \(W\) is one-dimensional, positive inner product fixes its orientation and hence fixes the distinct partner \(v\). If \(P_Wu=0\), no equality direction belongs to the open hemisphere, but maximal Rayleigh quotient \(a^2\) is still approached along secants; no smaller radius encloses the ellipsoid. This also covers the round-ball case \(A=aI\): all other boundary points are sharp contacts.

**4. Normal/support representation and extrema.** The support point with outer normal \(\nu\) is \(s=c+A^2\nu/\|A\nu\|\). Writing \(u=A\nu/\|A\nu\|\), one obtains \(q=1/\|A\nu\|\), giving (2). The values of \(q\) on the sphere fill the interval \([1/a,1/b]\) (constant when \(a=b\)); (1) therefore ranges over \([a,a^2/b]\).

**5. Local curvature and exact gap.** Tangent directions to the unit parameter sphere at \(u\) are \(z\perp u\). Along any smooth unit-sphere curve \(v(t)\) through \(u\) with derivative \(z\), the limit of (4) is \(q\|Az\|^2/\|z\|^2\). The maximal such limiting quotient is the largest local principal radius of curvature. This identifies \(R_{\mathrm{loc}}\) and makes the comparison with \(a^2q\) exact. A Rayleigh quotient reaches \(a^2\) on the tangent plane if and only if the tangent plane intersects \(W\) nontrivially. If \(\dim W\ge2\), it always does; if \(\dim W=1\), it does exactly when \(u\perp W\). For \(u=e\), a major-axis eigenvector with unique largest semiaxis, \(q=1/a\) and the largest tangential eigenvalue is \(a_2^2\), giving the displayed ratio, which diverges as \(a/a_2\to\infty\). This completes the proof.

## Verification

The standalone standard-library program `verify.py` performs exact-rational checks, not floating-point curve fitting. Rational unit vectors are generated by stereographic parametrization. The code tests the equivalent Rayleigh containment inequalities for a collection of two- through four-dimensional ellipsoids, including repeated maximal axes and spheres, checks reflected secondary contacts, verifies several exact local/global ratios, and tests a sequence of near-equatorial secants for sharpness without a second contact. Executing the embedded program gives `PASS: 2023 exact-rational checks`. These finite checks are supplementary; the proof above supplies the universal quantifiers.

## Relationship to prior work

Nour (arXiv:2610.28789v1, first public 2026-10-20) studies variable-radius spherical support and the canonical intersections of tangent balls for general sets, but does not tabulate the pointwise minimal ball radius or classify additional tangencies for ellipsoids. Nacry–Thibault (2024) develops variable-radius strong convexity and the general supporting-normal inequality, which is used here as background; their curvature lower bound is local and does not give the sharp nonlocal radius by itself. Weber–Reissig (2014, Example 3.9) expressly states the *global* constant-radius ellipsoid threshold \(a^2/b\) in equivalent matrix notation, with necessity and sufficiency. Formula (1) recovers that known global maximum but also resolves the distinct pointwise problem and its complete remote-contact structure. Earlier calculations of ellipsoidal principal curvature describe the local term and are not claimed as novel.

The pointwise formula and remote-contact classification were not identified in the inspected sources or available research records; these searches are not a proof of historical priority. If a source giving the same pointwise Rayleigh extremization and contacts is found, originality must be revisited by an independent literature review.

## Limitations

The result is specific to Euclidean ellipsoids and the requirement that the enclosing ball be tangent at a prescribed point with its center on the interior normal ray. It does not characterize arbitrary strongly convex sets or solve a general nonconvex variable-radius problem. General supporting-ball representations and the constant global radius were established earlier. Historical priority cannot be concluded merely from available search results.

## References

1. C. Nour, *Spherically Supported Sets with Variable Radii*, arXiv:2610.28789v1, 2026-10-20, https://arxiv.org/html/2610.28789v1.
2. F. Nacry and L. Thibault, *Strongly convex sets with variable radii*, Mathematical Control and Related Fields 14 (2024), 1530–1559, DOI:10.3934/mcrf.2024044. Author-accessible text: https://www.researchgate.net/publication/379613071_Strongly_convex_sets_with_variable_radii.
3. A. Weber and G. Reissig, *Classical and strong convexity of sublevel sets and application to attainable sets of nonlinear systems*, SIAM J. Control Optim. 52 (2014), 2857–2876, arXiv:1311.4989v2, Example 3.9, https://arxiv.org/html/1311.4989v2.
4. N. M'Arthur, *Principal radii of curvature at a point on an ellipsoid*, Edinburgh Mathematical Notes 24 (1929), xvi–xvii, DOI:10.1017/S1757748900001961.
