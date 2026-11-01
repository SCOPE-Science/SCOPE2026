# Loewner rigidity and an exact angular orphan law for two-site anisotropic Voronoi cells

## Finding

For two distinct sites in the Euclidean plane, endowed with **independently assigned positive-definite quadratic distance metrics**, star-shapedness of each full-plane Voronoi cell at its own site is equivalent to a Loewner inequality between the two metric matrices. In particular, **both cells are star-shaped at their sites if and only if the two matrices coincide**.

When the matrices are incomparable in Loewner order, exactly one cell has a disconnected orphan component for every relative site displacement except two exceptional unoriented lines (four oriented rays). For a uniformly random displacement direction, the probability of which cell has the orphan is an explicit arctangent of two matrix eigenvalues. The result is independent of the length of the site displacement.

Write \(A,B\) for real symmetric positive-definite \(2\times2\) matrices, and take sites \(0,p\), where \(p\ne0\). Define
\[
 d_0(x)^2=x^\top Ax,\qquad d_p(x)^2=(x-p)^\top B(x-p),\qquad
 C_0=\{x:d_0(x)^2\le d_p(x)^2\},\quad C_p=\{x:d_p(x)^2\le d_0(x)^2\}.
\]
Then \(C_0\) is star-shaped at \(0\) exactly when \(A-B\succeq0\), and \(C_p\) is star-shaped at \(p\) exactly when \(B-A\succeq0\). In either star-shaped case, the corresponding cell is actually convex.

Suppose \(H=A-B\) is indefinite. Put
\[
 K=(B^{-1}-A^{-1})^{-1},\qquad \eta=p^\top Kp.
\]
The matrix \(K\) is well defined, symmetric, and indefinite. If \(\eta>0\), precisely \(C_p\) has two connected components; if \(\eta<0\), precisely \(C_0\) has two connected components. The component not containing its site is an orphan. If \(\eta=0\), both closed cells are connected but each has two sectors meeting at a single boundary point. These are the only exceptional displacement directions.

Let \(\lambda_+>0\) and \(-\mu<0\) be the eigenvalues of \(K\). If the direction of \(p\) is uniform on the unit circle and its length is arbitrary and positive, then
\[
 \Pr(C_0\text{ has an orphan})=\frac2\pi\arctan\sqrt{\frac{\mu}{\lambda_+}},
 \qquad
 \Pr(C_p\text{ has an orphan})=1-\frac2\pi\arctan\sqrt{\frac{\mu}{\lambda_+}}.
\]
The probability that neither cell has a disconnected orphan is zero. This is a *whole-plane* theorem: clipping the diagram to a bounded observation window can remove remote orphan components.

## Assumptions and scope

The plane is \(\mathbb R^2\), both site matrices are fixed positive-definite symmetric matrices, and site distance is the square root of the associated **site-assigned** quadratic form. Cells are closed full-plane sublevel sets, with common bisector included in both. Star-shapedness is always about the cell's generating site, not some unspecified center. Connected components are components of the closed cells. In the angular law the matrices are fixed; only the direction of the nonzero relative displacement is isotropic. We make no bounded-domain, multi-site, or location-dependent-metric claim.

## Proof

**1. Quadratic reduction and signs at the sites.** Write \(H=A-B\), \(b=Bp\), and \(c=p^\top Bp>0\). The difference of squared distances is
\[
 q(x)=d_0(x)^2-d_p(x)^2=x^\top Hx+2b^\top x-c.
\]
Thus \(C_0=\{q\le0\}\), \(C_p=\{q\ge0\}\), \(q(0)=-c<0\), and \(q(p)=p^\top Ap>0\). Also \(b\ne0\).

**2. Exact star-shapedness criterion.** If \(H\succeq0\), then \(q\) is convex and \(\{q\le0\}=C_0\) is convex, hence star-shaped at \(0\). Conversely suppose \(H\) has a negative eigenvalue and \(C_0\) were star-shaped at \(0\). For every direction \(u\) with \(u^\top Hu<0\), the term \(t^2u^\top Hu\) forces \(q(tu)<0\) for all sufficiently large positive \(t\). Star-shapedness then forces \(q(tu)\le0\) for **every** \(t\ge0\). If \(H\preceq0\) with a negative eigenvalue, the negative directions are dense in the unit circle (or comprise the whole circle). By continuity \(q\le0\) everywhere, contrary to \(q(p)>0\). If \(H\) is indefinite, its negative cone has two distinct null-line boundary directions \(u,v\). By closure, \(q(tu)\le0\) and \(q(tv)\le0\) for every real \(t\), using both signs of each direction. Since \(u^\top Hu=v^\top Hv=0\), these inequalities say \(2t b^\top u-c\le0\) and \(2t b^\top v-c\le0\) for every real \(t\), forcing \(b^\top u=b^\top v=0\). Distinct null lines span \(\mathbb R^2\), so \(b=0\), contradiction. Therefore \(H\succeq0\) is necessary. Exchanging the sites and the two matrices gives the criterion for \(C_p\). Both inequalities hold exactly when \(A=B\).

**3. Indefinite phase diagram.** Assume \(H\) has one positive and one negative eigenvalue. Completing the square gives
\[
 q(x)=(x+H^{-1}b)^\top H(x+H^{-1}b)-\eta,
 \qquad \eta=c+b^\top H^{-1}b.
\]
The identity
\[
 B+BH^{-1}B=BH^{-1}A=(B^{-1}-A^{-1})^{-1}=K
\]
proves \(\eta=p^\top Kp\). The inverse difference \(B^{-1}-A^{-1}\) is congruent in inertia to \(H\) (equivalently, \(K\) has one eigenvalue of each sign), because \(\det K=\det A\det B/\det H<0\). Orthogonally diagonalizing \(H\) reduces \(q\) to \(\alpha s^2-\beta t^2-\eta\), with \(\alpha,\beta>0\). If \(\eta>0\), the superlevel set \(q\ge0\) consists of two disjoint hyperbola branches, whereas the sublevel set \(q\le0\) is connected. If \(\eta<0\), the sublevel set consists of two branches and the superlevel set is connected. If \(\eta=0\), the sets are pairs of opposite closed wedges, each connected through their common apex. Since \(q(0)<0<q(p)\), the site of any disconnected cell belongs to exactly one branch, leaving the other an orphan. The zero set of the indefinite form \(p^\top Kp\) is exactly two lines, giving four exceptional rays.

**4. Exact random-orientation law.** Orthogonal coordinates in which \(K=\operatorname{diag}(\lambda_+,-\mu)\) give, for \(p=r(\cos\theta,\sin\theta)\),
\[
 \eta=r^2\bigl(\lambda_+\cos^2\theta-\mu\sin^2\theta\bigr).
\]
The condition \(\eta<0\) is \(|\tan\theta|>\sqrt{\lambda_+/\mu}\). Its angular measure is \(4\arctan\sqrt{\mu/\lambda_+}\) in a full circle of length \(2\pi\). The two exceptional lines have zero Haar measure. These facts give both probabilities, independently of \(r\).

**5. Attainability of all three phases.** Take \(A=\operatorname{diag}(2,1/2)\), \(B=I\), giving \(H=\operatorname{diag}(1,-1/2)\), \(K=\operatorname{diag}(2,-1)\). For \(p=(1,0)\), \(\eta=2>0\); for \(p=(0,1)\), \(\eta=-1<0\); and for \(p=(1,\sqrt2)\), \(\eta=0\). The first has an orphan of \(C_p\), the second an orphan of \(C_0\), and the third the connected double-cone transition. For these matrices the exact probability of an orphan of \(C_0\) is \(2\arctan(1/\sqrt2)/\pi\).

## Verification

The self-contained script `verify.py` checks algebraic identities with rational matrices, verifies three explicit topological phases and ray reentry at prescribed points, and compares a deterministic angular count with the proved formula. Run `python verify.py` using Python 3. No external packages or network are needed. The proof above is analytic, not inferred from the finite checks.

## Relationship to prior work

Venkovic and Anzt (2026) derive Minkowski-tensor formulas for site-star-shaped planar anisotropic Voronoi cells. Their framework explicitly isolates star-convexity as a prerequisite and acknowledges that general anisotropic cells can be disconnected. The theorem here characterizes this prerequisite exactly for the entire two-site plane and quantifies the generic topological failure when the two metrics are incomparable. Labelle and Shewchuk (2003) prove visibility *within a specified wedge* and sufficient conditions for multi-site diagrams; they also note that orphan components can appear far from their sites. Canas and Gortler (2011) give metric-variation and sampling conditions sufficient for orphan-free diagrams. Those statements do not provide the present full-plane Loewner iff condition or the eigenvalue-dependent angular orphan law. The conic-section classification and the elementary probability calculation are acknowledged as standard components; the finding is their exact linkage to site-anchored quadratic Voronoi geometry and its sharp random-orientation phase boundary.

## Limitations

The result does not describe clipped or periodic Voronoi cells, more than two sites, or a continuously varying metric field. A connected cell can fail to be star-shaped at its site; connectedness and star-shapedness must not be conflated. The angular law concerns Haar-uniform directions only; anisotropic displacement sampling would alter the probabilities. No claim is made of independent validation or definitive historical priority; earlier conic Voronoi treatments could contain equivalent special cases.

## References

- N. Venkovic and H. Anzt, *Minkowski Tensors of Planar Anisotropic Voronoi Diagrams* (2026), arXiv:2610.08656, https://arxiv.org/abs/2610.08656 (first posted 2026-10-06).
- F. Labelle and J. R. Shewchuk, *Anisotropic Voronoi Diagrams and Guaranteed-Quality Anisotropic Mesh Generation*, SoCG 2003, https://www.ljll.fr/~frey/papers/meshing/Labelle%20F.%2C%20Anisotropic%20Voronoi%20diagrams%20and%20guaranteed-quality%20anisotropic%20mesh%20generation.pdf.
- G. D. Canas and S. J. Gortler, *Orphan-Free Anisotropic Voronoi Diagrams* (2011), arXiv:1102.3670, https://arxiv.org/abs/1102.3670.
