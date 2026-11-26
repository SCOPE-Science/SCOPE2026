# Exact equilibrium loss and the optimizer set for Beverton–Holt dispersal

## Finding

Consider \(p\ge2\) patches with carrying capacities \(K_i>0\) and intrinsic growth rates \(r_i>0\). A fixed strictly positive column-stochastic matrix \(D\) redistributes individuals before local recruitment. In one step \(x\mapsto g(Dx)\), where
\[
 b_i=r_i/K_i,\qquad g_i(z)=\frac{(1+r_i)z}{1+b_i z}.
\]
Write \(x(D)\) for the positive equilibrium, \(y(D)=Dx(D)\), and \(N(D)=\sum_i x_i(D)\). The scalar population ceiling \(N^*\) and the corresponding pre-recruitment allocation \(y^*\) can be written in terms of
\[
 a_i=b_i^{-1},\quad s_i=\sqrt{1+r_i},\quad
 B=\sum_i a_i s_i,\quad C=\sum_i a_i(s_i^2+1),\quad
 t=\frac{2}{C/B+\sqrt{(C/B)^2-4}},\quad \tau=t^2,
\]
as \(y_i^*=a_i(s_i/t-1)\) and \(N^*=\sum_i y_i^*=B/t-\sum_i a_i\). Let \(x_i^*=g_i(y_i^*)=s_i t y_i^*\).

**Exact loss.** For every such fixed matrix, the abundance deficit is exactly
\[
 (1-\tau)(N^*-N(D))=
 \tau\sum_{i=1}^p\frac{b_i(y_i(D)-y_i^*)^2}{1+b_i y_i(D)}.
\]
The formula identifies the quantitative cost of allocation error, including away from the maximizing allocation. The weights on the right are evaluated at the actual pre-recruitment equilibrium; the identity is not an asymptotic expansion or a curvature bound.

**Optimizer set.** The maximizing matrices are precisely the admissible \(D\) with \(Dx^*=y^*\). Under the invertible linear map \(W_{ij}=D_{ij}x_j^*\), this set is the relative interior of the transportation polytope with row sums \(y^*\) and column sums \(x^*\). Its affine dimension is \((p-1)^2\). Thus the optimal allocation and equilibrium are unique, even though there is a positive-dimensional family of optimal mixing matrices.

## Proof

**Positive equilibrium.** The map \(F(x)=g(Dx)\) is monotone on the nonnegative cone, bounded coordinatewise by \((1+r_i)/b_i\), and strictly subhomogeneous at positive \(x\): \(F(cx)<cF(x)\) for \(c>1\). A positive Perron vector \(u\) of \(\operatorname{diag}(1+r_i)D\) has eigenvalue greater than one, since all column sums exceed one. Hence for sufficiently small \(\epsilon>0\), \(F(\epsilon u)>\epsilon u\). Choose an upper solution above the coordinate bounds and the lower solution. Increasing and decreasing iterates from these ordered bounds yield positive fixed points. If two positive fixed points differ, after interchanging them if necessary one is dominated by the smallest multiple \(c>1\) of the other, with equality in at least one coordinate. Monotonicity and strict subhomogeneity contradict equality at a touching coordinate. For any positive initial state the two initial bounds may be chosen to contain it, yielding convergence by sandwiching.

**Conservation and exact remainder.** The relation \(C-2B=\sum_i a_i(s_i-1)^2>0\) gives \(0<t<1\) and \(t+t^{-1}=C/B\). At the positive vector \(y^*\), \(1+b_i y_i^*=s_i/t\), so \(g_i'(y_i^*)=\tau\). Furthermore,
\[
 \sum_i (g_i(y_i^*)-y_i^*)
 =\sum_i a_i(s_i t-1)(s_i/t-1)=C-B(t+t^{-1})=0.
\]
In particular \(x^*\) and \(y^*\) have equal total \(N^*\). Use \(g_i(z)=(s_i^2/b_i)(1-(1+b_i z)^{-1})\) and subtract its value and tangent at \(y_i^*\). For any \(z\ge0\), putting the resulting fractions over a common denominator gives
\[
 g_i(y_i^*)+\tau(z-y_i^*)-g_i(z)
 =\frac{\tau b_i(z-y_i^*)^2}{1+b_i z}.
\]
For any equilibrium, \(x_i(D)=g_i(y_i(D))\) and \(\sum_i x_i(D)=\sum_i y_i(D)\). Thus summing the remainders at \(z=y_i(D)\) gives the stated loss formula. It excludes equality except at \(y(D)=y^*\). The rank-one matrix with every column \(y^*/N^*\) maps \(x^*\) to \(y^*\), so it attains the ceiling. More generally \(Dx^*=y^*\) is sufficient because \(x^*\) is then a positive fixed point, and it is necessary because equality requires \(y(D)=y^*\) and hence \(x(D)=x^*\).

**Geometry.** The change of variables to \(W\) sends the column stochasticity equations to the stated column sums, and \(Dx^*=y^*\) to the row sums. The equations determine the last row and column from the leading \((p-1)\times(p-1)\) block; the final condition is consistent because the totals coincide. There is a strictly positive feasible array, \(W_{ij}=y_i^*x_j^*/N^*\), so positivity leaves a full-dimensional open subset of the affine constraint space. A feasible array with a zero entry is on a relative supporting hyperplane of the nonnegative polytope, as that coordinate is positive at the exhibited feasible array. This proves the relative-interior and dimension statements.

As a reference, evaluating the same exact remainder at \(z=K_i\) and using \(g_i(K_i)=K_i\) gives the analogous expression for \(N^*-\sum_i K_i\). Equality requires \(K_i=y_i^*\) for every patch, which forces \(g_i'(K_i)=1/(1+r_i)=\tau\); conversely, if all \(r_i\) are equal, \(t=(1+r_i)^{-1/2}\) gives \(y_i^*=K_i\) directly.

## Reproduction and scope

For \(K=(3,8)\), \(r=(3,8)\), one finds \(t=(3-\sqrt5)/2\), \(y^*=(2+\sqrt5,(7+3\sqrt5)/2)\), and \(N^*=(11+5\sqrt5)/2\). The accompanying `verify.py` compares the conservation, tangent, and loss identities in this exact field example and samples 780 numerical configurations with one through six patches. It is a finite corroboration only; there is no assertion that the optimizing matrix is unique. The general proof covers fixed positive matrices, not sparse, lossy, or state-dependent dispersal or transient metrics.

## Relationship to prior results

- [*Sharp adaptive-dispersal population ceiling for Beverton–Holt patches*](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-sharp-adaptive-dispersal-population-ceiling-for-beverton-holt-pa--0d23b062c337/RESULT.md) gives the same scalar ceiling, optimal allocation, rank-one attainment, and isolated-capacity comparison, even for adaptive conservative redistribution. Its quantitative allocation result is a strong-concavity inequality against the best allocation at the current total and obtains asymptotic rigidity. It implies that an optimal constant matrix has the displayed allocation at equilibrium. The focus here is the exact fixed-matrix equilibrium loss identity and the full transportation-polytope description, rather than the scalar capacity or asymptotic rigidity.
- Bravo de la Parra, *Dispersal and Total Population Size in Discrete-Time Metapopulation Models*, DOI [10.3390/math14193624](https://doi.org/10.3390/math14193624), establishes global stability in the conservative discrete-time model and gives a two-patch rank-one construction ensuring a strict gain over the isolated total. The cited construction gives a sign criterion rather than the exact loss for each matrix.
- Grumbach et al., *The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models*, DOI [10.1007/s00285-023-01984-8](https://doi.org/10.1007/s00285-023-01984-8), give exact optima over a scalar symmetric dispersal family in a two-patch growth-before-dispersal model.
