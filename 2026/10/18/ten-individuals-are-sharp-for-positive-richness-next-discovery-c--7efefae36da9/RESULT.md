# Ten individuals are sharp for positive richness–next-discovery covariance in finite rarefaction

## Finding

Let a population consist of \(N\) labeled individuals, divided among \(S\geq 1\) species with positive integer abundances \(a_1,\ldots,a_S\), and sample in uniformly random order **without replacement**. After \(m\) draws, let \(K_m\) be the number of distinct species observed, and let \(D_{m+1}=K_{m+1}-K_m\in\{0,1\}\) indicate a novel species on the next draw. For every population with \(N\leq9\) and each \(1\leq m<N\),
\[
\operatorname{Cov}(K_m,D_{m+1})\leq0.
\]
The threshold is sharp: at \(N=10\), the abundance profile \((4,1,1,1,1,1,1)\) has
\[
\operatorname{Cov}(K_2,D_3)=\frac1{450}>0,
\qquad
\operatorname{Cov}(K_9,D_{10})=-\frac6{25}<0.
\]
More generally, for every integer \(s\geq6\), the profile \((4,1,\ldots,1)\) with \(s\) singleton species (\(N=s+4\)) has strictly positive covariance at \(m=2\) and strictly negative covariance at \(m=N-1\). Thus arbitrarily large finite populations exhibit an opposite-sign association between current richness and imminent discovery at different sampling depths.

## Assumptions and scope

All \(N\) individuals are distinct sampling units; each has one fixed known species identity. A uniformly random permutation of the individuals is sampled sequentially, without replacement and with perfect identification. Covariances are unconditional under this sampling law. No iid replacement, Bayesian prior, imperfect observation, unknown abundance, or extrapolation assumption is used. At \(m=N\), a next draw is undefined and is excluded. The case \(N=1\) has no legal sample depth and satisfies the universal statement vacuously.

## Proof

For a fixed draw depth \(m<N\), define
\[
q_m(u)=\begin{cases}\displaystyle\frac{\binom{N-u}{m}}{\binom Nm},&N-u\geq m,\\0,&N-u<m.\end{cases}
\]
This is the chance of avoiding a specified population subset of \(u\) individuals. Let \(Z_i\) indicate that species \(i\) has not yet appeared. Then
\[
K_m=S-\sum_i Z_i,
\qquad
U_m=\frac1{N-m}\sum_i a_i Z_i,
\]
where \(U_m=\Pr(D_{m+1}=1\mid\text{first }m\text{ draws})\). Hence \(\operatorname{Cov}(K_m,D_{m+1})=\operatorname{Cov}(K_m,U_m)\). Since \(\mathbb E[Z_i]=q_m(a_i)\) and \(\mathbb E[Z_iZ_j]=q_m(a_i+a_j)\) for distinct species, expansion yields the exact identity
\[
\boxed{\operatorname{Cov}(K_m,D_{m+1})=
\frac{\left(\sum_i a_iq_m(a_i)\right)\left(\sum_jq_m(a_j)-1\right)
-\sum_{i\ne j}a_iq_m(a_i+a_j)}{N-m}.}
\tag{1}
\]
All terms in (1) are rational numbers, so sign decisions are exact.

To establish the lower population bound, enumerate positive nondecreasing integer sequences whose sum is each \(N=2,\ldots,9\); these are exactly the abundance profiles up to species relabeling. Evaluate (1) for every integer \(1\leq m<N\). The complete finite certificate is reproduced by the standalone `verify.py`: 590 profile-depth pairs (2, 6, 15, 28, 55, 90, 154, 240 for \(N=2,\ldots,9\)), and each computed covariance is nonpositive. This is an exhaustive finite proof rather than an inference from randomly selected trials. As a logically independent check, the verifier enumerates all size-\(m\) subsets of individually labeled populations, directly computes \(K_m\) and the conditional probability of a novel next draw, and agrees exactly with (1) on every one of the 590 pairs.

For a general profile with one species of abundance \(t\geq2\) and \(s\) singleton species, write \(N=t+s\). At \(m=2\), observed richness is one exactly when both draws come from the abundant species. This event has probability \(t(t-1)/[N(N-1)]\). Its conditional next-discovery probability is \(s/(N-2)\). Conditional on two distinct species, the next-discovery probability is
\[
\frac{(s-1)(2t+N-2)}{(N-2)(2t+s-1)}.
\]
Their difference has the sign of \(t(s-3)-2(s-1)\), giving the exact factorization
\[
\boxed{\operatorname{Cov}(K_2,D_3)=
\frac{t(t-1)s\,[t(s-3)-2(s-1)]}{N^2(N-1)^2(N-2)}.}
\tag{2}
\]
When \(t=4\), this is positive precisely for integers \(s\geq6\); the smallest such population has \(N=10\), and (2) reduces to \(1/450\) at \(s=6\). The full ten-individual exhaustive comparison finds two positive profiles up to relabeling: \((4,1^6)\) with covariance \(1/450\), and \((5,1^5)\) with covariance \(1/324\), both only at depth \(m=2\). These assertions are also checked by exhaustive labeled-subset enumeration.

At \(m=N-1\), the unobserved last individual is a singleton with probability \(s/N\), in which case \(K_{N-1}=s\) and \(D_N=1\). Otherwise it belongs to the abundant species, with probability \(t/N\), in which case \(K_{N-1}=s+1\) and \(D_N=0\). Consequently,
\[
\boxed{\operatorname{Cov}(K_{N-1},D_N)=-\frac{ts}{N^2}<0.}
\tag{3}
\]
Equations (2) and (3) prove the unbounded-family assertion for all integers \(s\geq6\), not merely for the finitely verified range.

## Verification

Run `python verify.py` in the directory containing the two supplied files. The standard-library verifier requires no downloaded dependencies. Its output should equal `CERTIFICATE.json`. It checks (1) against direct labeled-subset enumeration for every abundance partition and depth through \(N=10\); independently checks the closed family formula for a finite parameter grid; and checks the explicitly claimed sign reversal and full covariance sequence for the smallest witness. Exact arithmetic uses `fractions.Fraction`, and the finite completeness relies on the included recursive integer-partition generator. The infinite-family claims are justified by (2) and (3), not by numerical extrapolation.

## Relationship to prior work

The classical species-discovery literature studies missing species, sample coverage and expected accumulation, notably Good and Toulmin (1956) and Heck, van Belle and Simberloff (1975). Chao and coauthors (2012) analyze coverage-based rarefaction, and Chiu (2023) treats estimation under sampling without replacement. A related published mathematical record, *Exact missing-mass covariance identity and sign reversal for successive species discoveries* (2026), treats covariance between **two successive discovery indicators** in an iid model. That differs from the present covariance between **cumulative observed richness** and the **next discovery** under finite sampling without replacement. The available inspected material does not give the sharp \(N=10\) cutoff or the opposite-sign finite-family construction. Bibliographic coverage is not asserted to be exhaustive.

## Limitations

The sign is a statistical feature of a fully specified random sampling design, not evidence of ecological facilitation or causation. No assertion is made for sampling with replacement, imperfect detection or clustered sampling. Only the existence of a sign change is proved for the unbounded family; no uniqueness of its sign switch is claimed. The exhaustive small-population certificate does not prove any theorem about an infinite class beyond the separate symbolic identities. A related historical source and a closely related published mathematical record were not fully accessible, leaving a residual bibliographic risk. Independent expert review has not been performed.

## References

- Good, I. J. and Toulmin, G. H. (1956), *The number of new species, and the increase in population coverage, when a sample is increased*, Biometrika **43**, 45–63, doi:10.1093/biomet/43.1-2.45 (published 1956-06-01).
- Heck, K. L., van Belle, G. and Simberloff, D. (1975), *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*, Ecology **56**, 1459–1461, doi:10.2307/1934716.
- Chao, A. et al. (2012), *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size*, Ecology **93**, 2533–2547, doi:10.1890/11-1952.1.
- Chiu, C.-H. (2023), *A species richness estimator for sample-based incidence data sampled without replacement*, Methods in Ecology and Evolution **14**, 2482–2493, doi:10.1111/2041-210X.14146.
- *Exact missing-mass covariance identity and sign reversal for successive species discoveries* (2026), publicly indexed mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-successive-species-discovery-covariance-missing-mass--4b975bda1dac.
