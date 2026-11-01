# Finite stabilization of polyhedral translate depth with a sharp box cutoff

## Finding
For every integer \(d\ge2\), let \(K\subset\mathbb R^d\) be a full-dimensional compact convex polytope with an **irredundant** facet representation
\[
K=\{x:\langle u_j,x\rangle\le h_j,\quad j=1,\ldots,m\},\qquad \|u_j\|_2=1.
\]
For the facet \(F_j=\{x\in K:\langle u_j,x\rangle=h_j\}\), select any \(p_j\in\operatorname{relint}(F_j)\). Define the strictly positive facet-clearance parameter
\[
\eta=\min_{1\le j\le m}\min_{i\ne j}\big(h_i-\langle u_i,p_j\rangle\big)>0.
\]
For any Borel probability law \(\mu\) supported in a Euclidean ball of radius \(R\ge0\), and any real \(t>0\) satisfying \(t\eta\ge 2R\), its depth defined by translates of \(tK\) satisfies, **simultaneously for every query point** \(y\in\mathbb R^d\),
\[
\boxed{\mathsf d_{tK}(y;\mu)=\min_{1\le j\le m}\mu\{x:\langle u_j,x\rangle\ge\langle u_j,y\rangle\}.}
\]
This is equality at a finite, explicitly bounded dilation—not merely convergence as the testing polytope grows.

At every level \(0<\alpha\le1\), put
\[
q_j(\alpha)=\sup\{s\in\mathbb R:\mu\{x:\langle u_j,x\rangle\ge s\}\ge\alpha\}.
\]
All these upper quantiles are finite, and the exact level region becomes the (possibly empty) polytope
\[
\boxed{D_\alpha^{tK}(\mu)=\bigcap_{j=1}^{m}\{y:\langle u_j,y\rangle\le q_j(\alpha)\}.}
\]
There is no independence, smooth-density, or boundary-null assumption.

**Sharp box case.** Let \(K=\prod_{i=1}^d[0,\ell_i]\), \(\ell_i>0\), and suppose \(\mu\) is supported in \(B=\prod_{i=1}^d[a_i,a_i+w_i]\), \(w_i\ge0\). Then the preceding exact depth and contour formulas hold already when
\[
\boxed{t\ge T_B:=\max_i\frac{w_i}{\ell_i}.}
\]
This cutoff is the smallest **universal** scale valid for all probability laws supported in the prescribed box and all query points. For positive widths the lower bound is witnessed by a uniform measure along a segment in a maximally restrictive coordinate direction; if all widths are zero the infimum cutoff is zero and any \(t>0\) works.

## Assumptions and scope
The depth convention is exactly
\[
\mathsf d_{C}(y;\mu)=1-\sup_{z:\,y\notin C+z}\mu(C+z),
\]
with closed translates and strict exclusion of \(y\). The underlying dimension is finite and at least two. The measure has compact support, but may be atomic, singular or dependent across coordinates. Facet normals are outer unit normals and every inequality in the display for \(K\) is facet-defining; otherwise the clearance parameter need not be positive. A zero-radius enclosing ball is allowed provided \(t>0\).

## Proof
**1. Universal upper bound on missing-translate mass.** If a translate \(tK+z\) misses \(y\), some facet inequality is violated:
\[
\langle u_j,y\rangle>t h_j+\langle u_j,z\rangle=:a.
\]
Since the entire translate lies in \(H_j(a)=\{x:\langle u_j,x\rangle\le a\}\), its mass is at most \(\mu\{x:\langle u_j,x\rangle<\langle u_j,y\rangle\}\). Hence
\[
\sup_{z:y\notin tK+z}\mu(tK+z)\le\max_j\mu\{x:\langle u_j,x\rangle<\langle u_j,y\rangle\}.
\]

**2. Exact finite realization of each facet halfspace on the support.** Translate coordinates so that \(\operatorname{supp}\mu\subset B_R(0)\). Fix a facet \(j\) and a real cutoff \(a\in[-R,R]\). Consider
\[
T_{j,a}=a u_j+t(K-p_j).
\]
The \(j\)-th inequality for this translate is precisely \(\langle u_j,x\rangle\le a\). For every other inequality \(i\ne j\), any \(x\in B_R(0)\) satisfies
\[
\langle u_i,x-a u_j\rangle\le R+|a|\le2R\le t\big(h_i-\langle u_i,p_j\rangle\big).
\]
Thus the other constraints cannot exclude any point of \(B_R(0)\), and
\[
\boxed{T_{j,a}\cap B_R(0)=H_j(a)\cap B_R(0).}
\]
If \(a<\langle u_j,y\rangle\), the translate misses \(y\). Therefore it realizes the entire halfspace mass \(\mu(H_j(a))\) with an admissible translate.

The supremum of these masses as \(a<\langle u_j,y\rangle\) is \(\mu\{x:\langle u_j,x\rangle<\langle u_j,y\rangle\}\), by continuity from below. It suffices to use \(a\in[-R,R]\): a lower cutoff has zero mass (except at the endpoint \(-R\), which is included), while any cutoff above \(R\) may be replaced by \(R\) without loss of mass and while remaining strictly below the query projection. This is valid even if \(\mu\) has atoms on supporting hyperplanes. Together with step 1 it proves the stated depth formula.

**3. Quantile level regions.** For \(\alpha>0\), the condition \(\mathsf d_{tK}(y;\mu)\ge\alpha\) is equivalent to \(\mu\{x:\langle u_j,x\rangle\ge\langle u_j,y\rangle\}\ge\alpha\) for every facet. For compactly supported laws, continuity of measures under decreasing closed upper-ray events shows that each inequality is equivalent to \(\langle u_j,y\rangle\le q_j(\alpha)\). This proves the contour identity.

**4. Improved cutoff for boxes.** If \(t\ell_i\ge w_i\) in every coordinate, a testing box with its \(j\)-th upper face at \(a\in[a_j,a_j+w_j]\) can cover the whole support-box extent in all other coordinates while having \(j\)-th interval \([a-t\ell_j,a]\). Its intersection with the support is exactly the half-box \(\{x\in B:x_j\le a\}\); the lower-face construction similarly realizes \(\{x\in B:x_j\ge a\}\). Outside the support projection range, the cutoff may be clamped to its nearest endpoint. The universal upper bound in step 1 therefore becomes equality at \(t\ge T_B\).

To prove optimality **uniformly over supported laws**, suppose \(t<T_B\) and choose \(j\) with \(L:=t\ell_j<w_j\). Let \(\mu\) be uniform on the segment parallel to coordinate \(j\) from \(a_j\) to \(a_j+w_j\), all other coordinates fixed at points inside their intervals. Choose a query \(y\) with the same fixed other coordinates and
\[
a_j+\max\{L,w_j/2\}<y_j<a_j+w_j.
\]
The largest halfspace mass excluding \(y\) is \((y_j-a_j)/w_j>L/w_j\), while any translated testing box missing \(y\) either misses the entire supporting segment via another coordinate or meets that segment in length at most \(L\). Thus its captured probability is at most \(L/w_j\), a strict gap. No smaller universal scale can work.

## Verification
The standalone program `verify_polyhedral_depth.py` uses exact rational arithmetic and deterministic sample points, weights and query points. It checks explicit facet-translate witnesses against the corresponding facet-halfspace counts for a square, triangle, diamond and three-dimensional octahedron; it also checks rational witnesses for sharpness below the box cutoff. Run `python verify_polyhedral_depth.py` in the directory containing this document. The program reports 9,342 successful exact checks and four sharpness witnesses; only the analytic proof establishes the infinite quantified theorem.

## Relationship to prior work
Molchanov and Nagy introduce the translated-convex-body depth and show convergence of its dilation limit to a tangent-cone depth under a boundary-null hypothesis (Theorem 5.2). Their discussion also identifies polyhedral computational arrangements, but does not establish an all-point finite stopping threshold, the facet-normal quantile equality for all compactly supported measures including atoms, or the optimal universal width cutoff for a parallelotope. The present statement is a **finite-scale sharpening in the polyhedral regime**, not a replacement for their broader asymptotic theory. The halfspace and projection-quantile principles are standard and are not asserted as novel individually.

## Limitations
The bound \(2R/\eta\) is sufficient and generally not claimed optimal; its value depends on selected facet interior points. Compact support is essential to a universal finite threshold of this form. The displayed quantile contours are not asserted to characterize the original distribution. Nothing here establishes finite stopping for an arbitrary smooth or nonpolyhedral testing body. Historical-priority searches cannot establish absolute uniqueness; independent review has not occurred.

## References
1. I. Molchanov and S. Nagy, *Depth based on translates of a convex body: geometry, floating bodies, and empirical theory*, arXiv:2610.26108v1, first submitted 19 October 2026, Sections 2.2, 5.1–5.2 and 7.4. https://arxiv.org/html/2610.26108v1
2. S. Nagy, C. Schütt and E. M. Werner, *Halfspace depth and floating body*, Statistics Surveys 13 (2019), 52–118; background for the established halfspace-depth notion. https://doi.org/10.1214/19-SS123
