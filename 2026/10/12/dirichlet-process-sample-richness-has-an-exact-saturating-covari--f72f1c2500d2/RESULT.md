# Dirichlet-process sample richness has an exact saturating covariance with latent Shannon entropy

## Finding

Let
\[
P=(P_i)_{i\ge1}\sim\operatorname{PD}(0,\theta),\qquad \theta>0,
\]
and, conditionally on \(P\), let \(X_1,\ldots,X_n\) be iid draws from \(P\). Let
\[
K_n=\#\{X_1,\ldots,X_n\}
\]
be the number of distinct observed species, and let
\[
H(P)=-\sum_{i\ge1}P_i\log P_i
\]
be the Shannon entropy of the latent random frequencies.

For every integer \(n\ge1\),
\[
\boxed{
\operatorname{Cov}(K_n,H(P))
=
\theta\left[
\sum_{k=1}^{n-1}\frac1{(\theta+k)^2}
-
\frac1{\theta+n}\sum_{k=1}^{n-1}\frac1{\theta+k}
\right].
}
\tag{1}
\]

Equivalently,
\[
\boxed{
\operatorname{Cov}(K_n,H(P))
=
\theta\left[
\psi_1(\theta+1)-\psi_1(\theta+n)
-
\frac{\psi(\theta+n)-\psi(\theta+1)}{\theta+n}
\right].
}
\tag{2}
\]

The covariance is \(0\) at \(n=1\). For every \(n\ge1\),
\[
\boxed{
\operatorname{Cov}(K_{n+1},H)-\operatorname{Cov}(K_n,H)
=
\frac{\theta}{(\theta+n)(\theta+n+1)}
\sum_{j=1}^{n}\frac1{\theta+j}>0.
}
\tag{3}
\]

Thus the covariance is strictly positive for every \(n\ge2\), increases with sample size, and saturates:
\[
\boxed{
\operatorname{Cov}(K_n,H)\uparrow\theta\psi_1(\theta+1).
}
\tag{4}
\]

The Dirichlet-process cluster count satisfies
\[
\operatorname{Var}(K_n)\sim\theta\log n.
\]
With
\[
V_H=
\frac{\theta}{(\theta+1)^2}
+\frac{\psi_1(2)}{\theta+1}
-\psi_1(\theta+2),
\tag{5}
\]
the standard Dirichlet-process Shannon-entropy variance, one further obtains
\[
\boxed{
\sqrt{\log n}\,
\operatorname{Corr}(K_n,H)
\longrightarrow
\frac{\sqrt{\theta}\,\psi_1(\theta+1)}{\sqrt{V_H}}.
}
\tag{6}
\]

Hence continued sampling creates ever more richness variation, but the raw covariance that richness carries about latent Shannon entropy approaches a finite ceiling.

## Assumptions and scope

The frequencies follow the one-parameter Poisson--Dirichlet law \(\operatorname{PD}(0,\theta)\), equivalently the ranked atom weights of a Dirichlet process with nonatomic base distribution and concentration parameter \(\theta\). The sample is conditionally iid from those frequencies.

The covariance is under the joint prior-predictive law of \(P\) and the sample. It is not a posterior covariance conditioned on a realized sample, and it is not the entropy of the empirical frequency vector.

No positive-discount \(\operatorname{PD}(\alpha,\theta)\) extension is claimed.

## Proof

Let
\[
I_{n+1}=\mathbf1\{X_{n+1}\notin\{X_1,\ldots,X_n\}\}.
\]
Then
\[
K_{n+1}=K_n+I_{n+1}.
\tag{7}
\]

Conditioning on \(P\), and averaging over the first \(n\) observations,
\[
\mathbb E[I_{n+1}\mid P]
=
\Delta_n(P)
=
\sum_{i\ge1}P_i(1-P_i)^n.
\tag{8}
\]
Since \(H(P)\) is measurable with respect to \(P\),
\[
\operatorname{Cov}(I_{n+1},H)
=
\operatorname{Cov}(\Delta_n(P),H).
\tag{9}
\]

For \(\operatorname{PD}(0,\theta)\), the first two size-biased frequencies have the GEM representation
\[
\widetilde P_1=V_1,\qquad
\widetilde P_2=(1-V_1)V_2,
\]
with independent
\[
V_1,V_2\sim\operatorname{Beta}(1,\theta).
\tag{10}
\]

A first size-biased pick gives
\[
\mathbb E\Delta_n(P)
=
\mathbb E(1-V_1)^n
=
\frac{\theta}{\theta+n}.
\tag{11}
\]

Split \(\mathbb E[\Delta_nH]\) into equal-species and distinct-species terms. The equal-species part is
\[
A_n=
\mathbb E[-V_1\log V_1(1-V_1)^n]
=
\frac{\theta}{(\theta+n)(\theta+n+1)}
[\psi(\theta+n+2)-\psi(2)].
\tag{12}
\]

Sequential size-biased sampling gives the distinct-species part
\[
B_n=
\mathbb E[(1-\widetilde P_1)^{n+1}(-\log\widetilde P_2)].
\]
Using (10) and beta differentiation,
\[
B_n=
\frac{\theta}{(\theta+n+1)^2}
+
\frac{\theta}{\theta+n+1}
[\psi(\theta+1)-\psi(1)].
\tag{13}
\]

Also
\[
\mathbb EH=\psi(\theta+1)-\psi(1).
\tag{14}
\]
Subtracting \(\mathbb E\Delta_n\,\mathbb EH\) from \(A_n+B_n\), and using the digamma recurrence, yields
\[
\operatorname{Cov}(\Delta_n,H)
=
\frac{\theta}{(\theta+n)(\theta+n+1)}
[\psi(\theta+n+1)-\psi(\theta+1)].
\]
Therefore
\[
\operatorname{Cov}(\Delta_n,H)
=
\frac{\theta}{(\theta+n)(\theta+n+1)}
\sum_{j=1}^{n}\frac1{\theta+j},
\tag{15}
\]
which proves the positive increment (3).

Since \(K_1=1\) is constant, telescoping (15) gives
\[
\operatorname{Cov}(K_n,H)
=
\theta\sum_{k=1}^{n-1}
\frac{A_k^\star}{(\theta+k)(\theta+k+1)},
\quad
A_k^\star=\sum_{j=1}^{k}\frac1{\theta+j}.
\tag{16}
\]
With
\[
b_k=\frac1{\theta+k},
\]
we have
\[
\frac1{(\theta+k)(\theta+k+1)}=b_k-b_{k+1}.
\]
Summation by parts gives
\[
\sum_{k=1}^{n-1}A_k^\star(b_k-b_{k+1})
=
\sum_{k=1}^{n-1}b_k^2-A_{n-1}^\star b_n,
\]
which is exactly (1). Digamma and trigamma finite-difference identities give (2).

The second term in (1) is \(O((\log n)/n)\), while the square sum tends to \(\psi_1(\theta+1)\), proving (4).

For the final statement, the Dirichlet-process new-table indicators are independent Bernoulli variables with success probabilities
\[
\frac{\theta}{\theta+j-1}.
\]
Hence
\[
\operatorname{Var}(K_n)
=
\sum_{j=1}^{n}
\frac{\theta}{\theta+j-1}
\left(1-\frac{\theta}{\theta+j-1}\right)
\sim\theta\log n.
\tag{17}
\]
Combining (4), (5), and (17) proves (6).

## Verification

The accompanying checker evaluates the mixed discovery-entropy increment in two independent deterministic ways. One route uses the beta-integral formulas (12)--(13); the second evaluates the closed digamma expression in (15).

Across a grid of concentration parameters and sample sizes, the checker requires these two routes to agree. It then cumulatively sums the increments and compares them with both the finite-sum covariance (1) and trigamma covariance (2), checks strict monotonicity, and verifies the finite saturation level.

It also evaluates the exact cluster-count variance through digamma and trigamma sums and checks the \(\sqrt{\log n}\)-scaled correlation limit at very large symbolic sample sizes.

The computations are supplementary. The all-\(n\), all-\(\theta>0\) theorem is the analytic beta-integral and telescoping argument above.

## Relationship to prior work

Cerquetti develops prior and posterior diversity moments under Gnedin--Pitman priors. In the Poisson--Dirichlet specialization, the paper supplies explicit Shannon-entropy moments and species-sampling structure, but the inspected full text does not state a covariance between the sample number of observed species and latent Shannon entropy.

Archer, Park, and Pillow derive Shannon-entropy moments for Dirichlet and Pitman--Yor priors using size-biased stick breaking. Their posterior entropy formulas explicitly involve the number \(K\) of unique observed symbols, but the inspected full article does not state the unconditional covariance of \(K_n\) with latent entropy or the saturation law (4).

Chao, Wang, and Jost show a close relationship between fixed-population Shannon entropy and the species accumulation curve through successive expected discovery probabilities. That identity motivates the discovery-increment route, but the abundance vector there is fixed rather than random under a Dirichlet-process prior.

The present theorem is therefore a joint prior-predictive statement: observed richness becomes increasingly positively aligned with latent entropy, while the raw covariance approaches a finite ceiling even though richness variance diverges.

## Limitations

The theorem is restricted to zero Pitman--Yor discount. Positive discount changes both the discovery mechanism and the asymptotic scale of \(K_n\).

The covariance is prior-predictive, not posterior conditional on an observed frequency table.

Negative or positive dependence beyond second moments is not claimed.

The species-sampling literature is extensive. Although the closest full sources were inspected and targeted searches found no explicit equivalent, an older source could contain the same identity under cluster-count, richness, or entropy-estimation terminology.

## References

1. A. Cerquetti, “Bayesian nonparametric estimation of Tsallis diversity indices under Gnedin--Pitman priors,” arXiv:1404.3441, first public version 2014-04-14.
2. E. Archer, I. M. Park, and J. W. Pillow, “Bayesian Entropy Estimation for Countable Discrete Distributions,” *Journal of Machine Learning Research* 15 (2014), 2833–2868; arXiv:1302.0328, first public version 2013-02-02.
3. A. Chao, Y. T. Wang, and L. Jost, “Entropy and the species accumulation curve: a novel entropy estimator via discovery rates of new species,” *Methods in Ecology and Evolution* 4 (2013), 1091–1100, first published 2013-08-19.
4. J. Pitman, *Combinatorial Stochastic Processes*, Lecture Notes in Mathematics 1875, Springer, 2006.
