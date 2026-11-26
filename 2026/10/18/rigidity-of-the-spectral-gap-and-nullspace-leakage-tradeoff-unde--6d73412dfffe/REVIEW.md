# Independent mathematical audit

## correctness

PASS

I checked the infinitesimal reduction by rotating the block matrix in the plane-plus-normal basis: conjugate by exp(epsilon S), with S skew and upper-right block U^T D u, so the first-order off-diagonal blocks cancel. Weyl's inequality gives the two leading eigenvalues of the compression T=U^T D U with an O(epsilon^2) error, even for a repeated eigenvalue. Separately, the plane coordinate of the unit dominant eigenvector satisfies (lambda_3 I-epsilon T)y=epsilon U^T D u times its normal coordinate. Thus the norm of y, exactly the bottom-space projector residual, is epsilon||U^T D u||+O(epsilon^2). For coordinate probes p_i=u_i^2, the gap is 1-p_i and the squared leakage is p_i(1-p_i), excluding any zero p_i and forcing the common ratio squared (1-p_i)/p_i to be 2 for every i. For the balanced case, tr T=2 sum(d)/3 and tr(T^2)=sum(d_i^2)/3+(sum d)^2/9; using 2 tr(T^2)-(tr T)^2 and ||P D u||^2 gives the two claimed coefficients. I checked the CDF independently using consecutive spacings a,b of the ordered uniforms: their density is 6(1-a-b), and G^2=4(a^2+ab+b^2)/9. In q=a+b/2, r=sqrt(3)b/2 this integrates over a disk sector of angle pi/3 and radius R=3g/2; for g<=1/sqrt(3) the truncation a+b<=1 is automatic. The integral is (2pi/sqrt(3))R^2-(8/3)R^3, which is exactly F(g). There are no atoms at either boundary, so convergence of the joint event follows, including g=sqrt(2) ell and g>sqrt(2) ell.

## originality

PASS

The supported distinct claim is the deterministic, all-diagonal, balanced-only proportionality of first-order gap and unsquared nullspace residual, including the coefficient and its application to a joint event. The conventional perturbation reductions, separate repulsion/residual estimates and uniform variance CDF are not new. The inspected strongest matches do not state or yield the joint rigidity merely by parameter substitution. This is a best-of-knowledge judgment, not proof of priority.

## value

PASS

The two quality metrics have distinct numerical roles: splitting a null cluster helps separate its eigenvalues but degrades its status as an exact nullspace. Three coordinates are the smallest rank-one setting with a two-dimensional null cluster, and treating all orientations is not an arbitrary slice. The iff theorem and sharp pointwise ratio show exactly when these metrics are locked and when no orientation-independent-in-D ratio exists. This is a motivated structural calibration beyond the known marginal variance calculation, even though the proof is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
