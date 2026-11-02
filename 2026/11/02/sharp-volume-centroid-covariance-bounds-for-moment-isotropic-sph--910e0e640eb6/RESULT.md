# Sharp volume–centroid covariance bounds for moment-isotropic spherical simplices

## Finding

**Theorem.** Let \(d\geq2\) be an integer, and let \(\mu\) be any Borel probability measure on the Euclidean unit sphere \(S^{d-1}\subset\mathbb R^d\) satisfying
\[
\mathbb E_\mu X=0,\qquad \mathbb E_\mu[XX^{\mathsf T}]=I_d/d.
\]
Take \(d+1\) independent points \(X_0,\ldots,X_d\) with law \(\mu\). Let \(V\) be the (nonnegative) Euclidean \(d\)-volume of their convex hull, and let \(C=(d+1)^{-1}\sum_{i=0}^{d}X_i\) be its vertex barycenter. Put \(T_3=\mathbb E_\mu X^{\otimes3}\) and \(\kappa=\|T_3\|_F^2\). Then
\[
\mathbb EV^2=\frac{(d+1)!}{d^d(d!)^2},\qquad
\frac{\operatorname{Cov}(\|C\|^2,V^2)}{\mathbb EV^2}
=-\frac{2+d^2\kappa}{(d+1)^2}.
\tag{1}
\]
Furthermore, \(0\leq\kappa\leq(d-1)/d^2\), and therefore the **sharp, dimension-only covariance bounds** are
\[
-\frac{1}{d+1}
\ \leq\ \frac{\operatorname{Cov}(\|C\|^2,V^2)}{\mathbb EV^2}
\ \leq\ -\frac{2}{(d+1)^2}<0.
\tag{2}
\]
The upper equality holds **exactly** when \(T_3=0\), i.e. \(\mu\) integrates all polynomials of degree at most three as does uniform spherical measure (a weighted spherical \(3\)-design). The lower equality holds **exactly** when \(\mu\) gives equal mass to the \(d+1\) vertices of a regular inscribed \(d\)-simplex, up to orthogonal transformation.

Equivalently, under squared-volume size bias, the expected squared barycenter radius belongs to the sharp interval
\[
0\leq\frac{\mathbb E[\|C\|^2V^2]}{\mathbb EV^2}
=\frac{d-1-d^2\kappa}{(d+1)^2}
\leq\frac{d-1}{(d+1)^2}.
\tag{3}
\]
Thus even though the unweighted mean \(\mathbb E\|C\|^2=1/(d+1)\) is the same for every moment-isotropic spherical measure, squared-volume reweighting strictly decreases it, with a completely classified pair of extreme families.

## Assumptions and scope

The distribution is **moment-isotropic** rather than necessarily rotation-invariant. It may be discrete, continuous, or mixed. All \(d+1\) samples are independent and drawn with replacement. The simplex is allowed to have volume zero. The norm \(\|T_3\|_F\) is the Frobenius norm of the full symmetric order-three coordinate tensor. Only the stated spherical support and two moment constraints are assumed. Dimension \(d=1\) is excluded; in that dimension the unit sphere contains just two points and the two extremal descriptions coalesce.

## Proof

**1. A two-column determinant identity.** Write \(m=d+1\), and augment each random point to the column \(W_i=(1,X_i)^{\mathsf T}\in\mathbb R^m\). Its second-moment matrix is
\[
\Sigma=\mathbb E[W_iW_i^{\mathsf T}]
=\operatorname{diag}(1,I_d/d),\qquad\det\Sigma=d^{-d}.
\]
For any two fixed columns \(u,v\in\mathbb R^m\), and \(m-2\) independent further columns with second moment \(\Sigma\), the standard multilinear determinant expansion (or expansion of the exterior square of the first two columns) gives
\[
\mathbb E\det(u,v,W_2,\ldots,W_{m-1})^2
=(m-2)!\det\Sigma\,
\big[(u^{\mathsf T}\Sigma^{-1}u)(v^{\mathsf T}\Sigma^{-1}v)
-(u^{\mathsf T}\Sigma^{-1}v)^2\big].
\tag{4}
\]
For completeness, whiten all columns by \(\Sigma^{-1/2}\). Expanding the determinant along the fixed two-column exterior product, the expectation of the squared complementary \((m-2)\)-minor equals \((m-2)!\) times the squared coefficient of that exterior product, because distinct coordinate-minor cross terms vanish after independent second-moment contractions. Undoing whitening multiplies by \(\det\Sigma\), giving (4). The same expansion with no fixed columns yields \(\mathbb E\det(W_0,\ldots,W_{m-1})^2=m!\det\Sigma\). Since \(V=|\det(W_0,\ldots,W_d)|/d!\), this proves the first identity in (1).

**2. The mixed moment.** Let \(t=X_0\cdot X_1\). Spherical support gives
\[
W_i^{\mathsf T}\Sigma^{-1}W_i=d+1,\qquad
W_0^{\mathsf T}\Sigma^{-1}W_1=1+dt.
\]
Substitute in (4) and use \(m=d+1\):
\[
\mathbb E[(d!V)^2\mid X_0,X_1]
=(d-1)!d^{-d}\big[(d+1)^2-(1+dt)^2\big].
\tag{5}
\]
Independence, centering, and covariance isotropy imply \(\mathbb Et=0\), \(\mathbb Et^2=1/d\), while
\[
\mathbb Et^3=\sum_{a,b,c=1}^{d}(\mathbb E X_aX_bX_c)^2=\kappa.
\tag{6}
\]
Consequently,
\[
\frac{\mathbb E[tV^2]}{\mathbb EV^2}
=-\frac{2+d^2\kappa}{d(d+1)}.
\tag{7}
\]
The barycenter identity
\[
\|C\|^2=\frac{1}{d+1}+\frac{2}{(d+1)^2}
\sum_{0\leq i<j\leq d}X_i\cdot X_j
\]
shows that \(\mathbb E\|C\|^2=1/(d+1)\). All \(\binom{d+1}{2}\) pairwise terms have the same mixed expectation (7) by exchangeability. Multiplication by \(2\binom{d+1}{2}/(d+1)^2=d/(d+1)\) gives the second identity in (1), and rearrangement gives (3).

**3. Sharp tensor bound.** Formula (6) establishes \(\kappa\geq0\), with equality exactly when every entry of \(T_3\) vanishes. Under the first-two-moment constraints, this means all monomials through degree three agree with spherical average (where odd moments vanish), establishing the upper-equality description.

For the other bound, for every \(t\in[-1,1]\) the polynomial
\[
(1-t)(t+1/d)^2\geq0.
\tag{8}
\]
Apply (8) to the inner product of independent \(X,Y\) with law \(\mu\). Using \(\mathbb Et=0\) and \(\mathbb Et^2=1/d\) gives
\[
\kappa=\mathbb Et^3\leq (d-1)/d^2.
\tag{9}
\]
Equality forces \(X\cdot Y\in\{1,-1/d\}\) almost surely. Since the integrand (8) is continuous and nonnegative, equality holds for **all** pairs in the closed support of \(\mu\). Distinct support points therefore have inner product \(-1/d\). There cannot be more than \(d+1\) such points: the associated \(N\)-point Gram matrix has the form \((1+1/d)I_N-(1/d)\mathbf1\mathbf1^{\mathsf T}\), which ceases to be positive semidefinite when \(N>d+1\). On the other hand, \(\mathbb E[XX^{\mathsf T}]=I_d/d\) has full rank and \(\mathbb EX=0\), so the support must contain at least \(d+1\) points. Thus there are exactly \(d+1\) points forming a regular inscribed simplex. The only positive weights producing mean zero are equal ones (its Gram nullspace is spanned by \(\mathbf1\)). Conversely the uniform regular-simplex law attains (9). This proves both sharp equalities and (2).

## Verification

The standalone `verify.py` performs exact-rational exhaustive evaluation of all ordered samples from two moment-isotropic finite spherical laws: the regular-simplex vertex law and the signed-coordinate (crosspolytope) law in dimensions \(d=2\) and \(d=3\). It constructs squared simplex volume from the Gram determinant of edge differences, computes \(\|C\|^2\), and checks equations (1)–(3) against exact rational expectations. For the regular-simplex law, the squared-volume-weighted barycenter radius is exactly zero; for the crosspolytope law, it equals \((d-1)/(d+1)^2\). This is a finite arithmetic cross-check only; the proof above establishes all dimensions and all admissible probability laws.

Run the included Python 3 standard-library file as `python verify.py`; it requires no packages, external files, or network access.

## Relationship to prior work

The general squared-volume/determinant-of-covariance identity is classical and appears in Rademacher, *On the monotonicity of the expected volume of a random simplex* (arXiv:1008.3944v1, Lemma 4). Ambrus and Böröczky, *Stability results for the volume of random simplices* (arXiv:1005.5024), distinguish random-simplex models from a simplex with **one fixed vertex at the population centroid**. These are different from the **random vertex barycenter** in (1)–(3). The present result concerns a joint mixed moment, its dependence on the cubic moment tensor, and a sharp characterization of both extremizing spherical measures, none of which follows from knowledge of \(\mathbb EV^2\) alone.

Miles, *Isotropic random simplices* (Advances in Applied Probability 3 (1971), 353–382), studies moments of random simplex volume and is a plausible historical-priority source. Only its abstract was accessible during this comparison. Hence possible stronger prior results in its full text are an explicit limitation; absence of its full text is **not** evidence of noncoverage.

## Limitations

The theorem is confined to the Euclidean unit sphere and moment-isotropic probability measures, with independent sampling **with replacement**. It does not assert covariance signs for arbitrary anisotropic or off-sphere distributions, nor any independence of volume and barycenter. The optimality statements classify equality, not quantitative stability near equality. Priority relative to inaccessible historical literature, especially Miles (1971), remains subject to independent bibliographic checking. The computational verifier tests finitely supported examples only and is not an infinite proof or independent validation.

## References

1. L. Rademacher, *On the monotonicity of the expected volume of a random simplex*, arXiv:1008.3944v1 (public 24 August 2010), especially Lemma 4. https://arxiv.org/html/1008.3944v1
2. G. Ambrus and K. J. Böröczky, *Stability results for the volume of random simplices*, arXiv:1005.5024 (2010). https://arxiv.org/html/1005.5024v2
3. R. E. Miles, *Isotropic random simplices*, Advances in Applied Probability 3 (1971), 353–382. https://doi.org/10.2307/1426176 (abstract available; full text not examined).
