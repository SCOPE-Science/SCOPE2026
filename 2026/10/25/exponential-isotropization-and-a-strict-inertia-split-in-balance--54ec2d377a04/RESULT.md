# Exponential isotropization and a strict inertia split in balanced rank-two matroid polytopes

## Finding

Let \(r\ge3\) and \(m\ge2\) be integers. Partition \(N=rm\) coordinates into \(r\) blocks of size \(m\). The balanced rank-two matroid base polytope is
\[
P_{r,m}=\operatorname{conv}\{e_i+e_j:\text{the coordinates }i,j\text{ lie in different blocks}\}\subset\mathbb R^N.
\]
Write \(X\) for a point sampled uniformly by intrinsic Euclidean volume from this polytope. Its covariance has exactly two distinct positive eigenvalues: \(\lambda_{\mathrm{within}}\), of multiplicity \(r(m-1)\), for directions whose sum in every block is zero, and \(\lambda_{\mathrm{between}}\), of multiplicity \(r-1\), for directions constant within each block and summing to zero globally.

Put \(k=(r-1)m\) and define the regularized beta upper tails and the retention fraction by
\[
p_{a,b}=\frac{1}{\mathrm B(a,b)}\int_{1/2}^1 t^{a-1}(1-t)^{b-1}\,dt,\qquad h=1-rp_{m,k}>0.
\]
The following rational expression determines both eigenvalues exactly:
\[
u=\frac{m(m+1)}{N(N+1)}\frac{1-p_{m+2,k}-(r-1)p_{m,k+2}}{h},
\qquad \lambda_{\mathrm{within}}=\frac{4u}{m(m+1)},
\qquad \lambda_{\mathrm{between}}=\frac{4r}{(r-1)m}\left(u-\frac1{r^2}\right).
\]
The strict spectral separation has the closed form
\[
\boxed{\lambda_{\mathrm{within}}-\lambda_{\mathrm{between}}=
\frac{2^{1-N}(r-2)}{(r-1)(m+1)(k+1)\,\mathrm B(m,k)\,h}>0.}
\]
In particular, the directionwise variances are never exactly isotropic at any finite \(m\ge2\), despite asymptotic isotropy.

For every fixed integer \(r\ge3\), let
\[
\rho_r=\frac{r^r}{2^r(r-1)^{r-1}}\in(0,1),
\qquad C_r=\frac{r^{3/2}(r-2)}{2\sqrt{2\pi}(r-1)^{3/2}}.
\]
Then the **sharp exponential isotropization law** is
\[
\boxed{1-\frac{\lambda_{\mathrm{between}}}{\lambda_{\mathrm{within}}}\sim C_r\sqrt m\,\rho_r^m\qquad (m\to\infty;\ r\text{ fixed}).}
\]
For example, when \(r=3\) and \(m=2\), the exact eigenvalues are \(\lambda_{\mathrm{within}}=4/49\) and \(\lambda_{\mathrm{between}}=5/147\), with exact gap \(1/21\). This strict gap decays exponentially relative to either eigenvalue as the block size grows.

## Assumptions and scope

The geometry uses the ordinary Euclidean metric inherited by the affine hyperplane \(\sum_{i=1}^N x_i=2\), rather than an unnormalized coordinate-slice measure. The graph is the complete \(r\)-partite graph with all \(r\) parts of size \(m\); its edge polytope is precisely \(P_{r,m}\). This is also the base polytope of the connected rank-two matroid with \(r\) parallel classes of size \(m\). The theorem requires integer \(r\ge3\) and \(m\ge2\). The distinct eigenspaces above exhaust the \(N-1\) dimensions of its affine span. The two-class case is a product of simplices in a smaller affine span, so it is not included. At \(m=1\), the within-block eigenspace has dimension zero and the strict two-eigenvalue statement is inapplicable.

## Proof

**1. A capped simplex model.** The rank-two matroid rank inequalities give the exact halfspace description
\[
P_{r,m}=\{x\in\mathbb R^N_{\ge0}:\sum_i x_i=2,\ \sum_{i\in B_j}x_i\le1\text{ for }1\le j\le r\},
\]
where \(B_j\) are the blocks. Set \(Y=X/2\). The uniform probability measure on the full standard simplex \(\{y_i\ge0:\sum y_i=1\}\) is \(\operatorname{Dirichlet}(1,\dots,1)\); restricting it to the stated halfspaces gives exactly the uniform measure on \(P_{r,m}\). The block masses \(T_j=\sum_{i\in B_j}Y_i\), before restriction, are \(\operatorname{Dirichlet}(m,\dots,m)\). The restriction is the event \(E=\{\max_j T_j\le1/2\}\). Since \(\sum_jT_j=1\), two different blocks cannot have \(T_j>1/2\) simultaneously. Therefore \(\Pr(E)=h=1-rp_{m,k}>0\). In fact the intrinsic volume of \(P_{r,m}\) is \(h\) times that of the scaled simplex \(2\Delta_{N-1}\), a useful geometric interpretation of the truncation.

**2. Conditional block moment.** By symmetry, \(\mathbb E(T_j\mid E)=1/r\). Let \(u=\mathbb E(T_1^2\mid E)\). Without the cap, \(u_0=\mathbb ET_1^2=m(m+1)/(N(N+1))\). Multiplying the Dirichlet density by \(T_1^2\) increases its first parameter from \(m\) to \(m+2\). Consequently,
\[
\mathbb E[T_1^2\mathbf1_{\{T_1>1/2\}}]=u_0p_{m+2,k},\qquad
\mathbb E[T_1^2\mathbf1_{\{T_j>1/2\}}]=u_0p_{m,k+2}\quad(j\ne1).
\]
Subtracting the disjoint forbidden caps from the unrestricted second moment and dividing by \(h\) gives the displayed exact formula for \(u\).

**3. Covariance decomposition.** Conditional on the block masses, the within-block coordinate proportions are independent \(\operatorname{Dirichlet}(1,\ldots,1)\), unaffected by the cap. Their covariance is \((m(m+1))^{-1}\) times the orthogonal projection onto the coordinate-sum-zero subspace of that block. Scaling the block by \(2T_j\) and averaging gives eigenvalue \(4u/[m(m+1)]\) on the direct sum of these subspaces, with dimension \(r(m-1)\). For a unit vector constant on each block and orthogonal to the all-ones vector, the associated linear statistic is \(2/\sqrt m\) times a zero-sum linear statistic of \((T_1,\ldots,T_r)\). Because the conditional law is exchangeable and the masses sum to one, the covariance on the zero-sum space of block masses has eigenvalue \(r\operatorname{Var}(T_1\mid E)/(r-1)\). Substituting \(\operatorname{Var}(T_1\mid E)=u-1/r^2\) yields \(\lambda_{\mathrm{between}}\). The two invariant subspaces are orthogonal and exhaust the tangent hyperplane; cross-covariances vanish by blockwise permutation symmetry.

**4. Strict exact gap.** For positive integers \(a,b\), elementary beta integration by parts gives
\[
p_{a+1,b}-p_{a,b}=\frac{2^{-(a+b)}}{a\mathrm B(a,b)},
\qquad p_{a,b+1}-p_{a,b}=-\frac{2^{-(a+b)}}{b\mathrm B(a,b)}.
\]
Apply these twice and use \(k=(r-1)m\), \(N=m+k\). Direct cancellation gives
\[
p_{m+2,k}+(r-1)p_{m,k+2}-rp_{m,k}
=\frac{N(r-2)2^{-(N+1)}}{(m+1)(k+1)\mathrm B(m,k)}.
\]
Thus
\[
u_0-u=\frac{m(r-2)2^{-(N+1)}}{(N+1)(k+1)\mathrm B(m,k)h}.
\]
From the two covariance formulas,
\[
\lambda_{\mathrm{within}}-\lambda_{\mathrm{between}}
=\frac{4(N+1)(u_0-u)}{(r-1)m(m+1)}.
\]
Substitution yields the stated positive closed expression. Positivity is strict because \(r>2\), \(m\ge2\), \(\mathrm B(m,k)>0\), and \(h>0\); no finite experiment is used to prove the all-dimensional inequality.

**5. Exponential asymptotics.** For fixed \(r\ge3\), the unrestricted beta random variable has mean \(1/r<1/2\) and variance \(O(m^{-1})\), so Chebyshev's inequality implies \(p_{m,k}\to0\) and hence \(h\to1\). The exact gap identity then implies \(u-u_0\to0\) at the scale appearing below, and \(\lambda_{\mathrm{within}}\sim4/[N(N+1)]\sim4/(r^2m^2)\). Stirling's formula supplies
\[
\mathrm B(m,(r-1)m)\sim
\sqrt{\frac{2\pi}{m}}\sqrt{\frac r{r-1}}
\left(\frac{(r-1)^{r-1}}{r^r}\right)^m.
\]
Substitute into the exact gap and divide by \(\lambda_{\mathrm{within}}\) to obtain
\[
1-\frac{\lambda_{\mathrm{between}}}{\lambda_{\mathrm{within}}}
\sim\frac{r^{3/2}(r-2)}{2\sqrt{2\pi}(r-1)^{3/2}}\sqrt m
\left(\frac{r^r}{2^r(r-1)^{r-1}}\right)^m.
\]
Finally, \(\rho_r<1\) follows from the strict positivity of the binary relative entropy between Bernoulli parameters \(1/r\) and \(1/2\): \(-\log\rho_r=rD_{\mathrm{KL}}(1/r\|1/2)>0\).

## Verification

The standalone \(\texttt{verify.py}\) script uses only Python's standard library. It independently evaluates the exact beta-tail expressions and checks positivity and both spectra for \(54\) integer parameter pairs. It integrates the conditional three-block polynomial density exactly over the two-dimensional simplex for six separate block sizes, not merely by reusing the beta recurrence. Four deterministic-seed simulations provide additional finite numerical checks. Four high-parameter checks compare the exact rational gap against the asymptotic coefficient. Run \(\texttt{python3 verify.py}\) from a directory containing the supplied script. The reported result is

```text
VERIFY_OK exact_spectra=54 independent_polytope_integrals=6 seeded_mc=4 asymptotic_ratios=4
```

The simulations and finite checks are corroboration only. The beta recurrence, Dirichlet geometry, and Stirling argument prove the infinite family.

## Relationship to prior work

Ferroni, Jochemko, and Schröter's paper on Ehrhart polynomials of rank-two matroids (first arXiv version 15 June 2021) supplies the canonical halfspace/flat description and exact discrete invariants. Its section on matroid polytopes, especially the rank-two description, is the appropriate geometric starting point. Ferroni and Schröter subsequently computed face-enumeration invariants of split matroid polytopes, including the rank-two case. The claims here concern uniform *continuous* volume covariance, its strict spectral ordering, and a sharp exponential rate; neither cited work gives these conclusions. Standard Dirichlet marginal and beta-integral identities used in the proof are classical and are not claimed as new. The distinctive contribution is their exact application to this natural polytope family and the resulting finite-dimensional spectral classification and exponential asymptotics.

## Limitations

The theorem concerns balanced complete multipartite graphs with fixed number of parts \(r\) in the asymptotic regime. It does not classify unequal parallel-class sizes, the growing-number-of-parts regime, or higher moments. An equivalent special case could exist under capped-simplex, truncated-Dirichlet, or conditioned-compositional-data terminology; the present literature comparison cannot eliminate that risk. Independent mathematical validation has not been performed.

## References

1. L. Ferroni, K. Jochemko, B. Schröter, *Ehrhart polynomials of rank two matroids*, Advances in Applied Mathematics **141** (2022), 102410. Earliest arXiv submission 2021-06-15, https://arxiv.org/abs/2106.08183; open full text: https://cris.unibo.it/bitstream/11585/1005131/1/1-s2.0-S019688582200094X-main.pdf.
2. L. Ferroni, B. Schröter, *Face enumeration for split matroid polytopes*, Combinatorics, Probability and Computing **34** (2025), 528–544, https://doi.org/10.1017/S0963548325000021. Open full text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8AB800A4A0AAB1AEF4720C07899107AF/S0963548325000021a.pdf/div-class-title-face-enumeration-for-split-matroid-polytopes-div.pdf.
