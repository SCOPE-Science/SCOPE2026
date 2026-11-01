# Exact John–Löwner ellipsoids of capped paraboloids and an invariant cone enclosure

## Finding
For every integer \(d\ge2\), the solid capped paraboloid
\[
K_d=\{(x,z)\in\mathbb R^{d-1}\times\mathbb R:\ \|x\|_2^2\le z\le1\}
\]
has the following unique maximum-volume inscribed (John) and minimum-volume enclosing (Löwner) ellipsoids. Write \(E(a,b,c)=\{(x,z):\|x\|_2^2/a^2+(z-c)^2/b^2\le1\}\), with transverse radius \(a>0\), axial radius \(b>0\) and axial center \(c\). Then
\[
J_d=E\left(\frac d{d+1},\frac{2d}{(d+1)^2},\frac{d^2+1}{(d+1)^2}\right),\quad
L_d=E\left(\frac d{\sqrt{d^2-1}},\frac d{d+1},\frac d{d+1}\right).
\]
Furthermore, the entire convex cone cap
\[
C_d=\{(x,z):0\le z\le1,\ \|x\|_2\le z\}
\]
is a proper subset of \(K_d\), yet **has exactly the same unique minimum-volume enclosing ellipsoid**: \(L(C_d)=L(K_d)=L_d\). Their exact enclosing-to-inscribed volume ratio is
\[
\mathcal R_d=\frac{\operatorname{vol}_d(L_d)}{\operatorname{vol}_d(J_d)}
=\frac{d+1}{2}\left(\frac{d+1}{d-1}\right)^{(d-1)/2},\qquad
\frac{\mathcal R_d}{d}\longrightarrow\frac e2.
\]
The John contacts are precisely the top pole and a full horizontal contact sphere; the Löwner contacts are precisely the lower vertex and the top rim sphere.

## Assumptions and scope
The dimension is any integer \(d\ge2\). The ambient Euclidean structure is standard. A John ellipsoid means a full-dimensional ellipsoid **contained** in the compact convex body with maximal \(d\)-volume; a Löwner ellipsoid means a full-dimensional ellipsoid **containing** the body with minimal \(d\)-volume. The balls and spheres in the formulas are Euclidean, not surface-area measures on the paraboloid. Equality of enclosing ellipsoids is an exact equality of subsets of ambient space, rather than equality of their volumes alone.

The body has nonempty interior (for example at \(x=0\) and \(0<z<1\)); the stated formulas are therefore nondegenerate. The two-dimensional case is included. The result also gives the extremal ellipsoids of every invertible affine image of \(K_d\) by affine equivariance; it does not claim a classification of arbitrary quadratic epigraph truncations.

## Proof
**1. Symmetry and candidates.** Rotations of the \(x\)-coordinates fix \(K_d\). The existence and uniqueness theorems for extremal ellipsoids imply both extremal ellipsoids are rotationally symmetric, hence of the form \(E(a,b,c)\). We establish explicit containment and optimal contact measures, which prove maximality/minimality among *all* ellipsoids, not only rotationally invariant candidates.

**2. Inner containment and the exact tangency identity.** Put
\[
a=\frac d{d+1},\quad b=\frac{2d}{(d+1)^2},\quad c=\frac{d^2+1}{(d+1)^2},\quad z_0=\frac{d-1}{d+1}.
\]
The ellipsoid's axial range is \([c-b,c+b]=[z_0^2,1]\), entirely inside \([0,1]\). At height \(z\) in that range, its maximal squared transverse radius is \(a^2(1-(z-c)^2/b^2)\). Direct expansion yields the *identity*
\[
z-a^2\left(1-\frac{(z-c)^2}{b^2}\right)
=\frac{(d+1)^2}{4}(z-z_0)^2\ge0.
\]
Thus \(J_d\subseteq K_d\). Equality with the curved wall occurs precisely at \(z=z_0\), where \(\|x\|_2=\sqrt{z_0}\); the flat cap also touches at the top pole \((0,1)\).

**3. An exact John contact certificate.** Apply the invertible affine map \((x,z)\mapsto(x/a,(z-c)/b)\) sending \(J_d\) to the unit ball. Its upper contact maps to \(u_+=(0,1)\). The curved contact sphere maps to
\[
u_-(\theta)=\left(\sqrt{1-d^{-2}}\,\theta,-\frac1d\right),
\qquad \theta\in S^{d-2}.
\]
Assign weight \(1/(d+1)\) to \(u_+\) and \(d/(d+1)\) to normalized uniform measure on \(u_-(\theta)\). The total-weight-one measure has
\[
\mathbb E[u]=0,\qquad \mathbb E[uu^T]=\frac1d I_d.
\]
Indeed the axial mean is \(1/(d+1)-1/(d+1)=0\), the axial second moment is \((1+d^{-1})/(d+1)=1/d\), and the transverse block is \(\frac d{d+1}(1-d^{-2})I_{d-1}/(d-1)=I_{d-1}/d\). Multiplication of the weights by \(d\) gives the standard John conditions \(\sum\lambda_i u_i=0\) and \(\sum\lambda_i u_iu_i^T=I_d\). A finite certificate is obtained by replacing uniform measure with the equally weighted \(2(d-1)\) vectors \(\theta=\pm e_j\). John's contact theorem therefore proves that \(J_d\) is the unique maximum-volume inscribed ellipsoid.

**4. Outer containment and equality with the cone.** Put
\[
A=\frac d{\sqrt{d^2-1}},\qquad B=C=\frac d{d+1}.
\]
For every \((x,z)\in K_d\), \(0\le z\le1\) and \(\|x\|_2^2\le z\). Therefore its outer-ellipsoid quadratic form is bounded by
\[
\frac{\|x\|_2^2}{A^2}+\frac{(z-C)^2}{B^2}
\le g(z):=\frac z{A^2}+\frac{(z-C)^2}{B^2}.
\]
The function \(g\) is strictly convex and satisfies \(g(0)=g(1)=1\). The chord inequality for convex functions implies \(g(z)\le1\) throughout \([0,1]\), proving \(K_d\subseteq L_d\). Strict convexity shows that contact with \(L_d\) can occur only at \(z=0\) or \(z=1\). At \(z=0\), the sole point of \(K_d\) is \((0,0)\); at \(z=1\), the quadratic form equals one precisely when \(\|x\|_2=1\). Both contact sets are also on the cone \(C_d\). Moreover \(C_d\subsetneq K_d\): for example \(z=1/4\) and \(\|x\|_2=3/8\) belong to \(K_d\) but not \(C_d\).

**5. An exact Löwner contact certificate.** Normalize \(L_d\) to the unit ball by \((x,z)\mapsto(x/A,(z-C)/B)\). The bottom contact maps to \(v_-=(0,-1)\), and the rim maps to
\[
v_+(\theta)=\left(\sqrt{1-d^{-2}}\,\theta,\frac1d\right),
\qquad\theta\in S^{d-2}.
\]
Assign total weight \(1/(d+1)\) to \(v_-\) and \(d/(d+1)\) to uniform rim directions. Their weighted barycenter is zero, their axial second moment is \(1/d\), and their transverse covariance is \(I_{d-1}/d\). Thus this measure satisfies the sufficient and necessary Löwner-contact identities. Replacing the uniform rim with the finite \(\pm e_j\) design is again possible. The contact theorem proves uniqueness and minimality of \(L_d\) for \(K_d\). Because *the same contact certificate* lies on \(C_d\) and \(C_d\subseteq L_d\), it simultaneously certifies \(L(C_d)=L_d\).

**6. Volume calculation and asymptotics.** An ellipsoid \(E(a,b,c)\) has volume \(\kappa_d a^{d-1}b\), independent of its center. The transverse semiaxis ratio equals \(A/a=\sqrt{(d+1)/(d-1)}\) and the axial ratio equals \(B/b=(d+1)/2\). Their product gives the stated exact \(\mathcal R_d\). As \(d\to\infty\), \(((d+1)/(d-1))^{(d-1)/2}\to e\), so \(\mathcal R_d/d\to e/2\).

## Verification
The standalone Python program `verify.py` implements the explicit formulas for ten dimensions, tests the exact squared-radius identity on 10,001 axial sample locations per dimension, checks 10,001 enclosure sections per dimension, checks the explicit normalized contact algebra, verifies volume-ratio identities, and independently optimizes the rotationally symmetric ellipsoid parameters numerically in dimensions \(2,3,5,8\). Command: `python verify.py`; dependencies: Python 3, NumPy, SciPy. The recorded successful run reported 8 optimization matches with maximum relative parameter discrepancy approximately \(3.85\times10^{-8}\). The exact identity and contact-measure argument above, not these numerical experiments, prove the all-dimensional statement.

## Relationship to prior work
The contact characterization is standard in Löwner–John theory. Güler and Gürtuna (2007), particularly its sections on truncated ellipsoids and second-order cones, is a closely related primary reference. Its cut-ellipsoid (ball/slab) calculations do **not** address quadratic epigraph caps. Its circular-cone enclosing results can determine the outer ellipsoid of the *smaller cone* \(C_d\), but do not imply the equality \(L(K_d)=L(C_d)\) for the strictly larger quadratic cap: that equality requires the explicit convex-chord containment proof above. The present result additionally supplies the John ellipsoid of \(K_d\), both exact contact geometries and a sharp dimension-dependent volume ratio. Gruber and Schuster (2012) give a modern proof of the contact characterization. Text and theorem comparisons found no matching published formula in the literature inspected, but absence from search does not establish universal historical priority.

## Limitations
Only the normalized circular quadratic epigraph truncated at height one (and its affine images) is classified. The theorem makes no claim about arbitrary paraboloid intersections, nonquadratic powers, or unbounded epigraphs. An independent audit has not been performed; older or unindexed literature might independently contain an equivalent special case. Numerical optimization and finite sampling are corroboration only; they do not certify unsampled dimensions or points.

## References
1. O. Güler and F. Gürtuna, *The extremal volume ellipsoids of convex bodies, their symmetry properties, and their determination in some special cases*, arXiv:0709.0707 (first version September 5, 2007). Full-text primary comparison, especially sections 7–8. https://arxiv.org/abs/0709.0707
2. P. M. Gruber and F. E. Schuster, *An arithmetic proof of John's ellipsoid theorem*, arXiv:1207.7246 (2012). Contact-theorem background. https://arxiv.org/abs/1207.7246
