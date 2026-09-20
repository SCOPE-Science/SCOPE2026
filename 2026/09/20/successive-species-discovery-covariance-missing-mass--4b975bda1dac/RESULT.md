# Exact missing-mass covariance identity and sign reversal for successive species discoveries

## Setting

Let \(X_1,X_2,\ldots\) be iid draws from an arbitrary countable probability mass function \(p=(p_i)\). Define the discovery indicator
\[
D_{n+1}=\mathbf 1\{X_{n+1}\notin\{X_1,\ldots,X_n\}\},\qquad n\ge1.
\]
Write \(N_i(n)\) for the number of occurrences of species \(i\) among the first \(n\) draws, and define the random missing mass and squared missing mass
\[
M_n=\sum_i p_i\mathbf 1\{N_i(n)=0\},\qquad
Q_n=\sum_i p_i^2\mathbf 1\{N_i(n)=0\}.
\]
Also set
\[
m_n=\mathbb E M_n=\sum_i p_i(1-p_i)^n.
\]
Thus \(m_n=\Pr(D_{n+1}=1)\) is the unconditional discovery probability at the next draw.

## Main identity

For every countable species law and every \(n\ge1\),
\[
\boxed{\operatorname{Cov}(D_{n+1},D_{n+2})
=\operatorname{Var}(M_n)-(m_n-m_{n+1})(1-m_n).}
\]
Equivalently, because
\[
m_n-m_{n+1}=\sum_i p_i^2(1-p_i)^n=\mathbb E Q_n,
\]
the covariance is exactly "missing-mass heterogeneity minus one-step depletion."

### Proof

Condition on \(\mathcal F_n=\sigma(X_1,\ldots,X_n)\). The first future draw is a discovery with probability \(M_n\). Both next draws are discoveries precisely when they hit two distinct species that are both unseen at time \(n\). Hence
\[
\Pr(D_{n+1}=D_{n+2}=1\mid\mathcal F_n)
=\sum_{i\ne j}p_i p_j\mathbf 1\{N_i(n)=N_j(n)=0\}
=M_n^2-Q_n.
\]
Taking expectations gives
\[
\Pr(D_{n+1}=D_{n+2}=1)=\mathbb E M_n^2-\mathbb E Q_n.
\]
Since \(\Pr(D_{n+1}=1)=m_n\), \(\Pr(D_{n+2}=1)=m_{n+1}\), and \(\mathbb E Q_n=m_n-m_{n+1}\), subtracting \(m_nm_{n+1}\) yields the claimed identity.

A direct nonconditional form is
\[
\Pr(D_{n+1}=D_{n+2}=1)
=\sum_{i\ne j}p_i p_j(1-p_i-p_j)^n.
\]

## Consequence: the sign is not universal

The identity gives the exact criterion
\[
\operatorname{Cov}(D_{n+1},D_{n+2})>0
\iff
\operatorname{Var}(M_n)>(1-m_n)(m_n-m_{n+1}).
\]
Thus the decreasing mean discovery probability \(m_{n+1}\le m_n\) does not imply negative dependence between successive realized discoveries.

### Negative covariance: uniform species

For the uniform law on \(K\ge2\) species,
\[
m_n=(1-1/K)^n
\]
and
\[
\Pr(D_{n+1}=D_{n+2}=1)
=(1-1/K)(1-2/K)^n.
\]
Therefore
\[
\boxed{
\operatorname{Cov}(D_{n+1},D_{n+2})
=(1-1/K)\left[(1-2/K)^n-(1-1/K)^{2n}\right]<0.
}
\]
The strict inequality follows from \(1-2/K<(1-1/K)^2\).

### Positive covariance: one common species plus many rare species

Fix \(0<a<1\). For integer \(K\ge2\), take one species of mass \(1-a\) and \(K\) species each of mass \(a/K\). Then
\[
m_{n,K}=(1-a)a^n+a(1-a/K)^n
\]
and
\[
J_{n,K}:=\Pr(D_{n+1}=D_{n+2}=1)
=2(1-a)a^{n+1}(1-1/K)^n
+a^2(1-1/K)(1-2a/K)^n.
\]
Consequently \(C_{n,K}=J_{n,K}-m_{n,K}m_{n+1,K}\), and
\[
\boxed{
\lim_{K\to\infty}C_{n,K}
=a^{n+1}(1-a)^2(1-a^n)>0.
}
\]
It follows that for every fixed \(n\ge1\) there are finite iid species laws with positive covariance. Combined with the uniform example, both signs occur for every \(n\ge1\).

The limit has a simple interpretation: a single atom of mass \(1-a\) plus diffuse mass \(a\), where every diffuse draw is almost surely a previously unseen label. The finite equal-rare family above shows that no diffuse component is needed for the sign-reversal statement.

## A sharp calculation inside the one-atom/diffuse-tail family

In the diffuse-tail limit the covariance is
\[
f_n(a)=a^{n+1}(1-a)^2(1-a^n),\qquad 0<a<1.
\]
Its logarithm is strictly concave:
\[
\frac{d^2}{da^2}\log f_n(a)
=-\frac{n+1}{a^2}-\frac{2}{(1-a)^2}
-n\left[\frac{(n-1)a^{n-2}}{1-a^n}+\frac{n a^{2n-2}}{(1-a^n)^2}\right]<0.
\]
Hence this family has a unique maximizer \(a_n^*\), characterized by
\[
\frac{n+1}{a}-\frac{2}{1-a}-\frac{n a^{n-1}}{1-a^n}=0.
\]
Writing \(a=1-c/n\),
\[
n^2 f_n(1-c/n)\longrightarrow h(c)=c^2e^{-c}(1-e^{-c}).
\]
The unique maximizer \(c_*\) of \(h\) solves
\[
\frac{2}{c}-1+\frac{1}{e^c-1}=0,
\]
with
\[
c_*=2.262810129196914\ldots,\qquad
h(c_*)=0.477364740089417\ldots.
\]
Thus, within this family,
\[
1-a_n^*\sim \frac{c_*}{n},
\qquad
\max_{0<a<1} f_n(a)\sim\frac{0.477364740089417}{n^2}.
\]
This is a family-specific optimum, not a claimed global maximum over all species laws.

## Relation to prior literature

Good and Toulmin (1956) study prediction of numbers of new species and population coverage under sample enlargement. Starr (1979), Clayton and Frees (1987), and later discovery-probability work focus on estimating the probability that future observations reveal new species. Ben-Hamou, Boucheron and Ohannessian (2017) establish concentration results for occupancy counts and missing mass. Chebunin and Zuyev (2022) prove functional central limit theorems for occupancy and missing-mass processes and provide process-level covariance functions under regular variation.

To the best of our knowledge, the exact adjacent-discovery identity above, its heterogeneity-versus-depletion sign criterion, and the fact that finite iid species laws realize both signs for every \(n\) have not been stated in the checked literature. The elementary nature of the identity creates a real residual risk that an equivalent formula appears in older occupancy, urn, or species-sampling literature under different terminology.

## Limitations

- The main theorem concerns two consecutive discovery indicators in iid sampling; it does not characterize longer-range dependence or higher-order joint laws.
- The positive construction proves existence and gives an explicit limiting mechanism, but no global extremum over all species laws is claimed.
- The diffuse-tail optimization is only for that one-parameter limiting family.
- Several older sources were identifiable only through abstracts or bibliographic records during the literature comparison; equivalent older formulations remain the main originality uncertainty.

## Reproducibility

`artifacts/verify_discovery_covariance.py` uses exact rational arithmetic to check the covariance identity on representative finite laws, the uniform negative family, and finite positive examples. It also independently recomputes the numerical constant in the diffuse-tail asymptotic. `artifacts/VERIFICATION.txt` records the verified output.

## References

1. Good, I. J. and Toulmin, G. H. (1956). *The Number of New Species, and the Increase in Population Coverage, When a Sample Is Increased*. Biometrika 43, 45–63. https://doi.org/10.1093/biomet/43.1-2.45
2. Starr, N. (1979). *Linear Estimation of the Probability of Discovering a New Species*. Annals of Statistics 7, 644–652. https://doi.org/10.1214/aos/1176344684
3. Clayton, M. K. and Frees, E. W. (1987). *Nonparametric Estimation of the Probability of Discovering a New Species*. Journal of the American Statistical Association 82, 305–311. https://doi.org/10.1080/01621459.1987.10478434
4. Ben-Hamou, A., Boucheron, S. and Ohannessian, M. I. (2017). *Concentration Inequalities in the Infinite Urn Scheme for Occupancy Counts and the Missing Mass, with Applications*. Bernoulli 23, 249–287. https://doi.org/10.3150/15-BEJ743
5. Chebunin, M. and Zuyev, S. (2022). *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*. Journal of Theoretical Probability 35, 1–19. https://doi.org/10.1007/s10959-020-01053-6
6. Skorski, M. (2021). *On Missing Mass Variance*. arXiv:2104.07028. https://arxiv.org/abs/2104.07028
