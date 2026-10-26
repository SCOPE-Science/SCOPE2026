# Harmonic-cubic rigidity and a sharp localization crossover for orthogonal-frame finite differences

## Finding

Fix an integer \(n\ge2\), a radius \(\delta>0\), and a real fully symmetric order-three tensor \(T=(T_{ijk})_{1\le i,j,k\le n}\). Let \(\phi:\mathbb R^n\to\mathbb R\) be even and differentiable at the origin, and define
\[
f(x)=\frac16\sum_{i,j,k=1}^n T_{ijk}x_ix_jx_k+\phi(x).
\]
Then \(\nabla f(0)=0\). For any orthonormal basis \(U=(u_1,\ldots,u_n)\), let
\[
G_U=\sum_{a=1}^n\frac{f(\delta u_a)-f(-\delta u_a)}{2\delta}\,u_a.
\]
For a Haar-uniform orthogonal basis, write \(t_i=\sum_j T_{ijj}\) and
\[
H_{ijk}=T_{ijk}-\frac{t_i\delta_{jk}+t_j\delta_{ik}+t_k\delta_{ij}}{n+2}.
\]
Here \(\delta_{ij}\) denotes the Kronecker symbol. The exact mean and squared Euclidean orientation variance are
\[
\mathbb E_U G_U=\frac{\delta^2}{2(n+2)}t,
\qquad
\mathbb E_U\|G_U-\mathbb E_U G_U\|_2^2
=\frac{\delta^4}{6(n+2)(n+4)}\|H\|_F^2.
\]
**Zero orientation variance occurs exactly when \(H=0\)**, equivalently when the cubic form is radial-linear:
\[
T[x,x,x]=\frac{3}{n+2}(t\cdot x)\|x\|_2^2.
\]
In that case every orthonormal basis produces the same nonzero gradient approximation \(\delta^2 t/[2(n+2)]\) whenever \(t\ne0\). Thus zero random-frame variance does not imply zero finite-difference bias.

For the unit rank-one tensor \(T=a^{\otimes3}\), \(\|a\|_2=1\), compare a complete Haar basis with the standard coordinate basis. With noiseless values their mean-squared errors relative to the actual zero gradient are
\[
R_{\rm Haar}=\frac{\delta^4}{36}\frac{15}{(n+2)(n+4)},
\qquad R_{\rm coord}=\frac{\delta^4}{36}\sum_{i=1}^n a_i^6.
\]
Consequently the Haar estimator is strictly better **if and only if**
\[
\sum_{i=1}^n a_i^6>\frac{15}{(n+2)(n+4)},
\]
with a tie at equality and worse performance when the inequality reverses. Axis-aligned directions attain the maximum coordinate risk; equal-magnitude directions attain the minimum. Across all unit \(a\), the sharp ratios are
\[
\max_a\frac{R_{\rm coord}}{R_{\rm Haar}}=\frac{(n+2)(n+4)}{15},
\quad
\max_a\frac{R_{\rm Haar}}{R_{\rm coord}}=\frac{15n^2}{(n+2)(n+4)}.
\]
Both are strictly greater than one for every \(n\ge2\), and the latter tends to \(15\) as \(n\to\infty\). The comparison is unchanged when each of the \(2n\) queried function values has independent zero-mean noise of the same finite variance \(\sigma^2\): both risks gain the identical term \(n\sigma^2/(2\delta^2)\).

## Assumptions and scope

The tensor entries are real and invariant under permutations of indices. No regularity of the even component away from zero is needed; its contributions to antipodal differences cancel exactly. The basis is Haar-distributed on the real orthogonal group, using all \(n\) directions and exactly two antipodal evaluations per direction. Numerical errors due to floating-point arithmetic are excluded. Measurement noises, if present, are mutually independent, mean zero, have common finite variance, and are independent of the random basis.

The rank-one comparison is realized at the exact unique minimizer of a globally strongly convex objective: for any unit \(a\), define \(s=a\cdot x\) and
\[
f_a(x)=\tfrac12\|x\|_2^2+\tfrac16 s^3+\tfrac1{24}s^4.
\]
Its Hessian is \(\nabla^2 f_a(x)=I+(s+s^2/2)aa^\mathsf T\succeq I/2\) because \(s+s^2/2=(s+1)^2/2-1/2\); hence zero is its unique global minimizer. Its even quadratic/quartic pieces cancel in antipodal differences, leaving exactly the stated rank-one cubic estimation error for every \(\delta>0\).

## Proof

**Step 1: cubic reduction.** Since \(\phi(\delta u)=\phi(-\delta u)\), the central difference equals \(\delta^2 T[u,u,u]/6\). Consequently
\[
G_U=\frac{\delta^2}{6}\sum_{a=1}^n T[u_a,u_a,u_a]u_a.
\]
By orthonormality, \(\|G_U\|_2^2=\delta^4\sum_a T[u_a,u_a,u_a]^2/36\), with no cross terms.

**Step 2: exact fourth and sixth sphere moments.** A column \(u\) of a Haar orthogonal matrix is uniformly distributed on the unit sphere. Directly from rotational invariance and normalization, its fourth and sixth coordinate moments are the sums over all three and fifteen pair partitions, respectively:
\[
\mathbb E[u_i u_j u_k u_l]
=\frac{\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}}{n(n+2)},
\]
\[
\mathbb E[u_{i_1}\cdots u_{i_6}]
=\frac{\displaystyle\sum_{P\in\mathcal P_2(6)}\prod_{\{r,s\}\in P}\delta_{i_ri_s}}{n(n+2)(n+4)}.
\]
For completeness, these follow by writing \(u=g/\|g\|_2\) for an isotropic Gaussian \(g\); radial independence, the Gaussian pairing identity, and \(\mathbb E\|g\|_2^{2m}=n(n+2)\cdots(n+2m-2)\) give the formulas for \(m=2,3\).

Contraction with the symmetric tensor gives
\[
\mathbb E[T[u,u,u]u]=\frac{3t}{n(n+2)},
\quad
\mathbb E[T[u,u,u]^2]
=\frac{6\|T\|_F^2+9\|t\|_2^2}{n(n+2)(n+4)}.
\]
In the sixth moment, six pairings connect all three tensor legs across the two copies and contribute \(\|T\|_F^2\); nine pairings join one pair internally in each copy and contribute \(\|t\|_2^2\). Multiplication by the \(n\) equivalent frame columns gives
\[
\mathbb E G_U=\frac{\delta^2t}{2(n+2)},
\quad
\mathbb E\|G_U\|_2^2
=\frac{\delta^4(6\|T\|_F^2+9\|t\|_2^2)}{36(n+2)(n+4)}.
\]

**Step 3: orthogonal tensor decomposition.** Put \(P_{ijk}=(t_i\delta_{jk}+t_j\delta_{ik}+t_k\delta_{ij})/(n+2)\). Then \(\operatorname{tr}P=t\), \(\operatorname{tr}H=0\), and the trace-free and pure-trace pieces are Frobenius-orthogonal. Explicit contraction yields
\[
\|T\|_F^2=\|H\|_F^2+\frac3{n+2}\|t\|_2^2.
\]
Subtracting the squared mean from the second moment cancels the pure-trace term and proves
\[
\mathbb E\|G_U-\mathbb E G_U\|_2^2
=\frac{\delta^4\|H\|_F^2}{6(n+2)(n+4)}.
\]
The strictly positive coefficient proves the stated if-and-only-if rigidity. If \(H=0\), then for every unit \(u\), \(T[u,u,u]=3(t\cdot u)/(n+2)\); summing \((t\cdot u_a)u_a\) over a complete basis yields \(t\), proving basiswise determinism directly.

**Step 4: rank-one localization.** For \(T=a^{\otimes3}\), \(\|a\|_2=1\), spherical sixth moments give \(n\mathbb E[(a\cdot u)^6]=15/[(n+2)(n+4)]\). Evaluating at canonical axes instead gives \(\sum_i a_i^6\). The sharp bounds \(1/n^2\le\sum_i a_i^6\le1\) follow from convexity of the cube function applied to the nonnegative weights \(a_i^2\); equality holds for equal magnitudes and coordinate axes respectively. Since \(1/n^2<15/[(n+2)(n+4)]<1\) for every \(n\ge2\), both orderings exist and the exact maximal ratios follow.

**Step 5: measurement noise.** For either orthonormal basis, each centered difference has independent noise of variance \(\sigma^2/(2\delta^2)\). Summing the squared coefficients over an orthonormal basis produces total noise risk \(n\sigma^2/(2\delta^2)\). Zero means and independence eliminate cross terms with the deterministic directional differences, so the crossover is unaffected.

## Verification

The accompanying standalone Python 3 program `verify.py` enumerates the three fourth-moment and fifteen sixth-moment pair partitions, evaluates full tensor contractions using exact rational arithmetic for independent symmetric-tensor examples in dimensions two through four, checks the pure-trace zero-variance case and a rationally rotated basis, and verifies the rank-one crossover inequalities in dimensions two through one hundred. It passed when executed from the saved package. The exhaustive pair partitions, not the finite selection of tensor inputs, support the symbolic moment proof above. The strong-convexity inequality is established analytically by completing the square.

## Relationship to prior work

Feng and Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds* (arXiv:2205.14737v1, May 29, 2022), introduce precisely the Stiefel-frame central-difference estimator used here and prove general variance/bias **bounds**. Their Section 3 and appendix contain spherical moment tools, but the inspected statements do not give an exact harmonic trace-free variance identity, zero-variance classification for nonzero cubics, or the coordinate-versus-Haar sixth-power crossover. These are exact structural refinements, not a new estimator.

Kozak, Molinari, Rosasco, Tenorio, and Villa, *Zeroth order optimization with orthogonal random directions* (arXiv:2107.03941v1, July 8, 2021), analyze convergence for random orthogonal subspace updates and explain the coordinate and full-frame specializations; their displayed directional difference is forward, not this central cubic comparison. Berahas, Cao, Choromanski, and Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization* (arXiv:1905.01332v1, May 3, 2019), compare orthogonal interpolation, coordinate finite differences, and smoothing by error bounds but do not supply this exact stationary-point tensor classification.

Related exact Haar second-moment results for sparse stochastic subspace descent concern rank-one quadratic gradients rather than the sixth-moment, third-derivative truncation structure analyzed here. The source's fourth/sixth moments make the present answer derivable with additional contraction and harmonic-decomposition arguments; this derivability is an originality limitation, not an assertion of absolute publication priority.

## Limitations

The equality is for a complete **real orthogonal frame** and the cubic odd part (plus any even part) at a zero-gradient point. It does not establish the same rigidity for general smooth functions, incomplete frames, correlated evaluation noise, complex frames, or entire optimization trajectories. The strongly convex example has a Hessian growing with position, so no globally Lipschitz-gradient claim is made. The classification is exact in arithmetic; floating-point cancellation and finite-difference roundoff are outside scope. An equivalent harmonic-moment specialization might appear in unindexed literature; no independent priority audit has been performed.

## References

1. Y. Feng and T. Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds*, arXiv:2205.14737v1 (first submitted 2022-05-29), https://arxiv.org/abs/2205.14737.
2. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio, S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941v1 (first submitted 2021-07-08), https://arxiv.org/abs/2107.03941.
3. A. S. Berahas, L. Cao, K. Choromanski, K. Scheinberg, *A Theoretical and Empirical Comparison of Gradient Approximations in Derivative-Free Optimization*, arXiv:1905.01332v1 (first submitted 2019-05-03), https://arxiv.org/abs/1905.01332.
