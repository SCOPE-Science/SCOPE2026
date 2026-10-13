# Exact richness–Simpson covariance under Pitman–Yor sampling
## Finding
Let \(\Pi_n\), \(n\ge2\), be the two-parameter Pitman–Yor exchangeable partition with
\[
0\le\alpha<1,
\qquad
\theta>-\alpha.
\]
Write \(K_n\) for its number of blocks. Define empirical pair homozygosity by
\[
Q_n
=
\frac{1}{(n)_2}
\sum_{B\in\Pi_n}(|B|)_2
=
\frac{1}{\binom n2}
\sum_{1\le i<j\le n}\mathbf 1\{i\sim j\},
\]
and empirical pair diversity by
\[
D_n=1-Q_n.
\]
Put
\[
R_n(\alpha,\theta)
=
\prod_{j=2}^{n-1}\frac{\theta+j+\alpha}{\theta+j},
\qquad R_2(\alpha,\theta)=1.
\]
Then
\[
\boxed{
\operatorname{Cov}(K_n,Q_n)
=
-\frac{(1-\alpha)(\theta+\alpha)}{(\theta+1)^2}R_n(\alpha,\theta)
}
\]
and therefore
\[
\boxed{
\operatorname{Cov}(K_n,D_n)
=
\frac{(1-\alpha)(\theta+\alpha)}{(\theta+1)^2}R_n(\alpha,\theta).
}
\]

A stronger conditional statement drives the covariance. For the first two labels,
\[
\boxed{
\mathbb E[K_n\mid1\not\sim2]
-
\mathbb E[K_n\mid1\sim2]
=
R_n(\alpha,\theta).
}
\]
More precisely, writing \(\mu_n=\mathbb E K_n\),
\[
\mathbb E[K_n\mid1\sim2]-\mu_n
=
-\frac{\theta+\alpha}{\theta+1}R_n(\alpha,\theta),
\]
while
\[
\mathbb E[K_n\mid1\not\sim2]-\mu_n
=
\frac{1-\alpha}{\theta+1}R_n(\alpha,\theta).
\]
Thus a single observed pair disagreement has an exact finite effect on expected richness, and exchangeability converts that local effect into the global richness–diversity covariance.

For the conventional sample homozygosity
\[
\widehat H_n
=
\sum_{B\in\Pi_n}\left(\frac{|B|}{n}\right)^2,
\]
one has
\[
\widehat H_n
=
\frac1n+\frac{n-1}{n}Q_n,
\]
so
\[
\boxed{
\operatorname{Cov}(K_n,\widehat H_n)
=
-\frac{n-1}{n}
\frac{(1-\alpha)(\theta+\alpha)}{(\theta+1)^2}
R_n(\alpha,\theta).
}
\]
The empirical Gini–Simpson diversity \(1-\widehat H_n\) has the opposite covariance.

In the Ewens/Dirichlet case \(\alpha=0\),
\[
R_n(0,\theta)=1
\]
for every \(n\), hence
\[
\boxed{
\operatorname{Cov}(K_n,D_n)=\frac{\theta}{(\theta+1)^2}
\quad\text{for every }n\ge2.
}
\]
For the uniform random-permutation cycle partition, corresponding to \(\theta=1\), this is exactly
\[
\operatorname{Cov}(K_n,D_n)=\frac14
\]
for every sample size \(n\ge2\).

For fixed \(0<\alpha<1\), gamma-function asymptotics give
\[
R_n(\alpha,\theta)
\sim
\frac{\Gamma(\theta+2)}{\Gamma(\theta+2+\alpha)}n^\alpha,
\]
so the unnormalized richness–pair-diversity covariance grows on the same power scale as Pitman–Yor richness.

## Assumptions and scope
The partition follows the standard two-parameter Pitman–Yor sampling rule. Given \(m\) observations in \(k\) blocks, a new observation joins a block of size \(s\) with probability
\[
\frac{s-\alpha}{\theta+m}
\]
and creates a new block with probability
\[
\frac{\theta+\alpha k}{\theta+m}.
\]
The admissible range used here is \(0\le\alpha<1\) and \(\theta>-\alpha\).

The statistic \(Q_n\) is the without-replacement probability that a uniformly chosen unordered pair of sample labels lies in the same block. The statistic \(\widehat H_n\) is the with-replacement squared-frequency homozygosity. Their deterministic affine relation is stated above, so no convention is hidden in the covariance conversion.

The finding concerns finite-sample dependence among statistics of the observed random partition. It is distinct from covariance statements for latent Poisson–Dirichlet functionals of the underlying random frequencies.

## Proof
Let
\[
A=\{1\sim2\}.
\]
The second customer in the Chinese-restaurant construction joins the first customer's block with probability
\[
\mathbb P(A)=\frac{1-\alpha}{\theta+1},
\]
and starts a new block with probability
\[
\mathbb P(A^c)=\frac{\theta+\alpha}{\theta+1}.
\]
Conditional on \(A\), the process at time two starts with one block; conditional on \(A^c\), it starts with two blocks.

For \(m\ge2\), let \(u_m^{(k)}\) be the expected number of blocks at time \(m\) for the same Pitman–Yor growth rule started at time two with \(k\in\{1,2\}\) blocks. Given a current block count \(K_m\), the conditional expected increment is
\[
\frac{\theta+\alpha K_m}{\theta+m}.
\]
Therefore
\[
u_{m+1}^{(k)}
=
\left(1+\frac{\alpha}{\theta+m}\right)u_m^{(k)}
+
\frac{\theta}{\theta+m}.
\]
Subtracting the recurrences for the two initial states eliminates the inhomogeneous term. Since
\[
u_2^{(2)}-u_2^{(1)}=1,
\]
we obtain
\[
u_n^{(2)}-u_n^{(1)}
=
\prod_{j=2}^{n-1}rac{\theta+j+\alpha}{\theta+j}
=
R_n(\alpha,\theta).
\]
Thus
\[
\mathbb E[K_n\mid A^c]-\mathbb E[K_n\mid A]=R_n.
\]

Let \(\mu_n=\mathbb E K_n\). For a two-component mixture whose conditional means differ by \(R_n\), elementary centering gives
\[
\mathbb E[K_n\mid A]-\mu_n
=
-\mathbb P(A^c)R_n
=
-\frac{\theta+\alpha}{\theta+1}R_n
\]
and
\[
\mathbb E[K_n\mid A^c]-\mu_n
=
\mathbb P(A)R_n
=
\frac{1-\alpha}{\theta+1}R_n.
\]
Consequently,
\[
\operatorname{Cov}(K_n,\mathbf1_A)
=
\mathbb P(A)
\left(
\mathbb E[K_n\mid A]-\mu_n
\right)
=
-\frac{(1-\alpha)(\theta+\alpha)}{(\theta+1)^2}R_n.
\]

By exchangeability, the same covariance holds for every pair indicator \(\mathbf1\{i\sim j\}\). Since \(Q_n\) is their average,
\[
\operatorname{Cov}(K_n,Q_n)
=
\operatorname{Cov}(K_n,\mathbf1_A),
\]
which proves the first formula. The formulas for \(D_n\) and \(\widehat H_n\) follow by deterministic affine transformations.

When \(\alpha=0\), every factor in \(R_n\) is one. For \(0<\alpha<1\), writing the product as a ratio of gamma functions gives
\[
R_n
=
\frac{\Gamma(\theta+n+\alpha)}{\Gamma(\theta+2+\alpha)}
\frac{\Gamma(\theta+2)}{\Gamma(\theta+n)},
\]
and the stated power asymptotic follows.

## Verification
The accompanying `checker.py` independently enumerates all set partitions through \(n=8\) using restricted-growth strings. For five rational parameter choices it assigns each partition its exact Pitman sampling-formula probability, computes \(K_n\), pair homozygosity, and sample homozygosity directly, and verifies the covariance and conditional-gap formulas with rational arithmetic.

The same checker replays the conditional-mean difference recurrence through \(n=500\) for several rational parameter pairs. These finite computations are consistency checks; the all-\(n\) result follows from the symbolic recurrence and exchangeability argument.

## Relationship to prior work
Pitman's exchangeable-partition paper gives the two-parameter sequential construction and exchangeable partition probability function that define the model used here. It does not state a homozygosity or Simpson-diversity covariance.

Yamato and Sibuya study moments of the Pitman sampling formula, especially moments of the number of components. Sibuya later develops restart and subsampling distributions and exact moment formulas for species counts. Those results provide broad finite-partition machinery, but the inspected full restart/subsampling paper contains no homozygosity, Simpson, or covariance statement, and the present pair-conditioned richness gap is not stated there.

For the Ewens special case, Tavaré reviews both \(K_n\), the number of observed types, and Watterson's sample homozygosity statistic \(\widehat H_n\). The classical testing framework conditions the allele-frequency configuration on \(K_n\); the exact unconditional covariance displayed here is a different finite-sample relation.

The finding therefore isolates a simple dependence law that is not visible from the marginal richness formulas alone: a pair mismatch shifts expected future richness by the multiplicative factor \(R_n\), and this local shift exactly determines the global richness–Simpson covariance.

## Limitations
The result assumes the standard two-parameter Pitman–Yor partition rule and the stated parameter range. Other Gibbs-type partitions need not have the affine block-count drift that makes the conditional difference close multiplicatively.

The result is a second-moment and conditional-mean identity. It does not assert stochastic monotonicity of the full conditional distribution of \(K_n\) given homozygosity, nor does it identify a complete joint law of \(K_n\) and \(Q_n\).

Older population-genetics literature may contain an equivalent mixed-moment identity under allele-count or homozygosity notation. The closest inaccessible primary source located during review was Watterson's classical homozygosity paper; its accessible record establishes relevance but was insufficient to rule out an unindexed equivalent formula in the full text.

## References
1. J. Pitman, “Exchangeable and partially exchangeable random partitions,” *Probability Theory and Related Fields* 102 (1995), 145–158. DOI: 10.1007/BF01213386.
2. H. Yamato and M. Sibuya, “Moments of some statistics of Pitman sampling formula,” *Bulletin of Informatics and Cybernetics* 32 (2000), 1–10. DOI: 10.5109/13490.
3. J. Pitman, *Combinatorial Stochastic Processes*, Berkeley Statistics Technical Report 621 (2002).
4. M. Sibuya, “Prediction in Ewens–Pitman sampling formula and random samples from number partitions,” *Annals of the Institute of Statistical Mathematics* 66 (2014), 833–864. DOI: 10.1007/s10463-013-0427-8.
5. S. Tavaré, “The magical Ewens sampling formula,” *Bulletin of the London Mathematical Society* 53 (2021), 1563–1582. DOI: 10.1112/blms.12537.
