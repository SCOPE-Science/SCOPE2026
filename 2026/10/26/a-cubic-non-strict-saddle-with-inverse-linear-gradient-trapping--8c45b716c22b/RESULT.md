# A cubic non-strict saddle with inverse-linear gradient trapping in depth-three scalar factorization

## Finding

Consider the scalar depth-three regularized matrix-factorization objective

\[
F(w_1,w_2,w_3)=(w_1w_2w_3-y_\star)^2+w_1^2+w_2^2+w_3^2,
\qquad y_\star=\frac{4}{3^{3/4}}.
\]

Put \(a=3^{-1/4}\). The point \(w_\star=(a,a,a)\) is a critical point with Hessian spectrum \(\{0,4,4\}\), but it is not a local extremum: along the permutation-invariant diagonal,

\[
F(x,x,x)-F(a,a,a)=12a^3(x-a)^3+O((x-a)^4).
\]

For simultaneous gradient descent with a fixed sufficiently small step size \(\eta>0\), the diagonal is invariant. If \(x_0>a\) is sufficiently close to \(a\), then \(x_k\downarrow a\) and

\[
\lim_{k\to\infty}k(x_k-a)=\frac{1}{12\eta a^3}.
\]
If \(x_0<a\) is sufficiently close to \(a\), the diagonal iterates instead leave every sufficiently small neighborhood on the lower side. Thus the degenerate critical point has a one-sided inverse-linear trapping law, with an exact leading coefficient.

## Assumptions and scope

The variables \(w_1,w_2,w_3\) are real, the target is the scalar \(y_\star>0\), and each layer has unit quadratic regularization. Gradient descent means the simultaneous Euclidean update \(w^{k+1}=w^k-\eta\nabla F(w^k)\), with one common step size. The dynamical assertion is local and concerns initial conditions exactly on the invariant diagonal; it is not a claim about random initialization or all nearby trajectories in three dimensions.

## Proof

Let \(p=w_1w_2w_3\). The gradient component is

\[
\partial_iF=2w_i+2(p-y_\star)w_jw_k,
\qquad \{i,j,k\}=\{1,2,3\}.
\]

Since \(a^4=1/3\), we have \(y_\star=4a^3\) and \(a^3-y_\star=-3a^3=-1/a\). Hence every gradient component vanishes at \(w_\star\).

At this point the Hessian has diagonal entries \(2(1+a^4)=8/3\) and off-diagonal entries \(2(a^4-1)=-4/3\). The all-ones direction therefore has eigenvalue \(8/3+2(-4/3)=0\); its orthogonal complement has eigenvalue \(8/3-(-4/3)=4\), with multiplicity two.

Permutation symmetry makes the diagonal invariant. Write \(w_1=w_2=w_3=x\), and define

\[
g(x)=x^4-y_\star x+1.
\]

Using \(y_\star=4a^3\) and \(3a^4=1\), direct expansion gives the exact factorization

\[
g(x)=(x-a)^2(x^2+2ax+3a^2).
\]

The simultaneous gradient update on the diagonal is consequently

\[
x_{k+1}=x_k-2\eta x_k(x_k-a)^2(x_k^2+2ax_k+3a^2).
\]

For \(\delta_k=x_k-a\) near zero this yields

\[
\delta_{k+1}=\delta_k-12\eta a^3\delta_k^2+O(\delta_k^3).
\]

For sufficiently small positive \(\delta_0\) and sufficiently small fixed \(\eta\), the sequence remains positive and decreases to zero. The reciprocal increment satisfies

\[
\frac{1}{\delta_{k+1}}-\frac{1}{\delta_k}\longrightarrow 12\eta a^3.
\]

Taking Cesàro means gives \(1/(k\delta_k)\to12\eta a^3\), which proves the stated limit. For negative \(\delta_0\) sufficiently close to zero, the exact factorization shows that the update decreases \(x_k\) while it remains in that neighborhood. It cannot converge to a fixed point there because \(g(x)>0\) for \(x\ne a\); hence it exits through the lower side in finite time.

Finally, the cubic term changes sign across \(x=a\), while the Hessian is positive semidefinite. Therefore \(w_\star\) is neither a local minimum nor a local maximum and is a non-strict saddle.

## Verification

The bundled `verify.py` checks the exact polynomial factorization coefficients, the Hessian eigenvalues, and the leading coefficients in the cubic expansion and diagonal update using rational identities. It does not use finite numerical trajectories as proof of the asymptotic limit; that limit follows from the reciprocal-increment argument above.

## Relationship to prior work

Chen, Jiang, and Wang characterize critical points of the regularized deep matrix-factorization objective in the non-scalar setting and identify the corresponding parameter equality for non-strict saddles. They explicitly note that the fully scalar case can be handled separately by a direct scalar argument. The present statement does not claim the threshold equality as new. It supplies a direct scalar proof and adds the exact local cubic coefficient and the one-sided inverse-linear gradient-descent asymptotic on the invariant diagonal, which are not stated in the inspected classification.

## Limitations

The result is for one scalar depth-three instance with unit layer penalties and a specially tuned target. It gives an exact trajectory law only on the invariant diagonal. It does not establish a basin-size estimate for off-diagonal initial conditions, a random-initialization probability, or a general rate theorem for non-strict saddles. Related work on second-order landscapes of deep linear networks remains a possible source of broader implications; no claim is made that the coefficient here generalizes beyond this model.

## References

1. P. Chen, R. Jiang, and P. Wang, “A Complete Loss Landscape Analysis of Regularized Deep Matrix Factorization,” arXiv:2506.20344, first submitted 25 June 2025, revised 28 May 2026. The paper states MSC 90C26, 90C30, 15A23. https://arxiv.org/abs/2506.20344
2. E. M. Achour, F. Malgouyres, and S. Gerchinovitz, “The loss landscape of deep linear neural networks: A second-order analysis,” Journal of Machine Learning Research 25 (2024), article 242. This is related landscape literature for the unregularized setting; it is not treated as covering the regularized local-dynamics claim above.
