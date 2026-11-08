# A fourth-root cap transition and a first-order motif law for random spherical right-angle graphs

## Finding

Fix an integer \(k\ge3\). For each dimension \(d\ge k+2\) let \(X_1,\ldots,X_k\) be independent points uniformly distributed by spherical area in the cap
\[
C_d(h)=\{x\in S^{d-1}\subset\mathbb R^d:x_1\ge h\},\qquad 0\le h<1.
\]
Their **right-angle graph** has an edge \(ij\) exactly when \(\langle X_i,X_j\rangle\ge0\). Denote its labelled edge set by \(G_d\), put \(E=\binom{[k]}2\) and \(m=|E|\). For a prescribed labelled graph \(H\) on \([k]\), set \(\sigma_e=1\) on its edges and \(\sigma_e=-1\) on its nonedges. For \(p\in(0,1)\), define \(q_e=p\) if \(\sigma_e=1\), and \(q_e=1-p\) otherwise, and set
\[
\begin{aligned}
 B_H(p)&=\prod_{e\in E}q_e,\\
 L_H(p)&=\sum_{e\in E}\sigma_e\prod_{f\in E\setminus\{e\}}q_f,\\
 T_H(p)&=\sum_{1\le i<j<\ell\le k}\sigma_{ij}\sigma_{j\ell}\sigma_{i\ell}
       \prod_{f\in E\setminus\{ij,j\ell,i\ell\}}q_f.
\end{aligned}
\]
Empty products equal one. Write \(\Phi\) and \(\phi\) for the standard Gaussian distribution function and density.

**Critical fourth-root transition.** For any sequence \(h_d\in[0,1)\) with \(d^{1/4}h_d\to\lambda\in[0,\infty]\), the complete graph-valued law of \(G_d\) converges to the independent-edge law \(G(k,\Phi(\lambda^2))\), where \(\Phi(+\infty)=1\). In particular, at \(\lambda=0\) the limit is \(G(k,1/2)\), while at \(\lambda=+\infty\) it is the complete graph. These limiting statements are for each fixed \(k\), not for \(k\) growing with \(d\).

**Sharp motif correction at the critical scale.** For fixed \(\lambda>0\) and exactly \(h_d=\lambda d^{-1/4}\), let \(p=\Phi(\lambda^2)\) and \(v=\phi(\lambda^2)\). For each prescribed graph \(H\),
\[
\boxed{\Pr(G_d=H)=B_H(p)+\frac{(2+\lambda^4)v L_H(p)+v^3 T_H(p)}{\sqrt d}+o_{k,\lambda}(d^{-1/2}).}
\]

**Sharp equatorial boundary layer.** For fixed \(a\ge0\) and exactly \(h_d=a/\sqrt d\), put \(\mu_a=\phi(a)/(1-\Phi(a))\) and \(v_0=\phi(0)\). Then for every prescribed \(H\),
\[
\boxed{\Pr(G_d=H)=2^{-m}+\frac{\mu_a^2v_0 L_H(1/2)+v_0^3T_H(1/2)}{\sqrt d}+o_{k,a}(d^{-1/2}).}
\]
This includes uniform sampling on a hemisphere at \(a=0\). The two finite-size corrections do **not** commute under \(\lambda\downarrow0\), because \(a/\sqrt d\) resolves a smaller, distinct angular boundary layer. No uniformity in \(a,\lambda,k\) is claimed.

For example, with three vertices at the critical scale, the probability that **all three pairwise angles at the origin are at most a right angle** is
\[
\Pr(G_d=K_3)=\Phi(\lambda^2)^3+
\frac{3(2+\lambda^4)\Phi(\lambda^2)^2\phi(\lambda^2)+\phi(\lambda^2)^3}{\sqrt d}+o_\lambda(d^{-1/2}).
\]
On the hemisphere \(h=0\) it is
\[
\Pr(G_d=K_3)=\frac18+\frac{2}{\pi\sqrt{2\pi d}}+o(d^{-1/2}).
\]
The formula concerns pairwise origin-centered angles between position vectors, **not** the intrinsic vertex angles of a spherical geodesic triangle.

## Assumptions and scope

All randomness is independent and uniform with respect to normalized spherical surface area **conditional on membership in the specified single cap**. The coordinate direction defining the cap is fixed and arbitrary by rotational symmetry. The dimension tends to infinity with a fixed labelled vertex count \(k\). The critical and equatorial correction statements use exact prescribed cap heights rather than unspecified asymptotically equivalent heights; an \(o(d^{-1/4})\) perturbation can change the first correction. Edges satisfy the non-strict inequality, but equality has probability zero.

## Proof

**1. Exact radial–tangential factorization.** Write
\[
X_i=(S_i,\sqrt{1-S_i^2}\,U_i),
\]
where the \(U_i\) are independent and uniform on \(S^{d-2}\subset\mathbb R^{d-1}\), independent of the \(S_i\). The \(S_i\) have common density proportional to
\[
(1-s^2)^{(d-3)/2}\mathbf 1_{[h,1]}(s).
\]
Set \(D=d-1\) and \(Z_{ij}=\sqrt D\langle U_i,U_j\rangle\). The inner-product array satisfies exactly
\[
Y_{ij}:=\sqrt d\langle X_i,X_j\rangle
=\sqrt d S_iS_j+\sqrt{d/D}\sqrt{(1-S_i^2)(1-S_j^2)}\,Z_{ij}.
\]

**2. First correction of the tangential Gram law.** For fixed \(k\), the density of the off-diagonal entries of the Gram matrix \(I+Z/\sqrt D\) is proportional, on the positive-definite locus, to
\[
\det(I+Z/\sqrt D)^{(D-k-1)/2},\qquad Z_{ii}=0.
\]
Here the density is with respect to Lebesgue measure on its \(m\) distinct off-diagonal entries. From \(\operatorname{tr}Z=0\), \(\operatorname{tr}Z^2=2\sum_{e\in E}Z_e^2\), and \(\operatorname{tr}Z^3=6\sum_{i<j<\ell} Z_{ij}Z_{j\ell}Z_{i\ell}\), expanding the logarithmic determinant gives
\[
\log f_D(z)=-\tfrac m2\log(2\pi)-\tfrac12\sum_ez_e^2+
D^{-1/2}\sum_{i<j<\ell}z_{ij}z_{j\ell}z_{i\ell}+O_k(D^{-1}P_k(z))
\]
on the moderate-deviation region \(\max_e|z_e|\le\sqrt{C\log D}\), for a fixed polynomial \(P_k\). More precisely, truncation to \(\max_e|z_e|\le\sqrt{C\log D}\), together with the exact spherical-coordinate sub-Gaussian tail bound on the complement, gives the **integrated** expansion
\[
f_D(z)=\prod_{e\in E}\phi(z_e)\left(1+D^{-1/2}\sum_{i<j<\ell}z_{ij}z_{j\ell}z_{i\ell}\right)+r_D(z),
\qquad \int|r_D(z)|\,dz=o(D^{-1/2}).
\]
The normalizing constant has no \(D^{-1/2}\) term: every Gaussian triangle monomial has zero integral. The displayed density expansion follows with \(O_k(D^{-1}(\log D)^{C_k})\) integrated remainder by taking the truncation coefficient large enough. The same calculation proves joint convergence of all \(Z_e\) to independent standard Gaussians.

**3. Radial boundary layers.** Suppose \(h=\lambda d^{-1/4}\) for fixed \(\lambda>0\). With
\[
W_i=\frac{dh}{1-h^2}(S_i-h),
\]
Taylor expansion of the logarithm of the radial density, using its monotone hazard and exponential domination, proves \(W_i\Rightarrow\operatorname{Exp}(1)\) and convergence of every fixed moment. Thus \(\mathbb E W_i\to1\). In the exact inner-product identity of step 1, expansions with bounded first moments give
\[
Y_{ij}=\lambda^2+Z_{ij}+d^{-1/2}(W_i+W_j-\lambda^2 Z_{ij})+o_{L^1}(d^{-1/2}).
\]
The right-angle threshold is therefore a shift of the tangential boundary \(Z_{ij}=-\lambda^2\) by
\[
-d^{-1/2}(W_i+W_j+\lambda^4)+o(d^{-1/2}),
\]
whose expected shift is \(-(2+\lambda^4)d^{-1/2}+o(d^{-1/2})\).

When instead \(h=a/\sqrt d\) for fixed \(a\ge0\), the variables \(V_i=\sqrt d S_i\) converge in every fixed moment to independent standard Gaussians conditioned to lie in \([a,\infty)\); their means converge to \(\mu_a\). Now
\[
Y_{ij}=Z_{ij}+d^{-1/2}V_iV_j+o_{L^1}(d^{-1/2}),
\]
so the expected boundary shift is \(-\mu_a^2d^{-1/2}+o(d^{-1/2})\).

**4. Integration of all graph patterns.** For an independent Gaussian array with edge threshold \(-\lambda^2\), each edge status contributes \(q_e\); shifting one boundary inward by a small amount \(t\) changes the probability by \(\sigma_e\phi(\lambda^2)t\prod_{f\ne e}q_f+o(t)\). Multiple simultaneous moving boundaries contribute only at quadratic order because the joint limiting density is smooth and all radial perturbations have bounded moments. Averaging step 3 therefore produces exactly the \(L_H\) term. The cubic Gram-density term integrates using
\[
\int_{-\lambda^2}^\infty z\phi(z)\,dz=\phi(\lambda^2),\qquad
\int_{-\infty}^{-\lambda^2}z\phi(z)\,dz=-\phi(\lambda^2).
\]
Consequently each triple contributes its sign product times \(\phi(\lambda^2)^3\) and the untouched-edge probabilities, yielding \(T_H\). The \(L^1\) Gram error and the moment-controlled boundary errors are \(o(d^{-1/2})\), proving the critical formula. Identical integration with threshold zero and radial mean \(\mu_a\) proves the equatorial formula.

**5. Phase diagram.** If \(d^{1/4}h_d\to\lambda\in(0,\infty)\), the cap's radial variable satisfies \(S_i/h_d\to1\) in probability, so \(\sqrt d S_iS_j\to\lambda^2\), and tangential inner products approach independent Gaussians. If \(d^{1/4}h_d\to0\), spherical marginal tail bounds yield \(\sqrt d S_iS_j\to0\) in probability. If \(d^{1/4}h_d\to\infty\), \(\sqrt d S_iS_j\ge\sqrt d h_d^2\to\infty\) while the tangential term is tight. The three cases give the stated graph limits.

## Verification

A standalone checker implements the exact conditional beta-coordinate sampler and an independent sequential-coordinate construction of the three-edge Gram matrix. It evaluates the analytic motif coefficients for all four triangle-pattern orbit types (three, two, one, or zero positive edges), compares them against direct spherical-cap sampling at two dimensions, and verifies exact normalization of the signed first-order corrections across all labelled patterns. Its random numerical tests are corroboration only, not substitutes for the density and boundary-layer arguments. Execute `python check_cap_graph.py`; dependencies appear in `requirements.txt`.

## Relationship to prior work

The full-sphere high-dimensional geometric graph model and signed triangles are classical inputs from Bubeck, Ding, Eldan and Rácz (2014). The tangential Gaussian Gram expansion is also related to general spherical-angle limit laws. Bárány, Hug, Reitzner and Schneider (2015) study spherical convex hulls of hemisphere-uniform points rather than right-angle adjacency patterns. Bangachev and Bresler (2024) study Fourier-coefficient bounds for **rotation-invariant full-sphere** random geometric graphs. None of these inspected results states the conditional-cap graph law or its two explicit radial boundary-layer coefficients. The novelty claim is the combined cap-conditioned, all-labelled-pattern expansion and its discontinuous scale matching, not the underlying Gaussian integral, spherical marginal density, or signed-triangle technique.

## Limitations

All asymptotics fix \(k\). No claim is made for a growing graph, an arbitrary anisotropic distribution, general angular thresholds, or a uniform error constant across cap-height regimes. The two correction formulas apply to exact height sequences; extrapolating one to the other is invalid. Historical priority remains provisional because equivalent cap-conditioned expansions may appear in geometric graph or multivariate-normal approximation literature not identified in the search. No independent mathematical audit has been performed.

## References

1. S. Bubeck, J. Ding, R. Eldan and M. Rácz, *Testing for high-dimensional geometry in random graphs*, arXiv:1411.5713, first posted 20 November 2014. https://arxiv.org/abs/1411.5713
2. I. Bárány, D. Hug, M. Reitzner and R. Schneider, *Random points in halfspheres*, arXiv:1505.04672, first posted 18 May 2015. https://arxiv.org/abs/1505.04672
3. K. Bangachev and G. Bresler, *On the Fourier Coefficients of High-Dimensional Random Geometric Graphs*, arXiv:2402.12589, first posted 19 February 2024. https://arxiv.org/abs/2402.12589
