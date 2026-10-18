# John ellipsoids and perfect-square roundness for two-layer Boolean pyramids

## Finding

Let \(n\ge3\) and \(1\le k<n\) be integers. Put \(\ell=\min\{k,n-k\}\), \(\mathbf1=(1,\ldots,1)\), and
\[
P_{n,k}=\operatorname{conv}\bigl(\{0\}\cup\{\mathbf1_A:A\subseteq[n],\ |A|=k\}\bigr)\subset\mathbb R^n.
\]
Its unique John ellipsoid (maximum-volume enclosed Euclidean ellipsoid) is \(E=\{c+Q^{1/2}z:\|z\|_2\le1\}\), where
\[
c=\frac{k}{n+1}\mathbf1,\quad Q=u\left(I-\frac{\mathbf1\mathbf1^{\mathsf T}}n\right)+v\frac{\mathbf1\mathbf1^{\mathsf T}}n,\quad
u=\frac{\ell^2}{n(n+1)},\quad v=\frac{k^2}{n(n+1)^2}.
\]
Here \(u\) (multiplicity \(n-1\)) and \(v\) (multiplicity one) are squared principal semiaxes. Its Euclidean volume is
\[
\operatorname{vol}_n(E)=\operatorname{vol}_n(B_2^n)\frac{k\ell^{n-1}}{n^{n/2}(n+1)^{(n+1)/2}}.
\]
Every tangent facet and its unique contact point are as follows. The top facet \(\sum_i x_i=k\) always contacts at \(p_0=(k/n)\mathbf1\). If \(2k\le n\), the \(n\) lower-coordinate facets \(x_i=0\) contact at the vectors \(p_i\) with \((p_i)_i=0\) and \((p_i)_j=k/n\) for \(j\ne i\). If \(2k\ge n\), the \(n\) oblique facets \(k x_i=\sum_j x_j\) contact at \(q_i\) with \((q_i)_i=(n-1)/n\) and \((q_i)_j=(k-1)/n\) for \(j\ne i\). There are exactly \(n+1\) tangent facets for \(2k\ne n\), and \(2n+1\) for \(2k=n\). Endpoint parameter values \(k=1\) and \(k=n-1\) have the claimed \(n+1\) facets; redundant supporting inequalities are not counted as facets.

The ellipsoid is round (\(Q\) a scalar multiple of \(I\)) precisely in the infinite arithmetic family
\[
n=m^2-1,\qquad k=m(m-1),\qquad m\in\mathbb Z,\quad m\ge2.
\]
The first pairs are \((n,k)=(3,2),(8,6),(15,12),(24,20)\). In particular, infinitely many nonsimplex rank-selected Boolean polytopes have a Euclidean ball as their John ellipsoid.

## Assumptions and scope

The polytope uses the standard Euclidean metric on \(\mathbb R^n\), not the intrinsic metric of its top hypersimplex. It is the two-layer \(S\)-hypersimplex \(\Delta(n,\{0,k\})\), a pyramid over the ordinary hypersimplex. The shape convention is that \(Q\) is the positive-definite covariance-like ellipsoid matrix, so the polar quadratic inequality is \((x-c)^{\mathsf T}Q^{-1}(x-c)\le1\). Positive dimensions \(n\ge3\) and ranks \(1\le k<n\) are quantified universally.

## Proof

**1. All halfspaces.** A nonzero point of \(P_{n,k}\) lies in a radial slice \(s=\sum_i x_i\in(0,k]\), with \(x=(s/k)y\) and \(y\in\Delta(n,k)=\{y\in[0,1]^n:\sum_i y_i=k\}\). Conversely, every such scaled point is in the convex hull of the apex and base. It follows exactly that
\[
P_{n,k}=\left\{x\in\mathbb R^n:x_i\ge0,\quad kx_i\le\sum_jx_j\ \text{for each }i,\quad\sum_jx_j\le k\right\}.
\]
For \(2\le k\le n-2\), the \(n\) lower and \(n\) oblique inequalities each describe a facet (cones from the respective ordinary hypersimplex facets), in addition to the top facet. For \(k=1\), the oblique inequalities are redundant, and for \(k=n-1\), the lower inequalities are redundant. This list is exhaustive by the displayed exact halfspace description.

**2. Containment.** Write \(t=k/(n+1)\), and let the proposed \(Q\) have the eigenvalues \(u,v\) stated above. For a halfspace \(a^{\mathsf T}x\le b\), containment of \(E\) is equivalent to \(a^{\mathsf T}c+\sqrt{a^{\mathsf T}Qa}\le b\). The top inequality is saturated because \(\sqrt{\mathbf1^{\mathsf T}Q\mathbf1}=k/(n+1)=k-nt\). For lower-coordinate halfspaces, the squared difference between the available offset and support radius is
\[
\delta_{\rm lo}=t^2-e_i^{\mathsf T}Qe_i=
\begin{cases}0,&2k\le n,\\[2pt]\dfrac{(n-1)(2k-n)}{n(n+1)},&2k\ge n.\end{cases}
\]
For oblique halfspaces, put \(a=ke_i-\mathbf1\). Its available offset from \(c\) equals \((n-k)t>0\). Direct substitution gives
\[
\delta_{\rm ob}=((n-k)t)^2-a^{\mathsf T}Qa=
\begin{cases}\dfrac{k^2(n-1)(n-2k)}{n(n+1)},&2k\le n,\\[2pt]0,&2k\ge n.\end{cases}
\]
Both differences are nonnegative, hence all defining inequalities hold for the whole ellipsoid. The inequalities are strict exactly in the regimes indicated. Since an ellipsoid contacts a given supporting hyperplane in at most one point, the tangent-facet classification follows once the listed points are identified.

**3. Positive contact certificate.** In the regime \(2k\le n\), select the \(n+1\) points \(z_0=p_0,z_i=p_i\). In the regime \(2k>n\), select \(z_0=p_0,z_i=q_i\). Substituting the explicit coordinates into the halfspace representation shows that each point belongs to \(P_{n,k}\), lies on the asserted facet, and has ellipsoidal squared norm \((z_i-c)^{\mathsf T}Q^{-1}(z_i-c)=1\). With \(d_i=z_i-c\), elementary coordinate summation gives the two exact moment identities
\[
\sum_{i=0}^{n}d_i=0,\qquad \frac n{n+1}\sum_{i=0}^{n}d_id_i^{\mathsf T}=Q.
\]
Set \(u_i=Q^{-1/2}d_i\). Then each \(u_i\) is a unit contact vector and, with strictly positive weights \(\lambda_i=n/(n+1)\), one has \(\sum_i\lambda_i u_i=0\), \(\sum_i\lambda_i u_i u_i^{\mathsf T}=I\). John's contact characterization proves that the unit ball is the unique maximum-volume ellipsoid of the affine-normalized body \(Q^{-1/2}(P_{n,k}-c)\). Affine reversal establishes the claimed unique John ellipsoid of \(P_{n,k}\). At \(2k=n\), both the coordinate and oblique families are tangent; the selected \(p_i\) contacts already suffice for the certificate.

**4. Volume and roundness.** The spectral factors imply \(\det Q=u^{n-1}v=k^2\ell^{2n-2}/[n^n(n+1)^{n+1}]\), proving the volume formula. If \(k\le n/2\), then \(u/v=n+1>1\). If \(k>n/2\), then \(u=v\) is equivalent to \(k/(n-k)=\sqrt{n+1}\). Since the left side is rational, \(\sqrt{n+1}\) is an integer \(m\ge2\). Solving yields \(n=m^2-1\), \(k=m(m-1)\), and every such pair satisfies \(u=v\). No other cases exist.

## Verification

The standalone reproducibility script `hypersimplex_john_checker.py` uses Python's exact rational numbers only. It checks every parameter pair \(3\le n\le25\), \(1\le k<n\), which comprises 299 profiles. For each, it verifies the complete containment inequalities, active-set margins, all chosen contact points, ellipsoid boundary norms, contact-normal alignment, both John moment identities, determinant and spherical criterion. The observed 11 simultaneous two-facet-family transitions and four round cases agree with the closed-form theorem. These finite checks are corroboration; the universal result is proved analytically above.

## Relationship to prior work

Manecke, Sanyal, and So introduced and studied \(S\)-hypersimplices as rank-selected Boolean polytopes, providing their face theory, pulling triangulations and monotone paths. Their original December 2018 preprint and the accessible full 2019 revision do not state the John ellipsoid of this two-layer family. The rank-selected outer ellipsoid and minimum enclosing sphere are distinct optimization problems; the John ellipsoid of a capped cube with all ranks up to a threshold also concerns a different convex body. John's classical maximum-volume ellipsoid/contact criterion is used as a standard proof tool, not claimed as new.

## Limitations

This theorem concerns exactly the two-rank family \(\{0,k\}\), not general rank sets, and its roundness statement refers to the standard Euclidean embedding. The research comparison does not prove historical uniqueness of the result; an earlier equivalent formulation may exist. Independent mathematical validation has not been performed. The exact rational checks do not independently establish infinitely many dimensions.

## References

1. S. Manecke, R. Sanyal, J. So, *S-hypersimplices, pulling triangulations, and monotone paths*, arXiv:1812.07491 (first public version 2018-12-18; accessible revised full text 2019-11-28). https://arxiv.org/abs/1812.07491 ; https://arxiv.org/html/1812.07491v2 .
2. F. John, *Extremum problems with inequalities as subsidiary conditions*, in *Studies and Essays Presented to R. Courant on his 60th Birthday*, 1948. Classical positive contact-moment criterion.
