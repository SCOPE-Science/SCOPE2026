# Pearson covariance is exactly a binomial average of discrete curvature
## Finding
Let
\[
(N_1,\ldots,N_m)\sim\operatorname{Multinomial}\!\left(n;\frac1m,\ldots,\frac1m\right),
\qquad m,n\ge2,
\]
and define Pearson's goodness-of-fit statistic
\[
X^2=\sum_{i=1}^m\frac{(N_i-n/m)^2}{n/m}.
\]
For any function
\[
h:\{0,1,\ldots,n\}\longrightarrow\mathbb R,
\]
put
\[
T_h=\sum_{i=1}^m h(N_i),
\qquad
\Delta^2h(y)=h(y+2)-2h(y+1)+h(y).
\]
If
\[
Y\sim\operatorname{Binomial}\!\left(n-2,\frac1m\right),
\]
then the finite-sample covariance is exactly
\[
\boxed{
\operatorname{Cov}(X^2,T_h)
=
\frac{(n-1)(m-1)}m\,
\mathbb E[\Delta^2h(Y)].
}
\tag{1}
\]
Thus the covariance of Pearson's statistic with every additive cell statistic is governed by one binomial average of the discrete curvature of its cell score. In particular, if \(h\) is discretely convex, the covariance is nonnegative; if \(h\) is strictly discretely convex on the support of \(Y\), it is strictly positive. The signs reverse for discrete concavity.

For the Cressie--Read power-divergence statistic
\[
D_\lambda
=
\frac{2}{\lambda(\lambda+1)}
\sum_{i=1}^m
N_i
\left[
\left(\frac{mN_i}{n}\right)^\lambda-1
\right],
\qquad
\lambda>-1,
\quad
\lambda\ne0,
\tag{2}
\]
with the continuous definition at \(\lambda=0\), formula (1) implies
\[
\boxed{
\operatorname{Cov}(X^2,D_\lambda)>0
\qquad
\text{for every }\lambda>-1,
}
\tag{3}
\]
for every finite \(m,n\ge2\).

At \(\lambda=0\), \(D_0\) is the log-likelihood-ratio statistic
\[
G^2
=
2\sum_{i=1}^m
N_i\log\!\left(\frac{N_i}{n/m}\right),
\]
with the convention \(0\log0=0\). Let
\[
f(k)=
\begin{cases}
k\log k,&k\ge1,\\0,&k=0.
\end{cases}
\]
Then
\[
\boxed{
\operatorname{Cov}(X^2,G^2)
=
\frac{2(n-1)(m-1)}m
\mathbb E\!
\left[
 f(Y+2)-2f(Y+1)+f(Y)
\right]
>0.
}
\tag{4}
\]
Equivalently,
\[
\operatorname{Cov}(X^2,G^2)
=
\frac{2(n-1)(m-1)}m
\sum_{y=0}^{n-2}
\binom{n-2}{y}
\left(\frac1m\right)^y
\left(1-\frac1m\right)^{n-2-y}
\Delta^2f(y).
\tag{5}
\]
For fixed \(m\),
\[
\boxed{
\operatorname{Cov}(X^2,G^2)\longrightarrow2(m-1)
\qquad(n\to\infty).
}
\tag{6}
\]
The limiting value is the variance of the common \(\chi^2_{m-1}\) limit, while (4) supplies the exact finite-sample coupling.

## Assumptions and scope
The null distribution is the equiprobable multinomial law. Formula (1) is exact for every real-valued cell score on the finite count set; no smoothness or asymptotics are required.

The power-divergence sign conclusion is stated for \(\lambda>-1\). This is the range in which \(N_i^{\lambda+1}\) is finite at an empty cell under the convention used above. The modified log-likelihood statistic at \(\lambda=-1\) can diverge when a cell is empty and is not part of the claim.

The result concerns covariance, not positive association, stochastic ordering, or monotone likelihood ratio between the statistics.

## Proof
Let \(Z_1,\ldots,Z_n\) be the underlying independent uniform cell labels and define the collision count
\[
C=\sum_{1\le a<b\le n}\mathbf1\{Z_a=Z_b\}.
\]
Since
\[
\sum_{i=1}^mN_i^2=n+2C,
\]
Pearson's statistic has the exact representation
\[
X^2=m-n+\frac{2m}{n}C.
\tag{7}
\]
Consequently,
\[
\operatorname{Cov}(X^2,T_h)
=
\frac{2m}{n}\operatorname{Cov}(C,T_h).
\tag{8}
\]

Write
\[
I=\mathbf1\{Z_1=Z_2\}.
\]
Exchangeability of the observation pairs gives
\[
\operatorname{Cov}(C,T_h)
=
\binom n2\operatorname{Cov}(I,T_h).
\tag{9}
\]
Now condition on whether the first two observations coincide. The remaining \(n-2\) observations are still independent uniform labels.

On \(I=1\), the common cell has occupancy \(Y+2\), while each of the other cells has the same marginal distribution as \(Y\). Linearity of expectation therefore gives
\[
\mathbb E[T_h\mid I=1]
=
\mathbb E[h(Y+2)+(m-1)h(Y)].
\tag{10}
\]
On \(I=0\), the first two observations occupy two distinct cells, so
\[
\mathbb E[T_h\mid I=0]
=
\mathbb E[2h(Y+1)+(m-2)h(Y)].
\tag{11}
\]
Subtracting gives
\[
\mathbb E[T_h\mid I=1]-\mathbb E[T_h\mid I=0]
=
\mathbb E[\Delta^2h(Y)].
\tag{12}
\]
Because
\[
\mathbb P(I=1)=\frac1m,
\]
we have
\[
\operatorname{Cov}(I,T_h)
=
\frac1m\left(1-\frac1m\right)
\mathbb E[\Delta^2h(Y)].
\tag{13}
\]
Combining (8), (9), and (13) proves (1).

For \(\lambda\ne0\), constants in (2) do not affect covariance, and
\[
D_\lambda
=
\frac{2(m/n)^\lambda}{\lambda(\lambda+1)}
\sum_{i=1}^mN_i^{\lambda+1}
+
\text{constant}.
\tag{14}
\]
If \(\lambda>0\), the function \(k\mapsto k^{\lambda+1}\) is strictly convex and the prefactor in (14) is positive. If \(-1<\lambda<0\), the same function is strictly concave and the prefactor is negative. Formula (1) therefore gives strict positivity in both cases.

At \(\lambda=0\), constants again disappear and
\[
G^2=2\sum_{i=1}^m f(N_i)+\text{constant}.
\]
The function \(f(k)=k\log k\) is strictly discretely convex, which proves (4). More explicitly,
\[
\Delta^2f(y)
=
\int_0^1\int_0^1\frac{ds\,dt}{y+s+t}>0,
\tag{15}
\]
where the integral is finite also for \(y=0\). This also makes the finite positivity transparent.

For fixed \(m\), the binomial variable satisfies \(Y/n\to1/m\) in probability. From (15),
\[
n\Delta^2f(Y)\longrightarrow m
\]
in probability. On \(Y\ge n/(2m)\), the quantity is uniformly bounded; on the complementary event, a binomial Chernoff bound together with the global bound \(0<\Delta^2f(y)\le2\log2\) makes the expectation contribution vanish. Hence
\[
n\mathbb E[\Delta^2f(Y)]\longrightarrow m,
\]
and (6) follows from (4).

As a consistency check, choose \(h(k)=k^2\). Then \(\Delta^2h\equiv2\), and (1), together with (7), gives the exact familiar variance
\[
\operatorname{Var}(X^2)
=
\frac{2(m-1)(n-1)}n.
\]

## Verification
The accompanying checker enumerates every multinomial count vector for \(2\le m\le7\) and \(2\le n\le9\), weights each vector by its exact multinomial multiplicity, and compares the directly computed Pearson--likelihood-ratio covariance with formula (4). It separately checks formula (1) with the quadratic cell score and verifies that this recovers the exact finite Pearson variance.

The checker also evaluates seven nonzero power-divergence parameters on a grid of small \((m,n)\) values and confirms the covariance formula and strict sign. Finally it evaluates (4) at \(n=5000\) for four values of \(m\) as a numerical check on (6). These finite computations supplement the symbolic proof and are not used to infer the all-parameter statements.

## Relationship to prior work
Cressie and Read introduced the power-divergence family and identified Pearson's statistic and the log-likelihood-ratio statistic as special parameter values. Their published summary says that the principal analytic focus is the asymptotic difference between members of the family, with finite-sample results supplied as checks and supplements.

Marhuenda, Marhuenda, and Morales later gave exact algorithms for the equiprobable multinomial model. Their public paper computes exact marginal distributions, critical values, and power comparisons for several power-divergence statistics, including Pearson and log likelihood. The inspected introduction, exact-distribution sections, exact-power section, and tables do not state a joint covariance; full-text searches for covariance, correlation, and joint terminology returned no matching result. Exact marginal distributions alone do not determine the covariance between two statistics evaluated on the same count vector.

The present result instead gives a closed finite mixed-moment identity for Pearson's statistic against every additive cell score. The positivity across the entire finite power-divergence range \(\lambda>-1\) is a direct structural consequence of that identity, not a simulation or an asymptotic comparison.

## Limitations
The simple binomial curvature reduction uses equal cell probabilities. For a nonuniform multinomial null, Pearson's statistic is a weighted quadratic form and pair collisions no longer enter with one common coefficient, so formula (1) does not transfer unchanged.

The foundational 1984 power-divergence article could not be fully inspected from a stable public full-text endpoint in this review. Its accessible summary and first-page material do not expose the covariance identity, but an equivalent formula elsewhere in that article or in older categorical-data literature remains the principal originality risk.

The theorem gives second-order dependence only. Strictly positive covariance does not imply that two power-divergence statistics rank every sample in the same way or have identical finite-sample rejection regions.

## References
1. N. Cressie and T. R. C. Read, “Multinomial Goodness-Of-Fit Tests,” *Journal of the Royal Statistical Society: Series B (Methodological)* 46 (1984), 440–464. DOI: 10.1111/j.2517-6161.1984.tb01318.x.
2. N. Cressie and T. R. C. Read, “Pearson's \(X^2\) and the Loglikelihood Ratio Statistic \(G^2\): A Comparative Review,” *International Statistical Review* 57 (1989), 19–43. DOI: 10.2307/1403582.
3. M. A. Marhuenda, Y. Marhuenda, and D. Morales, “On the Computation of the Exact Distribution of Power Divergence Test Statistics,” *Kybernetika* 39 (2003), 55–74. DML-CZ identifier: 135508.
4. B. Jann, “Multinomial Goodness-of-Fit: Large-Sample Tests with Survey Design Correction and Exact Tests for Small Samples,” *The Stata Journal* 8 (2008), 147–169. DOI: 10.1177/1536867X0800800201.
