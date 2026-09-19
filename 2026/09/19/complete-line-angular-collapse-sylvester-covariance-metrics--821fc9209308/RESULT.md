# Completeness and angular collapse in Sylvester-power covariance metrics

## Setting

Li, Mishra, Jawanpuria and Mostajeran introduced in arXiv:2609.17089 a two-parameter Riemannian metric on the cone \(\mathbb S_{++}^n\) of symmetric positive-definite matrices.  For \(X=P\operatorname{diag}(d_1,\ldots,d_n)P^T\) and tangent matrices \(U,V\), it is the kernel metric
\[
g_X^{(p,q)}(U,V)
 =\sum_{i,j}\frac{U'_{ij}V'_{ij}}{\phi_{p,q}(d_i,d_j)},
\qquad U'=P^TUP,
\]
with
\[
\phi_{p,q}(x,y)
 =\frac12\,4^{(p-q)^2}(x^py^q+x^qy^p).
\]
Write
\[
r=p+q,\qquad a=p-q.
\]
Then
\[
\phi_{p,q}(x,y)
 =4^{a^2}(xy)^{r/2}
 \cosh\!\left(\frac a2\log\frac xy\right),
\]
so \(r\) is its homogeneity degree while \(a\) controls the shape at fixed degree.

The results below identify an exact global-geometric boundary that is independent of the local Hessian-conditioning analysis in the source paper.

## 1. A homogeneous-kernel completeness lemma

Consider any smooth positive symmetric kernel \(\phi:(0,\infty)^2\to(0,\infty)\) satisfying
\[
\phi(tx,ty)=t^r\phi(x,y),\qquad t>0,
\]
and the associated kernel metric
\[
g_X^\phi(U,V)=\sum_{i,j}\frac{U'_{ij}V'_{ij}}{\phi(d_i,d_j)}.
\]

**Theorem 1.** The Riemannian manifold \((\mathbb S_{++}^n,g^\phi)\) is metrically, hence geodesically, complete if and only if
\[
\boxed{r=2.}
\]

### Necessity

Let \(X=xI\) and \(U=\dot x I\).  Homogeneity gives
\[
\phi(x,x)=\phi(1,1)x^r,
\]
so the scalar ray has speed
\[
\|\dot X\|_{g^\phi}
 =\sqrt{\frac{n}{\phi(1,1)}}\,|\dot x|x^{-r/2}.
\]
If \(r<2\), the ray has finite length from any positive \(x\) to \(x=0\); if \(r>2\), it has finite length from any positive \(x\) to \(x=\infty\).  In either case a sequence escaping the manifold is Cauchy in finite length, so the metric is incomplete.

### Sufficiency

Suppose \(r=2\) and put \(c=\phi(1,1)>0\).  Along any piecewise \(C^1\) curve, use continuously ordered eigenvalue branches away from crossings and the standard a.e. eigenvalue derivative formula at crossings.  The diagonal terms of the kernel metric give
\[
\|\dot X\|_{g^\phi}^2
 \ge \frac1c\sum_i\left(\frac{\dot\lambda_i}{\lambda_i}\right)^2.
\]
Hence path length controls Euclidean displacement of the ordered log-spectrum:
\[
L_{g^\phi}(X(\cdot))
 \ge \frac1{\sqrt c}\left\|
  \log\lambda(X(1))-\log\lambda(X(0))
 \right\|_2.
\]
Therefore every \(g^\phi\)-Cauchy sequence has all eigenvalues eventually confined to a fixed compact interval \([m,M]\subset(0,\infty)\).  A sufficiently short connecting curve cannot leave a slightly larger spectral annulus, because doing so would require a fixed positive change in the log-spectrum and hence fixed positive metric length.  On that larger annulus, positivity and continuity of \(\phi\) give uniform two-sided equivalence between \(g^\phi\) and the Frobenius metric.  Thus a \(g^\phi\)-Cauchy sequence is Frobenius-Cauchy and converges to an SPD matrix; the same local uniform equivalence then gives convergence in \(g^\phi\).  Hopf--Rinow yields geodesic completeness.

This removes the mean-kernel hypothesis from the familiar degree-two completeness result for the homogeneous kernel class.

## 2. Exact complete line for the new covariance-metric family

Applying Theorem 1 to \(\phi_{p,q}\) gives immediately:

**Corollary 2.** For every real \(p,q\),
\[
\boxed{
(\mathbb S_{++}^n,g^{(p,q)})\text{ is complete}
\iff p+q=2.
}
\]

Thus the affine-invariant member \((1,1)\) is not an isolated complete point: the whole line \(p+q=2\) is complete, including members with one exponent negative.

## 3. Completeness is exactly the scale- and inversion-symmetric line

Two exact pullback identities hold for the family.

For dilation \(D_c(X)=cX\),
\[
\boxed{D_c^*g^{(p,q)}=c^{2-(p+q)}g^{(p,q)}.}
\]
Hence all positive dilations are isometries exactly when \(p+q=2\).

For inversion \(\iota(X)=X^{-1}\), differentiation contributes a factor \((d_i d_j)^{-1}\) to each tangent entry, and one obtains
\[
\boxed{\iota^*g^{(p,q)}=g^{(2-p,\,2-q)}.}
\]
Because \(g^{(p,q)}=g^{(q,p)}\), inversion is an isometry exactly on \(p+q=2\).  Consequently
\[
\boxed{
\text{complete}
\iff \text{dilation-invariant}
\iff \text{inversion-invariant}
\iff p+q=2.
}
\]

This gives the exponent \(r=2\) a global geometric meaning in addition to its role in local Hessian conditioning.

## 4. Where the complete line leaves the mean-kernel class

On \(p+q=2\), multiply the metric by the harmless positive constant \(4^{a^2}\):
\[
\bar g^{(p,q)}:=4^{a^2}g^{(p,q)}.
\]
Its kernel is
\[
\bar\phi_a(x,y)
 =xy\cosh\!\left(\frac a2\log\frac xy\right)
 =M_a(x,y)^2,
\]
where
\[
M_a(x,y)=\sqrt{xy\cosh\!\left(\frac a2\log\frac xy\right)}.
\]
The logarithmic partial derivatives are
\[
\frac{\partial\log M_a}{\partial\log x}
 =\frac12+\frac a4\tanh\!\left(\frac a2\log\frac xy\right),
\]
\[
\frac{\partial\log M_a}{\partial\log y}
 =\frac12-\frac a4\tanh\!\left(\frac a2\log\frac xy\right).
\]
Both are nonnegative for all \(x,y>0\) if and only if \(|a|\le2\).  Since \(M_a\) is symmetric, homogeneous and satisfies \(M_a(x,x)=x\), this is also exactly the condition for \(M_a\) to be a symmetric homogeneous mean.  Therefore
\[
\boxed{\bar\phi_a=M_a^2\text{ is a mean kernel exactly when }|p-q|\le2.}
\]

The established Hiai--Petz / Thanwerdas--Pennec mean-kernel completeness theorem already covers the portion \(p+q=2, |p-q|\le2\).  Corollary 2 extends completeness to the non-mean region
\[
\boxed{p+q=2,\qquad |p-q|>2.}
\]

## 5. A sharp angular-collapse threshold inside the complete line

The non-mean complete region has a distinct geometry.  After the normalization above, diagonal eigenvalue-change directions agree exactly with the affine-invariant metric.  For an off-diagonal eigendirection corresponding to eigenvalues \(x,y\), the metric coefficient relative to affine-invariant geometry is
\[
\boxed{
\frac{\bar g(E_{ij},E_{ij})}{g^{\rm AI}(E_{ij},E_{ij})}
 =\operatorname{sech}\!\left(\frac a2\log\frac xy\right).
}
\]
Thus eigenvector rotations become progressively cheaper as the spectral ratio grows whenever \(a\ne0\).

This can be made exact in dimension two.  Let
\[
D_\kappa=\operatorname{diag}(\sqrt\kappa,\kappa^{-1/2}),
\qquad
X_\kappa(\theta)=R_\theta D_\kappa R_\theta^T,
\qquad 0\le\theta\le\frac\pi2,
\]
where \(R_\theta\) is the planar rotation matrix.  The matrices all have determinant one and condition number \(\kappa\); the endpoints differ only by swapping their eigendirections.  Direct substitution gives the exact quarter-turn length
\[
\boxed{
\bar L_\kappa(a)
 =\frac\pi{\sqrt2}\,
 \frac{\sqrt\kappa-\kappa^{-1/2}}
 {\sqrt{\cosh((a/2)\log\kappa)}}.
}
\]
For \(a\ne0\),
\[
\boxed{
\bar L_\kappa(a)
 \sim \pi\,\kappa^{(2-|a|)/4}
 \qquad(\kappa\to\infty).
}
\]
At \(a=0\), \(\bar L_\kappa(0)\sim(\pi/\sqrt2)\kappa^{1/2}\).

Hence:

- if \(|a|<2\), the quarter-turn cost diverges;
- if \(|a|=2\), it tends to \(\pi\);
- if \(|a|>2\), it tends to zero.

In particular, throughout the complete but non-mean region,
\[
\boxed{
\operatorname{dist}_{\bar g}
\left(D_\kappa,R_{\pi/2}D_\kappa R_{\pi/2}^T\right)
\le \bar L_\kappa(a)\longrightarrow0.
}
\]
So two increasingly ill-conditioned covariance matrices with the same eigenvalues but orthogonal principal axes can become arbitrarily close in metric distance.  This is an angular-collapse phenomenon at infinity, not a failure of completeness: both endpoint sequences themselves leave every compact subset of the SPD cone.

The threshold \(|p-q|=2\) is exactly the boundary of the mean-kernel region found above.

## 6. Optimization interpretation

The motivating paper treats \((p,q)\) as an intrinsic preconditioner and shows that the local Hessian condition number separates into the exponent \(r=p+q\) and a shape parameter \(p-q\).  The present result adds two global constraints that local Hessian conditioning alone does not see:

1. \(p+q\ne2\) makes one end of the scalar covariance scale reachable in finite Riemannian length: the boundary for \(p+q<2\), or infinite scale for \(p+q>2\).
2. Even on the complete line \(p+q=2\), choosing \(|p-q|>2\) makes large-condition-number eigendirection rotations asymptotically free after constant normalization.

This does **not** imply that an optimizer should always restrict to \(p+q=2\) or \(|p-q|\le2\): incompleteness can be acceptable for a problem whose iterates remain in a compact region, and cheap angular motion may sometimes be beneficial.  It does mean that metric tuning has a sharp global-geometric phase diagram in addition to the source paper's local conditioning phase diagram.

## Verification

`artifacts/verify_covmetric_geometry.py` checks:

- homogeneity of \(\phi_{p,q}\) on random positive arguments;
- the exact inversion-kernel identity;
- the direct two-dimensional metric speed against the closed-form rotation formula;
- the \(\kappa^{(2-|a|)/4}\) asymptotic and its \(\pi\) coefficient for \(a\ne0\);
- the mean-kernel monotonicity threshold at \(|a|=2\).

The recorded output was produced with Python 3.13.5 and NumPy 2.3.5.  The computation is only a consistency check; the statements above are proved analytically.

## Relation to prior literature and originality boundary

Li--Mishra--Jawanpuria--Mostajeran introduce the two-parameter metric, its kernel factorization, and the separation into exponent \(p+q\) and shape \(p-q\).  Those are source results, not claimed here.

Hiai--Petz (2009) introduced kernel metrics and proved that **mean-kernel** metrics \(\phi=aM^\theta\) are complete exactly for homogeneity power \(\theta=2\).  Thanwerdas--Pennec later synthesized this result and extended related structural results to larger classes of \(O(n)\)-invariant metrics.  Their published completeness criterion is stated for mean-kernel (or extended mean-kernel) metrics.  The portion of the present \(p+q=2\) line satisfying \(|p-q|\le2\) lies in that established mean-kernel theory and is not claimed as new.

To the best of our knowledge, the following combined statements were not located in the checked literature: the removal of the mean hypothesis for positive homogeneous kernel metrics; the consequent completeness of the new family's non-mean \(p+q=2, |p-q|>2\) members; the equivalence of completeness with dilation and inversion invariance in this family; and the exact \(|p-q|=2\) angular-collapse threshold with the quarter-turn asymptotic above.

The main residual originality risk is older matrix-geometry literature using different terminology for homogeneous kernel metrics or isospectral-orbit degeneracy.  The result should therefore be read with the usual “to the best of our knowledge” qualification.

## Limitations

The angular-collapse construction is an upper bound on distance obtained from a specific isospectral path; it is not a closed-form geodesic-distance formula.  It concerns the behavior of the metric at increasingly ill-conditioned matrices and does not establish poor optimization performance.  Completeness is a global property of the full SPD cone and says nothing by itself about convergence of a particular retraction-based algorithm, line search, or objective.  No curvature classification or closed-form exponential map is derived.

## References

1. Y. Li, B. Mishra, P. Jawanpuria, C. Mostajeran, *Optimization over covariance matrices with a parameterized metric*, arXiv:2609.17089 (2026). https://arxiv.org/abs/2609.17089
2. F. Hiai, D. Petz, *Riemannian metrics on positive definite matrices related to means*, Linear Algebra Appl. 430 (2009), 3105--3130; arXiv:0809.4974. https://arxiv.org/abs/0809.4974
3. Y. Thanwerdas, X. Pennec, *O(n)-invariant Riemannian metrics on SPD matrices*, Linear Algebra Appl. 661 (2023), 163--201; arXiv:2109.05768. https://arxiv.org/abs/2109.05768
4. Y. Thanwerdas, X. Pennec, *The geometry of mixed-Euclidean metrics on symmetric positive definite matrices*, Differential Geom. Appl. 81 (2022), 101867; arXiv:2111.02990. https://arxiv.org/abs/2111.02990
