# Exact John ellipsoid of square fixed-cardinality assignment polytopes

## Finding

For all integers \(n\ge2\) and \(1\le k<n\), let the \(k\)-assignment polytope be
\[
P_{n,k}=\left\{X\in\mathbb R_{\ge0}^{n\times n}:
\sum_{i,j}X_{ij}=k,\quad
\sum_jX_{ij}\le1,\quad \sum_iX_{ij}\le1\right\}.
\]
This is the convex hull of the \(n\times n\) partial permutation matrices containing exactly \(k\) ones. Use the Frobenius Euclidean metric on its \((n^2-1)\)-dimensional affine hull.

Let \(J=\mathbf1\mathbf1^{\mathsf T}\), \(H=J/n\), and \(F=I-H\). On the linear space \(L=\{Y:\sum_{ij}Y_{ij}=0\}\), define orthogonal projections
\[
P_UY=FYH+HYF,\qquad P_WY=FYF.
\]
Their respective ranks are \(2(n-1)\) and \((n-1)^2\), and \(P_U+P_W=I_L\). Put \(C=(k/n^2)J\). The unique John ellipsoid (maximum-volume inscribed ellipsoid) of \(P_{n,k}\) is
\[
E_{n,k}=\left\{C+Y:\frac{\|P_UY\|_F^2}{u}+\frac{\|P_WY\|_F^2}{v}\le1\right\},
\]
where the squared principal semiaxes are
\[
(u,v)=\begin{cases}
\left(\dfrac{k^2}{n^2(n^2-1)},\dfrac{k^2}{n^2(n^2-1)}\right),
&k^2\le(n+1)(n-k)^2,\\[5pt]
\left(\dfrac{(n-k)^2}{n^2(n-1)},
\dfrac{k^2-2(n-k)^2}{n^2(n-1)^2}\right),
&k^2>(n+1)(n-k)^2.
\end{cases}
\]
Thus the ellipsoid is a Euclidean ball exactly when \(k\le n+1-\sqrt{n+1}\); otherwise \(v>u>0\). Its intrinsic Euclidean volume is
\[
\operatorname{vol}_{n^2-1}(E_{n,k})=
\kappa_{n^2-1}\,u^{n-1}v^{(n-1)^2/2},
\]
where \(\kappa_d=\pi^{d/2}/\Gamma(1+d/2)\) is the Euclidean unit-ball volume.

Every one of the \(n^2\) coordinate-nonnegativity facets is tangent to \(E_{n,k}\). Every row-sum and column-sum facet is also tangent precisely when \(k^2\ge(n+1)(n-k)^2\); these \(2n\) additional facets exist for \(1<k<n\). The threshold equality occurs at integer parameters exactly when \(n=h^2-1\) and \(k=h(h-1)\) for an integer \(h\ge2\).

In the anisotropic regime, the volume relative to the largest inscribed Euclidean ball of \(P_{n,k}\) is
\[
\frac{\operatorname{vol}_{n^2-1}(E_{n,k})}{\operatorname{vol}_{n^2-1}(B_{\mathrm{in}})}
=\left(\frac{k^2-2(n-k)^2}{(n-1)(n-k)^2}\right)^{(n-1)^2/2}>1.
\]

## Assumptions and scope

The assertion applies to every integer \(n\ge2\) and integer \(k\) satisfying \(1\le k<n\), not to the lower-dimensional perfect-matching endpoint \(k=n\) or to rectangular assignment polytopes. All stated ellipsoids are measured in the *affine-hull* Frobenius metric, not in an artificial full-dimensional ambient metric. The parameter \(k\) is a cardinality, never a continuous relaxation. The affine-hull dimension is \(d=n^2-1\) because the strictly positive matrix \(C\) has all row and column sums strictly below one. The defining halfspaces are exact by the integral network-flow description of assignments [1,2].

## Proof

**Step 1: orthogonal decomposition and support inequalities.** For a matrix \(Y\) whose entries sum to zero, the decomposition
\(Y=FYH+HYF+FYF\) is orthogonal for the Frobenius inner product. The first two terms have dimensions \(n-1\) each, and the last has dimension \((n-1)^2\). Row and column permutations and transposition preserve \(P_{n,k}\). Uniqueness of the John ellipsoid and this symmetry force its center to equal \(C\) and its covariance/shape operator to have the form
\(\Sigma=uP_U+vP_W\) with \(u,v>0\): the row-contrast and column-contrast summands have equivalent scalar coefficients under transpose, and the doubly-centered summand is a distinct irreducible component. Independently, the explicit contact certificate in Step 3 establishes unrestricted global optimality, without relying on this symmetry reduction.

Write \(p_{ij}=e_ie_j^{\mathsf T}-J/n^2\) for the projection of a coordinate normal to \(L\). Its squared projection norms are
\[
\|P_Up_{ij}\|_F^2=\frac{2(n-1)}{n^2},\qquad
\|P_Wp_{ij}\|_F^2=\frac{(n-1)^2}{n^2}.
\]
The distance from \(C\) to the coordinate facet \(X_{ij}=0\) in the support-function scale is \(s=k/n^2\). An ellipsoid with shape \(\Sigma\) is contained in all coordinate halfspaces if and only if
\[
\frac{2(n-1)}{n^2}u+\frac{(n-1)^2}{n^2}v
\le \frac{k^2}{n^4}.\tag{1}
\]
For a row constraint \(\sum_jX_{ij}\le1\), the projected normal is
\(r_i=(e_i-n^{-1}\mathbf1)\mathbf1^{\mathsf T}\), which has squared norm \(n-1\), belongs to \(\operatorname{im}P_U\), and has zero \(P_W\)-part. A column normal is analogous. The row/column support slack at \(C\) is \(t=(n-k)/n\). All these halfspaces contain the ellipsoid if and only if
\[
(n-1)u\le t^2,
\quad\text{equivalently}\quad
u\le\frac{(n-k)^2}{n^2(n-1)}.\tag{2}
\]
The H-representation [1,2] has no other necessary inequalities, so (1)--(2) are sufficient for containment.

**Step 2: exact maximum-volume shape.** Let
\[
a=\frac{2(n-1)}{n^2},\qquad
b=\frac{(n-1)^2}{n^2},\qquad
c=\frac{k^2}{n^4},\qquad
h=\frac{(n-k)^2}{n^2(n-1)}.
\]
The determinant of \(\Sigma\) on \(L\) is \(u^{2(n-1)}v^{(n-1)^2}\). Therefore the log-volume objective, up to constants, is
\(2(n-1)\log u+(n-1)^2\log v\), a strictly concave function on \(u,v>0\), subject to \(au+bv\le c\) and \(u\le h\). The first constraint binds because increasing \(v\) increases volume. The unconstrained optimum on \(au+bv=c\) is the round value
\(u=v=k^2/[n^2(n^2-1)]\). This is feasible if and only if
\(k^2\le(n+1)(n-k)^2\). If the inequality reverses, strict concavity makes the unique optimum lie on \(u=h\), yielding
\(v=[k^2-2(n-k)^2]/[n^2(n-1)^2]\).
In the second case, \(v-u=[k^2-(n+1)(n-k)^2]/[n^2(n-1)^2]>0\), proving positivity and the strict anisotropy statement. In both regimes (1) binds, while (2) binds exactly at and above the transition.

**Step 3: direct global John certificate.** For completeness, this step proves optimality against ellipsoids of *arbitrary* centers and shapes, not merely the invariant candidates. Regard \(\Sigma^{1/2}\) as the positive square root acting on \(L\). For each coordinate inequality, define the standardized contact point
\(z_{ij}=-\Sigma^{1/2}p_{ij}/s\).
It has unit length by the equality in (1), and corresponds to tangency on \(X_{ij}=0\). When (2) binds, define additional standardized row contacts
\(z_i^r=\Sigma^{1/2}r_i/t\) and analogous column contacts \(z_j^c\). They also have unit length.

Assign equal weights to all contact points in each orbit:
\[
w_0=\frac{s^2}{v}>0,\qquad
w_1=\frac{t^2}{nu}\left(1-\frac uv\right)\ge0.
\]
In the round regime use only the \(n^2\) coordinate contacts (then \(w_1=0\)). In the anisotropic regime \(w_1>0\), and each of the \(2n\) row/column contacts is present. At threshold, the extra row/column facets touch but zero weight is needed in the certificate.

Each contact orbit sums to zero, because
\(\sum_{i,j}p_{ij}=0\) and \(\sum_i r_i=\sum_j c_j=0\). The following exact operator identities hold on \(L\):
\[
\sum_{i,j}p_{ij}\otimes p_{ij}=I_L,\qquad
\sum_i r_i\otimes r_i+\sum_j c_j\otimes c_j=nP_U.
\]
Consequently the weighted contact second moment is
\[
\frac{w_0}{s^2}\Sigma+
\frac{nw_1}{t^2}\Sigma^{1/2}P_U\Sigma^{1/2}
=\frac{\Sigma}{v}+\left(1-\frac uv\right)P_U=I_L.
\]
Thus the weighted contacts have zero first moment and identity second moment. John's contact criterion [3] proves the candidate ellipsoid is **the unique maximum-volume inscribed ellipsoid** in the full affine dimension. This also independently certifies that the facet inequalities have been normalized correctly. The trace gives \(n^2w_0+2nw_1=n^2-1\), as required.

**Step 4: transition, contacts, and volume.** Equality in (1) proves coordinate tangency, while equality in (2) characterizes row/column tangency. The transition equation is
\(k=n+1-\sqrt{n+1}\), equivalently \(n-k=\sqrt{n+1}-1\); the claimed integer equality cases follow by setting \(h=\sqrt{n+1}\in\mathbb Z\). The eigenspace dimensions give the volume formula. In the anisotropic regime the largest centered Euclidean inball has squared radius \(u=h\), since its nearest facets are the row/column facets; no off-center Euclidean ball can exceed that radius by symmetry averaging or the row/column support bounds. The volume ratio then follows by dividing the ellipsoid volume by \(\kappa_{n^2-1}u^{(n^2-1)/2}\).

## Verification

The standalone file `verify.py` uses only Python's standard library `fractions.Fraction`. It checks 4,950 exact integer pairs with \(2\le n\le100\), \(1\le k<n\), verifying both regimes' support equalities/inequalities, positive semiaxes, KKT identities, John's positive contact weights, the weighted second-moment identities in both invariant eigenspaces, and the trace condition. Separately, it reconstructs actual matrix projections of each coordinate normal for \(2\le n\le16\), checks row/column normal projections, and verifies Frobenius orthogonality. These finite tests are **not** an exhaustive proof for all dimensions; the algebraic argument in Steps 1--4 supplies the unrestricted theorem. To reproduce, run `python verify.py` from the extracted package directory.

## Relationship to prior work

Gill and Linusson [1], especially their Theorem 3 and facet table, establish the complete \(k\)-assignment halfspace model, its affine dimension, and combinatorial facial structure. Torres [2] proves the matching-polytope fractional H-representation and normality. Their results are used as premises, not claimed as discoveries. Earlier Euclidean *inradius* calculations determine the largest inscribed ball and identify the same facet-distance threshold, but an inradius neither gives the John ellipsoid's anisotropic eigenspaces nor determines its determinant-maximizing volume. In particular, restricting a John ellipsoid of the full doubly substochastic polytope to a fixed-sum slice does not generally produce the John ellipsoid of the slice. The contribution here is the complete **all-parameter inscribed-ellipsoid shape, contact-orbit weights, exact volume, and high-cardinality anisotropy**. John's contact theorem [3] supplies the general optimization criterion; the concrete certificate and formulas are specific to this family.

## Limitations

The result does not include \(k=n\) (a different-dimensional Birkhoff-polytope affine hull) or rectangular assignment polytopes. It does not assert a universal numerical-estimation algorithm for unrelated polytopes or independently certify bibliographic priority. Earlier equivalent formulas may exist under partial-permutation, transportation-section, or optimal-design terminology. The calculations are exact with a self-contained proof; finite verification is corroborative, not an infinite certificate.

## References

[1] J. Gill and S. Linusson, *The k-assignment polytope*, Discrete Optimization 6 (2009), 148--161, DOI: 10.1016/j.disopt.2008.10.003. Lawful postprint: https://www.diva-portal.org/smash/get/diva2:210918/fulltext01.pdf.

[2] J. C. Torres, *Normality of k-Matching Polytopes of Bipartite Graphs*, arXiv:2306.11910v1 (first public version 2023-06-20), later Revista Colombiana de Matemáticas 57 (2023), 193--206, DOI: 10.15446/recolma.v57n2.115853. https://arxiv.org/abs/2306.11910.

[3] F. John, *Extremum problems with inequalities as subsidiary conditions*, in Studies and Essays Presented to R. Courant (1948), pp. 187--204; see M. Henk, *Löwner--John Ellipsoids*, Documenta Mathematica ISMP (2012), pp. 95--106.
